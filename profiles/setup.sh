#!/usr/bin/env bash
# profiles/setup.sh — Create/update Honcho profiles for all RA agents.
#
# REQ-TOOL-101~107 (SPEC-RA-TOOL-001)
#
# Usage:
#   bash profiles/setup.sh
#   HERMES_CMD=/usr/local/bin/hermes bash profiles/setup.sh
#
# Env vars (override defaults via [IF] pattern):
#   HERMES_CMD          hermes CLI binary (default: hermes on PATH)
#   TEMPLATE_DIR        dir with *.honcho.json.template (default: profiles/honcho-config-templates)
#   SOUL_DIR            dir with *-SOUL.md files (default: profiles/souls)
#   DRY_RUN             set to 1 to print commands without executing

set -euo pipefail
SCRIPT_DIR="$(cd "${BASH_SOURCE[0]%/*}" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# REQ-TOOL-108: load device-aware URLs first.
# shellcheck disable=SC1090
source "${REPO_ROOT}/scripts/detect-device.sh"

HERMES_CMD="${HERMES_CMD:-hermes}"
TEMPLATE_DIR="${TEMPLATE_DIR:-${REPO_ROOT}/profiles/honcho-config-templates}"
SOUL_DIR="${SOUL_DIR:-${REPO_ROOT}/profiles/souls}"
DRY_RUN="${DRY_RUN:-0}"

OK=0
SKIP=0
FAIL=0

_run() {
  if [ "${DRY_RUN}" = "1" ]; then
    echo "[DRY-RUN] $*"
  else
    "$@"
  fi
}

# Resolve SOUL.md path for an agent.
# infra-* agents share a single infra-SOUL.md (1:N mapping).
_soul_path() {
  local profile_id="$1"
  local exact="${SOUL_DIR}/${profile_id}-SOUL.md"
  if [ -f "${exact}" ]; then
    echo "${exact}"
    return
  fi
  # infra-* fallback to infra-SOUL.md
  if [[ "${profile_id}" == infra-* ]]; then
    local fallback="${SOUL_DIR}/infra-SOUL.md"
    if [ -f "${fallback}" ]; then
      echo "${fallback}"
      return
    fi
  fi
  echo ""
}

# Derive profile id from template filename.
# e.g. ra-us.honcho.json.template → ra-us
_profile_id() {
  local filename="$1"
  local base
  base=$(basename "${filename}")
  echo "${base%.honcho.json.template}"
}

# Process a single template file.
_process_template() {
  local template="$1"
  local profile_id
  profile_id=$(_profile_id "${template}")
  echo "--- ${profile_id} ---"

  # Expand env vars in template (device-specific URLs from detect-device.sh).
  local rendered_config
  rendered_config=$(envsubst < "${template}" 2>/dev/null) || {
    echo "  [FAIL] envsubst failed for ${template}"
    FAIL=$((FAIL + 1))
    return
  }

  # Write rendered config to a temp file for hermes to consume.
  local tmpfile
  tmpfile=$(mktemp /tmp/honcho-profile-XXXXXX.json)
  # shellcheck disable=SC2064
  trap "rm -f ${tmpfile}" EXIT
  echo "${rendered_config}" > "${tmpfile}"

  # Create profile (idempotent: skip if already exists per REQ-TOOL-107).
  local create_out
  if create_out=$(_run "${HERMES_CMD}" profile create "${profile_id}" --config "${tmpfile}" 2>&1); then
    echo "  [OK]   profile created: ${profile_id}"
    OK=$((OK + 1))
  else
    if echo "${create_out}" | grep -qi "already exist"; then
      echo "  [SKIP] already exists: ${profile_id}"
      SKIP=$((SKIP + 1))
    else
      echo "  [FAIL] profile create: ${create_out}"
      FAIL=$((FAIL + 1))
      return
    fi
  fi

  # Update SOUL.md if available.
  local soul_path
  soul_path=$(_soul_path "${profile_id}")
  if [ -n "${soul_path}" ]; then
    if _run "${HERMES_CMD}" profile update "${profile_id}" --soul "${soul_path}" 2>&1; then
      echo "  [OK]   soul updated: $(basename "${soul_path}")"
    else
      echo "  [FAIL] soul update failed for ${profile_id}"
      FAIL=$((FAIL + 1))
    fi
  else
    echo "  [WARN] no SOUL.md for ${profile_id} (skipping soul update)"
  fi
}

# Verify hermes CLI is available.
if ! command -v "${HERMES_CMD}" >/dev/null 2>&1; then
  echo "ERROR: hermes CLI not found at '${HERMES_CMD}'"
  echo "  Set HERMES_CMD to the correct path, e.g.:"
  echo "    HERMES_CMD=/usr/local/bin/hermes bash profiles/setup.sh"
  exit 2
fi

echo "=== Profile Setup (SPEC-RA-TOOL-001) ==="
echo "hermes: $(command -v "${HERMES_CMD}")"
echo "templates: ${TEMPLATE_DIR}"
echo "souls:     ${SOUL_DIR}"
echo ""

# Iterate all template files.
# Using /usr/bin/find for T3610 PATH compatibility (REQ absolute paths).
while IFS= read -r template; do
  _process_template "${template}"
done < <(/usr/bin/find "${TEMPLATE_DIR}" -maxdepth 1 -name "*.honcho.json.template" | sort)

echo ""
echo "=== ${OK} created, ${SKIP} skipped, ${FAIL} failed ==="

[ "${FAIL}" -eq 0 ] && exit 0 || exit 1
