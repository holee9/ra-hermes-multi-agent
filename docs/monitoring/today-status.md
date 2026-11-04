=== Daily Monitoring Report ===
Date: 2026-11-04
Timestamp: 2026-11-04T08:00:00+09:00

## 1. System Status
=================
- [x] Honcho API healthy
- [x] Advisory API (:8643) healthy
- [x] KB watch: 23 files changed, all reflected in pgvector
- [x] PostgreSQL pgvector ready
- [x] Redis responsive
- [x] Honcho deriver running
- [x] Backup last run OK (OK 20261104-043000 daily, 3h ago)

## 2. Growth Metrics
=================
Latest report: reports/growth-2026-11-04.json

### Current Metrics
{
  "correction_rate": {
    "value": 0.034482758620689655,
    "numerator": 1,
    "denominator": 29,
    "case_defects": {
      "count": 1,
      "corrected": 0,
      "capture_failed": 0,
      "source_mismatch": 0,
      "kb_source_error": 1,
      "unevaluated_legacy": 0
    },
    "excluding_case_defects": {
      "value": 0.03571428571428571,
      "numerator": 1,
      "denominator": 28,
      "meaning": "conditional correction rate over cases with no input-defect flag; NOT agent attribution (output defects are not judged here, #147)"
    },
    "samples": [
      {
        "session": "kb-eval-feedback-2026-11-02",
        "actor": "ra_kr",
        "score": 1,
        "changed": {
          "note": "① \"Korean labeling & IFU — format per MFDS 고시 제16조 SBOM 관리\" — 라벨링 형식과 SBOM 보안지침의 부자연스러운 결합(식별자 오배선) ② 외국 CER 인정 고시 날짜 '2025-01-10' — 동일 소스의 사이버보안 가이드라인 날짜 오전용 ③ Generator '1등급(비의료기기)→신고' 자기모순적 서술. / **1점 확정**: ① 'MFDS notice expanding foreign CER acceptance (2025-01-10)' — 동일 소스의 사이버보안 가이드라인 날짜 오전용 ② 'Korean labeling & IFU format per 고시 제16조 SBOM 관리' — 라벨링 형식과 SBOM 보안지침 식별자 오결합 ③ 'Korean guidance classifies such systems as 3등급...' 등 근거 없는 등급 규칙 서술(창작) ④ Generator '1등급(비의료기기)→신고' 자기모순. 체계적 식별자 오결합+규칙 창작 → 정정 필요."
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
    "denominator": 29,
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
    "value": 1,
    "yellow_total": 0,
    "correction_total": 1,
    "yellow_by_domain": {},
    "correction_by_domain": {
      "unclassified": 1
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
        "session": "kb-eval-feedback-2026-11-02",
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
[내부?/infra-ref] docs/monitoring/today-status.md:438 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:439 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:440 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:444 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:445 — NAS mount path: /mnt/nas
[내부?/infra-ref] docs/monitoring/today-status.md:447 — NAS mount path: /mnt/nas
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
[내부?/infra-ref] docs/monitoring/today-status.md:133 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:134 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:135 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:375 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:376 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:377 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:378 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:379 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:380 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:381 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:382 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:383 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:384 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:385 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:386 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:387 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:388 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:389 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:390 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:391 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:392 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:393 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:394 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:395 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:396 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:397 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:398 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:399 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:400 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:401 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:402 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:403 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:404 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:405 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:406 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:407 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:408 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:409 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:410 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:411 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:412 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:413 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:414 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:415 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:416 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:417 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:418 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:419 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:420 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:421 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:422 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:423 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:424 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:425 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:426 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:427 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:428 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:429 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:430 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:431 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:432 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:433 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:434 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:435 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:436 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:437 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:441 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:442 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:443 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:446 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:448 — internal Gitea repo reference (DR_RnD): DR_RnD/
[내부?/infra-ref] docs/monitoring/today-status.md:449 — internal Gitea repo reference (DR_RnD): DR_RnD/
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
scan complete: 0 CONTENT finding(s) across 442 tracked files
```
