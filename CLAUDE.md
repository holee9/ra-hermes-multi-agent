# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**RA Hermes Multi-Agent** — A learning multi-agent system for medical device regulatory affairs (RA). Automates email triage and work package management via AI agents that grow smarter through human feedback.

Current status: **MVP skeleton implemented. T3610 deployment in progress.**

---

## Development Commands

### Git / GitHub CLI (ALWAYS use the Bash tool — never PowerShell)

```bash
git push origin main
gh issue create --title "title" --body "body"
gh issue comment <number> --body "body"
gh pr create --title "title" --body "body"
```

`git` and `gh` are not on the PowerShell PATH. Use the `Bash` tool for all git/gh operations.
`gh` is at `/c/Users/drake/bin/gh`, authenticated as `holee9` (repo + workflow scope).
Remote: `https://github.com/holee9/ra-hermes-multi-agent.git`

### Virtual Office Prototype

`virtual-office/virtual-office.html` is a self-contained file. Open directly in a browser — no build step required.

---

## Architecture

### System Components

```
Business Workspace                       Infrastructure Workspace
 ├ ra_us / ra_eu / ra_kr (Hermes)         ├ infra_t3610 / infra_gx10 / infra_rpi
 ├ op_manager                             └ (vote-based consensus)
 └ n8n_manager
        │                                          │
   [n8n: mail-triage, gate, bridge]  ←─bridge─────┘
        │
   OpenProject (WPs)  ·  Honcho (T3610)  ·  GX10 Qwen3 (inference)
        │
   Virtual Office (read-only, Honcho activity log)
```

### Hardware

| Machine | Spec | Role |
|---------|------|------|
| T3610 | Xeon 12C/24T, 32GB, Linux | Honcho server (FastAPI + deriver + PostgreSQL/pgvector + Redis) + RA experts |
| GX10 | Grace Blackwell ARM, Qwen3 | LLM inference backend (tool-calling required) |
| Raspberry Pi 5+ | 16GB | OpenProject + n8n |

Honcho delegates all inference to GX10 via OpenAI-compatible endpoint over 2.5G LAN.

### Key Boundaries

**Coded artifacts** (implementation targets in `docs/implementation-spec.md`):
- n8n mail-triage workflow (parsing, routing, WP operations, Honcho recording)
- Infrastructure agent voting scaffold (interface only — rules left empty for learning)
- n8n bridge (infra → business, unidirectional)
- Virtual office web app (Docker single-container, read-only observer)

**Hermes runtime** (NOT coded — configured and operated):
- RA agent profiles (ra_us/ra_eu/ra_kr) and their SOUL.md personas
- Honcho memory learning loop and 3-point evaluation feedback
- Skill self-improvement and session persistence

**Do not reimplement what Hermes already provides** (memory, sessions, skills, Kanban).

### Data Contracts (Fixed)

**RA analysis result JSON** (mail-triage output, frozen):
```json
{ "actor":"ra_us", "wp":"WP-123|null", "match":"existing|new",
  "confidence":0.0-1.0, "region":"US|EU|KR",
  "comment":"...", "transition_proposed":"리뷰중|null" }
```

**Activity log format** (Honcho output = Virtual Office input, frozen):
```json
{ "ts":"ISO8601", "type":"mail_received|matched|comment_added|...",
  "actor":"<actor_id>", "payload":{...} }
```

Actor IDs: `ra_us`, `ra_eu`, `ra_kr`, `op_manager`, `n8n_manager`, `infra_*`, `human`, `system`

### Gate Rules (Hard, Never Coded Around)

| Action | Authority |
|--------|-----------|
| Matching + comment | Agent autonomous (Green) |
| Status transition (except close) | Escalates to autonomous as learning matures |
| **Close / Reopen WP** | **Human only — permanently** |
| n8n workflow changes | Report first, then proceed |
| Destructive infra actions | Human approval required |

---

## Key Documents

| File | Purpose |
|------|---------|
| `docs/RA-multi-agent-master-design.md` | Master design — architecture, philosophy, decisions, open items |
| `docs/implementation-spec.md` | Implementation spec for coding tools — what to build vs what Hermes handles |
| `docs/operations-guide.md` | Operations guide for humans + Hermes runtime configuration |
| `ECOSYSTEM.md` | Ecosystem map across all related projects (injected into every repo) |
| `virtual-office/virtual-office.html` | Pixel-art visualization prototype (mockup data, no build needed) |
| `virtual-office/virtual-office-org-chart.md` | Character-to-agent mapping for the virtual office |
| `virtual-office/pixel-character-guide.md` | Sprite swap guide (code-drawn → Kenney CC0 PNG) |
| `virtual-office/virtual-office-mvp.md` | Virtual office MVP design spec |

---

## Implementation Maturity Markers

`[구현]` in spec files = ready to code at full depth.
`[IF]` in spec files = interface only — internal rules intentionally left empty for learning. Do NOT hardcode thresholds, weights, or consensus rules. Read them from external config so operations can tune them at runtime.

---

## Ecosystem Position

This repo is one piece of a larger RA ecosystem. Knowledge bases are separate projects (`llm-wiki`, `ra-project`, `MD-process`) — agents reference them unidirectionally; do not duplicate RAG here. The virtual office reads from this system but this system is unaware of the virtual office.
