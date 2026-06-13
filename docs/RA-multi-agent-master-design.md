# RA 멀티 에이전트 시스템 — 마스터 설계서

> 전체 토의를 교차검증해 재구성한 통합 설계서. **시스템 구축 계획서이자 제안서**이며, GitHub 레포로 버전 관리한다(호스팅: GitHub 확정, 2026-06-05).
> 표기: **확정**(합의됨) · **고정 규칙**(불변) · **체크**(구현 중 검증) · **미결**(추후 결정).
> 사실 검증 기준일: 2026-06-05.

---

## 0. 설계 철학 (모든 결정의 기준)

이 시스템은 세 철학을 **지향**하며 지속 설계한다. 구조를 미리 박제하는 게 아니라, 매 설계 결정을 이 철학에 비추어 방향을 잡는다.

1. **T자형 성장** — 각 에이전트(및 각 조직 단위)는 T자다. 가로획 = 공통 지식 토대(폭), 세로획 = 자기 전문성(깊이). 가로만이면 얕은 만능가, 세로만이면 맥락 없는 전문가. 폭넓은 공통 기반 위에 깊은 전문성을 얹는 것이 진정한 전문가다.
2. **프랙탈 성장** — 같은 구조가 규모를 바꿔 자기복제한다(전문가:팀 = 팀:조직). *성장·복제의 원리.*
3. **벌집 지향** — 단위들이 서로 나눠 지탱해 단단해지는 견고함을 지향한다. 벌집을 만드는 게 목적이 아니라, 분산·상호지탱이라는 성질을 방향으로 삼는다. *견고함·연결의 원리.*

> 프랙탈(세로로 쌓임)과 벌집(가로로 지탱)은 직교한다. 위로 복제하며 확장하고, 옆으로 맞물려 견고해진다. 단, 견고함은 형상이 아니라 **연결의 품질**에서 온다.

**중앙 두뇌 없음**: 전체를 통제하는 단일 조정자를 두지 않는다. 판단은 분산, 집계는 규칙, 출력은 배관(n8n). 종합·조율 역할(팀장)은 두되 통제하지 않는다. 이 분산 원칙은 에이전트 간·조각 간·층위 간 모든 수준에서 동일하게 적용된다.

**정확성·신뢰성 우선** (모든 자동화 결정의 최우선 제약): 이 시스템은 의료기기 인허가를 다룬다. 잘못된 분류·매칭·규제 판단은 환자 안전과 직결된다. **속도는 정확성이 확보된 뒤의 부산물**이며, 정확성과 상충할 때 속도를 양보한다. 에이전트는 사람 RA 전문가를 *보조*하고, 불확실할 때는 언제나 사람에게 올린다. 자동화 비중은 사전 설계가 아니라 학습·평가 누적으로 점진적으로 높인다.

---

## 1. 기술 기반 (사실 검증 완료, 기준일 2026-06-05)

**Hermes Agent** (NousResearch, MIT) — 현재 v0.14.0 (2026.5.16 "Foundation Release", PyPI는 v0.13.0). 자기개선 루프가 핵심: 성공한 워크플로우를 재사용 스킬로 자동 변환·정제, 세션 히스토리를 SQLite에 저장, 세션을 넘어 사용자 모델을 구축. 6개 터미널 백엔드(local/Docker/SSH/Daytona/Singularity/Modal).
- **Kanban**(v0.13.0 정식): durable multi-agent board — heartbeat·reclaim·zombie detection·auto-block·per-task retries. 인프라 에이전트 셋의 분산 작업 추적에 활용 가능.
- **메모리 플러그인 시스템**: 2026.5 정책으로 in-tree provider는 닫힘(built-in: honcho/mem0/supermemory/byterover/hindsight/holographic/openviking/retaindb). 본 시스템은 **honcho를 built-in 그대로 사용** → 정책 영향 없음.
- **미구현(체크)**: ConsensusEngine(분산 투표 집계) — Issue 단계, 직접 구현 필요.

**프레임워크 선택 근거 (확정)**: OpenClaw가 아니라 Hermes. 네 축(학습 방식·메모리 구조·강점 영역·보안 기본값) 모두에서 이 시스템 목표("학습하며 성장하는 전문가")에 Hermes가 부합. OpenClaw는 정적·사람작성 스킬, control-plane 중심 — 본 시스템 철학과 불일치. 외부 통합·오케스트레이션은 이미 n8n이 담당하므로 OpenClaw의 강점(채널 폭)이 들어설 자리 없음. → **Hermes 단독 + n8n 공존.**

**Honcho** — AI-native 메모리 백엔드(Hermes 메모리 플러그인 레퍼런스). 단순 key-value가 아니라 대화를 사후 추론(dialectic)해 사용자 모델을 누적. FastAPI 서버 + deriver 워커 + PostgreSQL/pgvector + Redis. 추론·임베딩 LLM은 OpenAI 호환 엔드포인트(Ollama/vLLM 등)로 외부 위임 가능 → 자체 호스팅 시 서버 본체 경량(약 6GB급).

**핵심 개념**:
- **workspace** = 완전 격리된 네임스페이스(데이터·인증 경계). = 조직 단위.
- **peer** = workspace 내 엔티티(사람/AI). 한 peer는 한 workspace에 종속(두 workspace를 걸치지 못함). workspace당 다수 peer 수용(사람 1 + AI N).
- **프로파일** = 독립된 Hermes 홈(config·SOUL.md·메모리·스킬·세션). 프로파일마다 전용 AI peer + 동일 user workspace 공유. `--clone`으로 생성.
- **5개 메모리 도구**: honcho_profile, honcho_search, honcho_context, honcho_reasoning(LLM), honcho_conclude. 모두 `peer="user"|"ai"|<id>` 타게팅 — AI peer 타게팅으로 자기 교정 가능.

---

## 2. 장비 배치 (확정)

| 장비 | 사양 | 역할 |
|---|---|---|
| **T3610** | Xeon 12C/24T, 32G, Linux | Honcho 서버 본체(FastAPI+deriver+PostgreSQL/pgvector+Redis) / RA 전문가 / 인프라 에이전트 |
| **GX10** | GB10 Grace Blackwell(ARM), Qwen3 로컬 LLM | 추론·임베딩 백엔드 / 영상처리·코딩 / 인프라 에이전트 |
| **라즈베리파이 5+** | RAM 16G | OpenProject / n8n / 업무 담당·n8n 담당·인프라 에이전트 |

- 추론 전량 GX10 Qwen3에 위임(OpenAI 호환, 2.5G LAN — T3610에서 검증됨). Honcho 서버 부하 경량화.
- Honcho 서버는 T3610(추론 위임으로 약 6GB급). 라즈베리는 기존 부하(n8n+OpenProject) 때문에 서버 부적합 — 클라이언트·업무 역할만.
- GX10 ARM Docker 오버헤드 우려는 회피됨: Docker 스택(Honcho)은 x86 T3610, GX10은 추론만.

---

## 3. 조직 구조 (확정 + 자리 예약)

### 3.1 workspace 분리 = 2개로 시작 (최소 단위)
- **업무 workspace** / **인프라 workspace**. 완전 격리로 신호/잡음 분리.
- 2개는 팀 간 연결(브릿지)·격리·투표를 검증하는 최소 단위. 팀이 늘면 workspace가 늘어난다(프랙탈).

### 3.2 현재 AI peer 구성 (총 8 + 사람 1)
**업무 workspace** — RA 전문가는 처음부터 지역별 3종(규제 철학이 근본적으로 달라 표상 분리):
- **한국 RA** (MFDS/KGMP) — 독자 체계 + 국제 정합(2026.1 개정으로 OECD 임상자료·CER 수용). 해외 근거를 한국 체계로 잇는 가교형.
- **미국 RA** (FDA 510(k)) — substantial equivalence 논증이 핵심. 예측가능·신속(3–6개월). 효율·전략형. QMSR(2026.2 ISO 13485 정합) 반영.
- **유럽 RA** (CE MDR) — 기기별 임상 근거·포괄 문서가 핵심. Notified Body 심사. 철저·장기형.
- **OpenProject 사안 담당** — 사안 라이프사이클 추적.
- **n8n 자동화 담당** — 워크플로우 개선·신규(호출형).

**인프라 workspace** — 장비별 인프라 에이전트 ×3(라즈베리·T3610·GX10). 셋이 모여 분산 의사결정.

**사람** — 현재 1인, user peer 하나, 전체 최종 결정자.

### 3.3 완성형 조직 계층 (자리 예약 — 미리 설계, 구현은 단계적)
- **팀장**: 종합·대외 창구·배분. 통제 아님(중앙 두뇌 원칙 유지).
- **팀원**: 규제권별 전문가 등.
- **세부 전문가**: 인접 독립 직능(임상·품질·시판후감시·사이버보안). 판단 철학이 RA와 다르면 별도 에이전트.
- **세부 기법**: 같은 판단 체계 안의 경로·문서·논증법 → **스킬**로 누적.

### 3.4 사람 층 확장 (자리 예약)
조직이 커지면 사람도 단위별 할당(팀 담당 → 그룹 총괄 → 전체 책임). workspace 격리가 사람의 책임 경계. Honcho는 workspace당 다수 user peer 수용하므로 구조적으로 가능. 각 담당의 판단 성향이 해당 workspace에 독립 누적.
- **미결**: 사람이 여럿이 되면 사람 간 방향 정렬 문제(1인일 땐 없음). 그룹 총괄 또는 공통 헌장으로 해소.

---

## 4. T자형 성장 메커니즘 (확정)

| 획 | 내용 | 소스 | 성장 방식 |
|---|---|---|---|
| **가로(폭)** | 공통 지식 토대 | llm-wiki(NAS RAG, 인덱싱 중)·ra-project·MD-process — **이미 별도 프로젝트로 진행 중** | 공유 참조 — 토대가 풍부해지면 모든 에이전트가 함께 넓어짐 |
| **세로(깊이)** | 개별 전문성 | 자기 사안 처리 + 사람 3점 평가 | 분리 누적(Honcho) — 에이전트마다 독립적으로 깊어짐, 섞이지 않음 |

- 가로획은 에이전트가 직접 키우지 않는다. 전담 프로젝트가 키우고 에이전트는 단방향 참조(자체 RAG 중복 생성 금지). 가로·세로는 **독립 병렬**로 자라며 연결 지점에서 만난다.
- 세부 기법은 세로획의 더 깊은 층 → 스킬. 인접 직능은 또 하나의 T자 → 별도 에이전트.

---

## 5. 의사결정·학습 루프 (확정)

- **블랙보드 + 투표**: 조정자 없는 공유 판단 공간(workspace). 위험 감지한 에이전트가 자율로 투표 소집, 나머지가 응답. 선택형 판단엔 합의보다 투표가 적합.
- **작업 추적**: Hermes v0.13.0 정식 Kanban(durable multi-agent board: heartbeat·reclaim·zombie detection)을 인프라 에이전트 셋의 공유 작업 보드로 활용 가능. 투표 집계 자체는 별도 구현(ConsensusEngine 미구현).
- **사후 평가**: 사람이 공동 결정에 **3점 척도**(나쁨·보통·좋음) + 근거 한 줄. → Honcho AI peer 자기 표상으로 누적 → 자기 교정.
- **가중치 자동 조정**: 누적 평가가 **사안 영역별** 가중치를 조정(앞에서 설계하지 않음). 평가된 결정만 가중치 이동, 무평가는 중립.
- **부재 기반 성장**: 나뉜 구조라 부재가 드러남 → 예약 자리를 채움. 단 부재가 **패턴으로 확정**될 때만(조율 비용 > 전문성 이득 방지). 같은 철학이면 스킬, 독립 직능이면 에이전트.

---

## 6. 고정 규칙 (불변)

- **WP 완료·재오픈은 사람 전용.** 에이전트는 완료 제안만 덧글로. (완료 시점 맥락은 학습 신호로 포착)
- **n8n 워크플로우 변경은 보고 후 진행**(사람 승인).
- **인프라 파괴적 조치**(디스크 정리·컨테이너 삭제·설정 변경)는 사람 승인. 모니터링·보고는 자율.
- **순환 의존 회피**: Honcho 서버(T3610) 자체 장애는 Honcho 경유 브릿지로 나르지 않음 — n8n이 Honcho 우회 직접 경보.
- **매칭·덧글 추가는 자율**(되돌리기 쉬움, 덧글은 추가형이라 충돌 없음). 상태 전이(완료 제외)만 게이트·충돌 회피 대상.

---

## 7. 브릿지 (확정)

- 별도 두뇌가 아니다. 인프라 에이전트 셋이 인프라 workspace에서 투표로 종합 판단 → **n8n이 결과를 업무 workspace로 옮겨 씀**(판단=셋, 집계=규칙, 출력=n8n).
- 방향: 인프라 → 업무 단방향(운영 제약). 성격: 원시 데이터가 아닌 행동 가능한 최소 신호로 요약.
- 1차부터 자동(인프라 알림 전달에 한정 — 인프라 에이전트가 감지한 이상 신호를 사람 매개 없이 업무 workspace로 넘기는 것). 명시적 임계 조건만 규칙으로 감지. 사람은 알림 이력을 간헐 검토·튜닝.
  > **주의**: 이 "자동화"는 인프라 상태 알림 전달에만 해당한다. RA 규제 판단(매칭·분류·전이 제안)에서는 §0의 정확성 우선 원칙이 적용되며, 불확실한 RA 판단을 사람 검토 없이 넘기는 근거로 이 구절을 사용해서는 안 된다.

---

## 8. 1차 PoC 범위 (확정)

- **업무 도메인**: RA 업무 하나로 시작(OpenProject가 다루는 여러 업무 중). 성공 후 타 업무 도메인 확산.
- **RA 전문가 3종 전부 가동**(도메인이 RA 하나로 한정되므로 측정은 단일 통제).
- **해결 목표**: 재전송 메일 후속 왕복이 중복 WP로 등록되는 오류 교정.
- **첫 워크플로우**: Gmail 재전송 분석(mail-triage). form 접수는 2차.

### 매칭 동작 (확정)
- 재전송으로 원본 헤더(threadId/References) 파괴됨 → **본문 기반 매칭**이 주력.
- 본문에 원본 맥락(원 제목·원 발신자·인용 원문·사안 식별자) 보존 확인됨 → 정규화해 매칭 키. 후속 메일은 원문 인용 누적되어 신호 강함.
- 매칭 후보 = **미완료 WP**(오픈·진행중·리뷰중). 완료 WP 신규 메일은 재오픈 제안 또는 신규 WP.
- 사안↔WP 매핑을 Honcho conclusion으로 누적. WP 완료 시 후보에서 제거.
- **규제권 라우팅**: 본문의 규제기관(FDA/MDR/MFDS)·제출 종류로 해당 RA 전문가에 배정.

### OpenProject 워크플로우 (확정)
- 상태: 오픈 → 진행중 → 리뷰중 → 완료(다단계). 사람·에이전트 모두 처리 가능(완료만 사람 전용).
- 메일 내용이 전이 신호일 수 있음 → mail-triage가 전이 제안(1차 자동 실행 아님, Yellow 게이트).

---

## 9. 가상 오피스 (살) — 별도 MVP

- 뼈대(운영)와 분리된 표현 계층. 웹브라우저(비설치형), Docker 단일 컨테이너.
- **관찰자 구조**: 활동 기록을 읽기만, 운영에 개입 안 함. 실시간 아닌 **기록 재생**(조용하다 일 있을 때만 캐릭터가 잠깐 움직임 — 비동기·호출형 시스템의 정직한 표현).
- **목업 = 계약**: 뼈대 출력 형태(conclusion·투표·매칭·3점평가)를 목업으로 고정 → 살을 독립 선개발 → 연동 시 `DATA_SOURCE`만 목업→Honcho 교체.
- 뼈대는 시각화 존재를 모르고 운영 기록만 남김(단방향).
- 선례 다수 확인됨(코딩 에이전트 시각화 중심). 단 Honcho 데이터를 읽는 어댑터는 직접 필요.

---

## 10. 생태계 내 위치 (확정)

본 시스템은 의료기기 인허가 **거대 생태계의 한 독립 조각**. 어느 레포도 상위가 아니며, 조각들이 각자 완성되어 가며 맞물린다.

| 조각 | 역할 | 본 시스템과의 관계 |
|---|---|---|
| MD-process | 내부 SOP·정책 | 가로획 토대(단방향 참조) |
| ra-project | RA 규제 지식 | 가로획 토대(단방향 참조) |
| Regula(ra-med-bot) | 직원용 질의응답 챗봇 | 같은 지식원, 다른 방향(질의응답 vs 업무수행) |
| llm-wiki | NAS RAG 인덱싱 | 가로획 토대·지식 조회 인터페이스 |
| **RA 멀티 에이전트(본 시스템)** | 사안 능동 처리·학습 | — |
| 가상 오피스 | 활동 시각화 | 본 시스템 활동 기록 단방향 읽기 |

- 조각 간 **연계는 사람이 판단하는 별도 프로젝트**. 본 문서는 이 한 조각 완성에 집중하고 외부 연계는 인터페이스 자리만 비움.
- 생태계 지도(ECOSYSTEM.md)는 모든 레포에 동일 주입, 각자 자기 부분 갱신(운영 중 조각=스케줄형, 구현 중 조각=점검형).

---

## 11. 체크항목 (구현 중 검증)

> 표기: [검증됨]=공식 문서·도구로 가능 확인(2026-06-05), 나머지는 구현 중 실측 필요.

**인프라**: GX10 Qwen3의 tool-calling 노출 여부(deriver 관찰 추출 성공으로 판명) · 임베딩 로컬/클라우드 결정(로컬이면 벡터 차원 정합 수정) · T3610 Honcho ↔ ra-med-bot 자원 경합(Docker limit) · GX10 부하 집중·dream 주기(약 8h) 간섭 · 라즈베리 16G 프로파일 3개 동시 구동 한계 실측.
- [검증됨] Honcho self-host 스택(API+deriver+pgvector PG+Redis), OpenAI 호환 LLM 위임, DERIVER_WORKERS 분산 — 공식 문서·자동 설치 스크립트(elkimek/honcho-self-hosted) 존재.

**연동**: mail-triage 웹훅 왕복 · 재전송 본문 파싱 매칭 키 · 규제권 라우팅(결정론 vs 수신 전문가 판단) · 다수 규제권 사안의 RA 전문가 간 비동기 참조 · 인프라→업무 브릿지 동작 · Honcho 장애 우회 직접 경보.
- [검증됨] n8n의 OpenProject WP 생성·코멘트 추가·상태 변경 — 커뮤니티 노드 및 OpenProject MCP 서버(create/update_status/add_comment/get_statuses)로 가능 확인.

**동작**: 매칭 적중률 · close WP 매핑 제거 연동 · 경계 케이스 Yellow 게이트 · **중복 WP 생성 감소(핵심 지표)** · 전이 제안 정확도 · 사람 개입·정정 빈도 감소(성장 지표) · 사람 정정 유형의 차회 자동 적중(학습 회수).

**의사결정·평가**: 투표 자율 소집 트리거 · 집계 구현 위치(n8n vs Hermes 직접) · 3점 평가의 Honcho 반영 경로 · 가중치 사안영역별 분리.
- [부분] Hermes Kanban(v0.13.0 정식)으로 공유 작업 보드는 가능. ConsensusEngine(투표 집계)은 미구현 — 직접 개발 필요.

**workspace**: 두 workspace 간 필수 전달 정보 식별 · 사람 user peer 양 workspace 독립 표상.
- [검증됨] workspace 완전 격리(데이터·인증 경계), peer의 workspace 종속성 — 공식 아키텍처 문서 확인.

---

## 12. 미결 항목

- [완료] 레포 호스팅: GitHub 확정 (2026-06-05).
- [완료] 학습 시드: OP 이력 backfill 완료 (#18 SEED-1, 2026-06-09).
- 무평가 결정 해석: 중립 vs 약한 긍정.
- [완료] GX10 임베딩: 로컬(온프레미스) 확정 — 4096차원 (Qwen3 qwen3-embedding:latest, 2026-06-05).
- **[완료] T자형 가로획 구축**: ra-project·MD-process·Gitea/NAS 지식 인덱싱 경로 정리 완료 (#34, #35, #36).
- **[부분 완료] 성장 루프 계장화**: 성장 트리거 알림·자율 학습 루프 완료 (#38, #42). Layer 4 API → mail-triage 실시간 연결은 후속 (#37).
- **[진행중] 인프라 투표 활성화**: vote-rules.json 초기값 미설정, 브로드캐스트 n8n 미구현 (#39).
- **[부분 완료] 안전/QA 하드닝**: mail-triage Yellow 게이트·기존 WP 상태 검증·n8n env/config 외부화·테스트 하네스·문서 동기화 레포 반영 (#43~#47). #43~#45는 RPi n8n import 및 운영 E2E 검증 필요.
- 외부 지식 연계·Regula 연계: 각각 후속 연계 프로젝트 (사람이 시점 판단).
- 사람 다중화 시 방향 정렬 메커니즘.

---

## 13. 단계 요약

1. ~~**인프라 검증**~~ ✅: T3610 Honcho ↔ GX10 Qwen3 deriver 성공 (2026-06-05).
2. ~~**mail-triage 이관**~~ ✅: Gmail 재전송 분석 → RA 3종 → WP 처리 → GROWTH 루프 (2026-06-09).
3. ~~**T자형 가로획 구축**~~ ✅: ra-project·MD-process·Gitea/NAS 지식 인덱싱 경로 정리 (#34-36).
4. **성장 루프 계장화** (부분 완료): 성장 트리거 알림·자율 학습 루프 완료 (#38, #42), Layer 4 API mail-triage 연결 후속 (#37).
5. **인프라 투표 활성화** (진행 예정): vote-rules 초기값 · 브로드캐스트 구현 (#39).
6. **확장** (조건부): form 이관 · 세부 전문가 에이전트 · 프랙탈 workspace 추가 (#40-41).
7. **안전/QA 하드닝** (레포 반영): Yellow 게이트, WP 상태 검증, env/config 외부화, `npm test` 품질 게이트, 문서 동기화 (#43-47).

---

## 14. MVP 구현 가이드 (검증된 사실 기반, 2026-06-05)

추상 설계와 실제 착수 사이의 공백을 메우는 구체. 모든 항목은 공식 문서·실제 도구로 검증됨.

### 14.1 Honcho 서버 (T3610)

**스택**: API(FastAPI, :8000) + deriver 워커 + PostgreSQL(pgvector/pgvector:pg15) + Redis.
- 빠른 경로: **elkimek/honcho-self-hosted** 자동 설치 스크립트(Docker·Honcho·PG·Redis·Hermes 설정·MCP까지 약 3분). Hermes 전용으로 만들어짐.
- 수동 경로: plastic-labs/honcho의 `docker-compose.yml.example` → `docker-compose.yml` 복사 후 기동.

**필수 환경변수**:
- `DB_CONNECTION_URI=postgresql+psycopg://...` (psycopg 프리픽스 필수 — sqlalchemy 요건)
- `CACHE_URL=redis://redis:6379/0` , `CACHE_ENABLED=true`
- LLM: 기본값은 openai gpt-5.4-mini(텍스트)/text-embedding-3-small(임베딩). **GX10 Qwen3로 위임 시** Deriver/Dialectic/Summary/Dream 섹션의 `*_MODEL_CONFIG__OVERRIDES__BASE_URL`을 GX10 엔드포인트로 지정. **모델은 tool calling 지원 필수**(Qwen3 충족).
- 포트 바인딩(2026-06-05 갱신): API 0.0.0.0:8000, PG 0.0.0.0:5433→5432(호스트 충돌 방지), Redis 127.0.0.1:6379(루프백 유지). T3610 내 멀티 서비스 LAN 접근 목적.

**스키마**: 마이그레이션 실행 시 workspaces·peers·sessions·messages·큐 테이블 생성.
**확장**: `DERIVER_WORKERS`(기본 1) 증가로 처리량↑. deriver를 여러 장비에 분산하면 DB 큐로 조율.

**[확정] 임베딩 차원**: GX10 Qwen3 로컬 임베딩 확정 — 4096차원 (qwen3-embedding:latest). init-vector-dim.sql로 pgvector 스키마 초기화 적용 (2026-06-05).

**[확정] 운영 서비스 URL 맵 (2026-06-11, /opt/hermes-ra/.env 기준)**:

| 서비스 | URL / 경로 | 비고 |
|--------|-----------|------|
| Honcho API | `http://localhost:8000` | T3610 Docker |
| hermes-api-server.py (Layer 4) | `http://localhost:8643` | `API_SERVER_PORT=8643` |
| GX10 Ollama | `http://192.168.100.1:11434` | OpenAI-compatible, Qwen3 |
| n8n | `https://n8n.abyz-lab.work` | RPi 호스팅 |
| OpenProject | `https://plm.abyz-lab.work` | RPi 호스팅 |
| pgvector | `localhost:5433` | Docker 포트 바인딩 |
| Redis | `localhost:6379` | Docker, 루프백 |
| NAS | `/mnt/nas-ra/공통자료/RA` | T3610 NFS 로컬 마운트 (Tailscale 불필요) |

규제기관 API 키: `OPENFDA_API_KEY`, `LAW_GO_KR_OC`, `DATA_GO_KR_API_KEY` — 모두 .env 설정 완료. 신규 환경 구성 시 `.env.example` 참조.

### 14.2 RA 전문가 프로파일 (T3610)

- `hermes profile create ra-us` (→ `ra-us` 별칭 자동 생성), `--clone`으로 ra-eu·ra-kr 파생.
- 각 프로파일 `SOUL.md`에 페르소나(규제권 철학·판단 성향·고정 규칙). honcho.json의 host 블록에서 `workspace="work"`, `aiPeer="ra_us"` 등 지정.
- 메모리 도구로 학습: `honcho_conclude`(사안↔WP 매핑 기록), `peer="ai"`(자기 교정), `honcho_search/context`(과거 맥락 주입).

### 14.3 mail-triage 워크플로우 (라즈베리 n8n)

검증된 n8n 도구로 구성 가능:
- **OpenProject 연동**: 커뮤니티 노드(`n8n-nodes-openproject` 계열)가 WP 생성·조회·수정·목록·**코멘트 추가** 지원. 또는 OpenProject MCP 서버(`create_work_package`·`update_work_package_status`·`add_comment`·`get_statuses`·`get_types`)를 n8n MCP Client로 연결.
- **흐름**: Gmail 트리거 → 본문 파싱(원 제목·원 발신자·식별자 → 매칭 키 + 규제권 판별) → 해당 RA 프로파일 호출(Hermes `/v1/chat/completions` 또는 게이트웨이) → 분석 결과 수신 → 미완료 WP 매칭 시 코멘트 추가, 미매칭 시 WP 생성 → 결과를 Honcho conclusion으로 기록.
- **게이트**: 매칭·코멘트는 자율(Green). 상태 전이 제안은 Yellow(사람 확정). 완료는 사람 전용(불변).

### 14.4 가상 오피스 MVP (별도 웹앱)

- 현재 `virtual-office.html`이 목업 이벤트로 동작하는 프로토타입(코드 픽셀 캐릭터 내장).
- 정교화: Kenney CC0 캐릭터 PNG를 `assets/characters/`에 두고 CHARS의 `sprite` 경로로 교체(렌더 PNG 우선). pixel-character-guide.md 참조.
- 연동: 목업 `EVENTS` 배열을 실제 Honcho 활동 기록 소스로 교체(`DATA_SOURCE` 전환). 뼈대는 시각화를 모름(단방향).
- 배포: Docker 단일 컨테이너. 상시 가동 + Honcho 네트워크 접근 장비.

### 14.5 MVP 최소 성공 기준

1. T3610 Honcho가 GX10 Qwen3로 deriver 관찰 추출 성공(= tool-calling 노출 검증).
2. ra-us 프로파일이 재전송 메일을 분석해 미완료 WP에 코멘트 추가, 신규는 WP 생성.
3. 동일 사안 반복 메일에서 중복 WP 생성이 감소(핵심 지표).
4. 사람 3점 평가가 Honcho AI peer 표상에 반영되어 차회 분석에 영향.
