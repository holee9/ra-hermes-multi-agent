#!/usr/bin/env bash
# verify-honcho.sh — Verify Honcho server, pgvector dimensions, deriver, and GX10.
#
# REQ-TOOL-201~208 (SPEC-RA-TOOL-001)
#
# Usage:
#   bash scripts/verify-honcho.sh
#   HONCHO_URL=http://t3610:8000 bash scripts/verify-honcho.sh
#
# Env vars (override device-map defaults via [IF] pattern):
#   HONCHO_URL        default: from detect-device.sh
#   GX10_URL          default: from detect-device.sh
#   POSTGRES_URL      default: from detect-device.sh
#   POSTGRES_DOCKER   name of the running postgres container (default: honcho-postgres-1)
#   DERIVER_DOCKER    name of the running deriver container (default: honcho-deriver-1)
#   GX10_CHAT_MODEL   expected chat model id (default: qwen3.6:latest)
#   GX10_EMBED_MODEL  expected embedding model id (default: qwen3-embedding:latest)
#   PGVECTOR_DIMS     expected embedding dimension (default: 4096)

set -euo pipefail
SCRIPT_DIR="$(cd "${BASH_SOURCE[0]%/*}" && pwd)"

# Load local secrets if present (git-ignored, never committed).
# shellcheck disable=SC1091
[ -f "${SCRIPT_DIR}/.env" ] && source "${SCRIPT_DIR}/.env"

# Load device-aware URLs.
# shellcheck disable=SC1090
source "${SCRIPT_DIR}/detect-device.sh"

POSTGRES_DOCKER="${POSTGRES_DOCKER:-honcho-postgres-1}"
DERIVER_DOCKER="${DERIVER_DOCKER:-honcho-deriver-1}"
GX10_CHAT_MODEL="${GX10_CHAT_MODEL:-gpt-oss:120b}"
GX10_EMBED_MODEL="${GX10_EMBED_MODEL:-qwen3-embedding:latest}"
PGVECTOR_DIMS="${PGVECTOR_DIMS:-4096}"

CURL=/usr/bin/curl
DOCKER=/usr/bin/docker
JQ=/usr/bin/jq

PASS=0
FAIL=0
TOTAL=6

_pass() { echo "[PASS] $1"; PASS=$((PASS + 1)); }
_fail() { echo "[FAIL] $1"; FAIL=$((FAIL + 1)); }

# 1. Honcho API health —————————————————————————————————————
resp=$("${CURL}" -sf "${HONCHO_URL}/health" 2>/dev/null) || { _fail "Honcho API health: ${HONCHO_URL}/health unreachable"; resp=""; }
if [ -n "${resp}" ]; then
  status=$(echo "${resp}" | "${JQ}" -r '.status // empty' 2>/dev/null)
  if [ "${status}" = "ok" ]; then
    _pass "Honcho API health"
  else
    _fail "Honcho API health: expected status=ok, got '${status}'"
  fi
fi

# 2. workspace: work / infra ——————————————————————————————
_check_workspace() {
  local ws="$1"
  local body
  body=$("${CURL}" -sf -X POST "${HONCHO_URL}/v3/workspaces/list" \
    -H "Content-Type: application/json" -d '{}' 2>/dev/null) || { _fail "workspace ${ws}: list request failed"; return; }
  local found
  found=$(echo "${body}" | "${JQ}" -r --arg id "${ws}" '.items[]? | select(.id == $id) | .id' 2>/dev/null)
  if [ "${found}" = "${ws}" ]; then
    _pass "workspace: ${ws}"
  else
    _fail "workspace: ${ws} not found in /v3/workspaces/list"
  fi
}
_check_workspace "work"
_check_workspace "infra"

# 4. pgvector dimensions ————————————————————————————————————
# @MX:ANCHOR REQ-TOOL-203: 4096 dimension is coupled to qwen3-embedding — do not change.
_check_pgvector() {
  if [ ! -x "${DOCKER}" ]; then
    _fail "pgvector dimensions: docker not found at ${DOCKER}"
    return
  fi
  if ! "${DOCKER}" ps --filter "name=${POSTGRES_DOCKER}" --format "{{.Names}}" 2>/dev/null | /usr/bin/grep -q "${POSTGRES_DOCKER}"; then
    _fail "pgvector dimensions: container ${POSTGRES_DOCKER} not running"
    return
  fi
  # Simple confirmed query (matches what Honcho migrations create).
  local dims
  dims=$("${DOCKER}" exec "${POSTGRES_DOCKER}" psql -U honcho -d honcho -t -c \
    "SELECT atttypmod FROM pg_attribute JOIN pg_class ON attrelid = pg_class.oid
     WHERE relname = 'documents' AND attname = 'embedding' LIMIT 1;" \
    2>/dev/null) || dims=""
  dims="${dims// /}"
  dims="${dims//$'\n'/}"
  if [ "${dims}" = "${PGVECTOR_DIMS}" ]; then
    _pass "pgvector dimensions: ${dims}"
  elif [ -z "${dims}" ]; then
    _fail "pgvector dimensions: 'documents.embedding' column not found (migration not applied?)"
  else
    _fail "pgvector dimensions: expected ${PGVECTOR_DIMS}, got '${dims}'"
  fi
}
_check_pgvector

# 5. deriver running ————————————————————————————————————————
_check_deriver() {
  if [ ! -x "${DOCKER}" ]; then
    _fail "deriver: docker not found at ${DOCKER}"
    return
  fi
  local running
  running=$("${DOCKER}" inspect "${DERIVER_DOCKER}" --format "{{.State.Running}}" 2>/dev/null) || running=""
  if [ "${running}" = "true" ]; then
    _pass "deriver: ${DERIVER_DOCKER} running"
  else
    _fail "deriver: ${DERIVER_DOCKER} not running (got '${running}')"
  fi
}
_check_deriver

# 6. GX10 models ————————————————————————————————————————————
_check_gx10() {
  local models
  models=$("${CURL}" -sf "${GX10_URL}/v1/models" 2>/dev/null) || { _fail "GX10 models: ${GX10_URL}/v1/models unreachable"; return; }
  local chat_found embed_found
  chat_found=$(echo "${models}" | "${JQ}" -r --arg m "${GX10_CHAT_MODEL}" '.data[]? | select(.id == $m) | .id' 2>/dev/null)
  embed_found=$(echo "${models}" | "${JQ}" -r --arg m "${GX10_EMBED_MODEL}" '.data[]? | select(.id == $m) | .id' 2>/dev/null)
  if [ -n "${chat_found}" ] && [ -n "${embed_found}" ]; then
    _pass "GX10 models: ${GX10_CHAT_MODEL} + ${GX10_EMBED_MODEL}"
  else
    local missing=""
    [ -z "${chat_found}" ]  && missing="${GX10_CHAT_MODEL}"
    [ -z "${embed_found}" ] && missing="${missing:+${missing}, }${GX10_EMBED_MODEL}"
    _fail "GX10 models: not found: ${missing}"
  fi
}
_check_gx10

# Summary ———————————————————————————————————————————————————
echo ""
if [ "${FAIL}" -eq 0 ]; then
  echo "=== ${PASS}/${TOTAL} checks passed ==="
  exit 0
else
  echo "=== ${FAIL}/${TOTAL} checks failed ==="
  exit 1
fi
