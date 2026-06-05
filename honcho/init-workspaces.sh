#!/usr/bin/env bash
# Honcho workspace 초기화: work + infra 생성
# 실행: ./init-workspaces.sh (Honcho API :8000 기동 후)

set -euo pipefail

HONCHO_URL="${HONCHO_URL:-http://localhost:8000}"

wait_for_api() {
  echo "Waiting for Honcho API at ${HONCHO_URL}..."
  i=0
  while [ $i -lt 30 ]; do
    if /usr/bin/curl -sf "${HONCHO_URL}/health" > /dev/null 2>&1; then
      echo "API ready."
      return
    fi
    /bin/sleep 2
    i=$((i + 1))
  done
  echo "ERROR: Honcho API not reachable after 60s" >&2
  exit 1
}

create_workspace() {
  local name="$1"
  echo "Creating workspace: ${name}"
  # Honcho v3 API: POST /v3/workspaces (no app concept)
  /usr/bin/curl -sf -X POST "${HONCHO_URL}/v3/workspaces" \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"${name}\"}" \
    || echo "  (workspace '${name}' may already exist — skipping)"
}

wait_for_api
create_workspace "work"
create_workspace "infra"
echo "Done. Workspaces: work, infra"
