# KB Eval Checksheet - 2026-07-15 Iteration 12

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260715-it12-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_us-001", "iteration": 12, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "77d7e4f4d875cc51", "source": "github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md", "source_hash": "efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `77d7e4f4d875cc51`
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

### kb-eval-20260715-it12-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_us-002", "iteration": 12, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "5963be4cc1f41a4a", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "a622ee7076c4fd98e60854417742c547284a2a3b0d82065d9b4e2a9da67c1fab"} -->

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

### kb-eval-20260715-it12-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_us-003", "iteration": 12, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "7af4385337bceb92", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md", "source_hash": "97de49bbadccdb15a9e8d69e565d0f20cece9e4b2fdc5ab69791a845de2ad377"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `7af4385337bceb92`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_05_Software_Section.md)
- Source hash: `97de49bbadccdb15a9e8d69e565d0f20cece9e4b2fdc5ab69791a845de2ad377`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_05_Software_Section.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. --- | IEC 62304 프로세스 단계 | 생성 eSTAR 문서 | |--...
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

1. Chunk `1023300943338888510`

> ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. ---

2. Chunk `158289574441238809`

> | IEC 62304 프로세스 단계 | 생성 eSTAR 문서 | |---|---| | 5.1 Software Development Planning | Dev & Config Management, Software Description | | 5.2 Requirements Analysis | SRS | | 5.3 Architectural Design | Software Description, Architecture Chart, Risk Management File | | 5.4 Detailed Design | SDS (Enhanced only) | | 5.5 Unit Implementation & Verification | Dev & Config Management, Testing Doc (Unit) | | 5.6 Integration Testing | Testing Doc (Integration) | | 5.7 System Testing | Testing Doc (System) | | 5.8 Software Release | Version History, Unresolved Anomalies | | 6 Maintenance Process | Dev & Config Management | | 7 Risk Management | Risk Mana...

### kb-eval-20260715-it12-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_us-004", "iteration": 12, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "8d3a92fcc262cd91", "source": "github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md", "source_hash": "19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8d3a92fcc262cd91`
- Source: `github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_%C2%A7820.30_subsection_citations_systemic.md)
- Source hash: `19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf`
- Focus: SaMD change impact
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md`는 `238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: `00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨. ## 배경 audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스...
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

1. Chunk `1123403925433224246`

> `00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨.

2. Chunk `152477499522968513`

> ## 배경 audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스 전반에 분산 잔존**함을 grep 점검에서 확인. eCFR 21 CFR Part 820(QMSR, 2026-02-02 시행) §820.30은 본문 전체가 Reserved이고, 설계관리 요구는 §820.10(c)가 ISO 13485:2016 §7.3을 incorporation by reference로 끌어오는 단일 경로로 일원화되었다.

### kb-eval-20260715-it12-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_us-005", "iteration": 12, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "574e48125525c91a", "source": "github:holee9/MD-process/issue-drafts/948_AUDIT_IEC81001_5_1_FDA_Cyber_2023_09_본문잔존_광범위노후.md", "source_hash": "18f2fa75926a8721e70c0a7aa5866a1e5da7b536c39a8eea720edf7b6e31ead3"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `574e48125525c91a`
- Source: `github:holee9/MD-process/issue-drafts/948_AUDIT_IEC81001_5_1_FDA_Cyber_2023_09_본문잔존_광범위노후.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/948_AUDIT_IEC81001_5_1_FDA_Cyber_2023_09_%EB%B3%B8%EB%AC%B8%EC%9E%94%EC%A1%B4_%EA%B4%91%EB%B2%94%EC%9C%84%EB%85%B8%ED%9B%84.md)
- Source hash: `18f2fa75926a8721e70c0a7aa5866a1e5da7b536c39a8eea720edf7b6e31ead3`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `948_AUDIT_IEC81001_5_1_FDA_Cyber_2023_09_본문잔존_광범위노후.md`는 `948_AUDIT_IEC81001_5_1_FDA_Cyber_2023_09_본문잔존_광범위노후.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 대상 - 문서 A: `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md` v0.3 §1 본문 L42 (frontmatter는 2026-02 Final로 정정 완료 — [audit #938] — but §1 본문은 미정정 잔존) - 문서 B: `02_품질경영시스템_QMS/SOP-CVD-001_조정된_취약점_공개_정책.md` L32 - 문서 C: `05_검사_시험_밸리데이션/X-ray_장비_안전성능_표준_매핑.md` L93 - 문서 D: `05_검사_시험_밸리데이션/외부_Pen-test_계획서_v0.1.md` L10 + L46 (2건) - 관리표: `00_프로젝트관리/문서_매트릭스.md`...
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

1. Chunk `1037058292288034000`

> ## 대상 - 문서 A: `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md` v0.3 §1 본문 L42 (frontmatter는 2026-02 Final로 정정 완료 — [audit #938] — but §1 본문은 미정정 잔존) - 문서 B: `02_품질경영시스템_QMS/SOP-CVD-001_조정된_취약점_공개_정책.md` L32 - 문서 C: `05_검사_시험_밸리데이션/X-ray_장비_안전성능_표준_매핑.md` L93 - 문서 D: `05_검사_시험_밸리데이션/외부_Pen-test_계획서_v0.1.md` L10 + L46 (2건) - 관리표: `00_프로젝트관리/문서_매트릭스.md` L172, L537 (외부_Pen-test_계획서 applicable/summary 열) - 자매재발: audit **#938** (2026-06-29, TF-TD-001 §18.5), audit **#940** (2026-07-03 close, 벤치마크_2026-Q2 3건). 두 감사 모두 close 되었으나 grep 스캔이 특정 문서군에 국한되어 위 5+건 잔존.

2. Chunk `238266956254574171`

> ### D2 — `02_품질경영시스템_QMS/SOP-CVD-001_조정된_취약점_공개_정책.md` L32 - **기재값:** `- FDA Premarket Cybersecurity Guidance(2023-09-26): SBOM·VEX·CVD plan 제출 의무` - **정답:** 2026-02 Final로 정정 + Docket 명시. SBOM/VEX/CVD 조항 위치는 신·구 판본 대응표 참조 필요(2026-02 Final Attachment 1/2).

## ra_eu

### kb-eval-20260715-it12-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_eu-001", "iteration": 12, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c24649f0779391dc", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

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

### kb-eval-20260715-it12-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_eu-002", "iteration": 12, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "cefe5efabb520900", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

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

### kb-eval-20260715-it12-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_eu-003", "iteration": 12, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d127b11ff4140383", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d127b11ff4140383`
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

### kb-eval-20260715-it12-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_eu-004", "iteration": 12, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "8901f28b2035bd5c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8901f28b2035bd5c`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/README.md)
- Source hash: `30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules) ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software...
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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20260715-it12-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_eu-005", "iteration": 12, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "5d560026db6d99ba", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

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

## ra_kr

### kb-eval-20260715-it12-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_kr-001", "iteration": 12, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5e56abfc4c099082", "source": "github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md", "source_hash": "54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5e56abfc4c099082`
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

### kb-eval-20260715-it12-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_kr-002", "iteration": 12, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "ebda78848c29a7df", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

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

### kb-eval-20260715-it12-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_kr-003", "iteration": 12, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "0b701ca933adffd1", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0b701ca933adffd1`
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

### kb-eval-20260715-it12-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_kr-004", "iteration": 12, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "a7efba22826195ec", "source": "github:holee9/MD-process/issue-drafts/956_AUDIT_디지털의료제품법_요구사항_매트릭스_DR02_조항_인용부정확.md", "source_hash": "6e02eaedc1e24e41f1a1bf208b930a59f96d8b39f382a3eeb018e5f289d2d799"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `a7efba22826195ec`
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

### kb-eval-20260715-it12-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it12-ra_kr-005", "iteration": 12, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "265221442076caef", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `265221442076caef`
- Source: `github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/014_01_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `014_01_디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 배경 디지털의료제품법은 2025-01-24 시행, 시행규칙 2025-02-28 현행. 사용적합성 자료 제출 의무화, 사이버보안 요구 확대(15→35), AI 변경관리 계획, 구성요소 단위 성능평가(2026 시행) 등 본 프로젝트(X-ray Workstation SW·AI 영상분석 모듈 가능성)에 직접 영향. 2026-04-22 교차검증에서 G2(사용적합성 증빙 미대응), G3(구성요소 평가 적용 여부 미판정), G4(RA-01~RA-20 전수 매핑 미완) 도출. ## 참고 링크 - `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` - `12_교차검증_보고서/2026-04-22_SBOM_디지털의료제...
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

1. Chunk `1061576322702878078`

> ## 배경 디지털의료제품법은 2025-01-24 시행, 시행규칙 2025-02-28 현행. 사용적합성 자료 제출 의무화, 사이버보안 요구 확대(15→35), AI 변경관리 계획, 구성요소 단위 성능평가(2026 시행) 등 본 프로젝트(X-ray Workstation SW·AI 영상분석 모듈 가능성)에 직접 영향. 2026-04-22 교차검증에서 G2(사용적합성 증빙 미대응), G3(구성요소 평가 적용 여부 미판정), G4(RA-01~RA-20 전수 매핑 미완) 도출.

2. Chunk `1016004334478948993`

> ## 참고 링크 - `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` - `12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md` - MFDS 디지털의료제품 정보 포털 (emedi.mfds.go.kr) - 국가법령정보센터 「디지털의료제품법」 - 관련 이슈: 005(GSPR 체크리스트 v0.2→v0.3), 009(사이버보안), 013(SBOM)
