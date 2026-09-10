#!/usr/bin/env python3
"""hive thread 재구성 — 세션 모델 A(#150 P3-0 (5))의 `-z <context>` 빌더.

`log.jsonl`(라우터 감사 로그)에서 한 conversation 의 스레드를 시간순으로 뽑아 hermes 일회성 호출에 넘길
문맥 문자열을 만든다. **LLM 을 부르지 않는다.** 크기(문자·줄·추정 토큰)를 함께 돌려주므로 실측 담당자가
같은 입력으로 품질·비용을 잰다. 추정 토큰은 `chars/4` 휴리스틱이며 측정값이 아니다 — 보고서에는 실측 토큰을 쓴다.

규칙
- 출처는 log.jsonl 의 확정 항목뿐이다(journal·inbox 원본 아님). conversation 이 같은 항목 + 직접 corr 로
  이어진 선행 항목을 ts 순으로 모은다.
- 대상 메시지(msg_id) 이후의 항목은 넣지 않는다(재구성 시점 기준 과거만).
- 상한: max_events(기본 12) — 넘으면 오래된 것부터 생략하고 `truncated` 로 보고한다. HOP_CAP 은 상한이 아니다.
- payload 는 그대로 JSON 직렬화한다(요약·재작성 없음). text_ref 같은 참조는 참조 그대로 둔다 — 해석은 peer 몫.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Thread:
    conversation: str | None
    target_id: str
    events: list[dict]                       # 시간순, target 포함
    context: str
    chars: int
    lines: int
    est_tokens: int                          # chars/4 — 휴리스틱, 실측 아님
    truncated: int = 0                       # 상한으로 생략된 선행 항목 수
    sources: list[str] = field(default_factory=list)   # 포함된 event id (감사용)


def _ts(ev: dict) -> str:
    return ev.get("ts") if isinstance(ev.get("ts"), str) else ""


def collect(records: list[dict], target_id: str, max_events: int = 12) -> Thread:
    by_id = {r["id"]: r for r in records if isinstance(r, dict) and isinstance(r.get("id"), str)}
    target = by_id.get(target_id)
    if target is None:
        raise KeyError(f"log 에 없는 id: {target_id}")
    conv = target.get("conversation") if isinstance(target.get("conversation"), str) else None
    picked: dict[str, dict] = {}
    if conv:
        for r in by_id.values():
            if r.get("conversation") == conv and _ts(r) <= _ts(target) and r["id"] != target_id:
                picked[r["id"]] = r
    # corr 체인 (conversation 이 없거나 다른 스레드에서 이어진 경우)
    cur = target
    while isinstance(cur.get("corr"), str) and cur["corr"] in by_id and cur["corr"] not in picked:
        cur = by_id[cur["corr"]]
        picked[cur["id"]] = cur
    prior = sorted(picked.values(), key=lambda r: (_ts(r), r["id"]))
    truncated = 0
    if len(prior) > max_events - 1:
        truncated = len(prior) - (max_events - 1)
        prior = prior[truncated:]
    events = prior + [target]
    lines = []
    if truncated:
        lines.append(f"[이전 {truncated}개 항목 생략 — 원장 {conv or 'corr-chain'} 참조]")
    for r in events:
        who = r.get("actor", "?")
        to = f" → {r['to']}" if isinstance(r.get("to"), str) else ""
        act = f" ({r['act']})" if isinstance(r.get("act"), str) else ""
        lines.append(f"[{_ts(r)}] {who}{to} {r.get('kind', '?')}{act} id={r['id']}")
        lines.append("  " + json.dumps(r.get("payload", {}), ensure_ascii=False, sort_keys=True))
    context = "\n".join(lines)
    return Thread(conv, target_id, events, context, len(context), len(lines), len(context) // 4, truncated,
                  [r["id"] for r in events])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="log.jsonl 에서 스레드 문맥을 만든다 (LLM 호출 없음)")
    ap.add_argument("log")
    ap.add_argument("msg_id")
    ap.add_argument("--max-events", type=int, default=12)
    ap.add_argument("--json", action="store_true", help="크기 보고를 JSON 으로")
    a = ap.parse_args(argv)
    records = []
    for line in Path(a.log).read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    t = collect(records, a.msg_id, a.max_events)
    if a.json:
        print(json.dumps({"conversation": t.conversation, "events": len(t.events), "truncated": t.truncated,
                          "chars": t.chars, "lines": t.lines, "est_tokens_heuristic": t.est_tokens,
                          "sources": t.sources}, ensure_ascii=False))
    else:
        print(t.context)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
