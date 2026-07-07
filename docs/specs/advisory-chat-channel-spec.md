# SPEC — VO Built-in RA Advisory Channel (Discussion Asset + Implementation Plan)

> **Document type**: Discussion asset and implementation planning SPEC. Not implementation kickoff.
> Unresolved items are explicitly marked DEFERRED so the next session can resume without context loss.
> **Status**: PROPOSED — awaiting human approval of the unidirectional-principle redefinition (Section 7).
> **Date**: 2026-07-07.

---

## 1. Overview / Problem

The Virtual Office (`virtual-office/virtual-office.html`) is currently a fully read-only observer
(CLAUDE.md:212 — "The virtual office reads from this system; this system is unaware of the virtual office";
virtual-office-mvp.md:10 — "관찰자 구조: 살은 뼈대 활동을 읽기만 한다. 운영에 개입하지 않는다").
The user can observe activity history (log + detail panel + heat map) but cannot talk back to the agents.

Today, RA agents (ra_us / ra_eu / ra_kr) communicate with humans only through the machine-to-machine
pipeline: email → n8n → Hermes (CLAUDE.md:60-71, Contract A/B). There is **no channel for a human to
directly ask an RA agent for advisory**.

**User need (verified scope)**: Let the user directly query an RA agent from the VO to:

1. Probe the agent's current knowledge level (capability diagnosis),
2. Discover knowledge-base gaps,
3. Update the KB,
4. Close the agent-growth loop.

This is fundamentally **capability diagnosis + KB quality management**, not a generic chatbot. The
phrase the user used to frame it: **"RA 에이전트의 현재 지식 수준을 사람이 직접 점검 → 지식베이스 gap 발견 → KB 업데이트 → 에이전트 성장 루프를 닫는 도구. 본질적으로 '자문(Q&A)'이 아니라 '에이전트 역량 진단 + KB 품질 관리'."**

---

## 2. Scope (confirmed with user)

| Dimension | In Scope | Out of Scope |
|---|---|---|
| User | Single user (본인 단독, POC) | Multi-user, RBAC |
| Question types | Pure RA knowledge + learning/process questions + agent-domain overall | WP advisory (WP-NNN context) — explicitly EXCLUDED |
| History store | Honcho session (reuse existing `_honcho_record` ra_advisory pattern) | Separate DB, new schema |
| VO surfacing | Auto-display "human_query → ra_advisory" in activity log | New actor; new character |
| Response pattern | Background async + completion notification (request_id based) | Synchronous blocking; SSE streaming |
| Auth | Single-user session token or pre-shared key | OAuth, user accounts |

**Confirmed exclusions**:
- WP-NNN context advisory — OUT OF SCOPE (use the existing raspi5p path for that).
- Real-time streaming (SSE/WebSocket) — OUT OF SCOPE.
- Direct write to `llm-wiki` / `ra-project` / `MD-process` — PERMANENTLY PROHIBITED (CLAUDE.md:176, CLAUDE.md:206-210).

---

## 3. Design Pillars (Core Insights)

### 3.1 Adapter Backend Proxy Pattern

The VO must NOT call `hermes-api-server.py` directly. The Honcho adapter
(`virtual-office/virtual-office-honcho-adapter.js`) extends to act as a **backend proxy** that holds
`API_SERVER_KEY` server-side. From Hermes' point of view the caller is "the adapter", not "the VO".
This preserves CLAUDE.md:212 ("this system is unaware of the virtual office") because Hermes still
only sees an HTTP client with a valid bearer token, identical in shape to raspi5p's existing calls.

### 3.2 Reverse-Exploit the Unidirectional Pipe

The VO already consumes Honcho activity via `/api/events`
(`virtual-office-honcho-adapter.js:311-320`). Because `_honcho_record`
(`scripts/hermes-api-server.py:539-575`) writes each advisory into Honcho with
`record_type=ra_advisory` (line 567), the VO's existing event stream will automatically surface
"human_query → ra_advisory" events once the adapter maps them. **The VO itself remains read-only**;
only the `/api/chat` POST endpoint is whitelisted (single exception), all other write paths stay 405
(`virtual-office-honcho-adapter.js:304-309`).

### 3.3 GATE and Philosophy Compliance

- Agents **return advisory only**; never execute, never change WP state.
- "Close / Reopen WP" stays **Human only — permanently** (CLAUDE.md:173).
- "Write to llm-wiki / ra-project / MD-process repos" stays **Prohibited permanently** (CLAUDE.md:176).
- `ra-kr-SOUL.md` (and US/EU equivalents) — "never close or reopen WP" invariants remain untouched.
- KB writes flow only through the existing pgvector `ra_knowledge` path (CLAUDE.md:209-210).
- Every response MUST carry the explicit disclaimer "advisory only, human decides" (Risks Section 11).

---

## 4. Requirements (EARS format)

> Each requirement follows EARS grammar. IDs are stable across sessions.

### REQ-AC-001 (Query-only advisory, no WP context)
**WHEN** a request to `/v1/ra/advisory` contains `query` and omits `wp_context`,
**THE SYSTEM SHALL** accept it and return an RA agent advisory without raising a validation error.

- Evidence of feasibility: `scripts/hermes-api-server.py:749-753` — `query` is the only validated
  required field; `wp_context = data.get("wp_context") or {}` (line 752) defaults to empty dict.
- `build_advisory_context` at `scripts/hermes-api-server.py:441-447` already handles empty wp_context
  via `wp = wp_context or {}`; WP sections are skipped when `wp_list` is empty.

### REQ-AC-002 (Two advisory modes — mode b DEFERRED)
**THE SYSTEM SHALL** support two advisory modes: (a) knowledge query mode and (b) learning
retrospective mode ("최근 뭘 학습했어?").

- Mode (a) — FEASIBLE today via REQ-AC-001.
- Mode (b) — **DEFERRED**: see TECH VERIFICATION Section 8. Requires new code path to read prior
  Honcho messages for the routed peer and inject them as a context section in `build_advisory_context`.
- Until (b) is implemented, the UI MUST mark retrospective questions as "not yet supported".

### REQ-AC-003 (Adapter backend proxy)
**THE SYSTEM SHALL** proxy chat POST requests from the VO through the Honcho adapter to
`/v1/ra/advisory`, with `API_SERVER_KEY` held server-side only and never exposed to the browser.

- The browser-visible endpoint is `/api/chat` (extension to `virtual-office-honcho-adapter.js`).
- The adapter forwards to `${HERMES_API_URL}/v1/ra/advisory` with `Authorization: Bearer ${API_SERVER_KEY}`.
- The browser never sees `API_SERVER_KEY`. This is the load-bearing invariant of the whole design.

### REQ-AC-004 (Async + completion notification)
**WHEN** the user submits a chat query, **THE SYSTEM SHALL**:
1. Return a `request_id` immediately (HTTP 202 Accepted),
2. Process the advisory in the background (Hermes CLI subprocess, ≤180s timeout),
3. Notify the VO on completion via polling `/api/chat/status/<request_id>` or surfacing through
   the existing `/api/events` stream as an `advisory_returned` event.

- Reuse `request_ref = f"adv-{int(time.time())}"` pattern (`scripts/hermes-api-server.py:756`).
- The current endpoint is synchronous (`scripts/hermes-api-server.py:736-786` blocks on
  `_invoke_hermes`). Async is NEW work — see REQ-AC-009.

### REQ-AC-005 (Honcho recording — automatic VO surfacing)
**THE SYSTEM SHALL** record each human-initiated advisory to Honcho with `record_type=ra_advisory`,
reusing `_honcho_record` (`scripts/hermes-api-server.py:539-575`) so the VO activity log surfaces it
automatically via `/api/events`.

- The existing `_honcho_record("ra_advisory", ...)` call at `scripts/hermes-api-server.py:784`
  already does this. We must distinguish human-initiated advisories from raspi5p advisories by
  adding a `source: "human_chat"` field to `_adv_meta` (`scripts/hermes-api-server.py:525-536`).
- The adapter event mapping then emits a `human_query` event before the `advisory_returned`.

### REQ-AC-006 (Single-user authentication)
**THE SYSTEM SHALL** authenticate the single authorized user via a session token or pre-shared key
loaded from `.env`. Multi-user RBAC is OUT OF SCOPE.

- The browser stores the token in `sessionStorage` after a one-time login.
- The adapter validates the session before forwarding to `/v1/ra/advisory`.
- Failure mode: 401 with "auth required" — no advisory is sent.

### REQ-AC-007 (VO container stays read-only)
**THE VO CONTAINER SHALL** remain `read_only: true` in `docker-compose.yml`. Only the `/api/chat`
POST endpoint is whitelisted inside the adapter; all other non-GET methods continue to return 405
(`virtual-office-honcho-adapter.js:304-309`).

- Implementation: extend the `if (req.method !== 'GET')` block at line 305 with an exception for
  `req.method === 'POST' && parsedUrl.pathname === '/api/chat'`.

### REQ-AC-008 (Region hint passthrough)
**WHEN** the user selects a region (US / EU / KR / Auto) in the chat UI, **THE SYSTEM SHALL** pass
it as `region_hint` to `/v1/ra/advisory` (`scripts/hermes-api-server.py:753`).

- "Auto" → omit `region_hint`; server-side keyword routing decides
  (`scripts/hermes-api-server.py:355-377`).
- Multi-region / unclear → Yellow (`scripts/hermes-api-server.py:495-522`) — surfaced as a
  "needs human review" banner in the UI.

### REQ-AC-009 (Async status endpoint — NEW)
**THE SYSTEM SHALL** expose a status lookup so the browser can poll completion:

```
GET /api/chat/status/<request_id> → { state: "pending"|"completed"|"failed", advisory: {...}|null }
```

- Backed by either an in-process Map (simplest POC) or by querying Honcho messages by `request_ref`
  in metadata (`_adv_meta` at `scripts/hermes-api-server.py:525-536` already includes `request_ref`).
- Honcho-backed is preferred because it survives adapter restart.

### REQ-AC-010 (Advisory-only disclaimer)
**EACH** advisory rendered in the VO chat panel **SHALL** display the literal text
"advisory only, human decides" below the response.

- Static UI text, not agent-generated.
- Rationale: CLAUDE.md:20 ("에이전트는 사람 RA 전문가를 보조한다. 대체하지 않는다") and Risks Section 11.

### REQ-AC-011 (No side effects)
**THE SYSTEM SHALL NOT** perform any of the following as part of a chat advisory:
- Write to OpenProject,
- Write to `llm-wiki` / `ra-project` / `MD-process` repos,
- Modify WP state,
- Trigger n8n workflows.

- Enforcement: the chat path reuses `/v1/ra/advisory` which already has no write paths
  (`scripts/hermes-api-server.py:736-786` performs only `_invoke_hermes` + `_honcho_record`).

### REQ-AC-012 (Logging for diagnosis)
**THE SYSTEM SHALL** log each chat advisory input and outcome via the existing
`_log_adv_request` (`scripts/hermes-api-server.py:77-96`) so diagnosis is immediate.

- No new log file. Reuse `ADV_REQUEST_LOG` (line 65).
- Add `source: "human_chat"` to the logged JSON for filtering.

---

## 5. Architecture

### 5.1 Component flow (ASCII)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ BROWSER (VO, single user)                                                   │
│  ┌────────────────────────────┐                                             │
│  │  Chat panel (TBD layout)   │  type: "510(k) predicate device analysis"   │
│  │  + region selector (Auto)  │  + sessionStorage.token                     │
│  └─────────────┬──────────────┘                                             │
└────────────────┼────────────────────────────────────────────────────────────┘
                 │ POST /api/chat  { query, region_hint, token }
                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ADAPTER (virtual-office-honcho-adapter.js)  — Docker container, port 3001   │
│   • validates session token                                                 │
│   • injects Authorization: Bearer ${API_SERVER_KEY}   (server-side only)    │
│   • generates request_id (adv-<ts>-chat-<rand>)                             │
│   • returns 202 immediately                                                 │
│   • background task →                                                       │
└────────────────┼────────────────────────────────────────────────────────────┘
                 │ POST /v1/ra/advisory  { query, region_hint, source: "human_chat" }
                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ HERMES API SERVER (scripts/hermes-api-server.py, T3610:8643)                │
│   • route_advisory_region (line 355)  → actor                               │
│   • build_advisory_context (line 431)  — query-only OK (REQ-AC-001)         │
│   • _invoke_hermes (line 473)  → Hermes CLI subprocess (≤180s)              │
│   • parse_advisory + validate_advisory (line 402, 410)                      │
│   • _honcho_record("ra_advisory", ...)  (line 784)  → Honcho session        │
│   • _log_adv_request  (line 785)  → ADV_REQUEST_LOG                         │
│   • returns advisory JSON + request_ref                                     │
└────────────────┬────────────────────────────────────────────────────────────┘
                 │ (Hermes is unaware the query originated in the VO — it sees only
                 │  an HTTP client with a bearer token, identical to raspi5p.)
                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ HONCHO (T3610:8000)                                                         │
│   • session "ra-advisory"  ← new message with metadata.source="human_chat"  │
│   • existing /v3/workspaces/work/sessions/... messages API                  │
└────────────────┬────────────────────────────────────────────────────────────┘
                 │ Honcho's existing message stream (already consumed by adapter)
                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ADAPTER  /api/events  (existing endpoint)                                   │
│   • maps ra_advisory w/ source=human_chat → "human_query" event             │
│   • maps the same ra_advisory (final) → "advisory_returned" event           │
│   • existing dedupe + display pipeline unchanged                            │
└────────────────┬────────────────────────────────────────────────────────────┘
                 │ SSE-like polling (existing, 30s default)
                 ▼
   BROWSER renders: human_query → advisory_returned  in the activity log
                    AND in the chat panel (completion notification)
```

### 5.2 Why Hermes "remains unaware" of the VO

The `/v1/ra/advisory` endpoint (`scripts/hermes-api-server.py:736-786`) only inspects:
- `Authorization` header (line 745 — `check_auth()`) — identical for raspi5p and the adapter,
- JSON body fields `query`, `wp_context`, `region_hint` (lines 749-753).

It does not inspect the caller's identity beyond the bearer token. Therefore, if the adapter
presents the same `API_SERVER_KEY`, the call is — by construction — indistinguishable from a
raspi5p call. This is the load-bearing property that lets us keep CLAUDE.md:212 intact.

---

## 6. UI Placement (DEFERRED — decided at implementation time)

Two candidates remain on the table. Both are compatible with the backend proxy pattern. The
decision is deferred to the implementation session because it depends on user workflow preference,
not technical constraint.

### 6.1 Current VO layout (verified, file:line evidence)

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                          virtual-office.html                                         │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────┐  ┌──────────────────┐   │
│  │  STAGE  (760 x 440)              virtual-office.html:40  │  │  VIZ-PANEL       │   │
│  │  ┌──────────────────────────┐                            │  │  (300 x 440)     │   │
│  │  │  WORK OFFICE  (62%)      │   ← work room              │  │  Heat Map        │   │
│  │  │  kanban (line 256)       │                            │  │  (line 271-316)  │   │
│  │  │  ra_us ra_eu ra_kr       │                            │  │                  │   │
│  │  └──────────────────────────┘                            │  │  Confidence      │   │
│  │  ┌──────────────┐                                        │  │  legend          │   │
│  │  │ INFRA (38%)  │   ← infra room                         │  │                  │   │
│  │  │ t3610 gx10   │                                        │  │                  │   │
│  │  │ rpi          │                                        │  │                  │   │
│  │  └──────────────┘                                        │  │                  │   │
│  └─────────────────────────────────────────────────────────┘  └──────────────────┘   │
│                                                                                      │
│  ┌────────────────────────────────────────────────────────────────────────────────┐  │
│  │  LOG  (1068 x 220)            virtual-office.html:319, height line 142         │  │
│  └────────────────────────────────────────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────────────────────────────────────────┐  │
│  │  DETAIL-PANEL    (1068 x ≤440)  virtual-office.html:320, max-height line 152   │  │
│  └────────────────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────────────┘

main-container:  virtual-office.html:169  (display:flex; gap:8px; align-items:flex-start;)
```

### 6.2 Candidate A — Side column (3-column main-container)

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  ┌────────────────────┐ ┌──────────────┐ ┌──────────────────┐                       │
│  │  STAGE  (760x440)  │ │ VIZ-PANEL    │ │  CHAT-PANEL      │  <- NEW                │
│  │                    │ │ (300x440)    │ │  (300x440)       │                        │
│  │  (unchanged)       │ │ (unchanged)  │ │  history + input │                        │
│  └────────────────────┘ └──────────────┘ └──────────────────┘                       │
│  ┌───────────────────────────────────────────────────────────────────┐              │
│  │  LOG / DETAIL-PANEL (unchanged width, may need wrapping)          │              │
│  └───────────────────────────────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

**Pros**: chat visible alongside the activity stage; user watches the agent react in real time
when its own advisory appears in the log.
**Cons**: 1068px log width no longer fits above the three columns (760+300+300 = 1360px); forces
either horizontal scroll or log width reduction. Heat map and chat compete for attention.

### 6.3 Candidate B — Bottom panel (vertical expansion under detail-panel)

```
┌─────────────────────────────────────────────────────────────────────┐
│  ┌────────────────────────────┐  ┌──────────────────┐               │
│  │  STAGE  (760x440)          │  │  VIZ-PANEL       │               │
│  └────────────────────────────┘  └──────────────────┘               │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  LOG (220px, unchanged)                                       │ │
│  └───────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  DETAIL-PANEL  (collapsed when chat active)                    │ │
│  └───────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  CHAT-PANEL  (1068 x ~220)  <- NEW                             │ │
│  │  history scroll + input + region selector + advisory-only note │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

**Pros**: preserves existing 2-column main-container exactly (virtual-office.html:169); log width
stays 1068px; chat reads as a natural extension of the existing observation flow.
**Cons**: total page height grows; user must scroll to see chat if the viewport is short.

### 6.4 Decision

**DEFERRED.** The backend proxy pattern is identical either way. Decide at implementation time
after a quick user workflow observation.

---

## 7. Design Principle Redefinition (PROPOSED WORDING — human approval required)

The agent MUST NOT rewrite these documents unilaterally. The following is a proposed wording for
human review and approval. Once approved, the agent may apply the edits.

### 7.1 CLAUDE.md:212 (current)

> "The virtual office reads from this system; this system is unaware of the virtual office."

### 7.2 PROPOSED wording

> "The virtual office reads from this system. The RA agents remain unaware of the virtual office:
> human chat input flows through the Honcho adapter as a backend proxy, presenting the same
> `Authorization: Bearer <API_SERVER_KEY>` shape as any other `/v1/ra/advisory` client. Agents
> see an HTTP client, not a VO. The VO container stays read-only; only `/api/chat` POST is
> whitelisted as the chat input exception."

### 7.3 master-design.md:154 (current)

> "뼈대는 시각화 존재를 모르고 운영 기록만 남김(단방향)."

### 7.4 PROPOSED wording

> "뼈대는 시각화 존재를 모른다(단방향 유지). 단, 사용자 직접 자문은 예외적으로 허용된
> 단일 채널(VO `/api/chat` → 어댑터 백엔드 프록시 → `/v1/ra/advisory`)을 경유하며, 이
> 경로는 뼈대 입장에서 일반 HTTP 클라이언트와 동일하다. 뼈대는 여전히 시각화를 의식하지
> 않고 운영 기록만 남긴다."

### 7.5 virtual-office-mvp.md:10 (current)

> "관찰자 구조: 살은 뼈대 활동을 읽기만 한다. 운영에 개입하지 않는다."

### 7.6 PROPOSED wording

> "관찰자 구조 원칙 유지: 살은 뼈대 활동을 읽기만 한다. 단, 사용자가 뼈대 RA 에이전트에
> 직접 자문을 요청하는 단일 입력 채널(`/api/chat`)은 예외적으로 허용된다. 이 채널은
> 어댑터 백엔드 프록시를 경유하여 뼈대의 단방향 원칙(Hermes는 호출자가 VO임을 모름)을
> 훼손하지 않는다. 실행·WP 상태 변경은 기존 게이트룰(CLAUDE.md:167-178)이 그대로 적용된다."

---

## 8. TECH VERIFICATION NEEDED (results from reading the code)

### 8.1 TV-1: Query-only (no `wp_context`) feasibility — ✅ FEASIBLE

Verified by reading `scripts/hermes-api-server.py`:

| Evidence | File:line | Result |
|---|---|---|
| `query` is the only required field | `scripts/hermes-api-server.py:749-751` | 400 only if `query` missing or >8000 chars |
| `wp_context` defaults to empty dict | `scripts/hermes-api-server.py:752` | `wp_context = data.get("wp_context") or {}` |
| `region_hint` is optional | `scripts/hermes-api-server.py:753` | `str(data.get("region_hint") or "").strip() or None` |
| `build_advisory_context` handles empty wp_context | `scripts/hermes-api-server.py:441-447` | `wp = wp_context or {}`; WP sections added only if non-empty |
| `docs/ra-advisory-api.md` request schema | `docs/ra-advisory-api.md:20-23` | `wp_context` is documented optional |

**Conclusion**: REQ-AC-001 is implementable today with zero server changes. The VO chat path
simply omits `wp_context`.

### 8.2 TV-2: Learning retrospective mode — ❌ NOT FEASIBLE today (DEFERRED)

Verified by reading `scripts/hermes-api-server.py`:

| Evidence | File:line | Result |
|---|---|---|
| Hermes invocation | `scripts/hermes-api-server.py:476-478` | `[HERMES_BIN, "-p", profile, "-z", context, "--skills", "ra-expert"]` — fresh `-z` context, no memory recall |
| `_invoke_hermes` signature | `scripts/hermes-api-server.py:473-492` | takes `(profile, context, timeout)`, no Honcho input |
| `_honcho_record` is write-only | `scripts/hermes-api-server.py:539-575` | only POSTs messages; never reads |
| Honcho used elsewhere as input? | (grep) | no — Honcho is purely an output sink in this server |

**Conclusion**: The current `/v1/ra/advisory` path is **stateless**. The Hermes CLI is invoked
with `-z context` (line 477), where `context` is built fresh from `query + RAG + Layer4 wiki`
(`build_advisory_context` line 431-470). Honcho is used only to record the result.

To support "최근 뭘 학습했어?" the system needs **NEW code** that:
1. Reads recent Honcho messages for the routed peer from session `ra-advisory` (or a dedicated
   `study_insight` / `daily_growth_case` session),
2. Adds them as a new context section (e.g., `## 최근 학습 이력 (본인)`) inside
   `build_advisory_context`,
3. Probably needs a different output template — retrospective responses are not advisories.

This is non-trivial. **REQ-AC-002 mode (b) is DEFERRED.** Mode (a) ships first.

### 8.3 TV-3: Async request_id pattern — ⚠️ PARTIALLY FEASIBLE (NEW code needed)

| Evidence | File:line | Result |
|---|---|---|
| `request_ref` generation | `scripts/hermes-api-server.py:756` | `f"adv-{int(time.time())}"` — collision risk if two requests arrive in the same second; consider `adv-{ts}-{rand}` |
| `request_ref` as Honcho correlation key | `scripts/hermes-api-server.py:525-536, 784` | `_adv_meta` includes `request_ref`; `/v1/ra/advisory/feedback` (line 789-830) uses it |
| Current endpoint is synchronous | `scripts/hermes-api-server.py:736-786` | Flask route blocks on `_invoke_hermes` with `ADVISORY_TIMEOUT=180` (line 342, 771) |

**Conclusion**: `request_ref` exists for correlation, but the endpoint is blocking. To deliver
REQ-AC-004 (true async), one of:

- **Option 1 (preferred for POC)**: Adapter holds a request_id → Promise map in-process. Browser
  polls `/api/chat/status/<id>`. Adapter does the blocking call to `/v1/ra/advisory` in a worker.
  No hermes-api-server change needed.
- **Option 2 (cleaner)**: Add `/v1/ra/advisory/async` to hermes-api-server returning 202 + a job
  token; add `/v1/ra/advisory/status/<token>`. More moving parts.

**Recommendation**: Option 1 for POC (single-user, in-process map is fine). Document Option 2 as
future work.

---

## 9. Out of Scope

- WP-NNN context advisory (use existing raspi5p path).
- Multi-user / RBAC / OAuth.
- External expert invitation.
- Real-time SSE streaming.
- Direct write to `llm-wiki` / `ra-project` / `MD-process` (permanently prohibited,
  CLAUDE.md:176).
- Closing / reopening WPs from chat (permanently human-only, CLAUDE.md:173).
- Voice input.
- Cross-agent multi-turn dialogue (single turn per request in POC).
- REQ-AC-002 mode (b) — learning retrospective — until TV-2 is resolved with new code.

---

## 10. Acceptance Criteria (Definition of Done)

| # | Criterion | Verification |
|---|---|---|
| AC-1 | Single user can submit a query-only advisory from VO chat panel | Manual test in browser; check adapter log shows POST /api/chat |
| AC-2 | Advisory returns within 180s; status polling shows pending→completed | Browser DevTools network tab; /api/chat/status/<id> |
| AC-3 | Advisory appears in VO activity log as `human_query → advisory_returned` | Visual check; `record_type=ra_advisory` + `source=human_chat` in Honcho |
| AC-4 | Hermes server logs show no awareness of VO (no caller-id field) | `grep` hermes-api-server logs — only Authorization + JSON body |
| AC-5 | `API_SERVER_KEY` never appears in browser | Browser DevTools → Network → Headers inspection |
| AC-6 | All non-`/api/chat` POST/PUT/DELETE still return 405 | `curl -X POST /api/anything-else` → 405 |
| AC-7 | No side effects (no OP write, no repo write, no n8n trigger) | Code review + monitoring of OP + n8n |
| AC-8 | "advisory only, human decides" disclaimer rendered below each response | Visual check |
| AC-9 | Multi-region / unclear queries surface as Yellow banner | Send ambiguous query, expect `decision=yellow_review` |
| AC-10 | CLAUDE.md:212, master-design.md:154, mvp.md:10 updated per Section 7 (after human approval) | `git diff` on docs |
| AC-11 | GATE-rule violations: 0 | Code review; no close/reopen path in chat flow |
| AC-12 | REQ-AC-002 mode (b) marked DEFERRED in UI (greyed-out "learning retrospective" button with tooltip) | Visual check |

---

## 11. Risks & Considerations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Unidirectional principle redefinition rejected by user | Medium | High | Section 7 is PROPOSED only; no edit until human approval. Implementation can proceed in parallel because backend proxy preserves the property regardless of wording. |
| Hermes subprocess 120s/180s timeout | High | Medium | REQ-AC-004 async pattern is mandatory; browser never blocks. Show "thinking…" indicator with timeout. |
| `API_SERVER_KEY` leak to browser | Low | Critical | Adapter backend proxy is the only path. Code review checklist item. Add a test that greps browser-served HTML/JS for the key. |
| VO container `read_only: true` conflict with `/api/chat` POST | Medium | Medium | Whitelist only `/api/chat` in adapter; container stays read-only at the docker level (no filesystem writes; POST is in-memory + outbound HTTP). |
| User over-trusts agent advisory as final decision | Medium | High | REQ-AC-010 disclaimer on every response. CLAUDE.md:20 design philosophy reaffirmed. |
| Collision of `request_ref` (same-second requests) | Low | Low | Use `adv-{ts}-{rand}` in the new chat path; document collision risk in hermes-api-server for future fix. |
| Honcho downtime hides chat history | Medium | Medium | Adapter falls back to ADV_REQUEST_LOG tail (already exists, `scripts/hermes-api-server.py:65`). |
| Yellow-flood (every vague question becomes Yellow) | Medium | Medium | UI explains Yellow = "agent is uncertain, please refine or escalate". Not a defect — CLAUDE.md:21 ("불확실하면 반드시 사람에게 올린다"). |
| Scope creep toward general chatbot | Medium | Medium | Section 9 exclusions enforced; "capability diagnosis + KB quality" framing kept front-of-mind. |

---

## 12. Open Decisions (handoff to next session)

| ID | Decision | Owner | Status |
|---|---|---|---|
| OD-1 | UI placement: Candidate A (side) vs Candidate B (bottom) — Section 6 | User | RESOLVED 2026-07-07 → **Candidate B (bottom)** |
| OD-2 | Auth implementation: sessionStorage token vs HTTP basic auth vs mutual TLS | User | RESOLVED 2026-07-07 → **sessionStorage token** (single-user POC) |
| OD-3 | Notification form: character speech bubble vs badge vs toast | User | DEFERRED |
| OD-4 | Learning retrospective mode (REQ-AC-002b): ship as Phase 2 or cut from this SPEC? | User | DEFERRED — depends on TV-2 new-code appetite |
| OD-5 | Async option: Option 1 (adapter in-process map) vs Option 2 (server-side /async) | User | RESOLVED 2026-07-07 → **Option 1** (adapter in-process map; no Hermes server change) |
| OD-6 | Apply Section 7 wording edits to CLAUDE.md / master-design.md / mvp.md? | User | APPROVED 2026-07-07 — minimal-add wording (one-directional principle preserved; adapter, not VO, is the API caller) |
| OD-7 | New Honcho session name for human chat (e.g., `ra-advisory-human-chat`) or reuse `ra-advisory`? | User | DEFERRED (recommend reuse + `source` metadata) |
| OD-8 | Should human-chat advisories feed the agent learning loop (3-point evaluation)? | User | DEFERRED — out of scope for this SPEC but flagged for ecosystem alignment |

---

## Phase 1 Implementation Log (2026-07-07)

**Commit**: `115cac6` (feat #104). **Issue**: #104.

### Implemented
- `virtual-office-honcho-adapter.js`: `/api/chat` POST whitelist (other writes still 405), `API_SERVER_KEY` held server-side, OD-2 sessionStorage token auth, OD-5 Option 1 in-process map + `/api/chat/{id}` polling.
- `virtual-office.html`: bottom chat panel (OD-1 Candidate B) + token input + polling UI.
- `docker-compose.yml`: `HERMES_API_URL`/`API_SERVER_KEY`/`CHAT_AUTH_TOKEN` env. `.env.example` documents keys (`.env` gitignored).

### Live e2e verification (T3610)
| Check | Result |
|---|---|
| No-token POST → 401 | ✅ PASS |
| Valid-token POST → 202 + request_id | ✅ PASS |
| POST to other path → 405 (read-only preserved) | ✅ PASS |
| One-directional (no VO identifier to Hermes) | ✅ PASS |
| Advisory response returned | ⚠️ **FAIL** — 180s timeout, `socket hang up` |

### ⚠️ TV-1 REVERSED by live test (2026-07-07)
- TV-1 (code-only) said query-only advisory FEASIBLE. **Live test reverses this.**
- `/v1/ra/advisory` handler code DOES accept empty `wp_context` (`hermes-api-server.py:752`), but the `_invoke_hermes` subprocess (Hermes CLI) does NOT return within `ADVISORY_TIMEOUT=180s` for the test query ("한국 MFDS 의료기기 1등급 기준은?", region_hint=KR).
- raspi5p's hourly advisories (192.168.100.50) return `200` normally → Hermes itself works; the stall is **query-specific** (ra_kr routing + knowledge query, not wp_context emptiness).
- **REQ-AC-001 still valid at the contract level** (server accepts query-only); the gap is Hermes CLI response time for knowledge-type queries, which is OUT OF PHASE-1 SCOPE (adapter is correct).

### Diagnostic result (2026-07-07) → 분리 이슈 #105

bisect 완료. **Phase 1 어댑터는 정상**, 지연 근원 = `_invoke_hermes`.

| Path | Result |
|---|---|
| Adapter (401/202/405/one-directional) | ✅ PASS |
| Yellow (unclear region) "hello" | ✅ 0.18s (Hermes CLI not invoked) |
| `/v1/knowledge/fetch` (Layer 4 RAG) | ✅ 9s normal |
| **`_invoke_hermes` (Hermes CLI → GX10), US/KR knowledge query** | ❌ 300s timeout |

- raspi5p (192.168.100.50) hourly advisories return `200` normally → query-specific stall.
- "순수 지식 자문" 회신은 **#105** (Hermes CLI/GX10 runtime, Phase 1 scope 밖).
- Phase 1 adapter 코드: **DoD 달성**. VO에서 unclear/yellow 자문은 즉시 응답(0.18s).
- #104: #105 해결 후 close.

### Improvement A applied (2026-07-07, commit `7a50792`) — **TV-2 REVERSED**

**회고 query는 FEASIBLE** (TV-2의 NOT FEASIBLE 판정 정정). 근거:

- 단일 region_hint 강제 라우팅 시 ra_kr/ra_eu/ra_us 모두 107-171s 내 정상 회고 응답 (confidence 0.85-0.98).
- 다중 actor 회고 query("각 에이전트...")는 자동 분할 라우팅(개선안 A)로 처리 — 어댑터가 `isMultiAgentRetrospective(query)` 감지 시 KR/EU/US 3개 병렬 POST, parent request_id로 취합.
- 라이브 검증: 사용자 원래 query → 3개 답(ra_kr 0.85, ra_eu 0.96, ra_us 0.95) parent completed로 취합.

**#105 범위 축소**: 회고 query는 정상 동작하므로 #105는 **"구체적 지식 query"(예: "한국 MFDS 1등급 기준은?")의 Hermes CLI 지연**으로 한정. 회고 query는 #104 Phase 1에서 처리 완료.

**남은 개선안 (후속)**: B(회고 전용 decision `information_reply` + recommended_comment 의무화), C(evidence 포맷 정규화 — 현재 NAS/GitHub/상대경로 혼재), D(응답 시간 100-171s 개선 — warming/caching/SSE).

### Deep analysis (2026-07-07) — retrospective depth & KB necessity (사용자 딥싱크)

**관찰**: 회고 query는 응답(200)하지만, 세 agent의 답이 "학습 회고"가 아니라 **SOUL.md 정형 역할 + RAG 지식의 재진술**.
- 세 agent 답 ≈ SOUL.md Identity 줄 + 제품 분류표의 문장화. 시나리오 테스트 답과 실제 창 답이 **패턴 동일** (같은 SOUL.md + 같은 RAG 소스).
- 사용자 query의 핵심 "현재 어느 정도 지식을 축적했는지"에 대한 답 **없음** — 에이전트가 Honcho 학습 이력(growth_cases/성숙도/최근 학습 주제/부족 영역)을 **읽지 않음**.
- confidence 0.85-0.98은 "역할 정의 확신"이지 "학습 수준 정확 파악"이 아님.

**정정**: 앞선 "TV-2 REVERSED"는 **좁은 의미(응답 여부)**에서만 맞음. **질적 의미(진짜 학습 회고)**에서는 **여전히 NOT FEASIBLE**. 정확한 표현: *"회고 query는 응답은 하나, 학습 이력 반영 회고는 아직 안 된다."*

**"KB 없이 자율 성장?" 분석**: 의료기기 RA에서 완전 자율(크롤링→자체 저장)은 위험 — KB는 여전히 필요.
1. **신뢰성/출처 검증** — 틀리면 환자 안전·규제 위반. 사람 큐레이션·검토 출처 필수.
2. **사내 지식은 크롤링 불가** — H&abyz 제품 분류/내부 SOP는 웹에 없음. KB(pgvector)로만 접근.
3. **품질 관리** — 자율 KB 갱신은 오류 누적 위험 (`.moai/config` evolution safety 5층이 이것을 막음).
4. **법적/윤리** — 공식 사이트 문서도 자동 수집·재구성·재배포는 ToS·저작권 회색지대.
5. **설계 철학** — ECOSYSTEM 원칙 3("연결은 사람"), 8("정확성=판단 품질"), "에이전트는 보조, 대체하지 않는다". KB 업데이트는 사람 판단 영역.

→ "자율 성장"의 **안전한 형태** = 자율 탐지 + 사람 승인 업데이트 (KB 폐지 아님, KB + 인간 루프 강화).

**진짜 RA 전문 agent를 위한 4가지 (우선순위)**:
- **(a) Honcho 학습 이력 주입** (REQ-AC-002b 본격 구현) — `hermes-api-server.py` `build_advisory_context`에 에이전트 Honcho 학습 데이터(growth_cases/성숙도/최근 학습 주제/어려운 케이스) 주입. 회고/자문에서 과거 학습 반영.
- **(b) #105 해결** — 구체적 지식 query Hermes CLI 지연 진단. `_invoke_hermes` bisect: GX10 추론 시간 vs RAG 컨텍스트 과적 vs Hermes CLI 자체 루프.
- (c) **KB 갭 탐지 루프** — 자문 답이 KB에 없으면 "이 주제 KB 보완 필요" 자동 표시 → 사람이 KB 업데이트. (사용자 본래 목적 "부족한 부분을 사용자가 개선" 루프의 핵심.)
- (d) (선택) **최신 규제 모니터링** — agent가 공식 사이트 변화 탐지 → 사람 승인 시만 KB 업데이트 (완전 자율 아님).

**다음 세션 우선순위**: **(a) + (b)**. 이 둘이 "진짜 RA 전문 agent"를 가로막은 두 기둥. (c)는 (a) 이후 자연스럽게, (d)는 별도 검토.

### Implementation (2026-07-07) — (a) + (b) 완료

**(a) Honcho 학습 이력 주입 — 구현 완료 (REQ-AC-002b)**
- `hermes-api-server.py`: `_honcho_post_json()` + `_fetch_learning_history(actor)` 추가. date 기반 직접 probe(`growth-{actor}-daily-{date}` 세션)로 최근 7일 `daily_growth_case` 에서 "Primary focus" + 출처를 추출해 compact 컨텍스트를 생성 (fail-safe, ~50-75ms).
- `build_advisory_context(..., learning_history=None)` 시그니처 추가, evidence(RAG/Layer4)와 출력 지시 사이에 "## 담당자 최근 학습 이력 (Honcho)" 섹션 주입. "학습 이력 자체는 evidence가 아님" 명시 (정확성 우선 철학 준수).
- 라이브 검증: ra_us/eu/kr 각 7개 학습 주제 추출(55-74ms). hyphen actor → `""` (peer-id 안전). pytest 32 passed.

**(b) #105 해결 — 근본 원인 규명 + fix (검증 완료)**
- **근본 원인**: `ra-expert` 스킬이 "Search NAS Qdrant RAG"를 지시 → 지식 query에서 다중턴 RAG tool/thinking 루프. `gpt-oss:120b`(~49s/turn, thinking 포함) × N턴 × `max_turns:150` → 300s+ 행, stdout 0 bytes. "hello"가 0.18s인 이유: 서버가 Hermes 호출 **전** Yellow 라우팅.
- **bisect 증거** (동일 query/동일 evidence context):
  - `--skills ra-expert` → 120s timeout, **0 bytes** (행).
  - `--skills` 제거 → **75s, 유효 JSON 답** (conf 0.93, evidence 인용).
  - 직접 GX10 `/api/chat`: 48.8s 정상 (GX10 자체는 정상, 원인은 Hermes 오케스트레이션).
- **fix**: `_invoke_hermes(..., skills="ra-expert")` 파라미터화. advisory는 `ADVISORY_SKILLS=""`(기본값, 스킬 제거)로 호출 — 서버가 이미 RAG evidence를 주입하므로 스킬의 tool 호출은 중복. 이메일 triage(`chat_completions`)는 default `ra-expert` 유지(미변경). `ADVISORY_SKILLS=ra-expert` env로 환원 가능.
- **통합 라이브 e2e** (실제 코드 경로): learning_history 주입 + `skills=""` → **129.6s, 유효 advisory JSON** (이전 300s+/0 bytes). #105 해결 확정.

**배포 상태**: fix는 repo `scripts/hermes-api-server.py`에만 반영. 실운영 서버 `/opt/hermes-ra/hermes-api-server.py`(systemd `hermes-api-server.service`)는 이전 코드 → (a)+(b) 라이브 반영을 위해 복사 + 재기동 필요 (사용자 승인 대기).

---

## Next Session Entrypoint

The next session can resume immediately by running through this checklist. Do not start coding
until each item is resolved.

### Resume checklist

1. **Read this SPEC in full** (`docs/specs/advisory-chat-channel-spec.md`).
2. **Verify TECH VERIFICATION findings are still current**:
   - Re-grep `scripts/hermes-api-server.py:749-753` for `wp_context` optionality.
   - Re-grep `scripts/hermes-api-server.py:476-478` for `-z` invocation (stateless).
   - Re-grep `scripts/hermes-api-server.py:539-575` for `_honcho_record` write-only behavior.
   - Re-grep `virtual-office-honcho-adapter.js:304-309` for the 405 block.
3. ~~Resolve OD-6~~ — **RESOLVED 2026-07-07 (APPROVED)**. Apply Section 7 minimal-add wording to
   CLAUDE.md:212, master-design.md:154/170, mvp.md:10 (one-directional principle preserved).
4. ~~Resolve OD-1/OD-2/OD-5~~ — **ALL RESOLVED 2026-07-07**. OD-1 = bottom, OD-2 = sessionStorage
   token, OD-5 = Option 1 (adapter in-process map + polling). **Ready for Phase 1.**
5. **Create a GitHub issue** referencing this SPEC before any code change
   (per CLAUDE.md:143-151 Issue History Protocol).
6. **Update `memory/next-session-entrypoint.md`** after each work session (per Session Handoff
   Protocol, CLAUDE.md:154-163).

### Suggested implementation order (once decisions are made)

- **Phase 0** (no code): Apply Section 7 doc edits — OD-6 APPROVED, OD-1 = bottom. Use minimal-add
  wording (one-directional principle preserved; adapter, not VO, is the API caller).
- **Phase 1**: Backend proxy + `/api/chat` POST whitelist (REQ-AC-003, REQ-AC-007). OD-2 = sessionStorage
  token, OD-5 = Option 1 (adapter in-process map + `/api/chat/{request_id}` polling).
- **Phase 2**: Single-user auth (REQ-AC-006).
- **Phase 3**: Async request_id + status endpoint (REQ-AC-004, REQ-AC-009).
- **Phase 4**: Chat UI (placement = **Candidate B bottom**, OD-1 resolved) + disclaimer (REQ-AC-010).
- **Phase 5**: VO event mapping for `human_query → advisory_returned` (REQ-AC-005).
- **Phase 6**: Logging + diagnosis (REQ-AC-012).
- **Phase 7 (DEFERRED)**: Learning retrospective mode (REQ-AC-002b) — only if OD-4 approved.

### Files this SPEC touches (predicted)

| File | Change type |
|---|---|
| `virtual-office/virtual-office-honcho-adapter.js` | Extend with `/api/chat` + `/api/chat/status/:id` |
| `virtual-office/virtual-office.html` | Add chat panel UI (placement per OD-1) |
| `scripts/hermes-api-server.py` | Possibly minor: add `source` to `_adv_meta`; no architectural change |
| `CLAUDE.md` | Section 7 wording (OD-6) |
| `docs/RA-multi-agent-master-design.md` | Section 7 wording (OD-6) |
| `virtual-office/virtual-office-mvp.md` | Section 7 wording (OD-6) |
| `docs/ra-advisory-api.md` | Document `source` metadata field |
| `virtual-office/docker-compose.yml` | Confirm `read_only: true` retained |

---

## Annex A — Cross-reference index

| Claim | Source |
|---|---|
| VO is read-only | `CLAUDE.md:212`, `virtual-office-mvp.md:10` |
| Hermes unaware of VO | `CLAUDE.md:212`, `master-design.md:154`, `master-design.md:170`, `master-design.md:281` |
| GATE: Close/Reopen WP human-only | `CLAUDE.md:173` |
| GATE: KB repos read-only | `CLAUDE.md:176`, `CLAUDE.md:206-210` |
| Design philosophy | `CLAUDE.md:18-22` |
| `/v1/ra/advisory` query optional check | `scripts/hermes-api-server.py:749-753` |
| `build_advisory_context` wp_context handling | `scripts/hermes-api-server.py:431-470` |
| Hermes stateless invocation | `scripts/hermes-api-server.py:476-478` |
| `_honcho_record` write-only | `scripts/hermes-api-server.py:539-575` |
| `request_ref` pattern | `scripts/hermes-api-server.py:756, 525-536, 789-830` |
| Adapter 405 block | `virtual-office-honcho-adapter.js:304-309` |
| VO main-container layout | `virtual-office.html:169, 252-317` |
| VO log + detail panel | `virtual-office.html:319-320` |
| Stage dimensions | `virtual-office.html:39-40` |
| Heat Map (viz-panel) | `virtual-office.html:271-316` |
| `advisory_returned` event already handled | `virtual-office.html:502, 604-607` |

---

End of SPEC.
