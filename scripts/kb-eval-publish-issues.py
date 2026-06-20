#!/usr/bin/env python3
"""Publish KB eval checksheets as GitHub evaluation issues.

Each iteration Markdown file becomes one GitHub issue whose title is explicitly
marked as evaluation work, not a defect/bug issue.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "kb-eval-checksheets"
START_MARKER = "<!-- kb_eval_issue_links:start -->"
END_MARKER = "<!-- kb_eval_issue_links:end -->"


@dataclass(frozen=True)
class PublishedIssue:
    iteration: int
    title: str
    number: int
    url: str
    path: Path
    created: bool


def run(cmd: list[str], *, input_text: str | None = None) -> str:
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(cmd)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result.stdout.strip()


def repo_slug() -> str:
    data = json.loads(run(["gh", "repo", "view", "--json", "nameWithOwner"]))
    return str(data["nameWithOwner"])


def date_from_dir(path: Path) -> str:
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", path.name):
        return path.name
    raise ValueError(f"input directory must be a date folder: {path}")


def iteration_from_path(path: Path) -> int:
    match = re.fullmatch(r"iteration-(\d+)\.md", path.name)
    if not match:
        raise ValueError(f"not an iteration file: {path}")
    return int(match.group(1))


def title_for(run_date: str, iteration: int) -> str:
    return f"[EVAL][평가] KB Eval {run_date} Iteration {iteration:02d}"


def issue_body(path: Path, run_date: str, iteration: int, repo: str) -> str:
    rel = path.relative_to(ROOT)
    original = path.read_text(encoding="utf-8").rstrip()
    return "\n".join([
        "This is an evaluation checklist, not a defect report.",
        "",
        f"- Evaluation date: `{run_date}`",
        f"- Iteration: `{iteration:02d}`",
        f"- Source Markdown: `{rel}`",
        f"- Repository: `{repo}`",
        "",
        "Reviewer instruction:",
        "",
        "- For each case, check exactly one score.",
        "- Check only the fast checks that are true.",
        "- Add a correction note only when needed.",
        "- The checked issue body can be ingested later as `score_given` feedback.",
        "",
        "---",
        "",
        original,
        "",
    ])


def list_existing_eval_issues() -> dict[str, dict[str, Any]]:
    out = run([
        "gh",
        "issue",
        "list",
        "--state",
        "all",
        "--search",
        '"[EVAL][평가] KB Eval" in:title',
        "--json",
        "number,title,state,url",
        "--limit",
        "200",
    ])
    issues = json.loads(out or "[]")
    return {str(issue["title"]): issue for issue in issues}


def create_issue(title: str, body: str) -> dict[str, Any]:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as tmp:
        tmp.write(body)
        tmp_path = Path(tmp.name)
    try:
        url = run(["gh", "issue", "create", "--title", title, "--body-file", str(tmp_path)])
    finally:
        tmp_path.unlink(missing_ok=True)
    match = re.search(r"/issues/(\d+)$", url)
    if not match:
        raise RuntimeError(f"could not parse issue number from gh output: {url}")
    return {
        "number": int(match.group(1)),
        "title": title,
        "state": "OPEN",
        "url": url,
    }


def render_links(issues: list[PublishedIssue]) -> str:
    lines = [
        START_MARKER,
        "",
        "## GitHub Evaluation Issues",
        "",
        "These issues are evaluation checklists, not defect reports. Use the GitHub checkboxes for quick review.",
        "",
    ]
    for issue in sorted(issues, key=lambda item: item.iteration):
        lines.append(
            f"- Iteration {issue.iteration:02d}: [#{issue.number}]({issue.url}) "
            f"`{issue.title}`"
        )
    lines.extend(["", END_MARKER, ""])
    return "\n".join(lines)


def update_date_readme(date_dir: Path, issues: list[PublishedIssue]) -> None:
    readme = date_dir / "README.md"
    original = readme.read_text(encoding="utf-8") if readme.exists() else f"# KB Eval Checklists - {date_dir.name}\n"
    block = render_links(issues)
    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}\n?",
        re.DOTALL,
    )
    if pattern.search(original):
        updated = pattern.sub(block, original).rstrip() + "\n"
    else:
        updated = original.rstrip() + "\n\n" + block
    readme.write_text(updated, encoding="utf-8")


def publish(date_dir: Path, execute: bool, update_readme: bool) -> list[PublishedIssue]:
    run_date = date_from_dir(date_dir)
    repo = repo_slug()
    existing = list_existing_eval_issues()
    published: list[PublishedIssue] = []

    for path in sorted(date_dir.glob("iteration-*.md")):
        iteration = iteration_from_path(path)
        title = title_for(run_date, iteration)
        created = False
        issue = existing.get(title)
        if issue is None:
            body = issue_body(path, run_date, iteration, repo)
            if execute:
                issue = create_issue(title, body)
                created = True
            else:
                issue = {
                    "number": 0,
                    "title": title,
                    "state": "DRY_RUN",
                    "url": "",
                }
        published.append(
            PublishedIssue(
                iteration=iteration,
                title=title,
                number=int(issue["number"]),
                url=str(issue["url"]),
                path=path,
                created=created,
            )
        )

    if execute and update_readme:
        update_date_readme(date_dir, published)
    return published


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date-dir", default=None, help="Date folder, e.g. docs/kb-eval-checksheets/2026-06-20")
    parser.add_argument("--execute", action="store_true", help="Create missing GitHub issues.")
    parser.add_argument("--no-update-readme", action="store_true", help="Do not update the date README with issue links.")
    args = parser.parse_args()

    date_dir = Path(args.date_dir) if args.date_dir else max(
        (path for path in DEFAULT_INPUT.iterdir() if path.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", path.name)),
        key=lambda item: item.name,
    )
    if not date_dir.is_absolute():
        date_dir = ROOT / date_dir
    issues = publish(date_dir, execute=args.execute, update_readme=not args.no_update_readme)
    print(json.dumps([
        {
            "iteration": issue.iteration,
            "title": issue.title,
            "number": issue.number,
            "url": issue.url,
            "created": issue.created,
        }
        for issue in issues
    ], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
