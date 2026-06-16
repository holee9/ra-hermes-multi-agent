#!/usr/bin/env bash
# deploy-n8n-rpi.sh — n8n 워크플로우 RPi 배포 스크립트
#
# 사전 조건:
#   1. SSH 접근 가능: ssh abyz-lab@10.20.6.187
#   2. n8n Global Variables 설정 완료 (아래 env 섹션 참조)
#   3. Gmail OAuth2 자격증명 설정 (mail-triage용)
#
# 사용법:
#   bash scripts/deploy-n8n-rpi.sh [RPI_SSH_ALIAS]
#
# 기본값: RPI_SSH=raspi5p (SSH config alias for 10.20.6.187)

set -euo pipefail

RPI_SSH="${1:-raspi5p}"  # SSH config alias (User raspi5p, Host 10.20.6.187, IdentityFile ~/.ssh/id_ed25519)
N8N_CONTAINER="n8n-stack-n8n-1"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORKFLOWS_DIR="${REPO_ROOT}/n8n/workflows"

log() { echo "[$(date '+%H:%M:%S')] $*"; }
fail() { echo "[ERROR] $*" >&2; exit 1; }

# ── 1. SSH 연결 확인 ─────────────────────────────────────────────────────────
log "RPi SSH 연결 확인: ${RPI_SSH}"
ssh -o ConnectTimeout=10 -o BatchMode=yes "${RPI_SSH}" "echo OK" \
    || fail "SSH 접근 불가. 키 등록 또는 패스워드 인증 확인 필요."
log "SSH OK"

# ── 2. n8n 컨테이너 상태 확인 ─────────────────────────────────────────────
log "n8n 컨테이너 상태 확인"
ssh "${RPI_SSH}" "docker ps --filter name=${N8N_CONTAINER} --format '{{.Status}}'" \
    | grep -q "Up" || fail "n8n 컨테이너(${N8N_CONTAINER})가 실행 중이 아닙니다."
log "n8n 컨테이너 실행 중"

# ── 3. 필수 환경변수 확인 ────────────────────────────────────────────────
log "n8n 필수 환경변수 확인"
HONCHO_URL=$(ssh "${RPI_SSH}" \
    "docker exec ${N8N_CONTAINER} env 2>/dev/null | grep HONCHO_API_URL | cut -d= -f2" || echo "")
HONCHO_WS=$(ssh "${RPI_SSH}" \
    "docker exec ${N8N_CONTAINER} env 2>/dev/null | grep HONCHO_WORK_WORKSPACE | cut -d= -f2" || echo "")
HERMES_URL=$(ssh "${RPI_SSH}" \
    "docker exec ${N8N_CONTAINER} env 2>/dev/null | grep HERMES_API_URL | cut -d= -f2" || echo "")
API_SERVER_KEY=$(ssh "${RPI_SSH}" \
    "docker exec ${N8N_CONTAINER} env 2>/dev/null | grep API_SERVER_KEY | cut -d= -f2" || echo "")
OPENPROJECT_URL=$(ssh "${RPI_SSH}" \
    "docker exec ${N8N_CONTAINER} env 2>/dev/null | grep OPENPROJECT_API_URL | cut -d= -f2" || echo "")
YELLOW_THRESHOLD=$(ssh "${RPI_SSH}" \
    "docker exec ${N8N_CONTAINER} env 2>/dev/null | grep YELLOW_CONFIDENCE_THRESHOLD | cut -d= -f2" || echo "")

if [ -z "$HONCHO_URL" ] || [ -z "$HONCHO_WS" ] || [ -z "$HERMES_URL" ] || [ -z "$API_SERVER_KEY" ] || [ -z "$OPENPROJECT_URL" ] || [ -z "$YELLOW_THRESHOLD" ]; then
    echo ""
    echo "⚠️  n8n Global Variables 또는 컨테이너 환경변수 설정 필요:"
    echo "   n8n 관리자 UI → Settings → Global Variables 에서 등록:"
    echo "     HONCHO_API_URL       = http://10.20.6.140:8000"
    echo "     HONCHO_WORK_WORKSPACE = ra-hermes"
    echo "     HERMES_API_URL       = http://10.20.6.140:8643"
    echo "     API_SERVER_KEY       = <hermes-api-server key>"
    echo "     OPENPROJECT_API_URL  = http://<openproject-host>:8080"
    echo "     YELLOW_CONFIDENCE_THRESHOLD = 0.70"
    echo "   또는 docker-compose .env / n8n_CUSTOM_ENV 환경변수로 주입"
    echo ""
    echo "  설정 후 이 스크립트를 다시 실행하세요."
    fail "필수 환경변수 미설정"
fi
log "HONCHO_API_URL=${HONCHO_URL}, HONCHO_WORK_WORKSPACE=${HONCHO_WS}"
log "HERMES_API_URL=${HERMES_URL}, OPENPROJECT_API_URL=${OPENPROJECT_URL}, YELLOW_CONFIDENCE_THRESHOLD=${YELLOW_THRESHOLD}"

# ── 4. Honcho 연결 테스트 (RPi → T3610) ──────────────────────────────────
log "Honcho API 연결 테스트 (RPi → T3610)"
HONCHO_STATUS=$(ssh "${RPI_SSH}" \
    "curl -sf -o /dev/null -w '%{http_code}' -X POST '${HONCHO_URL}/v3/workspaces/list' -H 'Content-Type: application/json' -d '{\"page\":1,\"page_size\":5}'" || echo "000")
[ "$HONCHO_STATUS" = "200" ] || [ "$HONCHO_STATUS" = "422" ] \
    || fail "Honcho 응답 없음 (${HONCHO_STATUS}). T3610 Honcho 서버 상태 확인 필요."
log "Honcho 연결 OK (HTTP ${HONCHO_STATUS})"

# ── 4a. Hermes API / Layer 4 연결 테스트 ────────────────────────────────
log "Hermes API / Layer 4 연결 테스트 (RPi → T3610)"
HERMES_STATUS=$(ssh "${RPI_SSH}" \
    "curl -sf -o /dev/null -w '%{http_code}' -H 'Authorization: Bearer ${API_SERVER_KEY}' '${HERMES_URL}/v1/models'" || echo "000")
[ "$HERMES_STATUS" = "200" ] || fail "Hermes API 응답 없음 (${HERMES_STATUS}). HERMES_API_URL/API_SERVER_KEY 확인 필요."
log "Hermes API 연결 OK (HTTP ${HERMES_STATUS})"

LAYER4_STATUS=$(ssh "${RPI_SSH}" \
    "curl -sf -o /dev/null -w '%{http_code}' -X POST '${HERMES_URL}/v1/knowledge/fetch' -H 'Content-Type: application/json' -H 'Authorization: Bearer ${API_SERVER_KEY}' -d '{\"query\":\"FDA 510(k) predicate\",\"model\":\"ra_us\",\"top\":1}'" || echo "000")
[ "$LAYER4_STATUS" = "200" ] || fail "Layer 4 조회 엔드포인트 응답 없음 (${LAYER4_STATUS}). hermes-api-server.py 배포 상태 확인 필요."
log "Layer 4 조회 엔드포인트 OK (HTTP ${LAYER4_STATUS})"

# ── 5. 워크플로우 파일 전송 ────────────────────────────────────────────────
WORKFLOWS=("feedback-recorder.json" "infra-to-work-bridge.json" "infra-vote-broadcast.json" "mail-triage.json")
WORKFLOW_IDS=("iBzjnDJ7KRb93EOF" "DVldSLZ7lKwcBXML" "infraVoteBroadcast001" "4B9bDkXgH0HFjP7o")
log "워크플로우 파일 전송 (${#WORKFLOWS[@]}개)"
for wf in "${WORKFLOWS[@]}"; do
    scp "${WORKFLOWS_DIR}/${wf}" "${RPI_SSH}:/tmp/${wf}"
    ssh "${RPI_SSH}" "docker cp /tmp/${wf} ${N8N_CONTAINER}:/tmp/${wf}"
    log "  전송: ${wf}"
done

# ── 6. n8n에 워크플로우 import ────────────────────────────────────────────
log "n8n 워크플로우 import 시작"
for wf in "${WORKFLOWS[@]}"; do
    ssh "${RPI_SSH}" \
        "docker exec ${N8N_CONTAINER} n8n import:workflow --input=/tmp/${wf}" \
        || fail "n8n workflow import 실패: ${wf}"
    log "  import OK: ${wf}"
done

# ── 6a. import 후 workflow 활성화 ────────────────────────────────────────
log "n8n 워크플로우 활성화"
for i in "${!WORKFLOW_IDS[@]}"; do
    wf="${WORKFLOWS[$i]}"
    wf_id="${WORKFLOW_IDS[$i]}"
    ssh "${RPI_SSH}" \
        "docker exec ${N8N_CONTAINER} n8n update:workflow --id=${wf_id} --active=true" \
        || fail "n8n workflow 활성화 실패: ${wf} (${wf_id})"
    log "  active OK: ${wf}"
done

log "n8n 컨테이너 재시작 (import/activation 반영)"
ssh "${RPI_SSH}" "cd /home/raspi5p/workspace/n8n-stack && docker compose restart n8n n8n-worker"
log "n8n public webhook readiness 대기"
for i in {1..12}; do
    if curl -sf -o /dev/null "https://n8n.abyz-lab.work/" 2>/dev/null; then
        break
    fi
    sleep 5
done
sleep 5

# ── 7. feedback-recorder webhook 동작 테스트 ──────────────────────────────
log "feedback-recorder webhook 동작 테스트"
WEBHOOK_URL="https://n8n.abyz-lab.work/webhook/feedback"
TEST_PAYLOAD='{"actor":"ra_us","score":3,"rationale":"deploy-test","decision_ref":"DEPLOY-TEST-001"}'
RESPONSE=$(curl -sf -X POST "${WEBHOOK_URL}" \
    -H "Content-Type: application/json" \
    -d "${TEST_PAYLOAD}" 2>&1 || echo "CURL_FAILED")
echo "  응답: ${RESPONSE}"
if echo "$RESPONSE" | grep -q "started\|Workflow"; then
    log "  webhook 트리거 OK"
else
    fail "feedback webhook 응답 실패: ${RESPONSE}"
fi

# ── 8. Honcho 기록 확인 (5초 대기 후) ────────────────────────────────────
log "Honcho 세션 기록 확인 (5초 대기)"
sleep 5
SESSION_COUNT=$(curl -sf -X POST "http://localhost:8000/v3/workspaces/${HONCHO_WS}/sessions/list" \
    -H "Content-Type: application/json" \
    -d '{"page":1,"page_size":5}' \
    | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d.get('items',[])))" 2>/dev/null || echo "0")
log "Honcho 세션 수: ${SESSION_COUNT}"

echo ""
echo "═══════════════════════════════════════════════"
echo " 배포 완료 요약"
echo "═══════════════════════════════════════════════"
echo " ✅ SSH 연결: ${RPI_SSH}"
echo " ✅ n8n 워크플로우 ${#WORKFLOWS[@]}개 import"
echo " ✅ feedback webhook 트리거 확인"
echo " 📊 Honcho 세션: ${SESSION_COUNT}개"
echo ""
echo " 다음 단계:"
echo "  1. n8n UI에서 mail-triage 워크플로우 Gmail OAuth 설정"
echo "  2. mail-triage test webhook으로 high/low/parse/closed-WP/Layer4 시나리오 검증 (#37,#43,#44,#45)"
echo "  3. 가상오피스 실데이터 표시 확인 (#10)"
echo "═══════════════════════════════════════════════"
