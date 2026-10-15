=== Daily Monitoring Report ===
Date: 2026-10-15
Timestamp: 2026-10-15T08:00:00+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running
- [x] Backup last run OK (OK 20261015-043000 daily, 3h ago)

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-10-15.json

### Current Metrics
{
  "correction_rate": {
    "value": 0.9,
    "numerator": 27,
    "denominator": 30,
    "case_defects": {
      "count": 1,
      "corrected": 1,
      "capture_failed": 0,
      "source_mismatch": 1,
      "kb_source_error": 0,
      "unevaluated_legacy": 0
    },
    "excluding_case_defects": {
      "value": 0.896551724137931,
      "numerator": 26,
      "denominator": 29,
      "meaning": "conditional correction rate over cases with no input-defect flag; NOT agent attribution (output defects are not judged here, #147)"
    },
    "samples": [
      {
        "session": "kb-eval-feedback-2026-10-10",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "Class B로 단정하며 원문의 'AEC·판독지원 포함 시 Class C 가능(Pre-Sub 확인)' 조건 누락. 'Class III 또는 De Novo', 'Special 510(k)/FDA-approved amendment'는 근거 없는 경로 서술(같은 KB PCCP 가이드 81행: Special 510(k) PCCP 불허)."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "PCCP 4요소·FR 2024-28361 정확. 'IEC 82304-2 기준 Class II risk'(존재하지 않는 등급 개념)와 '편향 발견 시 FDA notification'(근거 없음) 수정 필요. 기기 정보 없이 892.2050/Class II 전제."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "원문의 범위 밖 변경 3경로(새 510(k)/De Novo/PMA Supplement) 중 PMA Supplement 누락. 21 CFR 803.11은 보고 양식 조항(보고 의무는 803.30/803.50). '≥5% 성능 저하' 임계값은 근거 없는 수치."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "ISO 14971 현행판은 2019('ISO 14971:2021' 부존재 판본). FDA 사이버보안 가이던스는 2023-09-27 최종('2022' 인용 오류, 2025-06 개정 존재). '62304 Class C 상향 시 새 510(k)'는 논리 근거 없음."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "CVD = Coordinated Vulnerability Disclosure — 'Corrective/Preventive Action' 오풀이(2회) 수정. '연간 cybersecurity update 제출', 'SBOM 기한 미준수 30일 경과 시 FDA 통보', 'CVSS≥7.0 → MDR 803' 모두 원문 근거 없음."
        },
        "case_defect": null
      }
    ],
    "direction": "down",
    "note": "fraction of human-reviewed decisions where agent was overridden (system-level; excluding_case_defects is a conditional rate, not attribution, #147)"
  },
  "first_pass_match_accuracy": {
    "value": 1.0,
    "numerator": 30,
    "denominator": 30,
    "direction": "up",
    "note": "fraction of WP match decisions confirmed correct by human"
  },
  "confidence_calibration": {
    "value": null,
    "n_pairs": 0,
    "direction": "zero",
    "note": "Brier score: mean((confidence - actual_correct)^2). Lower → better calibrated."
  },
  "warmstart_lift": {
    "value": null,
    "warm_mean": null,
    "cold_mean": null,
    "warm_n": 0,
    "cold_n": 0,
    "direction": "positive",
    "note": "warm_mean - cold_mean (1-3 scale). Positive → memory helps."
  },
  "escalation_precision": {
    "value": null,
    "numerator": 0,
    "denominator": 0,
    "direction": "up",
    "note": "fraction of escalations that required actual human correction (score=1)"
  },
  "autonomous_study_sessions": {
    "value": 0,
    "numerator": 0,
    "denominator": null,
    "by_agent": {},
    "samples": [],
    "direction": "up",
    "note": "autonomous study sessions completed by all RA agents (higher = more self-study)"
  },
  "study_insights_count": {
    "value": 0,
    "numerator": 0,
    "denominator": null,
    "by_agent": {},
    "samples": [],
    "direction": "up",
    "note": "knowledge insights extracted during autonomous study (higher = richer knowledge base)"
  },
  "absence_pattern_signals": {
    "value": 27,
    "yellow_total": 0,
    "correction_total": 27,
    "yellow_by_domain": {},
    "correction_by_domain": {
      "clinical_evaluation": 1,
      "cybersecurity": 1,
      "quality_capa": 2,
      "unclassified": 23
    },
    "strongest_domain": "unclassified",
    "domains": [
      "clinical_evaluation",
      "coordination",
      "cybersecurity",
      "pms_vigilance",
      "quality_capa"
    ],
    "samples": [
      {
        "session": "kb-eval-feedback-2026-10-10",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "domain": "cybersecurity",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-10",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      }
    ],
    "direction": "diagnostic",
    "note": "early absence-pattern signal for specialist expansion; not an auto-create trigger"
  }
}
- [x] Growth metrics available

## 3. Growth Loop Status
=======================
- [x] daily-growth-runner available
- [ ] No today's growth execution yet ⚠️  MANUAL CHECK
- [x] Study scheduler checkpoint exists
Bootstrap progress: N/A

## 4. Summary
=========
- **PASS**: 8
- **WARN**: 1
- **FAIL**: 0

## 5. Status
🟢 **NORMAL (인프라 점검 범위, 경고 1건)** - 실패 없음. 경고 항목은 위 목록 확인

> **이 점검이 확인하지 않은 것**: 메일 유입과 mail-triage 처리 경로는 검사 대상이 아니다.
> 위 판정은 인프라 구성요소의 응답 여부이며, **메일이 실제로 처리되고 있다는 증거가 아니다**.
> 처리 여부는 n8n 실행 이력과 OpenProject 반영으로 따로 확인해야 한다 (#141).
