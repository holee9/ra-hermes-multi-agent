#!/bin/bash
# connect-kb.sh — Verify and set up knowledge base paths for Hermes RA agents
#
# This script checks that ra-project and MD-process are accessible at the paths
# referenced in SOUL.md routing tables, and optionally fixes the ra-project clone.
#
# Run: bash profiles/scripts/connect-kb.sh [--fix]
#   --fix : if ra-project is wrong, back up and re-clone from GitHub

set -e

RA_PROJECT_PATH="/home/abyz-lab/work/workspace-github/holee9/ra-project"
MD_PROCESS_PATH="/home/abyz-lab/work/workspace-github/holee9/MD-process"
RA_PROJECT_EXPECTED_MARKER="01_규제지식베이스"
FIX_MODE=false

[[ "$1" == "--fix" ]] && FIX_MODE=true

echo "=== Hermes RA Knowledge Base Connection Check ==="

# --- MD-process ---
echo ""
echo "[1/2] MD-process check: $MD_PROCESS_PATH"
if [[ -d "$MD_PROCESS_PATH/$RA_PROJECT_EXPECTED_MARKER" ]] || [[ -d "$MD_PROCESS_PATH/01_법규_규제" ]]; then
    echo "  ✅ MD-process accessible (01_법규_규제 found)"
    DIRS=$(ls "$MD_PROCESS_PATH" 2>/dev/null | /usr/bin/wc -l)
    echo "  Top-level dirs: $DIRS"
else
    echo "  ❌ MD-process NOT found at expected path"
    echo "     Fix: git clone https://github.com/holee9/MD-process.git $MD_PROCESS_PATH"
fi

# --- ra-project ---
echo ""
echo "[2/2] ra-project check: $RA_PROJECT_PATH"
if [[ -d "$RA_PROJECT_PATH/$RA_PROJECT_EXPECTED_MARKER" ]]; then
    echo "  ✅ ra-project accessible (01_규제지식베이스 found)"
    DIRS=$(ls "$RA_PROJECT_PATH" 2>/dev/null | /usr/bin/wc -l)
    echo "  Top-level dirs: $DIRS"
else
    # Check what's actually there
    if [[ -d "$RA_PROJECT_PATH/.git" ]]; then
        REMOTE=$(git -C "$RA_PROJECT_PATH" remote get-url origin 2>/dev/null || echo "unknown")
        echo "  ⚠️  ra-project exists but is wrong repo (remote: $REMOTE)"
    elif [[ ! -d "$RA_PROJECT_PATH" ]]; then
        echo "  ❌ ra-project NOT found at expected path"
    fi

    if $FIX_MODE; then
        BACKUP_PATH="${RA_PROJECT_PATH}-hermes-bak"
        echo "  → --fix mode: backing up to $BACKUP_PATH"
        mv "$RA_PROJECT_PATH" "$BACKUP_PATH"
        echo "  → Cloning holee9/ra-project ..."
        git clone https://github.com/holee9/ra-project.git "$RA_PROJECT_PATH"
        echo "  ✅ ra-project re-cloned"
    else
        echo ""
        echo "  Fix (manual steps):"
        echo "    mv $RA_PROJECT_PATH ${RA_PROJECT_PATH}-hermes-bak"
        echo "    git clone https://github.com/holee9/ra-project.git $RA_PROJECT_PATH"
        echo "  Or run: bash profiles/scripts/connect-kb.sh --fix"
    fi
fi

echo ""
echo "=== SOUL.md routing table paths ==="
echo "  ra-kr: $RA_PROJECT_PATH + $MD_PROCESS_PATH"
echo "  ra-us: $RA_PROJECT_PATH + $MD_PROCESS_PATH"
echo "  ra-eu: $RA_PROJECT_PATH + $MD_PROCESS_PATH"
echo ""
echo "Done. Agents can query these paths directly once both are accessible."
