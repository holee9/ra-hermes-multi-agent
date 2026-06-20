# 30일 Data Collection 운영 계획

**작성일**: 2026-06-18  
**목적**: 성장 metrics threshold 정책 수립을 위한 데이터 확보  
**대상**: issue #65 [MONITOR-2]

---

## 📊 현재 상태 (Day 3)

### 데이터 확보 현황
- **기간**: 2026-06-16 ~ 2026-06-18 (3일)
- **messages_scanned**: 302개
- **valid_metrics_days**: 3일
- **핵심 metrics**: 모두 null (실제 운영 데이터 부족)

### 인프라 상태
- ✅ daily-growth-runner: 정상 작동
- ✅ growth-metrics.py: 정상 수집
- ✅ growth-trigger-config.json: 구조 완비
- ✅ systemd 타이머: 매일 02:00 KST 실행

---

## 🎯 30일 Data Collection 목표

### 1차 목표 (Day 30까지)
- **messages_scanned**: 1,000개 이상
- **valid_metrics_days**: 30일 완료
- **correction_rate samples**: 100개 이상
- **first_pass_match samples**: 100개 이상

### 2차 목표 (운영 데이터 확보)
- **실제 운영 패턴 반영**: 사람-에이전트 상호작용
- **domain별 correction 데이터**: 5개 domain 별 20개 이상
- **confidence calibration**: 50쌍 이상 (confidence-actual 쌍)

---

## 📅 단계별 실행 계획

### Phase 0: KB 평가 채점지 fast evidence (Day 0-2)

**목표**: 30일 production 기준을 유지하면서 pilot 판단용 사람 채점 denominator를 빠르게 확보한다.

| 작업 | 주기 | 빈도 | 책임자 |
|------|------|------|---------|
| KB 평가 채점지 생성 | 수동 | 필요 시 3~6회 iteration | 시스템 엔지니어 |
| 체크박스 기반 사람 채점 | 수시 | 50~100 cases/day | RA 전문가 |
| `score_given` dry-run 검산 | 채점 후 | 매번 | 시스템 엔지니어 |
| Honcho feedback ingest | 승인 후 | 배치 단위 | 시스템 엔지니어 |

**2026-06-20 초기 상태**:
- [x] `docs/kb-eval-checksheets/2026-06-20/` 생성
- [x] 6 iterations / 90 cases 생성
- [x] ingest dry-run checked 0건 확인
- [ ] 사람 체크 완료
- [ ] `score_given` execute 반영
- [ ] growth metrics 재계산

**성공 기준**:
- [ ] `score_given` denominator 50건 이상
- [ ] RA별 최소 15건 이상 채점
- [ ] score 1/2/3 중복 체크 없음
- [ ] `first_pass_match_accuracy` 값 생성
- [ ] `correction_rate` 값 생성

### Phase 1: 기반 강화 (Day 4-10)

**목표**: 안정적인 데이터 수집 기반 마련

| 작업 | 주기 | 빈도 | 책임자 |
|------|------|------|---------|
| daily-growth-runner 안정화 | 매일 | 1회/day | RA 운영자 |
| growth-metrics.py 검증 | Day 5 | 1회 | 시스템 엔지니어 |
| error handling 개선 | Day 5 | 1회 | 시스템 엔지니어 |
| dashboard copy 자동화 | Day 6 | 1회 | 시스템 엔지니어 |

**성공 기준**:
- [ ] daily-growth-runner 7일 연속 무중단 실행
- [ ] growth metrics JSON 무결점 생성
- [ ] dashboard 최신 상태 유지

---

### Phase 2: 데이터 품질 (Day 11-20)

**목표**: 실제 운영 데이터 수집 시작

| 작업 | 주기 | 빈도 | 책임자 |
|------|------|------|---------|
| 사람 피드백 수집 시작 | 수시 | 지속 | RA 전문가 |
| correction rate 데이터 확보 | 매일 | 누적 | 자동 |
| first_pass accuracy 데이터 확보 | 매일 | 누적 | 자동 |
| domain별 correction 분류 | 주 3회 | 누적 | 자동 |

**성공 기준**:
- [ ] correction_rate samples: 50개 이상
- [ ] first_pass_match samples: 50개 이상
- [ ] domain별 데이터: 3개 domain × 10개 이상

---

### Phase 3: 안정화 검증 (Day 21-30)

**목표**: 통계적 유의성 확보

| 작업 | 주기 | 빈도 | 책임자 |
|------|------|------|---------|
| metrics 품질 분석 | Day 21, 25, 29 | 3회 | 데이터 분석가 |
| 이상치 감지 및 조치 | 수시 | 즉시 | 시스템 엔지니어 |
| threshold 기본값 검토 | Day 25 | 1회 | 운영팀 |
| 최종 threshold 제안 | Day 30 | 1회 | 운영팀 |

**성공 기준**:
- [ ] 모든 핵심 metrics: 100개 이상 samples
- [ ] 통계적 유의성 확인
- [ ] threshold baseline 제안 완성

---

## ⚠️ 위험 요소 및 완화

### 1. 데이터 품질
- **위험**: 실제 운영 데이터가 부족할 경우
- **완화**: Day 15 중간 점검, 데이터 품질 저하시 조치

### 2. 시스템 안정성
- **위험**: growth-metrics 실행 실패
- **완화**: 에러 모니터링, fallback 메커니즘 구현

### 3. 분석 기준 부족
- **위험**: 30일 후에도 통계적 유의성 확보 불가
- **완화**: 중간 분석 기준 마련, 전문가 검토

---

## 📋 모니터링 체크리스트

### 일일 (매일 02:00 KST 자동 실행)
- [ ] growth-metrics.py 실행 확인
- [ ] JSON 생성 확인
- [ ] dashboard 업데이트 확인
- [ ] 에러 로그 확인

### 주간 (매주 금요일 10:00)
- [ ] 지난 주 데이터 품질 확인
- [ ] metrics samples 누적 현황
- [ ] 이슈 발생 시 조치

### 중간 점검 (Day 15, 25)
- [ ] 전체 데이터 품질 검토
- [ ] threshold baseline 조정
- [ ] 남은 15일 계획 조정

---

## 🎯 Day 30 최종 산출물

1. **Threshold 최종 제안** (`docs/proposals/threshold-baseline-proposal.md` 업데이트)
2. **Data Collection 완료 보고서** (`docs/reports/30-day-data-collection-summary.md`)
3. **운영 정책 제안** (`feedback/config/growth-trigger-config.json` 업데이트)
4. **Notification 웹훅 설정** (webhook URL 설정)

---

## 🚀 현재 실행 가능한 작업

### 즉시 실행 (오늘)
- [x] threshold baseline 제안 작성
- [ ] Day 15 중간 점겁 일정 확정
- [ ] monitoring dashboard 개선

### 단기 실행 (이번 주)
- [ ] growth-metrics.py error handling 개선
- [ ] dashboard copy 자동화 개선

### 중기 실행 (다음 주)
- [ ] people feedback collection 시작
- [ ] domain별 correction tracking

---

**현재 3일 데이터 기반으로는 통계적 의미가 없으나, 시스템 안정화와 기반 구축을 위해서는 지금도 운영 계획을 수립하고 실행하는 것이 중요합니다.**
