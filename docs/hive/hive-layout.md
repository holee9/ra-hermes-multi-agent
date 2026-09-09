# hive 레이아웃 및 쓰기 규율

> 해결하는 결손: **D3 동시 쓰기 규율 부재**
> 원천: Munder Difflin HIVE.md §2 확정 결정 1·2, §3 온디스크 레이아웃 (MIT)
> 저장 위치: Gitea 저장소 `ra-hive` (신규, DS224+). 정본은 git이며 NAS JSONL은 사영.

---

## 1. 디렉토리

```
ra-hive/
  PROTOCOL.md                 # peer 대면 규약 → hive/PROTOCOL.md
  registry/
    actors.json               # 로스터 — config-as-code, 변경은 PR
    workspaces.json           # workspace(=층) 정의
  log.jsonl                   # append-only 이벤트 로그 (계약 v2.1). 살의 유일 원천
  agents/<actor_id>/
    identity.md               # 역할·역량 — PR로만 변경
    inbox/                    # 라우터가 씀, peer가 읽음
    inbox/.done/              # 라우터가 옮김 — 삭제 없음, 감사 보존
    outbox/                   # peer가 씀, 라우터가 비움
    outbox/.sent/             # 라우터가 옮김
    cursor.json               # 라우터 관리 { last_processed: "<id>" }
```

MD와의 차이:
- `board.md`(공동 편집 블랙보드) **없음** — 단일 서기가 GOD이므로. OpenProject WP가 대체.
- `tasks.json` **없음** — OpenProject WP가 원장.
- `memory.md` **없음** — Honcho가 학습 계층. 파일 메모리를 두면 이중 원천.
- `registry.json` → `registry/` 디렉토리로 분리. 로스터와 workspace를 각각 PR 단위로.

---

## 2. 쓰기 규율 — 누가 무엇을 쓰는가

| 경로 | 기록자 | 읽는 자 |
|---|---|---|
| `agents/<a>/outbox/` | **peer `a`만** | 라우터 |
| `agents/<a>/inbox/` | **라우터만** | peer `a` |
| `agents/<a>/inbox/.done/` | 라우터만 | 감사 |
| `agents/<a>/cursor.json` | 라우터만 | 라우터 |
| `log.jsonl` | **라우터만** | 살, 감사, 정책 엔진 |
| `registry/*` | **사람 (PR 머지)** | 라우터, 살 |
| `agents/<a>/identity.md` | 사람 (PR 머지) | peer `a` 시작 시 |
| `PROTOCOL.md` | 사람 (PR 머지) | 모든 peer 시작 시 |

**불변 규칙 4가지**

1. **파일당 단일 기록자.** 어떤 파일도 두 프로세스가 쓰지 않는다. 위 표에 없는 조합은 금지.
2. **단일 커미터.** git 커밋은 **라우터(n8n)만** 수행한다. peer는 git을 호출하지 않는다. `.git/index.lock` 손상의 원천 제거.
3. **메시지 1건 = 파일 1개.** 공유 메일박스 파일 금지. 임시 파일 → `rename`으로 원자적 기록.
4. **삭제 없음.** 처리분은 `.done/`·`.sent/`로 이동. 감사 추적은 삭제로 끊기지 않는다.

---

## 3. 원자적 기록 — peer 측 구현

```bash
# peer가 outbox에 쓸 때
tmp="$OUTBOX/.tmp-$$-$RANDOM"
printf '%s' "$json" > "$tmp"
mv "$tmp" "$OUTBOX/$(date -u +%Y%m%dT%H%M%S)-$(openssl rand -hex 2).json"
```

`.tmp-*` 접두 파일은 라우터가 무시한다. `mv`는 같은 파일시스템 내에서 원자적이다.

---

## 4. registry/actors.json

```json
{
  "version": 1,
  "actors": {
    "ra_us": {
      "workspace": "work",
      "role": "US 규제 전문가",
      "display_name": "Mike",
      "modalities": ["text", "docx", "xlsx"],
      "seat": { "floor": 1, "x": 4, "y": 4 },
      "status": "active",
      "hermes_profile": "ra-us",
      "host": "t3610"
    },
    "ra_eu": { "workspace": "work", "role": "EU 규제 전문가", "display_name": "Theo",
               "modalities": ["text", "docx"], "seat": { "floor": 1, "x": 6, "y": 4 },
               "status": "active", "hermes_profile": "ra-eu", "host": "t3610" },
    "ra_kr": { "workspace": "work", "role": "KR 규제 전문가", "display_name": "Sam",
               "modalities": ["text", "docx"], "seat": { "floor": 1, "x": 8, "y": 4 },
               "status": "active", "hermes_profile": "ra-kr", "host": "t3610" },
    "ra_case": { "workspace": "work", "role": "사안 관리", "display_name": "Margot",
                 "modalities": ["text"], "seat": { "floor": 1, "x": 4, "y": 8 },
                 "status": "paused", "hermes_profile": null, "host": null },
    "op_manager": { "workspace": "work", "role": "자동화·OpenProject", "display_name": "Olly",
                    "modalities": ["text"], "seat": { "floor": 1, "x": 6, "y": 8 },
                    "status": "active", "hermes_profile": "op-manager", "host": "t3610" },
    "infra_t3610": { "workspace": "infra", "role": "T3610 운영", "display_name": "Finn",
                     "modalities": ["text"], "seat": { "floor": 2, "x": 4, "y": 4 },
                     "status": "active", "hermes_profile": "infra-t3610", "host": "t3610" },
    "infra_gx10": { "workspace": "infra", "role": "GX10 운영", "display_name": "Leo",
                    "modalities": ["text"], "seat": { "floor": 2, "x": 6, "y": 4 },
                    "status": "active", "hermes_profile": "infra-gx10", "host": "t3610" },
    "infra_rpi": { "workspace": "infra", "role": "Raspberry Pi 운영", "display_name": "Gus",
                   "modalities": ["text"], "seat": { "floor": 2, "x": 8, "y": 4 },
                   "status": "active", "hermes_profile": "infra-rpi", "host": "t3610" }
  }
}
```

- `display_name`은 **살에서만** 사용. 이벤트·메시지에 절대 등장하지 않는다(원칙 9). 이 파일이 매핑 테이블의 유일 위치다.
- `status`: `active` \| `paused` \| `archived`. 라우터는 `active`에만 전달. `broadcast` 팬아웃 대상도 `active`만.
- 좌석은 6월 구성원 화면의 좌표 체계(1F (4,4) 등)를 그대로 따른다.
- `n8n_manager`는 라우터 자신이므로 actor로 등록하지 않는다. `hive/PROTOCOL.md` 대상 목록도 동일.

### 4.1 actor ↔ Hermes 프로필 ↔ 호스트 매핑 (실측 2026-09-09)

**actor ID와 프로필 ID는 별개 식별자다.** actor ID(=Honcho peer ID)는 밑줄(`ra_us`), Hermes 프로필 디렉토리는 하이픈(`ra-us`) — `.claude/rules/autonomous-study-bootstrap-safety.md`의 규약과 동일하며 `profiles/setup.sh`가 `id//-/_`로 변환한다. `hermes_profile`에는 **하이픈 프로필 ID**를 적는다.

| actor | hermes_profile | 프로필 존재 (`~/.hermes/profiles/`, T3610) | SOUL | 실행 방식 | status |
|---|---|---|---|---|---|
| `ra_us` | `ra-us` | ✓ | `ra-us-SOUL.md` | Hermes 게이트웨이 세션 (T3610) | active |
| `ra_eu` | `ra-eu` | ✓ | `ra-eu-SOUL.md` | 동일 | active |
| `ra_kr` | `ra-kr` | ✓ | `ra-kr-SOUL.md` | 동일 | active |
| `ra_case` | — | **✗** (setup.sh 생성 목록에 없음) | 없음 | 미정 — 프로필·SOUL이 PR로 추가되기 전까지 `paused` | paused |
| `op_manager` | `op-manager` | ✓ | `op-manager-SOUL.md` | Hermes 세션 (현재 T3610에 생성됨; rpi5 상주 여부 미확인) | active |
| `infra_t3610` | `infra-t3610` | ✓ | `infra-SOUL.md` (공유) | Hermes 세션 | active |
| `infra_gx10` | `infra-gx10` | ✓ | `infra-SOUL.md` (공유) | Hermes 세션 (T3610에 생성됨; gx10 상주 여부 미확인) | active |
| `infra_rpi` | `infra-rpi` | ✓ | `infra-SOUL.md` (공유) | Hermes 세션 (T3610에 생성됨; rpi5 상주 여부 미확인) | active |
| `n8n_manager` | `n8n-manager` | ✓ | `n8n-manager-SOUL.md` | **peer 아님** — 라우터(n8n) 자신 | 미등록 |

- `host`는 **프로필이 실제로 생성·기동되는 호스트**를 적는다. 현재 `profiles/setup.sh`는 8개 프로필을 실행 호스트(T3610)에 모두 만들므로 실측값은 전부 `t3610`이다. 다른 호스트로 옮기려면 그 호스트에서 setup.sh를 실행하고 이 표를 PR로 갱신한다 — registry에 적혀 있다는 이유만으로 실행 가능하다고 보지 않는다.
- registry에 없는 actor를 라우터가 임의로 만들지 않는다(§6 채용 절차).
- P3 파일럿 대상은 이 표에서 `active`이고 프로필이 확인된 RA peer **2개**(`ra_us`, `ra_eu`)로 한정한다(#150 리뷰 P3).

---

## 5. registry/workspaces.json

```json
{
  "version": 1,
  "workspaces": {
    "work":  { "floor": 1, "label": "업무", "seats": 8 },
    "infra": { "floor": 2, "label": "인프라", "seats": 4 }
  },
  "reserved_floors": [3]
}
```

새 workspace = 새 항목 + 새 층. 프랙탈 원칙의 파일 표현.

---

## 6. 빈 좌석 = 부재

`seats`보다 `active` actor 수가 적으면 그 차이가 빈 좌석이다. 살은 빈 좌석에 `absence` 이벤트 카운터를 표기한다. 채용은 `hire_proposal` → 사람 승인 → 이 파일에 PR로 actor 추가 → 라우터가 다음 커밋부터 인식.

---

## 7. Gitea 백업

기존 Gitea 백업 스크립트(2주 주기, DS224+)에 `ra-hive` 저장소를 포함한다. 추가 작업 없음 — 저장소 목록에 1행 추가.
