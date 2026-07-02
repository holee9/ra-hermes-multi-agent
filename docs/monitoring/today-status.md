=== Daily Monitoring Report ===
Date: 2026-07-02
Timestamp: 2026-07-02T09:45:24+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-07-02.json

### Current Metrics
{
  "correction_rate": {
    "value": null,
    "numerator": 0,
    "denominator": 0,
    "samples": [],
    "direction": "down",
    "note": "fraction of human-reviewed decisions where agent was overridden"
  },
  "first_pass_match_accuracy": {
    "value": null,
    "numerator": 0,
    "denominator": 0,
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
    "value": 0,
    "yellow_total": 0,
    "correction_total": 0,
    "yellow_by_domain": {},
    "correction_by_domain": {},
    "strongest_domain": null,
    "domains": [
      "clinical_evaluation",
      "coordination",
      "cybersecurity",
      "pms_vigilance",
      "quality_capa"
    ],
    "samples": [],
    "direction": "diagnostic",
    "note": "early absence-pattern signal for specialist expansion; not an auto-create trigger"
  }
}
- [x] Growth metrics available

## 3. Growth Loop Status
=======================
- [x] daily-growth-runner available
- [x] Today's growth execution found
- [x] Study scheduler checkpoint exists
Bootstrap progress: N/A

## 4. Summary
=========
- **PASS**: 8
- **WARN**: 0
- **FAIL**: 0

## 5. Status
🟢 **NORMAL** - All critical systems operational
