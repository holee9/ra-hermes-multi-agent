# 2026-06-13 Autonomous Study Bootstrap Peer ID Incident

GitHub issue: #49

## Severity

P0 critical data-contract incident.

## Summary

The autonomous study bootstrap wrote RA learning records to profile-style IDs such as
`ra-us` instead of the frozen Honcho peer IDs `ra_us`, `ra_eu`, and `ra_kr`.

This is not a cosmetic naming mismatch. Honcho memory, documents, representation
queues, and peer growth are keyed by `peer_id`, so the bootstrap grew a spurious peer
instead of Hermes' intended RA agents.

## Contract That Was Violated

`profiles/setup.sh` states the data contract explicitly:

> aiPeer uses underscore convention (ra_us, not ra-us) to match the frozen data contract.

Therefore:

| Concept | Valid Example | Invalid Example |
| --- | --- | --- |
| Hermes profile ID | `ra-us` | `ra_us` |
| Honcho peer ID / aiPeer | `ra_us` | `ra-us` |

## Evidence Observed

- `scripts/autonomous-study-scheduler.py` used `AGENTS[].id` values `ra-us`, `ra-eu`,
  and `ra-kr` as Honcho message `peer_id` values.
- The running bootstrap produced study records under `ra-us`.
- Honcho contained a spurious `ra-us` peer while the intended frozen peers are
  `ra_us`, `ra_eu`, and `ra_kr`.
- Study records and derived documents were attached to `ra-us`, not `ra_us`.
- Some derived observations were meta-level records about `study_insight` authorship
  rather than direct RA domain knowledge, because the message content was a JSON
  envelope.

## Remediation

- Separate `profile_id` from `peer_id` in the autonomous study scheduler.
- Fail fast if a configured Honcho `peer_id` contains a hyphen.
- Key bootstrap resume progress by underscore `peer_id`, not profile ID.
- Create study sessions as `study-ra_us-...`, `study-ra_eu-...`, and `study-ra_kr-...`.
- Write Honcho message content as readable regulatory knowledge text rather than a
  JSON envelope, while keeping structured fields in metadata.
- Add `scripts/verify-study-scheduler.py` to catch this regression without touching
  Honcho or Postgres.

## Side-Effect Boundary

This fix does not delete, migrate, or mutate historical Honcho data. Existing polluted
records under `ra-us` remain for a separately approved cleanup/migration step.

## Required Reflection For Future Claude Code Sessions

Before touching Hermes autonomous learning code, verify these invariants:

1. Profile IDs are for filesystem/profile selection only.
2. Honcho `peer_id` values must be underscore IDs.
3. Bootstrap progress must not resume from legacy hyphen peer keys.
4. Honcho message content should be memory-derivable domain text, not raw JSON envelopes.
5. Database cleanup is a separate operation requiring explicit approval.
