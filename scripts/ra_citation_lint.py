"""Code-level regulatory-citation linter for RA advisory output (#134 option B).

Background
---------
#123 fixed top-level Annex/Rule labels via the ra-eu persona reference table;
#132 fixed IEC/Article/GSPR labels the same way. Each fix worked *inside its
table's coverage*, but fabrication kept relocating to whatever the table did not
cover (#134: 4 consecutive rounds). A curated table cannot win a race against an
open sub-identifier space by enumeration alone. This module adds the
complementary code-level check the persona table cannot: a deterministic pass
over the generated text.

What ships (C1) and what does not (C2) — a measured decision
------------------------------------------------------------
Two checks were designed and both were measured offline against the real
2026-07-19 ra_eu batch (15 captured model responses) BEFORE shipping:

  C1  nonexistent article sub-paragraph — e.g. "Art.86(1)(d)" when Art.86(1)
      has only (a)(b)(c). Purely STRUCTURAL: it asks "can this sub-identifier
      exist?", never "is it near the right subject?". Table-safe.
      MEASUREMENT: 2 flags on the batch, both true (the #133 KB-source-error
      propagation), zero false positives. -> SHIPPED, severity "error"
      (the live path hard-gates on it, like the #118 unverified_identifier gate).

  C2  subject<->citation same-kind mismatch — e.g. "SSCP ... Art.66" when SSCP
      is Art.32. SEMANTIC: it must pair a subject with its citation by text
      proximity. MEASUREMENT: 107 flags (all-in-window) -> 76 (nearest-only) ->
      10 (prose-only, tables stripped); inspection showed even the final 10 are
      false positives (list/sentence boundaries, and over-strict "Annex XIV" vs
      "Annex XIV Part A"). Regulatory drafts are table- and list-dense, so
      character-proximity cannot reliably pair a subject with ITS citation. A
      viable semantic check would need real structure parsing (a larger effort
      with uncertain payoff). -> NOT SHIPPED. The code is retained below as a
      documented negative result so a future attempt does not repeat it.

Strategic finding for #134: code-level verification cleanly solves the
STRUCTURAL sub-class (nonexistent identifiers) but not the SEMANTIC one
(right identifier, wrong subject). The semantic sub-class stays with the
persona table + human review.

Purity: no network, no external dependencies, no imports beyond `re`.
Every registry value is verified against EUR-Lex CELEX:32017R0745.
"""
from __future__ import annotations

import re

SEV_ERROR = "error"
SEV_WARNING = "warning"


# ── C1 registry: article -> paragraph -> set of existing sub-point letters ──
# Only articles whose exact sub-structure is verified against EUR-Lex are
# listed. An article absent here is never C1-flagged (missing entry == "unknown
# structure", which must stay silent, not error).
#
# Art.86(1) (PSUR contents): (a) benefit-risk conclusions, (b) main PMCF
# findings, (c) volume of sales + population estimate. No (d)/(e).
_ARTICLE_SUBPOINTS: dict[str, dict[str, frozenset[str]]] = {
    "86": {"1": frozenset({"a", "b", "c"})},
}

# "Art.86(1)(d)", "Article 86 (1)(d)", "Art 86(1)(d)".
_ARTICLE_SUBPOINT_RE = re.compile(
    r"\bart(?:icle|\.)?\s*(\d{1,3})\s*\(\s*(\d{1,2})\s*\)\s*\(\s*([a-z])\s*\)",
    re.IGNORECASE,
)


def _c1(text: str) -> list[dict]:
    flags: list[dict] = []
    for match in _ARTICLE_SUBPOINT_RE.finditer(text):
        art, para, letter = match.group(1), match.group(2), match.group(3).lower()
        paras = _ARTICLE_SUBPOINTS.get(art)
        if not paras or para not in paras:
            continue  # unknown structure -> stay silent
        valid = paras[para]
        if letter not in valid:
            listed = "/".join(f"({x})" for x in sorted(valid))
            flags.append({
                "check": "C1",
                "severity": SEV_ERROR,
                "message": (
                    f"Art.{art}({para})({letter}) does not exist — "
                    f"Art.{art}({para}) has only {listed}."
                ),
                "span": match.group(0),
            })
    return flags


def lint_citations(text: str | None) -> list[dict]:
    """Return citation flags for `text` (the shipped check == C1 only).

    Each flag: {"check", "severity", "message", "span"}. Empty list == no
    structural contradiction found. This is a registry-contradiction check, not
    proof of correctness: an article whose structure the registry does not know
    is left alone (silent), never asserted correct.
    """
    if not text:
        return []
    return _c1(text)


def has_error(flags: list[dict]) -> bool:
    """True if any flag is severity error (the tier the live path hard-gates on)."""
    return any(f.get("severity") == SEV_ERROR for f in flags)


# ─────────────────────────────────────────────────────────────────────────────
# C2 — RETAINED NEGATIVE RESULT, NOT WIRED INTO lint_citations().
#
# @MX:DEBT: proximity-based subject<->citation matching, measured non-viable.
# @MX:CEILING: usable only on single-clause prose with one subject + one
#   citation; breaks on the tables/lists that dominate real advisory output.
# @MX:UPGRADE: replace character-proximity with markdown-table-row / sentence
#   structural parsing before enabling; re-measure FP on a live batch and only
#   then consider wiring into lint_citations. See #134.
#
# Kept so the exact design and its measured failure are recoverable; callers
# who want to re-measure invoke lint_subject_citation_experimental() directly.
# ─────────────────────────────────────────────────────────────────────────────

_SUBJECT_GOLD: list[tuple[str, frozenset[tuple[str, str]]]] = [
    (r"summary of safety and clinical performance|\bsscp\b", frozenset({("art", "32")})),
    (r"declaration of conformity|\bdoc\b", frozenset({("art", "19"), ("annex", "iv")})),
    (r"clinical evaluation report|\bcer\b", frozenset({("annex", "xiv part a"), ("art", "61")})),
    (r"\bpmcf\b|post-?market clinical follow-?up", frozenset({("annex", "xiv part b")})),
    (r"\bpsur\b|periodic safety update report", frozenset({("art", "86")})),
    (r"pms system", frozenset({("art", "83")})),
    (r"pms plan", frozenset({("art", "84")})),
    (r"serious incident|field safety corrective action|\bfsca\b|vigilance report", frozenset({("art", "87")})),
    (r"trend report", frozenset({("art", "88")})),
    (r"products? without an intended medical purpose", frozenset({("annex", "xvi")})),
    (r"\blabel(?:ing|ling)?\b|instructions for use", frozenset({("annex", "i")})),
    (r"risk management", frozenset({("annex", "i")})),
]
_SUBJECT_GOLD_COMPILED = [(re.compile(pat, re.IGNORECASE), gold) for pat, gold in _SUBJECT_GOLD]

_CITATION_RE = re.compile(
    r"\b(?:art(?:icle|\.)?\s*(?P<artnum>\d{1,3})"
    r"|annex\s+(?P<roman>[ivx]{1,5})(?:\s+part\s+(?P<part>[ab]))?)\b",
    re.IGNORECASE,
)
_PROXIMITY = 45


def _norm_citation(match: re.Match) -> tuple[str, str] | None:
    if match.group("artnum"):
        return ("art", match.group("artnum"))
    roman = (match.group("roman") or "").lower()
    if not roman:
        return None
    part = (match.group("part") or "").lower()
    return ("annex", f"{roman} part {part}".strip() if part else roman)


def _render(cite: tuple[str, str]) -> str:
    kind, val = cite
    if kind == "art":
        return f"Art.{val}"
    return "Annex " + val.upper().replace(" PART ", " Part ")


def lint_subject_citation_experimental(text: str | None) -> list[dict]:
    """EXPERIMENTAL / NOT SHIPPED — see the C2 negative-result note above.

    Pairs each subject occurrence with the nearest same-kind citation within a
    window and flags a mismatch against the gold registry. Measured to produce
    a high false-positive rate on real (table/list-dense) advisory text. Present
    for re-measurement only; not called by lint_citations().
    """
    if not text:
        return []
    flags: list[dict] = []
    citations = [(mt.start(), mt.end(), _norm_citation(mt), mt.group(0))
                 for mt in _CITATION_RE.finditer(text)]
    citations = [c for c in citations if c[2] is not None]
    seen: set[tuple[int, str]] = set()
    for subj_re, gold in _SUBJECT_GOLD_COMPILED:
        gold_kinds = {kind for kind, _ in gold}
        for sm in subj_re.finditer(text):
            s0, s1 = sm.start(), sm.end()
            nearest: dict[str, tuple[int, tuple[str, str], str]] = {}
            for c0, c1, cite, raw in citations:
                kind = cite[0]
                if kind not in gold_kinds:
                    continue
                dist = c0 - s1 if c0 >= s1 else s0 - c1
                if dist > _PROXIMITY:
                    continue
                if kind not in nearest or dist < nearest[kind][0]:
                    nearest[kind] = (dist, cite, raw)
            for kind, (_dist, cite, raw) in nearest.items():
                if cite in gold:
                    continue
                key = (sm.start(), cite[1])
                if key in seen:
                    continue
                seen.add(key)
                want = ", ".join(_render(g) for g in sorted(gold) if g[0] == kind)
                flags.append({
                    "check": "C2",
                    "severity": SEV_WARNING,
                    "message": f'"{sm.group(0)}" is cited to {_render(cite)}, but its reference is {want}.',
                    "span": raw,
                })
    return flags
