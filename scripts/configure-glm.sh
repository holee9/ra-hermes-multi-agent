#!/usr/bin/env bash
# Configure existing Hermes profiles to use GLM through an OpenAI-compatible API.
#
# Defaults target Z.ai GLM-5.2 general API. For GLM Coding Plan, set:
#   GLM_BASE_URL=https://api.z.ai/api/coding/paas/v4
#
# This script does not print API keys. By default it stores the key in each
# profile config only when WRITE_API_KEY=1 is set. Otherwise export OPENAI_API_KEY
# in the runtime environment that launches Hermes.

set -euo pipefail

SCRIPT_DIR="$(cd "${BASH_SOURCE[0]%/*}" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

HERMES_CMD="${HERMES_CMD:-/home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes}"
HERMES_HOME="${HERMES_HOME:-${HOME}/.hermes}"
GLM_MODEL="${GLM_MODEL:-glm-5.2}"
GLM_BASE_URL="${GLM_BASE_URL:-https://api.z.ai/api/paas/v4}"
GLM_API_KEY="${GLM_API_KEY:-${ZAI_API_KEY:-${Z_AI_API_KEY:-}}}"
WRITE_API_KEY="${WRITE_API_KEY:-0}"
DRY_RUN="${DRY_RUN:-0}"

PROFILES="${PROFILES:-ra-us ra-eu ra-kr op-manager n8n-manager infra-t3610 infra-gx10 infra-rpi}"

if [ ! -x "${HERMES_CMD}" ]; then
  echo "ERROR: hermes CLI not found: ${HERMES_CMD}" >&2
  exit 2
fi

run_config_set() {
  local profile_dir="$1"
  local key="$2"
  local value="$3"

  if [ "${DRY_RUN}" = "1" ]; then
    if [ "${key}" = "model.api_key" ]; then
      echo "[DRY] HERMES_HOME=${profile_dir} hermes config set ${key} <redacted>"
    else
      echo "[DRY] HERMES_HOME=${profile_dir} hermes config set ${key} ${value}"
    fi
    return
  fi

  HERMES_HOME="${profile_dir}" "${HERMES_CMD}" config set "${key}" "${value}" \
    2>&1 | /usr/bin/grep -v "^$" || true
}

echo "=== GLM profile configuration ==="
echo "model    : ${GLM_MODEL}"
echo "base_url : ${GLM_BASE_URL}"
echo "profiles : ${PROFILES}"
if [ -n "${GLM_API_KEY}" ]; then
  if [ "${WRITE_API_KEY}" = "1" ]; then
    echo "api_key  : present; will write to local profile config"
  else
    echo "api_key  : present; not writing because WRITE_API_KEY!=1"
  fi
else
  echo "api_key  : missing; set GLM_API_KEY or ZAI_API_KEY before testing"
fi
echo ""

for profile in ${PROFILES}; do
  profile_dir="${HERMES_HOME}/profiles/${profile}"
  if [ ! -d "${profile_dir}" ]; then
    echo "[SKIP] profile not found: ${profile}"
    continue
  fi

  echo "--- ${profile} ---"
  run_config_set "${profile_dir}" memory.provider honcho
  run_config_set "${profile_dir}" model.default "${GLM_MODEL}"
  run_config_set "${profile_dir}" model.provider custom
  run_config_set "${profile_dir}" model.base_url "${GLM_BASE_URL}"
  if [ "${WRITE_API_KEY}" = "1" ] && [ -n "${GLM_API_KEY}" ]; then
    run_config_set "${profile_dir}" model.api_key "${GLM_API_KEY}"
  fi
done

echo ""
echo "Done."
if [ "${WRITE_API_KEY}" != "1" ]; then
  echo "Runtime requirement: export OPENAI_API_KEY=\"\${GLM_API_KEY}\" before running Hermes."
fi
