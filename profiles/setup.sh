#!/usr/bin/env bash
# profiles/setup.sh — Create RA Hermes agent profiles and configure Honcho.
#
# REQ-TOOL-101~107 (SPEC-RA-TOOL-001)
#
# How it works:
#   1. Writes ~/.hermes/honcho.json with root-level baseUrl and a default host
#      block. hermes reads baseUrl from the JSON root (not from hosts.hermes).
#      Per-profile identity (aiPeer, workspace) lives in hosts.hermes_<id>.
#   2. Runs `hermes profile create <id> --no-skills` for each agent.
#      --no-skills skips bundled skill download (#13 handles SOUL.md inoculation).
#      Note: --clone is NOT used; profile host blocks are written manually (step 3).
#   3. Writes per-profile host block in honcho.json (aiPeer=<id>, workspace).
#      Also sets memory.provider=honcho in each profile's config.yaml via
#      `HERMES_HOME=~/.hermes/profiles/<id> hermes config set`.
#   4. Copies the project SOUL.md over the freshly-created profile's SOUL.md.
#
# Usage:
#   bash profiles/setup.sh
#   HERMES_CMD=/home/abyz-lab/.local/bin/hermes bash profiles/setup.sh
#   DRY_RUN=1 bash profiles/setup.sh
#
# Env vars ([IF] pattern — any can be overridden at runtime):
#   HERMES_CMD    hermes CLI binary (default: /home/abyz-lab/.local/bin/hermes)
#   SOUL_DIR      dir with *-SOUL.md files (default: profiles/souls)
#   HERMES_HOME   hermes default profile dir (default: ~/.hermes)
#   MODEL_DEFAULT default chat model (default: gpt-oss:120b)
#   MODEL_BASE_URL OpenAI-compatible chat endpoint (default: GX10_BASE_URL)
#   MODEL_API_KEY optional API key for MODEL_BASE_URL (not printed)
#   DRY_RUN       set to 1 to print commands without executing
#
# Prerequisites: Honcho stack running (verify-honcho.sh passes).

set -euo pipefail
SCRIPT_DIR="$(cd "${BASH_SOURCE[0]%/*}" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Load device-aware URLs (REQ-TOOL-108).
# shellcheck disable=SC1090
source "${REPO_ROOT}/scripts/detect-device.sh"

HERMES_CMD="${HERMES_CMD:-/home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes}"
SOUL_DIR="${SOUL_DIR:-${REPO_ROOT}/profiles/souls}"
HERMES_HOME="${HERMES_HOME:-${HOME}/.hermes}"
DRY_RUN="${DRY_RUN:-0}"
JQ=/usr/bin/jq
MODEL_DEFAULT="${MODEL_DEFAULT:-gpt-oss:120b}"
MODEL_BASE_URL="${MODEL_BASE_URL:-${GX10_BASE_URL:-http://192.168.100.1:11434/v1}}"
MODEL_API_KEY="${MODEL_API_KEY:-}"

OK=0
SKIP=0
FAIL=0

_run() {
  if [ "${DRY_RUN}" = "1" ]; then
    echo "[DRY] $*"
    return 0
  fi
  "$@"
}

# Verify required binaries.
if [ ! -x "${HERMES_CMD}" ]; then
  echo "ERROR: hermes CLI not found: ${HERMES_CMD}"
  echo "  Adjust HERMES_CMD, e.g.:"
  echo "    HERMES_CMD=/home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes bash profiles/setup.sh"
  exit 2
fi
if [ ! -x "${JQ}" ]; then
  echo "ERROR: jq not found at ${JQ}"
  exit 2
fi

# --- Step 1: Write ~/.hermes/honcho.json with correct root-level baseUrl ---
# hermes reads baseUrl from the ROOT of honcho.json, not from hosts.hermes.
# Per hermes source (client.py): base_url = raw.get("baseUrl") (root level).
# The hosts.* blocks hold per-profile identity (aiPeer, workspace, enabled).
_setup_honcho_json() {
  local honcho_json="${HERMES_HOME}/honcho.json"
  local url="${HONCHO_URL}"

  if [ "${DRY_RUN}" = "1" ]; then
    echo "[DRY] would write ${honcho_json} with baseUrl=${url} (root level)"
    return
  fi

  if [ -f "${honcho_json}" ]; then
    local existing_url
    existing_url=$("${JQ}" -r '.baseUrl // ""' "${honcho_json}" 2>/dev/null)
    if [ "${existing_url}" = "${url}" ]; then
      echo "[OK]   honcho.json already configured (baseUrl=${url})"
      return
    fi
    echo "  updating root baseUrl: ${existing_url:-<none>} -> ${url}"
    local tmp
    tmp=$(/usr/bin/mktemp)
    "${JQ}" --arg url "${url}" '.baseUrl = $url' "${honcho_json}" > "${tmp}" && /bin/mv "${tmp}" "${honcho_json}"
  else
    "${JQ}" -n \
      --arg url "${url}" \
      '{"baseUrl": $url, "hosts": {"hermes": {"workspace": "work", "enabled": true}}}' \
      > "${honcho_json}"
  fi
  echo "[OK]   honcho.json configured (baseUrl=${url})"
}

# Resolve SOUL.md path for a profile id.
# infra-* agents share a single infra-SOUL.md (1:N mapping per spec).
_soul_path() {
  local id="$1"
  local exact="${SOUL_DIR}/${id}-SOUL.md"
  [ -f "${exact}" ] && { echo "${exact}"; return; }
  if [[ "${id}" == infra-* ]]; then
    local fallback="${SOUL_DIR}/infra-SOUL.md"
    [ -f "${fallback}" ] && { echo "${fallback}"; return; }
  fi
  echo ""
}

# Create one hermes profile, override workspace if needed, copy SOUL.md.
# Args: <profile_id> <workspace>
_create_profile() {
  local id="$1"
  local workspace="$2"
  echo "--- ${id} (workspace=${workspace}) ---"

  # Create profile. --no-skills skips bundled skill download (#13 handles inoculation).
  local create_out
  if [ "${DRY_RUN}" = "1" ]; then
    echo "[DRY] hermes profile create ${id} --no-skills"
    OK=$((OK + 1))
  elif create_out=$("${HERMES_CMD}" profile create "${id}" --no-skills 2>&1); then
    echo "  [OK]   created: ${id}"
    OK=$((OK + 1))
  else
    if echo "${create_out}" | /usr/bin/grep -qi "already exist\|already created\|already a profile"; then
      echo "  [SKIP] already exists: ${id}"
      SKIP=$((SKIP + 1))
    else
      echo "  [FAIL] ${create_out}"
      FAIL=$((FAIL + 1))
      return
    fi
  fi

  # Write/update the profile host block in honcho.json.
  # hermes reads aiPeer from hosts.<key>.aiPeer (falls back to host key if absent).
  # baseUrl is read from root level (not per-host).
  # aiPeer uses underscore convention (ra_us, not ra-us) to match the frozen data contract.
  local honcho_json="${HERMES_HOME}/honcho.json"
  local host_key="hermes_${id}"
  local peer_id="${id//-/_}"  # ra-us -> ra_us (data contract: underscore)
  if [ -f "${honcho_json}" ] && [ "${DRY_RUN}" != "1" ]; then
    local current_ws current_peer
    current_ws=$("${JQ}" -r --arg k "${host_key}" '.hosts[$k].workspace // ""' "${honcho_json}" 2>/dev/null)
    current_peer=$("${JQ}" -r --arg k "${host_key}" '.hosts[$k].aiPeer // ""' "${honcho_json}" 2>/dev/null)
    if [ "${current_ws}" = "${workspace}" ] && [ "${current_peer}" = "${peer_id}" ]; then
      echo "  [OK]   honcho host block already correct"
    else
      local tmp
      tmp=$(/usr/bin/mktemp)
      "${JQ}" \
        --arg k "${host_key}" \
        --arg ws "${workspace}" \
        --arg peer "${peer_id}" \
        '.hosts[$k] = (.hosts[$k] // {}) | .hosts[$k].aiPeer = $peer | .hosts[$k].workspace = $ws | .hosts[$k].enabled = true' \
        "${honcho_json}" > "${tmp}" && /bin/mv "${tmp}" "${honcho_json}"
      echo "  [OK]   honcho host block: aiPeer=${peer_id}, workspace=${workspace}"
    fi
  fi

  # Set memory.provider = honcho in the profile-specific config.yaml.
  # Each profile has its own HERMES_HOME, so config.yaml must be patched per-profile.
  local profile_dir="${HERMES_HOME}/profiles/${id}"
  if [ "${DRY_RUN}" = "1" ]; then
    echo "[DRY] HERMES_HOME=${profile_dir} hermes config set memory.provider honcho"
    echo "[DRY] HERMES_HOME=${profile_dir} hermes config set model.default ${MODEL_DEFAULT}"
    echo "[DRY] HERMES_HOME=${profile_dir} hermes config set model.provider custom"
    echo "[DRY] HERMES_HOME=${profile_dir} hermes config set model.base_url ${MODEL_BASE_URL}"
    [ -n "${MODEL_API_KEY}" ] && echo "[DRY] HERMES_HOME=${profile_dir} hermes config set model.api_key <redacted>"
  elif [ -d "${profile_dir}" ]; then
    HERMES_HOME="${profile_dir}" "${HERMES_CMD}" config set memory.provider honcho 2>&1 | /usr/bin/grep -v "^$" || true
    # Model config must be set per-profile: profiles don't inherit from base ~/.hermes/config.yaml.
    HERMES_HOME="${profile_dir}" "${HERMES_CMD}" config set model.default "${MODEL_DEFAULT}" 2>&1 | /usr/bin/grep -v "^$" || true
    HERMES_HOME="${profile_dir}" "${HERMES_CMD}" config set model.provider custom 2>&1 | /usr/bin/grep -v "^$" || true
    HERMES_HOME="${profile_dir}" "${HERMES_CMD}" config set model.base_url "${MODEL_BASE_URL}" 2>&1 | /usr/bin/grep -v "^$" || true
    if [ -n "${MODEL_API_KEY}" ]; then
      HERMES_HOME="${profile_dir}" "${HERMES_CMD}" config set model.api_key "${MODEL_API_KEY}" 2>&1 | /usr/bin/grep -v "^$" || true
    fi
  fi

  # Copy project SOUL.md over the freshly-created profile's default SOUL.md.
  local soul
  soul=$(_soul_path "${id}")
  if [ -n "${soul}" ]; then
    if [ -d "${profile_dir}" ] || [ "${DRY_RUN}" = "1" ]; then
      _run /bin/cp "${soul}" "${profile_dir}/SOUL.md"
      echo "  [OK]   SOUL.md <- ${soul##*/}"
    else
      echo "  [WARN] profile dir not found: ${profile_dir} (SOUL.md not copied)"
    fi
  else
    echo "  [WARN] no SOUL.md found for ${id} in ${SOUL_DIR}"
  fi
}

# --- Main ---
echo "=== RA Profile Setup (SPEC-RA-TOOL-001) ==="
echo "hermes  : ${HERMES_CMD}"
echo "honcho  : ${HONCHO_URL}"
echo "souls   : ${SOUL_DIR}"
echo ""

echo "--- honcho.json setup ---"
_setup_honcho_json

echo ""
echo "--- Phase 1: work workspace (RA + operations) ---"
for id in ra-us ra-eu ra-kr op-manager n8n-manager; do
  _create_profile "${id}" "work"
done

echo ""
echo "--- Phase 2: infra workspace ---"
for id in infra-t3610 infra-gx10 infra-rpi; do
  _create_profile "${id}" "infra"
done

echo ""
echo "=== ${OK} created, ${SKIP} skipped, ${FAIL} failed ==="
[ "${FAIL}" -eq 0 ] && exit 0 || exit 1
