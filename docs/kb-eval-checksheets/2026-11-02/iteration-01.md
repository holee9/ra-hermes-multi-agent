# KB Eval Checksheet - 2026-11-02 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261102-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_us-001", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "5bb35d299b07246a", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `5bb35d299b07246a`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 source excerpt transparency (no captured response — inferred only)을 기준으로 판정합니다.

**Agent Response** — capture failed (fail-safe: fast checks fall back to source-only inference)

> ⚠️ response capture error: timed out

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [x] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261102-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "562589e9d0b42dd0", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `562589e9d0b42dd0`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md)
- Source hash: `757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`는 `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분 ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR (21 CFR Part 820) Readiness Assessment**

---

### 1. Bottom‑Line Determination  
- **Device class & submission route:** The QMSR applies to every FDA‑regulated device regardless of classification. Assuming the product is a Class II medical device (the most common scenario for software‑enabled imaging or diagnostic accessories), the required pre‑market pathway will be a **510(k) Premarket Notification** (21 CFR Part 807).  
- **Key regulatory gap:** ISO 13485:2016 **§4.2.5 (record management)** alone is insufficient; FDA’s additional record‑keeping mandates in **21 CFR §820.35(a–d)** must be fully implemented and evidenced.

---

### 2. Required Evidence of QMSR Compliance  

| Requirement (FDA) | Supporting Standard / Section | Evidentiary Artifact |
|-------------------|--------------------------------|----------------------|
| **Record‑management system** – creation, maintenance, retrieval, retention, and protection of device‑related records | 21 CFR §820.35(a–d); ISO 13485 §4.2.5 (basic) | • Updated SOP‑DOC‑001 (adds §820.35(a–d) language)<br>• Controlled record‑control log demonstrating retention periods and archive locations |
| **UDI generation, labeling & GUDID submission** | 21 CFR Part 830 (UDI requirements); 21 CFR §820.35(c) (UDI record) | • SOP‑TRC‑001 / SOP‑UDI‑001 with UDI assignment procedures<br>• Proof of initial GUDID upload and any subsequent updates |
| **Service/field-maintenance documentation** – capture of six required service items for X‑ray field service | 21 CFR §820.35(b) (service records) | • SOP‑SVC‑001 (new 6‑item service record form)<br>• Sample completed forms from recent field visits |
| **Complaint handling & MDR decision tree** – triage, determination of reportable events, and generation of FDA Form 3500A when required | 21 CFR §803.50 & §803.53 (MDR triggers) | • SOP‑PMS‑001 with embedded MDR decision tree (30‑day/5‑work‑day thresholds)<br>• Log of complaints processed in the last quarter showing correct routing |
| **Electronic records & signatures** – separate Part 11 scope as indicated in SOP‑DOC‑001 | 21 CFR Part 11 (referenced but isolated) | • Evidence that any electronic record system is validated per Part 11 (validation plan, test reports) and referenced separately from §820.35 |
| **Internal audit & objective evidence** – inclusion of “objective evidence for external review” | ISO 13485 §4.2.5; SOP‑IA‑001 (audit report criteria) | • Recent internal audit reports with attached objective evidentiary artifacts (e.g., screenshots, logs) |

---

### 3. Missing / Incomplete Information  

| Gap | Impact | Action Needed |
|-----|--------|----------------|
| **Explicit mapping of each SOP to the specific sub‑clauses of §820.35** (a–d) | FDA may reject a 510(k) for incomplete QMS evidence | Create a compliance matrix linking SOP sections to each regulatory requirement |
| **Proof of GUDID submission and periodic update compliance** | Required under Part 830; absence is a non‑conformity | Submit GUDID records, retain acknowledgment receipts, schedule quarterly verification |
| **Demonstration that the “six service record items” meet all data elements stipulated in §820.35(b)** | Service documentation may be deemed inadequate | Provide a template with field definitions and sample completed records for at least three distinct service events |
| **Validation evidence for any electronic record system** (even if Part 11 is separated) | Part 11 still applies to electronic QMS records; lack of validation can trigger Form 483 | Compile system validation plan, test protocols, and final reports; archive in controlled location |
| **Documented risk management file** (ISO 14971:2019) supporting design‑control activities | Required for 510(k) design‑history file (DHF) | Generate a Risk Management Report covering hazard identification, risk analysis, controls, and residual risk evaluation |

---

### 4. Core Risk Controls (Design‑Control & QMS Integration)

| Control Area | Standard / Regulation | Implementation Summary |
|--------------|-----------------------|------------------------|
| **Design Input/Output & Verification** | 21 CFR §820.30; ISO 13485 §7.3 | Maintain design history file (DHF) with traceability matrices |
| **Risk Management** | ISO 14971:2019 (primary edition) | Conduct risk analysis early, document mitigations, tie controls to design outputs and QMS procedures |
| **Process Validation** | IEC 62304 (software); IEC 60601‑1 (if electrical) | Provide validation protocols/results for critical manufacturing/process steps |
| **Post‑market Surveillance** | 21 CFR §803; ISO 13485 §8.2.4 | Operate complaint handling system with MDR decision tree; generate periodic trend reports |
| **Change Management** | Predetermined Change Control Plan (PCCP) – FDA guidance Dec 2024 | Document anticipated software/firmware updates, include impact analysis in change plan |

---

### 5. Citations  

- **Regulatory framework:** 21 CFR Part 820 (QMSR); 21 CFR Part 830 (UDI); 21 CFR Part 803 §§803.50 & 803.53 (MDR triggers).  
- **ISO references:** ISO 13485:2016 §4.2.5 (record management); ISO 14971:2019 (risk management); IEC 62304 2006+A1:2015; IEC 60601‑1 2005+A1:2012+A2:2020.  
- **Source‑specific identifiers:** No device‑clearance numbers or other instance IDs appear in the supplied excerpts – “no specific identifier found in source — verify separately.”

---

### 6. Human‑Escalation Triggers  

| Condition | Who Escalates | Why |
|-----------|----------------|-----|
| Any SOP fails to reference **all** sub‑clauses of §820.35 (a–d) | QA Manager → RA Lead | Incomplete QMS evidence will block 510(k) acceptance. |
| Missing or outdated GUDID submission record | Regulatory Affairs → Senior Management | Non‑compliance with Part 830 can lead to Form 483. |
| Service records lack any of the six required data elements | Service Lead → QA Director | Violates §820.35(b); risk of FDA finding during inspection. |
| Complaint handling system does **not** generate MDR decision tree output within 30‑day (or 5‑work‑day) windows | RA Specialist → Compliance Officer | Failure to meet §§803.50/803.53 triggers mandatory reporting violations. |
| Electronic record system validation evidence cannot be produced on request | IT/QM Lead → Regulatory Affairs | Part 11 deficiency; may result in enforcement action. |
| Risk Management File incomplete or not linked to DHF | Design Engineer → RA Lead | Required for 510(k) design‑history file; gaps cause review delays. |

When any trigger occurs, the responsible functional owner must **immediately notify** the Regulatory Affairs lead and document the issue in the QMS non‑conformance log with a target corrective action date.

---

### 7. Peer Review Request  

> *“Colleague RA team members, please challenge: (1) the assumption that the product will follow a Class II 510(k) route without device‑specific classification data; (2) completeness of the SOP‑to‑§820.35 mapping; and (3) any jurisdictional gaps where EU/Korean references in source material might have been inadvertently carried into this US‑focused assessment.”*

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

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `130165779856845378`

> ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시 §820.35(a)(b)(c)(d) 추가요건" 절 신설, Part 11은 §820.35 외부로 별도 절 분리 | QA | 기록관리 절차에 불만/서비스/UDI/기밀성·Part 11 분리 기재 여부 | | SOP-PMS-001 | MDR 결정 트리(§803.50 30cd / §803.53 5wd 트리거 기준) + 미보고 사유 양식 첨부 | QA/RA | 불만 → MDR 판정 → 기록 흐름 완비 여부 | | SOP-TRC-001 / SOP-UDI-001 | UDI 기록관리 절 추가 — **§820.35(c)** + 21 CFR Part 830 | RA | GUDID 제출·갱신 기록 체계 구축 여부 | | SOP-SVC-001 (신설/갱신) | **§820.35(b)** 6항목 서비스 기록 양식 도입 | Service/QA | X-ray 출장정비 기록 6항목 완결성 | | SOP-IA-001 | 감사보고서 작성 기준에 "외부 열람 대비 객관적 증거 인용" 항목 추가 | QA | 보고서 품질 기준 갱신 여부 |

### kb-eval-20261102-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "67b2165dbb15685b", "source": "github:holee9/MD-process/03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md", "source_hash": "8ae673fb6f1587e4dc2d26f9f4b3680719f501c71d0ce6d5450609814a7d126e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `67b2165dbb15685b`
- Source: `github:holee9/MD-process/03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/03_%EC%84%A4%EA%B3%84_%EA%B0%9C%EB%B0%9C%EA%B4%80%EB%A6%AC/SOP-SBOM-001_SBOM_%EC%83%9D%EC%84%B1%EA%B4%80%EB%A6%AC_%EC%A0%88%EC%B0%A8.md)
- Source hash: `8ae673fb6f1587e4dc2d26f9f4b3680719f501c71d0ce6d5450609814a7d126e`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `SOP-SBOM-001_SBOM_생성관리_절차.md`는 `SOP-SBOM-001_SBOM_생성관리_절차.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ┌──┬──────────┬────────┬──────┬────────────┬──────┬──────┐ │# │구성요소 │CVE ID │CVSS │VEX 판정 │사유 │조치 │ │ │(PURL) │ │Score │ │ │기한 │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │1 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │2 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ └──┴────...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR / Design‑Control Readiness**

---

### 1. Bottom‑line recommendation  
- **Presumed device class:** Class II (most software‑enabled medical devices) → **510(k) pre‑market notification** is the fastest, FDA‑recognised route.  
- **Core regulatory gap:** No documented SBOM / VEX / VDR evidence that meets the new FDA Quality Management System Regulation (QMSR) requirements (effective 2 Feb 2026).  

Proceed with a 510(k) submission *only after* establishing a compliant SBOM program and evidencing traceability, electronic signatures and audit‑ready “Cybersecurity File” as outlined below.

---

### 2. Classification / Submission pathway  

| Aspect | Determination |
|--------|---------------|
| **Product panel** | Not specified in source; assuming a device with software (e.g., imaging or diagnostic) → likely falls under **21 CFR Part 892** (if imaging) or **Part 862/820** for other categories. |
| **Device class** | Class II (most software‑enabled devices). |
| **Regulatory route** | **510(k) – Substantial equivalence**. No de Novo justification required unless the device is truly novel. |
| **Key FDA citations** | • 21 CFR §807 (premarket notification) <br>• 21 CFR Part 820 (QMS) – especially §820.35 (Document control) <br>• QMSR (effective 2‑Feb‑2026) – incorporated by reference into Part 820. |

*If the device is a Class III or high‑risk system, a PMA would be required; this cannot be confirmed from the source.*

---

### 3. Required evidence for QMSR compliance  

| Item | Evidence to provide (minimum) |
|------|--------------------------------|
| **SBOM record** | Full Software Bill of Materials stored in the “Cybersecurity File” within the Master Device File (MDF). Must satisfy ISO 13485:2016 §4.2.5 (record‑keeping). |
| **VEX / VDR linkage** | Versioned Vulnerability Exploit (VEX) and Vulnerability Disclosure Report (VDR) files linked to each SBOM entry; include CVE IDs, CVSS scores, fix status (N/A, Affected, Fixed, Under investigation). |
| **Change‑control traceability** | 1:1:1 mapping – Build ID ↔ SBOM ↔ VEX – demonstrated in a change‑log matrix. |
| **Electronic signature** | SBOM and associated files must carry an FDA‑acceptable electronic signature (21 CFR §820.100). |
| **Audit readiness** | Ability to present the complete Cybersecurity File within **2 hours** of FDA inspection request (per SOP step 5.8.3). |
| **Quarterly self‑audit report** | Documentation that a quarterly internal QMSR audit has been performed on SBOM updates, VEX rationale and patch timelines (step 5.8.4). |
| **Risk management** | ISO 14971:2019 risk analysis showing how identified software vulnerabilities are mitigated; cross‑referenced to the SBOM/VEX entries. |
| **Design‑control records** | Design History File (DHF) entries linking software requirements, verification/validation results and cybersecurity controls (per 21 CFR §820.30). |

*No specific instance identifiers (e.g., cleared 510(k) numbers) appear in the source – verify separately.*

---

### 4. Missing information that must be supplied before submission  

| Gap | Why it matters |
|-----|----------------|
| **Device description & intended use** | Required for predicate device comparison and labeling (§801). |
| **Predicate 510(k) reference** | Needed to claim substantial equivalence (21 CFR §807.92). |
| **UDI strategy** | Must comply with 21 CFR Part 830; source does not mention UDI generation. |
| **Labeling & IFU content** | Must include cybersecurity and SBOM statements per FDA guidance. |
| **Software risk management file (ISO 14971) reference number** | Needed to demonstrate compliance with risk controls. |
| **Electronic signature policy** | Evidence that signatures on SBOM files meet §820.100 requirements. |
| **Verification of QMSR “Cybersecurity File” location in MDF** | Physical/ electronic layout must be documented for inspection. |

---

### 5. Risk‑control considerations (FDA & ISO standards)  

1. **Identify software hazards** – Use ISO 14971:2019 hazard analysis, map each CVE to a risk level.  
2. **Implement mitigations** – Patch management, code signing, runtime integrity checks; document in VDR.  
3. **Control design changes** – Apply Predetermined Change Control Plan (PCCP) for AI/ML updates (FDA Guidance Dec 2024).  
4. **Document control** – Follow 21 CFR §820.35 and ISO 13485:2016 §4.2.5 for SBOM records, change logs and audit trails.  
5. **Monitoring & post‑market surveillance** – Establish a process to capture new vulnerabilities (e.g., via CVE feeds) and update the Cybersecurity File within the defined 1‑day window.

---

### 6. Citations  

| Reference type | Citation |
|----------------|----------|
| **Framework – regulation** | FDA Quality Management System Regulation (QMSR), effective 2 Feb 2026, incorporated into **21 CFR Part 820** (§820.35). |
| **Framework – ISO standard** | **ISO 13485:2016 §4.2.5** – Record‑keeping requirements. |
| **Framework – risk management** | **ISO 14971:2019** (risk management for medical devices). |
| **Framework – software life‑cycle** | **IEC 62304:2006+A1:2015** (software development processes). |
| **Source‑specific item** | No specific identifier found in source — verify separately (SBOM record, VEX table format, audit timeline). |

---

### 7. Human‑escalation triggers  

| Trigger condition | Escalation action |
|-------------------|-------------------|
| **Inability to produce the Cybersecurity File within 2 h** upon FDA request (step 5.8.3) | Notify RA Lead → initiate Contingency Plan; consider filing a Request for Additional Information (AI) with FDA. |
| **Quarterly self‑audit not completed or findings unresolved** (step 5.8.4) | Escalate to Quality Assurance Director and senior management; halt 510(k) submission until closure. |
| **SBOM missing CVE, CVSS, or fix status data** | Prompt Security Officer to complete VEX entries; if not resolved in 48 h, raise to Chief Compliance Officer. |
| **Electronic signature absent or non‑conforming** | Immediate mitigation by QA Manager; document deviation and submit a corrective action plan to FDA prior to filing. |
| **Any QMSR audit finding labelled “non‑compliant”** | Stop submission workflow; convene cross‑functional remediation team; report to the FDA as needed under 21 CFR §820.100‑§820.105. |

---

### 8. Peer‑review prompt  

> *Colleague, please review: (1) our assumption that the device will be Class II/510(k); (2) completeness of the SBOM/VEX evidence list against FDA QMSR guidance; and (3) any jurisdiction‑specific items we may have omitted (e.g., UDI generation, labeling requirements). Highlight gaps or alternative pathways you see.*

---

**End of draft.**

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

> ① VEX를 "Versioned Vulnerability Exploit"로 전개 — 정확히는 Vulnerability Exploitability eXchange ② 전자서명 근거를 "21 CFR §820.100"으로 인용 — 구 QSR §820.100=CAPA, 전자서명은 Part 11 ③ "§820.100-§820.105" 시정보고 근거도 동일 오류.

**Source Excerpts**

1. Chunk `1031175965966205535`

> ┌──┬──────────┬────────┬──────┬────────────┬──────┬──────┐ │# │구성요소 │CVE ID │CVSS │VEX 판정 │사유 │조치 │ │ │(PURL) │ │Score │ │ │기한 │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │1 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │2 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ └──┴──────────┴────────┴──────┴────────────┴──────┴──────┘ (N/A=not_affected, Aff=affected, Fix=fixed, Inv=under_investigation) 총 취약점: __건 Critical: __ High: __ Medium: __ Low: __ 변경관리 진입 건수: __건 (SOP-CC-001) 승인: Security Officer ___________ 일자: ____-__-__ ```

2. Chunk `1070786144928344628`

> ### 5.8 QMSR 실사 대응 — SBOM 기록 요구사항 (v0.3 신설) FDA QMSR(2026-02-02 시행)에 따라 SBOM 관련 기록은 ISO 13485:2016 §4.2.5 기록 관리 요구사항을 준수해야 한다. | 단계 | 수행자 | 활동 | 판정 기준 | |------|--------|------|-----------| | 5.8.1 | QA Manager | SBOM·VEX·VDR을 MDF 내 사이버보안 파일(Cybersecurity File)로 편입 | QMSR §820.35/ISO 13485 §4.2.5 준수 | | 5.8.2 | QA Manager | SBOM 변경 이력의 추적성 확보 — 빌드 ID↔SBOM↔VEX 삼중 연결 | 1:1:1 대응 확인 | | 5.8.3 | RA Lead | FDA 실사 시 SBOM 즉시 제시 가능 상태 유지 (전자 서명 포함) | 2시간 내 제출 가능 | | 5.8.4 | Security Officer | QMSR 감사 관점 자체 점검 — SBOM 갱신 이력, VEX 판정 근거, 패치 타임라인 문서화 | 분기 자체감사 완료 | **QMSR 실사 체크포인트:** - 사이버보안 파일(Cybersecurity File)이 MDF 내 독립 섹션으로 구성되어 있는가? - SBOM이 최신 릴리스...

### kb-eval-20261102-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "92ded92c13b6b2df", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "ace8476c9535cd1cadac8d64a788cb46b3d78a905da01c1e1dfc3e038615f0f4"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `92ded92c13b6b2df`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_2026.md)
- Source hash: `ace8476c9535cd1cadac8d64a788cb46b3d78a905da01c1e1dfc3e038615f0f4`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_2026.md`는 FDA QMSR 2026 전환에 따른 ISO 13485 기반 QMS·design control·inspection 준비 문서입니다.
- 현재 excerpt 핵심: ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR & Design‑Control Readiness**

**Bottom‑line recommendation**  
- The device must be cleared through the **510(k) Premarket Notification** pathway (Class I–III depending on its intended use and applicable product code).  
- Prior to submission, a full **QMSR (21 CFR 820)** compliance package – including documented design controls – is required. Until the classification, predicate, and complete design‑control artifacts are identified, the 510(k) cannot be finalized; escalation to senior RA leadership is warranted.

---

### 1. Classification & Submission Route
| Item | Determination |
|------|---------------|
| **Regulatory panel** | Determined by device function (e.g., imaging → 21 CFR Part 892; clinical chemistry → Part 862). The QMSR applies to *all* medical devices irrespective of panel. |
| **Device class** | Must be established via the FDA’s classification database or product code lookup. <br>**If Class I:** may qualify for an exempt 510(k) (still must meet QMSR). <br>**If Class II/III:** requires a traditional 510(k) with design‑control documentation. |
| **Submission type** | Standard **510(k)** (Premarket Notification) – no “supplement” pathway exists for 510(k)s. |
| **Key regulatory citation** | 21 CFR Part 807 (establishment registration & 510(k) submission). |

> *Action:* Identify the product code and confirm class before drafting the 510(k).

---

### 2. Required Evidence for QMSR Compliance

| Requirement | Evidence to be prepared |
|-------------|--------------------------|
| **Quality Management System (QMS)** – ISO 13485:2016 incorporation by reference | • Copy of current ISO 13485:2016‑certified QMS manual (or equivalent internal system) <br>• Mapping matrix showing how each ISO clause satisfies the new 21 CFR 820 subparts. |
| **Design Controls (Subpart C)** – Design & Development Planning, Input/Output, Review, Verification, Validation, Transfer, Changes | • Design‑control plan (including milestones and responsibilities) <br>• Design input specification sheet <br>• Risk Management File (ISO 14971:2019) linked to design inputs/outputs <br>• Design verification & validation protocols & reports (including usability testing if applicable) <br>• Design change control records (PCCP if AI/ML). |
| **Documented Procedures** – CAPA, Complaint Handling, Corrective Actions, Production & Process Controls | • SOPs satisfying each 820 subpart (e.g., SOP‑QMS‑001 – Management Review) <br>• Records of their implementation (training logs, audit reports). |
| **UDI Requirements** – Device label and packaging | • Label mock‑up with UDI in accordance with 21 CFR 830.10–830.30 (no specific § cited in source; verify separately). |
| **Post‑Market Surveillance Plan** (if required by device class) | • PMCF is not a US term; instead, provide a **Medical Device Reporting (MDR)** and **Recall/Correction** plan per 21 CFR 803 & 806. |

> *Citation:* The QMSR rulemaking text – Federal Register 2024‑01709 (final rule) and technical amendment 2025‑21955 – establishes the ISO 13485:2016 incorporation ([source 1] & [source 2]). No specific § numbers for design‑control subparts appeared in the source; **no specific identifier found in source — verify separately**.

---

### 3. Missing Information (must be obtained before submission)

| Gap | Why it matters |
|-----|-----------------|
| **Device classification & product code** | Determines 510(k) requirement, need for special controls, and applicable predicate device. |
| **Predicate device(s)** (if Class II) | Required to demonstrate substantial equivalence; includes cleared 510(k) numbers. |
| **Intended use/indications for use statement** | Core of the 510(k) summary & labeling requirements (21 CFR 801). |
| **Risk Management File (ISO 14971:2019)** – complete hazard analysis, risk control verification, residual risk evaluation. |
| **Software documentation** (if applicable) – validation plan, architecture diagram, and **Predetermined Change Control Plan (PCCP)** when AI/ML is used. |
| **UDI issuance agency details** (label format, record in GUDID). |
| **Evidence of QMSR training for all relevant staff** | Demonstrates compliance with 820.100‑820.110 requirements. |

---

### 4. Core Risk Controls to Embed in Design‑Control Package

1. **Risk Management Process** – Align with ISO 14971:2019 (hazard identification → risk analysis → risk evaluation → risk control implementation).  
2. **Design Verification & Validation** – Include testing that shows each design input is met and the device performs as intended under normal use conditions.  
3. **Usability Engineering** – Follow IEC 62366‑1:2015+A1:2020 for user interface risk.  
4. **Change Management** – Adopt a **Predetermined Change Control Plan (PCCP)** for any AI/ML updates.  
5. **CAPA System** – Document root‑cause analysis and corrective actions per 820.100‑820.110.  

---

### 5. Key Citations

| Item | Source |
|------|--------|
| QMSR rulemaking (final rule) | Federal Register 2024‑01709 (effective 2 Feb 2024). |
| Technical amendment to QMSR | Federal Register 2025‑21955. |
| Incorporation of ISO 13485:2016 | Source [2] – “ISO 13485:2016을 참조편입”. |
| eCFR link for 21 CFR Part 820 (effective 02‑Feb‑2026) | Source [1]. |
| FDA QMSR FAQs | Source [1] URLs. |

*No specific § numbers for design‑control subparts were present in the source; verify separately.*

---

### 6. Human‑Escalation Triggers

| Trigger | Recommended escalation |
|--------|--------------------------|
| **Classification or predicate cannot be identified** within 3 working days of review | Escalate to Senior RA Manager (or Regulatory Lead). |
| **Design‑control documentation incomplete** (missing verification/validation reports, risk file) | Pause submission; notify Project Lead and Quality Engineer. |
| **QMSR training records missing for >10% of key personnel** | Raise to Compliance Officer for immediate remediation. |
| **UDI labeling non‑conformant or GUDID entry not completed** | Alert Regulatory Operations Manager (21 CFR 830 compliance). |
| **Discrepancy between ISO 13485 QMS and 21 CFR 820 requirements** uncovered during internal audit | Convene cross‑functional corrective‑action meeting; involve QA Director. |

---

### 7. Peer Review Prompt

> *Colleague, please review the assumptions above:*
> - Have we accurately captured all design‑control deliverables required under the new QMSR for a typical Class II device?  
> - Are there any jurisdiction‑specific nuances (e.g., special controls, FDA guidance documents) that our current checklist misses?  
> - Does the list of missing information cover everything needed to draft a complete 510(k) submission, or should additional items (e.g., sterilization validation, biocompatibility data per ISO 10993‑1:2018) be added based on device type?

--- 

*End of Draft.*

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

> ① "Federal Register 2024-01709 (effective 2 Feb 2024)" — 공표일과 발효일 혼동(발효는 2026-02-02, 자기 표와 모순) ② QMSR 교육 근거 "820.100-820.110" — 교육은 §820.25.

**Source Excerpts**

1. Chunk `197674093189403324`

> ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820 - Federal Register: 2024-01709 (제정), 2025-21955 (기술적 수정) - FDA Compliance Program 7382.850 - 확인일: 2026-05-25

2. Chunk `211815826167619677`

> ## 1. 규정 개요 | 항목 | 내용 | |------|------| | 규정 | 21 CFR Part 820 | | 명칭 변경 | Quality System Regulation(QSR) → **Quality Management System Regulation(QMSR)** | | 최종규칙 공포 | Federal Register 2024-01709 (2024.2.2) | | 기술적 수정 | Federal Register 2025-21955 | | **발효일** | **2026년 2월 2일** | | 핵심 변경 | ISO 13485:2016을 참조편입(Incorporation by Reference)하고, FDA 추가요구를 별도 조항으로 보존 |

### kb-eval-20261102-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_us-005", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "8c1fdf2ec268ea0a", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8c1fdf2ec268ea0a`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-20_GSPR_QMSR_PRRC_%EC%A0%95%ED%95%A9%EC%84%B1%EA%B2%80%EC%A6%9D.md)
- Source hash: `5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`는 `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR & Design‑Control Readiness**  

---

### 1. Bottom‑Line Decision
- **Classification:** Determine Class based on intended use and risk profile. If the device is moderate‑risk (most diagnostic/monitoring devices) it will be **Class II → 510(k)**. Novel AI/ML functionality without a clear predicate may require **De Novo** classification.  
- **Submission Route:** 510(k) is fastest credible path for Class II; De Novo if no predicate exists.  

*Action:* Obtain the device’s intended‑use statement and perform a formal classification rule analysis (21 CFR §§ 862, 892 as appropriate).  

---  

### 2. Required Evidence & Documentation  

| Area | FDA/ISO Requirement | Evidence Needed |
|------|---------------------|-----------------|
| **Quality Management System** | 21 CFR §820 (effective Feb‑2026) – QMSR | Complete QMS manual, SOP inventory, records of implementation; compliance with §820.35(b) for document control. |
| **UDI** | 21 CFR §830 + EU MDR Art.27 (referenced in source) | Integrated UDI Data Record (UDR) SOP, label/packaging showing a full UDI, GUDID submission package. |
| **Design Controls** | 21 CFR §820.30 (design planning, inputs, outputs, verification, validation, transfer) | Design History File (DHF) containing design plan, requirement traceability matrix, verification & validation protocols and reports. |
| **Risk Management** | ISO 14971:2019 (A11 amendment referenced as “A11”) | Risk Management Plan, risk analysis workbook, risk control measures, residual risk justification. |
| **Biocompatibility** | ISO 10993 series (multiple parts) | Test reports for cytotoxicity, sensitization, irritation, systemic toxicity, etc., mapped to device‑contact duration. |
| **Sterilization (if applicable)** | ISO 11135/11137/17665/11737 | Validation reports (microbial inactivation, load mapping), labeling of sterilization method. |
| **Electrical Safety & EMC** | IEC 60601‑1 series (2020 amendment cited) | Test certificates for safety, leakage current, EMI/EMC compliance; applicable Annex/Clause citations. |
| **Software Lifecycle** | IEC 62304:2006+A1:2015 | Software Development Plan, architecture documents, verification & validation test suites, traceability matrix. |
| **Usability / Human Factors** | IEC 62366‑1:2015+A1:2020 | Usability engineering file, formative and summative testing results, risk control of use errors. |
| **Cybersecurity** | IEC 82304‑1 (state‑of‑the‑art) & FDA PCCP guidance Dec 2024 | Threat model, mitigation plan, Predetermined Change Control Plan (PCCP) if AI/ML updates are anticipated. |
| **Labeling** | 21 CFR §801; ISO 15223‑1:2021 | Labels, IFUs, symbols, warnings mapped to identified hazards. |
| **Electronic Signatures** | 21 CFR Part 11 (scope defined in SOP “QM‑IT‑001”) | Signed SOPs, audit trails, validation of e‑signature system. |

*Citation notes:* The source lists the standards as “Harmonized” or “State‑of‑the‑art” but provides no specific docket numbers; therefore **no device‑specific identifier was found – verify separately** for each item.

---  

### 3. Missing Information & Gap Mitigation  

| Gap (from source) | What is missing | Action required |
|-------------------|-----------------|-----------------|
| **MDR decision‑document template absent in domestic SOPs** | Formal decision‑making record for risk acceptability (ML‑MDR‑001) | Draft and approve the template; integrate into design‑control SOPs. |
| **UDI Master Record fragmented** | Unified UDI Data Record per §820.35(b) & 21 CFR §830 | Consolidate UDI entries into a single controlled database; update SOP “UDR Management”. |
| **Internal audit report narrative insufficient** | Objective evidence citations for audit findings | Revise the “External Audit Response” template to require traceability to records (e.g., SOP, test reports). |
| **Electronic‑signature scope ambiguous** | Defined applicability of 21 CFR Part 11 | Finalize “QM‑IT‑001 – Electronic Signature Scope”; train users on covered documents. |
| **AI/ML device lacking EU AI Act alignment** | Documentation of compliance with the EU AI Act (for export) and FDA PCCP for US market | Develop a cross‑jurisdictional AI/ML governance file; include change‑control plan per FDA guidance. |

---  

### 4. Core Risk Controls (derived from ISO 14971 & IEC 15223‑1)

1. **Design Input Verification** – ensure each requirement is testable and traceable.  
2. **Software Validation** – including algorithm performance, data set representativeness, and robustness to input variability.  
3. **Usability Safeguards** – critical user tasks labeled with IEC 15223‑1 symbols; error‑prevention UI design.  
4. **Labeling Warnings** – risk–based warnings (e.g., “Contraindicated for patients with X”) per ISO 15223‑1.  
5. **Device‑specific Sterilization Controls** – validated microbiological inactivation cycles.  
6. **Electrical Safety Measures** – insulation, leakage current limits, grounding per IEC 60601‑1 series.  
7. **Cybersecurity Controls** – authentication, encryption, vulnerability management plan.  
8. **PCCP** – pre‑specified change control for AI/ML model updates (FDA Dec 2024 guidance).  

---  

### 5. Human‑Escalation Triggers  

| Trigger | Who Must Be Notified | Deadline |
|--------|----------------------|----------|
| **Unresolved SOP gap (e.g., MDR decision template)** | QA Manager → Regulatory Lead | Within 5 working days of identification. |
| **UDI master‑record inconsistency** | QMS/Regulatory Compliance Officer | Immediate; halt any new labeling until resolved. |
| **Part 11 scope undefined** | IT Compliance Lead & QA Director | Before the next audit cycle (≤10 days). |
| **AI/ML change‑control plan not approved** | Head of Software Development → Regulatory Affairs VP | Prior to any model release or update. |
| **Evidence package incomplete for 510(k) / De Novo** | Regulatory Project Lead | Minimum 30 days before submission deadline; raise to senior management if delay >14 days. |
| **Adverse event signal emerging during design verification** | Safety Officer & Clinical Affairs | Immediate (within 24 h). |

---  

### 6. Reusable RA Judgment (Lesson Learned)

> **When mapping GSPR to US requirements, always verify the harmonization status of each standard against the FDA’s “Recognized Consensus Standards” database; do not assume EU‑MDR references satisfy QMSR obligations. Consolidate UDI data in a single controlled record per §820.35(b) and align the scope of Part 11 before any electronic signing is used for design‑control artifacts.**  

---  

### 7. Peer Review Prompt  

*“@RA‑Peer, please evaluate: (1) our assumption that the device will fall under Class II/510(k); (2) completeness of the evidence list given the gaps identified in the source; and (3) whether any additional US‑specific regulatory items (e.g., FDA Guidance on Clinical Evaluation for AI/ML, post‑market surveillance requirements) have been omitted.”*

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

1. Chunk `1061533089543682126`

> ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적용 | | AI/ML 기기 | OJEU/MDCG 단독 등재 없음 → EU AI Act 병행 필요(후속 과제) | | 운영 영향 | 체크리스트에 H/S 컬럼 신설, 개정판 번호(A11, A1, A2) 기재 의무화 |

2. Chunk `1066441905930561439`

> ### Gap → 조치 | Gap | 조치 | |-----|------| | 국내 SOP에 MDR 결정문서 양식 부재 | 양식 ML-MDR-001 초안(보고/미보고 결정트리) 신설 | | UDI 마스터 레코드 단편화 | UDR(UDI Data Record) 통합 관리 SOP 초안 (§820.35(b) + 21 CFR 830 + EU MDR Art.27) | | 내부감사 보고서 서술 수준 | "외부감사 대응 수준" 템플릿 개정 (객관적 증거 필수 인용) | | 전자서명 범위 모호 | Part 11 적용범위 정의 문서(QM-IT-001) 초안 예정 |

## ra_eu

### kb-eval-20261102-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7e2a36f15ae5489c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7e2a36f15ae5489c`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md)
- Source hash: `ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexIII_PMS_TD_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – PMS / PMCF Planning for the Three X‑ray‑related Products**  

---

### 1. Product‑specific classification & conformity‑assessment route  

| # | Product (as listed in source) | MDR rule used (Annex VIII) | Resulting **Class** | Conformity‑assessment route (Art. 52) |
|---|-------------------------------|---------------------------|---------------------|--------------------------------------|
| 1 | **X‑ray Detector** (image‑acquisition device) | Rule 17 – “devices intended for recording diagnostic images generated by X‑ray radiation” | **Class IIa** | Art. 52(6): **Annex IX** (full QMS + technical‑documentation assessment by a NB). *Alternative* Annex II & III + Annex XI §10 is possible but Annex IX is the usual route for Class IIa. |
| 2 | **Handheld X‑ray Source** (portable ionising‑radiation emitter) | Rule 10 – “active devices emitting ionising radiation for diagnostic radiology” | **Class IIb** | Art. 52(4): **Annex X** (type‑examination) **+ Annex XI** (production‑conformity verification). NB involvement is mandatory. |
| 3 | **GUI Software (SaMD)** – provides image display and diagnostic decision support | Rule 11 – “software providing information for diagnostic or therapeutic decisions” (impact assessed as non‑life‑threatening) | **Class IIa** | Art. 52(6): **Annex IX** (QMS + technical‑documentation assessment). |

*All classifications are derived from the MDR classification rules (Annex VIII) – no device‑specific identifiers appear in the source, therefore no further verification of a “predicate” or “registration number” is required at this stage.*

---

### 2. Post‑Market Surveillance (PMS) obligations  

| Requirement | Legal basis | Implementation note (per source) |
|-------------|--------------|-----------------------------------|
| **PMS system** | Art. 83 MDR | Must be established for each product; the source lists data‑sources (serious incidents, complaints, trend reporting, literature, user feedback). |
| **PMS plan** | Art. 84 MDR | Should describe frequency & methods of data collection – the source already defines periodicities (immediate/quarterly for serious incidents, monthly for non‑serious, quarterly for trends, etc.). |
| **Periodic Safety Update Report (PSUR)** | Art. 86(1)(a)–(c) MDR | • X‑ray Detector & GUI SW (Class IIa): update every **2 years** – matches source “PSUR 갱신 주기 2년”. <br>• Handheld Source (Class IIb): update **annually** – matches source “1년”. |
| **PMCF requirement** | Annex XIV Part B MDR | • X‑ray Detector: PMCF triggered after equivalence claim review. <br>• Handheld Source: “clinical data actively collected” because of ionising radiation exposure. <br>• GUI SW (SaMD): “error‑data collection during use mandatory”. |
| **EUDAMED obligations** | Art. 33‑39 MDR | All three devices require UDI registration; vigilance reports must be uploaded (source: “UDI 등록 + Vigilance 보고”). |

---

### 3. Required clinical & technical evidence  

| Evidence type | Where required (by product) | Source‑cited basis |
|---------------|----------------------------|--------------------|
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | All three devices | Source links CER to each product under “연계 문서”. |
| **PMCF Plan & PMCF Evaluation Report** – Annex XIV Part B | Handheld Source (mandatory), X‑ray Detector (after equivalence review), GUI SW (error‑data collection) | Same column “PMCF 필요성”. |
| **Performance test data** – IEC 62220‑1‑1 (DQE measurement) | X‑ray Detector (DQE degradation) | Explicitly listed as required evidence. |
| **Radiation dose monitoring data** | Handheld Source (dose‑over‑exposure, patient dose) | Listed under “PMS 담당 데이터 소스”. |
| **Software lifecycle records** – IEC 62304 (maintenance & bug logs) | GUI SW (maintenance record, bug log) | Explicit in source. |
| **Usability/Human factors evaluation** – IEC 62366‑1 | GUI SW (use‑error data collection) – not explicitly present → *missing* and must be generated to satisfy Annex I §5 & §22. |
| **Battery health verification** – IEC 60601‑2‑54 / IEC 60601‑1 (electrical safety) | Handheld Source (battery abnormality) – source notes “배터리 이상” as a PMS data point; detailed test results are *missing*. |
| **Trend‑analysis methodology** (statistical thresholds, control charts) | All devices – source shows trend reporting but no quantitative limits → *missing* and must be defined in the PMS plan. |

---

### 4. Gaps / Missing Information  

| Gap | Why it matters (regulatory impact) | Suggested action |
|-----|-----------------------------------|------------------|
| **Usability evaluation for GUI SW** (IEC 62366‑1) | Needed to address Annex I §5 (use‑error risks) and to justify the “error data collection mandatory” claim. | Conduct formative & summative usability testing; feed results into RMF & PMCF. |
| **Quantitative acceptance criteria for DQE degradation** | Required for PSUR conclusions on performance stability (Annex XIV Part A). | Define a statistical limit (e.g., ≤ 5 % drop over 12 months) and document validation. |
| **Dose‑over‑exposure alarm specifications** | Annex I §16 (radiation protection) demands demonstrable safeguards. | Provide functional testing data & risk controls for the handheld source. |
| **Battery failure mode analysis & mitigation** | Annex I §6 (device lifetime) and §7 (transport/storage). | Add FMEA/FTA items, battery health monitoring algorithm, and replacement schedule. |
| **Trend‑reporting statistical thresholds** | Art. 88 requires trend reporting; the PMS plan must specify when a trend triggers investigation. | Set quantitative limits (e.g., ≥ 2 % increase in dose‑over‑exposure events per quarter). |
| **Evidence of equivalence for X‑ray Detector** (if pursuing “equivalence claim”) | PMCF for the detector is contingent on this review; lack of evidence may force full clinical investigation. | Compile comparative bench data, published literature, and any existing CE‑marked predicates; document in CER. |
| **Current UDI registration status & vigilance submission logs** | EUDAMED compliance (Art. 33‑39) – missing proof could delay market access. | Verify UDI entries, upload all FSCA records to EUDAMED. |

---

### 5. Risk Management – Key Controls to be Documented in the RMF (Annex I §3)

| Hazard | Control(s) | Evidence required |
|--------|------------|--------------------|
| **DQE degradation** → image quality loss | *Periodic DQE testing*; alarm when > 5 % drop; corrective action: recalibration or device replacement. | IEC 62220‑1‑1 test reports, trend data in PMS. |
| **Radiation dose over‑exposure** (handheld) | *Real‑time dosimetry*; interlock shut‑off; user training on exposure limits. | Dose‑monitoring logs, functional safety tests (IEC 60601‑2‑54). |
| **Battery failure / overheating** | Battery health monitoring algorithm; temperature sensor; automatic shutdown. | Test data per IEC 60601‑1, FMEA results. |
| **Software error (GUI)** → misdisplay or incorrect decision support | *Error‑logging*, periodic software updates, verification of algorithm version, usability safeguards (confirmation dialogs). | IEC 62304 maintenance records, bug log, usability test reports. |
| **Use‑error by non‑expert operators** | Clear labeling (Annex I §23), training material, UI design complying with IEC 62366‑1. | Label & IFU review, user‑testing outcomes. |

All controls must be reflected in the **Risk Management File** and linked to residual‑risk evaluation in the PSUR/PMCF reports.

---

### 6. Human‑escalation triggers (when a reviewer or project lead must intervene)

| Trigger condition | Reason for escalation |
|-------------------|-----------------------|
| **Serious incident / FSCA** recorded in vigilance system (source line 1) | Immediate reporting to Competent Authority (Art. 87) and internal root‑cause analysis; may halt distribution. |
| **Trend exceeds pre‑defined threshold** (e.g., > 2 % rise in dose‑over‑exposure events per quarter) | Must initiate corrective action plan and possibly update PSUR ahead of schedule (Art. 88). |
| **Failure to generate required PMCF data within the planned timeframe** (e.g., no clinical dose data for handheld source after 6 months) | Escalate to senior Clinical Affairs lead; consider supplemental clinical investigation (Annex XIV Part B). |
| **Missing or incomplete UDI registration / vigilance upload in EUDAMED** | Flag to Regulatory Compliance Manager – non‑compliance with Art. 33‑39 may block CE mark renewal. |
| **Inability to meet PSUR update schedule** (annual for Class IIb, biennial for Class IIa) | Escalate to Project Management; allocate resources for data collection and reporting. |
| **New regulatory guidance published affecting X‑ray devices or SaMD** (e.g., MDCG guidance on AI/ML SaMD) | Initiate impact assessment; update risk control & PMCF plan if needed. |

---

### 7. Summary judgment  

- **X‑ray Detector** – Class IIa, route **Annex IX**. Current PMS data sources are adequate but lack usability evidence and quantitative DQE limits.  
- **Handheld X‑ray Source** – Class IIb, route **Annex X + XI**. Requires full type‑examination dossier plus annual PSUR; missing detailed dose‑monitoring validation and battery failure analysis.  
- **GUI Software (SaMD)** – Class IIa, route **Annex IX**. PMS plan includes error logging, but usability testing and IEC 62366‑1 compliance are not demonstrated.

All three products must finalize the listed missing evidence, embed the identified risk controls in their RMFs, and ensure that trigger thresholds for escalation are documented in the PMS plan.

---

### 8. Peer‑review request  

> **To a fellow EU RA colleague:**  
> Please challenge the assumptions made above regarding (i) classification of the GUI software as Class IIa under Rule 11, (ii) the sufficiency of the proposed PSUR frequencies versus the actual risk profile of the handheld source, and (iii) any gaps that may arise from recent MDCG guidance on AI‑based SaMD or ionising‑radiation safety. Identify any jurisdiction‑specific obligations that have not been captured (e.g., national competent‑authority requirements for portable X‑ray units). Your feedback will be used to refine the PMS/PMCF strategy before submission to the Notified Body.

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
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① IIa 대안경로 "Annex II & III + Annex XI §10" — Annex II/III는 TD 내용 규정으로 적합성평가 경로가 아님(52(6) 대안은 Annex XI Part A). KB Week04에도 없는 모델 자체 왜곡 ② [KB 원본 오류 재관측] PSUR IIb '1년' — Art. 86(1)상 IIb는 2년(10-29 발견분과 동일 원본). / **재검증으로 판정 철회·3점**: 'Annex II & III + Annex XI §10'은 Art. 52(6) 제2옵션의 정확한 표현임이 원문에서 확정(기술문서 Annex II·III + Annex XI §10/§18 적합성평가) — 최초 채점자(세션)가 '왜곡'으로 오단. 잔여 PSUR IIb 1년은 KB 원본 오류 전파(#144, 체크 유지)로 점수 무영향.

**Source Excerpts**

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

### kb-eval-20261102-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d22323874c00e9ab", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d22323874c00e9ab`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/README.md)
- Source hash: `30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules) ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software...
- 이 항목의 평가 포인트: 이 source는 PMS/PMCF 전용 문서가 아닐 수 있습니다. 좋은 답변은 surveillance 결론을 단정하지 않고 PMS/PMSR/PMCF에 연결되는 근거와 한계를 구분해야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – PMS / PMCF Planning for an Ionising‑Radiation Diagnostic Device (X‑ray Generator)**  

---

### 1. Device Synopsis (as understood from the source)

| Item | Description |
|------|-------------|
| **Intended purpose** | Emission of ionising radiation for diagnostic imaging (radiography / fluoroscopy). |
| **Technology family** | X‑ray generation system; may be accompanied by software that processes images (SaMD). |
| **Regulatory source cited** | “Rule 10: 이온화 방사선 방출 진단기기 (X‑ray 발생장치 → Class IIb)” – excerpt 2. |

*No further device‑specific data (model, accessories, user group) are supplied in the excerpts; those will have to be collected from the manufacturer before any submission can proceed.*

---

### 2. Classification & Conformity‑Assessment Route  

| Regulatory element | Reference (framework) |
|---------------------|------------------------|
| **Classification rule** | Rule 10 of Annex VIII – “Active devices for diagnosis and monitoring that emit ionising radiation” → **Class IIb** (source excerpt 2). |
| **Applicable Art. 52 paragraph** | **Art. 52(4)** – Class IIb devices require either a full technical‑documentation assessment under **Annex IX**, or the combined **type‑examination route (Annex X) together with production conformity verification (Annex XI)**. |
| **NB involvement** | Mandatory, because the device is Class IIb (Art. 52(4)). |
| **Chosen route (proposed)** | **Annex IX** – QMS + technical‑documentation assessment (simpler than the Annex X+XI combination for a single product line). |
| **Relevant MDR parts** | • Annex I – GSPR (to be demonstrated)  <br>• Annex II – Technical Documentation structure  <br>• Annex III – PMS documentation  <br>• Annex VIII – Classification rule  <br>• Annex XIV – Clinical Evaluation Report (CER) & PMCF plan. |
| **Declaration of Conformity** | Must be issued in accordance with **Art. 19** and Annex IV (content). |

---

### 3. Evidence Package Required for NB Review  

| Requirement | Where it belongs (MDR/ISO/IEC) | Minimum content | Citation |
|-------------|-------------------------------|-----------------|----------|
| **Technical Documentation (TD)** | Annex II §§1‑6 | • Device description, intended use, variants<br>• Design & manufacturing information<br>• GSPR compliance matrix (Annex I)<br>• Risk Management File (ISO 14971:2019) <br>• Verification & validation data | Annex II |
| **Risk Management System** | Annex I §3  (RMF basis) + ISO 14971:2019 | • Risk management plan, risk analysis, evaluation of residual risk, risk‑control measures, post‑production information collection | Annex I §3; ISO 14971 |
| **General Safety & Performance Requirements (GSPR) compliance** | Annex I §§1‑23 (esp. §16.4 – ionising radiation) | • Checklist mapping each GSPR to evidence (e.g., IEC 60601‑2‑54 for electrical safety, IEC 60601‑2‑28 for tube assemblies, IEC 62366‑1 for usability) | Annex I §16.4; no specific identifier found in source — verify separately |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (kept current under Art. 61) | • State‑of‑the‑art literature review (Rule 10 devices), <br>• Clinical data from investigations or post‑market use, <br>• Benefit–risk determination | Annex XIV Part A |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | • Systematic collection of PMS data, <br>• Definition of PMS indicators, <br>• Periodicity of updates, <br>• Integration with risk management | Art. 84 |
| **PMS System (process & responsibilities)** | Art. 83 | • Organizational structure for PMS, <br>• Reporting channels (serious incidents, FSCA), <br>• Trend analysis methodology | Art. 83 |
| **PMCF Plan** | Annex XIV Part B | • Objectives, study design, endpoints, enrolment criteria, timelines, data‑analysis plan, alignment with residual risk and GSPR gaps identified in the CER | Annex XIV Part B |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (annual for Class IIb) | • Conclusions of benefit–risk assessment, <br>• Main PMCF findings, <br>• Sales volume & population estimate, <br>• Any corrective actions taken | Art. 86 |
| **Quality Management System (QMS)** | ISO 13485:2016 (mandatory for Annex IX) | • Documented procedures covering design‑control, production, post‑market activities, internal audits, management review | ISO 13485 |
| **Software – SaMD classification & compliance** | Rule 11 (Annex VIII) – “Medical Device Software” (source excerpt 2) | • Classification justification, <br>• IEC 62304 lifecycle documentation, <br>• Cybersecurity risk assessment (Annex I §22), <br>• Usability validation (IEC 62366‑1). | Rule 11; Annex I §22; no specific identifier found in source — verify separately |

---

### 4. Gaps / Missing Information (to be obtained before NB submission)

| Gap | Why it matters | Action needed |
|-----|----------------|---------------|
| **Exact intended use statement & user profile** | Determines scope of clinical evaluation and risk analysis. | Obtain from manufacturer’s labeling/IFU. |
| **Device architecture diagram & bill‑of‑materials** | Required for Annex II §3 (design & manufacturing). | Request detailed engineering documentation. |
| **Clinical data source(s)** – either a dedicated clinical investigation or robust post‑market clinical follow‑up data. | Needed for CER and to satisfy Art. 61/62 obligations. | Identify existing studies; if none, design PMCF study. |
| **PMS indicators & trigger thresholds** | Must be defined in PMS plan (Art. 84) and fed into risk management updates. | Develop PMS KPI list with quantitative targets. |
| **Software functional specification & classification justification** | Rule 11 applies; software may raise the overall device class if it drives therapeutic decisions. | Provide SaMD scope, intended decision impact analysis. |
| **Evidence of compliance with IEC 60601‑2‑54 (X‑ray equipment) and IEC 60601‑2‑28 (tube assemblies)** | Directly linked to GSPR §16 (radiation safety). | Gather test reports, type‑examination certificates. |
| **Usability engineering evidence** (IEC 62366‑1) for lay‑person use if applicable. | Supports GSPR §22 & reduces use‑error risk (§5). | Conduct usability evaluation report. |
| **Post‑production information collection procedure** (Art. 83, §3) | Needed to feed the PMS system with real‑world data. | Define SOPs for field data capture. |

---

### 5. Summary of Required Risk Controls (high‑level)

1. **Radiation protection** – Design controls meeting IEC 60601‑2‑54 & Annex I §16.4 (shielding, dose monitoring).  
2. **Electrical safety & EMC** – IEC 60601‑1 series compliance (protective earthing, leakage currents).  
3. **Software safety** – IEC 62304 lifecycle processes; security controls per Annex I §22.  
4. **Usability / use‑error mitigation** – IEC 62366‑1 usability engineering & labeling per Annex I §23.  
5. **Residual risk evaluation** – Documented in RMF, cross‑checked against GSPR (§8) and reflected in PMCF objectives.  

All controls must be traced to the relevant GSPR clauses (Annex I §§3‑9, 16‑22, 23).

---

### 6. Human‑Escalation Triggers  

| Trigger | Severity | Escalation step |
|---------|----------|-----------------|
| **Missing clinical evidence** (no CE‑valid CER or PMCF data) | Critical – cannot demonstrate benefit–risk. | Halt submission; notify Project Lead → seek Clinical Evidence Team to design study. |
| **Incomplete PMS plan / missing indicators** | High – would breach Art. 84 & impede PSUR preparation. | Request immediate completion; if not delivered within 2 weeks, elevate to Regulatory Management. |
| **Unresolved SaMD classification ambiguity** (possible upgrade to Class III) | Medium‑High – may change conformity route. | Convene cross‑functional risk workshop; involve senior RA and Clinical Lead. |
| **Absent or insufficient IEC 60601‑2‑54 test data** | High – non‑compliance with radiation safety GSPR (§16). | Issue “stop‑work” order to Engineering; require corrective testing before NB submission. |
| **QMS gap identified during internal audit (e.g., missing design‑control records)** | Medium – required for Annex IX NB review. | Immediate CAPA, report to Quality Manager, update schedule. |
| **Deadline breach for PSUR (annual for Class IIb) > 30 days overdue** | Critical – Art. 86 non‑compliance leads to market‑surveillance penalties. | Alert Market Surveillance Officer; prepare remedial filing with NB. |

When any of the above triggers fire, the responsible person must log the issue in the project risk register, notify the Project Manager, and seek a formal decision from senior regulatory leadership before proceeding.

---

### 7. Peer‑Review Prompt  

> **Colleague, please review:**  
> - The assumption that Annex IX is the preferred route for this X‑ray generator (are there any strategic reasons to consider Annex X + XI?).  
> - Completeness of the evidence checklist – have we missed any MDR annexes or standard references specific to ionising‑radiation devices?  
> - Whether the identified gaps (clinical data, SaMD classification, IEC‑60601‑2‑54 compliance) are exhaustive given the limited source excerpts.  
> - Any jurisdictional nuances (e.g., upcoming EU guidance on AI/ML software that could affect Rule 11 interpretation).  

Your feedback will be incorporated before finalising the submission package.

--- 

*Prepared by: Theo – EU MDR Regulatory Affairs Specialist*

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

> "PSUR Art. 86 (annual for Class IIb)" — IIb는 2년(III·이식형만 연간). 소스에 주기 없어 모델 자체 오류.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261102-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "5c2415e27c6c6ca5", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `5c2415e27c6c6ca5`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week04_MDR_EU_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `Week04_MDR_EU_체계_상세.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUF...
- 이 항목의 평가 포인트: 이 source는 PMS/PMCF 전용 문서가 아닐 수 있습니다. 좋은 답변은 surveillance 결론을 단정하지 않고 PMS/PMSR/PMCF에 연결되는 근거와 한계를 구분해야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning**  
*Prepared for the EU MDR 2017/745 compliance team*  

---

### 1. Scope & Device Context (as understood from source)

| Item | Current knowledge | Gap / Evidence required |
|------|-------------------|------------------------|
| **Intended purpose / indication** | Not provided in the excerpt | Detailed device description, intended use, patient population, and clinical benefits must be documented (Annex II §1). |
| **Device type & technology** | Unknown – “growth case” only indicates a medical device subject to PMS/PMCF. | Classification rule(s) applicable to the technology (e.g., Rule 9‑11, 17, etc.) are required to determine class. |
| **Manufacturer / Authorized Representative** | Mention of an authorized representative (Art 11 MDR). | Name, address and EU declaration of conformity must be in place (Art 19; Annex IV). |
| **UDI assignment** | UDI portal & EUDAMED referenced. | UDI carrier, issuing agency and registration in EUDAMED must be confirmed (Art 27‑28). |

*Action:* Obtain the full device specification (label, IFU, risk analysis) before any classification work proceeds.

---

### 2. Classification & Conformity‑Assessment Route  

1. **Classification basis** – Apply the sequential rules of **Annex VIII** (Article 51 MDR). The highest‑ranked rule that matches the device determines the class (source excerpt [2]).  
   *If the device is active therapeutic → Rule 9 (Class IIa/IIb);*  
   *if it is an active diagnostic system → Rule 10 or Rule 17;*  
   *if it is software alone → Rule 11.*  

2. **Self‑classification responsibility** – The manufacturer bears the classification burden (source [2]). If uncertainty remains, consult the Competent Authority (CA) or the MDCG “Borderline and Classification” manual (latest 2023‑09 version v2.1.1).

3. **Conformity‑assessment route** (based on final class):  

| Class | MDR Art. 52 reference | Required NB involvement |
|-------|----------------------|--------------------------|
| **I (non‑sterile, non‑measuring)** | Art 52(7) – self‑declaration (Technical Documentation + DoC) | No NB |
| **Is / Im / Ir** | Art 52(7) – Annex IX Chapters I & III *or* Annex XI Part A (limited scope) | Yes (NB limited to sterile/measuring/reusable aspect) |
| **IIa** | Art 52(6) – Annex IX (QMS + technical‑documentation assessment of one representative device) or Annex II/III + Annex XI §10/§18 | Yes |
| **IIb** | Art 52(4) – Annex IX (representative per generic group) *or* Annex X + Annex XI | Yes |
| **III** | Art 52(3) – Annex IX full assessment *or* Annex X + Annex XI | Yes |

*Action:* Once the class is settled, select the appropriate route and initiate NB engagement (if required).

---

### 3. Required Evidence Package  

| Evidence | MDR reference | What must be provided |
|----------|---------------|-----------------------|
| **Technical Documentation (TD)** | Annex II §§1‑6 | Device description, design & manufacturing info, GSPR compliance, risk management file, verification/validation data, and clinical evaluation (see below). |
| **EU Declaration of Conformity** | Art 19 MDR; content in Annex IV | Signed by manufacturer, referencing all applicable conformity‑assessment procedures. |
| **Clinical Evaluation Report (CER)** | **Annex XIV Part A** – “CEP + CER (Article 61)” (source [1]) | Systematic literature review, clinical data from equivalent devices, benefit‑risk analysis; kept up‑to‑date per Art 61. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | Planned clinical investigations after CE marking, including objectives, endpoints, population, methodology and timeline. |
| **Post‑Market Surveillance (PMS) System** | Art 83 MDR | Structured PMS plan (Art 84), procedures for trend analysis, field safety corrective actions, etc. |
| **Periodic Safety Update Report (PSUR)** | Art 86 MDR (for Class IIa/IIb/III) – annual for IIb/III, biennial for IIa | Summaries of PMS data, PMCF findings, sales volume and user population. |
| **Vigilance reporting** | Art 87 MDR (source [1]) | Procedure for serious incident & field‑safety corrective action reporting to the CA. |
| **UDI registration** | Art 27‑28 MDR; EUDAMED entries | UDI carrier, issuing agency, device identifier, production identifier. |

*Missing items that must be supplied before NB submission:*  

- Full **risk management file** (RMF) complying with **Annex I §3‑9** and ISO 14971:2019.  
- Detailed **PMCF protocol** (including sample size justification).  
- **PMS plan** covering data collection, analysis methods, and update schedule.  
- **Clinical data source list** (clinical investigations, registries, literature) supporting the CER.  

---

### 4. Risk Controls & GSPR Alignment  

| GSPR § | Requirement | Typical control actions (examples) |
|--------|-------------|-------------------------------------|
| **§3 – Risk Management System** | Establish and maintain RMF (ISO 14971:2019). | Identify hazards, assess residual risk, verify effectiveness of controls. |
| **§4 – Risk Control Measures** | Apply ALARP principle; prove benefit outweighs risks. | Design safeguards, alarms, user training, labeling. |
| **§5 – Use‑error Risks** | Analyse potential misuse and design for safe use. | Usability engineering (IEC 62366‑1:2020). |
| **§6 – Device Lifetime** | Define expected service life; include in labeling. | Reliability testing per IEC 60601‑1. |
| **§8 – Benefit‑risk determination** | Document in CER & PMS reports. | Continuous benefit‑risk assessment throughout device lifecycle. |
| **§23 – Information supplied with the device** | Provide IFU, labeling, safety information (including UDI). | Align with MDR Annex I §23 and IEC 62366‑1 usability results. |

*Evidence to demonstrate compliance:* risk management plan, verification/validation reports, usability test outcomes, updated CER conclusions.

---

### 5. Human‑Escalation Triggers  

| Situation | Why escalation is required | Who should act |
|-----------|----------------------------|---------------|
| **Unclear classification** (multiple Annex VIII rules apply) | Misclassification leads to wrong conformity route & regulatory penalties. | Senior RA lead → consult MDCG guidance or CA. |
| **Missing clinical data for CER** (no adequate equivalence, insufficient post‑market evidence) | Incomplete CE marking dossier – NB will request additional evidence. | Clinical affairs team → acquire/plan investigational study. |
| **Device classified as Class IIb/III** but no NB contract in place | NB involvement is mandatory; delay may halt market launch. | Project manager → initiate NB selection & contract negotiation. |
| **PMS system not yet operational** (no procedures for incident capture, trend analysis) | Art 83‑86 require a functional PMS before CE marking. | Quality management officer → develop SOPs, assign responsibilities. |
| **PMCF plan absent or not aligned with CER conclusions** | Annex XIV Part B requires a proactive PMCF to close residual risk gaps. | Clinical research lead → design & submit PMCF protocol to NB. |
| **UDI not registered in EUDAMED** | Failure breaches Art 27‑28; may block market entry and post‑market reporting. | Regulatory compliance officer → complete UDI registration. |

When any trigger is hit, the responsible function must raise a formal “Regulatory Issue” ticket (e.g., via internal risk register) and notify the RA manager for decision‑making.

---

### 6. Summary Judgment  

1. **Classification** – Must be derived from Annex VIII rules; manufacturer holds responsibility (source [2]).  
2. **Conformity route** – Determined by final class per Art 52; NB involvement required for Classes Is/Im/Ir, IIa‑III.  
3. **Evidence package** – TD, DoC, CER (Art 61 Annex XIV), PMCF plan/report, PMS system (Art 83‑86), PSUR (if applicable) and vigilance procedures (Art 87).  
4. **Key gaps** – Intended use, device description, risk management file, clinical data sources, PMCF protocol, complete PMS plan, UDI registration.  

All identified gaps must be resolved before the dossier can pass NB assessment.

---

### 7. Peer‑Review Prompt  

> *“Colleague, could you examine whether our interpretation of the classification process (Annex VIII sequential rule application) fully captures any special rules that might push this device into a higher class (e.g., Rule 9/10/11 interactions)? Also, verify that we have accounted for all mandatory post‑market documentation for the identified class—especially the need for a PSUR versus a PMS report per Articles 85/86. Finally, confirm whether any additional national provisions (e.g., Korean §31 cited in source [1]) might affect the EU submission timeline or requirements.”*  

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist.*

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

> ① "PSUR annual for IIb/III" — IIb는 2년 ② IIa 대안 "Annex II/III + Annex XI §10/§18" 왜곡 반복.

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261102-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "8073c98cf657e132", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8073c98cf657e132`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_MDR_2017_745.md)
- Source hash: `15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_MDR_2017_745.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | |...
- 이 항목의 평가 포인트: 이 source는 PMS/PMCF 전용 문서가 아닐 수 있습니다. 좋은 답변은 surveillance 결론을 단정하지 않고 PMS/PMSR/PMCF에 연결되는 근거와 한계를 구분해야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – PMS / PMCF Planning & Conformity‑Assessment Outlook**

---

### 1. Scope of the current evidence (what we have from the source)

| Source | Content relevant to MDR | Comment |
|--------|--------------------------|---------|
| **Excerpt [1]** – “TD 작성 절차” | Lists the activities and deliverables that must be produced for a complete Technical Documentation (TD): TD checklist, design & manufacturing data, GSPR‑mapping report, Clinical Evaluation Report (CER), Risk Management File (RMF), PMS Plan, NB submission record. | Demonstrates that the organisation already follows a structured MDR‑aligned workflow. |
| **Excerpt [2]** – “EU_MDR_2017_745 … guide” | References the primary regulatory texts and standards that will govern the device: EU MDR 2017/745 (incl. Annex I GSPR, Annex VIII classification rules), ISO 13485:2016, ISO 14971:2019, IEC 62304, IEC 60601‑1, IEC 60601‑2‑54, plus the internal form “F‑MDR‑TD‑CHK‑001”. | Supplies the framework but **no device‐specific identifiers** (e.g. intended purpose, risk class). |

> *No specific device description, intended use, or classification rule number appears in the source excerpts – this must be obtained before any definitive regulatory judgment can be made.*

---

### 2. Classification & Conformity‑Assessment Route – What is needed

| Step | Requirement (MDR) | Evidence to be supplied |
|------|-------------------|--------------------------|
| **2.1 Identify intended medical purpose** | Art. 2(1) MDR defines the “medical device” and its intended use. | Written Intended Use Statement, Indications for Use, Target Population. |
| **2.2 Map to Classification Rules (Annex VIII)** | Apply the appropriate rule (e.g. Rule 9‑11‑17 for active devices, Rule 22 for measuring). | Decision tree showing which rule(s) apply; reference to device function. |
| **2.3 Determine class** | Art. 52 MDR – class I–III based on the rule outcome. | Classification justification document (incl. rule number and rationale). |
| **2.4 Select conformity‑assessment route** <br> • **Class I (non‑sterile, non‑measuring)** – Self‑declaration (Art. 52(7)), no NB involvement.<br> • **Is / Im / Ir** – Annex IX (limited scope) or Annex XI (partial).<br> • **Class IIa** – Annex IX full assessment **or** Annex II + III + Annex XI §10/§18.<br> • **Class IIb** – Annex IX full assessment **or** Annex X + Annex XI.<br> • **Class III** – Annex IX full assessment **or** Annex X + Annex XI. | Class determination (Step 2.3) feeds directly into the route matrix (Art. 52). |

*Citation: MDR Art. 52(3‑7); Annex VIII classification rules; Annex IX, X, XI conformity‑assessment procedures.*

**Current status:** *Unable to assign a class because intended use and functional description are missing.*  

---

### 3. Required Evidence for the Technical Documentation (TD)

| Annex II § | Requirement | Typical artefact | Source reference |
|-----------|-------------|------------------|-------------------|
| **§1 – Device Description** | Name, model, version, variants, intended purpose. | Device Specification Sheet. | Excerpt [1] – “TD 목차·체크리스트”. |
| **§2 – Manufacturer Information** | Legal name, address, UDI‑system enrolment. | Company registration, UDI‑DB entry. | — |
| **§3 – Design & Manufacturing Information** | Design drawings, processes, material specs, V&V results. | “설계·제조 정보, V&V 결과” (Excerpt [1] step 2). |
| **§4 – General Safety & Performance Requirements (GSPR)** | Mapping of each GSPR (Annex I) to evidence. | GSPR‑mapping checklist & report (Excerpt [1] step 3). |
| **§5 – Benefit–Risk Assessment & Risk Management** | RMF, risk analysis, residual risk evaluation. | “위험관리 파일 통합” (Excerpt [1] step 5); ISO 14971:2019. |
| **§6 – Verification & Validation / Clinical Evaluation** | *Part 6.1* – Clinical Evaluation Report (CER). <br>*Part 6.2* – PMCF plan/evaluation (if required). | CER (Excerpt [1] step 4); PMCF plan (to be drafted). |
| **Annex III** – PMS System | Art. 83–86 – PMS Plan, periodic safety update report (PSUR) or PMS Report. | “PMS 계획서 작성” (Excerpt [1] step 6). |

All of the above must be compiled and signed off in the **TD approval record** (Excerpt [1] step 7).

---

### 4. Missing Information – Gaps that must be filled before NB submission

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Device name, model, variants & versioning** | Required in Annex II §1 & for UDI registration (Art. 33‑36). | Obtain from R&D / product management. |
| **Detailed intended use / Indications** | Drives classification (Annex VIII) and clinical evaluation scope (Annex XIV Part A). | Draft Intended Use Statement; include target patient group, anatomical site, mode of action. |
| **Functional description & principle of operation** | Needed to select the correct classification rule(s) (Rule 9‑11‑17 etc.). | Collect from design dossier. |
| **Clinical evidence plan** (type of data: literature review, clinical investigation, PMCF) | Determines whether a CER alone suffices or if additional PMCF is mandatory (Art. 61 & Annex XIV Part B). | Define Clinical Evaluation Strategy; map to available data sources. |
| **Risk Management File (RMF) – current version** | Must demonstrate compliance with GSPR §3‑9 and ISO 14971:2019. | Provide latest RMF, include risk control measures for identified hazards. |
| **PMS Plan details** – scope, methods, reporting intervals | Required by Art. 84; basis for PSUR (Art. 86) or PMS Report (Art. 85). | Draft PMS Plan with data‑collection procedures, responsibilities, and timelines. |
| **Sterility / Measuring / Reusable surgical status** (if applicable) | Determines whether the device falls into Is/Im/Ir and thus a limited NB scope (Art. 52(7)). | Clarify product attributes. |

*All missing items are explicitly flagged as “no specific identifier found in source – verify separately.”*

---

### 5. Risk Controls – Core Requirements

| GSPR reference | Control required | Typical evidence |
|----------------|------------------|-------------------|
| **Annex I §3** (Risk‑management system) | Implement ISO 14971:2019 risk management process; maintain RMF. | Risk Management File, risk analysis matrix. |
| **§4** (Risk control measures) | Identify and apply protective measures; verify effectiveness. | Verification & validation reports, post‑market data. |
| **§5** (Use‑error) | Usability engineering per IEC 62366‑1:2020; mitigate user errors. | Usability test reports, UI design rationale. |
| **§6** (Device lifetime) | Define expected service life and maintenance schedule. | Lifecycle plan, ageing studies. |
| **§7** (Transport & storage) | Design packaging, handling instructions to preserve safety. | Packaging Specification, transport validation. |
| **§8** (Benefit‑risk) | Document the overall benefit–risk determination. | Benefit‑risk analysis summary within RMF. |

*These controls are already reflected in the workflow steps of Excerpt [1] (GSPR mapping, risk file integration).*

---

### 6. Human‑Escalation Triggers

| Trigger | Action required | Responsible role |
|--------|-----------------|-------------------|
| **Insufficient device description / intended purpose** | Pause classification work; request complete Intended Use Statement. | RA Lead → R&D liaison. |
| **Classification outcome = Class IIb or III** | NB involvement mandatory (Annex IX full assessment **or** Annex X + XI). Initiate NB selection and contact. | RA Lead + Regulatory Project Manager. |
| **Absence of clinical evidence sufficient for CER** | Either commission a clinical investigation or develop PMCF plan to generate data. | Clinical Affairs → RA. |
| **RMF not up‑to‑date with latest design changes** | Update risk analysis; re‑run GSPR mapping before TD sign‑off. | QA / Risk Management Officer. |
| **PMS Plan missing data‑collection methodology** | Draft detailed PMS procedures (sampling, adverse event reporting). | Post‑Market Surveillance Coordinator. |
| **Approaching EU‑MDR implementation deadline for X‑ray systems (2026 schedule)** | Verify that IEC 60601‑2‑54 compliance documentation is complete; confirm UDI registration. | Compliance Engineer. |

When any of the above triggers fire, the RA team must raise a **“Regulatory Gap Review”** ticket in the project management system and obtain sign‑off from the RA Lead before proceeding.

---

### 7. Regulatory Judgment (preliminary)

*Given the current documentation state (see Section 4), the device’s classification cannot be conclusively determined. The essential missing elements are a clear Intended Use Statement, functional description, and evidence of clinical performance. Until these are supplied, no definitive conformity‑assessment route can be assigned, and NB involvement cannot be scheduled.*

**Next step:** Obtain the missing product‑specific information (Intended Use, mode of action, risk profile) and update the Risk Management File accordingly. Once available, re‑run the Annex VIII classification matrix and select the appropriate MDR conformity‑assessment route per Art. 52.

---

### 8. Peer‑Review Prompt

> **Colleague, could you review the above draft for**  
> • Completeness of the required evidence list (Annex II/III, Annex XIV) given the limited source data,  
> • Correctness of the classification‑route matrix (Art. 52 & Annex IX/X/XI), and  
> • Any jurisdictional gaps we may have missed, especially concerning X‑ray systems referenced in the guide (IEC 60601‑2‑54 compliance, radiation‑related GSPR §16).  

Please challenge any assumptions or suggest additional items that should be flagged before we seek NB feedback.

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

> IIa 대안 "Annex II + III + Annex XI §10/§18" 왜곡(Art. 52(6) 대안은 Annex XI Part A). Annex II §1-6 구조는 이번엔 정확. / **재검증으로 판정 철회·3점**: IIa 대안 'Annex II+III+Annex XI §10/§18' 표기는 원문 Art. 52(6) 부합(위와 동일). 다른 결함 없음 — Annex II §1-6 구조·Art.52 단락 모두 정확.

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `1072636411107495596`

> --- doc-id: EU_MDR_2017_745 title: "EU MDR — Regulation (EU) 2017/745 요약 및 적용 지침" type: Guide version: v0.3.1 status: draft category: 01_법규_규제 purpose: "EU MDR 2017/745 핵심 요구사항, 2026 일정, 기술문서 구성 및 X-ray 시스템 적용 지침" applicable: [EU MDR 2017/745, EU MDR GSPR Annex I, ISO13485:2016, ISO14971:2019, IEC 62304, IEC 60601-1, IEC 60601-2-54, UDI] forms: [F-MDR-TD-CHK-001] related-docs: - GSPR_정합표준_매핑표 - GSPR_체크리스트_v0.2_템플릿 - PRRC_역할_및_한미_대응자_매핑 - EU_AI_Act_MDR_중첩적용_매핑 - ISO13485_2016_요약 - SOP-CC-001 - SOP-PSUR-001 - SOP-FSCA-001 - TF-TD-001 related-issues: [4, 5, 22, 33, 989] owner: RA/QA Lead last-review: 2026-07-23 review-due: 2027-06-09 --- # EU...

### kb-eval-20261102-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "27e387bdbf72c0eb", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "229ed67db908335f1ee3f0eb51fd11a50f828f2ecba0f269c5461bb4f52f2547"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `27e387bdbf72c0eb`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PSUR_%ED%85%9C%ED%94%8C%EB%A6%BF_MDR_Article86.md)
- Source hash: `229ed67db908335f1ee3f0eb51fd11a50f828f2ecba0f269c5461bb4f52f2547`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PSUR_템플릿_MDR_Article86.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Section 4. 심각한 부작용 및 안전 신호 (Art.86(1) 본문 — PMS 데이터 분석 · Art.88 trend) **4.1 보고 기간 내 Serious Incidents** | 이벤트 번호 | 발생일 | 제품 관련성 | 내용 요약 | 취해진 조치 | 보고 상태 | |---|---|---|---|---|---| | SI-[번호] | [날짜] | [확인/추정/관련없음] | [요약] | [FSCA/경고문 등] | [CA 보고 완료] | | (해당 없음) | — | — | 보고 기간 내 Serious Incident 없음 | — | — | **4.2 Trend Reporting (Art.88)** | 관찰된 트렌드 |...
- 이 항목의 평가 포인트: 이 source는 PMS/PMCF 전용 문서가 아닐 수 있습니다. 좋은 답변은 surveillance 결론을 단정하지 않고 PMS/PMSR/PMCF에 연결되는 근거와 한계를 구분해야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Periodic Safety Update Report (PSUR) Planning**  
(derived from the “PSUR _템플릿_MDR_Article86.md” source)

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Reasoning / Evidence |
|------|-----------------------|
| **Class (pre‑liminary)** | The preparation of a PSUR indicates that the device falls into **Class IIa, IIb or III** – only these classes are required to produce a PSUR under **Art. 86 MDR**【source [2]】. |
| **Classification rule** | Not supplied in the source. The manufacturer must apply the appropriate rule(s) of **Annex VIII** (e.g., Rule 9‑11, Rule 17 etc.) to determine the final class. *Missing information – verify separately.* |
| **Conformity‑assessment route** | <ul><li>If **Class IIa** → **Art. 52(6)**: Annex IX (QMS + technical‑documentation assessment) with NB involvement.</li><li>If **Class IIb/III** → **Art. 52(4) / 52(3)**: Either <br> – Annex IX (full technical‑documentation assessment) **or**<br> – Annex X (type‑examination) **combined with** Annex XI (production conformity verification). NB involvement is mandatory.</li></ul> |

*Action*: Confirm the final class and rule; then select the matching route.

---

### 2. Required Evidence for a Complete PSUR  

| Requirement | Source / Regulatory Basis | Current Status (from source) |
|-------------|---------------------------|------------------------------|
| **PMS data set** (serious incidents, field safety corrective actions, trend analysis) | **Art. 86(1)** – content of the PSUR; **Art. 88** – Trend Reporting (source [1]) | Table placeholders only; no actual incident numbers supplied. |
| **Benefit‑Risk evaluation** (comparison with previous PSUR & CER) | **Art. 86(1)(a)** – conclusions on benefit‑risk balance (source [2]) | Qualitative summary fields present, but quantitative data missing. |
| **Clinical Evaluation Report (CER)** – up‑to‑date version | **Annex XIV Part A** – CER must be kept current under **Art. 61** | Not referenced in the excerpts; presumed required. |
| **PMCF plan & results** | **Annex XIV Part B** – PMCF planning and evaluation report | No PMCF data shown; gap identified. |
| **PMS Plan** (overall system) | **Art. 84** – PMS plan must be documented | Not present in the template excerpt. |
| **Risk Management File (RMF) updates** | **Annex I §3‑§8** – risk management system and residual‑risk assessment | No explicit RMF evidence cited; required to reflect any new risks identified in the PSUR. |
| **Labeling / IFU changes** | **Annex I §23** – information supplied with the device | Not shown; must be updated if corrective actions affect user instructions. |

*Action*: Populate all tables with real data, attach the latest CER and PMCF documentation, and ensure RMF reflects any residual‑risk updates.

---

### 3. Missing Information / Gaps  

| Gap | Why it matters | How to obtain |
|-----|----------------|---------------|
| **Device name, model & intended purpose** | Needed for classification, risk analysis and to link PMS data to the correct product. | Manufacturer’s technical file. |
| **Exact classification rule (Annex VIII)** | Determines NB involvement and the appropriate conformity‑assessment route. | Apply rule matrix to device description. |
| **Serious incident details (SI‑numbers, dates, causality assessments)** | Required for Art. 86(1) serious‑incident table; triggers possible FSCA. | Collect from vigilance system / national reporting database. |
| **Trend‑reporting thresholds & observed values** | Art. 88 requires detection of trends exceeding predefined limits. | Define in PMS plan; populate after data analysis. |
| **Quantitative benefit‑risk metrics (e.g., incidence rates, effect sizes)** | Supports the “overall benefit‑risk conclusion” required by Art. 86(1)(a). | Analyse clinical and post‑market data, update CER. |
| **PMCF results for the reporting period** | Annex XIV Part B mandates inclusion of PMCF findings in the PSUR (benefit‑risk input). | Execute or summarize ongoing PMCF studies. |
| **Corrective/Preventive actions taken** | Must be documented in the “actions taken” column and reflected in RMF & labeling. | Record from field notices, design change orders. |
| **Updated risk control measures** (e.g., new safety‑critical software updates) | Required under GSPR §3‑§8 to show that residual risk remains acceptable. | Update RMF and re‑run risk assessments. |

---

### 4. Recommended Risk Controls & Documentation Updates  

1. **Update the Risk Management File** – capture any newly identified hazards from serious incidents or trends; apply ISO 14971:2019 risk control hierarchy.  
2. **Issue Field Safety Corrective Actions (FSCA)** where required – include recall, device modification, or labeling change per Art. 86(1) and Annex I §23.  
3. **Revise the IFU / labeling** to incorporate new warnings, contraindications, or usage instructions derived from incident analysis.  
4. **Implement design changes** (if warranted by trend analysis) following IEC 60601‑2‑54/28 etc., and document in technical file (Annex II §5).  
5. **Strengthen PMS plan thresholds** – define quantitative limits for each adverse event type; ensure they trigger a formal review when exceeded (Art. 84, Art. 88).  

All above actions must be recorded in the **Post‑Market Surveillance Report (Annex III)** and communicated to the Notified Body during the next surveillance audit.

---

### 5. Human‑Escalation Triggers  

| Trigger | Immediate Action |
|--------|-------------------|
| **Any Serious Incident (SI) reported** | Notify the NB within the statutory timelines (Art. 87); initiate FSCA; update PSUR tables. |
| **Trend exceeds predefined threshold** (per Art. 88) | Convene a cross‑functional risk review, prepare corrective action plan, and inform the NB if the trend may affect device safety. |
| **Change in benefit‑risk balance** (negative shift identified in Section 6) | Re‑evaluate the CER, potentially launch additional PMCF studies; update RS/IFU; consider Class‑specific reporting to competent authorities. |
| **New residual risk uncovered that is not mitigated** | Perform a supplemental risk assessment per ISO 14971:2019; implement additional controls before next market release. |
| **NB requests clarification or supplemental evidence** | Provide requested documentation (e.g., updated RMF, PMCF data) within the deadline set by the NB. |
| **Regulatory amendment affecting GSPR or classification** | Review impact on device, update technical file, and submit amendment to EUDAMED/competent authority as required. |

---

### 6. Summary Judgment  

*The device is currently presumed to be Class IIa–III based on the necessity of a PSUR (Art. 86). The appropriate conformity‑assessment route must be confirmed after the exact classification rule is applied (Annex VIII). A complete PSUR will require populated serious‑incident tables, trend‑analysis data, an updated benefit‑risk evaluation, the latest CER and PMCF evidence, and corresponding updates to the Risk Management File, labeling, and PMS plan. Any occurrence of a serious incident, a adverse trend, or an unfavorable shift in benefit‑risk must trigger immediate human escalation as defined above.*

---

### 7. Peer‑Review Prompt  

> **Colleague, could you verify:**  
> - The assumed class (IIa vs IIb/III) based on the product description we have not seen yet.  
> - That all mandatory evidence items listed under Art. 86(1) and Annex XIV Part B are captured in our PSUR template.  
> - Any jurisdiction‑specific nuances (e.g., national reporting timelines) that might affect the escalation thresholds outlined above.  

*Please challenge any assumptions, highlight missing source coverage, and point out potential gaps in EU‑MDR compliance.*

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

1. Chunk `1068941934152517684`

> ### Section 4. 심각한 부작용 및 안전 신호 (Art.86(1) 본문 — PMS 데이터 분석 · Art.88 trend) **4.1 보고 기간 내 Serious Incidents** | 이벤트 번호 | 발생일 | 제품 관련성 | 내용 요약 | 취해진 조치 | 보고 상태 | |---|---|---|---|---|---| | SI-[번호] | [날짜] | [확인/추정/관련없음] | [요약] | [FSCA/경고문 등] | [CA 보고 완료] | | (해당 없음) | — | — | 보고 기간 내 Serious Incident 없음 | — | — | **4.2 Trend Reporting (Art.88)** | 관찰된 트렌드 | 예상 발생률 | 실제 발생률 | 조치 | |---|---|---|---| | [항목] | [기준치] | [실제치] | [FSCA/경고문/설계변경 등] | | (해당 없음) | — | — | 임계값 초과 없음 | — | ---

2. Chunk `1141979248009057881`

> ### Section 6. Benefit-Risk Balance 결론 (Art.86(1)(a)) > 이전 PSUR / CER 대비 benefit-risk balance 변화 여부 평가. | 평가 항목 | 이전 PSUR | 이번 PSUR | 변화 여부 | |---|---|---|---| | 주요 편익 (Clinical benefits) | [요약] | [요약] | [변화 없음/변화 있음] | | 잔존 위험 (Residual risks) | [요약] | [요약] | [변화 없음/변화 있음] | | Overall benefit-risk 결론 | 유리함 | [유리함/불확실/불리함] | [변화 없음/변화 있음] | **Benefit-risk 결론:** > [이번 보고 기간의 데이터를 종합할 때, 해당 기기의 benefit-risk balance는 여전히 유리하며/변화가 없으며, 기존 적응증에서의 사용은 적절한 것으로 판단됩니다. / 또는: 새로운 위험 신호가 확인되어 다음의 조치를 취합니다: ...] ---

## ra_kr

### kb-eval-20261102-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "76a94645e1f116dc", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `76a94645e1f116dc`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e`
- Focus: digital medical products act impact
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital “AI 영상분석 모듈” (소프트웨어 기반 의료기기)**  

---

### 1. Device Overview  
* **형태**: 독립형 AI‑기반 영상 분석 소프트웨어(콘솔/뷰어 형태)  
* **예상 적용 대상**: 의료기관의 영상 진단 보조·AI 판독 지원  
* **주요 기능**: 병변 탐지·정량화, 보고서 자동생성 (알고리즘은 생성형 AI 활용 가능)  

---

### 2. Classification & Submission Route  

| 항목 | 판단 근거 |
|------|-----------|
| **예상 등급** | 영상‑진단 보조 소프트웨어는 일반적으로 **3등급·4등급**에 해당하지만, 정확한 위험도(위험 점수)와 사용 환경을 반영해 *‘의료기기 품목 및 품목별 등급에 관한 규정’*에 따라 최종 등급 확인이 필요함. |
| **제출 경로** | 3등급·4등급 → **허가(신청)** 절차 (MFDS 직접 심사) <br>※ 2등급인 경우는 **인증**(심사기관)으로 전환될 수 있음. 정확한 등급 확인 후 해당 경로 선택. |
| **필요 인증** | KGMP 적합성인정(의료기기법 제28조) – 제조·품질관리 체계 구축 필요 |

*No specific identifier found in source — verify separately.*

---

### 3. Required Evidence  

| 구분 | 내용 | 근거/가이드라인 |
|------|------|-----------------|
| **위험 관리** | ISO 14971:2019 기반 위험 관리 파일, 위험‑보완 조치 (RBI) | 프레임워크 기준 (ISO 14971) |
| **소프트웨어 생명주기** | IEC 62304 2006+A1:2015 적용 – 개발·검증·유지보수 기록 | 프레임워크 기준 (IEC 62304) |
| **사용적합성(Usability)** | IEC 62366‑1 2015+A1:2020 기반 사용성 엔지니어링 계획 및 검증 보고서 | “사용적합성 엔지니어링 계획 수립” – [2] |
| **사이버 보안** | • 보안 사양, SBOM 관리 절차<br>• ‘의료기기 사이버보안 허가·심사 가이드라인(개정)’ 적용 <br>• ‘디지털의료기기 전자적 침해행위 보안 지침(안)’ 적용 | “SBOM 관리 절차 정합성 확인” – [2]; “디지털 의료제품법_요구사항_매트릭스” – [2] |
| **임상·효능 데이터** | - 국내 임상시험계획서 (필수 여부는 등급·외국 CER 수용 범위에 따라 결정) <br>- 해외 CE 마크/ FDA 510(k) 등 기존 임상 평가 보고서(가능한 경우 MFDS ‘foreign clinical evaluation report’ 인정 여부 확인) | “생성형 AI 의료기기 허가·심사 가이드라인” – [1] (중간 관련성) |
| **라벨링·사용설명서** | 한국어 라벨·IFU, 필수 표시사항(품목코드, 제조원, 사용제한 등) | MFDS 고시 ‘의료기기 라벨·포장’ 규정 (프레임워크 기준) |
| **품질경영시스템** | KGMP 인증을 위한 QMS 문서(품질 매뉴얼, SOP 등) | KGMP 제도 요구사항 |
| **데이터·거버넌스** | AI 데이터셋·모델 거버넌스 절차 (SOP‑AIDATA‑001 / SOP‑AIGOV‑001) | “AI 모델 데이터셋·거버넌스 절차 수립” – [2] |

---

### 4. Identified Gaps / Missing Information  

| 항목 | 현재 상황 | 필요 조치 |
|------|----------|-----------|
| **정확한 등급** | 추정만 존재 | MFDS ‘의료기기 품목 및 품목별 등級에 관한 규정’ 적용 후 등급 확정 |
| **국내 임상 데이터 요구 여부** | 외국 CER 활용 가능성은 가이드라인에 언급됨(중) | MFDS ‘foreign clinical evaluation report’ 수용 범위 최신 고시 확인·필요 시 국내 임상시험 설계 |
| **한국어 라벨·IFU 샘플** | 아직 미제공 | 한국어 표기 요구사항 정리 및 초안 작성 |
| **KGMP 인증 현황** | 제조/품질 관리 체계 문서 비공개 | KGMP 적합성 평가를 위한 QMS 문서 전면 검토 |
| **사이버 보안 상세 구현** | SBOM·보안 매트릭스(RA‑01~RA‑20) 진행 중 | 최종 보안 테스트 결과 및 대응 매트릭스 완성 |
| **사용자 교육·유효성 검사 계획** | 사용적합성 엔지니어링 계획 v0.2 완료 | 실제 사용자 검증(User Testing) 결과 보고서 추가 필요 |

---

### 5. Core Risk Controls (Korean‑Specific)

1. **위험 관리 파일** – ISO 14971 적용, 위험 수준이 ‘고(Severe)’인 경우 반드시 국내 임상 데이터 확보.  
2. **소프트웨어 안전 라이프사이클** – IEC 62304에 따라 개발 단계별 검증·검증 기록 보관.  
3. **사용성 검증** – IEC 62366‑1 기반 사용 시나리오, 오류 예방 설계, 최종 사용자 테스트 (의료인/환자).  
4. **사이버 보안** – SBOM 작성·관리, 취약점 주기적 스캔, 네트워크 연결 시 암호화·인증 적용, MFDS ‘디지털 의료제품법’에 명시된 사이버보안 가이드라인 전면 적용.  
5. **데이터 거버넌스** – 데이터셋 품질·대표성 검증, 모델 업데이트 절차(SOP‑AIGOV‑001) 마련.  

---

### 6. Citations  

| 구분 | 출처 |
|------|------|
| **프레임워크 (ISO/IEC)** | ISO 14971:2019, IEC 62304 2006+A1:2015, IEC 62366‑1 2015+A1:2020 |
| **디지털 의료 제품법 가이드라인(2024~2025)** | “생성형 AI 의료기기 허가·심사 가이드라인” – [1] (중) <br>“독립형 디지털의료기기SW 사용적합성 가이드라인” – [1] (높음) |
| **사이버보안·SBOM 관련** | “의료기기 사이버보안 허가·심사 가이드라인(개정)” – [1] (높음) <br>“디지털의료기기 전자적 침해행위 보안 지침(안)” – [1] (높음) |
| **프로젝트‑레벨 조치 매트릭스** | “RA‑01~RA‑20 대응 매트릭스 작성” – [2] <br>“사용적합성 엔지니어링 계획 수립” – [2] <br>“SBOM 관리 절차 정합성 확인” – [2] |
| **MFDS 고시·규정** | No specific identifier found in source — verify separately. |

---

### 7. Human‑Escalation Triggers  

| 상황 | 필요 조치 (Human Review) |
|------|---------------------------|
| 등급(3등급/4등급) 확정 불가 | MFDS ‘품목별 등급 규정’ 검토 후 최종 등급 결정 요청 |
| 외국 임상 평가 보고서(CER) 수용 여부 미확인 | 최신 MFMF 고시·지침(외국 CER 인정 범위) 확인 및 필요 시 국내 임상시험계획 승인 신청 |
| 한국어 라벨·IFU 초안 부재 | 라벨링 전문가와 협업, 법정 필수 표기 검증 |
| KGMP 인증 미완료 | 품질팀에 KGMP 적합성인증 프로세스 가속화 요청 |
| 사이버 보안 매트릭스(RA‑01~RA‑20) 완성도 부족 | 정보보안 담당자와 회의, 취약점 점검 및 대응 절차 확정 |
| 사용성 검증 결과 미제공 | 임상·사용자 테스트 계획 수립 및 실행 단계 보고 |
| 위험 관리 파일에 ‘고(Severe)’ 위험 항목이 존재하지만 근거 데이터 부족 | 추가 안전성/효능 자료 확보 또는 설계 변경 검토 |

---

### 8. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> - Are the assumptions about likely 3등급·4등급 classification consistent with current MFDS practice for AI 영상분석 모듈?  
> - Does the source coverage (guidelines listed in [1] and action items in [2]) adequately capture all Korean‑specific evidentiary requirements, especially regarding foreign CER acceptance and cyber‑security SOPs?  
> - Identify any jurisdiction‑specific gaps (e.g., post‑market surveillance reporting, mandatory Korean clinical data) that may have been overlooked.  

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

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |

### kb-eval-20261102-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "6ba7aeec5035f661", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `6ba7aeec5035f661`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: digital medical products act impact
- Matched keywords: KGMP

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **규제 초안 – “촬영실 GUI SW”(SaMD, 독립형 의료 소프트웨어)**  

---

## 1️⃣ 등급·인허가 경로  
| 항목 | 내용 |
|------|------|
| **예상 등급** | 디지털 의료제품법·의료기기 품목별 등급 규정에 따라 위험도(진단/치료 목적, 사용 환경, AI/ML 적용 여부 등)를 평가 후 1~4등급 중 결정 필요. 현재 제공된 정보만으로는 **3등급 또는 4등급** 가능성이 높음(고위험 소프트웨어·AI 포함 시). |
| **인허가 경로** | - 3등급·4등급 → **허가(신고·인증이 아닌 MFDS 직접 허가)**<br>- 2등급일 경우는 **인증**(MFDS‑지정 심사기관) – 다만, 현재 가정에선 2등급으로 판단되지 않음. |
| **확인 필요** | - 《의료기기 품목 및 품목별 등급에 관한 규정」**제23조** 혹은 최신 고시 확인<br>- 디지털 의료제품법 시행령(2025) 내 “소프트웨어 위험도 분류 기준” 적용 여부 |

> *※ 위 등급·경로는 현 단계 추정이며, 정확한 등급 확정 전까지 “등급 미확인 – 인간 검토 필요” 로 표시하고 진행하십시오.*

---

## 2️⃣ 제출에 필요한 근거Evidence

| 구분 | 요구사항 | 주요 근거 (프레임워크) |
|------|----------|------------------------|
| **품질경영시스템** | KGMP(의료기기법 제28조) 인증 + ISO 13485:2016 적용 증명 | *ISO 13485* (framework) |
| **소프트웨어 개발·검증** | • IEC 62304 Safety Class C 전 단계 문서(SDP, SRS, SAD, SVP, SVR) <br>• 회귀 테스트 자동화, 변경관리 SOP | *IEC 62304* (framework) |
| **위험 관리** | 위험 분석·평가·통제·재평가 자료(ISO 14971 적용) | *ISO 14971* (framework) |
| **사이버보안** | Threat Model, SBOM, PCCP 통합 보고서 | *MFDS 사이버보안 가이드라인 2025* (framework) |
| **AI/ML 기능** (해당 시) | AI 위험도 평가, 사전 적합성 판단(고위험 여부), 지속적 모니터링 계획 | *디지털의료제품법*, *FDA PCCP (2024‑12‑03)*, *EU AI Act Reg. 2024/1689* (framework) |
| **불만·사후관리** | MFDS에 30일 내 보고 절차, MDR(30‑day reportable) 판단 기록 | *MFDS 보고* (framework) |
| **UDI·라벨링** | 한국어 라벨·사용설명서(IFU) 작성, UDI 부여 및 관리 | *MFDS 고시* (구체적 번호는 소스에 없음 → 별도 확인 필요) |
| **임상 평가** | 디지털 의료제품법에 따른 임상 데이터(필요 시 현지 임상시험 또는 해외 CE/FDA 허가 자료 활용) | *디지털의료제품법* (framework) |
| **제조·유통 계약** | 계약멸균·재라벨링·외국 초기 유통업체 포함 QMSR 적용 증명(§820.10(a) 참고) | *21 CFR §820.10(b)*, *§820.35* (instance identifier – 외국 규정) |
| **KGMP 시설 인증** | 제조 시설 KGMP 적합성 인정서(2026‑07‑01 개편 후 최신 요건) | *KGMP* (framework) |

> **※ 위 목록은 현 소스에서 확인된 주요 요구사항이며, 실제 제출 시 추가·보완이 필요할 수 있습니다.**

---

## 3️⃣ 현재 누락·불명확 정보  

| 항목 | 구체적인 결함 |
|------|---------------|
| **제품 의도·사용자** | 상세한 적응증·사용 환경·대상 사용자(전문의, 방사선과 등) 미기재 |
| **위험도 분류 근거** | IEC 62304 Class C 지정 이유와 MFDS 위험도 매트릭스 매핑 자료 부재 |
| **AI/ML 적용 세부** | 알고리즘 종류·학습 데이터·성능 검증 방식·변경 관리 계획이 없음 |
| **임상 평가 범위** | 현지 임상시험 여부, 기존 FDA 510(k) 혹은 CE 마크 이용 가능성 명시 안 됨 |
| **제조·품질 인증 현황** | KGMP 시설인증서 사본·제조공정 흐름도 미제공 |
| **라벨·IFU 번역** | 한국어 라벨·사용설명서 초안 부재 (언어 요건 충족 여부 불투명) |
| **사이버보안 상세 계획** | Threat Model, SBOM, PCCP 결과물 샘플이 없음 |
| **불만·시판후조사 절차** | MFDS 30일 보고 프로세스에 대한 SOP 초안 미제공 |
| **UDI 부여·관리 체계** | UDI 부여 전략 및 데이터베이스 연동 방안 누락 |

---

## 4️⃣ 핵심 위험 통제·보완 조치  

1. **소프트웨어 안전 클래스 C 대응** – IEC 62304에 따른 설계/개발 단계별 검증 절차, 코드 리뷰, 자동화 회귀 테스트 도입.  
2. **사이버 보안** – MFDS 사이버보안 가이드라인 2025에 따라 위협 모델링 수행 → SBOM 작성 → PCCP(Patient‑Centric Cybersecurity Program) 문서화.  
3. **AI/ML 고위험 관리** – AI Act 고위험 요건 대비, 사전 위험도 평가와 재검증 계획 수립(알고리즘 업데이트 시 재적합성평가 면제 여부 검토).  
4. **불만·시판후조사** – MFDS 보고 규정에 따라 30일 내 신고 체계 구축, MDR reportable 판단 기준을 QMS 절차서에 명시.  
5. **ARR(Applicable Regulatory Requirements) 통합** – 미국 21 CFR §820.10(b), §820.35(a) 등 외국 ARR 항목을 KGMP ARR 항목에 매핑해 QMS SOP에 포함.  

---

## 5️⃣ 인용·출처 정리  

| 구분 | 출처 |
|------|------|
| **프레임워크** | ISO 13485:2016, IEC 62304 (Safety Class C), IEC 62366‑1:2020, MFDS 사이버보안 가이드라인 2025, 디지털의료제품법, KGMP(의료기기법 제28조) |
| **인스턴스 식별자** | 21 CFR §820.10(b), 21 CFR §820.35(a), 21 CFR §820.35 (미국 FDA QSR 조항) – 소스 [1] 에서 직접 언급 |
| **기타** | “MFDS 보고”·“디지털의료제품법 연계” 등 구체적 고시 번호는 소스에 없음 → **별도 확인 필요** |

---

## 6️⃣ 인간‑에스컬레이션(Review) 트리거  

| 상황 | 에스컬레이션 대상 |
|------|-------------------|
| 등급 ※확정 불가| 책임자·규제팀 리드 – 최종 등급 판단 전까지 진행 보류 |
| AI/ML 기능 포함 ※위험도·검증 미비| AI 전문팀·법무팀 – 고위험 AI 규정(AI Act, FDA PCCP) 적용 여부 검토 |
| 현지 임상 데이터 필요 | 임상연구 담당자 – 국내 임상시험 계획서(BRP) 수립 및 IRB 승인 |
| KGMP 시설 인증 미획득 | 제조/품질팀 – KGMP 적합성인증 절차 가속화 |
| 사이버보안 산출물(Threat Model, SBOM) 부재 | 정보보호·CTO – 보안팀에 즉시 요구 |
| UDI·라벨링·IFU 한국어 번역 미완료 | 마케팅·법무 – 라벨·사용설명서 초안 작성 및 검증 |
| ARR(미국 820 조항)와 MFDS 요건 매핑이 불분명 | 규제컨설턴트·법률고객 – 매핑 가이드라인 추가 조사 |
| 제출 기한 4주 이내에 모든 결함 해소되지 않을 경우 | 프로젝트 관리자 – 일정 재조정 및 리스크 보고 |

---

## 📌 최종 판단  

- **제품은 현재 3등급 또는 4등급**으로 추정되며, **허가(신고·인증이 아닌 MFDS 직접 허가) 경로**를 준비해야 한다.  
- 위 **누락 정보와 위험 통제**를 보완한 뒤, **KGMP 인증**, **한국어 라벨·IFU**, **UDI 부여**, **사이버보안 및 AI/ML 고위험 대응**을 모두 충족시켜야 허가 가능성이 확보된다.  

> **에스컬레이션 필요 사항은 표 6‑항목을 기준으로 즉시 담당자에게 전달하십시오.**

---

### 🤝 Peer‑Review Prompt  
다음 동료 RA에게 검토를 요청합니다.

1. 제시된 등급·인허가 경로 가정이 디지털 의료제품법 최신 해석과 일치하는가?  
2. 소스[2]에 나타난 “DG → MDR” 매핑이 실제 MFDS 요구사항(ARR 포함)과 정확히 연결됐는지 여부.  
3. AI/ML 기능 적용 시 추가로 필요한 국내 임상·안전성 자료가 누락되지 않았는지 확인해 주세요.  
4. 사이버보안 가이드라인 2025에 대한 구체적 산출물(Threat Model, SBOM) 요구 수준이 충분히 반영됐는지 의견을 부탁합니다.

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

> ① PCCP를 "Patient-Centric Cybersecurity Program"으로 전개 — Predetermined Change Control Plan의 오전개 ② 등급 규정 "제23조" 근거 없는 조번 ③ "MDR(30-day reportable)" FDA-MDR 개념의 MFDS 보고 행 병입(관할 혼입 경미) ④ "BRP" 비표준 용어.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261102-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "15a5c15b4ecd34b2", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `15a5c15b4ecd34b2`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-22_SBOM_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%A0%95%ED%95%A9%EC%84%B1.md)
- Source hash: `00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `2026-04-22_SBOM_디지털의료제품법_정합성.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMD...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital‑Medical‑Product Act (디지털의료제품법) Impact Assessment for the X‑ray System Project**

| Item | Korean grade (1~4등급) | Submission track* | Core evidence required | Gaps / missing information |
|------|------------------------|-------------------|-----------------------|----------------------------|
| **Generator firmware** (HW control only, no network) | 1등급 (non‑medical‑device) – not covered by 디지털의료제품법 | 신고 | None (software excluded from medical‑device scope) | Confirmation of “non‑connected” status; declaration that the firmware does not affect clinical performance. |
| **Detector firmware** (potentially network‑enabled) | △ – conditional 2등급/3등급 | • If classified as a medical device → 2등급 ⇒ 인증 (MFDS‑designated 심사기관) <br>• If 3등급 or higher → 허가 (direct MFDS review) | ‑ Functional safety data (IEC 60601‑1)<br>‑ Cybersecurity & SBOM (RA‑07 항목) <br>‑ Risk management file (ISO 14971:2019) | Intended use description (does network connectivity alter clinical function?)<br>‑ Decision whether the firmware constitutes SaMD. |
| **Acquisition Workstation software** (stand‑alone, networked, AI possible) | 3등급 – SaMD that performs image acquisition & limited analysis (AI‑enabled) | 허가 (MFDS approval) | ‑ Clinical performance data (local or accepted foreign CER)<br>‑ Risk management file (ISO 14971:2019)<br>‑ KGMP‑compliant development environment<br>‑ SBOM compliance per MFDS guidance (RA‑07) – SPDX 2.3 or CycloneDX 1.5 format <br>‑ Korean IFU & labeling (language requirement) | Detailed AI algorithm description, intended clinical claim, and any required local clinical study. |
| **Image post‑processing / AI analysis module** (SaMD + AI) | 4등급 – high‑risk SaMD performing diagnostic support | 허가 (MFDS approval) | ‑ Clinical validation data (prospective/retrospective study)<br>‑ Robust risk management, including “learning” algorithm controls (ISO 62366‑1, IEC 82304‑2)<br>‑ SBOM (RA‑07) in SPDX 2.3 or CycloneDX 1.5<br>‑ Korean language labeling & IFU <br>‑ KGMP certification for software development | Confirmation of intended use (diagnostic vs. adjunct); evidence that AI performance meets safety thresholds; post‑market surveillance plan (시판후조사). |
| **DICOM transmission / PACS integration** (communication function) | △ – borderline medical device (depends on whether it merely transports data or adds clinical functionality) | • If purely transport → 1등급 신고 <br>• If adds interpretation/decision support → 2‑4등급 (인증/허가) | ‑ Functional description of added value<br>‑ Cybersecurity & SBOM compliance (RA‑07) | Precise functional scope; determination whether “communication” qualifies as a medical device under 디지털의료제품법. |

\*Submission tracks per Korean classification:  
- **1등급 → 신고**  
- **2등급 → 인증** (technical review by MFDS‑designated 심사기관)  
- **3~4등급 → 허가** (MFDS direct approval)

---

### 1. Classification & Submission Pathway

* The digital‑medical‑product law aligns with MFDS’s “의료기기 품목 및 품목별 등급에 관한 규정”. Each software component must be examined for clinical purpose, risk to patient, and whether it performs a medical function (SaMD).  
* Components that are purely hardware control without network or clinical impact (Generator) fall outside the scope → 1등급 신고.  
* Network‑enabled firmware that could affect acquisition parameters may become a medical device (2~3등급) – **decision point**: confirm whether connectivity changes clinical performance.  
* Stand‑alone acquisition software with AI is SaMD; Korean guidance classifies such systems as **3등급** when risk is moderate, but if the AI provides diagnostic conclusions → **4등급**.  

### 2. Required Evidence (per MFDS & International Frameworks)

| Requirement | Reference (framework) | Source citation |
|-------------|-----------------------|-----------------|
| **Risk Management** – ISO 14971:2019 compliance | ISO 14971 (2019) | — |
| **Cybersecurity / SBOM** – SPDX 2.3 or CycloneDX 1.5, RA‑07 항목 | MFDS guidance (RA‑07) as noted in the SOP‑SBOM‑001 v0.1 | 【1】 |
| **Clinical Evaluation** – Acceptance of foreign CER (if applicable) or local clinical data | MFDS notice expanding foreign CER acceptance (date 2025‑01‑10) – specific notice number not provided in source | no specific identifier found in source — verify separately |
| **KGMP certification** for software development environment | KGMP (의료기기법 제28조) | — |
| **Korean labeling & IFU** – Korean language requirement, format per MFDS 고시 제16조 SBOM 관리 (security guidance) | MFDS 고시 제16조 (SBOM 관리) | 【1】 |
| **Post‑Market Surveillance** – 시판후조사 plan aligned with MFDS 고시 | MFDS 고시 (post‑market) | — |

### 3. Missing / Unconfirmed Information

1. **Exact intended use statements** for each firmware/software element (especially Detector firmware and DICOM/PACS module).  
2. **Risk classification rationale** – justification per “의료기기 품목 및 품목별 등급에 관한 규정”.  
3. **Clinical performance data** or foreign CER reference numbers (e.g., FDA 510(k) predicate, CE‑mark) for acquisition workstation and AI analysis module.  
4. **KGMP compliance evidence** – facility certificates, QMS documentation.  
5. **Full SBOM artifact** – the actual SPDX 2.3 / CycloneDX 1.5 file covering all software components.  

### 4. Risk Controls & Cybersecurity Measures

* Adopt MFDS‑recommended **SBOM management (RA‑07)** – maintain version‑controlled SPDX/CycloneDX documents; integrate into development lifecycle.  
* Implement **secure boot, code signing, and runtime integrity checks** per IEC 62304 and IMDRF N73 cybersecurity principles.  
* Conduct **vulnerability scanning & patch management** aligned with NTIA 7‑element baseline (as referenced for FDA/MDR/MFDS).  
* Define a **post‑market vulnerability response plan** (Section 524B style) to satisfy both pre‑market and post‑market security obligations.

### 5. Human‑Escalation Triggers

| Trigger | Action |
|---------|--------|
| Unclear classification of Detector firmware or DICOM module | Escalate to senior RA for formal “medical‑device scope” determination (MFDS 품목별 등급 규정). |
| Absence of SBOM in required SPDX/CycloneDX format | Pause submission; request generation of compliant SBOM from development team. |
| No local clinical data or accepted foreign CER identified | Initiate feasibility study for local clinical validation or seek MFDS waiver (if applicable). |
| KGMP certification not yet obtained for software development site | Escalate to manufacturing compliance lead; defer filing until KGMP is confirmed. |
| Korean IFU/labeling draft incomplete | Route to regulatory‑writing team for language review before dossier assembly. |

---

### 6. Regulatory Judgment (Summary)

- **Generator firmware**: 1등급 → 신고 (no further evidence).  
- **Detector firmware**: conditional 2~3등급 – requires clarification of network‑enabled functions; prepare risk file and SBOM.  
- **Acquisition workstation software**: 3등급 SaMD → 허가, with full clinical evaluation, KR‑language IFU, KGMP, SBOM, and risk management.  
- **AI post‑processing module**: likely 4등급 SaMD (diagnostic) → 허가; needs robust AI validation data, post‑market surveillance plan, and stringent cybersecurity controls.  
- **DICOM/PACS integration**: classification to be decided; if only transport → 1등급 신고; otherwise treat as 2~3등급 with corresponding evidence.

All components must satisfy MFDS SBOM guidance (RA‑07) using SPDX 2.3 or CycloneDX 1.5 per the SOP‑SBOM‑001 v0.1, and comply with KGMP for software development.  

---

**Peer Review Prompt**

> @RA‑colleague: Please review the above classification assumptions, especially the split between 2등급 인증 vs 3~4등급 허가 for the Detector firmware and DICOM integration. Verify whether the source excerpts fully support the risk‑based grading or if additional Korean 규정 (e.g., “의료기기 품목 및 품목별 등급에 관한 규정”) need to be consulted. Also check that all cited MFDS references are accurate given the limited identifiers in the source and flag any missing notice numbers or article citations that require verification.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

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

> ① "Korean labeling & IFU — format per MFDS 고시 제16조 SBOM 관리" — 라벨링 형식과 SBOM 보안지침의 부자연스러운 결합(식별자 오배선) ② 외국 CER 인정 고시 날짜 '2025-01-10' — 동일 소스의 사이버보안 가이드라인 날짜 오전용 ③ Generator '1등급(비의료기기)→신고' 자기모순적 서술. / **1점 확정**: ① 'MFDS notice expanding foreign CER acceptance (2025-01-10)' — 동일 소스의 사이버보안 가이드라인 날짜 오전용 ② 'Korean labeling & IFU format per 고시 제16조 SBOM 관리' — 라벨링 형식과 SBOM 보안지침 식별자 오결합 ③ 'Korean guidance classifies such systems as 3등급...' 등 근거 없는 등급 규칙 서술(창작) ④ Generator '1등급(비의료기기)→신고' 자기모순. 체계적 식별자 오결합+규칙 창작 → 정정 필요.

**Source Excerpts**

1. Chunk `1055466385786976527`

> ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMDRF N73 원칙 | NTIA 7요소 + License + Hash | NB 심사 자료 | PMS Plan/PSUR 포함 | | MFDS (2025-01-10) | 국내 허가 심사 | 권고 (SPDX/CycloneDX) | RA-07 항목 | 심사 자료 (권고) | 보안 지침 제16조 SBOM 관리 | **정합성 판정: 본 SOP-SBOM-001 v0.1은 3축 모두 수용 가능한 상위 호환 설계** - SPDX 2.3 또는 CycloneDX 1.5 채택 → FDA/MDR/MFDS 동시 만족 - NTIA Baseli...

2. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

### kb-eval-20261102-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "50fa5ea422b41891", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `50fa5ea422b41891`
- Source: `github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week02_MFDS_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b`
- Focus: digital medical products act impact
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `Week02_MFDS_체계_상세.md`는 `Week02_MFDS_체계_상세.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 --- ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|------...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on a SaMD‑type digital health device**

---

### 1️⃣ Classification & Submission Route  

| Step | Korean regulatory requirement | Typical pathway for a SaMD |
|------|------------------------------|----------------------------|
| **Device grade** | Must be determined from the *“의료기기 품목 및 품목별 등급에 관한 규정”* (MFDS_인허가_상세가이드.md §2). The source does not specify a grade for this SaMD. | *No specific identifier found in source – verify separately.* |
| **1~4등급 → route** | • 1등급 → 신고  <br>• 2등급 → 인증 (technical‑document review by an MFDS‑designated 심사기관)  <br>• 3·4등급 → 허가 (full MFMF approval) | If the device falls into **2등급** → submit for **인증** to a designated 심사기관 (e.g., KTL, KTR, TÜV SÜD Korea, etc.).<br>If **3등급·4등급** → pursue **허가** with MFDS. |

> **Action:** Confirm the exact grade before selecting the submission track.

---

### 2️⃣ Required Evidence for a SaMD (post‑2025 디지털의료제품법)

| Category | Mandatory items (Korean law / guidelines) | Reference framework |
|----------|-------------------------------------------|---------------------|
| **KGMP (Good Manufacturing Practice)** | • GMP 적합인증 (valid 3 years, renewal required). <br>• Inspection report & corrective‑action plan for any Critical/Major findings. | MFDS 고시 5.2 GMP 적합인정 절차 (see source [1]) |
| **Risk Management** | • Risk analysis & control per ISO 14971 (2019). <br>• Hazard mitigations documented in a risk‑management file (RMF). | ISO 14971:2019 |
| **Software Lifecycle** | • IEC 62304 (2006+A1:2015) compliance – design, verification, validation. | IEC 62304 2006+A1:2015 |
| **Usability / Human‑Factors** | • IEC 62366‑1 (2015+A1:2020) usability engineering process. | IEC 62366‑1 2015+A1:2020 |
| **Clinical Evidence** | • Clinical Evaluation Report (CER) that meets MFDS 디지털의료기기 가이드라인 (AI/ML 기반 GUI SW, 2025‑05‑07). <br>• If the device is a novel algorithm, prospective or retrospective clinical data per the guideline. | MFDS 디지털의료기기 가이드라인 6종 (source [2]) |
| **Labeling & IFU** | • Korean language labeling, device name, intended use, precautions, contraindications, and post‑market surveillance plan. | MFDS 라벨링 규정 (standard) |
| **Cybersecurity** | • Conformity to MFDS 사이버보안 가이드라인 (referencing IEC 81001‑5‑1 2021). | IEC 81001‑5‑1 2021 |
| **Performance Certification (future)** | • For autonomous performance certification (planned 2026), a pre‑certification dossier may be required. | Upcoming regulation note (source [2]) |

---

### 3️⃣ Missing Information (to be obtained from the sponsor)

| Item | Why it matters |
|------|----------------|
| **Exact device grade (1~4등급)** | Determines whether the route is 신고/인증/허가. |
| **Intended use statement & risk classification rationale** | Required for the RMF and to justify the grade. |
| **Clinical data scope (local vs. foreign) and any existing CE/FDA clearance** | MFDS may accept foreign CERs only under specific notice; clarification needed. |
| **Cybersecurity architecture details** | Needed to satisfy MFDS 사이버보안 가이드라인. |
| **Change‑management plan** – whether anticipated modifications fall under the “네거티브 방식 변경허가제” (important vs. minor changes). | Determines if pre‑approval is required for future updates. |
| **Selection of 심사기관** – sponsor’s preference and any prior relationship with NIDS. | NIDS can now perform GMP 적합판정 (source [1] & [2]). |

---

### 4️⃣ Core Risk Controls to be Demonstrated

1. **Hazard identification & risk analysis** per ISO 14971 (2019).  
2. **Software verification & validation** aligned with IEC 62304 (2006+A1:2015).  
3. **AI/ML algorithm transparency & performance monitoring** as required by the 2025‑05‑07 MFDS AI/ML guideline.  
4. **Usability engineering** (IEC 62366‑1) to mitigate use errors in the GUI.  
5. **Cybersecurity safeguards** – authentication, data integrity, intrusion detection per IEC 81001‑5‑1 (2021).  
6. **Post‑market surveillance (시판후조사)** plan with predefined vigilance reporting thresholds.

---

### 5️⃣ Citations

| Content | Source excerpt |
|---------|----------------|
| GMP 적합인증 절차 (신청 → 현장조사 → 결함 통보 → 시정 조치 제출 → 적합인정서 발급) | **[1]** Chunk 1078228256164017760 |
| NIDS begins digital‑medical‑device GMP assessment (effective 2025‑01‑24) | **[1]** same chunk |
| Major regulatory changes 2025–2026 – Digital Medical Products Act, AI/ML guideline release, upcoming autonomous performance certification & negative‑change regime | **[2]** Chunk 1121184088796802935 |

*Framework references (ISO/IEC numbers) are stated as facts and do not require a source identifier.*

---

### 6️⃣ Human–Escalation Triggers  

| Trigger | Required action |
|--------|----------------|
| **Critical or Major GMP finding** during NIDS/KTL inspection | Immediate corrective‑action submission; escalation to senior QA & possible temporary halt of manufacturing until resolution. |
| **Classification determined as 3등급·4등급** | Initiate full 허가 dossier and submit to MFDS; involve regulatory affairs lead for timeline management. |
| **Proposed device change classified as “중요 변경” under the negative‑change regime** (source [2]) | Submit change‑approval application *before* implementation; suspend release until approval. |
| **AI/ML algorithm update that alters performance metrics** | Conduct supplemental clinical evaluation and submit revised CER; trigger internal review board sign‑off. |
| **Cybersecurity incident affecting patient data** | Activate incident‑response plan, notify MFDS per 사이버보안 가이드라인, and report to the Ministry of Health & Welfare within 24 h. |
| **Expiry of KGMP 적합인증 (3‑year term)** | Begin renewal preparation ≥6 months before expiry; if not renewed, suspend distribution. |

---

### 7️⃣ Peer Review Prompt  

> **To a fellow RA colleague:**  
> Please examine the assumptions made about the device’s grade and the applicability of the AI/ML guideline to this SaMD. Have we captured all necessary Korean‑specific evidence gaps (e.g., local clinical data, cybersecurity documentation) given the source excerpts? Are there any additional MFDS notices or decree numbers that should be cross‑checked before finalizing the submission strategy?

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

> "보건복지부 24시간 내 보고" — 소스에 근거 없는 수치(10-29 kr-005 'MFDS 24시간'과 동일 계열 재발). 나머지(NIDS·심사기관 6개·2025-05-07 가이드라인)는 소스 정합. 부수: "full MFMF approval" 오타.

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---

### kb-eval-20261102-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-02", "decision_ref": "kb-eval-20261102-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "f07d36317376f55b", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md", "source_hash": "eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f07d36317376f55b`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-24_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EC%A0%95%ED%95%A9%EC%84%B1.md)
- Source hash: `eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `2026-04-24_디지털의료제품법_요구사항_정합성.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버 ### 3.2 불일치·공백 항목...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **디지털 의료기기 규제 검토 – 한국(MFDS) 적용 초안**

---

### 1. 제품·법적 정의
* **대상** : 소프트웨어 기반 디지털 의료제품(예: 독립형 진단‑지원 앱).  
* **관련 법령** : *의료기기법* + *디지털의료제품법* (양립 적용).  

> **주의** – 제품이 “의료기기로” 인정되는지, 혹은 “비의료 디지털헬스 서비스(보건복지부 산하)”로 분류되는지는 사전 확인 필요.  

---

### 2. 등급·허가 경로 판단
| 단계 | 내용 |
|------|------|
| **등급** | 현재 출처에 등급 명시 없음 → 「의료기기 품목 및 품목별 등급에 관한 규정」(MFDS_인허가_상세가이드.md §2) 에서 해당 제품군을 검토 후 **1~4등급** 중 판단 필요. |
| **예상 시나리오** | 디지털 진단·치료용 소프트웨어는 대부분 **3등급** 또는 **4등급**에 배정됨 (고위험, 임상의 직접 사용). <br>※ 등급 확정 전까지 *등급 미확정*으로 표시. |
| **허가 경로** | 3등급·4등급 → **허가(인증·승인) 절차** : MFDS 직접 심사 (허가 신청서, 기술문서, 임상시험·평가 자료 등). <br>※ 2등급이면 **인증**이지만 현재는 3~4등급 가정. |
| **필수 사전 요건** | *KGMP* 인증(의료기기법 제28조) 및 *MFDS 보안지침* 적용 (특히 제16조). |

> **Human‑Escalation Trigger ①** – 등급 미확정 시, 즉시 규제 담당자와 제품·용도 전문가 회의를 소집하여 등급 확정을 요청한다.

---

### 3. 제출에 요구되는 근거 서류·증거

| 구분 | 요구 내용 (한국 기준) | 대응 현황(출처) | 비고 |
|------|--------------------|---------------|------|
| **기술문서** | 설계·제조·시험 기록, 위험관리 파일 등 | 전반적 커버는 “DR‑21(ISO 14971)” 및 “DR‑22(IEC 62304)”에 부합 (출처①) | – |
| **위험관리** | ISO 14971 적용 → 위험 식별·분석·통제·검증 | DR‑21(ISO 14971) ‑ 전면 커버 (출처①) | – |
| **소프트웨어 생명주기** | IEC 62304 준수, SW 버전 관리, 개발 단계 산출물 | DR‑22(IEC 62304) ‑ 전면 커버 (출처①) | – |
| **사용성·적합성** | IEC 62366‑1 기반 사용성 평가 계획서 | 현재 “DR‑06(IEC 62366‑1 사용적합성 계획서 템플릿 미정)”가 **불일치/공백(P1)** (출처②) | ‡ |
| **보안·SBOM** | MFDS 보안지침 제16조에 의거 SBOM 제출 | “DR‑09(SBOM)” 전면 일치 (출처①) | – |
| **UDI** | 의료기기법 + 디지털의료제품법 연계 UDI 발급·라벨링 | DR‑19(UDI) 커버 (출처①) | 라벨 템플릿 미작성 → “DR‑10(P1)” (출처②) |
| **품질경영(KGMP)** | KGMP 적합판정 신청서 초안 필요 | “DR‑02(부분) – GMP 적합판정 신청서 초안 미작성” (P1) (출처②) |
| **임상/성능평가** | 디지털 의료기기에 따라 국내 임상 데이터 요구 여부 | 현 단계에서 *국내 임상* 요구 여부 확인 필요 (법령·제조‑품목 별 검토) | – |
| **데이터 무결성** | ALCOA+ 원칙 적용 SOP | “DR‑31(P1)” – SOP 부재 (출처②) |
| **AI 투명성·공정성** | AI 설명성·공정성 평가 문서 | “DR‑32/33(P1)” – 문서 없음 (출처②) |
| **사후학습·드리프트 거버넌스** | 모델 업데이트, 성능 drift 감시 체계 | “DR‑35(P0)” – 전면 부재 (출소②) |
| **이상사례 보고** | PMS 고시에 따른 사건/이상 사례 보고 절차 및 템플릿 | “DR‑14”와 “PMS 고시” 연계 일치 (출처①) | – |

> **Framework citations** (no verification caveat)  
* ISO 14971:2019, IEC 62304:2006+A1:2015, IEC 62366‑1:2015+A1:2020, MFDS 보안지침 제16조, 의료기기법, 디지털의료제품법.  

> **Instance identifiers** – appear only as cited above (e.g., “MFDS 보안지침 제16조”). No other specific notice numbers were provided; for items lacking a concrete identifier the draft notes *“no specific identifier found in source — verify separately.”*

---

### 4. 현 단계에서 파악된 주요 결함(불일치·공백) 및 조치 필요사항

| Req‑ID | 결함 요약 | 우선도 | 요구되는 문서/절차 | 비고 |
|--------|-----------|------|-------------------|------|
| DR‑05 | **구성요소 성능평가 SOP 부재** | P0 | 구성품별 성능시험 표준운영절차(SOP) 작성 | 즉시 초안 마련, 품질팀 검토 |
| DR‑10 | **디지털 의료기기 표시기재 템플릿 미작성** | P1 | 라벨·IFU(한국어) 템플릿 및 UDI 매핑 표준화 | 라벨팀에 전달 |
| DR‑11 | **독립형 SW 사용적합성 평가 절차 부재** | P1 | 독립형 소프트웨어 사용성/안전성 평가 계획서 | 위험관리와 연계 |
| DR‑15 | **자율성능인증 신청 플레이북 부재** | P0 | 자율·AI 기반 의료기기 인증 가이드라인 초안 | AI 팀 협업 필요 |
| DR‑31 | **데이터 무결성(ALCOA+) SOP 부재** | P1 | 임상/연구 데이터 관리 SOP (ALCOA+ 원칙) | 품질팀 담당 |
| DR‑32/33 | **AI 설명·공정성 평가 문서 없음** | P1 | AI 투명성·공정성 보고서 및 검증 절차 | 윤리·법무 협업 |
| DR‑35 | **사후학습·드리프트 거버넌스 없음** | P0 | 모델 업데이트, 성능 drift 모니터링 프로세스 | R&D와 데이터 사이언스팀 연계 |
| DR‑02 (부분) | **GMP 적합판정 신청서 초안 미작성** | P1 | KGMP 인증 신청서 초안 | 규제담당자 작성 후 검토 |
| DR‑04 (부분) | **PCCP 결정트리 미확정** | P1 | 위험 등급·분류 기준(제품·사용 환경) 결정 트리 | 내부 회의 필요 |
| DR‑06 (부분) | **IEC 62366‑1 사용적합성 계획서 템플릿 미정** | P1 | IEC 62366‑1 기반 사용성 평가 계획서 템플릿 | 사용자경험(UX)팀 협조 |

#### 우선순위 정의
* **P0** – 제품 출시·승인에 직결되는 핵심 결함. 48시간 내 전담 담당자에게 알리고, 상위 관리자(규제/품질 부서장) 승인을 받아 즉시 조치.
* **P1** – 규제 요구사항 충족을 위해 반드시 해결해야 할 항목. 2주 이내 초안 작성·검토 완료 목표.

> **Human‑Escalation Trigger ②** – 위 P0 항목(특히 DR‑05, DR‑15, DR‑35) 중 하나라도 일정 내 미완료 시, 즉시 규제팀 책임자 및 CEO에게 보고하고 보류/중단 결정을 요청한다.  

---

### 5. 위험관리·보안대응 매핑 (ISO 14971 ↔ MFDS 요구)

| ISO 14971 단계 | 적용 현황 | MFDS 연계 항목 |
|----------------|-----------|----------------|
| **위험 식별** | 제품 기능·AI 알고리즘 위험 목록 보유 | DR‑05(성능평가), DR‑32/33(AI 투명성) |
| **위험 분석** | FMEA, HA (사용자 오류 포함) 수행 중 | DR‑11(사용적합성) |
| **위험 통제** | 설계·보호조치 (예: 데이터 암호화, 접근 제어) 적용 | MFDS 보안지침 제16조 (DR‑09) |
| **통제 검증** | 시험/시뮬레이션으로 효과 확인 | DR‑22(IEC 62304), DR‑21(ISO 14971) |
| **위험 관리 리뷰** | 주기적(6개월) 위험 재평가 미설정 → **DR‑35** (사후학습·드리프트 거버넍스) 보완 필요 |  |

> **보안 강화** – SBOM 및 사이버 위협 모델링이 현재 “전면 일치”(DR‑09)로 확인되었으나, *추가* 사후 학습 시 발생 가능한 코드 변경에 대한 SBOM 업데이트 절차를 SOP화해야 함 (연결: DR‑35).

---

### 6. 제출용 체크리스트(요약)

| 구분 | 준비 여부 | 비고 |
|------|-----------|------|
| KGMP 인증증명서 | ☐ | 등급·허가 경로에 따라 필수 |
| MFDS 보안지침 제16조 대응 SOP (SBOM 포함) | ✅ (DR‑09) | 유지·업데이트 절차 필요 |
| 위험관리 파일 (ISO 14971) | ✅ (DR‑21) | 최신화 필요 (P0/1 결함 반영) |
| 소프트웨어 생명주기 문서 (IEC 62304) | ✅ (DR‑22) | – |
| 사용성·적합성 계획서 (IEC 62366‑1) | ❌ (DR‑06, DR‑11) | 템플릿·초안 작성 필요 |
| UDI 라벨/IFU 한국어 버전 | ❌ (DR‑10) | 라벨 템플릿 제작 |
| AI 설명·공정성 평가 보고서 | ❌ (DR‑32/33) | 별도 문서 필요 |
| 데이터 무결성 SOP (ALCOA+) | ❌ (DR‑31) | – |
| 사후학습·드리프트 거버넌스 정책 | ❌ (DR‑35) | – |
| GMP 적합판정 신청서 초안 | ❌ (DR‑02) | – |
| PCCP(제품·위험 등급 결정트리) | ❌ (DR‑04) | – |

---

### 7. Human‑Escalation Triggers Summary
1. **등급 미확정** → 즉시 규제 담당자와 제품 전문가 회의 (Trigger ①).  
2. **P0 결함(DR‑05, DR‑15, DR‑35 등) 일정 초과** → 48시간 내 상위 관리자·CEO 보고 후 프로젝트 중단/보류 검토 (Trigger ②).  
3. **KGMP 인증 및 GMP 신청서 미제출** → 허가 접수 전까지 진행 불가, 담당자에게 일일 리마인드.  

---

### 8. Peer‑Review Request
> *Please review the assumptions made regarding the likely grade (3등급/4등급) and the mapping of the identified gaps to MFDS 보안지침·PMS 고시 requirements. Verify whether any additional foreign evidence (e.g., FDA 510(k) predicate, CE marking CER) could be leveraged under recent MFDS scope expansions, and flag any jurisdiction‑specific elements that may have been omitted.*  

--- 

*End of draft – all citations derived directly from the provided source excerpts; no invented notice or article numbers are included.*

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

1. Chunk `1091162552456558927`

> ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버

2. Chunk `434223568197517474`

> ### 3.2 불일치·공백 항목 | Req-ID | 불일치 유형 | 내용 | 우선도 | |---|---|---|---| | DR-05 | 공백 | 구성요소 성능평가 SOP 부재 | P0 | | DR-10 | 공백 | 디지털의료기기 표시기재 템플릿 미작성 | P1 | | DR-11 | 공백 | 독립형 SW 사용적합성 평가 절차 부재 | P1 | | DR-15 | 공백 | 자율성능인증 신청 플레이북 부재 | P0 | | DR-31 | 공백 | 데이터 무결성(ALCOA+) SOP 부재 | P1 | | DR-32/33 | 공백 | AI 설명성·공정성 평가 문서 없음 | P1 | | DR-35 | 공백 | 사후학습·드리프트 거버넌스 없음 | P0 | | DR-02 | 부분 | GMP 적합판정 신청서 초안 미작성 | P1 | | DR-04 | 부분 | PCCP 결정트리 미확정 | P1 | | DR-06 | 부분 | IEC 62366-1 사용적합성 계획서 템플릿 미정 | P1 |
