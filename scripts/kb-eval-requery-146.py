#!/usr/bin/env python3
"""#146 약어 오독 13건 targeted 재질의 — 전용 실행기 (기본 dry-run).

`docs/ra/sop-abbreviation-collisions.md` §4 매핑 표의 13건을, 2026-10-15 반영된
ra-us SOUL `### Document-name abbreviations vs FDA programs` 규칙 적용 후
**원본과 동일한 입력**(원본 체크시트에 기록된 source_path·recorded source_hash·발췌)으로
재호출해 약어 오독(PMA/RTA/PCCP), 510(k) supplement, AI 기한 창작, EU 용어 혼입이
해소됐는지 확인한다 (#146 DoD 4, 사용자 승인 2026-10-15 — 10-16 정기 회차 병행).

## #147 실행기와의 차이

- **원본 소스를 그대로 쓴다** (재선정 아님). 13건 중 4건의 소스는 `issue-drafts/`라
  #128/#154 이후 현재 KB(ra_knowledge)에 없으므로, DB 조회 대신 **원본 체크시트에
  기록된 발췌를 verbatim**으로 전달한다 — 바이트 동일 입력이어야 전후 비교가 성립한다.
- `recorded_source_hash` 는 원본 체크시트 메타데이터의 청크 기반 해시를 lineage 로
  그대로 남긴다(재계산 아님 — Codex 09-11 지침).

## 안전 규칙 (#147 실행기 계승)

- 기본 **dry-run**. `--execute` 없이는 LLM 을 호출하지 않는다.
- 호출 상한 **13회 고정**. 실패도 예산을 소모한다(재시도하지 않는다).
- 출력은 `reports/kb-eval-requery-146/` (+ `--batch` 서브디렉터리). 원본 체크시트는
  읽기만 하고 쓰지 않는다.
- 호출 **전에** 예산 소비를 원장에 영속 기록(fsync)하고, 결과는 즉시 기록한다.
- `unknown`(결과 없는 시도)이 있으면 재개를 막는다 — 예산을 모르게 쓰지 않는다.
- 배타 락으로 중복 실행이 같은 예산을 따로 소비하는 것을 막는다.

사용:
    python3 scripts/kb-eval-requery-146.py            # 계획만 출력
    python3 scripts/kb-eval-requery-146.py --execute  # 실제 13회 호출
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "reports" / "kb-eval-requery-146"
CALL_BUDGET = 13                      # 승인된 호출 수 — 초과 금지

CASES: list[dict] = [
    {
        "n": 1,
        "case_id": "kb-eval-20260722-it01-ra_us-001",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "510(k) supplement 미존재",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md",
        "recorded_source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6",
        "excerpts": [
            "> 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...",
            "### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---"
        ]
    },
    {
        "n": 2,
        "case_id": "kb-eval-20260721-it01-ra_us-003",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "PMA 약어 오독",
        "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md",
        "recorded_source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd",
        "excerpts": [
            "## 갭 내용 | 조항 | 요구사항 | 현재 상태 | |------|----------|-----------| | §8.1 | 적합성·효과성·개선 모니터링·분석·개선 계획 | partial | | §8.2.5 | 프로세스 성과 모니터링·미달 시 CAPA 트리거 | partial | | §8.5.1 | 품질정책·목표·감사·분석·시정·MR 통한 효과성 개선 | partial |",
            "## Definition of Done - [ ] `02_품질경영시스템_QMS/SOP-PMA-001_프로세스_모니터링_분석_절차.md` 신규 (v0.1) - 프로세스 카탈로그(설계·구매·제조·검사·서비스·PMS·CAPA·교육·문서) — 9개 - KPI 매트릭스(프로세스 × 측정지표 × 주기 × 임계치 × 소유자) — 정량 - 데이터 수집·분석 방법(통계기법: SPC·Pareto·Ishikawa) - 미달 시 트리거(CAPA·MR 입력·자원 재배치) 폐쇄루프 - §8.5.1 효과성 측정 연계(품질목표→KPI→MR) - [ ] `02_품질경영시스템_QMS/F-PMA-001_KPI_매트릭스.md` 신규 — 27개 셀(9프로세스×3차원) - [ ] CHK-ISO13485-001 ISO-8.1/8.2.5/8.5.1 `status: met` 갱신 - [ ] SOP-MR-001/SOP-CAPA-001/F-MR-001 정합성 — KPI ↔ MR 입력 ↔ CAPA 트리거 - [ ] 규제 매핑: ISO 13485 §8.1/8.2.5/8.5.1, FDA QMSR §820.250(통계기법)·§820.100(CAPA), EU MDR Art.10(9)(j) - [ ] 적대적 자기검토(심사관 모드)"
        ]
    },
    {
        "n": 3,
        "case_id": "kb-eval-20260720-it01-ra_us-005",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "PCCP 약어 오독",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md",
        "recorded_source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76",
        "excerpts": [
            "### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. ---",
            "## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로 사전 승인된 변경 범위 운영 | | **AI-Enabled Device Software Functions: Lifecycle Management & Marketing Submission Recommendations** | **초안(Draft)** | 2025-01-06 | ⏸ 초안 유지(FY2026 B-list) | TPLC 전반 설계·제출 권고(투명성·편향·HF·사이버보안) | > 의견수렴: 수명주기 초안은 2025-04-07 코멘트 마감. 이후 확정본 미발표(2026-06 기준). ---"
        ]
    },
    {
        "n": 4,
        "case_id": "kb-eval-20260720-it01-ra_us-001",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "EU 용어 혼입 (Class IIb)",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md",
        "recorded_source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503",
        "excerpts": [
            "## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VMP** | 필수 | PMS 계획에 포함 | 업데이트 정책으로 요구 | | **Pen Test** | 권고 | 권고 | 권고 | | **표준 참조** | IEC 81001-5-1, NIST CSF | IEC 81001-5-1 (조화표준 진행) | IEC 81001-5-1, MFDS 자체 가이드 | | **포스트마켓** | 법적 의무 (패치, CVD, 모니터링) | PMS + Vigilance 연계 | 이상사례 보고 + 업데이트 절차 | > MDR/MFDS 영향: GUI SW의 경우 FDA 요건 충족 수준으로 작성하면...",
            "### 3.4 SBOM (Software Bill of Materials) **법적 의무** (Section 524B(b)(3)). **NTIA Minimum Elements** (FDA 준용): | 필드 | 설명 | 예시 | |---|---|---| | Supplier Name | SW 공급자 | OpenJDK Foundation | | Component Name | 컴포넌트 명칭 | OpenJDK | | Version | 버전 문자열 | 17.0.9 | | Unique Identifier | CPE 또는 PURL | `pkg:maven/org.openjdk/jdk@17.0.9` | | Dependency Relationship | 의존성 관계 | DependsOn: spring-boot@3.2.0 | | Author of SBOM | SBOM 작성자 | [제조사명] | | Timestamp | 생성일시 ISO 8601 | 2026-04-29T00:00:00Z | **형식**: SPDX 2.3+ 또는 CycloneDX 1.5+ (machine-readable JSON/XML 권장) **포함 범위**: - Manufacturer-developed SW (자체 개발) - Third-party commercial/licensed SW - Ope..."
        ]
    },
    {
        "n": 5,
        "case_id": "kb-eval-20260719-it01-ra_us-001",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "510(k) supplement 미존재",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md",
        "recorded_source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11",
        "excerpts": [
            "## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용",
            "## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응"
        ]
    },
    {
        "n": 6,
        "case_id": "kb-eval-20260718-it01-ra_us-005",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "510(k) supplement 미존재",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md",
        "recorded_source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503",
        "excerpts": [
            "## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VMP** | 필수 | PMS 계획에 포함 | 업데이트 정책으로 요구 | | **Pen Test** | 권고 | 권고 | 권고 | | **표준 참조** | IEC 81001-5-1, NIST CSF | IEC 81001-5-1 (조화표준 진행) | IEC 81001-5-1, MFDS 자체 가이드 | | **포스트마켓** | 법적 의무 (패치, CVD, 모니터링) | PMS + Vigilance 연계 | 이상사례 보고 + 업데이트 절차 | > MDR/MFDS 영향: GUI SW의 경우 FDA 요건 충족 수준으로 작성하면...",
            "### 3.4 SBOM (Software Bill of Materials) **법적 의무** (Section 524B(b)(3)). **NTIA Minimum Elements** (FDA 준용): | 필드 | 설명 | 예시 | |---|---|---| | Supplier Name | SW 공급자 | OpenJDK Foundation | | Component Name | 컴포넌트 명칭 | OpenJDK | | Version | 버전 문자열 | 17.0.9 | | Unique Identifier | CPE 또는 PURL | `pkg:maven/org.openjdk/jdk@17.0.9` | | Dependency Relationship | 의존성 관계 | DependsOn: spring-boot@3.2.0 | | Author of SBOM | SBOM 작성자 | [제조사명] | | Timestamp | 생성일시 ISO 8601 | 2026-04-29T00:00:00Z | **형식**: SPDX 2.3+ 또는 CycloneDX 1.5+ (machine-readable JSON/XML 권장) **포함 범위**: - Manufacturer-developed SW (자체 개발) - Third-party commercial/licensed SW - Ope..."
        ]
    },
    {
        "n": 7,
        "case_id": "kb-eval-20260718-it01-ra_us-003",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "PCCP 오독 · supplement · EU 용어",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md",
        "recorded_source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76",
        "excerpts": [
            "### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. ---",
            "## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로 사전 승인된 변경 범위 운영 | | **AI-Enabled Device Software Functions: Lifecycle Management & Marketing Submission Recommendations** | **초안(Draft)** | 2025-01-06 | ⏸ 초안 유지(FY2026 B-list) | TPLC 전반 설계·제출 권고(투명성·편향·HF·사이버보안) | > 의견수렴: 수명주기 초안은 2025-04-07 코멘트 마감. 이후 확정본 미발표(2026-06 기준). ---"
        ]
    },
    {
        "n": 8,
        "case_id": "kb-eval-20260718-it01-ra_us-002",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "PCCP 오독 · supplement · EU 용어",
        "source": "github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md",
        "recorded_source_hash": "efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff",
        "excerpts": [
            "> 참고: 사내 자매문서 `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md` v0.3는 §3에서 \"FDA PCCP Guidance 2024\" 및 §4 용어표 \"PCCP — Predetermined Change Control Plan\"로 정확히 최종본을 인용하고 있어, 본 문서만 노후 인용 상태가 단절되어 있다.",
            "## Tier 2 (보조 — 범위 가늠용) - King & Spalding alert \"FDA Publishes Final Predetermined Change Control Plan Guidance for AI-Enabled Device Software Functions\" (2024-12) - Ropes & Gray, McDermott+ 알림(최종본 발행일 2024-12-03 확인용)"
        ]
    },
    {
        "n": 9,
        "case_id": "kb-eval-20260717-it01-ra_us-005",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "Special 510(k) 오용",
        "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md",
        "recorded_source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1",
        "excerpts": [
            "## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분",
            "--- doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5 title: \"FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표\" type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: \"FDA QMSR §820.35와 ISO 13485 §4.2.5 간 차이 분석 및 X-ray 시스템 기록관리 적용 지침\" applicable: [FDA QMSR 21 CFR 820, ISO13485:2016 §4.2.5, 21 CFR 803, 21 CFR 830, 21 CFR Part 11, UDI] forms: [F-QMSR-REC-001] related-docs: - FDA_QMSR_2026 - ISO13485_2016_요약 - SOP-DOC-001 - SOP-TRC-001 - SOP-FSCA-001 - SOP-PSUR-001 related-issues: [44] owner: RA/QA Lead last-review: 2026-05-25 review-due: 2027-05-25 --- # FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표"
        ]
    },
    {
        "n": 10,
        "case_id": "kb-eval-20260717-it01-ra_us-003",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "PMA 약어 오독",
        "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md",
        "recorded_source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd",
        "excerpts": [
            "## 갭 내용 | 조항 | 요구사항 | 현재 상태 | |------|----------|-----------| | §8.1 | 적합성·효과성·개선 모니터링·분석·개선 계획 | partial | | §8.2.5 | 프로세스 성과 모니터링·미달 시 CAPA 트리거 | partial | | §8.5.1 | 품질정책·목표·감사·분석·시정·MR 통한 효과성 개선 | partial |",
            "## Definition of Done - [ ] `02_품질경영시스템_QMS/SOP-PMA-001_프로세스_모니터링_분석_절차.md` 신규 (v0.1) - 프로세스 카탈로그(설계·구매·제조·검사·서비스·PMS·CAPA·교육·문서) — 9개 - KPI 매트릭스(프로세스 × 측정지표 × 주기 × 임계치 × 소유자) — 정량 - 데이터 수집·분석 방법(통계기법: SPC·Pareto·Ishikawa) - 미달 시 트리거(CAPA·MR 입력·자원 재배치) 폐쇄루프 - §8.5.1 효과성 측정 연계(품질목표→KPI→MR) - [ ] `02_품질경영시스템_QMS/F-PMA-001_KPI_매트릭스.md` 신규 — 27개 셀(9프로세스×3차원) - [ ] CHK-ISO13485-001 ISO-8.1/8.2.5/8.5.1 `status: met` 갱신 - [ ] SOP-MR-001/SOP-CAPA-001/F-MR-001 정합성 — KPI ↔ MR 입력 ↔ CAPA 트리거 - [ ] 규제 매핑: ISO 13485 §8.1/8.2.5/8.5.1, FDA QMSR §820.250(통계기법)·§820.100(CAPA), EU MDR Art.10(9)(j) - [ ] 적대적 자기검토(심사관 모드)"
        ]
    },
    {
        "n": 11,
        "case_id": "kb-eval-20260716-it01-ra_us-005",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "supplement · EU 용어(FSN)",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md",
        "recorded_source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6",
        "excerpts": [
            "> 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...",
            "### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---"
        ]
    },
    {
        "n": 12,
        "case_id": "kb-eval-20260716-it01-ra_us-001",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "AI 기한 창작",
        "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md",
        "recorded_source_hash": "b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82",
        "excerpts": [
            "### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합",
            "> 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: https://www.fda.gov/media/73507/download (FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022) | https://medicaldeviceacademy.com/additional-information-request/ | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | MDUFA V Commitment Letter https://www.fda.gov/media/158308/download # FDA Additional Information (AI) 대응 전략 및 샘플 답변 체계"
        ]
    },
    {
        "n": 13,
        "case_id": "kb-eval-20260715-it13-ra_us-001",
        "profile": "ra-us",
        "peer": "ra_us",
        "focus": "510(k) predicate strategy",
        "defect": "RTA 오독 (미존재 기기 창작)",
        "source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md",
        "recorded_source_hash": "a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232",
        "excerpts": [
            "## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **3주 연속 0% 정체** (06-26 / 07-03 / 07-10 동일). #951(2026-07-03 등록)이 미착수 상태로 재이월됨.",
            "## 이관 배경 - 선행 이슈: #951 (2026-07-03 등록, status: draft, 착수 실적 없음) - 원인 추정: 이번 주 개발/QA 인력이 감사(audit) sweep(01_법규_규제, 02_품질경영시스템_QMS)에 전량 투입되어 체크리스트 보강 착수 못함"
        ]
    }
]


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


LEDGER = OUT_DIR / "ledger.jsonl"
LOCK = OUT_DIR / ".lock"


def ledger_append(rec: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def ledger_state() -> dict:
    starts, results, corrupt = {}, {}, 0
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except ValueError:
                corrupt += 1
                continue
            if r.get("event") == "attempt_start":
                starts[r["attempt_id"]] = r
            elif r.get("event") == "attempt_result":
                results[r["attempt_id"]] = r
    unknown = [a for a in starts if a not in results]
    return {"consumed": len(starts), "resolved": len(results), "corrupt_lines": corrupt,
            "determinable": corrupt == 0,
            "unknown": unknown, "remaining": CALL_BUDGET - len(starts),
            "attempted_case_ids": {r["case_id"] for r in starts.values()},
            "done_case_ids": {results[a]["case_id"] for a in results if results[a].get("ok")}}


def acquire_lock() -> bool:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, f"{os.getpid()} {datetime.now(timezone.utc).isoformat()}\n".encode())
    os.close(fd)
    return True


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def build_assignment(case: dict) -> str:
    """과제문 — #147 실행기와 같은 골격. 발췌는 원본 체크시트에서 verbatim."""
    lines = [
        "Daily regulatory growth case (re-query)",
        f"[internal run metadata — not a device attribute] Re-query of: {case['case_id']}",
        f"[internal run metadata — not a device attribute] Reason: #146 abbreviation-misread verification after SOUL rule update",
        f"Primary focus: {case['focus']}",
        f"Source: {case['source']}",
        f"Source hash: {case['recorded_source_hash']}",
        "Note: the lines above marked '[internal run metadata]' are pipeline bookkeeping only — "
        "they are not device names, categories, or classifications. Do not reference them when "
        "determining device type, intended use, or regulatory classification.",
        "Assignment: Produce a regulatory draft that identifies classification/submission route, "
        "required evidence, missing information, risk controls, citations, and human-escalation triggers.",
        "Cite only identifiers that appear in the source excerpts below. If the source does not "
        "contain an identifier you need, say so explicitly instead of supplying one.",
        "",
        "Source excerpts:",
    ]
    lines += [f"- {e}" for e in case["excerpts"]]
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="#146 약어 오독 13건 재질의 (기본 dry-run)")
    ap.add_argument("--execute", action="store_true", help="실제 LLM 호출 (없으면 계획만)")
    ap.add_argument("--batch", default=None,
                    help="승인 배치 이름. 지정하면 reports/kb-eval-requery-146/<batch>/ 에 "
                         "원장·락을 따로 둔다")
    a = ap.parse_args(argv)

    global OUT_DIR, LEDGER, LOCK
    if a.batch:
        import re as _re
        if not _re.fullmatch(r"[A-Za-z0-9._-]{1,64}", a.batch):
            print(json.dumps({"error": "batch 이름은 영숫자·점·밑줄·하이픈 1~64자"}, ensure_ascii=False))
            return 2
        OUT_DIR = OUT_DIR / a.batch
        LEDGER = OUT_DIR / "ledger.jsonl"
        LOCK = OUT_DIR / ".lock"

    assert len(CASES) == CALL_BUDGET, f"케이스 수({len(CASES)}) != 승인 호출 수({CALL_BUDGET})"

    plan = [{**c, "assignment": build_assignment(c)} for c in CASES]

    if not a.execute:
        print(json.dumps({
            "mode": "dry-run", "planned_calls": len(plan), "call_budget": CALL_BUDGET,
            "output_dir": rel(OUT_DIR),
            "touches_original_checksheets": False,
            "cases": [{"n": p["n"], "case_id": p["case_id"],
                       "source": p["source"].split("/")[-1], "defect": p["defect"],
                       "excerpts": len(p["excerpts"]),
                       "assignment_chars": len(p["assignment"])} for p in plan],
        }, ensure_ascii=False, indent=2))
        return 0

    if not acquire_lock():
        owner = ""
        try:
            owner = LOCK.read_text(encoding="utf-8").strip()
        except OSError:
            pass
        print(json.dumps({
            "error": "락이 잡혀 있다 — 다른 실행이 진행 중이거나 비정상 종료로 남은 것이다",
            "lock": rel(LOCK), "lock_owner": owner or "(읽을 수 없음)",
            "steps": ["1. 위 PID 가 살아 있는지 확인", "2. 살아 있으면 기다린다",
                      "3. 죽어 있으면 원장 ledger.jsonl 로 소비 호출 수 확인 후 재개"],
        }, ensure_ascii=False, indent=2))
        return 2

    try:
        st = ledger_state()
        if not st["determinable"]:
            print(json.dumps({"error": "원장에 손상된 줄이 있어 소비 호출 수를 확정할 수 없다",
                              "corrupt_lines": st["corrupt_lines"], "ledger": rel(LEDGER)}, ensure_ascii=False, indent=2))
            return 2
        if st["remaining"] <= 0:
            print(json.dumps({"error": "승인 예산 소진", **st}, ensure_ascii=False, indent=2, default=list))
            return 2
        if st["unknown"]:
            print(json.dumps({"error": "결과 없는 시도(unknown)가 있어 재개하지 않는다",
                              "unknown": st["unknown"], "consumed": st["consumed"],
                              "ledger": rel(LEDGER)}, ensure_ascii=False, indent=2))
            return 2

        sheet = _load("kb_eval_checksheet_146", "kb-eval-checksheet.py")
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        todo = [p for p in plan if p["case_id"] not in st["attempted_case_ids"]]
        used = 0
        for p in todo:
            if used >= st["remaining"]:
                break
            attempt_id = f"{run_id}-{p['n']:02d}"
            ledger_append({"event": "attempt_start", "attempt_id": attempt_id,
                           "case_id": p["case_id"], "profile": p["profile"],
                           "source_path": p["source"], "recorded_source_hash": p["recorded_source_hash"],
                           "defect": p["defect"],
                           "assignment": p["assignment"], "excerpt_chars": len(p["assignment"]),
                           "ts": datetime.now(timezone.utc).isoformat()})
            used += 1
            text, error = sheet.capture_agent_response(p["profile"], p["assignment"])
            ok = not error and bool(text and text.strip())
            ledger_append({"event": "attempt_result", "attempt_id": attempt_id,
                           "case_id": p["case_id"], "ok": ok, "error": error or None,
                           "chars": len(text or ""),
                           "defect": p["defect"],
                           "response": text or "",
                           "ts": datetime.now(timezone.utc).isoformat()})

        st2 = ledger_state()
        ok_n = len(st2["done_case_ids"])
        failed_n = st2["resolved"] - ok_n
        missing_n = len(CASES) - ok_n
        print(json.dumps({
            "mode": "execute", "run_id": run_id, "calls_this_run": used,
            "budget": CALL_BUDGET, "consumed_total": st2["consumed"],
            "recorded": st2["resolved"], "ok": ok_n, "failed": failed_n,
            "unknown": st2["unknown"],
            "remaining_cases": missing_n, "remaining_budget": st2["remaining"],
            "ledger": rel(LEDGER),
            "lineage_note": "원본 체크시트는 수정하지 않았다. 발췌·source_hash 는 원본 기록값을 verbatim 사용.",
        }, ensure_ascii=False, indent=2))
        return 0 if (missing_n == 0 and failed_n == 0 and not st2["unknown"]) else 1
    finally:
        LOCK.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
