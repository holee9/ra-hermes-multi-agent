# RA Hermes 에이전트 확장 가이드 (초안)

> **상태: 초안** — 운영 데이터 축적 후 실측 기반으로 갱신 예정.
> 이 가이드는 구현 설계서가 아닙니다. "언제, 어떻게 에이전트를 추가하는가"의 의사결정 절차입니다.

---

## 원칙: 부재 기반 성장 (master-design.md §5)

에이전트 추가는 **부재가 패턴으로 확정될 때만** 한다.

- 일회성 요청 → 기존 에이전트 스킬 추가 (프로파일 분리 불필요)
- 반복 패턴 확인 + 조율 비용 > 전문성 이득 → 별도 에이전트 추가 검토
- 최종 결정은 **사람 판단 + 승인**

---

## 1. 성장 신호 확인

### 1.1 growth-metrics로 부재 측정

`scripts/growth-metrics.py` 출력에서 다음을 확인:

| 지표 | 부재 신호 |
|------|----------|
| `human_correction_rate` | 특정 영역 정정이 반복 (사람이 패턴 파악) |
| `transition_accuracy` | 특정 유형 사안에서 정확도 정체 |
| Yellow 게이트 비율 | 특정 영역에서 에스컬레이션 집중 |

### 1.2 부재 유형 판별

| 부재 유형 | 대응 방식 |
|----------|----------|
| 기존 에이전트의 지식 부족 | 스킬 추가 (§2) |
| 독립 판단 철학이 필요한 새 직능 | 별도 에이전트 추가 (§3) |
| 조율 비용 초과 | 팀장 에이전트 활성화 (§4) |

---

## 2. 스킬 추가 (기존 에이전트 보강)

### 적합한 경우

- 같은 판단 철학 안에서 새로운 기법·지식이 필요한 경우
- 예: ra-us에 §524B 사이버보안 심사 스킬 추가

### 절차

```bash
# Hermes 스킬 추가 (T3610)
hermes skill create <skill-name> --profile <profile-id>
# SOUL.md는 그대로 유지 — 기존 페르소나에 기법 추가
```

사람 승인 불필요 (스킬 추가는 에이전트 자율 영역).
단, 스킬 내용에 게이트 변경이 포함되면 보고 후 진행.

---

## 3. 별도 에이전트 추가 (프랙탈 확장)

### 적합한 경우

- 기존 RA 3종의 판단 철학과 독립적인 전문 직능
- 예: 임상 평가 전문가 (CER), PMS 전문가, CAPA 전문가

### 부재 확인 기준 (모두 충족 필요)

- [ ] 해당 영역 Yellow 게이트 비율이 전체의 X% 이상 (X는 운영 후 결정)
- [ ] 사람 정정 중 해당 영역 비중이 유의미하게 상승
- [ ] 기존 에이전트 스킬 추가로 해결 안 됨

### 추가 절차

```bash
# 1. 새 프로파일 생성 (T3610)
hermes profile create <agent-id> --no-skills

# 2. SOUL.md 이식 (profiles/souls/<agent>-SOUL.md → 프로파일 디렉토리)
cp profiles/souls/<agent>-SOUL.md ~/.hermes/profiles/<profile-id>/SOUL.md

# 3. Honcho 설정 파일 생성 (profiles/honcho-config-templates/ 참고)
# 4. 지식베이스 연결
bash profiles/scripts/connect-kb.sh <profile-id>

# 5. 학습 루프 시작 전 사람 검증 실시
```

### SOUL.md 작성 요령

1. 회사 컨텍스트 섹션 필수 (Company Context)
2. 독립 판단 철학 명시 (다른 에이전트와 무엇이 다른가)
3. 고정 규칙 명시 (사람 전용 결정 목록)
4. `미활성` 마커 제거 후 사람 검토

기존 SOUL.md 파일: `profiles/souls/` 디렉토리 참조.

---

## 4. 팀장 에이전트 활성화

### 적합한 경우

RA 전문가 수가 늘어나거나, 멀티리전 사안 빈도가 증가하여 조율 비용이 전문성 이득을 초과할 때.

### 활성화 절차

1. `profiles/souls/coordinator-SOUL.md` 검토·확정 (사람 승인)
2. 기존 RA 에이전트 SOUL.md에 "팀장 에이전트와의 협업" 섹션 추가
3. n8n 라우팅 노드 수정 (사람 보고 후 진행)
4. E2E 테스트 후 활성화

---

## 5. 프랙탈 확장: workspace 추가

운영 범위가 새 규제권(예: 일본 PMDA, 중국 NMPA)으로 확대될 때.

### 절차 요약

1. 신규 규제권 SOUL.md 작성 (기존 ra-kr-SOUL.md 참고)
2. `profiles/honcho-config-templates/` 에 honcho 설정 템플릿 추가
3. 동일 workspace 안에서 프로파일 생성 (기존 조직과 동일 Honcho 인스턴스 공유)
4. 지식베이스 연결 + 초기 캘리브레이션 (사람 50건 평가)
5. 3종 체제 유지 원칙: 단일 규제권 추가가 원칙. 여러 권역을 한 에이전트에 묶지 않는다.

### 규모 조정 기준

| 에이전트 수 | 팀 구조 |
|------------|---------|
| 3종 이하 | 팀장 불필요, 직접 조율 |
| 4~6종 | 팀장 에이전트 활성화 검토 |
| 7종 이상 | 규제권별 sub-workspace 분리 검토 |

---

## 관련 문서

- `docs/RA-multi-agent-master-design.md` §3.3 조직 계층, §5 부재 기반 성장
- `docs/operations-guide.md` §5 성장 기준
- `profiles/souls/coordinator-SOUL.md` 팀장 에이전트 초안 (미활성)
- `scripts/growth-metrics.py` 부재 측정 데이터 공급

---

*버전: 초안 v0.1. 30일 운영 데이터 수집 후 실측 기반으로 갱신 예정.*
