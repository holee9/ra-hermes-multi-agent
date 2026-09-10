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
# 실행 중 hermes 프로세스 — pid/부모/실행시간/사용자 + `-p <profile>` 토큰만 (그 외 argv 는 출력하지 않는다)
ps -eo pid,ppid,etime,user,args | awk '/[h]ermes/ {p=""; for(i=5;i<=NF;i++) if($i=="-p"){p=$(i+1)}; print $1,$2,$3,$4,"profile="p}'
# systemd 단위·타이머 (이름·상태만)
systemctl list-units --all --no-pager --plain | grep -iE 'hermes' | awk '{print $1, $3, $4}'
systemctl list-timers --all --no-pager --plain | grep -iE 'hermes|growth|study|advisory' | awk '{print $NF, $(NF-1)}'
# cron — hermes 를 부르는 줄의 **개수와 줄 번호만** (원문 출력 금지)
crontab -l 2>/dev/null | grep -n hermes | cut -d: -f1 | tr '\n' ' '; echo
sudo grep -ln hermes /etc/cron.d/* 2>/dev/null
# 두 서비스의 환경 — 라이브 PID, **정확한 변수명 allowlist** 의 값만 출력. 그 외 변수는 이름만 (값 없음)
GW=$(systemctl show -p MainPID --value hermes-gateway); API=$(systemctl show -p MainPID --value hermes-api-server)
ALLOW='^(HERMES_HOME|HERMES_PROFILE|HERMES_PROFILES_DIR|HERMES_BIN|HERMES_TIMEOUT|HIVE_LEDGER_PATH|HIVE_SUBMIT_ENABLED|KNOWLEDGE_SCRIPT|RAG_SCRIPT)='
for P in $GW $API; do echo "== pid $P"; sudo cat /proc/$P/environ | tr '\0' '\n' | grep -E "$ALLOW"; echo "-- other names:"; sudo cat /proc/$P/environ | tr '\0' '\n' | grep -vE "$ALLOW" | cut -d= -f1 | sort | tr '\n' ' '; echo; done
# gateway 와 RA profile 의 저장소 경로 키만 (값에 URL·자격증명이 있으면 키만 남긴다)
grep -nE '^(state|session|profile|home|data)[a-z_]*:' ~/.hermes/config.yaml ~/.hermes/profiles/ra-us/config.yaml ~/.hermes/profiles/ra-eu/config.yaml
```

**allowlist(정확히 이 명령만, 다른 것은 실행하지 않는다):** `ps -eo … | awk`(위 형태), `systemctl list-units/list-timers/show`, `crontab -l | grep -n | cut`, `sudo grep -ln hermes /etc/cron.d/*`, `/proc/<pid>/environ` 읽기(위 ALLOW 필터·이름만 출력), `grep -nE` on 위 3개 config.yaml. 환경 값이 출력되는 변수는 ALLOW 9개뿐이며 그중 자격증명은 없다(API_SERVER_KEY·HONCHO_*·ADVISORY_LLM_URL 등은 이름만).

기록: 호출자 목록(프로세스/서비스/cron), 각 호출자의 profile, gateway가 `ra-*` profile을 로드하는지 여부(`environ`·`config.yaml` 근거). **결론 형식**: "API 서버 외 `ra-us`/`ra-eu` 호출자 있음/없음(근거)". 있으면 API profile lock은 그 호출자를 덮지 못하므로 §3.1 범위 한정을 유지하고 설계를 다시 검토한다.

## 2. 처리 개시(accepted) 신호 — Hermes CLI가 노출하는 것 확인

```bash
# 최근 세션 파일 — 주의: ls -lt 는 **mtime**(마지막 수정)이지 생성 시각이 아니다. 생성 시각은 파일 내부 메타(§2 후보)로 본다
ls -lt --time-style=full-iso ~/.hermes/profiles/ra-us/sessions | head -5
# hermes CLI 옵션 — 주의: --help 에 hook 이 없다고 hook 이 없는 것이 아니다(코드 경로 §2 후보가 정본). 참고용
$HOME/.local/bin/hermes --help 2>&1 | grep -iE 'hook|session|resume|json' | head -10
# 세션 DB 스키마 (개시/턴 메타 컬럼 유무)
sqlite3 -readonly ~/.hermes/profiles/ra-us/state.db '.schema' 2>/dev/null | head -40
```

후보(codex, 설치 Hermes `f8adefde` 코드 읽기 — 실행·설치 없음): `agent/turn_context.py:238` inbound user turn의 조기 `_persist_session`, `:316` `pre_llm_call` hook(session_id/task_id/turn_id/user_message). CLI one-shot 경로는 `cli.py:13443` → `run_conversation` → `build_turn_context`. **둘 다 fail-soft** — 신호 부재를 미수신으로 읽으면 안 된다. 재사용 원칙: 기존 훅/저장 관측을 쓰고, 보존은 `msg_id ↔ session_id/turn_id/generation` 메타데이터만(본문 아님). 의미 구분 고정: 턴 준비 진입 ≠ 모델 수락 ≠ handled(§5.1).

확인 명령(읽기 전용):
```bash
sed -n 225,260p ~/.hermes/hermes-agent/agent/turn_context.py; sed -n 300,330p ~/.hermes/hermes-agent/agent/turn_context.py
grep -n "pre_llm_call\|_persist_session" -r ~/.hermes/hermes-agent/agent ~/.hermes/hermes-agent/hermes_cli 2>/dev/null | head
# 최근 one-shot 호출 뒤 profile sessions/state.db 에 turn 메타가 남는지 (승인된 호출 1회 후)
sqlite3 -readonly ~/.hermes/profiles/ra-us/state.db 'select name from sqlite_master where type="table"' 2>/dev/null
```

기록: "CLI가 입력 읽기/처리 개시를 외부에 알리는 방법 있음/없음" + 있으면 어느 훅/저장에서 `session_id/turn_id`를 읽을 수 있는지. 없으면 §3.1대로 `submitted`→`completed` 사이는 unknown으로 유지하고 P3에서 개시 신호 없이 운영 가능한지(턴 단위 간격 + reply 기반 handled만으로) 판단한다.

## 3. 3턴 스레드 재구성 실측 — (5) — **B부: 능동 실험**

빌더는 LLM을 부르지 않는다. 실제 호출은 **agentic CLI**(`--skills ra-expert`)라 읽기 전용이 아니다: 도구 실행, 파일 쓰기, Honcho 기록, 세션 저장, GX10 추론이 일어난다. profile·시각 승인은 도구의 외부 영향을 막지 못한다.

### 3.0 실행안 (사람 승인 대상 — 승인 없이는 §3 실행 금지) — **강제 가능한 설정으로만**

관측된 활성 도구면(이 세션, `hermes tools list`, 기본 profile 기준 — `ra-us`는 `hermes -p ra-us tools list --summary`로 다시 확인): `terminal`·`file`·`code_execution`·`browser`·`web`·`messaging`·`cronjob`·`delegation`·`computer_use`·`image_gen`·`tts`·`moa`·`todo`·`session_search`·`clarify`·`vision`·`memory`·`skills` 활성, MCP `filesystem` 전체 활성. 즉 일회성 호출 하나가 셸 실행·파일 쓰기·메시지 발송·cron 등록을 할 수 있다. **profile 사본은 도구·MCP·자격증명을 격리하지 않는다** — 아래는 CLI가 실제로 강제하는 설정이다.

| 항목 | 강제 수단 (실행 전 검증 명령) |
|---|---|
| toolset 별 쓰기 면 (설치 `toolsets.py`, 읽기만) | `skills` = `skills_list, skill_view, skill_manage`(**create/edit 포함** → 읽기 전용 아님). `memory` = `memory`(영속 메모리 **쓰기**; provider honcho면 Honcho peer에 기록). `safe` = tools 없음 + includes `web, vision, image_gen`(**외부 웹 요청** 포함 → 무영향 아님). 쓰기 없는 built-in toolset은 **없다**. `-t memory,skills`는 읽기 전용 집합이 아니다 |
| 도구 비활성 (확인된 지원 기능만) | 제한 단위는 **toolset**뿐이다(설치 `model_tools.py:352-381` `enabled_toolsets`는 toolset 이름만 validate/resolve; 개별 도구명 `-t skill_view`는 미지원, `tools_config.py` include/exclude는 MCP 서버용이라 builtin `skill_manage` 차단에 쓸 수 없다 — codex 코드 읽기). 실험 profile에서 `hermes -p ra-us-p30test tools disable terminal,file,code_execution,browser,web,messaging,cronjob,delegation,computer_use,image_gen,tts,moa,todo,session_search,clarify,vision` 후 `tools list --summary`로 남은 toolset이 `memory`·`skills`뿐임을 확인 |
| memory·skills 쓰기 허용 범위 (읽기 전용이 필수는 아니다 — **승인된 실험 저장소 안이면 허용**) | 두 toolset은 쓴다. 허용 조건 = 쓰기 대상이 실험 profile 전용 저장소임을 확인: (1) memory: config 파일을 **구조 파서**로 읽어 키만 출력(`grep '^\S+:'`는 스칼라 값도 찍는다): `P=$(hermes -p ra-us-p30test config path); python3 -c "import sys,yaml; c=yaml.safe_load(open(sys.argv[1])) or {}; print('top:', sorted(c)); m=c.get('memory') or {}; print('memory keys:', sorted(m)); print({k: m.get(k) for k in ('provider','workspace','workspace_id','peer','peer_name','pin_peer_name') if k in m})" "$P"` — 값을 찍는 키는 이 6개뿐; 플러그인 기본 `workspace_id="hermes"`, `peer_name=None`→호스트명, `plugins/memory/honcho/client.py:296-312`) → peer가 운영 `ra_us`/`ra_eu`와 **다름**을 확인. (2) skills: `readlink -f ~/.hermes/profiles/ra-us-p30test/skills`가 운영 profile·공용 `~/.hermes/skills`를 가리키지 않음을 확인. 둘 다 충족 → `-t memory,skills` 허용, 쓰기는 그 저장소 안으로 한정됨을 기록. 하나라도 미충족 → **실험을 보류**하고 격리 경로를 먼저 마련한다(무도구·무메모리 기준선은 운영 RA의 도구·메모리 동작 검증을 대체하지 못하므로 측정으로 치지 않는다). `-t ""`는 0개 강제가 **아니다** — 설치 `cli.py:13178-13193`에서 toolsets가 비면 `_get_platform_tools(config, 'cli')`로 **fallback**한다(codex 코드 읽기). 따라서 강제 수단은 profile config의 `tools disable`뿐이고, 실행 전 검증은 `hermes -p ra-us-p30test tools list --summary`(resolver가 실제로 쓰는 목록)로만 한다. 첫 호출 exit code로는 확인할 수 없다 |
| MCP | `hermes -p ra-us-p30test mcp list` → 서버가 있으면 `hermes -p ra-us-p30test mcp remove <name>` → 다시 `mcp list`가 비어 있음을 확인 |
| 호출 단위 이중 제한 | 매 호출 `-t <위 결정의 toolset>` + `--max-turns 6` |
| 자격증명·저장소 실제 경로 | `hermes -p ra-us-p30test config path`·`env-path`로 **경로만** 출력. `ls -la $(dirname <path>)`로 `auth.json`·`.env`·`sessions`·`state.db`가 symlink인지, 운영 `~/.hermes/profiles/ra-us` 또는 `~/.hermes` 공용 파일을 가리키는지 확인(`readlink -f`). 공유면 "격리 아님"으로 기록하고 실험 입력에 자격증명이 필요한 스킬 도구를 쓰지 않는다. `config show` 전체 출력은 하지 않는다(값 제한 불가) |
| 스킬 | `hermes skills list`에서 `ra-expert`가 local/enabled로 확인됨(이 세션). 스킬 목록은 **활성 권한 목록이 아니다** — 스킬이 호출하는 도구는 위 toolset 제한을 받는다 |
| 예산·시간 | 호출 3회 이내(3턴 1·5턴 1·재시도 1), `timeout 900` 래퍼(`time`은 제한이 아니다), GX10 토큰 상한은 profile 모델 설정값을 기록 |
| 중지 조건 | 응답 로그에 terminal/file/messaging/write_file/patch/send_message 호출 흔적이 보이면 즉시 중단·기록(비활성이면 있어선 안 된다). `skill_manage`·`memory` 호출은 허용 저장소 안이면 기록만, 밖(경로가 실험 profile 밖)이면 중단. timeout 1회 초과 시 중단 |
| 성장 지표 제외 근거 | `scripts/growth-metrics.py` 69–74행: 지표는 metadata `record_type ∈ EXPECTED_GROWTH_RECORD_TYPES`(score_given·mail_triaged·ra_analysis·study_session_complete·study_insight)만 집계. CLI 직접 호출의 Honcho memory 쓰기에는 `record_type`이 없어 `unclassified`(360행)로 분류돼 **성장 지표에는 들어가지 않는다**. 단 `sessions_scanned/messages_scanned` 수집 진단 카운트에는 포함될 수 있으므로 실험 세션 id를 #150에 남긴다. `purpose` 태그만으로 제외되는 것이 아니다 |
| 기록 | 응답 본문 미기록, 품질 판정·토큰·시간만. 실험 profile은 실측 후 `hermes profile delete ra-us-p30test`(사람) |

### 3.1 입력

"3턴"은 **실제 3턴 conversation**이어야 한다 — 긴 스레드를 `--max-events 3`으로 잘라낸 것은 3턴 품질이 아니다(생략 안내 줄이 들어가고 맥락이 끊긴다). 목업에서 3턴은 `conv_1042_class`, 5턴은 `conv_1042_vote`.

```bash
# (a) 입력 생성 (읽기 전용)
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T093210_0015 --json  > /tmp/ctx-3turn.json
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T093210_0015         > /tmp/ctx-3turn.txt
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T091100_0012 --json     > /tmp/ctx-5turn.json
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T091100_0012            > /tmp/ctx-5turn.txt
# (b) 실제 호출 — §3.0 승인 후, 실험용 profile 로만
# 실행 전: tools list --summary 가 memory·skills 만, mcp list 가 비어 있음, memory peer·skills 경로 격리를 확인·기록했는가? (미확인이면 실행하지 않는다)
timeout 900 $HOME/.local/bin/hermes -p ra-us-p30test -t memory,skills --max-turns 6 -z "$(cat /tmp/ctx-3turn.txt)" --skills ra-expert > /tmp/out-3turn.txt; echo "exit=$?"
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
