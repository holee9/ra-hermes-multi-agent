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
    """Return citation flags for `text` (shipped checks: C1 + C3).

    Each flag: {"check", "severity", "message", "span"}. Empty list == no
    structural contradiction found. This is a registry-contradiction check, not
    proof of correctness: an article whose structure the registry does not know
    is left alone (silent), never asserted correct.

    C3 (Art. 52 class<->paragraph) was wired in 2026-10-28 after offline
    measurement on every captured batch 2026-07-15..2026-10-28: 2 flags, both
    true positives (Class IIb cited with 52(1)), zero false positives, and a
    unit-expectation suite of 11 representative lines.
    """
    if not text:
        return []
    return _c1(text) + _art52_class(text)


def has_error(flags: list[dict]) -> bool:
    """True if any flag is severity error (the tier the live path hard-gates on)."""
    return any(f.get("severity") == SEV_ERROR for f in flags)


# ─────────────────────────────────────────────────────────────────────────────
# C3 — MDR Art. 52 class<->paragraph consistency (#134, 2026-10-28).
#
# Motivating measurement: 2026-10-28 batch — the check was designed and
# measured BEFORE wiring (the #134 measured-deployment doctrine), and that
# process caught a critical authoring error: the first draft registry was
# built from a search-summary mapping (52(1)=I, 52(5)=IIa, 52(7)=III) that
# was WRONG and produced 97 false positives across the 2026-10-19..28
# captured batches. The registry below is the verified mapping (primary
# text: medical-device-regulation.eu Article 52 page, corroborated by the
# CMI notified-body procedure doc and consistent with every correct corpus
# response):
#   52(1)-(2) general obligations (placing on market / putting into service)
#   52(3) Class III · 52(4) Class IIb (+ per-device assessment for IIb
#   implantables) · 52(5) Class IIb implantable derogations (sutures etc.)
#   52(6) Class IIa · 52(7) Class I incl. Is/Im/Ir NB-aspect involvement
#   52(8) custom-made devices · 52(9)+ out of registry (silent).
#
# Design constraints inherited from C2's measured failure (#134): pairing by
# character proximity produced 107→10 flags that were all false positives on
# table/list-dense advisory prose. C3 therefore pairs ONLY inside a structural
# unit (one markdown line — a table row is one line) and only fires when the
# paragraph is disallowed for EVERY class token in the unit (union fail-open).
# Paragraphs outside the registry (9+) stay silent, per C1 doctrine.
# ─────────────────────────────────────────────────────────────────────────────

# class token -> allowed Art. 52 paragraph numbers (bare integers)
_ART52_ALLOWED: dict[str, frozenset[int]] = {
    "i": frozenset({7}),
    "is": frozenset({7}),
    "im": frozenset({7}),
    "ir": frozenset({7}),
    "ii": frozenset({4, 5, 6}),  # generic "Class II" — either subclass
    "iia": frozenset({6}),
    "iib": frozenset({4, 5}),
    "iii": frozenset({3}),
}
_ART52_MAX_PARA = 8  # beyond: not in registry, silent

# "Class IIa", "classes IIb", "Class I". Case-insensitive, covers all grades.
_ART52_CLASS_ANCHORED_RE = re.compile(
    r"\bclass(?:es)?\s+(iii|iia|iib|is|im|ir|ii|i)\b", re.IGNORECASE
)
# Bare grades only as a cell/line-start LIST ("| IIa | …", "| **IIb / III** |",
# "<br>‑ IIa → …" compressed in-cell routes). Anchoring to these structural
# starts keeps out the roman numerals of "Annex II & III" / "Chapters I & III",
# which measured as the dominant false-positive source on the 2026-07..10
# corpus. The trailing "(?![A-Za-z0-9.])" keeps out outline markers ("III.").
_ART52_CLASS_BARE_LIST_RE = re.compile(
    r"(?:^|\||\*\*|<br\s*/?>|[‑‒–—•·]\s*)[ \t]*"
    r"((?:III|IIa|IIb|II|Is|Im|Ir|I)"
    r"(?:\s*(?:[/·,–—-])\s*(?:III|IIa|IIb|II|Is|Im|Ir|I))*)"
    r"(?![A-Za-z0-9.])"
)
_ART52_BARE_ITEM_RE = re.compile(r"III|IIa|IIb|II|Is|Im|Ir|I")


def _art52_unit_classes(unit: str) -> set[str]:
    """Class tokens present in one structural unit (line), anchored or bare."""
    found = {m.group(1).lower() for m in _ART52_CLASS_ANCHORED_RE.finditer(unit)}
    for m in _ART52_CLASS_BARE_LIST_RE.finditer(unit):
        for item in _ART52_BARE_ITEM_RE.findall(m.group(1)):
            found.add(item.lower())
    return found

_ART52_CITE_RE = re.compile(
    r"\bart(?:icle|\.)?\s*52\s*\(\s*(\d{1,2})\s*\)", re.IGNORECASE
)

_ART52_PARA_LABELS = {
    "i": "Class I (52(7))",
    "is": "Class Is (52(7), NB aspects)",
    "im": "Class Im (52(7), NB aspects)",
    "ir": "Class Ir (52(7), NB aspects)",
    "ii": "Class II generic (IIa 52(6) / IIb 52(4)-(5))",
    "iia": "Class IIa (52(6))",
    "iib": "Class IIb (52(4); 52(5) implantable derogations)",
    "iii": "Class III (52(3))",
}


def _art52_class(text: str) -> list[dict]:
    flags: list[dict] = []
    for unit in text.splitlines():
        classes = _art52_unit_classes(unit)
        if not classes:
            continue
        allowed: set[int] = set()
        for c in classes:
            allowed |= set(_ART52_ALLOWED[c])
        for m in _ART52_CITE_RE.finditer(unit):
            n = int(m.group(1))
            if n > _ART52_MAX_PARA or n in allowed:
                continue
            label = " / ".join(_ART52_PARA_LABELS[c] for c in sorted(classes))
            flags.append({
                "check": "C3",
                "severity": SEV_ERROR,
                "message": (
                    f"Art. 52({n}) is inconsistent with the device class on this line "
                    f"({label}) — verify the paragraph against MDR Art. 52."
                ),
                "span": m.group(0),
                "unit": unit.strip()[:160],
            })
    return flags


def lint_art52_class(text: str | None) -> list[dict]:
    """Return C3 flags for `text` (also included in lint_citations())."""
    if not text:
        return []
    return _art52_class(text)


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
