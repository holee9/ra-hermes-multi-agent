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
- Run bootstrap `--dry-run` with `STUDY_BOOTSTRAP_MAX=1` before any real bootstrap restart.
- Check host processes with `ps -eo pid,ppid,etime,args`; do not rely only on sandbox-local process visibility.

## Forbidden Pattern

Any write like `"peer_id": agent_id` is forbidden when `agent_id` can contain `ra-us`,
`ra-eu`, or `ra-kr`.

Direct DB rename of wrong-peer data is also forbidden:

- Do not update `messages.peer_name` from `ra-us` to `ra_us`.
- Do not update `documents.observer`/`observed` from `ra-us` to `ra_us`.
- Do not move wrong-peer derived documents into correct peers.
- Do not restart bootstrap while `scripts/study-bootstrap-progress.json` contains legacy hyphen keys.

## Database Safety

Wrong-peer recovery must use this sequence:

1. Stop the wrong bootstrap process and child `claude -p` process first.
2. Stop `honcho-deriver-1` before queue/document mutation.
3. Export affected `messages`, `documents`, `queue`, and `sessions` to local JSONL backups.
4. Quarantine wrong-peer pending queue rows.
5. Soft-delete or quarantine wrong-peer derived documents.
6. Recover only from raw `study_insight` payloads, replayed as clean text into underscore peers.
7. Restart `honcho-deriver-1` and monitor correct-peer backlog.

Use the idempotent recovery tool for #49-style payload replay:

```bash
set -a && . scripts/.env && set +a
python3 scripts/replay-study-insights-issue49.py
python3 scripts/replay-study-insights-issue49.py --execute --batch-size 50
```

Polluted records under legacy hyphen IDs must be preserved or quarantined for audit unless the user explicitly approves irreversible deletion.
