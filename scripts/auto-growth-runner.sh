#!/usr/bin/env bash
# auto-growth-runner.sh — non-email RA growth automation entrypoint.
#
# Daily:
#   - Run pre-auto readiness checks.
#   - Execute the daily KB growth case idempotently.
# Weekly:
#   - On Monday, execute source curriculum seed idempotently for all RA peers.
# Monthly/Quarterly:
#   - Run autonomous-study delta dry-run and source coverage audit via
#     non-email-growth-loop.py.

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

RUN_TS="$(date -u +%Y%m%dT%H%M%SZ)"
REPORT_DIR="$REPO_ROOT/reports/auto-growth"
mkdir -p "$REPORT_DIR"

OPERATION_TZ="${AUTO_GROWTH_OPERATION_TZ:-Asia/Seoul}"
RUN_DATE="$(TZ="$OPERATION_TZ" date +%F)"
WEEKDAY="$(TZ="$OPERATION_TZ" date +%u)"
PENDING_SCOPE="${AUTO_GROWTH_PENDING_SCOPE:-ra}"
MAX_PENDING="${AUTO_GROWTH_MAX_PENDING:-0}"
CASES_PER_AGENT="${AUTO_GROWTH_CASES_PER_AGENT:-1}"
SOURCE_POOL="${AUTO_GROWTH_SOURCE_POOL:-10}"
MAX_CHUNKS_PER_CASE="${AUTO_GROWTH_MAX_CHUNKS_PER_CASE:-1}"
EXECUTE_CURRICULUM_MODE="${AUTO_GROWTH_EXECUTE_CURRICULUM:-weekly}"

echo "auto-growth started at ${RUN_TS}"
echo "operation_timezone=${OPERATION_TZ} run_date=${RUN_DATE}"
echo "pending_scope=${PENDING_SCOPE} max_pending=${MAX_PENDING}"

python3 scripts/pre-auto-growth-loop.py \
  --iterations 1 \
  --pending-scope "$PENDING_SCOPE" \
  --max-pending "$MAX_PENDING" \
  --cases-per-agent "$CASES_PER_AGENT" \
  --source-pool "$SOURCE_POOL" \
  --max-chunks-per-case "$MAX_CHUNKS_PER_CASE" \
  --date "$RUN_DATE" \
  --operation-timezone "$OPERATION_TZ" \
  --sleep-seconds 10 \
  --drain-timeout-seconds 900 \
  --execute-daily-growth \
  --output "$REPORT_DIR/pre-auto-${RUN_TS}.json"

NON_EMAIL_ARGS=(
  --cadence all
  --agent all
  --max-pending "$MAX_PENDING"
  --cases-per-agent "$CASES_PER_AGENT"
  --source-pool "$SOURCE_POOL"
  --max-chunks-per-case "$MAX_CHUNKS_PER_CASE"
  --date "$RUN_DATE"
  --operation-timezone "$OPERATION_TZ"
  --output "$REPORT_DIR/non-email-${RUN_TS}.json"
)

if [[ "$EXECUTE_CURRICULUM_MODE" == "always" ]] || {
  [[ "$EXECUTE_CURRICULUM_MODE" == "weekly" ]] && [[ "$WEEKDAY" == "1" ]]
}; then
  NON_EMAIL_ARGS+=(--execute-curriculum)
fi

python3 scripts/non-email-growth-loop.py "${NON_EMAIL_ARGS[@]}"

echo "auto-growth completed at $(date -u +%Y%m%dT%H%M%SZ)"
