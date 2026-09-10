# P3-0 실측 런북 — 세션 모델 A 연결 전 필수 (#150)

> 이 문서는 **실터미널(T3610 실제 셸)** 에서 사람이 실행할 명령과 기록 형식이다. Claude Code Bash 세션은
> 도커·systemd·`/opt`·다른 프로세스 환경을 볼 수 없어(`CLAUDE.local.md`) 여기 항목을 대신 실행하지 못한다.
> **A부(§1·§2)는 읽기 전용**, **B부(§3)는 능동 실험**이다 — `hermes -z --skills ra-expert`는 agentic CLI라 도구를 실행하고
> 파일·Honcho·세션에 쓴다. profile·시각 승인만으로 도구의 외부 영향이 격리되지 않으므로 B부는 도구·대상·예산·중지 조건을
> 한정한 실행안(§3.0)을 사람이 승인한 뒤에만 실행한다. 결과는 #150 댓글에 붙이되 **필요한 필드만** 붙인다(argv 전체·crontab
> 전체·환경 전체 덤프 금지 — 자격증명·메일 본문이 섞인다).

## 0. 현재까지의 근거 (코드·디렉터리 읽기, 2026-09-10)

| 항목 | 관측 | 출처 |
|---|---|---|
| RA 진입점 | `hermes -p <profile> -z <context> --skills ra-expert` 일회성 subprocess, `/v1/chat/completions`(운영) + `_invoke_hermes`(hive submit) | `scripts/hermes-api-server.py` |
| 별도 gateway | `hermes-gateway.service` PID 2874353, argv `hermes gateway`, `-p` 없음, HERMES_HOME/PROFILE 환경 없음 | codex 읽기 전용 실측 |
| profile 저장소 | `~/.hermes/profiles/{ra-us,ra-eu,ra-kr,…}` 각각 `SOUL.md`·`config.yaml`·`state.db`·`sessions`를 **따로** 가짐. gateway는 `~/.hermes/state.db`·`~/.hermes/sessions` 사용 추정 | 디렉터리 목록(이 세션, 읽기만). `config.yaml`이 다른 경로를 가리킬 수 있어 **격리 확정 아님** |
| CLI 세션 | resume 없으면 호출마다 새 session id; `active_sessions` lease는 총량 상한 | codex, `cli.py:3399`/`3494` |

## 1. host 전체 hermes 호출자 목록 — (1)

```bash
# 실행 중 hermes 프로세스 — pid/부모/실행시간 + argv 는 profile 인자만 (전체 argv 덤프 금지)
ps -eo pid,ppid,etime,user,args | grep -E '[h]ermes' | sed -E 's/(-p [^ ]+).*/\1/' | cut -c1-120
# systemd 단위·타이머 (이름·상태만)
systemctl list-units --all --no-pager --plain | grep -iE 'hermes' | awk '{print $1, $3, $4}'
systemctl list-timers --all --no-pager --plain | grep -iE 'hermes|growth|study|advisory' | awk '{print $NF, $(NF-1)}'
# cron — hermes 를 부르는 줄만
crontab -l 2>/dev/null | grep -n hermes; sudo grep -ln hermes /etc/cron.d/* 2>/dev/null
# 두 서비스의 환경 — **라이브 PID** 를 systemd 에서 읽고, HERMES*/HIVE* 키만 (값에 토큰이 있으면 가린다)
GW=$(systemctl show -p MainPID --value hermes-gateway); API=$(systemctl show -p MainPID --value hermes-api-server)
sudo cat /proc/$GW/environ  | tr '\0' '\n' | grep -E '^(HERMES|HIVE)[A-Z_]*=' | sed -E 's/(KEY|TOKEN|SECRET)=.*/\1=***/'
sudo cat /proc/$API/environ | tr '\0' '\n' | grep -E '^(HERMES|HIVE)[A-Z_]*=' | sed -E 's/(KEY|TOKEN|SECRET)=.*/\1=***/'
# gateway 와 RA profile 의 저장소 경로 키만
grep -nE '^(state|session|profile|home|data)[a-z_]*:' ~/.hermes/config.yaml ~/.hermes/profiles/ra-us/config.yaml ~/.hermes/profiles/ra-eu/config.yaml
```

**allowlist(정확히 이 명령만, 다른 것은 실행하지 않는다):** `ps`, `systemctl list-units/list-timers/show`, `crontab -l`, `grep -ln` on `/etc/cron.d`, `/proc/<pid>/environ` 읽기(필터), `grep -n` on 위 3개 config.yaml.

기록: 호출자 목록(프로세스/서비스/cron), 각 호출자의 profile, gateway가 `ra-*` profile을 로드하는지 여부(`environ`·`config.yaml` 근거). **결론 형식**: "API 서버 외 `ra-us`/`ra-eu` 호출자 있음/없음(근거)". 있으면 API profile lock은 그 호출자를 덮지 못하므로 §3.1 범위 한정을 유지하고 설계를 다시 검토한다.

## 2. 처리 개시(accepted) 신호 — Hermes CLI가 노출하는 것 확인

```bash
# 최근 세션 파일 — 주의: ls -lt 는 **mtime**(마지막 수정)이지 생성 시각이 아니다. 생성 시각은 파일 내부 메타(§2 후보)로 본다
ls -lt --time-style=full-iso ~/.hermes/profiles/ra-us/sessions | head -5
# hermes CLI 옵션 — 주의: --help 에 hook 이 없다고 hook 이 없는 것이 아니다(코드 경로 §2 후보가 정본). 참고용
$HOME/.local/bin/hermes --help 2>&1 | grep -iE 'hook|session|resume|json' | head -10
# 세션 DB 스키마 (개시/턴 메타 컬럼 유무)
sqlite3 ~/.hermes/profiles/ra-us/state.db '.schema' 2>/dev/null | head -40
```

후보(codex, 설치 Hermes `f8adefde` 코드 읽기 — 실행·설치 없음): `agent/turn_context.py:238` inbound user turn의 조기 `_persist_session`, `:316` `pre_llm_call` hook(session_id/task_id/turn_id/user_message). CLI one-shot 경로는 `cli.py:13443` → `run_conversation` → `build_turn_context`. **둘 다 fail-soft** — 신호 부재를 미수신으로 읽으면 안 된다. 재사용 원칙: 기존 훅/저장 관측을 쓰고, 보존은 `msg_id ↔ session_id/turn_id/generation` 메타데이터만(본문 아님). 의미 구분 고정: 턴 준비 진입 ≠ 모델 수락 ≠ handled(§5.1).

확인 명령(읽기 전용):
```bash
sed -n 225,260p ~/.hermes/hermes-agent/agent/turn_context.py; sed -n 300,330p ~/.hermes/hermes-agent/agent/turn_context.py
grep -n "pre_llm_call\|_persist_session" -r ~/.hermes/hermes-agent/agent ~/.hermes/hermes-agent/hermes_cli 2>/dev/null | head
# 최근 one-shot 호출 뒤 profile sessions/state.db 에 turn 메타가 남는지 (승인된 호출 1회 후)
sqlite3 ~/.hermes/profiles/ra-us/state.db 'select * from sqlite_master where type="table"' 2>/dev/null
```

기록: "CLI가 입력 읽기/처리 개시를 외부에 알리는 방법 있음/없음" + 있으면 어느 훅/저장에서 `session_id/turn_id`를 읽을 수 있는지. 없으면 §3.1대로 `submitted`→`completed` 사이는 unknown으로 유지하고 P3에서 개시 신호 없이 운영 가능한지(턴 단위 간격 + reply 기반 handled만으로) 판단한다.

## 3. 3턴 스레드 재구성 실측 — (5) — **B부: 능동 실험**

빌더는 LLM을 부르지 않는다. 실제 호출은 **agentic CLI**(`--skills ra-expert`)라 읽기 전용이 아니다: 도구 실행, 파일 쓰기, Honcho 기록, 세션 저장, GX10 추론이 일어난다. profile·시각 승인은 도구의 외부 영향을 막지 못한다.

### 3.0 실행안 (사람 승인 대상 — 승인 없이는 §3 실행 금지)

| 항목 | 한정 |
|---|---|
| 도구 | ra-expert 스킬이 부를 수 있는 도구 목록을 먼저 열거(`~/.hermes/profiles/ra-us/skills` 또는 스킬 정의 읽기). OpenProject·메일·외부 API 쓰기 도구가 있으면 **실험에서 비활성**(스킬 옵션 또는 실험용 profile 사본 `ra-us-p30test`로 격리). T3610은 OP를 쓰지 않는다는 계약 C를 실험에서도 지킨다 |
| 대상 | 실험용 profile 사본 1개(운영 `ra-us` 상태·세션에 섞지 않음). Honcho 기록은 실험 세션 id 로 표시해 성장 지표에서 제외(`purpose: p30-measure`) |
| 예산 | 호출 3회 이내(3턴 1·5턴 1·재시도 1), 호출당 timeout 900s, GX10 토큰 상한은 profile 설정값 |
| 중지 조건 | 도구가 파일 시스템 밖(네트워크 쓰기)으로 나가는 로그가 보이면 즉시 중단·기록. timeout 1회 초과 시 중단 |
| 기록 | 응답 본문은 붙이지 않고 품질 판정만; 토큰은 §3.2 정의대로 |

### 3.1 입력

"3턴"은 **실제 3턴 conversation**이어야 한다 — 긴 스레드를 `--max-events 3`으로 잘라낸 것은 3턴 품질이 아니다(생략 안내 줄이 들어가고 맥락이 끊긴다). 목업에서 3턴은 `conv_1042_class`, 5턴은 `conv_1042_vote`.

```bash
# (a) 입력 생성 (읽기 전용)
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T093210_0015 --json  > /tmp/ctx-3turn.json
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T093210_0015         > /tmp/ctx-3turn.txt
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T091100_0012 --json     > /tmp/ctx-5turn.json
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T091100_0012            > /tmp/ctx-5turn.txt
# (b) 실제 호출 — §3.0 승인 후, 실험용 profile 로만
time $HOME/.local/bin/hermes -p ra-us-p30test -z "$(cat /tmp/ctx-3turn.txt)" --skills ra-expert > /tmp/out-3turn.txt
```

### 3.2 토큰 정의

한 호출의 비용은 **그 session/turn 에 묶인 모든 LLM 요청(도구 루프·재시도 포함)의 prompt+completion 합계**다. 단일 `usage` 한 줄이 아니다. 연결 키는 §2에서 확인한 session_id/turn_id(또는 GX10 요청 로그의 request id). 합산이 불가능하면 "합산 불가 — 요청 N건 중 M건만 집계"로 적는다.

기록 표:

| 입력 | chars | est_tokens(chars/4, 참고) | **실측 토큰 합계(요청 N건)** | 응답 시간 | 품질(사람 판정: 스레드 맥락 반영/오류) |
|---|---|---|---|---|---|
| 3턴 (`conv_1042_class`, 실제 3턴) | (빌더 보고) | (빌더 보고) | | | |
| 5턴 (`conv_1042_vote`) | 755 | 188 | | | |

목업 5턴 빌더 보고(이 세션 실행): `chars=755, lines=10, est_tokens_heuristic=188, truncated=0`. 이 수치는 크기이지 비용이 아니다.

## 4. 배포 (별도, #150 5615905208·5615930525)

12파일 manifest 백업 → `bash scripts/deploy-local.sh --dry-run` → 실행 → 12파일 sha256 강제 대조 → 서비스 재시작 → `GET /health`. `HIVE_SUBMIT_ENABLED`는 **설정하지 않는다**(기본 비활성 유지). `HIVE_LEDGER_PATH`도 P3 파일럿 승인 전에는 설정하지 않는다.

## 5. 완료 판정

1~3의 기록이 #150에 있고, (1)에서 API 외 `ra-*` 호출자가 없거나 lock 범위가 재설계됐으며, (3)의 실측 토큰·품질이 사람 기준을 넘을 때 drain sink 연결(P3-2 sink adapter)을 별도 커밋으로 진행한다. 그 전에는 `hive_submit`은 비활성, drain은 dry-run이다.
