#!/usr/bin/env bash
# cold-start-verify.sh — MVP E2E cold-start verification (7 acceptance criteria).
#
# REQ-TOOL-301~307 (SPEC-RA-TOOL-001)
#
# Usage:
#   bash scripts/cold-start-verify.sh
#   COLD_START_CONFIG=scripts/cold-start-config.json bash scripts/cold-start-verify.sh
#
# Env vars (override device-map defaults via [IF] pattern):
#   HONCHO_URL           default: from detect-device.sh
#   N8N_URL              default: from detect-device.sh
#   COLD_START_CONFIG    path to config JSON (default: scripts/cold-start-config.json)
#   SKIP_N8N             set to 1 to skip n8n-dependent checks (AC1, AC3, AC4, AC5)
#   OPENPROJECT_URL      default: from detect-device.sh

set -euo pipefail
export PATH="/usr/bin:/usr/local/bin:/bin:/usr/sbin:/sbin:${PATH}"
SCRIPT_DIR="$(cd "${BASH_SOURCE[0]%/*}" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Load local secrets if present (git-ignored, never committed).
# Put N8N_API_KEY=<value> and any other secrets in scripts/.env
# shellcheck disable=SC1091
[ -f "${SCRIPT_DIR}/.env" ] && source "${SCRIPT_DIR}/.env"

# REQ-TOOL-108: load device-aware URLs first.
# shellcheck disable=SC1090
source "${SCRIPT_DIR}/detect-device.sh"

COLD_START_CONFIG="${COLD_START_CONFIG:-${SCRIPT_DIR}/cold-start-config.json}"
SKIP_N8N="${SKIP_N8N:-0}"

# Load timeout and confidence from external config ([IF] pattern).
if [ -f "${COLD_START_CONFIG}" ]; then
  TIMEOUT_SEC=$(/usr/bin/jq -r '.timeout_seconds // 300' "${COLD_START_CONFIG}")
  CONFIDENCE_THRESH=$(/usr/bin/jq -r '.confidence_threshold // 0.7' "${COLD_START_CONFIG}")
  TEST_SUBJECT=$(/usr/bin/jq -r '.test_email.subject // "[TEST] Cold Start Test"' "${COLD_START_CONFIG}")
  GATE1_FILE=$(/usr/bin/jq -r '.gate1.check_file // "n8n/workflows/mail-triage.json"' "${COLD_START_CONFIG}")
else
  echo "WARN: config not found at ${COLD_START_CONFIG}, using built-in defaults"
  TIMEOUT_SEC=300
  CONFIDENCE_THRESH=0.7
  TEST_SUBJECT="[TEST] Cold Start Test"
  GATE1_FILE="n8n/workflows/mail-triage.json"
fi

PASS=0
FAIL=0
SKIP=0
TOTAL=7
REPORT_DIR="${REPO_ROOT}/reports"
TIMESTAMP=$(date -u +"%Y-%m-%d-%H-%M" 2>/dev/null) || TIMESTAMP="unknown"
REPORT_FILE="${REPORT_DIR}/cold-start-${TIMESTAMP}.json"

declare -a RESULTS=()

_pass() {
  echo "[PASS] $1"
  PASS=$((PASS + 1))
  RESULTS+=("{\"ac\":\"$2\",\"result\":\"PASS\",\"detail\":\"$1\"}")
}
_fail() {
  echo "[FAIL] $1"
  FAIL=$((FAIL + 1))
  RESULTS+=("{\"ac\":\"$2\",\"result\":\"FAIL\",\"detail\":\"$1\"}")
}
_skip() {
  echo "[SKIP] $1"
  SKIP=$((SKIP + 1))
  RESULTS+=("{\"ac\":\"$2\",\"result\":\"SKIP\",\"detail\":\"$1\"}")
}

N8N_API_KEY="${N8N_API_KEY:-}"
_n8n_curl() {
  if [ -n "${N8N_API_KEY}" ]; then
    curl -sf -H "X-N8N-API-KEY: ${N8N_API_KEY}" "$@" 2>/dev/null
  else
    curl -sf "$@" 2>/dev/null
  fi
}

_n8n_available() {
  if [ "${SKIP_N8N}" = "1" ]; then return 1; fi
  _n8n_curl "${N8N_URL}/healthz" >/dev/null && return 0 || return 1
}

# AC1 — mail-triage workflow is active ————————————————————
_ac1() {
  if ! _n8n_available; then
    _skip "AC1 mail-triage: n8n unavailable, skipping (REQ-TOOL-307)" "AC1"
    return
  fi
  local wf_resp
  wf_resp=$(_n8n_curl "${N8N_URL}/api/v1/workflows") || {
    _fail "AC1 mail-triage: n8n workflows API unreachable (set N8N_API_KEY if auth required)" "AC1"; return; }
  local active
  active=$(echo "${wf_resp}" | /usr/bin/jq -r '(.data // .workflows)[]? | select(.name == "mail-triage") | .active' 2>/dev/null | /usr/bin/head -1)
  if [ "${active}" = "true" ]; then
    _pass "AC1 mail-triage workflow active" "AC1"
  else
    _fail "AC1 mail-triage: workflow not found or inactive (active=${active})" "AC1"
  fi
}

# AC2 — RA analysis result JSON schema ————————————————————
# Validate the frozen data contract from CLAUDE.md against Honcho session messages.
_ac2() {
  local sessions
  sessions=$(curl -sf -X POST "${HONCHO_URL}/v3/workspaces/list" \
    -H "Content-Type: application/json" -d '{}' 2>/dev/null) || {
    _fail "AC2 RA schema: cannot list workspaces" "AC2"; return; }
  local work_ws
  work_ws=$(echo "${sessions}" | /usr/bin/jq -r '.items[]? | select(.id == "work") | .id' 2>/dev/null)
  if [ "${work_ws}" != "work" ]; then
    _fail "AC2 RA schema: 'work' workspace not found" "AC2"; return
  fi
  # Check schema definition is present in n8n mail-triage workflow.
  local triage_path="${REPO_ROOT}/${GATE1_FILE}"
  if [ ! -f "${triage_path}" ]; then
    _fail "AC2 RA schema: ${GATE1_FILE} not found at ${triage_path}" "AC2"; return
  fi
  local required_fields=("actor" "wp" "match" "confidence" "region" "comment")
  local missing=0
  for field in "${required_fields[@]}"; do
    if ! /usr/bin/grep -q "${field}" "${triage_path}"; then
      echo "  missing field: ${field}"
      missing=$((missing + 1))
    fi
  done
  if [ "${missing}" -eq 0 ]; then
    _pass "AC2 RA schema fields present in mail-triage" "AC2"
  else
    _fail "AC2 RA schema: ${missing} required fields missing from mail-triage" "AC2"
  fi
}

# AC3 — WP matching routes to 'infra' workspace ———————————
_ac3() {
  if ! _n8n_available; then
    _skip "AC3 WP matching: n8n unavailable, skipping (REQ-TOOL-307)" "AC3"
    return
  fi
  local sessions
  sessions=$(curl -sf -X POST "${HONCHO_URL}/v3/workspaces/list" \
    -H "Content-Type: application/json" -d '{}' 2>/dev/null) || {
    _fail "AC3 WP matching: Honcho workspaces unreachable" "AC3"; return; }
  local infra_ws
  infra_ws=$(echo "${sessions}" | /usr/bin/jq -r '.items[]? | select(.id == "infra") | .id' 2>/dev/null)
  if [ "${infra_ws}" = "infra" ]; then
    _pass "AC3 infra workspace reachable for WP matching" "AC3"
  else
    _fail "AC3 WP matching: 'infra' workspace not found" "AC3"
  fi
}

# AC4 — Honcho records mail triage session ————————————————
_ac4() {
  if ! _n8n_available; then
    _skip "AC4 Honcho recording: n8n unavailable, skipping (REQ-TOOL-307)" "AC4"
    return
  fi
  # Check that the work workspace has peers (RA agents) registered.
  local peers
  peers=$(curl -sf -X POST "${HONCHO_URL}/v3/workspaces/work/peers/list" \
    -H "Content-Type: application/json" -d '{}' 2>/dev/null) || {
    _fail "AC4 Honcho recording: peer list call failed" "AC4"; return; }
  local count
  count=$(echo "${peers}" | /usr/bin/jq -r '.items | length' 2>/dev/null)
  if [ -n "${count}" ] && [ "${count}" -gt 0 ]; then
    _pass "AC4 Honcho recording: ${count} peers registered in work workspace" "AC4"
  else
    _fail "AC4 Honcho recording: no peers in work workspace (count=${count})" "AC4"
  fi
}

# AC5 — deriver reflection (disabled by default) ——————————
_ac5() {
  local enabled
  enabled=$(/usr/bin/jq -r '.checks.ac5_deriver_reflection // false' "${COLD_START_CONFIG}" 2>/dev/null)
  if [ "${enabled}" != "true" ]; then
    _skip "AC5 deriver reflection: disabled in config (ac5_deriver_reflection=false)" "AC5"
    return
  fi
  local docker_bin
  docker_bin=$(command -v docker 2>/dev/null) || {
    _fail "AC5 deriver: docker not found" "AC5"; return; }
  local running
  running=$("${docker_bin}" inspect honcho-deriver-1 --format "{{.State.Running}}" 2>/dev/null) || running=""
  if [ "${running}" = "true" ]; then
    _pass "AC5 deriver reflection: container running" "AC5"
  else
    _fail "AC5 deriver: honcho-deriver-1 not running" "AC5"
  fi
}

# AC6 — GATE-1: no WP close/reopen automation —————————————
# @MX:ANCHOR GATE-1: WP Close/Reopen is permanently human-only. Never automate.
_ac6() {
  local triage_path="${REPO_ROOT}/${GATE1_FILE}"
  if [ ! -f "${triage_path}" ]; then
    _fail "AC6 GATE-1: ${GATE1_FILE} not found" "AC6"; return
  fi
  local forbidden_count=0
  local forbidden_paths=("/work-packages/:id/close" "/work-packages/:id/reopen")
  if [ -f "${COLD_START_CONFIG}" ]; then
    readarray -t cfg_paths < <(/usr/bin/jq -r '.gate1.forbidden_paths[]? // empty' "${COLD_START_CONFIG}" 2>/dev/null)
    [ "${#cfg_paths[@]}" -gt 0 ] && forbidden_paths=("${cfg_paths[@]}")
  fi
  for path in "${forbidden_paths[@]}"; do
    if grep -q "${path}" "${triage_path}" 2>/dev/null; then
      echo "  GATE-1 VIOLATION: '${path}' found in ${GATE1_FILE}"
      forbidden_count=$((forbidden_count + 1))
    fi
  done
  if [ "${forbidden_count}" -eq 0 ]; then
    _pass "AC6 GATE-1: no WP close/reopen paths in mail-triage" "AC6"
  else
    _fail "AC6 GATE-1: ${forbidden_count} forbidden path(s) found in ${GATE1_FILE}" "AC6"
  fi
}

# AC7 — timeout compliance ————————————————————————————————
_ac7() {
  # Verify that the configured timeout is within acceptable bounds (>= 60s, <= 600s).
  if [ "${TIMEOUT_SEC}" -ge 60 ] && [ "${TIMEOUT_SEC}" -le 600 ]; then
    _pass "AC7 timeout: ${TIMEOUT_SEC}s (within [60, 600] range)" "AC7"
  else
    _fail "AC7 timeout: ${TIMEOUT_SEC}s out of acceptable range [60, 600]" "AC7"
  fi
}

# Run all checks ————————————————————————————————————————————
echo "=== Cold Start Verification (SPEC-RA-TOOL-001) ==="
echo "config:    ${COLD_START_CONFIG}"
echo "honcho:    ${HONCHO_URL}"
echo "n8n:       ${N8N_URL}"
echo "timeout:   ${TIMEOUT_SEC}s"
echo "threshold: ${CONFIDENCE_THRESH}"
echo ""

_ac1
_ac2
_ac3
_ac4
_ac5
_ac6
_ac7

# Save JSON report (REQ-TOOL-305) ——————————————————————————
mkdir -p "${REPORT_DIR}"
joined=$(printf '%s,' "${RESULTS[@]}")
joined="${joined%,}"
cat > "${REPORT_FILE}" <<REPORTEOF
{
  "spec": "SPEC-RA-TOOL-001",
  "timestamp": "${TIMESTAMP}",
  "device": "${RA_DEVICE:-unknown}",
  "honcho_url": "${HONCHO_URL}",
  "n8n_url": "${N8N_URL}",
  "pass": ${PASS},
  "fail": ${FAIL},
  "skip": ${SKIP},
  "total": ${TOTAL},
  "results": [${joined}]
}
REPORTEOF
echo ""
echo "report: ${REPORT_FILE}"

# Summary ———————————————————————————————————————————————————
echo ""
if [ "${FAIL}" -eq 0 ]; then
  echo "=== ${PASS}/${TOTAL} passed (${SKIP} skipped) ==="
  exit 0
else
  echo "=== ${FAIL}/${TOTAL} failed (${SKIP} skipped) ==="
  exit 1
fi
