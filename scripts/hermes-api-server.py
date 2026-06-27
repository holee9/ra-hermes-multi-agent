#!/usr/bin/env python3
"""
hermes-api-server.py — Hermes RA OpenAI-compatible HTTP bridge
Port: 8643 (0.0.0.0)
Auth: Authorization: Bearer <API_SERVER_KEY>

Pipeline:
  1. Qdrant RAG search (Layer 1) — NAS company documents
  2. Build context (email metadata + RAG results + WP list)
  3. hermes -z <context> --skills ra-expert  (PRIMARY, sole LLM engine)
  4. Return wp_comment JSON for OpenProject WP comment posting

RA classification rules and output format are defined in SKILL.md, not here.
"""

import json
import logging
import os
import re
import subprocess
import time
import urllib.request
import urllib.error
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = os.environ.get("API_SERVER_KEY", "")
HERMES_BIN = os.environ.get("HERMES_BIN", "/home/abyz-lab/.local/bin/hermes")
HERMES_MAX_TOKENS = int(os.environ.get("HERMES_MAX_TOKENS", "4096"))
PORT = int(os.environ.get("API_SERVER_PORT", "8643"))
TIMEOUT = int(os.environ.get("HERMES_TIMEOUT", "120"))
RAG_TIMEOUT = int(os.environ.get("RAG_TIMEOUT", "60"))

# Profile routing: model field → hermes -p <profile>
# n8n sends model: $json.primary_actor (ra_us / ra_eu / ra_kr)
PROFILE_MAP: dict[str, str] = {
    "ra_us": "ra-us",
    "ra-us": "ra-us",
    "ra_eu": "ra-eu",
    "ra-eu": "ra-eu",
    "ra_kr": "ra-kr",
    "ra-kr": "ra-kr",
    "hermes-ra": "ra-us",  # legacy / default fallback
}
DEFAULT_PROFILE = "ra-us"

# Response log for weekly_review.py analysis. Contract A (/v1/chat/completions) only —
# written by log_response() inside chat_completions(). Contract C (/v1/ra/advisory) logs to
# ADV_REQUEST_LOG instead, so this file goes stale while Contract A is unused. That staleness
# is expected, not a defect (#88 action 3 — closed as no-action 2026-06-28 after investigation).
RESPONSE_LOG = os.environ.get("RESPONSE_LOG", "/var/log/hermes-responses.jsonl")

_response_logger = logging.getLogger("hermes.responses")
_response_logger.setLevel(logging.INFO)
try:
    _fh = logging.FileHandler(RESPONSE_LOG)
    _fh.setFormatter(logging.Formatter("%(message)s"))
    _response_logger.addHandler(_fh)
except OSError:
    pass  # log dir not writable; skip silently

# Advisory request log: input (query + region_hint) + outcome, so unclear_region is
# immediately diagnosable (#88 action 2). Separate from RESPONSE_LOG (that is #88 action 3).
ADV_REQUEST_LOG = os.environ.get("ADV_REQUEST_LOG", "/var/log/ra-advisory-requests.jsonl")

_adv_request_logger = logging.getLogger("ra.advisory.requests")
_adv_request_logger.setLevel(logging.INFO)
try:
    _ar_fh = logging.FileHandler(ADV_REQUEST_LOG)
    _ar_fh.setFormatter(logging.Formatter("%(message)s"))
    _adv_request_logger.addHandler(_ar_fh)
except OSError:
    pass  # log dir not writable; skip silently


def _log_adv_request(request_ref: str, query: str, region_hint: str | None, adv: dict) -> None:
    """Log advisory request input + outcome so unclear_region is immediately diagnosable.

    Joinable with Honcho via request_ref. Never raises — logging must not break advisory.
    """
    try:
        _adv_request_logger.info(json.dumps({
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "request_ref": request_ref,
            "query_len": len(query),
            "query": query[:1000],
            "region_hint": region_hint,
            "region": adv.get("region"),
            "actor": adv.get("actor"),
            "decision": adv.get("decision"),
            "yellow_reason": adv.get("yellow_reason"),
            "confidence": adv.get("confidence"),
        }, ensure_ascii=False))
    except Exception:
        pass


def log_response(metadata: dict, parsed: dict) -> None:
    """Append one JSONL line per processed Contract A request for quality review.

    Contract A-only (called from chat_completions, /v1/chat/completions). The Contract C
    advisory path (/v1/ra/advisory) does not call this — it logs via ADV_REQUEST_LOG.
    RESPONSE_LOG therefore stays silent while Contract A is unused (#88 action 3).
    """
    try:
        record = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "subject": metadata.get("subject", ""),
            "sender": metadata.get("sender", ""),
            "wp_comment": parsed.get("wp_comment", parsed),
        }
        _response_logger.info(json.dumps(record, ensure_ascii=False))
    except Exception:
        pass

# Layer 1: Qdrant RAG
RAG_SCRIPT = os.environ.get("RAG_SCRIPT", "/opt/hermes-ra/skills/ra-expert/scripts/rag_search.py")
QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://192.168.100.1:11434")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "qwen3-embedding:latest")

# Layer 4: Real-time knowledge (llm-wiki, openFDA, law.go.kr)
# @MX:ANCHOR: Layer 4 integration point — called from chat_completions alongside RAG
# @MX:REASON: 3 callers expected (chat_completions, health check, future batch eval)
KNOWLEDGE_SCRIPT = os.environ.get("KNOWLEDGE_SCRIPT", "/opt/hermes-ra/scripts/knowledge_fetch.py")
KNOWLEDGE_TIMEOUT = int(os.environ.get("KNOWLEDGE_TIMEOUT", "12"))


def check_auth() -> bool:
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return False
    return auth[7:] == API_KEY


def _run_rag_search(query: str, top: int = 5) -> list[dict]:
    """Layer 1: Search NAS Qdrant for relevant RA documents."""
    if not query.strip():
        return []
    try:
        result = subprocess.run(
            ["python3", RAG_SCRIPT, query, "--top", str(top)],
            capture_output=True,
            text=True,
            timeout=RAG_TIMEOUT,
            env={
                **os.environ,
                "QDRANT_URL": QDRANT_URL,
                "OLLAMA_URL": OLLAMA_URL,
                "EMBED_MODEL": EMBED_MODEL,
            },
        )
        if result.returncode == 0 and result.stdout.strip():
            data = json.loads(result.stdout)
            return data.get("results", [])
    except Exception:
        pass
    return []


def _run_knowledge_fetch(query: str, profile: str, top: int = 3) -> dict:
    """Layer 4: Fetch real-time knowledge from llm-wiki, openFDA, law.go.kr."""
    if not query.strip():
        return {}
    try:
        result = subprocess.run(
            ["/usr/bin/python3", KNOWLEDGE_SCRIPT, query, "--profile", profile, "--top", str(top)],
            capture_output=True,
            text=True,
            timeout=KNOWLEDGE_TIMEOUT,
            env=os.environ,
        )
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout).get("results", {})
    except Exception:
        pass
    return {}


def build_context(
    messages: list[dict],
    metadata: dict,
    rag_results: list[dict],
    wp_list: str,
    wiki_results: dict | None = None,
) -> str:
    """Build context for Hermes: email data + RAG results + Layer 4 + WP list.
    RA classification rules and output format are in SKILL.md, not here.
    """
    last_user_content = ""
    for msg in reversed(messages):
        if msg.get("role") == "user":
            last_user_content = msg.get("content", "")
            break

    subject = metadata.get("subject", "")
    sender = metadata.get("sender", "")
    attachments = metadata.get("attachments", [])
    if isinstance(attachments, str):
        attachments = [attachments] if attachments else []

    parts = ["## 수신 이메일"]
    if subject:
        parts.append(f"제목: {subject}")
    if sender:
        parts.append(f"발신자: {sender}")
    if attachments:
        parts.append(f"첨부파일: {', '.join(str(a) for a in attachments)}")
    parts.append("")
    parts.append(last_user_content)

    if rag_results:
        parts.append("")
        parts.append("## NAS 문서 검색 결과")
        for i, r in enumerate(rag_results[:5], 1):
            src = r.get("source_file", "unknown")
            score = r.get("score", 0)
            text = r.get("text", "")[:400]
            parts.append(f"[{i}] {src} (관련도: {score:.3f})")
            if text:
                parts.append(text)
        parts.append("")
        parts.append("위 문서를 source_docs에 인용하세요.")

    if wiki_results:
        _add_wiki_context(parts, wiki_results)

    if wp_list.strip():
        parts.append("")
        parts.append("## 기존 OpenProject WP 목록")
        parts.append(wp_list)
        parts.append("")
        parts.append("이 이메일과 관련 있는 WP가 있으면 matched_wp_id에 숫자로 반환하세요. 없으면 null.")

    parts.append("")
    parts.append("## 출력 지시")
    parts.append("반드시 한국어로 다음 JSON 형식으로만 응답하세요. summary, recommendation, wp_title, org, product 등 모든 텍스트 필드를 한국어로 작성하세요 (다른 텍스트 금지, 마크다운 코드블록 금지):")
    parts.append('{"wp_comment": {"email_type": "완료통보|액션필요|정보수신", "wp_title": "...", "summary": "...", "recommendation": "...", "confidence": 0.9, "deadline": null, "product": "...", "org": "...", "matched_wp_id": null}}')
    return "\n".join(parts)


def _add_wiki_context(parts: list[str], wiki_results: dict) -> None:
    """Append Layer 4 real-time knowledge sections to context parts."""
    llm_wiki = wiki_results.get("llm_wiki", [])
    openfda = wiki_results.get("openfda", [])
    law_kr = wiki_results.get("law_kr", [])

    if llm_wiki:
        parts.append("")
        parts.append("## Layer 4a: llm-wiki 지식베이스")
        parts.append("H&abyz 내부 지식베이스에서 검색된 관련 개념:")
        for item in llm_wiki:
            parts.append(f"### {item.get('path', '')} (관련도: {item.get('relevance_score', 0)})")
            parts.append(item.get("excerpt", "")[:500])

    if openfda:
        parts.append("")
        parts.append("## Layer 4b: openFDA 510(k) 실시간 데이터")
        parts.append("FDA 데이터베이스에서 조회된 최신 510(k) 클리어런스:")
        for item in openfda:
            parts.append(
                f"- {item.get('k_number','')} [{item.get('product_code','')}] "
                f"{item.get('device_name','')} — {item.get('decision_code','')} ({item.get('decision_date','')})"
            )
        parts.append("위 데이터를 predicate device 분석 또는 경쟁사 현황 파악에 활용하세요.")

    if law_kr:
        parts.append("")
        parts.append("## Layer 4c: 국가법령정보 실시간 조회")
        for item in law_kr:
            parts.append(f"- {item.get('summary', '')}")


def extract_metadata(data: dict) -> dict:
    return {
        "subject": data.get("subject", data.get("mail_subject", "")),
        "sender": data.get("sender", data.get("mail_sender", data.get("from", ""))),
        "attachments": data.get("attachments", data.get("mail_attachments", [])),
    }


def parse_wp_comment(text: str) -> dict | None:
    """Extract wp_comment JSON from Hermes output."""
    json_pattern = re.search(r'\{.*"wp_comment".*\}', text, re.DOTALL)
    if json_pattern:
        try:
            return json.loads(json_pattern.group(0))
        except json.JSONDecodeError:
            pass
    return None


def ensure_real_source_paths(parsed: dict, rag_results: list[dict]) -> dict:
    """Replace LLM-generated index numbers with real NAS file paths."""
    if not rag_results:
        return parsed
    wpc = parsed.get("wp_comment", {})
    existing = wpc.get("source_docs", [])
    has_real_paths = any(
        (isinstance(d, str) and "/" in d)
        or (isinstance(d, dict) and "/" in d.get("file", ""))
        for d in existing
    )
    if not has_real_paths:
        wpc["source_docs"] = [
            {
                "file": r.get("source_file", ""),
                "score": r.get("score", 0),
                "excerpt": r.get("text", "")[:200],
            }
            for r in rag_results[:3]
        ]
        parsed["wp_comment"] = wpc
    return parsed


# ── RA Advisory (raspi5p ← T3610 consultant) ─────────────────────────────
# @MX:NOTE: advisory = T3610 RA agents advise; raspi5p Hermes executes.
# Boundary: T3610 never writes OpenProject. Honcho stays local; raspi5p uses 8643 only.
ADVISORY_REGION_KEYWORDS: dict[str, list[str]] = {
    "ra_us": ["fda", "510(k)", "510k", "qmsr", "de novo", "pma", "미국"],
    "ra_eu": ["mdr", "eudamed", "eu clinical", "ce mark", "ce-mdr", "유럽"],
    "ra_kr": ["mfds", "kgmp", "식약처", "한국", "국내", "허가"],
}
ADVISORY_ACTOR_PROFILE: dict[str, str] = {"ra_us": "ra-us", "ra_eu": "ra-eu", "ra_kr": "ra-kr"}
ADVISORY_REGION_LABEL: dict[str, str] = {"ra_us": "US", "ra_eu": "EU", "ra_kr": "KR"}
# Accept region hint as either label (US/EU/KR) or actor id (ra_us/ra_eu/ra_kr).
HINT_ALIASES: dict[str, str] = {
    "us": "ra_us", "eu": "ra_eu", "kr": "ra_kr",
    "ra_us": "ra_us", "ra_eu": "ra_eu", "ra_kr": "ra_kr",
}
ADVISORY_LOW_CONF = float(os.environ.get("ADVISORY_LOW_CONF", "0.5"))
ADVISORY_TIMEOUT = int(os.environ.get("ADVISORY_TIMEOUT", "180"))
ADVISORY_FALLBACK_ACTOR = os.environ.get("ADVISORY_FALLBACK_ACTOR", "ra_kr")
if ADVISORY_FALLBACK_ACTOR not in ADVISORY_ACTOR_PROFILE:
    ADVISORY_FALLBACK_ACTOR = "ra_kr"
HONCHO_API_URL = os.environ.get("HONCHO_API_URL", "http://localhost:8000")
HONCHO_WORKSPACE = os.environ.get("HONCHO_WORKSPACE", "work")


def normalize_region_hint(hint: str | None) -> str | None:
    """Normalize a region hint (US/EU/KR or ra_us/ra_eu/ra_kr) -> actor id, or None."""
    return HINT_ALIASES.get((hint or "").lower())


def route_advisory_region(query: str, hint: str | None) -> tuple[str | None, str | None]:
    """Server-side keyword routing. Returns (actor, yellow_reason).

    Single match -> actor; multi/none -> (None, yellow_reason). Caller hint is
    honored only when it does not conflict with detected regions.
    """
    hint = normalize_region_hint(hint)
    q = (query or "").lower()
    detected: set[str] = set()
    for actor, kws in ADVISORY_REGION_KEYWORDS.items():
        if any(kw in q for kw in kws):
            detected.add(actor)

    if hint in ADVISORY_ACTOR_PROFILE:
        if not detected or detected == {hint}:
            return hint, None
        return None, "multi_region"

    if len(detected) == 1:
        return next(iter(detected)), None
    if detected:
        return None, "multi_region"
    return None, "unclear_region"


def _extract_json_objects(text: str) -> list[dict]:
    """Return balanced JSON objects found in free text (handles nesting)."""
    objs: list[dict] = []
    depth = 0
    start = -1
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            if depth > 0:
                depth -= 1
                if depth == 0 and start >= 0:
                    try:
                        objs.append(json.loads(text[start : i + 1]))
                    except json.JSONDecodeError:
                        pass
                    start = -1
    return objs


def parse_advisory(text: str) -> dict | None:
    """Extract advisory JSON from Hermes output."""
    for d in _extract_json_objects(text):
        if isinstance(d, dict) and ("decision" in d or "recommended_comment" in d):
            return d
    return None


def validate_advisory(adv: dict, routed_actor: str) -> tuple[dict, str | None]:
    """Enforce advisory contract. Returns (normalized_adv, yellow_reason_or_None).

    Yellow when: invalid confidence, low confidence (< LOW_CONF = uncertain), or
    no evidence (accuracy-first: every executable advisory must cite a source).
    actor is ALWAYS the routed underscore actor (never trust LLM spelling) so a
    wrong/hyphen peer id can never leak.
    """
    adv["actor"] = routed_actor
    adv["region"] = ADVISORY_REGION_LABEL.get(routed_actor, "")
    conf = adv.get("confidence")
    if not isinstance(conf, (int, float)) or isinstance(conf, bool) or not (0 <= conf <= 1):
        adv["confidence"] = 0.0
        return adv, "invalid_confidence"
    if conf < ADVISORY_LOW_CONF:
        return adv, "low_confidence"
    if not (adv.get("evidence") or []):
        return adv, "no_evidence"
    return adv, None


def build_advisory_context(
    query: str,
    actor: str,
    region: str,
    rag_results: list[dict],
    wiki_results: dict | None,
    wp_context: dict | None,
) -> str:
    """Context for advisory output (NOT wp_comment). Reuses RAG/Layer4 evidence."""
    parts = [f"## RA 자문 요청 — 담당 {actor} ({region})", "", "## 사안", query]
    wp = wp_context or {}
    wp_list = wp.get("wp_list", "")
    wp_id = wp.get("wp_id")
    if isinstance(wp_list, str) and wp_list.strip():
        parts += ["", "## 기존 OpenProject WP 목록", wp_list]
    if wp_id:
        parts.append(f"(검토 대상 WP 후보: {wp_id})")
    if rag_results:
        parts += ["", "## 관련 문서(NAS) — evidence로 인용 가능"]
        for i, r in enumerate(rag_results[:5], 1):
            parts.append(f"[{i}] {r.get('source_file', '')} (관련도 {r.get('score', 0):.3f})")
            parts.append(r.get("text", "")[:300])
    if wiki_results:
        _add_wiki_context(parts, wiki_results)
    tmpl = (
        '{"actor": "' + actor + '", "region": "' + region + '", '
        '"confidence": 0.0~1.0, "decision": "comment_existing_wp|request_new_wp_review|yellow_review|no_action", '
        '"wp_candidate": <WP번호 또는 null>, "summary": "...", "recommended_comment": "...", '
        '"evidence": ["source/path.md"], "yellow_reason": null}'
    )
    parts += [
        "",
        "## 출력 지시",
        "반드시 한국어로 다음 JSON 형식으로만 응답하세요 (마크다운 코드블록 금지, 다른 텍스트 금지):",
        tmpl,
        "- confidence 0.5 이상 실행 응답은 evidence(출처) 1개 이상 필수. 근거 없으면 Yellow.",
        "- confidence 0.5 미만(불확실)이면 Yellow.",
        '- 불확실/근거 부족/다중 규제권이면 decision="yellow_review", yellow_reason 작성.',
    ]
    return "\n".join(parts)


def _invoke_hermes(profile: str, context: str, timeout: int = TIMEOUT) -> tuple[str, str]:
    """Call hermes -p profile -z context --skills ra-expert. Returns (stdout, error)."""
    try:
        result = subprocess.run(
            [HERMES_BIN, "-p", profile, "-z", context, "--skills", "ra-expert"],
            capture_output=True,
            text=True,
            timeout=timeout,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        )
        out = result.stdout.strip()
        if out:
            return out, ""
        return "", (result.stderr.strip()[:500] or "no output")
    except subprocess.TimeoutExpired:
        return "", f"hermes timeout after {timeout}s"
    except FileNotFoundError:
        return "", f"hermes binary not found: {HERMES_BIN}"
    except Exception as e:
        return "", str(e)


def _yellow_advisory(reason: str, region: str | None, error: str | None = None) -> dict:
    """Build a non-executable Yellow advisory (auto-execution forbidden)."""
    msg = {
        "multi_region": "다중 규제권이 감지되어 단일 RA 전문가 자문 불가",
        "unclear_region": "규제권을 특정할 수 없음",
        "low_confidence": "신뢰도 낮음(불확실) — 사람 검토 필요",
        "no_evidence": "근거(evidence) 없음 — 실행 불가",
        "invalid_confidence": "confidence 값이 유효하지 않음",
        "parse_or_hermes_failure": "RA agent 응답 파싱/호출 실패",
    }.get(reason, reason)
    if error:
        msg = f"{msg} ({error[:120]})"
    actor = region if region in ADVISORY_ACTOR_PROFILE else ADVISORY_FALLBACK_ACTOR
    return {
        "actor": actor,
        "region": ADVISORY_REGION_LABEL.get(actor, ""),
        "confidence": 0.0,
        "decision": "yellow_review",
        "wp_candidate": None,
        "summary": f"[Yellow] {msg}",
        "recommended_comment": None,
        "evidence": [],
        "yellow_reason": reason,
    }


def _adv_meta(adv: dict, request_ref: str) -> dict:
    """Structured metadata for Honcho (content stays clean text)."""
    return {
        "actor": adv.get("actor"),
        "region": adv.get("region"),
        "confidence": adv.get("confidence"),
        "decision": adv.get("decision"),
        "wp_candidate": adv.get("wp_candidate"),
        "evidence": adv.get("evidence") or [],
        "yellow_reason": adv.get("yellow_reason"),
        "request_ref": request_ref,
    }


def _honcho_record(record_type: str, peer_id: str, content_text: str, meta: dict) -> None:
    """Best-effort Honcho record (clean text content + structured metadata).

    Never raises: advisory must not fail because Honcho is down (circular-dep avoid).
    """
    try:
        session_id = {
            "ra_advisory": "ra-advisory",
            "ra_advisory_feedback": "ra-advisory-feedback",
            "ra_advisory_conclusion": "ra-advisory-conclusion",
        }.get(record_type, "ra-advisory-feedback")
        base = f"{HONCHO_API_URL}/v3/workspaces/{HONCHO_WORKSPACE}/sessions"
        sess_req = urllib.request.Request(
            f"{base}/{session_id}",
            data=json.dumps({"id": session_id, "metadata": {"purpose": record_type}}).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            urllib.request.urlopen(sess_req, timeout=5)
        except urllib.error.HTTPError:
            pass  # session already exists
        msg_req = urllib.request.Request(
            f"{base}/{session_id}/messages",
            data=json.dumps({
                "messages": [{
                    "peer_id": peer_id,
                    "content": content_text,
                    "metadata": {"record_type": record_type, **meta},
                }]
            }).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        urllib.request.urlopen(msg_req, timeout=5)
    except Exception:
        pass


@app.route("/v1/models", methods=["GET"])
def list_models():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    now = int(time.time())
    return jsonify({
        "object": "list",
        "data": [
            {"id": "ra_us", "object": "model", "created": now, "owned_by": "hermes"},
            {"id": "ra_eu", "object": "model", "created": now, "owned_by": "hermes"},
            {"id": "ra_kr", "object": "model", "created": now, "owned_by": "hermes"},
            {"id": "hermes-ra", "object": "model", "created": now, "owned_by": "hermes"},
        ],
    })


@app.route("/v1/knowledge/fetch", methods=["POST"])
def knowledge_fetch():
    """Expose Layer 4 lookup for n8n preflight context injection.

    The chat endpoint still performs its own Layer 4 lookup. This endpoint lets
    n8n record and pass the same real-time evidence explicitly before the RA
    call, while degrading safely to an empty result when upstream sources fail.
    """
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(force=True, silent=True) or {}
    query = str(data.get("query") or data.get("search_query") or "").strip()
    model = str(data.get("model") or data.get("profile") or DEFAULT_PROFILE)
    profile = PROFILE_MAP.get(model, model if model in PROFILE_MAP.values() else DEFAULT_PROFILE)
    try:
        top = int(data.get("top", 3))
    except (TypeError, ValueError):
        top = 3
    top = max(1, min(top, 10))

    if not query:
        return jsonify({
            "status": "skipped",
            "reason": "empty_query",
            "profile": profile,
            "results": {},
        })

    results = _run_knowledge_fetch(query, profile, top=top)
    return jsonify({
        "status": "ok" if results else "empty_or_unavailable",
        "profile": profile,
        "query": query,
        "top": top,
        "results": results,
    })


@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(force=True, silent=True) or {}
    messages = data.get("messages", [])

    if not messages:
        body_content = data.get("body", data.get("content", ""))
        if body_content:
            messages = [{"role": "user", "content": body_content}]
        else:
            return jsonify({"error": "No messages provided"}), 400

    metadata = extract_metadata(data)
    wp_list = data.get("wp_list", "")

    # Layer 1: Qdrant RAG
    search_query = metadata.get("subject", "")
    if not search_query.strip():
        for msg in reversed(messages):
            if msg.get("role") == "user":
                search_query = msg.get("content", "")[:150]
                break
    rag_results = _run_rag_search(search_query, top=5)

    # Resolve RA profile early (needed for Layer 4 source selection)
    profile = PROFILE_MAP.get(data.get("model", ""), DEFAULT_PROFILE)

    # Layer 4: Real-time knowledge (llm-wiki, openFDA, law.go.kr)
    wiki_results = _run_knowledge_fetch(search_query, profile, top=3)

    context = build_context(messages, metadata, rag_results, wp_list, wiki_results)

    # PRIMARY: Nous Hermes Agent with RA profile + ra-expert skill
    # -p loads SOUL.md (Mike/Theo/Sam persona) and enables ra-project/MD-process knowledge layers
    response_text = ""
    error_detail = ""
    try:
        result = subprocess.run(
            [HERMES_BIN, "-p", profile, "-z", context, "--skills", "ra-expert"],
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        )
        response_text = result.stdout.strip()
        if not response_text and result.stderr:
            error_detail = result.stderr.strip()[:500]
    except subprocess.TimeoutExpired:
        error_detail = f"hermes -z timeout after {TIMEOUT}s"
    except FileNotFoundError:
        error_detail = f"hermes binary not found: {HERMES_BIN}"
    except Exception as e:
        error_detail = str(e)

    if not response_text:
        content = json.dumps({
            "wp_comment": {
                "email_type": "액션필요",
                "matched_wp_id": None,
                "wp_title": f"[오류] {metadata.get('subject', '이메일 처리 실패')}",
                "summary": "Hermes Agent 호출에 실패했습니다. 서버 로그를 확인하세요.",
                "market_analysis": {"mfds": None, "ce_mdr": None, "fda": None},
                "source_docs": [],
                "recommendation": f"hermes 서비스 상태 확인: journalctl -u hermes-api-server. 오류: {error_detail}",
                "confidence": 0.0,
                "deadline": None,
                "product": None,
                "org": None,
                "flags": ["hermes_failed"],
            }
        }, ensure_ascii=False)
    else:
        parsed = parse_wp_comment(response_text)
        if parsed:
            parsed = ensure_real_source_paths(parsed, rag_results)
            content = json.dumps(parsed, ensure_ascii=False)
            log_response(metadata, parsed)
        else:
            content = response_text

    return jsonify({
        "id": f"chatcmpl-hermes-{int(time.time())}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": data.get("model", "hermes-ra"),
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": content},
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": len(context.split()),
            "completion_tokens": len(content.split()),
            "total_tokens": len(context.split()) + len(content.split()),
        },
    })


@app.route("/v1/ra/advisory", methods=["POST"])
def ra_advisory():
    """RA advisory: T3610 returns a processing plan; never writes OpenProject.

    raspi5p Hermes calls this, then re-verifies and executes locally. Output is
    the fixed advisory contract; routing/validation violations collapse to Yellow.
    """
    # @MX:ANCHOR: cross-machine advisory boundary (raspi5p caller, T3610 consultant)
    # @MX:REASON: gates all OP execution to raspi5p; T3610 only advises + records to local Honcho
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(force=True, silent=True) or {}
    query = str(data.get("query") or data.get("content") or "").strip()
    if not query or len(query) > 8000:
        return jsonify({"error": "query required (<=8000 chars)"}), 400
    wp_context = data.get("wp_context") or {}
    region_hint = str(data.get("region_hint") or "").strip() or None

    actor, yellow = route_advisory_region(query, region_hint)
    request_ref = f"adv-{int(time.time())}"

    if yellow:
        adv = _yellow_advisory(yellow, normalize_region_hint(region_hint))
        adv["request_ref"] = request_ref
        _honcho_record("ra_advisory", adv["actor"], adv["summary"], _adv_meta(adv, request_ref))
        _log_adv_request(request_ref, query, region_hint, adv)
        return jsonify(adv)

    profile = ADVISORY_ACTOR_PROFILE[actor]
    region = ADVISORY_REGION_LABEL[actor]
    rag_results = _run_rag_search(query, top=5)
    wiki_results = _run_knowledge_fetch(query, profile, top=3)
    context = build_advisory_context(query, actor, region, rag_results, wiki_results, wp_context)

    response_text, error_detail = _invoke_hermes(profile, context, timeout=ADVISORY_TIMEOUT)
    adv = parse_advisory(response_text) if response_text else None

    if adv:
        adv, vyellow = validate_advisory(adv, actor)
        if vyellow:
            adv = _yellow_advisory(vyellow, actor, error=str(vyellow))
        else:
            adv.setdefault("yellow_reason", None)
    else:
        adv = _yellow_advisory("parse_or_hermes_failure", actor, error=error_detail)

    adv["request_ref"] = request_ref
    _honcho_record("ra_advisory", actor, adv.get("summary", ""), _adv_meta(adv, request_ref))
    _log_adv_request(request_ref, query, region_hint, adv)
    return jsonify(adv)


@app.route("/v1/ra/advisory/feedback", methods=["POST"])
def ra_advisory_feedback():
    """raspi5p reports execution result; T3610 records ra_advisory_feedback locally."""
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(force=True, silent=True) or {}
    request_ref = str(data.get("request_ref") or "").strip()
    if not request_ref:
        return jsonify({"error": "request_ref required"}), 400
    action = str(data.get("action_taken") or "").strip()
    if action not in ("comment_added", "review_requested", "rejected", "no_action"):
        return jsonify({"error": "invalid action_taken"}), 400

    actor = str(data.get("actor") or ADVISORY_FALLBACK_ACTOR).strip()
    if actor not in ADVISORY_ACTOR_PROFILE:
        actor = ADVISORY_FALLBACK_ACTOR
    note = str(data.get("note") or data.get("summary") or "").strip()
    wp_id = data.get("wp_id")
    gate = data.get("gate_result")

    content = "[실행결과] " + action + (f" → WP {wp_id}" if wp_id else "") + (f": {note}" if note else "")
    meta = {
        "request_ref": request_ref,
        "action_taken": action,
        "wp_id": wp_id,
        "gate_result": gate,
    }
    _honcho_record("ra_advisory_feedback", actor, content, meta)
    if action in ("comment_added", "review_requested", "rejected", "no_action"):
        conclusion = "[결론] " + action + (f" / WP {wp_id}" if wp_id else " / WP 없음") + (f" / {note}" if note else "")
        _honcho_record("ra_advisory_conclusion", actor, conclusion, {
            **meta,
            "conclusion": {
                "request_ref": request_ref,
                "actor": actor,
                "action_taken": action,
                "wp_id": wp_id,
                "note": note,
            },
        })
    return jsonify({"status": "recorded", "request_ref": request_ref})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": True, "service": "hermes-api-server"})


if __name__ == "__main__":
    print(f"[hermes-api-server] Starting on 0.0.0.0:{PORT}")
    print(f"[hermes-api-server] HERMES_BIN={HERMES_BIN}")
    print(f"[hermes-api-server] API_KEY={'*' * len(API_KEY)}")
    app.run(host="0.0.0.0", port=PORT, debug=False, threaded=True)
