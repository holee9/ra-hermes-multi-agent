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
    knowledge_fetch.py
    index_github_repos.py
    index_ra_knowledge.py
    nas_indexer_v2.py
    growth-metrics.py
    meta_extractor.py
    extract_mail_qa.py
)

for f in "${SCRIPTS_TO_SYNC[@]}"; do
    src="${SCRIPT_DIR}/${f}"
    dst="${TARGET}/scripts/${f}"
    if [[ ! -f "$src" ]]; then
        echo "  SKIP (not in repo): $f"
        continue
    fi
    if $DRY_RUN; then
        echo "  [dry-run] cp $src → $dst"
    else
        /bin/cp "$src" "$dst"
        echo "  OK: $f"
    fi
done

# hermes-api-server.py also lives at TARGET root (service entry point)
if $DRY_RUN; then
    echo "  [dry-run] cp hermes-api-server.py → $TARGET/hermes-api-server.py"
else
    /bin/cp "${SCRIPT_DIR}/hermes-api-server.py" "${TARGET}/hermes-api-server.py"
    echo "  OK: hermes-api-server.py (root copy updated)"
fi

echo ""
echo "=== Restart service? ==="
echo "  sudo systemctl restart hermes-api-server"
echo "  sudo systemctl status hermes-api-server --no-pager"
