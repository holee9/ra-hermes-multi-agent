# 2026-06-13 Autonomous Study Bootstrap Peer ID Incident

GitHub issue: #49

## Discovery

This issue was discovered by the user (holee9) during manual testing of Hermes Agent sessions,
not by an automated Codex review. The user observed:
- 9,272 chunks processed
- ra-us session generated 1,144 insights, mostly under wrong peer `ra-us`
- EU bootstrap had 0 insights after hundreds of chunks

Evidence: https://github.com/holee9/ra-hermes-multi-agent/issues/48

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

### Code Fix

- Separate `profile_id` from `peer_id` in the autonomous study scheduler.
- Fail fast if a configured Honcho `peer_id` contains a hyphen.
- Key bootstrap resume progress by underscore `peer_id`, not profile ID.
- Create study sessions as `study-ra_us-...`, `study-ra_eu-...`, and `study-ra_kr-...`.
- Write Honcho message content as readable regulatory knowledge text rather than a
  JSON envelope, while keeping structured fields in metadata.
- Add `scripts/verify-study-scheduler.py` to catch this regression without touching
  Honcho or Postgres.

### Data Recovery Performed

Performed on 2026-06-13 after confirming the wrong-peer bootstrap process was still
running and continuing to write `ra-eu` records.

- Stopped the active wrong-peer bootstrap process.
- Stopped `honcho-deriver-1` before mutating affected queue/document rows.
- Exported affected rows to local JSONL backups under `backups/issue-49/`.
- Quarantined pending wrong-peer queue rows by marking them processed with an
  issue #49 quarantine note.
- Soft-deleted active derived documents where `observer` or `observed` was `ra-us`
  or `ra-eu`.
- Replayed 2,085 recoverable raw study insight payloads into the correct peers:
  - `ra-us` -> `ra_us`: 1,656 messages
  - `ra-eu` -> `ra_eu`: 429 messages
- Replayed messages use clean text content and recovery metadata instead of the
  original JSON envelope.
- Restarted `honcho-deriver-1` so clean `ra_us`/`ra_eu` messages can derive normal
  documents.

Final verification after replay:

| Check | Result |
| --- | ---: |
| Recovered `ra_us` messages | 1,656 |
| Recovered `ra_eu` messages | 429 |
| Recovered messages with JSON envelope content | 0 |
| Recovered messages with correct actor metadata | 2,085 / 2,085 |
| Wrong-peer `ra-us`/`ra-eu` active documents | 0 |
| Wrong-peer `ra-us`/`ra-eu` documents after cleanup queue pass | 0 |
| `ra_us -> ra_us` active documents observed after deriver restart | 71 |
| `ra_eu -> ra_eu` active documents observed after deriver restart | 94 |
| Replay idempotence check | `already_replayed=2085`, `to_replay=0` |

Recovery script:

```bash
set -a; . scripts/.env; set +a
python3 scripts/replay-study-insights-issue49.py --execute --batch-size 50
```

### Live DB Cleanup Follow-Up

On 2026-06-16, follow-up issue #56 removed the remaining live wrong-peer raw
records after confirming the clean replay and JSONL backups.

| Removed from live DB | Count |
| --- | ---: |
| `ra-us` / `ra-eu` messages | 2,086 |
| processed queue references | 639 |
| message embeddings | 2,086 |
| wrong-peer session memberships | 2 |

Post-cleanup verification:

| Check | Result |
| --- | ---: |
| Wrong-peer live messages | 0 |
| Wrong-peer queue refs | 0 |
| Wrong-peer embeddings | 0 |
| Wrong-peer session memberships | 0 |
| Wrong-peer active documents | 0 |
| Clean replay records retained under canonical peers | 2,085 |

## Side-Effect Boundary

The original wrong-peer rows are no longer retained in the live Honcho database.
Audit evidence is retained only in the JSONL backups under `backups/issue-49/`
with documented SHA-256 hashes. Derived wrong-peer documents were previously
removed from the active table. Pending wrong-peer queue rows were removed from
the live queue after backup verification.

## Required Reflection For Future Claude Code Sessions

Before touching Hermes autonomous learning code, verify these invariants:

1. Profile IDs are for filesystem/profile selection only.
2. Honcho `peer_id` values must be underscore IDs.
3. Bootstrap progress must not resume from legacy hyphen peer keys.
4. Honcho message content should be memory-derivable domain text, not raw JSON envelopes.
5. Do not directly rename wrong-peer documents into correct peers; recover from raw
   payloads and replay as clean text.
