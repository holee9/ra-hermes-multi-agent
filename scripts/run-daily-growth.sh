#!/usr/bin/env bash
# run-daily-growth.sh — established manual daily-growth routine.
#
# Pins cases-per-agent=3 (= 9 cases/day: ra_us/ra_eu/ra_kr x3), which is the
# baseline this project has run since 06-22. hermes-auto-growth.service ships
# AUTO_GROWTH_CASES_PER_AGENT=1 (= 3/day) as its default; running pre-auto-
# growth-loop.py with the service env alone under-fills the day. This wrapper
# makes the 9/day baseline explicit so the default-value footgun is gone.
#
# Safety guards (from autonomous-study-bootstrap-safety) are preserved because
# this just calls pre-auto-growth-loop.py: dry-run always runs first, the
# execute gate checks deriver pending, peer_id underscore is verified.
#
# Usage:
#   bash scripts/run-daily-growth.sh              # execute (write 9 cases)
#   bash scripts/run-daily-growth.sh --dry-run     # plan-only, no DB write
#   bash scripts/run-daily-growth.sh --max-pending 10   # raise gate when deriver backlog drains slowly
#
# Exit codes mirror pre-auto-growth-loop.py (non-zero on gate failure).

set -euo pipefail
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

if [[ -f "$SCRIPT_DIR/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  . "$SCRIPT_DIR/.env"
  set +a
fi

MAX_PENDING="${MAX_PENDING:-0}"
DRY_RUN=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --max-pending) MAX_PENDING="${2:?--max-pending needs a value}"; shift 2 ;;
    -h|--help)
      /usr/bin/sed -n '2,30p' "$0"
      exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

RUN_DATE="$(TZ=Asia/Seoul date +%F)"
RUN_TS="$(date -u +%Y%m%dT%H%M%SZ)"
REPORT_DIR="reports/auto-growth"
mkdir -p "$REPORT_DIR"

ARGS=(
  --iterations 1
  --pending-scope ra
  --max-pending "$MAX_PENDING"
  --cases-per-agent 3
  --source-pool 10
  --max-chunks-per-case 1
  --date "$RUN_DATE"
  --operation-timezone Asia/Seoul
  --sleep-seconds 10
  --drain-timeout-seconds 900
  --output "$REPORT_DIR/run-${RUN_TS}.json"
)
if [[ $DRY_RUN -eq 0 ]]; then
  ARGS+=(--execute-daily-growth)
  echo ">> daily-growth EXECUTE: cases-per-agent=3 (target 9/day, ra_us/eu/kr x3)"
  echo ">> max-pending=$MAX_PENDING (raise via --max-pending N if deriver backlog blocks the gate)"
else
  echo ">> daily-growth DRY-RUN (no DB write)"
fi

python3 scripts/pre-auto-growth-loop.py "${ARGS[@]}"
