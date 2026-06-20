#!/usr/bin/env python3
"""Generate KB-derived human review checksheets under docs/.

The output is intentionally Markdown so reviewers can commit checked boxes as
audit history before the checked cases are ingested as score_given feedback.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import random
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import psycopg2


ROOT = Path(__file__).resolve().parents[1]
DAILY_RUNNER = ROOT / "scripts" / "daily-growth-runner.py"
DEFAULT_OUTPUT = ROOT / "docs" / "kb-eval-checksheets"
DEFAULT_TZ = os.environ.get("AUTO_GROWTH_OPERATION_TZ", "Asia/Seoul")


def load_daily_runner() -> Any:
    spec = importlib.util.spec_from_file_location("daily_growth_runner", DAILY_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load {DAILY_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def operational_today(timezone_name: str) -> date:
    return datetime.now(ZoneInfo(timezone_name)).date()


def parse_date(value: str | None, timezone_name: str) -> date:
    if value:
        return datetime.strptime(value, "%Y-%m-%d").date()
    return operational_today(timezone_name)


def checkbox(label: str, checked: bool = False) -> str:
    mark = "x" if checked else " "
    return f"- [{mark}] {label}"


def case_metadata(base_date: date, iteration: int, agent: Any, case_index: int, case: Any) -> dict[str, Any]:
    decision_ref = f"kb-eval-{base_date.strftime('%Y%m%d')}-it{iteration:02d}-{agent.peer_id}-{case_index:03d}"
    return {
        "decision_ref": decision_ref,
        "base_date": base_date.isoformat(),
        "iteration": iteration,
        "agent": agent.peer_id,
        "profile_id": agent.profile_id,
        "scenario_id": case.scenario_id,
        "source": case.source_path,
        "source_hash": case.source_hash,
        "matched_keywords": list(case.matched_keywords),
    }


def render_case(base_date: date, iteration: int, agent: Any, case_index: int, case: Any) -> str:
    meta = case_metadata(base_date, iteration, agent, case_index, case)
    focus = agent.daily_focus[(base_date.toordinal() + iteration - 1) % len(agent.daily_focus)]
    lines = [
        f"### {meta['decision_ref']}",
        "",
        f"<!-- kb_eval_case {json.dumps(meta, ensure_ascii=False, sort_keys=True)} -->",
        "",
        f"- Agent: `{agent.peer_id}` / {agent.name} ({agent.region})",
        f"- Scenario: `{case.scenario_id}`",
        f"- Source: `{case.source_path}`",
        f"- Source hash: `{case.source_hash}`",
        f"- Focus: {focus}",
        f"- Matched keywords: {', '.join(case.matched_keywords) or 'source routing match'}",
        "",
        "**Reviewer Score**",
        "",
        checkbox("Score 3 - pass / usable without correction"),
        checkbox("Score 2 - usable with minor correction"),
        checkbox("Score 1 - correction required"),
        "",
        "**Fast Checks**",
        "",
        checkbox("Match correct"),
        checkbox("Evidence supported"),
        checkbox("Source cited"),
        checkbox("No hallucination"),
        checkbox("Escalation appropriate"),
        checkbox("Human correction needed"),
        "",
        "**Optional Correction Note**",
        "",
        ">",
        "",
        "**Source Excerpts**",
        "",
    ]
    for idx, excerpt in enumerate(case.excerpts, start=1):
        lines.extend([
            f"{idx}. Chunk `{excerpt['id']}`",
            "",
            f"> {excerpt['excerpt']}",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def render_iteration(base_date: date, iteration: int, cases_by_agent: dict[str, list[tuple[Any, Any]]]) -> str:
    total = sum(len(items) for items in cases_by_agent.values())
    lines = [
        f"# KB Eval Checksheet - {base_date.isoformat()} Iteration {iteration:02d}",
        "",
        "Reviewer workflow:",
        "",
        "1. Check exactly one score per case.",
        "2. Mark the fast checks that are true.",
        "3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.",
        "4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.",
        "",
        f"Total cases: {total}",
        "",
    ]
    for agent_peer, items in cases_by_agent.items():
        lines.extend([f"## {agent_peer}", ""])
        for case_index, (agent, case) in enumerate(items, start=1):
            lines.append(render_case(base_date, iteration, agent, case_index, case))
    return "\n".join(lines).rstrip() + "\n"


def render_index(base_date: date, iterations: list[int], cases_per_agent: int, selection_mode: str) -> str:
    lines = [
        f"# KB Eval Checklists - {base_date.isoformat()}",
        "",
        "This folder stores human review checksheets generated from the current RA knowledge base.",
        "Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.",
        "",
        f"- Iterations: {len(iterations)}",
        f"- Cases per agent per iteration: {cases_per_agent}",
        f"- Expected total cases: {len(iterations) * cases_per_agent * 3}",
        f"- Latest generation mode: {selection_mode}",
        "",
        "Files:",
        "",
    ]
    for iteration in iterations:
        lines.append(f"- [Iteration {iteration:02d}](iteration-{iteration:02d}.md)")
    return "\n".join(lines) + "\n"


def select_cases(
    daily: Any,
    conn: Any,
    agent: Any,
    run_date: date,
    cases_per_agent: int,
    source_pool: int,
    max_chunks: int,
    rng: random.Random | None,
) -> list[Any]:
    if rng is None:
        return daily.select_daily_cases(
            conn=conn,
            agent=agent,
            run_date=run_date,
            cases_per_agent=cases_per_agent,
            source_pool=source_pool,
            max_chunks=max_chunks,
        )

    paths = daily.fetch_source_paths(conn, agent, source_pool)
    rng.shuffle(paths)
    cases: list[Any] = []
    for source_path in paths:
        chunks = daily.fetch_source_chunks(conn, source_path, max_chunks)
        if not chunks:
            continue
        matched = daily.find_matches(
            source_path + " " + " ".join(str(chunk.get("metadata", "")) for chunk in chunks),
            agent.keywords,
        )
        excerpts = tuple(
            {"id": str(chunk.get("id", "")), "excerpt": daily.compact_text(chunk.get("content", ""))}
            for chunk in chunks
        )
        cases.append(
            daily.SourceCase(
                scenario_id=daily.scenario_id_for(run_date, agent, source_path),
                source_path=source_path,
                source_hash=daily.source_hash(chunks),
                chunk_count=len(chunks),
                matched_keywords=matched,
                excerpts=excerpts,
            )
        )
        if len(cases) >= cases_per_agent:
            break
    return cases


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="Base operation date, YYYY-MM-DD. Defaults to today in operation timezone.")
    parser.add_argument("--operation-timezone", default=DEFAULT_TZ)
    parser.add_argument("--iterations", type=int, default=3)
    parser.add_argument("--start-iteration", type=int, default=1)
    parser.add_argument("--cases-per-agent", type=int, default=5)
    parser.add_argument("--source-pool", type=int, default=60)
    parser.add_argument("--max-chunks-per-case", type=int, default=2)
    parser.add_argument("--randomize", action="store_true", help="Shuffle source candidates per agent/iteration.")
    parser.add_argument("--random-seed", default=None, help="Optional deterministic seed for randomize mode.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args()

    pg_dsn = os.environ.get("POSTGRES_URL")
    if not pg_dsn:
        raise SystemExit("POSTGRES_URL is required")
    if args.iterations < 1:
        raise SystemExit("--iterations must be >= 1")
    if args.start_iteration < 1:
        raise SystemExit("--start-iteration must be >= 1")
    if args.cases_per_agent < 1:
        raise SystemExit("--cases-per-agent must be >= 1")

    daily = load_daily_runner()
    daily.validate_agent_config()
    base_date = parse_date(args.date, args.operation_timezone)
    out_root = Path(args.output_dir) / base_date.isoformat()
    out_root.mkdir(parents=True, exist_ok=True)

    agents = list(daily.AGENTS.values())
    rng = random.Random(args.random_seed) if args.randomize else None
    written_iterations: list[int] = []
    with psycopg2.connect(pg_dsn) as conn:
        for iteration in range(args.start_iteration, args.start_iteration + args.iterations):
            selection_date = base_date + timedelta(days=iteration - 1)
            cases_by_agent: dict[str, list[tuple[Any, Any]]] = {}
            for agent in agents:
                cases = select_cases(
                    daily=daily,
                    conn=conn,
                    agent=agent,
                    run_date=selection_date,
                    cases_per_agent=args.cases_per_agent,
                    source_pool=args.source_pool,
                    max_chunks=args.max_chunks_per_case,
                    rng=rng,
                )
                cases_by_agent[agent.peer_id] = [(agent, case) for case in cases]
            path = out_root / f"iteration-{iteration:02d}.md"
            path.write_text(render_iteration(base_date, iteration, cases_by_agent), encoding="utf-8")
            written_iterations.append(iteration)

    existing_iterations = sorted(
        int(path.stem.split("-")[-1])
        for path in out_root.glob("iteration-*.md")
        if path.stem.split("-")[-1].isdigit()
    )
    (out_root / "README.md").write_text(
        render_index(
            base_date,
            existing_iterations,
            args.cases_per_agent,
            "random" if args.randomize else "deterministic rotation",
        ),
        encoding="utf-8",
    )
    print(f"wrote iterations {written_iterations} to {out_root.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
