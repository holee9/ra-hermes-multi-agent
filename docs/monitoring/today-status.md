=== Daily Monitoring Report ===
Date: 2026-11-16
Timestamp: 2026-11-16T08:00:00+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] Advisory API (:8643) healthy
- [x] KB watch: no repo changes in window
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running
- [x] Backup last run OK (OK 20261116-043000 daily, 3h ago)

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-11-16.json

### Current Metrics
{
  "correction_rate": {
    "value": null,
    "numerator": 0,
    "denominator": 0,
    "case_defects": {
      "count": 0,
      "corrected": 0,
      "capture_failed": 0,
      "source_mismatch": 0,
      "kb_source_error": 0,
      "unevaluated_legacy": 0
    },
    "excluding_case_defects": {
      "value": null,
      "numerator": 0,
      "denominator": 0,
      "meaning": "conditional correction rate over cases with no input-defect flag; NOT agent attribution (output defects are not judged here, #147)"
    },
    "samples": [],
    "direction": "down",
    "note": "fraction of human-reviewed decisions where agent was overridden (system-level; excluding_case_defects is a conditional rate, not attribution, #147)"
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
[내부?/infra-ref] docs/monitoring/today-status.md:171 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:172 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:173 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:174 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:175 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:176 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:177 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:178 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:179 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:180 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:181 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:182 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:183 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:184 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:185 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:186 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:187 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:188 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:189 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:190 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:191 — NAS mount path: /mnt/nas
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
[내부?/infra-ref] docs/monitoring/today-status.md:219 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:220 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:221 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:222 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:223 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:224 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:225 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:226 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:227 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:228 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:229 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:230 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:231 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:232 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:233 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:234 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:235 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:236 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:237 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:238 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:239 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:240 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:241 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:242 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:243 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:244 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:245 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:246 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:247 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:248 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:249 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:250 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:251 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:252 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:253 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:254 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:255 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:256 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:257 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:258 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:259 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:260 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:261 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:262 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:263 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:264 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:265 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:266 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:267 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:268 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:269 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:270 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:271 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:272 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:273 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:274 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:275 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:276 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:277 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:278 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:279 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:280 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:281 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:282 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:283 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:284 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:285 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:286 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:287 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:288 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:289 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:290 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:291 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:292 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:293 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:294 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:295 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:296 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:297 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:298 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:299 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:300 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:301 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:302 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:303 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:304 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:305 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:306 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:307 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:308 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:309 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:310 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:311 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:312 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:313 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:314 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:315 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:316 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:317 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:318 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:319 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:320 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:321 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:322 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:323 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:324 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:325 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:326 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:327 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:328 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:329 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:330 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:331 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:332 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:333 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:334 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:335 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:336 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:337 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:338 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:339 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:340 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:341 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:342 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:343 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:344 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:345 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:346 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:347 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:348 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:349 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:350 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:351 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:352 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:353 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:354 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:355 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:356 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:357 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:358 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:359 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:360 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:361 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:362 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:363 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:364 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:365 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:366 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:367 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:368 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:369 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:370 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:371 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:372 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:373 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:374 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:375 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:376 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:377 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:378 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:379 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:380 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:381 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:382 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:383 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:384 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:385 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:386 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:387 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:388 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:389 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:390 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:391 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:392 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:393 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:394 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:395 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:396 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:397 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:398 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:399 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:400 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:401 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:402 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:403 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:404 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:405 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:406 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:407 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:408 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:409 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:410 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:411 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:412 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:413 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:414 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:415 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:416 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:417 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:418 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:419 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:420 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:421 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:422 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:423 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:424 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:425 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:426 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:427 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:428 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:429 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:430 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:431 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:432 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:433 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:434 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:435 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:436 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:437 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:438 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:439 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:440 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:441 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:442 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:443 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:444 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:445 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:446 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:447 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:448 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:449 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:450 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:451 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:452 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:453 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:454 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:455 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:456 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:457 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:458 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:459 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:460 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:461 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:462 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:463 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:464 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:465 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:466 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:467 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:468 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:469 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:470 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:471 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:472 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:473 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:474 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:475 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:476 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:477 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:478 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:479 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:480 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:481 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:482 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:483 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:484 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:485 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:486 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:487 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:488 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:489 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:490 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:491 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:492 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:493 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:494 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:495 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:496 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:497 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:498 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:499 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:500 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:501 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:502 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:503 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:504 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:505 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:506 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:507 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:508 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:509 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:510 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:511 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:512 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:513 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:514 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:515 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:516 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:517 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:518 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:519 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:520 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:521 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:522 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:523 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:524 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:525 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:526 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:527 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:528 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:529 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:530 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:531 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:532 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:533 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:534 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:535 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:536 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:537 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:538 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:539 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:540 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:541 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:542 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:543 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:544 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:545 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:546 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:547 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:548 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:549 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:550 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:551 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:552 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:553 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:554 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:555 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:556 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:557 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:558 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:559 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:560 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:561 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:562 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:563 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:564 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:565 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:566 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:567 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:568 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:569 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:570 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:571 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:572 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:573 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:574 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:575 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:576 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:577 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:578 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:579 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:580 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:581 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:582 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:583 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:584 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:585 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:586 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:587 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:588 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:589 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:590 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:591 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:592 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:593 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:594 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:595 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:596 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:597 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:598 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:599 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:600 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:601 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:602 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:603 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:604 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:605 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:606 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:607 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:608 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:609 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:610 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:611 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:612 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:613 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:614 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:615 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:616 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:617 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:618 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:619 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:620 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:621 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:622 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:623 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:624 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:625 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:626 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:627 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:628 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:629 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:630 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:631 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:632 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:633 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:634 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:635 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:636 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:637 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:638 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:639 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:640 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:641 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:642 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:643 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:644 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:645 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:646 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:647 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:648 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:649 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:650 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:651 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:652 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:653 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:654 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:655 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:656 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:657 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:658 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:659 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:660 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:661 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:662 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:663 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:664 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:665 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:666 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:667 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:668 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:669 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:670 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:671 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:672 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:673 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:674 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:675 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:676 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:677 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:678 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:679 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:680 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:681 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:682 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:683 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:684 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:685 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:686 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:687 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:688 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:689 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:690 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:691 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:692 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:693 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:694 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:695 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:696 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:697 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:698 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:699 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:700 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:701 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:702 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:703 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:704 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:705 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:706 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:707 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:708 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:709 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:710 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:711 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:712 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:713 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:714 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:715 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:716 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:717 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:718 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:719 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:720 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:721 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:722 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:723 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:724 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:725 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:726 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:727 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:728 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:729 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:730 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:731 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:732 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:733 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:734 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:735 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:736 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:737 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:738 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:739 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:740 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:741 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:742 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:743 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:744 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:745 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:746 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:747 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:748 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:749 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:750 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:751 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:752 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:753 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:754 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:755 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:756 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:757 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:758 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:759 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:760 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:761 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:762 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:763 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:764 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:765 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:766 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:767 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:768 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:769 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:770 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:771 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:772 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:773 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:774 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:775 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:776 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:777 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:778 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:779 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:780 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:781 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:782 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:954 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:955 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:956 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:960 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:961 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:963 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:966 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:967 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:968 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:969 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:970 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:971 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:972 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:973 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:974 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:975 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:976 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:977 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:978 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:979 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:980 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:981 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:982 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:983 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:984 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:985 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:986 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:987 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:988 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:989 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:990 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:991 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:992 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:133 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:134 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:135 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:783 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:784 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:785 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:786 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:787 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:788 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:789 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:790 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:791 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:792 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:793 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:794 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:795 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:796 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:797 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:798 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:799 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:800 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:801 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:802 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:803 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:804 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:805 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:806 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:807 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:808 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:809 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:810 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:811 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:812 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:813 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:814 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:815 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:816 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:817 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:818 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:819 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:820 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:821 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:822 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:823 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:824 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:825 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:826 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:827 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:828 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:829 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:830 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:831 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:832 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:833 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:834 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:835 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:836 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:837 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:838 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:839 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:840 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:841 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:842 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:843 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:844 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:845 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:846 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:847 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:848 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:849 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:850 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:851 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:852 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:853 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:854 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:855 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:856 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:857 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:858 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:859 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:860 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:861 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:862 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:863 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:864 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:865 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:866 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:867 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:868 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:869 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:870 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:871 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:872 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:873 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:874 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:875 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:876 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:877 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:878 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:879 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:880 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:881 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:882 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:883 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:884 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:885 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:886 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:887 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:888 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:889 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:890 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:891 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:892 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:893 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:894 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:895 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:896 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:897 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:898 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:899 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:900 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:901 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:902 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:903 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:904 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:905 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:906 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:907 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:908 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:909 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:910 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:911 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:912 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:913 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:914 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:915 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:916 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:917 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:918 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:919 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:920 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:921 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:922 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:923 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:924 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:925 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:926 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:927 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:928 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:929 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:930 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:931 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:932 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:933 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:934 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:935 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:936 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:937 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:938 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:939 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:940 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:941 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:942 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:943 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:944 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:945 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:946 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:947 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:948 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:949 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:950 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:951 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:952 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:953 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:957 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:958 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:959 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:962 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:964 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:965 — internal Gitea repo reference (DR_RnD): DR_RnD/
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
scan complete: 0 CONTENT finding(s) across 454 tracked files
```
