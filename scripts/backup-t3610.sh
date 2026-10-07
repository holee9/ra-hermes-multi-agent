#!/usr/bin/env bash
# backup-t3610.sh — T3610 운영 데이터 백업 (Honcho pg_dump / Qdrant snapshot / /opt 설정)
#
# 사용:  backup-t3610.sh daily    # Honcho 덤프 + /opt 설정 (매일 04:30, 7세대)
#        backup-t3610.sh weekly   # Qdrant 스냅샷 (일요일 05:00, 1세대)
#        backup-t3610.sh verify-restore <dump.gpg>   # 임시 Postgres에 복원해 행수 비교
#
# 설계 근거: 2026-10-07 승인 설계안. 모든 산출물은 gpg AES-256 대칭 암호화 후 NAS에 저장
# (CIFS는 파일 권한이 0755로 고정되어 평문 보관 불가). 순환은 "새 세대 기록 → 검증 → 가장 오래된 세대 삭제".
set -euo pipefail

NAS_ROOT="${NAS_ROOT:-/mnt/nas-ra/backup/t3610}"
PASS_FILE="${PASS_FILE:-/home/abyz-lab/.keys/t3610-backup.passphrase}"
LOG_DIR="${LOG_DIR:-/var/log/t3610-backup}"
STATUS_FILE="$LOG_DIR/last-status.txt"
PG_CONTAINER="${PG_CONTAINER:-honcho-postgres-1}"
QDRANT_URL="${QDRANT_URL:-http://127.0.0.1:6333}"
QDRANT_SNAP_HOST_DIR="${QDRANT_SNAP_HOST_DIR:-/opt/hermes-ra/qdrant_storage/snapshots}"
QDRANT_COLLECTIONS="${QDRANT_COLLECTIONS:-nas_ra_docs ra_kb_markdown}"
OPT_DIR="${OPT_DIR:-/opt/hermes-ra}"
KEEP_DAILY="${KEEP_DAILY:-7}"
KEEP_WEEKLY="${KEEP_WEEKLY:-1}"
TS="$(date +%Y%m%d-%H%M%S)"

mkdir -p "$LOG_DIR"
log() { echo "[$(date '+%F %T')] $*" | tee -a "$LOG_DIR/backup.log"; }
fail() { log "ERROR: $*"; echo "FAIL $TS $*" > "$STATUS_FILE"; exit 1; }

[ -r "$PASS_FILE" ] || fail "passphrase file missing: $PASS_FILE"
mountpoint -q "$(dirname "$NAS_ROOT")/.." 2>/dev/null || mountpoint -q /mnt/nas-ra || fail "NAS not mounted"
mkdir -p "$NAS_ROOT"/{honcho,qdrant,opt}

enc() { gpg --batch --yes --quiet --symmetric --cipher-algo AES256 --passphrase-file "$PASS_FILE" -o "$2" "$1"; }
dec_to() { gpg --batch --yes --quiet --decrypt --passphrase-file "$PASS_FILE" -o "$2" "$1"; }

rotate() { # rotate <dir> <glob> <keep>
  local dir="$1" glob="$2" keep="$3"
  ls -1t "$dir"/$glob 2>/dev/null | tail -n +"$((keep + 1))" | while read -r old; do
    log "rotate: removing $old"; rm -f "$old" "$old.sha256"
  done
}

backup_honcho() {
  local tmp; tmp="$(mktemp -d /tmp/t3610bk.XXXXXX)"
  local dump="$tmp/honcho-$TS.dump"
  log "honcho: pg_dump start"
  # -Z 6: 실측 4.3GB(무압축) → 1.7GB(압축). 소요 약 6분.
  docker exec "$PG_CONTAINER" pg_dump -U honcho -d honcho -Fc -Z 6 > "$dump"
  log "honcho: dump $(du -h "$dump" | cut -f1); verifying with pg_restore --list"
  # custom 포맷은 탐색 가능한 파일이 필요 → 임시 디렉터리를 마운트해 검증
  local img; img="$(docker inspect "$PG_CONTAINER" --format '{{.Config.Image}}')"
  docker run --rm -v "$tmp":/d:ro "$img" pg_restore --list "/d/$(basename "$dump")" | grep -q 'TABLE DATA' || fail "honcho: pg_restore --list failed"
  enc "$dump" "$dump.gpg"
  sha256sum "$dump.gpg" | awk '{print $1}' > "$dump.gpg.sha256"
  cp "$dump.gpg" "$dump.gpg.sha256" "$NAS_ROOT/honcho/"
  local remote="$NAS_ROOT/honcho/$(basename "$dump.gpg")"
  [ "$(sha256sum "$remote" | awk '{print $1}')" = "$(cat "$dump.gpg.sha256")" ] || fail "honcho: NAS copy checksum mismatch"
  log "honcho: stored $remote ($(du -h "$remote" | cut -f1))"
  rm -rf "$tmp"
  rotate "$NAS_ROOT/honcho" 'honcho-*.dump.gpg' "$KEEP_DAILY"
}

backup_opt() {
  local tmp; tmp="$(mktemp -d /tmp/t3610bk.XXXXXX)"
  local tar="$tmp/opt-hermes-ra-$TS.tar"
  log "opt: tar $OPT_DIR (excluding qdrant_storage, indexer_state.db, __pycache__)"
  # *.bak*: 과거 수동 백업 사본(일부 root 600이라 읽기 불가). 현재 설정·스크립트만 보관 대상.
  tar -C "$(dirname "$OPT_DIR")" --exclude='hermes-ra/qdrant_storage' --exclude='hermes-ra/indexer_state.db' --exclude='__pycache__' --exclude='*.bak*' -cf "$tar" "$(basename "$OPT_DIR")"
  enc "$tar" "$tar.gpg"
  sha256sum "$tar.gpg" | awk '{print $1}' > "$tar.gpg.sha256"
  cp "$tar.gpg" "$tar.gpg.sha256" "$NAS_ROOT/opt/"
  local remote="$NAS_ROOT/opt/$(basename "$tar.gpg")"
  [ "$(sha256sum "$remote" | awk '{print $1}')" = "$(cat "$tar.gpg.sha256")" ] || fail "opt: NAS copy checksum mismatch"
  log "opt: stored $remote ($(du -h "$remote" | cut -f1))"
  rm -rf "$tmp"
  rotate "$NAS_ROOT/opt" 'opt-hermes-ra-*.tar.gpg' "$KEEP_DAILY"
}

backup_qdrant() {
  for c in $QDRANT_COLLECTIONS; do
    # 이전 실행이 실패해 남긴 스냅샷이 있으면 재사용(55GB 재생성 19분 절약), 없으면 새로 생성
    local name
    name="$(curl -sf "$QDRANT_URL/collections/$c/snapshots" | python3 -c 'import json,sys;r=json.load(sys.stdin)["result"];print(sorted(r,key=lambda s:s["creation_time"] or "")[-1]["name"] if r else "")')" || name=""
    if [ -n "$name" ]; then log "qdrant: reusing existing snapshot $name"; else
      log "qdrant: creating snapshot $c"
      name="$(curl -sf -X POST "$QDRANT_URL/collections/$c/snapshots" | python3 -c 'import json,sys;print(json.load(sys.stdin)["result"]["name"])')" || fail "qdrant: snapshot API failed for $c"
    fi
    # 스냅샷 파일은 컨테이너(root) 소유라 호스트 사용자가 못 읽음 → 컨테이너 안에서 스트리밍
    local cpath="/qdrant/storage/snapshots/$c/$name"
    docker exec qdrant test -f "$cpath" || fail "qdrant: snapshot file not found in container: $cpath"
    local src_sha; src_sha="$(docker exec qdrant cat "$cpath.checksum" 2>/dev/null | awk '{print $1}')"
    local out="$NAS_ROOT/qdrant/$c-$TS.snapshot.gpg"
    log "qdrant: $c snapshot $(docker exec qdrant du -h "$cpath" | cut -f1) -> encrypt+copy to NAS"
    local plain_sha_file; plain_sha_file="$(mktemp)"
    docker exec qdrant cat "$cpath" \
      | tee >(sha256sum | awk '{print $1}' > "$plain_sha_file") \
      | gpg --batch --yes --quiet --symmetric --cipher-algo AES256 --passphrase-file "$PASS_FILE" -o - \
      | tee "$out" | sha256sum | awk '{print $1}' > "$out.sha256"
    sync; sleep 1
    local plain_sha; plain_sha="$(cat "$plain_sha_file")"; rm -f "$plain_sha_file"
    local out_size; out_size="$(stat -c %s "$out")"
    [ "$out_size" -gt 1000000 ] || fail "qdrant: encrypted output too small ($out_size bytes) for $c"
    if [ -n "$src_sha" ]; then
      [ "$plain_sha" = "$src_sha" ] || fail "qdrant: plaintext sha256 mismatch vs Qdrant .checksum for $c"
      log "qdrant: source checksum verified ($c)"
    else
      log "qdrant: WARN no .checksum file for $c; plaintext sha256=$plain_sha recorded"
    fi
    echo "$plain_sha" > "$out.plain.sha256"
    log "qdrant: stored $out ($(du -h "$out" | cut -f1))"
    # 로컬 스냅샷은 Qdrant API로 삭제(디스크 55GB 회수)
    curl -sf -X DELETE "$QDRANT_URL/collections/$c/snapshots/$name" >/dev/null || log "qdrant: WARN local snapshot delete failed ($name)"
    rotate "$NAS_ROOT/qdrant" "$c-*.snapshot.gpg" "$KEEP_WEEKLY"
  done
}

verify_restore() { # verify_restore <dump.gpg>
  local gpgf="$1" tmp; tmp="$(mktemp -d /tmp/t3610rs.XXXXXX)"
  local dump="$tmp/restore.dump" cname="t3610-restore-test-$$"
  log "verify-restore: decrypting $gpgf"
  dec_to "$gpgf" "$dump"
  local img; img="$(docker inspect "$PG_CONTAINER" --format '{{.Config.Image}}')"
  docker run -d --rm --name "$cname" -e POSTGRES_PASSWORD=restoretest -e POSTGRES_USER=honcho -e POSTGRES_DB=honcho "$img" >/dev/null
  for _ in $(seq 1 30); do docker exec "$cname" pg_isready -U honcho >/dev/null 2>&1 && break; sleep 2; done
  docker cp "$dump" "$cname:/tmp/restore.dump"
  docker exec "$cname" pg_restore -U honcho -d honcho --no-owner --no-privileges /tmp/restore.dump || log "verify-restore: pg_restore returned non-zero (extensions/owners may warn)"
  local q="select relname, n_live_tup from pg_stat_user_tables where relname in ('messages','documents','ra_knowledge','sessions') order by 1"
  docker exec "$cname" psql -U honcho -d honcho -Atc "analyze" >/dev/null
  echo "table|restored|source"
  paste -d'|' <(docker exec "$cname" psql -U honcho -d honcho -Atc "$q" | tr '|' ' ' | awk '{print $1"|"$2}') <(docker exec "$PG_CONTAINER" psql -U honcho -d honcho -Atc "$q" | awk -F'|' '{print $2}')
  docker stop "$cname" >/dev/null; rm -rf "$tmp"
}

case "${1:-}" in
  daily)  backup_honcho; backup_opt; echo "OK $TS daily" > "$STATUS_FILE"; log "daily done" ;;
  weekly) backup_qdrant; echo "OK $TS weekly" > "$STATUS_FILE"; log "weekly done" ;;
  opt-only) backup_opt; echo "OK $TS opt-only" > "$STATUS_FILE"; log "opt-only done" ;;
  verify-restore) [ -n "${2:-}" ] || fail "usage: verify-restore <dump.gpg>"; verify_restore "$2" ;;
  *) echo "usage: $0 {daily|weekly|verify-restore <dump.gpg>}"; exit 2 ;;
esac
