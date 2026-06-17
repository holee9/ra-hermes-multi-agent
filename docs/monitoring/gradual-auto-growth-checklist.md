# 점진적 자동화 체크리스트

## Day 1-3: 강화 모니터링 + 일일 리뷰

### 매일 확인 항목 (Daily)

#### 1. 시스템 상태 확인
- [ ] Honcho API 정상 작동 (`curl -f http://localhost:8000/health`)
- [ ] PostgreSQL pgvector 정상 (`docker exec honcho-postgres-1 pg_isready`)
- [ ] Redis 정상 (`docker exec honcho-redis-1 redis-cli ping`)
- [ ] Honcho deriver 실행 중 (`docker ps | grep deriver`)

#### 2. 성장 루프 상태 확인
- [ ] `daily-growth-runner.py --dry-run` 실행 결과 확인
- [ ] `autonomous-study-scheduler.py` checkpoint 상태 확인
- [ ] `curriculum-seed.py` 로그 확인

#### 3. 성장 지표 기록
- [ ] correction_rate (기대값: 0.85+)
- [ ] first_pass_match_accuracy (기대값: 0.80+)
- [ ] confidence_calibration (기대값: ±0.10 이내)
- [ ] warmstart_lift (기대값: 0.20+)
- [ ] escalation_precision (기대값: 0.90+)

#### 4. Deriver Backlog 확인
- [ ] 현재 backlog 크기 (기대값: 50 미만)
- [ ] 24시간 내 처리 완료율 (기대값: 95%+)
- [ ] 오류 없는 처리율 (기대값: 99%+)

#### 5. RA Agents 세션 상태
- [ ] ra_us 세션 정상 (마지막 활동 24시간 이내)
- [ ] ra_eu 세션 정상 (마지막 활동 24시간 이내)
- [ ] ra_kr 세션 정상 (마지막 활동 24시간 이내)

### 이상 발견 시 대응
- [ ] ERROR 레벨 이벤트 발생 시 즉시 조치
- [ ] WARNING 레벨 이벤트 발생 시 2시간 내 조치
- [ ] 성장 지표가 ±15% 벗어날 시 즉시 조치

### Day 1-3 성공 기준
- [ ] 3일 연속 오류 없는 실행
- [ ] 성장 지표가 baseline에서 ±10% 이내 유지
- [ ] Deriver backlog가 누적되지 않음 (50 미만 유지)

---

## Day 4-5: 부분 자동화 시작

### 실행 전 확인 (Pre-execution)

#### 1. 실행 계획 승인
- [ ] 오늘 실행할 agent 선택 (ra-us → ra-eu → ra-kr 순서)
- [ ] 실행 모드 확인 (단일 agent에서 시작)
- [ ] 실행 시간대 결정 (업무 시간 외 권장)

#### 2. 시스템 상태 확인
- [ ] Day 1-3의 모든 매일 확인 항목 통과
- [ ] Deriver backlog가 30 미만인 상태

### 실행 중 모니터링

#### 1. 실행 시작 후 2시간
- [ ] 프로세스 정상 실행 중 확인
- [ ] 로그에 ERROR/CRITICAL 없음 확인
- [ ] 생성된 성장 케이스 품질 검토

#### 2. 실행 시작 후 4시간
- [ ] Deriver가 새로운 케이스 정상 처리 중 확인
- [ ] 성장 지표가 정상 범위 내 유지 확인

### 매일 확인 항목 (Day 4-5)
- [ ] Day 1-3의 모든 매일 확인 항목 동일하게 수행
- [ ] 추가: 실행된 agent의 생성 케이스 수량 확인
- [ ] 추가: 생성된 케이스의 정확성 검토 (샘플 10건)

### Day 4-5 성공 기준
- [ ] 2일 연속 사람 개입 없이 정상 완료
- [ ] 생성된 성장 케이스 품질 검증 통과 (90%+ 정확도)
- [ ] Honcho deriver가 정상적으로 모든 케이스 처리

---

## Day 6-7: Full 자동화 전환

### Day 6 아침 전환 승인

#### 1. 사전 조건 확인
- [ ] Day 1-5의 모든 성공 기준 통과
- [ ] 모든 3개 agent가 개별적으로 --execute 모드 성공
- [ ] Deriver backlog가 20 미만인 상태

#### 2. 전환 계획 승인
- [ ] 전체 agent 동시 실행 시간대 결정
- [ ] SystemD timer 활성화 시간 결정
- [ ] ERROR 알림 수신 방법 확인

### Day 6-7 실행 중 모니터링

#### 1. 실행 시작 후 2시간
- [ ] 모든 agent 정상 실행 중 확인
- [ ] Deriver가 모든 agent의 케이스 정상 처리 중 확인
- [ ] 전체 시스템 부하 확인 (CPU, Memory, Disk)

#### 2. 4시간 간격 점검 (Day 6-7)
- [ ] 오류 없는 지속 실행 확인
- [ ] 성장 지표가 정상 범위 내 유지 확인
- [ ] Deriver 처리 속도가 생성 속도를 따라가는지 확인

### ERROR 알림 대응 프로세스
- [ ] ERROR 레벨 이벤트 발생 시 즉시 알림 수신
- [ ] 10분 내에 원인 파악
- [ ] 30분 내에 대응 조치 결정
- [ ] 1시간 내에 조치 실행

### Day 6-7 성공 기준 (7일 차 완료 조건)
- [ ] 2일 연속 무인 정상 운영
- [ ] 모든 성장 지표가 목표 범위 내 유지
  - correction_rate: 0.85+
  - first_pass_match_accuracy: 0.80+
  - confidence_calibration: ±0.10 이내
  - warmstart_lift: 0.20+
  - escalation_precision: 0.90+
- [ ] ERROR 레벨 이벤트가 0건
- [ ] 사람 개입 필요시 모든 알림 정상 작동

---

## 7일 후 완료 시점 확인 항목

### 최종 승인 전 확인
- [ ] 모든 성공 기준 통과 확인
- [ ] 7일 전체 로그 검토 (ERROR, WARNING 이벤트 분석)
- [ ] 성장 지표 추세 분석 (개선 여부 확인)
- [ ] Deriver 처리 성능 분석 (병목 없는지 확인)

### SystemD Timer 영구 활성화
- [ ] `hermes-auto-growth.timer` 영구 활성화
- [ ] `hermes-auto-growth.service` 정상 작동 확인
- [ ] Timer schedule 확인 (매일 실행 시간대)
- [ ] ERROR 알림 시스템 정상 작동 확인

### 영구적 운영 모드 전환
- [ ]密集 모니터링 종료
- [ ] 이상 감시 위주의 경량 모니터링 시작
- [ ] 주간 리포트 스케줄 설정
- [ ] 월간 성장 리포트 스케줄 설정

### 최종 승인
- [ ] 7일 점진적 자동화 완료 보고
- [ ] 영구적 운영 모드 전환 승인
- [ ] README.md 상태 표 갱신 (자동성장 ✅ 완료)
