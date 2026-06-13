# Autonomous Study Bootstrap Safety

## Hard Invariants

Hermes RA agents have two different identifiers:

| Purpose | Convention | Examples |
| --- | --- | --- |
| Hermes profile / soul directory | hyphen | `ra-us`, `ra-eu`, `ra-kr` |
| Honcho peer ID / aiPeer / memory key | underscore | `ra_us`, `ra_eu`, `ra_kr` |

Never use a profile ID as a Honcho `peer_id`.

## Required Checks Before Editing Study Code

- Read `docs/incidents/2026-06-13-autonomous-study-bootstrap-peer-id.md`.
- Confirm scheduler config separates `profile_id` and `peer_id`.
- Confirm all Honcho writes use underscore `peer_id` values.
- Confirm bootstrap resume keys use underscore `peer_id` values.
- Run `python3 scripts/verify-study-scheduler.py` after any scheduler change.

## Forbidden Pattern

Any write like `"peer_id": agent_id` is forbidden when `agent_id` can contain `ra-us`,
`ra-eu`, or `ra-kr`.

## Database Safety

Do not delete, rewrite, or migrate historical Honcho data without explicit user approval.
Polluted records under legacy hyphen IDs must be treated as a separate cleanup task.
