# RA Hermes 프로젝트 — 운영 상태 & 완성도 점검

> 이 파일은 주기적 전수 조사 결과를 누적 기록한다.
> 이후 작업 착수 전 "현재 어디까지 됐나" 확인 기준점으로 사용한다.

---

## 점검 기록 #3 — 2026-06-11

### .env 점검 및 인프라 정보 반영

#### 발견 및 변경 사항

| 항목 | 이전 기록 | 확인된 실제 값 | 조치 |
|------|----------|--------------|------|
| NAS 연결 방식 | Tailscale HTTP (`diskstation:7001`) | NFS 로컬 마운트 (`/mnt/nas-ra/공통자료/RA`) | 이슈 #35 DoD 재정의, 코멘트 추가 |
| hermes-api-server.py 포트 | 미기록 | `8643` (`API_SERVER_PORT`) | master-design.md §14.1 업데이트 |
| Layer 4 API 키 변수명 | 미기록 | `OPENFDA_API_KEY`, `LAW_GO_KR_OC`, `DATA_GO_KR_API_KEY` | 이슈 #37 코멘트 추가 |
| GX10 Ollama URL | 192.168.100.1 (추정) | `http://192.168.100.1:11434` (확인) | master-design.md §14.1 추가 |
| Qdrant URL | pgvector 이전 완료 | 여전히 .env에 잔존 (미사용) | .env.example에 주석 처리 |

#### 변경된 파일

- `scripts/index_ra_knowledge.py`: `NAS_BASE` 하드코딩 → `NAS_RA_PATH` 환경변수 읽기
- `.env.example` 신규 생성: 모든 환경변수 이름 문서화 (값 없음)
- `docs/RA-multi-agent-master-design.md` §14.1: 운영 서비스 URL 맵 추가
- 이슈 #35 보정 코멘트: NAS 로컬 마운트 확인됨
- 이슈 #37 보정 코멘트: env var 이름 및 API 서버 포트 명시

---

## 점검 기록 #2 — 2026-06-11

### 전체 그림 재정립 (이 세션의 핵심 발견)

**핵심 재정립**: 이 시스템은 이메일 처리기가 아니다.  
**H&ABYZ의 AI 기반 의료기기 인허가 운영 부서**다.

H&ABYZ는 실제 X-ray 영상 진단 의료기기 제조사이며, 실제 제품들이 실제 허가를 받아야 한다.  
이메일 트리아지는 RA 업무 유입 채널(첫 번째 구현)이며, 시스템의 목적이 아니다.

### 생태계 구조 확인

```
지식 토대 (T자형 가로획 — 에이전트에게 단방향 주입)
  ra-project: 규제 지식 베이스
  MD-process: 사내 SOP·정책
  llm-wiki:   NAS 실무자료 RAG (인덱싱 진행중)
  → 모두 RA 에이전트에게 단방향 참조

RA 전문가 에이전트 (T자형 세로획 — H&ABYZ 특화 경험 누적)
  Mike(ra_us): FDA 510(k)/QMSR/Part 1020
  Theo(ra_eu): CE MDR/Notified Body
  Sam(ra_kr):  MFDS/KGMP/국제정합

관련 레포
  ra-med-bot(Regula): 내부 직원용 규제 Q&A (별도 레포)
  regula-eval-suite:  Regula 평가 스위트 (별도 레포)
```

### 식별된 구조적 갭 (현재 미완성)

| 갭 | 영향 | 비고 |
|----|------|------|
| ra-project/MD-process → pgvector 자동 인덱싱 없음 | T자형 가로획 미구축 | 수동 NAS 인덱싱만 |
| 성장 트리거 임계값 미정의 | 다음 단계 자동 진입 불가 | ops-guide §5.2 |
| infra 투표 브로드캐스트 없음 | 프랙탈 패턴 복제 불가 | [IF] 의도적 공백 |
| Layer 4 API 호출 mail-triage 미연결 | 실시간 규제 DB 미활용 | hermes-api-server.py 분리 |

### 제품 분류 수정

**이번 세션에서 보정**:
- `HnVUE` = **SaMD** (Software as a Medical Device — 독립 소프트웨어 의료기기)
- `Retrofit (HnX-R1)` = **SiMD** (Software in a Medical Device — 하드웨어 디지털화 키트 내장 SW)

**적용 문서**: ra-us/eu/kr-SOUL.md 전 3종 수정 완료 (2026-06-11)

**SaMD vs SiMD 규제 함의**:
- HnVUE(SaMD): IMDRF SaMD framework 적용; FDA FDARA §520(o); EU Rule 11; MFDS SDS 필수
- Retrofit(SiMD): 기기 허가 일부로 처리; FDA 510(k) device file; EU 기기 분류 루트; SaMD 독립 경로 불필요

---

## 점검 기록 #1 — 2026-06-11

### 요약 판정

**실사용 가능 상태 ✅** — MVP DoD 전 항목 완료, 미완료 작업 이슈 없음.

### GitHub 이슈 현황

| 구분 | 수 | 비고 |
|------|---|------|
| Open | 1 | #2 `[RULE]` rule-ref 참조 문서 (닫지 않는 이슈) |
| Closed | 33 | 모든 작업 이슈 완료 |

### 단계별 완료 현황

| 단계 | 상태 | 이슈 | 완료일 |
|------|------|------|--------|
| 설계 (ADR-001) | ✅ | #12 | ~06-02 |
| 골격 코드 구현 | ✅ | — | — |
| Honcho T3610 배포 | ✅ | #3 | 06-05 |
| MVP 자동화 스크립트 (SPEC-RA-TOOL-001) | ✅ | #16 | 06-05 |
| RA 프로파일 생성 (ra_us/eu/kr 외 5종) | ✅ | #4 | 06-05 |
| mail-triage n8n 배포 · E2E | ✅ | #5 | 06-08 |
| 투표 인터페이스 [IF] | ✅ | #7 | 06-08 |
| 브릿지 n8n 배포 | ✅ | #8 | 06-06 |
| 3점 평가 루프 n8n · Honcho 기록 | ✅ | #9 | 06-08 |
| Virtual Office Docker · 실데이터 연결 | ✅ | #10 | 06-08 |
| Cold Start E2E 검증 | ✅ | #11 | 06-08 |
| Qdrant → pgvector 포팅 (MIGRATE-1,2) | ✅ | #17, #19 | 06-08 |
| OP 이력 backfill 시드 (SEED-1) | ✅ | #18 | 06-09 |
| warm-start 학습 루프 (GROWTH-1) | ✅ | #20 | 06-09 |
| deriver reflection 활성화 (GROWTH-2) | ✅ | #21 | 06-09 |
| feedback delta 페어링 (GROWTH-3) | ✅ | #22 | 06-09 |
| WP 종결 → case digest (GROWTH-4) | ✅ | #23 | 06-09 |
| 일일 성장 지표 인프라 (GROWTH-5) | ✅ | #24 | 06-09 |
| Layer 4 knowledge_fetch E2E (openFDA/law.go.kr) | ✅ | #30 | 06-10 |
| data.go.kr Layer 4d 통합 (3/3 서비스) | ✅ | #31, #33 | 06-11 |
| hermes-api-server.py 프로파일 라우팅 수정 | ✅ | #28 | 06-10 |
| llm-wiki NAS 갭 (graceful degradation 처리) | ✅ | #29 | 06-10 |
| 정확성·신뢰성 원칙 문서 이식 | ✅ | #32 | 06-10 |
| Playwright E2E 테스트 추가 | ✅ | bc7379f | 06-11 |

### implementation-spec DoD 달성 현황

| # | 기준 | 유형 | 상태 |
|---|------|------|------|
| 1 | Honcho ↔ GX10 Qwen3 tool-calling 검증 | `[구현]` | ✅ |
| 2 | 재전송 메일 → RA 분석 → WP 처리 → Honcho 기록 | `[구현]` | ✅ |
| 3 | 반복 메일 중복 WP 감소 (핵심 지표) | `[구현]` | ✅ GROWTH 완료 |
| 4 | 인프라 3종 투표 집계 결정 산출 | `[IF]` | ⚙️ 의도적 공백 |
| 5 | 브릿지 인프라→업무 단방향 전달 | `[구현]` | ✅ |
| 6 | 3점 평가 Honcho 기록 → 차회 분석 영향 | `[구현]` | ✅ |
| 7 | Virtual Office 실데이터 재생 | `[구현]` | ✅ |

### [IF] 의도적 공백 항목 (버그 아님)

| 파일 | 내용 | 설명 |
|------|------|------|
| `voting/config/vote-rules.json` | 투표 집계 규칙 | 운영 관찰 후 채울 것 |
| `bridge/config/bridge-config.json` | relay_conditions | 운영 중 결정 |
| `feedback/config/weight-adjustment-config.json` | 가중치 공식 | 학습 데이터 쌓인 후 조정 |

### 현재 실사용 가능 기능

- Honcho 서버 (T3610, Docker 구동 중)
- mail-triage n8n 워크플로우 (RPi, E2E 검증)
- RA 에이전트 프로파일 3종 + 관리 에이전트 5종
- 3점 피드백 루프
- GROWTH 학습 루프 전체 (warm-start → deriver → delta → case digest → metrics)
- Layer 4 knowledge_fetch (openFDA, law.go.kr, data.go.kr)
- Virtual Office (목업↔실데이터 전환 가능)
- scripts/ 자동화 17종

### 잔여 과제 (필수 아님, 우선순위순)

1. llm-wiki NAS 라우팅 설정 (T3610 → 10.11.1.40 네트워크)
2. `vote-rules.json` 초기값 결정 (인프라 투표 활성화 시)
3. `growth-metrics.py` systemd timer 실 배포
