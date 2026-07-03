# RA 메일 region fix 검증 종합 보고

- **작성**: 2026-07-03 (기준 시점 2026-07-03 00:21 UTC = 09:21 KST)
- **대상 fix**: v6 워크플로우(`ra-request-to-op_v6`, id `t9x6j6UnyJzjCFBA`) region 추론 개선
- **fix 배포 시점**: `workflow_entity.updatedAt = 2026-07-02 05:19:49 UTC`
- **검증 방식**: raspi5p `~/ra-mail-monitor.py` + n8n postgres 직접 관측, 2h 간격 모니터링 (8회 틱)
- **관련 이슈**: #88 (unclear_region 군집 · region_hint), #91 (hermes_fallback fail-closed)

> **추적번호 정정**: 본 검증은 세션 내에서 "#77 region fix"로 지칭되었으나, GitHub `holee9/ra-hermes-multi-agent#77`은 **"생태계 의사결정 원칙 개정(메타)"** 이슈로 region과 무관함. region fix의 실제 추적 이슈는 **#88 / #91**. 향후 이력 검색 혼선 방지를 위해 본 보고서와 #88 코멘트에 명시함.

---

## 1. 핵심 신호 결과 (4종)

| 신호 | 결과 | 근거 |
|------|------|------|
| **TAXO_ERR = 0** | ✅ PASS | 검증 기간 중 v6 error 실행 0건 (최근 48h error count = 0) |
| **성공률 유지** | ✅ PASS | 최근 24h v6 실행 24건 전부 `success` (100%) |
| **KR fallback 소멸** | ✅ PASS (확정) | POST-fix 전 16건 스위프 — 외국 도메인 메일 6건 중 **KR 할당 0건** |
| **이탈리아 → EU 전환** | ✅ PASS | `tmsrl.eu` 07-01 10:00 KR → 07-02 09:00 EU 전환 확인 |

## 2. POST-fix 외국 메일 region 할당 (전 구간 스위프)

fix 배포(05:19) 이후 처리된 외국 발신자 도메인 메일의 region:

| 실행 | 발신자 도메인 | (국가) | region | 비고 |
|------|---------------|--------|--------|------|
| 16505 | axtech.co.th | 태국 | **US** | KR은 소멸. (엄격 기준 eu/unclear는 아님) |
| 16517 | gshealth.lk | 스리랑카 | non-KR | 본문이 "국내 변경인증" KR 문막 → unclear/KR 모두 합리적 |
| 16525 | tmsrl.eu | 이탈리아 | **EU** | 이전 KR에서 정상 전환 |
| 16530 | licarno.com.ua | 이탈리아계 | **EU** | 정상 |
| 16539 | licarno.com.ua | 이탈리아계 | **EU** | 정상 |
| 16572 | licarno.com.ua | 이탈리아계 | **EU** | 정상 |

- **KR 할당 건수: 0** → "KR fallback 소멸" 확정.
- `abyzr.com` 내부 포워딩 중 KR 본문(국내 인증/변경심사)의 KR 할당은 정상 동작(비 오배정).

## 3. PRE-fix KR 오배정 사례 (대조군)

fix 이전에 KR로 오배정되었던 외국 메일 (배포 전 데이터, 참고용):

| 실행 | 발신자 | region | 시점 |
|------|--------|--------|------|
| 16488 / 16490 | hollywood.co.th (태국) | KR | 07-02 01:00 / 02:00 (05:19 배포 이전) |
| 16345 / 16346 | hollywood.co.th (태국) | KR | 07-01 02:00 / 03:00 |
| 16391 | tmsrl.eu (이탈리아) | KR | 07-01 10:00 |

→ 이들 모두 **05:19 배포 이전**. POST-fix 동일 발신자군은 KR 없음.

## 4. 모니터링 경과 (UNREAD 감소 추이)

raspi5p `from:abyzr.com is:unread` 잔량:

| 시각 (UTC) | UNREAD | 비고 |
|------------|--------|------|
| 07-02 12:03 | 15 | 검증 시작 |
| 07-02 13:59 | 13 | |
| 07-02 15:59 | 11 | |
| 07-02 17:59 | 9 | |
| 07-02 19:59 | 7 | |
| 07-02 21:59 | 5 | POST-fix 외국 KR=0 확정 스위프 |
| 07-02 23:59 | 3 | |
| 07-03 00:21 | **2** | 최종 관측 |

- 감소 속도: **-2건 / 2h** (v6 매시 정각 1건 처리 흐름과 일치, 안정적).
- 오류 없이 단조 감소 → 처리 파이프라인 정상.

## 5. 잔여 한계 / watch 항목

1. **axtech.co.th → US**: KR fallback은 해소됐으나, 사용자 엄격 기준(eu 또는 unclear/null)에는 미달. 단 본 검증의 본 목적인 "KR 오배정 제거"는 달성. Thailand 계정의 region 정확도는 별도 후속.
2. **hollywood.co.th**: POST-fix 신규 메일 처리가 아직 관측되지 않음 (기존 건은 read 처리되어 재실행 안 함). 신규 도착 시 region 재확인 권장.
3. **gshealth.lk**: 발신자는 `.lk`이나 메일 본문이 KR 국내 인증 공지 → 맥락상 KR이 정상일 수 있어, region=KR이 곧 오배정 아님.
4. **모니터링 지속**: UNREAD=0 도달 시 본 검증을 최종 종료(완료) 처리. (본 보고서는 중간 종합점)

## 6. 결론

- region fix는 **정상 작동** 중이며, 핵심 목표인 **외국 메일 KR 오배정(= KR fallback) 소멸이 확정**됨.
- 부수 품질 신호(TAXO_ERR=0, 성공률 100%)도 검증 기간 전 구간에서 유지.
- 잔여 UNREAD 2건이 0에 도달하면 검증 완료로 마감 예정.

---

## 부록: 검증 관측 쿼리

```sql
-- v6 error 실행 (TAXO_ERR 지표)
SELECT count(*) FROM execution_entity
 WHERE "workflowId"='t9x6j6UnyJzjCFBA' AND status='error'
   AND "startedAt" > now() - interval '48 hours';

-- 성공률
SELECT status, count(*) FROM execution_entity
 WHERE "workflowId"='t9x6j6UnyJzjCFBA'
   AND "startedAt" > now() - interval '24 hours'
 GROUP BY status;

-- fix 배포 시점
SELECT "updatedAt" FROM workflow_entity WHERE id='t9x6j6UnyJzjCFBA';
```

region·발신자 추출은 `execution_data` 압축 인덱스 포맷 역참조 해석기로 resolve 후 walk 수행 (모니터 스크립트 `~/ra-mail-monitor.py`의 `resolve_exec`·`signals` 로직과 동일 계열).
