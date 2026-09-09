#!/usr/bin/env bash
# 1회 실행: 패치 적용 → 브랜치 push → 이슈 #148 등록 → 이슈 번호를 SPEC에 반영
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
git checkout -q -b feat/hive-v2.1 2>/dev/null || git checkout -q feat/hive-v2.1
git am --3way "${1:-0001-hive-v2.1.patch}"
python3 tools/validate_events.py virtual-office/mock/events-v2.1.jsonl
git push -u origin feat/hive-v2.1
N=$(gh issue create --repo holee9/ra-hermes-multi-agent --title "[HIVE] 이벤트 계약 v2.1 — 화행·홉 상한·단일 기록자·서킷 브레이커" --body-file docs/issues/148-hive-v2.1.md --label hive 2>/dev/null | grep -oE '[0-9]+$')
echo "issue #$N"
sed -i "s/related_issues: \[148\]/related_issues: [$N]/" .moai/specs/SPEC-HIVE-001/spec.md
git mv docs/issues/148-hive-v2.1.md "docs/issues/$N-hive-v2.1.md" 2>/dev/null || true
git commit -qam "docs(#$N): SPEC-HIVE-001 이슈 번호 반영" && git push -q
echo "done — feat/hive-v2.1 pushed, issue #$N"
