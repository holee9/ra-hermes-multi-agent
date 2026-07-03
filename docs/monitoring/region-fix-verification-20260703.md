# RA 메일 region fix 검증 종합 보고 (정정본)

- **작성**: 2026-07-03 · **정정**: 2026-07-03 (기준 시점 2026-07-03 01:59 UTC = 10:59 KST)
- **대상 fix**: v6 워크플로우(`ra-request-to-op_v6`, id `t9x6j6UnyJzjCFBA`) region 추론 개선
- **fix 배포 시점**: `workflow_entity.updatedAt = 2026-07-02 05:19:49 UTC`
- **검증 방식**: raspi5p `~/ra-mail-monitor.py` + n8n postgres 직접 관측, 2h 간격 모니터링 (9회 틱)
- **관련 이슈**: #88 (unclear_region 군집 · region_hint), #91 (hermes_fallback fail-closed)

> **추적번호 정정**: 본 검증은 세션 내에서 "#77 region fix"로 지칭되었으나, GitHub `holee9/ra-hermes-multi-agent#77`은 **"생태계 의사결정 원칙 개정(메타)"** 이슈로 region과 무관. region fix 실제 추적 = **#88 / #91**.

> **[정정 — KR fallback 소멸 주장 철회]** 초판에서 "POST-fix 외국 메일 KR 0건·KR fallback 소멸 확정"이라 게시했으나 **잘못된 결론**. 재측정 결과 **POST-fix 외국 메일 8건 중 3건이 region=KR**. 원인: (a) 초판 스위프가 07-02 21:59 스냅샷이라 07-03 실행(16642/16663 hollywood.co.th) 미관측, (b) `region` 키 다중 매칭 시 set 비결정성으로 wpId 노이즈(704/369)가 섞여 KR을 가린 측정 결함. 본 정정본은 클린 region 값(`^(eu|kr|us|unclear|null|multi_region)$`만 집계)으로 재측정.

---

## 1. 핵심 신호 결과 (4종) — 정정

| 신호 | 결과 | 근거 |
|------|------|------|
| **TAXO_ERR = 0** | ✅ PASS | 검증 기간 중 v6 error 0건 (최근 48h error = 0) |
| **성공률 유지** | ✅ PASS | 최근 24h v6 24건 전부 `success` (100%) |
| **KR fallback 소멸** | ❌ **FAIL (부분)** | POST-fix 외국 메일 8건 중 **3건 region=KR** (hollywood.co.th ×2, gshealth.lk) |
| **이탈리아 → EU 전환** | ✅ PASS | `tmsrl.eu` 07-01 10:00 KR → 07-02 09:00 EU. `licarno.com.ua` EU 유지 |

## 2. POST-fix 외국 메일 region 할당 (전 구간, 클린 측정)

fix 배포(05:19) 이후 처리된 외국 발신자 도메인 메일 8건:

| 실행 | 발신자 | (국가) | region | decision | 비고 |
|------|--------|--------|--------|----------|------|
| 16505 | axtech.co.th | 태국 | **US** | — | KR은 아님 (엄격 기준 eu/unclear도 아님) |
| 16517 | gshealth.lk | 스리랑카 | **KR** | yellow_review | 본문 "국내 변경인증" KR 문막 → KR 정상 가능 |
| 16525 | tmsrl.eu | 이탈리아 | **EU** | — | 정상 (rhint=eu) |
| 16530 | licarno.com.ua | 이탈리아계 | **EU** | — | 정상 (rhint=eu) |
| 16539 | licarno.com.ua | 이탈리아계 | **EU** | — | 정상 (rhint=eu) |
| 16572 | licarno.com.ua | 이탈리아계 | **EU** | — | 정상 (rhint=eu) |
| 16642 | hollywood.co.th | 태국 | **KR** | yellow_review | **순수 KR fallback — fix 미적용** (rhint 없음) |
| 16663 | hollywood.co.th | 태국 | **KR** | yellow_review | **순수 KR fallback — fix 미적용** (rhint 없음) |

- **KR 할당: 3건 / 8건** → KR fallback 소멸 **미달**.
- 단 3건 모두 `decision=yellow_review`(fail-closed, #91) → **잘못된 OP 기록은 발생 안 함**. region 라벨이 KR인 점은 잔존.
- `abyzr.com` 내부 포워딩의 KR 본문(국내 인증/변경심사) KR 할당은 정상 동작.

## 3. 근인 추정 (root cause)

region_hint 도출 로직이 **EU 키워드(EUDAMED 등)만 커버**, 태국/스리랑카 신호 미커버:

| 발신자 | region_hint 전송 | 최종 region |
|--------|------------------|-------------|
| licarno/tmsrl (EU 키워드) | `eu` ✅ | EU (정상) |
| hollywood.co.th (태국) | 없음 ❌ | KR (fallback) |
| axtech.co.th (태국) | 없음 | US (T3610 추론) |
| gshealth.lk (스리랑카) | 없음 | KR (fallback, 단 본문 KR) |

→ fix는 `region_hint` 경로가 트리거되는 EU 계정만 해소. **hint 없는 비EU 외국 메일은 T3610이 기본 KR/US로 fallback**. Thailand 라우팅 정확도가 핵심 갭.

## 4. 모니터링 경과 (UNREAD 감소 추이)

| 시각 (UTC) | UNREAD | 비고 |
|------------|--------|------|
| 07-02 12:03 | 15 | 검증 시작 |
| 07-02 13:59 | 13 | |
| 07-02 15:59 | 11 | |
| 07-02 17:59 | 9 | |
| 07-02 19:59 | 7 | |
| 07-02 21:59 | 5 | (초판 스위프 — 노이즈 포함, 정정 대상) |
| 07-02 23:59 | 3 | |
| 07-03 00:21 | 2 | |
| 07-03 01:59 | **1** | 최종 관측 |

- 감소 속도: **-2건 / 2h** (안정적). 처리 파이프라인 정상.

## 5. 결론 (정정)

- **TAXO_ERR=0 · 성공률 100% · 이탈리아 EU 전환**: PASS.
- **KR fallback 소멸**: **미달** — 태국(hollywood.co.th) POST-fix에도 KR 잔존. 단 decision=yellow_review(fail-closed)로 실제 OP 오기록은 없었음.
- fix는 EU 계정에만 유효; 비EU 외국(태국/스리랑카) region_hint 커버가 후속 과제.
- 본 보고서는 중간 종합점. UNREAD=0 도달 시 최종 마감.

## 6. 후속 권고

1. **region_hint 커버리지 확대**: 태국(FDA/CE 외 신호)/스리랑카 키워드 매핑 추가, 또는 hint 없을 때 T3610 fallback 기본값 검토(KR → unclear).
2. **hollywood.co.th 라우팅**: 본문 확인 후 실제 규제 region(EU/US/unclear) 확정.
3. **측정 신뢰성 교훈**: 실행 데이터에서 region 추출 시 `region` 키 다중 매칭을 피하고 advisory 객체의 단일 region 필드를 직접 읽을 것.

---

## 부록: 검증 관측 쿼리

```sql
-- v6 error (TAXO_ERR 지표)
SELECT count(*) FROM execution_entity
 WHERE "workflowId"='t9x6j6UnyJzjCFBA' AND status='error'
   AND "startedAt" > now() - interval '48 hours';
-- 성공률
SELECT status, count(*) FROM execution_entity
 WHERE "workflowId"='t9x6j6UnyJzjCFBA' AND "startedAt" > now() - interval '24 hours'
 GROUP BY status;
-- fix 배포 시점
SELECT "updatedAt" FROM workflow_entity WHERE id='t9x6j6UnyJzjCFBA';
```

region 추출(정정): `execution_data` resolve 후 `region` 키 값 중 `^(eu|kr|us|unclear|null|multi_region)$` 매칭값만 집계(wpId 노이즈 제거). 발신자는 `effectiveFrom`에서 도메인 추출.
