=== Daily Monitoring Report ===
Date: 2026-10-17
Timestamp: 2026-10-17T08:00:00+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] Advisory API (:8643) healthy
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running
- [x] Backup last run OK (OK 20261017-043000 daily, 3h ago)

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-10-17.json

### Current Metrics
{
  "correction_rate": {
    "value": 0.2,
    "numerator": 3,
    "denominator": 15,
    "case_defects": {
      "count": 1,
      "corrected": 0,
      "capture_failed": 0,
      "source_mismatch": 0,
      "kb_source_error": 1,
      "unevaluated_legacy": 0
    },
    "excluding_case_defects": {
      "value": 0.21428571428571427,
      "numerator": 3,
      "denominator": 14,
      "meaning": "conditional correction rate over cases with no input-defect flag; NOT agent attribution (output defects are not judged here, #147)"
    },
    "samples": [
      {
        "session": "kb-eval-feedback-2026-10-16",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "EU 용어 혼입 — 원문의 'EU MDR NB Deficiency (참고)' 절(PMCF·Class IIb·30~90일)을 미국 510(k) AI 대응 증거표에 병합. FDA 대응 표에는 PMCF/Class IIb가 없어야 함(#146 G4 계열). AI 응답 기한 180일은 정확(이전 30일 창작 해소)."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-16",
        "actor": "ra_eu",
        "score": 2,
        "changed": {
          "note": "'full technical-documentation assessment (Annex II)' — Annex II는 기술문서 '구조'이고 심사 '경로'는 Annex IX(#134 인접). Rule 11 가정·AI Act Art 6(1)(IIa+ 고위험)은 정확."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-16",
        "actor": "ra_kr",
        "score": 2,
        "changed": {
          "note": "① 'QMSR (MFDS 품질관리시스템 인증)' — QMSR은 FDA 21 CFR 820 규정명이며 MFDS 인증제도가 아님(원문 KGMP/QMSR 비교표를 관할 혼동). ② 'MFMF requires' → MFDS 오타(10-15 kr-005 재발). ③ 외국 CER 인정과 OECD-MAD(비임상 GLP)를 다시 병합(#129 전철). 등급 미확정 보류·1~4등급 표기는 정확(#145 유지)."
        },
        "case_defect": null
      }
    ],
    "direction": "down",
    "note": "fraction of human-reviewed decisions where agent was overridden (system-level; excluding_case_defects is a conditional rate, not attribution, #147)"
  },
  "first_pass_match_accuracy": {
    "value": 0.0,
    "numerator": 0,
    "denominator": 15,
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
    "value": 3,
    "yellow_total": 0,
    "correction_total": 3,
    "yellow_by_domain": {},
    "correction_by_domain": {
      "quality_capa": 1,
      "unclassified": 2
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
        "session": "kb-eval-feedback-2026-10-16",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-16",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-16",
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
- **PASS**: 9
- **WARN**: 1
- **FAIL**: 0

## 5. Status
🟢 **NORMAL (인프라 점검 범위, 경고 1건)** - 실패 없음. 경고 항목은 위 목록 확인

> **이 점검이 확인하지 않은 것**: 메일 유입과 mail-triage 처리 경로는 검사 대상이 아니다.
> 위 판정은 인프라 구성요소의 응답 여부이며, **메일이 실제로 처리되고 있다는 증거가 아니다**.
> 처리 여부는 n8n 실행 이력과 OpenProject 반영으로 따로 확인해야 한다 (#141).
