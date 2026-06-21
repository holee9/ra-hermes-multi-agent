# KB Eval Checksheet - 2026-06-20 Iteration 06

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260620-it06-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_us-001", "iteration": 6, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "f0586ff2f2d79db5", "source": "gitea:DR_RnD/ra-llm-wiki/wiki/comparisons/hnvue-domestic-fda-eu-document-mapping.md", "source_hash": "5c59e6441d5d9be631628e27a975239d44bd37588f99842da530687b198d7aff"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f0586ff2f2d79db5`
- Source: `gitea:DR_RnD/ra-llm-wiki/wiki/comparisons/hnvue-domestic-fda-eu-document-mapping.md`
- Source hash: `5c59e6441d5d9be631628e27a975239d44bd37588f99842da530687b198d7aff`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA

**Evaluation Target**

- Expected work product: concise RA judgment for `510(k) predicate strategy` based on this source.
- Review primarily:
  - Focus on predicate selection, IFU scope, technical differences, and data needed to justify substantial equivalence.
  - For FDA work, check predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, and submission evidence impact as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1111207777950698510`

> --- type: comparison title: HnVUE 국내·FDA·EU 문서 매핑 created: 2026-06-08 updated: 2026-06-08 tags: [비교, 국내, fda, eu, hnvue, 문서매핑] related: [hnvue, standalone-samd-certification, mfds-digital-health-regulatory-support-division, fda, llz, qih, hnvue-eu-clinical-evaluation-roadmap, hnvue-usability-engineering-roadmap, hnvue-risk-management-file-planning, 39-DHF%20%28%EC%9D%B8%ED%97%88%EA%B0%80%29--8-09_HnVUE--135-HnVUE%20%EB%8B%A8%EB%8F%85%EC%9D%B8%EC%A6%9D%28SaMD--10hyl0s] sources: ["DHF (인허가)/09_HnVUE/HnVUE 단독인증(SaMD) 필요문서 정리 건 260422.xlsx"] --- # HnVUE 국내·FDA·EU 문서 매핑 HnVUE 단독 인증 전략은 세 규제권역이 요구하는 문서가 완전히 다르지 않지만, 같은 내용을 각기 다른 구조로 재배치해야 한다는 전제...

2. Chunk `277857177848429773`

> 국내 경로는 분류 확정과 디지털 의료제품용 기술문서 재구성이 중요하다. 미국 경로는 [[llz]]·[[qih]] 후보와 predicate 선택, eSTAR 구조, 사이버보안 제출 세트가 중심이다. 유럽 경로는 CEP·CER·문헌검색 프로토콜 등 임상문서군과 GSPR 대응이 가장 무겁다. 따라서 “하나의 마스터 문서로 세 구역을 동시에 제출”하는 접근보다는, 하나의 코어 내용에서 세 개의 포맷을 파생시키는 전략이 더 적합하다. 이 점에서 HnVUE의 문서 전략은 단일 산출물 관리보다 재사용 가능한 내용 단위 관리에 가깝다. 가장 높은 공통 재사용성은 [[iec-62304]], [[iso-14971]], [[iec-62366]] 축에서 나타나고, 가장 큰 지역별 분기는 임상평가와 사이버보안 제출 구조에서 나타난다.

### kb-eval-20260620-it06-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_us-002", "iteration": 6, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "c0330d37329d81fc", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_Threat_Model_STRIDE_가이드.md", "source_hash": "f6cd656dce2527909f6e09f1befda964ccd3a78dfad81b725a69a2d8909efe44"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c0330d37329d81fc`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_Threat_Model_STRIDE_가이드.md`
- Source hash: `f6cd656dce2527909f6e09f1befda964ccd3a78dfad81b725a69a2d8909efe44`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA

**Evaluation Target**

- Expected work product: concise RA judgment for `510(k) predicate strategy` based on this source.
- Review primarily:
  - Focus on predicate selection, IFU scope, technical differences, and data needed to justify substantial equivalence.
  - For FDA work, check predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, and submission evidence impact as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1062634304825655780`

> ### 1.3 MFDS — 2025.01 개정 가이드라인 | 문서 | 내용 | |---|---| | 의료기기 사이버보안 원칙 및 실무 (N60) | Threat Model 포함 사전검토 요구 | | 레거시 의료기기 사이버보안 (N70) | 출시 후 레거시 제품 대응 | | SBOM 원칙 및 실무 (N73) | SW 구성요소 목록 관리 | | 허가·심사 가이드라인 (2025.01 개정) | 제출 자료: Threat Model, Risk Analysis, SBOM, 검증결과, 업데이트 정책 | ---

2. Chunk `1133947971991447253`

> ### 5.1 Cyber Device 해당 여부 | 제품 | SW 포함 | 네트워크 연결 | Cyber Device 판정 | 비고 | |---|---|---|---|---| | **X-ray Detector** | 펌웨어 포함 가능성 | DICOM 네트워크 연결 시 ○ | **조건부 ○** | 독립 동작 시 판정 재검토 필요 | | **Handheld X-ray Source** | 제어 SW / 무선 통신 모듈 | Bluetooth / Wi-Fi 탑재 시 ○ | **조건부 ○** | 무선 기능 유무 확인 필수 | | **촬영실 GUI SW** | SW 자체가 제품 | PACS/RIS/HIS 네트워크 필수 | **명확 ○** | 최우선 Threat Model 대상 | > **판정 원칙**: Section 524B (c) — SW를 "validate, install, or authorize" + 인터넷/네트워크 연결 능력. 두 조건 모두 해당 시 cyber device.

### kb-eval-20260620-it06-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_us-003", "iteration": 6, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "bf9ba1ece4ea0a37", "source": "github:holee9/MD-process/issue-drafts/009_03_SW_사이버보안_IEC81001_5_1_FDA.md", "source_hash": "bfde8ccac162058d143af5ce7e6e0ec7f9d3f13456d947bcf5780e1b7e49e1e1"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `bf9ba1ece4ea0a37`
- Source: `github:holee9/MD-process/issue-drafts/009_03_SW_사이버보안_IEC81001_5_1_FDA.md`
- Source hash: `bfde8ccac162058d143af5ce7e6e0ec7f9d3f13456d947bcf5780e1b7e49e1e1`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA

**Evaluation Target**

- Expected work product: concise RA judgment for `510(k) predicate strategy` based on this source.
- Review primarily:
  - Focus on predicate selection, IFU scope, technical differences, and data needed to justify substantial equivalence.
  - For FDA work, check predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, and submission evidence impact as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1139028071545473971`

> ## 참고 링크 - `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md` - `03_설계_개발관리/IEC_62304_SW_수명주기.md` - `12_교차검증_보고서/2026-04-21_Xray_안전성능_사이버보안_정합성.md`

2. Chunk `147599709023299597`

> ## 체크리스트 - [x] 표준·규제 범위 정의 - [x] Security Management Plan 11개 절 구조 확정 - [x] 81001-5-1 ↔ 62304 매핑표 - [x] FDA 제출물(SBOM, Threat Model, Architecture, VM Plan, Testing) 매핑 - [x] Coordinated Vulnerability Disclosure 절차 초안 - [ ] SBOM 생성 툴체인(CycloneDX/SPDX) 선정 - [ ] 디지털의료제품법·MFDS 가이드 최신 개정 반영 - [ ] TD 템플릿 Cybersecurity Annex로 연결

### kb-eval-20260620-it06-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_us-004", "iteration": 6, "matched_keywords": ["510k"], "profile_id": "ra-us", "scenario_id": "df04137342bfdcc6", "source": "github:holee9/ra-project/01_규제지식베이스/경쟁제품_510k_Summary_분석DB.md", "source_hash": "b5ba2e7d8e325fccda4dbe56432c75660eb8f450d4ed1bfcc29941bd772522ec"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `df04137342bfdcc6`
- Source: `github:holee9/ra-project/01_규제지식베이스/경쟁제품_510k_Summary_분석DB.md`
- Source hash: `b5ba2e7d8e325fccda4dbe56432c75660eb8f450d4ed1bfcc29941bd772522ec`
- Focus: 510(k) predicate strategy
- Matched keywords: 510k

**Evaluation Target**

- Expected work product: concise RA judgment for `510(k) predicate strategy` based on this source.
- Review primarily:
  - Focus on predicate selection, IFU scope, technical differences, and data needed to justify substantial equivalence.
  - For FDA work, check predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, and submission evidence impact as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1007953891767211662`

> | 구분 | 사실 (Fact) | 해석 (Interpretation) | 행동 지시 (Action) | |---|---|---|---| | 경쟁 강도 | 한국 기업이 IZL(Mobile X-ray) 시장 제출의 ~50% 차지, MQB(Detector)도 약 35% | 한국 기업들은 FDA 510(k) 취득 역량이 높음. 자사도 신속 대응 필요 | K251223(IZL) 기 cleared 활용, 신규 Detector 510(k) 우선 착수 | | Clearance 유형 | DRTECH·Iray 등은 Special 510(k) 활용 빈번 (연간 2~3건) | 제품 마이너 변경 시 Special로 ~3개월 처리. 전통적 510(k) 대비 비용·시간 절감 | 기 cleared 제품(K251223) 기반 마이너 변경은 Special 510(k) 검토 | | 번들 제출 | Carestream K253185: FPD + Mobile X-ray System 번들 | 시스템 통합 제품의 경우 단일 510(k)이 심사 일관성 유리 | Source + Detector + SW 시스템 제품화 시 번들 전략 검토 | | SW 단독 경로 | K251038(LLZ): 순수 DR Acquisition SW도 Class II 510(k) 취득 가능 (처리 ~4개월) |...

2. Chunk `104794288842511072`

> ## 8. 510(k) Summary 핵심 작성 패턴 실제 경쟁사 Summary 문서에서 공통적으로 확인된 구조:

### kb-eval-20260620-it06-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_us-005", "iteration": 6, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "dcdff75e976099e1", "source": "github:holee9/MD-process/issue-drafts/148_02_SOP-CVD-001_v0.3_FDA_사이버보안_QMSR.md", "source_hash": "644b975c641649f3ff1706bf813a3d1a74d8103137add6b8fdf02469f58eb1a4"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `dcdff75e976099e1`
- Source: `github:holee9/MD-process/issue-drafts/148_02_SOP-CVD-001_v0.3_FDA_사이버보안_QMSR.md`
- Source hash: `644b975c641649f3ff1706bf813a3d1a74d8103137add6b8fdf02469f58eb1a4`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, QMSR

**Evaluation Target**

- Expected work product: concise RA judgment for `510(k) predicate strategy` based on this source.
- Review primarily:
  - Focus on predicate selection, IFU scope, technical differences, and data needed to justify substantial equivalence.
  - For FDA work, check predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, and submission evidence impact as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `37260499763821515`

> --- title: "SOP-CVD-001 v0.3 보강 — FDA 사이버보안 지침 2026-02 반영·CVSS v4.0" labels: [enhancement, 02_QMS, v0.3, cybersecurity, QMSR] state: closed --- SOP-CVD-001 v0.2 → v0.3 보강 완료. - FDA 사이버보안 지침 2026-02-03 재발행 반영 (§15A.1) - CP 7382.850 사이버보안 CVD 점검 항목 추가 (§15A.2) - CVSS v3.1 → v4.0 전면 전환 (§15A.3) - X-ray 시스템 사이버보안 CVD 특수사항 추가 (§15A.4)

## ra_eu

### kb-eval-20260620-it06-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_eu-001", "iteration": 6, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "daf429915c54298c", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `daf429915c54298c`
- Source: `github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md`
- Source hash: `62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77`
- Focus: MDR classification and conformity route
- Matched keywords: EUDAMED

**Evaluation Target**

- Expected work product: concise RA judgment for `MDR classification and conformity route` based on this source.
- Review primarily:
  - Focus on MDR rule/class, conformity assessment route, NB involvement, and technical documentation evidence.
  - For EU MDR work, check classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, and MDR evidence traceability as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1048620351506847107`

> ### 5-A. 데이터베이스 등록 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR (EU) | |---|---|---|---| | 등록 DB | GUDID (FDA UDI DB) | UDI포털 (mfds.go.kr) | EUDAMED | | 의무화 시점 | 등급별 단계적 완료 | 2025 기준 진행 중 | 2026-05-28 (4개 모듈) | | 경제주체 등록 | FDA Establishment Registration (21 CFR 807) | 의료기기 제조업 허가 | SRN (Actor Module) | | 기기 등록 | 510(k)/PMA cleared → GUDID | 허가/인증/신고 후 UDI포털 | EUDAMED UDI/DEV | | UDI 발급기관 | GS1, HIBCC, ICCBBA | GS1(의무), HIBCC(가능) | GS1, HIBCC, ICCBBA | | Vigilance 보고 | eMDR (FDA MedWatch) | 이상사례 포털 | Module 5 (~Q2 2027) |

2. Chunk `1068273778649251618`

> ### Module 2: UDI/Device Registration (UDI/DEV) — UDI 및 기기 등록 #### 3-2-A. UDI 구조 ``` UDI = UDI-DI (고정) + UDI-PI (가변) Basic UDI-DI (레거시 식별자) └── UDI-DI (모델별) └── UDI-PI (생산 로트/일련번호) ``` - **Basic UDI-DI**: 동일 기기 군/버전을 식별하는 핵심 레퍼런스. EUDAMED에서 Globally Unique해야 함. - **UDI-DI**: 특정 버전/제품 모델 식별. - 발급 기관: GS1, HIBCC, ICCBBA 중 선택. #### 3-2-B. 등록 데이터 항목 (주요)

### kb-eval-20260620-it06-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_eu-002", "iteration": 6, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7db814277c776bf8", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "e58a514ed0c819866f9eb094ca113d09dad260f22054cadd6a7b17a7302724ef"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7db814277c776bf8`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md`
- Source hash: `e58a514ed0c819866f9eb094ca113d09dad260f22054cadd6a7b17a7302724ef`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Evaluation Target**

- Expected work product: concise RA judgment for `MDR classification and conformity route` based on this source.
- Review primarily:
  - Focus on MDR rule/class, conformity assessment route, NB involvement, and technical documentation evidence.
  - For EU MDR work, check classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, and MDR evidence traceability as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1042295090390197081`

> - Regulation (EU) 2024/1689 (AI Act) — 전문, Art. 6, 9-17, 43, 61-62, Annex II/III/IV - Regulation (EU) 2017/745 (MDR) — Art. 10, 15, 83-87, Annex I-III, IX-XI - MDCG 2019-11 (소프트웨어 분류), MDCG 2019-16 Rev.1 (사이버보안), MDCG 2020-3 (significant changes) - IEC 62304:2006/A1:2015, IEC 62366-1:2015/A1:2020, IEC 81001-5-1:2021 - ISO 14971:2019/A11:2021 - FDA AI/ML-based SaMD Action Plan, PCCP Draft Guidance 2023 - DQS Global — AI Act & AI-Enabled Medical Devices: Regulatory Status 2026 - MedDeviceGuide — EU AI Act for Medical Devices Compliance Guide 2026 - Gibson Dunn — EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines (2026) - Bird & Bird...

2. Chunk `1046173636268087282`

> ### 4.2 데이터 거버넌스 | AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 | X-ray 적용 | |-------------|------|----------------|-----------|-----------| | Data & Data Governance | Art. 10 | MDR Annex II §6.1, IEC 62304, GMLP | 학습/검증/테스트 데이터셋 관리 SOP | X-ray 영상 데이터: 다기관(≥3), 다장비 브랜드, 체형·연령·성별 대표성 확보 | | 데이터 품질 | Art. 10(2-5) | — | 라벨링 품질 관리, 편향 점검 | 판독 전문의 ≥2인 합의 라벨링, Cohen's κ ≥ 0.80 |

### kb-eval-20260620-it06-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_eu-003", "iteration": 6, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "1690befa42f6f162", "source": "github:holee9/MD-process/issue-drafts/004_01_EU_AI_Act_MDR_중첩매핑.md", "source_hash": "72ade98066fdbf0bf4c58031c9c00ef73a816c300c96ec3a6de724543bc72784"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `1690befa42f6f162`
- Source: `github:holee9/MD-process/issue-drafts/004_01_EU_AI_Act_MDR_중첩매핑.md`
- Source hash: `72ade98066fdbf0bf4c58031c9c00ef73a816c300c96ec3a6de724543bc72784`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Evaluation Target**

- Expected work product: concise RA judgment for `MDR classification and conformity route` based on this source.
- Review primarily:
  - Focus on MDR rule/class, conformity assessment route, NB involvement, and technical documentation evidence.
  - For EU MDR work, check classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, and MDR evidence traceability as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1004046925820759018`

> ## 체크리스트 - [x] High-risk 분류 기준 정리 - [x] Art.9/10/11/12/13/14/15/16–17/43/61/62 ↔ MDR/ISO/IEC 매핑 - [x] PCCP 3자(EU/FDA/KR) 정합 확인 - [x] Gap→조치 표 도출 (Risk File, 데이터 거버넌스, 모델 변경관리, PMS, TD) - [ ] SOP-DATA-001 / SOP-ML-001 후속 초안 작성 - [ ] TD 템플릿에 AI Act Annex IV 컬럼 적용

2. Chunk `12735660655387309`

> ## 배경 AI/ML 기반 SaMD(예: X-ray 영상 판독 보조) 는 AI Act Art. 6(1)에 의해 High-risk 분류 가능성이 높다. MDR과 중첩 요건을 사전 매핑하여 단일 QMS·기술문서·PMS에서 동시 충족 가능하도록 초안을 작성한다.

### kb-eval-20260620-it06-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_eu-004", "iteration": 6, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "432f4c2b5530b507", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `432f4c2b5530b507`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md`
- Source hash: `4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Evaluation Target**

- Expected work product: concise RA judgment for `MDR classification and conformity route` based on this source.
- Review primarily:
  - Focus on MDR rule/class, conformity assessment route, NB involvement, and technical documentation evidence.
  - For EU MDR work, check classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, and MDR evidence traceability as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

2. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

### kb-eval-20260620-it06-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_eu-005", "iteration": 6, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "501ed642434a0e70", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2019-16_Rev1_Cybersecurity_대응_체크리스트.md", "source_hash": "73cd35ce968999ac597a2ffd2cc0e9de93103ba5c45edee078877a0e708818ce"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `501ed642434a0e70`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2019-16_Rev1_Cybersecurity_대응_체크리스트.md`
- Source hash: `73cd35ce968999ac597a2ffd2cc0e9de93103ba5c45edee078877a0e708818ce`
- Focus: MDR classification and conformity route
- Matched keywords: MDR, MDCG

**Evaluation Target**

- Expected work product: concise RA judgment for `MDR classification and conformity route` based on this source.
- Review primarily:
  - Focus on MDR rule/class, conformity assessment route, NB involvement, and technical documentation evidence.
  - For EU MDR work, check classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, and MDR evidence traceability as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1033927941898965900`

> > ✅: 필수 적용 / △: 조건부 적용 / -: 해당없음 (위험 평가 결과에 따라 조정)

2. Chunk `1035120197226241881`

> > 최종 갱신: 2026-05-14 (자동보강 #44) > 근거: https://health.ec.europa.eu/system/files/2022-01/md_cybersecurity_en.pdf | https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en # MDCG 2019-16 Rev.1 Cybersecurity 대응 체크리스트

## ra_kr

### kb-eval-20260620-it06-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_kr-001", "iteration": 6, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "8470b8314ec6498c", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `8470b8314ec6498c`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source hash: `1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff`
- Focus: MFDS classification and licensing route
- Matched keywords: KGMP

**Evaluation Target**

- Expected work product: concise RA judgment for `MFDS classification and licensing route` based on this source.
- Review primarily:
  - Focus on Korean classification/licensing route, technical document needs, KGMP linkage, and MFDS-specific evidence.
  - For MFDS work, check licensing/classification, KGMP, digital medical product obligations, supplementary-response strategy, and Korean evidence readiness as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1037950769042691196`

> MDSAP 수용 (실사 대체 가능) | MDR Annex IX §3.2 — MDSAP 부분 수용 |

### kb-eval-20260620-it06-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_kr-002", "iteration": 6, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "e4213b377c160f4d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_6종_가이드라인_요약.md", "source_hash": "59cd597ad73333f3a36a6a56fb5fd2997d20bab166a18e0b7ed594f77fe17fff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `e4213b377c160f4d`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_6종_가이드라인_요약.md`
- Source hash: `59cd597ad73333f3a36a6a56fb5fd2997d20bab166a18e0b7ed594f77fe17fff`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Evaluation Target**

- Expected work product: concise RA judgment for `MFDS classification and licensing route` based on this source.
- Review primarily:
  - Focus on Korean classification/licensing route, technical document needs, KGMP linkage, and MFDS-specific evidence.
  - For MFDS work, check licensing/classification, KGMP, digital medical product obligations, supplementary-response strategy, and Korean evidence readiness as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1059459999498570675`

> ## 2. 6종 가이드라인 개요 | 번호 | 구분 | 가이드라인명 | 주요 적용 대상 | |---|---|---|---| | 1 | **제정** | 디지털의료기기소프트웨어 허가·심사 가이드라인 | 내장형·독립형 소프트웨어 전반 공통 기본서 | | 2 | 개정 | 의료기기 소프트웨어 허가·심사 가이드라인 | **내장형** 소프트웨어 + 의료기기 연동 앱·웹 | | 3 | 개정 | 인공지능기술이 적용된 디지털의료기기 허가·심사 가이드라인 | MLMD(Machine Learning-enabled Medical Device) 전반 | | 4 | 개정 | 가상융합기술이 적용된 디지털의료기기 허가·심사 가이드라인 | VR·AR·MR 기술 적용 의료기기 | | 5 | 개정 | 디지털치료기기 허가·심사 가이드라인 | **독립형** SW 중 질병 예방·관리·치료 목적 제품 | | 6 | 개정 | 인공지능기술이 적용된 디지털의료기기 임상시험방법 설계 가이드라인 | AI 적용 의료기기 임상시험계획 승인 | > **구조**: 가이드라인 1번(신제정)이 기본서 역할, 2~6번은 기본서를 보완하는 계층 구조. ---

2. Chunk `1114958470722170859`

> ## 7. 참조 문서 - `MFDS_디지털의료제품법_하위고시_추적.md` — 고시 제2025-23호·제2025-25호 상세 (#9) - `MFDS_기술문서_섹션별_작성가이드.md` — 기술문서 작성 지침 (#8) - `eSTAR_05_Software_Section.md` — FDA SW Section (IEC 62304 기반) 비교 참조 (#5)

### kb-eval-20260620-it06-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_kr-003", "iteration": 6, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "20fada09b49a42a2", "source": "github:holee9/ra-project/06_심사_QA이력/MFDS인허가/Acts_QA이력.md", "source_hash": "15a68c6c759e84d380e48841a71026a22f4bf3c240a638853cec2ede1e29c21c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `20fada09b49a42a2`
- Source: `github:holee9/ra-project/06_심사_QA이력/MFDS인허가/Acts_QA이력.md`
- Source hash: `15a68c6c759e84d380e48841a71026a22f4bf3c240a638853cec2ede1e29c21c`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS

**Evaluation Target**

- Expected work product: concise RA judgment for `MFDS classification and licensing route` based on this source.
- Review primarily:
  - Focus on Korean classification/licensing route, technical document needs, KGMP linkage, and MFDS-specific evidence.
  - For MFDS work, check licensing/classification, KGMP, digital medical product obligations, supplementary-response strategy, and Korean evidence readiness as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1011974532751774892`

> ### H&abyz SAR 시험 관련 (2025-01-13, 1건) - 발신: <jr.choi@actslab.co.kr> - 수신: '"한지민"' <hjm@abyzr.com>, <jw.kim@actslab.co.kr> - 내용 요약: 안녕하세요 ㈜액트에 최재락입니다. 다름이 아니 오라 디텍터의 SAR시험에 대한 내용 정리하여 보내 드립니다. SAR 시험 시 CONDUCTED 시료가 필요한 이유는 아래와 같습니다. 성적서에 무선 모듈의 평균 전력 값이 들어가야 하는데 RSE 시료로는 측정이 안됩니다. 그래서 CONDUCTED 시료가 필요하며 CONDUCTED 각 채널 별로 평균 전력을 측정하여 최고 Worst CASE의 채널에서 시험합니다. CONDUCTED 시료를 주실 때 디텍터 자체가 아닌 무선 모듈만 주셔도 무방하며 RSE 시료와 같이 강제 송. 수신 모드만 되면 됩니다. 최 우선 적인 것은 CONDUCTED 시료가 필요합니다. 감사합니다. 최재락 드림 JaeRak Choi / Director Mobile: +82-10-4705-7967 E-mail: <mailto:jr.choi ---

2. Chunk `1019630360084047424`

> ### H&abyz, 지원사업 관련 요청 건. (2025-05-14, 1건) - 발신: <jw.kim@actslab.co.kr> - 수신: '한지민' <hjm@abyzr.com> - 내용 요약: 한지민 리더님, 안녕하세요. 액트의 김주욱입니다. 금일 제가 외근으로 인해 회신이 늦어진 점 양해 부탁드립니다. 첨부로 하기 메일에 요청하신 자료 전달 드리니 확인바랍니다. * 1. 세금계산서 * 2. 인보이스 * 3. 송금증 * 4. 수정 견적서 (유선상으로 설명 드린 바와 같이 승인비용 수정된 견적서입니다) 첨부 및 위 내용 확인 후 기타 다른 문의 사항 있으시면 회신 바랍니다. 김주욱 드림. JuWuk Kim / Director Tel. +82-70-7119-3413 Fax. +82-31-8066-7366 Mobile. +82-10-9799-0009 Email. <mailto:jw.kim@actslab.co.kr> jw.kim@actslab.co.kr 이 이메일은 지정된 수신자만을 위한 것으로, 기밀 정보가 포함될 수 있습니다. 이 이메 ---

### kb-eval-20260620-it06-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_kr-004", "iteration": 6, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9a1672d7f0a0180d", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `9a1672d7f0a0180d`
- Source: `github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md`
- Source hash: `e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c`
- Focus: MFDS classification and licensing route
- Matched keywords: 디지털의료제품법

**Evaluation Target**

- Expected work product: concise RA judgment for `MFDS classification and licensing route` based on this source.
- Review primarily:
  - Focus on Korean classification/licensing route, technical document needs, KGMP linkage, and MFDS-specific evidence.
  - For MFDS work, check licensing/classification, KGMP, digital medical product obligations, supplementary-response strategy, and Korean evidence readiness as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1016004334478948993`

> ## 참고 링크 - `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` - `12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md` - MFDS 디지털의료제품 정보 포털 (emedi.mfds.go.kr) - 국가법령정보센터 「디지털의료제품법」 - 관련 이슈: 005(GSPR 체크리스트 v0.2→v0.3), 009(사이버보안), 013(SBOM)

2. Chunk `1061576322702878078`

> ## 배경 디지털의료제품법은 2025-01-24 시행, 시행규칙 2025-02-28 현행. 사용적합성 자료 제출 의무화, 사이버보안 요구 확대(15→35), AI 변경관리 계획, 구성요소 단위 성능평가(2026 시행) 등 본 프로젝트(X-ray Workstation SW·AI 영상분석 모듈 가능성)에 직접 영향. 2026-04-22 교차검증에서 G2(사용적합성 증빙 미대응), G3(구성요소 평가 적용 여부 미판정), G4(RA-01~RA-20 전수 매핑 미완) 도출.

### kb-eval-20260620-it06-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it06-ra_kr-005", "iteration": 6, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "2559c7b9e1a8bbca", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용방사선_안전관리규칙_개정이력.md", "source_hash": "72535c6d3f96f4fd7b79cd95bf14f95cd1f97e599100fb5e2131a61187ba9847"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2559c7b9e1a8bbca`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용방사선_안전관리규칙_개정이력.md`
- Source hash: `72535c6d3f96f4fd7b79cd95bf14f95cd1f97e599100fb5e2131a61187ba9847`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Evaluation Target**

- Expected work product: concise RA judgment for `MFDS classification and licensing route` based on this source.
- Review primarily:
  - Focus on Korean classification/licensing route, technical document needs, KGMP linkage, and MFDS-specific evidence.
  - For MFDS work, check licensing/classification, KGMP, digital medical product obligations, supplementary-response strategy, and Korean evidence readiness as applicable.
  - Uses the cited source excerpts, not generic regulatory memory.
  - States the required regulatory judgment, evidence gap, or action clearly.
  - Separates confirmed source facts from assumptions or missing information.
  - Identifies when human escalation is needed because the source is insufficient.

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

1. Chunk `1060309257388743492`

> ## 5. 본 프로젝트 대응 - [ ] 60601-2-54 형식시험 시 누설선량 2mR/h 요건 검증 케이스 추가 - [ ] IFU에 포터블 사용 시나리오·환자 외 피폭 방지 조치 섹션 반영 - [ ] 2025-07-18 개정(제1122호) 조문 원문 확보 후 본 문서 v0.2 갱신 - [ ] KIAQC 정기검사 대응 자료 패키지(제조자 제공) 업데이트

2. Chunk `202447493375001784`

> ## 4. 정기 검사 체계(참고) - 설치 신고 및 **3년 주기** 정기검사(한국의료영상품질관리원, KIAQC) - 정기검사 항목: 관전압·관전류 정확도, 선량, 공간분해능, 저대비 분해능, 누설선량
