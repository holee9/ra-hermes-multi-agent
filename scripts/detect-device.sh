#!/usr/bin/env bash
# detect-device.sh — Resolve which physical RA Hermes machine this session runs on.
#
# WHY: git-tracked files are shared across T3610 / GX10 / RPi / dev boxes, so they
# cannot encode "which device am I". This reads a git-UNTRACKED runtime signal (the
# live hostname) and maps it to device identity + device-aware service URLs.
#
# Selection priority (first match wins):
#   1. RA_DEVICE env override (explicit)
#   2. hostname substring match against scripts/device-map.json
#   3. "unknown" fallback (assumes remote services, destructive = UNSAFE)
#
# Any URL env var already set in the environment WINS over the map ([IF] pattern).
#
# Usage:
#   source scripts/detect-device.sh        # exports RA_DEVICE, HONCHO_URL, ... into the shell
#   bash   scripts/detect-device.sh --print # prints the resolved profile (also exports, then exits)
#   RA_DEVICE=gx10 source scripts/detect-device.sh   # force a device

# NOTE: intentionally no `set -e`/`set -u` at top level — this file is meant to be
# sourced, and those would leak into and disrupt the caller's shell.

__dd_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
__dd_map="${RA_DEVICE_MAP:-${__dd_script_dir}/device-map.json}"

__dd_fail() { echo "detect-device: $*" >&2; }

if ! command -v jq >/dev/null 2>&1; then
  __dd_fail "jq is required but not found on PATH"
  return 1 2>/dev/null || exit 1
fi
if [ ! -f "${__dd_map}" ]; then
  __dd_fail "device map not found: ${__dd_map}"
  return 1 2>/dev/null || exit 1
fi

# 1) Resolve device id.
__dd_device=""
if [ -n "${RA_DEVICE:-}" ]; then
  __dd_device="${RA_DEVICE}"
else
  __dd_host_lc="$(hostname 2>/dev/null | tr '[:upper:]' '[:lower:]')"
  while IFS= read -r __dd_d; do
    [ "${__dd_d}" = "unknown" ] && continue
    while IFS= read -r __dd_pat; do
      [ -z "${__dd_pat}" ] && continue
      case "${__dd_host_lc}" in
        *"${__dd_pat}"*) __dd_device="${__dd_d}"; break ;;
      esac
    done < <(jq -r --arg d "${__dd_d}" '.devices[$d].hostname_patterns[]?' "${__dd_map}")
    [ -n "${__dd_device}" ] && break
  done < <(jq -r '.devices | keys[]' "${__dd_map}")
fi
[ -z "${__dd_device}" ] && __dd_device="unknown"

# Validate the device exists in the map; otherwise fall back.
if ! jq -e --arg d "${__dd_device}" '.devices[$d]' "${__dd_map}" >/dev/null 2>&1; then
  __dd_fail "device '${__dd_device}' not in map; using 'unknown'"
  __dd_device="unknown"
fi

__dd_get() { jq -r --arg d "${__dd_device}" --arg k "$1" '.devices[$d].urls[$k] // empty' "${__dd_map}"; }
# Note: use an explicit null check (not `//`) — jq's `//` treats boolean false as
# absent, which would corrupt the honcho_local / destructive_is_production flags.
__dd_attr() { jq -r --arg d "${__dd_device}" --arg k "$1" '.devices[$d][$k] | if . == null then "" else . end' "${__dd_map}"; }

# 2) Export identity + device-aware URLs (env value wins if already set).
export RA_DEVICE="${__dd_device}"
export RA_DEVICE_ROLE="$(__dd_attr role)"
export RA_HONCHO_LOCAL="$(__dd_attr honcho_local)"
export RA_DESTRUCTIVE_IS_PROD="$(__dd_attr destructive_is_production)"
export HONCHO_URL="${HONCHO_URL:-$(__dd_get honcho)}"
export GX10_URL="${GX10_URL:-$(__dd_get gx10)}"
export POSTGRES_URL="${POSTGRES_URL:-$(__dd_get postgres)}"
export OPENPROJECT_URL="${OPENPROJECT_URL:-$(__dd_get openproject)}"
export N8N_URL="${N8N_URL:-$(__dd_get n8n)}"

__dd_print() {
  cat <<EOF
RA Hermes — Device Detection
  device    : ${RA_DEVICE}  (role: ${RA_DEVICE_ROLE})
  hostname  : $(hostname 2>/dev/null)
  honcho    : ${HONCHO_URL}   (honcho_local: ${RA_HONCHO_LOCAL})
  gx10      : ${GX10_URL}
  postgres  : ${POSTGRES_URL}
  openproj  : ${OPENPROJECT_URL}
  n8n       : ${N8N_URL}
  destructive_is_production: ${RA_DESTRUCTIVE_IS_PROD}
EOF
  if [ "${RA_DEVICE}" = "unknown" ]; then
    echo "  WARNING: device unrecognized — services assumed REMOTE, destructive ops treated as UNSAFE." >&2
  fi
}

# 3) Decide whether to print: if executed directly, or --print/--help passed.
__dd_sourced=0
# shellcheck disable=SC2128
if [ -n "${BASH_SOURCE:-}" ] && [ "${BASH_SOURCE[0]}" != "${0}" ]; then __dd_sourced=1; fi

case "${1:-}" in
  -h|--help)
    grep '^#' "${BASH_SOURCE[0]:-$0}" | sed 's/^# \{0,1\}//'
    ;;
  --print)
    __dd_print
    ;;
  *)
    [ "${__dd_sourced}" -eq 0 ] && __dd_print
    ;;
esac

# Clean up internal vars when sourced (keep the exported RA_*/*_URL ones).
unset __dd_script_dir __dd_map __dd_device __dd_host_lc __dd_d __dd_pat __dd_sourced 2>/dev/null
unset -f __dd_fail __dd_get __dd_attr __dd_print 2>/dev/null
return 0 2>/dev/null || exit 0
