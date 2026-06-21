# KB Eval Checksheet - 2026-06-20 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260620-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_us-001", "iteration": 2, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "fa967f7ad2e16c3f", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `fa967f7ad2e16c3f`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source hash: `1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff`
- Focus: 510(k) predicate strategy
- Matched keywords: QMSR

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

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1037950769042691196`

> MDSAP 수용 (실사 대체 가능) | MDR Annex IX §3.2 — MDSAP 부분 수용 |

### kb-eval-20260620-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_us-002", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "a96345dbb21f8b17", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "0ae1ab039639874633d1d56b38c299dfa9beb69da719e10871d3288430442dce"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `a96345dbb21f8b17`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md`
- Source hash: `0ae1ab039639874633d1d56b38c299dfa9beb69da719e10871d3288430442dce`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

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

1. Chunk `104826367722559813`

> ### 4.1 X-ray Detector (평판 검출기) - 센서 종류 (CMOS / a-Si+CsI / a-Se) - 영상영역(cm × cm 또는 inch) - 픽셀 피치(μm) · 총 픽셀 수 - 공간분해능(lp/mm) · MTF at 1 lp/mm, 2 lp/mm - DQE at 0 lp/mm, 1 lp/mm, 2 lp/mm (IEC 62220-1-1 측정조건 명기: RQA5 등) - AED(Automatic Exposure Detection) 기능 유무 - 통신 인터페이스 (GbE / Wi-Fi 규격 / Tethered) - 배터리 (해당 시) · 충전 방식 - 동작 온습도 범위 - 무게·낙하 내성 - 호환 Generator 목록

2. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

### kb-eval-20260620-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_us-003", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "dfd325d56064772a", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "c016b9b71c421bbff191427c089029b85d25aab55e122f03e3dabbff564b8880"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `dfd325d56064772a`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md`
- Source hash: `c016b9b71c421bbff191427c089029b85d25aab55e122f03e3dabbff564b8880`
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

1. Chunk `1031538840091158839`

> ### 4.2 응답서 구성 원칙 **FDA Guidance 권고 (Section V of FDA Guidance on deficiency responses)**: 각 결함에 대해 다음 3가지 중 하나로 응답: 1. 요청된 정보 또는 데이터 제공 2. 해당 사항이 없는 이유 설명 3. 대체 정보 제공 + 왜 그 정보가 문제를 해결하는지 설명 **형식 원칙**: - 결함 번호를 **원문 그대로** 복사·유지 (순서 변경 금지) - 표(Table) 형식 + 행 색상 교차 (FDA 원문 vs 회사 응답 구분) - 단일 부록 번호 체계 유지 (AI Response App. 001, 002, …) - 각 부록 표지: "What this is / What it proves / Where it's referenced" ---

2. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

### kb-eval-20260620-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "dc4735d558243a0c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_Threat_Model_STRIDE_가이드.md", "source_hash": "f6cd656dce2527909f6e09f1befda964ccd3a78dfad81b725a69a2d8909efe44"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `dc4735d558243a0c`
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

### kb-eval-20260620-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "4b4fd3a0a2c949c3", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "e0a1770f4c14eee7546a5f886bb84ebc12c923c94850a85b07ce8a572f4f8319"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4b4fd3a0a2c949c3`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md`
- Source hash: `e0a1770f4c14eee7546a5f886bb84ebc12c923c94850a85b07ce8a572f4f8319`
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

1. Chunk `1041077994247338699`

> ### 2.2 구조 매핑 | QMSR (21 CFR 820) | 내용 | 대응 ISO 13485 조항 | |-------------------|------|-------------------| | §820.1 | 범위 | — | | §820.3 | 정의 | ISO 13485 §3 + 추가 정의 | | §820.10 | ISO 13485 참조편입 선언 | 4~8 전체 | | §820.20 | 경영검토 추가 입력 | 5.6 보완 | | §820.25 | 라벨링·포장 관리 | 7.5 보완 | | §820.30 | 설계관리 유지 (Class I 면제 외) | 7.3 보완 | | §820.35 | 기록관리 추가요구 | 4.2.5 보완 | | §820.45 | 기기 표시 검사 | 신설 | | §820.180 | (폐지) 기밀성 예외 | — | | §820.198 | 불만처리 추가 | 8.2.2 보완 |

2. Chunk `1108022682513885495`

> ### 5.3 설계관리 (§820.30) - Class II X-ray 시스템: 설계관리 적용 (Class I 면제 아님) - IEC 62304 SW 수명주기 프로세스와 통합 - 설계변경 시 510(k) 재제출 필요성 판단 절차

## ra_eu

### kb-eval-20260620-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "f391aadc478ad668", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "07766aa926d3be57b6bf2d75f4605289efab7c283eadd6841a001afa2d8987be"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f391aadc478ad668`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md`
- Source hash: `07766aa926d3be57b6bf2d75f4605289efab7c283eadd6841a001afa2d8987be`
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

1. Chunk `1079572648514538742`

> ## 관련 KB 문서 - [공통_Clinical_Evaluation_Plan_Report_MDR_템플릿](../../../02_제품별_기술파일/공통/공통_Clinical_Evaluation_Plan_Report_MDR_템플릿.md) — CEP/CER 작성 템플릿 - [MDR_AnnexI_GSPR_Checklist](../MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md) — GSPR 전항목 체크리스트 - [MDR_AnnexII_Technical_Documentation_Template](../MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md) — 기술문서 구조 - [MDR_AnnexIII_PMS_TD_Template](../MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md) — PMCF 포함 PMS 문서

2. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

### kb-eval-20260620-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "f34b1a04e8c2b3f6", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f34b1a04e8c2b3f6`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20260620-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "252d2385dea272f1", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `252d2385dea272f1`
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

### kb-eval-20260620-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "582923980039ed6f", "source": "github:holee9/ra-project/02_제품별_기술파일/공통/공통_Clinical_Evaluation_Plan_Report_MDR_템플릿.md", "source_hash": "42a1e924df04a6bd384129cf252ae2226963b2fc69f0cbc788f8af162d0f61fd"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `582923980039ed6f`
- Source: `github:holee9/ra-project/02_제품별_기술파일/공통/공통_Clinical_Evaluation_Plan_Report_MDR_템플릿.md`
- Source hash: `42a1e924df04a6bd384129cf252ae2226963b2fc69f0cbc788f8af162d0f61fd`
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

1. Chunk `1006242736409429476`

> ### 문서 표지 | 항목 | 내용 | |---|---| | 문서 번호 | CEP-[제품코드]-[버전] | | 제품명 | [제품 정식 명칭] | | 모델 번호 | [모델 번호] | | MDR 분류 | [Class IIa / IIb] | | 문서 버전 | [버전] | | 작성일 | [YYYY-MM-DD] | | 작성자 | [이름, 직책] | | 검토자 | [이름, 직책] | | 승인자 | [이름, 직책] (PRRC 또는 책임자) | | 다음 갱신 예정일 | [YYYY-MM-DD] | ---

2. Chunk `1008262123982587034`

> ``` 검색 DB: PubMed, Embase, Cochrane CENTRAL, KOREAMED (MFDS용) 검색 기간: [YYYY-MM-DD] ~ [YYYY-MM-DD] 검색 언어: 영어, 한국어 (필요 시 기타) 주요 검색어 예시: - X-ray Detector: "digital radiography detector" OR "flat panel detector" AND "clinical performance" OR "image quality" - Handheld X-ray Source: "handheld X-ray" OR "portable X-ray generator" AND "radiation dose" OR "image quality" - GUI SW: "radiography software" OR "acquisition software" AND "usability" OR "clinical workflow" 포함 기준 (Inclusion): 동등 제품 또는 자사 제품 관련 임상 연구, RCT/코호트/케이스시리즈, 출판 후 동료심사 완료 제외 기준 (Exclusion): 전임상(in vitro/in vivo 동물), 초록만 존재, 중복 데이터 PRISMA 플로우차트: [첨부 문서 번호] ``` #### 4.3 문헌 평가 체계 ```...

### kb-eval-20260620-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "5f534b67b96c434f", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md", "source_hash": "4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `5f534b67b96c434f`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md`
- Source hash: `4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1`
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

1. Chunk `1007248354989010815`

> ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological processes: 일반 IIa / immediate danger IIb. > Others: Class I. **→ 촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III**

2. Chunk `1007987960287657537`

> ### 7.1 차등 시한 | Class | 시한 | |---|---| | Class III **custom-made** implantable | 2026-05-26 | | Class III / Class IIb **implantable** (sutures·screws 등 제외) | **2027-12-31** | | Class IIb **non-implantable** / IIa / Is / Im | **2028-12-31** |

## ra_kr

### kb-eval-20260620-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "bfb51897b719e74e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `bfb51897b719e74e`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md`
- Source hash: `2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02`
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

1. Chunk `341244002941932847`

> ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트

2. Chunk `634338496332185325`

> ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)

### kb-eval-20260620-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "bf71e84a0ab56b75", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/README.md", "source_hash": "955a83a25d265db55798a04d0d7968a79f47ac36e05a19a9321ef64a0749ffab"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `bf71e84a0ab56b75`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/README.md`
- Source hash: `955a83a25d265db55798a04d0d7968a79f47ac36e05a19a9321ef64a0749ffab`
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

1. Chunk `205092528198502292`

> ## 핵심 근거 (X-ray 관련) - 의료기기법 및 시행규칙 - 「의료기기 품목 및 품목별 등급에 관한 규정」 - 「의료기기 허가·신고·심사 등에 관한 규정」 - 「의료기기 GMP 심사·평가 등에 관한 규정」 - 「의료용 X선 발생장치 등 기술문서 작성 가이드라인」 - 「의료용 SW 허가·심사 가이드라인」

2. Chunk `550471061485587044`

> ## 수록 대상 - 의료기기법, 시행령, 시행규칙 - 식약처 고시 (제조·수입품목허가·신고 등) - 식약처 가이드라인·민원인안내서 - 의료기기 기술문서·임상시험 관련 고시

### kb-eval-20260620-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "0a8ef72bfe181b13", "source": "github:holee9/ra-project/06_심사_QA이력/MFDS인허가/Acts_QA이력.md", "source_hash": "15a68c6c759e84d380e48841a71026a22f4bf3c240a638853cec2ede1e29c21c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0a8ef72bfe181b13`
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

### kb-eval-20260620-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "dfbc6de4de340dfc", "source": "github:holee9/ra-project/06_심사_QA이력/MFDS컨설팅/Medi-Guide_QA이력.md", "source_hash": "4368ee399d24c7be329a1b42b455a18741b89d05d6538f70f709cbe49daaad93"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `dfbc6de4de340dfc`
- Source: `github:holee9/ra-project/06_심사_QA이력/MFDS컨설팅/Medi-Guide_QA이력.md`
- Source hash: `4368ee399d24c7be329a1b42b455a18741b89d05d6538f70f709cbe49daaad93`
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

1. Chunk `1013460470672057176`

> **[2025-12-08]** <guide20@medi-guide.com> → '한지민' <hjm@abyzr.com> 수신. H&abyz 한지민 팀장님 안녕하세요. 메디가이드 김호성입니다. 문의주신 사항에 대하여 회신 드립니다. 타 제품에서 설정하고 있는 환자 범위는 저희도 추가적인 조사가 필요하여 조사 후에 다시 회신 드리도록 하겠습니다. 다만, 현재까지 확인된 바에 따르면 덴탈용으로 사용되는 휴대형 x선 촬영 시스템의 경우, **[2025-12-15]** <guide20@medi-guide.com> → '김지연' <jykim@abyzr.com> 수신. 에이치앤아비즈 김지연 프로님 안녕하세요. 메디가이드 김호성입니다. 하기 메일에서 요청하신 PMS 계획서 전달 드립니다. 검토 사항에 대한 내용은 첨부된 문서의 메모를 참조 부탁드립니다. 추가적으로 방문 미팅 시간을 오전 10시로 변경이 가능할지 확인 요청 드립니다. 감사합니다.

2. Chunk `1074821498944196981`

> ### H&abyz. 포터블 CE MDR 컨설팅 관련 사전미팅 요청 건. (2025-06-27, 1건) - 발신: "HDH" <hdh@medi-guide.com> - 수신: '한지민' <hjm@abyzr.com>, "'Jung'" <guide02@medi-guide.com> - 내용 요약: 안녕하세요, 한지민 리더님. 사전 미팅 참석 가능합니다. 저는 화요일이 좋습니다. 시간은 편하게 정하시면 되는데, 되도록 차가 막히는 시간에 오고가는 것만 좀 피했으면 합니다. 감사합니다. Best regards, HONG, Dae Hee Chief Consultant & CEO of MEDIGUIDE Inc. / Professor of Daelim University Web: <http://www.medi-guide.com/> www.medi-guide.com Phone: +82-2-6949-3723 / +82-70-5057-6200 C.P.: +82-10-2363-8844 Fax: +82-50-5055-8661 Office (Main) : #410, 17, Deogan-ro 104beon-gil, Gwangmyeong-si, Gyeonggi-do, 14353, Korea ---

### kb-eval-20260620-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "c5b659796b8ba2b1", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_기술문서_섹션별_작성가이드.md", "source_hash": "f1a42b1b5d6bc604ca2faa7644dc90cfb166a98521fb98244ac09e80eec1e2b1"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c5b659796b8ba2b1`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_기술문서_섹션별_작성가이드.md`
- Source hash: `f1a42b1b5d6bc604ca2faa7644dc90cfb166a98521fb98244ac09e80eec1e2b1`
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

1. Chunk `1075785891198339619`

> ### 4.3 시험규격 설정 근거 작성 요령 - 국제 표준 근거: "IEC 60601-2-28:2017을 적용하였으며, 동 규격이 X선관 조립품(X-ray tube assembly)의 성능 시험 방법을 규정하는 국제 표준으로 MFDS 인정 기준과 일치함." - 자사 규격 근거: "국제 표준에서 정하지 않은 항목(예: 영상 처리 알고리즘 성능)은 의도된 사용목적 및 위험 분석 결과에 따라 자사 시험 규격 OQP-XXXX를 제정하여 적용함." - KS 표준 근거: "KS A ISO 9283 대응 자사 규격 적용." ---

2. Chunk `134996178882731357`

> ## 1. 기술문서 전체 구성 (시행규칙 별표 3 기준) ``` 기술문서 (MFDS 제출용) ├── 1. 개요 (제품명, 품목명, 분류번호, 모델명, 제조원) ├── 2. 사용목적 (Intended Use / Indications for Use) ├── 3. 작용원리 (Operating Principle / Mechanism of Action) ├── 4. 원재료·구성품·구조 (Materials & Structure) ├── 5. 제조방법 (Manufacturing Process) ├── 6. 성능·시험규격 (Performance & Test Specifications) │ ├── 6-1. 시험규격 및 설정근거 │ └── 6-2. 실측값 (성적서) ├── 7. 안전성 자료 (Safety Data) │ ├── 7-1. 전기·기계적 안전 │ ├── 7-2. 생물학적 안전 │ ├── 7-3. 방사선 (해당 시) │ ├── 7-4. 전자파(EMC) │ └── 7-5. SW 안전성 (해당 시) ├── 8. 임상자료 (해당 시) └── 9. 기재사항 (라벨, 사용설명서) ``` ---
