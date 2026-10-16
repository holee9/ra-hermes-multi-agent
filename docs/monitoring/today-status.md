=== Daily Monitoring Report ===
Date: 2026-10-16
Timestamp: 2026-10-16T08:00:00+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running
- [x] Backup last run OK (OK 20261016-043000 daily, 3h ago)

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-10-16.json

### Current Metrics
{
  "correction_rate": {
    "value": 0.7333333333333333,
    "numerator": 11,
    "denominator": 15,
    "case_defects": {
      "count": 0,
      "corrected": 0,
      "capture_failed": 0,
      "source_mismatch": 0,
      "kb_source_error": 0,
      "unevaluated_legacy": 0
    },
    "excluding_case_defects": {
      "value": 0.7333333333333333,
      "numerator": 11,
      "denominator": 15,
      "meaning": "conditional correction rate over cases with no input-defect flag; NOT agent attribution (output defects are not judged here, #147)"
    },
    "samples": [
      {
        "session": "kb-eval-feedback-2026-10-15",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "'predicate의 Device History Files' → predicate 공개문서는 510(k) Summary(DHF는 자사 내부 문서)로 수정. §892.2050 검증 플래그 처리는 모범적."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "'차이 ≤/> 30%' — FDA SE 기준에 존재하지 않는 수치. SE는 정성 판정(2014 'The 510(k) Program' 가이던스). 경로별 근거표(§510(k)·§513(f)(2)/§860·§515/§814)는 원문 충실."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
        "actor": "ra_us",
        "score": 2,
        "changed": {
          "note": "FDA 사이버 가이던스 '2022' 인용 오류 — 2018 초안→2023-09-27 최종, 2022 판본 부재(10-10 us-004 이후 재발, #134). Predicate 체크리스트 7단계는 원문 완전 충실."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
        "actor": "ra_us",
        "score": 1,
        "changed": {
          "note": "① 'De Novo per 21 CFR §814.94' — De Novo는 Part 860 Subpart D(§860.200~260), §814.94는 PMA 조항. ② '§807.90 classification criteria' — §807.90은 510(k) 제출 양식 조항. ③ 'ISO 14971:2023' 부존재 판본(현행 2019; 10-10 '14971:2021'과 동일 계열의 판본 창작). ④ 'SW >30%'·'위험 1×10⁻³' 근거 없는 수치. ※ '10년 내 predicate'는 FDA 초안 가이던스(2023-09)의 실제 권고 기준이나 무출처. 원문이 4줄 뼈대(v0.1)라 대부분 일반지식으로 구성."
        },
        "case_defect": null
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
        "actor": "ra_eu",
        "score": 2,
        "changed": {
          "note": "① '선택 루트: Annex IX + Annex XI' — 존재하지 않는 조합(Art 52(4): Annex IX 단독 또는 Annex X+XI; 10-14 eu-002 이후 재발, #134). ② 'EUDAMED Art 33-39' — UDI/등록은 Art 27·28·29-31, EUDAMED 33-34(35-39는 인증기관 조문). GSPR §16.4/§17/§18·PSUR 연1회는 정확."
        },
        "case_defect": null
      }
    ],
    "direction": "down",
    "note": "fraction of human-reviewed decisions where agent was overridden (system-level; excluding_case_defects is a conditional rate, not attribution, #147)"
  },
  "first_pass_match_accuracy": {
    "value": 1.0,
    "numerator": 15,
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
    "value": 11,
    "yellow_total": 0,
    "correction_total": 11,
    "yellow_by_domain": {},
    "correction_by_domain": {
      "clinical_evaluation": 1,
      "cybersecurity": 1,
      "unclassified": 9
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
        "session": "kb-eval-feedback-2026-10-15",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
        "domain": "cybersecurity",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
        "domain": "unclassified",
        "yellow_reason": null,
        "record_type": "score_given",
        "type": "score_given"
      },
      {
        "session": "kb-eval-feedback-2026-10-15",
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
