=== Daily Monitoring Report ===
Date: 2026-10-29
Timestamp: 2026-10-29T08:00:00+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] Advisory API (:8643) healthy
- [x] KB watch: no repo changes in window
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running
- [x] Backup last run OK (OK 20261029-043000 daily, 3h ago)

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-10-29.json

### Current Metrics
{
  "correction_rate": {
    "value": 0.0,
    "numerator": 0,
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
      "value": 0.0,
      "numerator": 0,
      "denominator": 15,
      "meaning": "conditional correction rate over cases with no input-defect flag; NOT agent attribution (output defects are not judged here, #147)"
    },
    "samples": [],
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
- [ ] No today's growth execution yet ⚠️  MANUAL CHECK
- [x] Study scheduler checkpoint exists
Bootstrap progress: N/A

## 4. Summary
=========
- **PASS**: 10
- **WARN**: 1
- **FAIL**: 0

## 5. Status
🟢 **NORMAL (인프라 점검 범위, 경고 1건)** - 실패 없음. 경고 항목은 위 목록 확인

> **이 점검이 확인하지 않은 것**: 메일 유입과 mail-triage 처리 경로는 검사 대상이 아니다.
> 위 판정은 인프라 구성요소의 응답 여부이며, **메일이 실제로 처리되고 있다는 증거가 아니다**.
> 처리 여부는 n8n 실행 이력과 OpenProject 반영으로 따로 확인해야 한다 (#141).

## Security scan (covenant v1.0)
```
[내부?/infra-ref] README.md:237 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] README.md:299 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] README.md:568 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/RA-multi-agent-master-design.md:260 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:136 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:137 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:138 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:139 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:140 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:141 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:142 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:143 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:144 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:145 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:146 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:147 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:148 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:149 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:150 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:151 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:152 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:153 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:154 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:155 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:156 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:157 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:158 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:159 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:160 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:161 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:162 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:163 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:164 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:165 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:166 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:167 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:168 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:169 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:170 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:180 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:181 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:182 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:186 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:187 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:189 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:192 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:193 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:194 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:195 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:196 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:197 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:198 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:199 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:200 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:201 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:202 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:203 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:204 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:205 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:206 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:207 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:208 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:209 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:210 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:211 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:212 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:213 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:214 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:215 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:216 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:217 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:218 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:133 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:134 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:135 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:171 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:172 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:173 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:174 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:175 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:176 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:177 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:178 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:179 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:183 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:184 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:185 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:188 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:190 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:191 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/operations-guide.md:770 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/specs/advisory-chat-channel-spec.md:608 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/specs/kb-rag-sync-spec.md:23 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/specs/kb-rag-sync-spec.md:107 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/specs/llm-wiki-operating-model.md:23 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/specs/llm-wiki-operating-model.md:45 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] profiles/souls/op-manager-SOUL.md:81 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/extract_mail_qa.py:37 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/growth-targets.json:17 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] scripts/index_ra_knowledge.py:29 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/knowledge_fetch.py:24 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] scripts/knowledge_fetch.py:43 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] scripts/meta_extractor.py:348 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/meta_extractor.py:349 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/meta_extractor.py:350 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:92 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:93 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:94 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:95 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:96 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:97 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:98 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:99 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:100 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:101 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:102 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:103 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:104 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:105 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:106 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:107 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:108 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:109 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:111 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:112 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:113 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:114 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:115 — NAS mount path: /mnt/nas
[내부?/infra-ref] scripts/nas_indexer_v2.py:116 — NAS mount path: /mnt/nas
scan complete: 0 CONTENT finding(s) across 432 tracked files
```
