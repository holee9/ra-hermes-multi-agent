# Threshold Baseline Proposal (보수적 기본값 제안)

**작성일**: 2026-06-18  
**상태**: 제안 (30일 데이터 확보 후 최종 결정)  
**대상**: issue #65 [MONITOR-2]

---

## 현재 상태

- **데이터 기간**: 3일 / 30일 (10% 달성)
- **모든 metrics**: null (실제 운영 데이터 부족)
- **위험도**: 낮음 (자동화 운영 중이 아님)

---

## 보수적 기본값 제안

### 1. duplicate_wp_reduction (중복 WP 감소율)

**현재 상태**: 중복 WP 데이터 없음

**제안 기본값**:
```json
{
  "threshold": 0.95,
  "direction": "above",
  "window_days": 7,
  "consecutive_days_required": 3,
  "next_action": "review_duplicate_detection_logic"
}
```

**근거**:
- 95% 이상 중복 감소 → duplicate detection 로직 개선
- 7일 이동 평균 안정화 확인 필요
- 3일 연속 달성 → 로직 적용 검토

**운영 영향**:
- [LOW] threshold 달성 시 로직 개선 권고
- [HIGH] 중복 WP 증가 시 즉시 조사

---

### 2. human_correction_rate (사람 정정 비율)

**현재 상태**: 사람 정정 데이터 없음

**제안 기본값**:
```json
{
  "threshold": 0.15,
  "direction": "below",
  "window_days": 7,
  "consecutive_days_required": 5,
  "next_action": "review_agent_guidance_quality"
}
```

**근거**:
- 15% 이하 → 사람 정정 감소는 성숙 신호
- 5일 연속 확인 → 안정화 판단
- 7일 이동 평균 사용

**운영 영향**:
- [MEDIUM] threshold 초과 시 agent prompts 재검토
- [HIGH] 지속 15% 초과 시 model 재훈련 고려

---

### 3. transition_accuracy (전이 제안 정확도)

**현재 상태**: 전이 데이터 없음

**제안 기본값**:
```json
{
  "threshold": 0.85,
  "direction": "above",
  "window_days": 7,
  "consecutive_days_required": 3,
  "next_action": "approve_expansion_candidate"
}
```

**근거**:
- 85% 이상 → 전이 전문가 성숙
- 3일 연속 달성 → 검증 완료 판단
- 7일 이동 평균 사용

**운영 영향**:
- [MEDIUM] threshold 달성 시 form workflow 이관 승인
- [HIGH] 85% 미달 시 전이 로직 재검토

---

### 4. mail_triage_stability (mail-triage 안정성)

**현재 상태**: mail-triage 안정화 중

**제안 기본값**:
```json
{
  "threshold": 0.90,
  "direction": "below",
  "stable_days_required": 30,
  "consecutive_days_required": 7,
  "secondary_metrics": ["first_pass_match_accuracy", "escalation_precision"],
  "next_action": "notify_form_workflow_ready"
}
```

**근거**:
- 90% 이하 안정화 → form workflow 후보
- 30일 안정 기간 + 7일 연속 확인
- 2차 metrics 복합 검증

**운영 영향**:
- [HIGH] form workflow 이관 승인
- [CRITICAL] 안정화 미달시 mail-triage 로직 수정

---

## ⚠️ 주의사항

1. **이 제안은 30일 데이터 확보 후 재검토됨**
   - 현재 3일 데이터만으로는 통계적 의미 없음
   - 실제 운영 패턴 반영 후 조정 필요

2. **Auto-trigger 비활성 정책 유지**
   - 사람 승인 없이 자동 작동 금지
   - notification은 alert 수단으로만 활용

3. **Forbidden basis 엄격 준수**
   - KR 20% pre-activation floor는 trigger 기준으로 사용 금지
   - Dashboard visual state만으로는 trigger 금지

---

## 📋 검토 일정

- [ ] Day 15: 중간 데이터 검토 (15일 metrics 확보 시점)
- [ ] Day 25: 2차 검토 (25일 metrics 확보 시점)
- [ ] Day 30: 최종 threshold 결정 (전체 데이터 분석 기반)

---

## 🎯 다음 단계

1. **현재 제안을 growth-trigger-config.json에 반영 여부 결정**
2. **30일 data collection 계획 수립**
3. **notification webhook 기본 구조 설정**
