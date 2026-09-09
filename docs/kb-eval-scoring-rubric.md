# KB Eval 채점 루브릭 — 기존 채점 120건 역추출

생성 2026-09-09 · 근거: 이미 채점된 120건 (보정 노트 74건)

선례 #119~122 및 06-20 배치에서 사람이 실제로 내린 판정을 역추출한 것이다.
추정이 아니라 관측된 채점 결과에서 도출했다.

## 1. Score 분포 (실측)

| Score | 건수 | 비율 |
|---|---:|---:|
| Score 3 | 21 | 17% |
| Score 2 | 60 | 50% |
| Score 1 | 39 | 32% |
| **합계** | **120** | |

**Score 2가 최빈값**이다. 대부분의 응답은 핵심 판단이 맞고 세부에 흠이 있다.

## 2. Score별 Fast Check 체크율 (실측)

| Fast Check | Score 3 | Score 2 | Score 1 |
|---|---:|---:|---:|
| Match correct | 100% | 90% | 28% |
| Evidence supported | 100% | 61% | 15% |
| Source cited | 100% | 96% | 58% |
| No hallucination | 95% | 60% | 53% |
| Escalation appropriate | 100% | 86% | 25% |
| Human correction needed | 0% | 45% | 100% |

### 판정 규칙 (위 실측에서 도출)

- **`Human correction needed` 가 결정적 분기점** — Score 3 에서 **0%**, Score 1 에서 **100%**.
  체크하면 Score 3 이 될 수 없고, 체크하지 않으면 Score 1 이 될 수 없다.
- **Score 3** = 6개 체크 사실상 전부 통과 (5개 100%, `No hallucination` 95%).
- **Score 2** = `Match correct`(90%)·`Source cited`(96%) 는 유지되나
  `Evidence supported`(61%)·`No hallucination`(60%) 이 무너진 상태.
  → **핵심 판단은 맞고 근거·인용에 흠**.
- **Score 1** = `Match correct` 28%, `Evidence supported` 15%.
  → **판단 자체가 성립하지 않음**.

## 3. 결함 유형 분포 (보정 노트 배타 분류)

| 유형 | S3 | S2 | S1 |
|---|---:|---:|---:|
| 캡처 실패 | 0 | 0 | 8 |
| 매칭 실패 (source↔focus) | 0 | 0 | 6 |
| 창작·검증불가 인용 | 0 | 13 | 7 |
| 식별자 오적용·오배치 | 1 | 6 | 6 |
| 결함 없음 | 7 | 3 | 1 |
| 기타 | 0 | 5 | 11 |

### 🔴 Score 1 의 다수는 에이전트 응답 품질 문제가 아니다

보정 노트가 있는 Score 1 39건 중 **14건 (35%)** 이
**캡처 실패** 또는 **source↔focus 매칭 실패**를 지적한다.

- 매칭 실패 예: *"EUDAMED 키워드가 UDI 등록문서를 선택 — clinical evaluation focus와 주제 불일치"*
- 매칭 실패 예: *"단일 MFDS가 SAR 시험·세금계산서 이메일(행정 QA 로그)을 오매칭"*

둘 다 **케이스 생성 단계**(`kb-eval-checksheet.py` 의 source 선택)의 결함이지
에이전트가 잘못 답한 것이 아니다. 채점 결과를 `correction_rate` 등 성장 지표에
투입할 때 이 둘을 분리하지 않으면 **에이전트 성능을 과소평가**한다.

## 4. 판정 절차 (권장)

1. **응답 캡처 여부 확인** — 없으면 Score 1 + `Human correction needed`, 사유 "캡처 실패" 명기.
2. **source ↔ focus 정합성 확인** — 어긋나면 Score 1, 사유 "매칭 실패" 명기 (에이전트 무관).
3. 위 둘을 통과하면 **응답 내용 판정**:
   - 규제 식별자가 source 및 공식 주제와 일치하는가 → `No hallucination`
   - source 근거를 실제로 사용했는가 (일반 지식만이 아닌가) → `Evidence supported`
   - 출처(chunk/source)를 명시했는가 → `Source cited`
   - focus 에 대한 RA 판단이 성립하는가 → `Match correct`
   - 불확실 항목을 사람 확인으로 넘겼는가 → `Escalation appropriate`
4. 위 5개가 모두 참이고 정정 불필요 → **Score 3**
   핵심은 맞으나 근거·인용에 흠 → **Score 2**
   판단 자체가 성립 안 함 → **Score 1**
5. 보정 노트는 **무엇이 맞고 무엇이 틀렸는지 분리**해서 쓴다 (실제 사례 형식):
   *"핵심 판단(510(k)/De Novo/PMA 근거)은 정확하나 De Novo eSTAR 표기가 소스와 자기모순"*

## 5. 미검증

- 결함 유형 분류는 보정 노트의 정규식 매칭이다. 노트가 없는 46건은 분류 대상에서 빠졌다.
- Score 3 의 `No hallucination` 95%(1건 미체크)의 사유는 개별 확인하지 않았다.
