# RA 에코시스템 현황 및 개발 전략

> 최초 작성: 2026-06-10  
> 관련 이슈: [#26 에코시스템 우선순위 분석](https://github.com/holee9/ra-hermes-multi-agent/issues/26) · [#27 AI 도구 연구](https://github.com/holee9/ra-hermes-multi-agent/issues/27)

---

## 1. 에코시스템 계층 구조

의료기기 인허가(RA) 도메인 단일 목표로 수렴하는 프로젝트 군.

```
[지식 레이어]
  ra-project            — 의료기기 X-ray 인허가 전문 지식베이스 (KR/US/EU 규제)
  MD-process            — 회사 내부 SOP·업무규칙 문서 자동화
  nas-llm               — NAS 전체 문서 → LLM Wiki 인제스트 인프라 (51K 파일 대상)

[AI 에이전트 레이어]
  ra-hermes-multi-agent — Hermes+Honcho 기반 학습하는 RA 전문 멀티에이전트 (본 레포)
  (hermes-ra            — 아카이브됨. ra-hermes-multi-agent로 통합 이전 완료)

[사용자 접점 레이어]
  ra-med-bot (Regula)   — 사내 직원용 RA 질의 챗봇 (ra-project + MD-process RAG)
  regula-eval-suite     — Regula 응답 품질 자동 벤치마크 (Waza 기반)

[미래/확장 레이어]
  hybrid-ra-saas        — 외부 고객용 글로벌 SaaS 플랫폼 (데이터 주권 분리형 아키텍처)
```

---

## 2. 코드 개발 대상 레포 우선순위 (2026-06-16 기준)

| 순위 | 레포 | Open 이슈 | 현재 상태 | 우선 이유 |
|------|------|----------|----------|---------|
| 1 | `ra-med-bot` | 60개 내외 | feat/issue-22-predicate 진행 중 | Wave 3 PREDICATE-001 구현 미완, 미결 이슈 최다 |
| 2 | `hybrid-ra-saas` | 10개 내외 | 로컬 미클론, 원격만 존재 | 사전작업 이슈 진행 중, 최근 push 활발 |
| 3 | `ra-hermes-multi-agent` | #37, #39~#45, #62~#65 등 | Phase 1~2 완료, 성장 루프/자율 학습/안전 하드닝 레포 반영. #48/#49 peer_id 오염은 2,085건 clean replay 완료, #56에서 live wrong-peer records 제거 완료. 비메일 성장 루프는 구현 완료이나 `hermes-auto-growth.timer`는 승인 전 OFF. 최근 growth reports가 sessions/messages 0이라 #64에서 ingestion/data contract 보정 필요. #43~#45는 운영 import/E2E 대기. | 에코시스템 오케스트레이터, Honcho/OpenProject/n8n 운영 계약 안정화 중 |
| 4 | `regula-eval-suite` | 0개 | 초기 단계 | ra-med-bot 평가 인프라, 연계 개발 필요 |
| 5 | `nas-llm` | 2개 | Phase 4 인제스트 진행 중 | Phase 4 전량 인제스트 미완 |

### 제외 레포

| 레포 | 제외 이유 |
|------|---------|
| `hermes-ra` | 아카이브됨 (`isArchived: true`) |
| `ra-project` | 코드 개발 아님 — RAG 지식소스 |
| `MD-process` | 코드 개발 아님 — SOP 문서 자동화 |
| `ra-project-hermes-bak` | 백업 레포 |
| `note` | 자격증명·메모 저장소 |

---

## 3. AI 도구 적용 전략 (2026-06-10 기준)

### 모델 선택 기준

| 모델 | 가격(입/출) | SWE-Bench | 권장 상황 |
|------|-----------|-----------|---------|
| Claude Fable 5 | $10/$50 | 80.3% | 복잡한 대규모 구현 |
| Claude Opus 4.8 | $5/$25 | 69.2% | 균형 잡힌 일반 작업 |
| Claude Sonnet 4.6 | $3/$15 | ~60% | 일상 유지보수·문서 |

### Ultracode 적용 기준

**활성화**: `ultracode: [작업]` 또는 `/effort ultracode`

| 조합 | 권장 작업 |
|------|---------|
| Fable 5 + ultracode | ra-med-bot Wave 4~5 대규모 구현, hybrid-ra-saas 초기 아키텍처 설계 |
| Opus 4.8 + ultracode | 코드베이스 전체 감사, regula-eval-suite 벤치마크 자동화 |
| Sonnet 4.6 + 일반 | 문서 업데이트, 이슈 관리, 일상 유지보수 |

> 주의: ultracode는 토큰 비용이 크게 증가. 소규모 테스트 후 `/workflows` 패널에서 사용량 확인 필수.

---

## 4. 변경 이력

| 날짜 | 내용 |
|------|------|
| 2026-06-16 | ra-hermes 상태 갱신 — #63~#65 등록. 프로젝트 현황을 RA 전문가 성장 운영 기준으로 재정렬하고, metrics ingestion 0건 보정과 threshold/notification 정책을 별도 이슈로 분리 |
| 2026-06-16 | ra-hermes 상태 갱신 — #62 정적 `docs/growth-dashboard.html` 추가, Git checkout에서 바로 보는 성장 모니터링 snapshot 제공 |
| 2026-06-16 | ra-hermes 상태 갱신 — #61 지속 성장 모니터링 감사, `ra-growth-metrics.timer` active/enabled 확인, 통합 성장 대시보드 미구현 및 최근 metrics 데이터 0건 한계를 #62 후속으로 등록 |
| 2026-06-16 | ra-hermes 상태 갱신 — #60 `ra_kr` 균형 보강 완료, 자동성장 readiness 16/16, timer는 명시 승인 전 OFF 유지 |
| 2026-06-16 | ra-hermes 상태 갱신 — #56 live wrong-peer raw records 제거, 자동성장 전환 전 오염 원본 live DB 0 확인 |
| 2026-06-15 | ra-hermes 상태 갱신 — #48/#49 incident 문서 사용자 발견 경로 추가, 전체 문서 전수 점검 완료, README/ecosystem 날짜 갱신 |
| 2026-06-13 | ra-hermes 상태 갱신 — #43~#47 안전/QA/문서 하드닝, #49 autonomous study peer_id 오염 containment/replay/backlog 모니터링 반영 |
| 2026-06-10 | 최초 작성 — 에코시스템 분석 및 AI 도구 전략 정리 |
