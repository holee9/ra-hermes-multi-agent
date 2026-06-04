#!/usr/bin/env bash
# Honcho workspace 초기화: work + infra 생성
# 실행: ./init-workspaces.sh (Honcho API :8000 기동 후)

set -euo pipefail

HONCHO_URL="${HONCHO_URL:-http://localhost:8000}"
APP_NAME="${HONCHO_APP_NAME:-ra-hermes}"

wait_for_api() {
  echo "Waiting for Honcho API at ${HONCHO_URL}..."
  for i in $(seq 1 30); do
    if curl -sf "${HONCHO_URL}/health" > /dev/null 2>&1; then
      echo "API ready."
      return
    fi
    sleep 2
  done
  echo "ERROR: Honcho API not reachable after 60s" >&2
  exit 1
}

create_workspace() {
  local name="$1"
  echo "Creating workspace: ${name}"
  curl -sf -X POST "${HONCHO_URL}/v1/apps/${APP_NAME}/workspaces" \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"${name}\"}" \
    || echo "  (workspace '${name}' may already exist — skipping)"
}

wait_for_api
create_workspace "work"
create_workspace "infra"
echo "Done. Workspaces: work, infra"
