=== Daily Monitoring Report ===
Date: 2026-10-08
Timestamp: 2026-10-08T08:00:00+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running
- [x] Backup last run OK (OK 20261008-043000 daily, 3h ago)

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-10-08.json

### Current Metrics
{
  "correction_rate": {
    "value": 0.916,
    "numerator": 229,
    "denominator": 250,
    "case_defects": {
      "count": 0,
      "corrected": 0,
      "capture_failed": 0,
      "source_mismatch": 0,
      "unevaluated_legacy": 250
    },
    "excluding_case_defects": {
      "value": 0.916,
      "numerator": 229,
      "denominator": 250,
      "meaning": "conditional correction rate over cases with no input-defect flag; NOT agent attribution (output defects are not judged here, #147)"
    },
    "samples": [
      {
        "session": "kb-eval-feedback-2026-07-15",
        "actor": "ra_us",
        "score": 1,
        "changed": {
          "note": "source의 `RTA`(Refuse to Accept)를 'real-time analysis'로 오독해 존재하지 않는 무선 센서+모바일 앱 실시간 모니터링 기기를 만들어내고, predicate 후보로 `K123456`(JTX, 2023-11-15 허가)·`K234567`(RME, 2024-04-02 허가)이라는 자리표시자 K-number를 실제 허가건처럼 날짜까지 붙여 제시했다. 가이던스 식별자 `2024-009`·`2024-001`·`2023-FDA-AIML`·`GHTF HU-1`, `ISO 14971:2019 (2023 amendment)`도 모두 실재하지 않아 predicate 판단 자체가 성립하지 않는다."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "actor": "ra_eu",
        "score": 2,
        "changed": {
          "note": "source의 'Rule 5/9' 오적용을 명시적으로 반박하고 진단용은 Rule 10, 치료용은 Rule 9로 분기시킨 핵심 판단이 정확하다. 다만 'PMS plan per Annex II-23'(PMS 기술문서는 Annex III)과 IEC 62387 인용이 근거 없이 제시되어 사람이 정정해야 한다."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "actor": "ra_kr",
        "score": 2,
        "changed": {
          "note": "고시 제2025-25호·제2025-23호·디지털 GMP·총리령 제2088호를 excerpt대로 인용해 허가·인증·신고 3경로를 정리한 뼈대는 유효하다. 그러나 'OECD CER Acceptance Scope – MFDO Revision 2026-01'은 실재하지 않는 창작 출처이고, 고시 제2025-25호 제4조(사용자 교육·훈련 의무)와 개인정보보호법 시행령 제23조도 근거 없이 붙인 조문이다. 아울러 2등급을 신고로 매핑한 결론도 틀렸다(2등급은 인증)."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "핵심 판단(510(k)/De Novo/PMA 근거)은 정확하나 De Novo eSTAR 표기가 소스와 자기모순(소스는 2025-10-01부 의무화 명시)."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "actor": "ra_us",
        "score": 1,
        "changed": {
          "note": "QMSR 조항(§820.30-820.40) 세부내용을 창작(MRE 분류체계 등) — 실제 QMSR은 해당 조항 대부분을 폐지하고 ISO 13485 준용으로 대체."
        },
        "case_defect": null
      }
    ],
    "direction": "down",
    "note": "fraction of human-reviewed decisions where agent was overridden (system-level; excluding_case_defects is a conditional rate, not attribution, #147)"
  },
  "first_pass_match_accuracy": {
    "value": 0.86,
    "numerator": 215,
    "denominator": 250,
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
    "value": 229,
    "yellow_total": 0,
    "correction_total": 229,
    "yellow_by_domain": {},
    "correction_by_domain": {
      "clinical_evaluation": 63,
      "cybersecurity": 8,
      "pms_vigilance": 16,
      "quality_capa": 28,
      "unclassified": 114
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
        "session": "kb-eval-feedback-2026-07-15",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "domain": "pms_vigilance",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "domain": "clinical_evaluation",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-07-15",
        "domain": "quality_capa",
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
