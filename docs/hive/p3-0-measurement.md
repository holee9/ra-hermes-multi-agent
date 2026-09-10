# P3-0 실측 런북 — 세션 모델 A 연결 전 필수 (#150)

> 이 문서는 **실터미널(T3610 실제 셸)** 에서 사람이 실행할 명령과 기록 형식이다. Claude Code Bash 세션은
> 도커·systemd·`/opt`·다른 프로세스 환경을 볼 수 없어(`CLAUDE.local.md`) 여기 항목을 대신 실행하지 못한다.
> 모든 명령은 **읽기 전용**이다. 결과는 #150 댓글에 그대로 붙인다(자격증명·메일 본문이 섞이면 가린다).

## 0. 현재까지의 근거 (코드·디렉터리 읽기, 2026-09-10)

| 항목 | 관측 | 출처 |
|---|---|---|
| RA 진입점 | `hermes -p <profile> -z <context> --skills ra-expert` 일회성 subprocess, `/v1/chat/completions`(운영) + `_invoke_hermes`(hive submit) | `scripts/hermes-api-server.py` |
| 별도 gateway | `hermes-gateway.service` PID 2874353, argv `hermes gateway`, `-p` 없음, HERMES_HOME/PROFILE 환경 없음 | codex 읽기 전용 실측 |
| profile 저장소 | `~/.hermes/profiles/{ra-us,ra-eu,ra-kr,…}` 각각 `SOUL.md`·`config.yaml`·`state.db`·`sessions`를 **따로** 가짐. gateway는 `~/.hermes/state.db`·`~/.hermes/sessions` 사용 추정 | 디렉터리 목록(이 세션, 읽기만). `config.yaml`이 다른 경로를 가리킬 수 있어 **격리 확정 아님** |
| CLI 세션 | resume 없으면 호출마다 새 session id; `active_sessions` lease는 총량 상한 | codex, `cli.py:3399`/`3494` |

## 1. host 전체 hermes 호출자 목록 — (1)

```bash
# 실행 중 프로세스 (argv 전체)
ps -eo pid,ppid,etime,user,args | grep -E '[h]ermes' 
# systemd 단위·타이머
systemctl list-units --all --no-pager | grep -i hermes
systemctl list-timers --all --no-pager | grep -iE 'hermes|growth|study|advisory'
# cron
crontab -l 2>/dev/null; sudo ls /etc/cron.d 2>/dev/null
# 두 서비스의 환경 (profile 경로 확정)
sudo cat /proc/2874353/environ | tr '\0' '\n' | grep -E '^HERMES|^HOME'
sudo cat /proc/$(systemctl show -p MainPID --value hermes-api-server)/environ | tr '\0' '\n' | grep -E '^HERMES|^HOME|^HIVE'
# gateway 와 RA profile 의 저장소가 같은 파일인지
grep -nE 'state|session|profile|home' ~/.hermes/config.yaml ~/.hermes/profiles/ra-us/config.yaml ~/.hermes/profiles/ra-eu/config.yaml
```

기록: 호출자 목록(프로세스/서비스/cron), 각 호출자의 profile, gateway가 `ra-*` profile을 로드하는지 여부(`environ`·`config.yaml` 근거). **결론 형식**: "API 서버 외 `ra-us`/`ra-eu` 호출자 있음/없음(근거)". 있으면 API profile lock은 그 호출자를 덮지 못하므로 §3.1 범위 한정을 유지하고 설계를 다시 검토한다.

## 2. 처리 개시(accepted) 신호 — Hermes CLI가 노출하는 것 확인

```bash
# 최근 세션 파일과 그 생성 시각 (CLI 가 세션을 언제 만드는지)
ls -lt --time-style=full-iso ~/.hermes/profiles/ra-us/sessions | head -5
# hermes CLI 의 hook/로그 옵션 (개시 시점 신호 유무)
$HOME/.local/bin/hermes --help 2>&1 | grep -iE 'hook|log|session|resume|json' 
# 세션 DB 스키마 (개시 시각 컬럼 유무)
sqlite3 ~/.hermes/profiles/ra-us/state.db '.schema' 2>/dev/null | head -40
```

기록: "CLI가 입력 읽기/처리 개시를 외부에 알리는 방법 있음/없음". 없으면 §3.1대로 `submitted`→`completed` 사이는 unknown으로 유지하고 P3에서 개시 신호 없이 운영 가능한지(턴 단위 간격 + reply 기반 handled만으로) 판단한다.

## 3. 3턴 스레드 재구성 실측 — (5)

빌더는 LLM을 부르지 않는다. 같은 입력으로 사람이 실제 호출해 토큰·품질을 잰다. **운영 profile로 호출하면 Honcho·세션에 기록이 남는다** — 반드시 사람 승인된 profile/시각에 실행하고 결과를 #150에 남긴다.

```bash
# (a) 입력 생성: 목업 log 의 5턴 conversation (실제 log.jsonl 이 생기면 그 경로로)
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T091100_0012 --json
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T091100_0012 > /tmp/ctx-5turn.txt
# 3턴 샘플: --max-events 3
python3 tools/hive_thread.py virtual-office/mock/events-v2.1.jsonl evt_20260909T091100_0012 --max-events 3 > /tmp/ctx-3turn.txt
# (b) 실제 호출 (승인 후) — 실측 토큰은 hermes 출력/로그의 usage 를 쓴다. usage 가 없으면 GX10 서버 로그의 prompt_tokens 를 쓴다
time $HOME/.local/bin/hermes -p ra-us -z "$(cat /tmp/ctx-3turn.txt)" --skills ra-expert > /tmp/out-3turn.txt
```

기록 표:

| 입력 | chars | est_tokens(chars/4, 참고) | **실측 prompt_tokens** | 응답 시간 | 품질(사람 판정: 스레드 맥락 반영/오류) |
|---|---|---|---|---|---|
| 3턴 | (빌더 보고) | (빌더 보고) | | | |
| 5턴 | 755 | 188 | | | |

목업 5턴 빌더 보고(이 세션 실행): `chars=755, lines=10, est_tokens_heuristic=188, truncated=0`. 이 수치는 크기이지 비용이 아니다.

## 4. 배포 (별도, #150 5615905208·5615930525)

12파일 manifest 백업 → `bash scripts/deploy-local.sh --dry-run` → 실행 → 12파일 sha256 강제 대조 → 서비스 재시작 → `GET /health`. `HIVE_SUBMIT_ENABLED`는 **설정하지 않는다**(기본 비활성 유지). `HIVE_LEDGER_PATH`도 P3 파일럿 승인 전에는 설정하지 않는다.

## 5. 완료 판정

1~3의 기록이 #150에 있고, (1)에서 API 외 `ra-*` 호출자가 없거나 lock 범위가 재설계됐으며, (3)의 실측 토큰·품질이 사람 기준을 넘을 때 drain sink 연결(P3-2 sink adapter)을 별도 커밋으로 진행한다. 그 전에는 `hive_submit`은 비활성, drain은 dry-run이다.
