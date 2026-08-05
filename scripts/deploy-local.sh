#!/usr/bin/env bash
# deploy-local.sh — sync git repo scripts to /opt/hermes-ra/ on T3610
#
# Run after committing changes to scripts/ to propagate to the live runtime.
# Safe: never touches .env, qdrant_storage, or skills/.
#
# Usage: bash scripts/deploy-local.sh [--dry-run]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
TARGET=/opt/hermes-ra

DRY_RUN=false
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=true
INSTALL_BIN="/usr/bin/install"

# Per-destination privilege resolution (#139). The previous logic set ONE global
# sudo prefix when either destination was unwritable, so an unwritable
# $TARGET/scripts forced sudo onto the root-copy install too. Under a sandbox
# that sets no_new_privs, sudo cannot escalate at all and the whole deploy
# failed — including the root copy, which is the actual service entry point and
# IS directly writable. Resolve per destination directory instead, and report a
# skip explicitly rather than failing the run silently.
SKIPPED_FILES=()

# Echoes the command prefix needed to write into $1: nothing when directly
# writable, "sudo" when sudo can escalate, "UNAVAILABLE" when neither.
resolve_prefix() {
    local dir="$1"
    if [[ -w "$dir" ]]; then
        echo ""
    elif sudo -n true 2>/dev/null; then
        echo "sudo"
    else
        echo "UNAVAILABLE"
    fi
}

install_file() {
    local src="$1" dst="$2" label="$3"
    local prefix
    prefix=$(resolve_prefix "$(dirname "$dst")")
    if [[ "$prefix" == "UNAVAILABLE" ]]; then
        echo "  SKIP (no write permission, sudo unavailable): $label → $dst" >&2
        SKIPPED_FILES+=("$label")
        return 0
    fi
    if $DRY_RUN; then
        echo "  [dry-run] ${prefix:+$prefix }$INSTALL_BIN -m 0644 $label → $dst"
        return 0
    fi
    if [[ -n "$prefix" ]]; then
        "$prefix" "$INSTALL_BIN" -m 0644 "$src" "$dst"
    else
        "$INSTALL_BIN" -m 0644 "$src" "$dst"
    fi
    echo "  OK: $label → $dst"
}

if [[ ! -d "$TARGET" ]]; then
    echo "ERROR: $TARGET not found. This script is for T3610 only." >&2
    exit 1
fi

# Confirm device
if ! /bin/hostname | /usr/bin/grep -qi "T3610"; then
    echo "WARNING: hostname does not contain 'T3610'. Proceed on this machine? (y/N) " >&2
    read -r answer
    [[ "$answer" =~ ^[Yy]$ ]] || exit 1
fi

echo "=== hermes deploy: $REPO_ROOT/scripts/ → $TARGET/scripts/ ==="

# Files managed in git: scripts/ → TARGET/scripts/
SCRIPTS_TO_SYNC=(
    hermes-api-server.py
    ra_citation_lint.py
    knowledge_fetch.py
    index_github_repos.py
    index_ra_knowledge.py
    nas_indexer_v2.py
    growth-metrics.py
    meta_extractor.py
    extract_mail_qa.py
)

# Files that must ALSO sit at TARGET root, next to the service entry point.
# hermes-api-server.py loads ra_citation_lint.py by absolute path derived from
# __file__ (see #134), so the runtime resolves it at TARGET root — NOT scripts/.
# Omitting it here is what made the deploy crash the service on import (#139).
ROOT_FILES=(
    hermes-api-server.py
    ra_citation_lint.py
)

# Interpreter the systemd unit actually runs, so the smoke check exercises the
# same environment as production. Falls back to python3 when the venv is absent.
SMOKE_PYTHON=/home/abyz-lab/.hermes/hermes-agent/venv/bin/python3
[[ -x "$SMOKE_PYTHON" ]] || SMOKE_PYTHON=$(command -v python3 || true)

# Import smoke check (#139): stage the root files in a temp dir and import the
# entry point there. A missing sibling module or a syntax error fails HERE
# instead of after install, where systemd Restart=on-failure/RestartSec=5 would
# turn it into a 5-second restart loop with the advisory API fully down.
# Log paths are redirected to the temp dir so the check never writes /var/log.
smoke_check_root_files() {
    if [[ -z "$SMOKE_PYTHON" ]]; then
        echo "  SMOKE SKIP: no python3 interpreter found" >&2
        return 0
    fi
    local stage
    stage=$(mktemp -d)
    local f
    for f in "${ROOT_FILES[@]}"; do
        [[ -f "${SCRIPT_DIR}/${f}" ]] || { echo "ERROR: missing root file in repo: $f" >&2; rm -rf "$stage"; return 1; }
        cp "${SCRIPT_DIR}/${f}" "${stage}/${f}"
    done
    if ADV_REQUEST_LOG="${stage}/adv.jsonl" \
       KB_GAPS_LOG="${stage}/kb-gaps.jsonl" \
       RESPONSE_LOG="${stage}/resp.jsonl" \
       "$SMOKE_PYTHON" - "${stage}/hermes-api-server.py" <<'SMOKE'
import importlib.util, sys
spec = importlib.util.spec_from_file_location("_deploy_smoke", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
SMOKE
    then
        echo "  SMOKE OK: entry point imports cleanly with its root-level dependencies"
        rm -rf "$stage"
        return 0
    fi
    echo "ERROR: import smoke check FAILED — deploy aborted (service would crash-loop on restart)" >&2
    rm -rf "$stage"
    return 1
}

smoke_check_root_files || exit 1

for f in "${SCRIPTS_TO_SYNC[@]}"; do
    src="${SCRIPT_DIR}/${f}"
    if [[ ! -f "$src" ]]; then
        echo "  SKIP (not in repo): $f"
        continue
    fi
    install_file "$src" "${TARGET}/scripts/${f}" "$f"
done

# Service entry point + its root-level sibling modules also live at TARGET root.
# These are what systemd actually executes, so a skip here is fatal — the deploy
# would leave the entry point and its sibling module at mismatched versions.
ROOT_SKIPPED_BEFORE=${#SKIPPED_FILES[@]}
for f in "${ROOT_FILES[@]}"; do
    install_file "${SCRIPT_DIR}/${f}" "${TARGET}/${f}" "$f (root copy)"
done
if (( ${#SKIPPED_FILES[@]} > ROOT_SKIPPED_BEFORE )); then
    echo "" >&2
    echo "ERROR: the service entry point could not be installed — deploy INCOMPLETE." >&2
    echo "       Re-run from a shell that can write $TARGET (or with working sudo)." >&2
    exit 1
fi

if (( ${#SKIPPED_FILES[@]} > 0 )); then
    echo ""
    echo "=== WARNING: ${#SKIPPED_FILES[@]} file(s) skipped ==="
    for f in "${SKIPPED_FILES[@]}"; do echo "  - $f"; done
    echo "  These live under $TARGET/scripts/ (owned by another uid) and were NOT updated."
    echo "  The service entry point at $TARGET root WAS updated."
fi

echo ""
echo "=== Restart service? ==="
echo "  sudo systemctl restart hermes-api-server"
echo "  sudo systemctl status hermes-api-server --no-pager"
