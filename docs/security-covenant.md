# Security Classification Covenant v1.0

**Established 2026-10-20 by direct user directive. Binding on all 3 sessions:
ra-hermes-multi-agent, hermes-ra, ra-med-bot. Amendments require explicit user
approval.**

## Article 1 — Classification by SOURCE, not content

- **[외부 사실] / public regulatory facts** — statutes, guidance, public
  FDA/official data, public standards → GitHub remote storage permitted.
- **[내부] / internal** — anything originating from the NAS, company email, or
  internal documents (product info, certification numbers, expiry dates,
  customers, invoices, staff, DHF derivatives) → **internal Gitea / NAS /
  T3610-local storage ONLY. Never commit, push, or paste into any GitHub
  remote — this repo included.**
- Decision principle: if the material came from the NAS, email, or internal
  documents, it is [내부] regardless of what the content looks like.

## Article 2 — Mechanical enforcement (promises are not controls)

1. Each session runs a periodic automated scan (pattern tripwire) on its own
   repo and surfaces results in monitoring/ops console.
   This repo: `python3 scripts/security-scan.py` (exit 1 = CONTENT finding).
2. New data files must state source classification; unclassified data is not
   committable.
3. Violation handling: block before push if possible; if already pushed →
   immediate remediation + notify all 3 sessions.
4. The covenant is reflected as a HARD rule in each session's top-level
   operating document (CLAUDE.md or equivalent).

## Article 3 — Immediate effect

Confidential ledgers/documents on GitHub remotes are prohibited (the
ra-project registry placement discussion is void; local confidential ledger +
structured lookup is the design). ra-project `06_심사_QA이력/` (partner
emails, invoices) is an [내부]-grade violation — migration plan to be
established by the owner with user approval.

## Article 4 — Amendments

User explicit approval only.
