/**
 * Honcho Activity Log Adapter (Node.js / Express)
 *
 * virtual-office.html에 /api/events 엔드포인트를 제공.
 * DATA_SOURCE=honcho 시 Honcho 활동 기록을 이벤트 배열로 변환.
 * DATA_SOURCE=mock 시 목업 이벤트 반환.
 *
 * 읽기 전용 — 쓰기 API 경로 없음.
 */

const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = parseInt(process.env.PORT || '3000');
const DATA_SOURCE = process.env.DATA_SOURCE || 'mock';
const HONCHO_API_URL = process.env.HONCHO_API_URL || 'http://localhost:8000';
// @MX:NOTE: workspace 'work' contains all production agent sessions; 'ra-hermes' is empty
const HONCHO_APP_NAME = process.env.HONCHO_APP_NAME || 'work';
const POLL_INTERVAL_MS = parseInt(process.env.POLL_INTERVAL_MS || '30000');

// Human→RA advisory channel (Phase 1, docs/specs/advisory-chat-channel-spec.md, issue #104).
// The ADAPTER is the API caller — Hermes never learns about the virtual office.
// @MX:ANCHOR: one-directional invariant — adapter MUST present as a normal /v1/ra/advisory
// client; never put "vo"/"virtual-office"/"dashboard" in User-Agent, headers, or request body.
// @MX:REASON: CLAUDE.md:212 "this system is unaware of the virtual office" must hold.
// @MX:SPEC: docs/specs/advisory-chat-channel-spec.md REQ-AC-003, REQ-AC-007
const HERMES_API_URL = process.env.HERMES_API_URL || 'http://192.168.100.200:8643';
const API_SERVER_KEY = process.env.API_SERVER_KEY || '';
// @MX:WARN: CHAT_AUTH_TOKEN empty = no client auth — POC internal-network single-user only.
// @MX:REASON: set a non-empty token before any non-LAN exposure; empty is only for the
// single-user POC on the trusted T3610 LAN.
const CHAT_AUTH_TOKEN = process.env.CHAT_AUTH_TOKEN || '';
const ADVISORY_TIMEOUT_MS = parseInt(process.env.ADVISORY_TIMEOUT_MS || '180000');

// 목업 이벤트 (virtual-office.html의 EVENTS 배열과 동일)
const MOCK_EVENTS = [
  {type:"mail_received", actor:"system", target:"ra_us", payload:{region:"US", subject:"510(k) follow-up"}},
  {type:"matched",       actor:"ra_us", payload:{wp:"WP-123", confidence:0.91, existing:true}},
  {type:"comment_added", actor:"ra_us", payload:{wp:"WP-123", note:"진행현황 반영"}},
  {type:"transition_proposed", actor:"ra_us", payload:{wp:"WP-123", to:"리뷰중"}},
  {type:"mail_received", actor:"system", target:"ra_eu", payload:{region:"EU", subject:"MDR CER update"}},
  {type:"matched",       actor:"ra_eu", payload:{wp:"WP-204", confidence:0.74, existing:false}},
  {type:"comment_added", actor:"ra_eu", payload:{wp:"WP-204", note:"신규 사안 등록"}},
  {type:"vote_opened",   actor:"infra_gx10", payload:{topic:"추론 부하 높음"}},
  {type:"vote_cast",     actor:"infra_t3610", payload:{vote:"defer"}},
  {type:"vote_cast",     actor:"infra_rpi", payload:{vote:"defer"}},
  {type:"vote_result",   actor:"system", payload:{result:"업무 지연 권고"}},
  {type:"score_given",   actor:"human", payload:{target:"Mike 매칭", score:3}}
];

// Honcho 메시지를 가상 오피스 이벤트 형식으로 변환
// @MX:NOTE: maps two distinct Honcho record shapes — (1) record_type-tagged work
// records whose structure lives in metadata, (2) activity_log/mail records whose
// structure is a self-describing JSON in content. Only real-work records render;
// conversational (NULL record_type) messages are intentionally skipped.
function adaptHonchoMessage(msg) {
  const meta = msg.metadata || {};

  // (1) daily_growth_case: content는 사람이 읽는 텍스트 → 구조는 metadata에 있음.
  // @MX:NOTE: growth cases (ra_us/ra_eu/ra_kr) are the daily learning heartbeat.
  if (meta.record_type === 'daily_growth_case') {
    const actor = meta.actor || meta.peer_id;
    if (!actor) return null;
    const kws = Array.isArray(meta.matched_keywords) ? meta.matched_keywords : [];
    return {
      ts: msg.created_at,
      type: 'growth_case',
      actor,
      payload: { domain: kws.join('/') || '규제', source: meta.source || null, scenario_id: meta.scenario_id || null }
    };
  }

  // (1b) ra_advisory: T3610 RA agent returned a processing plan to raspi5p.
  // @MX:NOTE: advisory loop — RA advises (ra_advisory), raspi5p executes (ra_advisory_feedback).
  if (meta.record_type === 'ra_advisory') {
    const actor = meta.actor || meta.peer_id;
    if (!actor) return null;
    return {
      ts: msg.created_at,
      type: 'advisory_returned',
      actor,
      payload: {
        decision: meta.decision || null,
        confidence: meta.confidence,
        region: meta.region || null,
        wp_candidate: meta.wp_candidate ?? null,
        summary: msg.content || meta.summary || '',
        yellow_reason: meta.yellow_reason ?? null
      }
    };
  }

  // (1c) ra_advisory_feedback: raspi5p (Iris) executed after local gate.
  // @MX:NOTE: executor is always raspi5p regardless of which RA advised.
  if (meta.record_type === 'ra_advisory_feedback') {
    return {
      ts: msg.created_at,
      type: 'advisory_executed',
      actor: 'raspi5p',
      payload: {
        action_taken: meta.action_taken || null,
        wp_id: meta.wp_id ?? null,
        note: msg.content || ''
      }
    };
  }

  // (1d) ra_advisory_conclusion: final summary written in the SAME cycle as feedback
  // (hermes-api-server records feedback then conclusion back-to-back per advisory).
  // @MX:NOTE: intentionally dropped — feedback (advisory_executed) already renders the
  // action; showing both would duplicate the same event on the dashboard. Re-enable as a
  // distinct event type only if a separate "conclusion" visualization is desired. See #95.
  if (meta.record_type === 'ra_advisory_conclusion') {
    return null;
  }

  // (2) 자기서술적 JSON content를 가진 작업 레코드 — score_given(KB-eval 사람 채점) +
  // activity_log(n8n mail-triage). content 전체가 {type, actor?, payload} 계약.
  // @MX:NOTE: score_given actor lives in metadata (human), content only has type/payload.
  const isScoreGiven = meta.record_type === 'score_given';
  const isActivityLog = meta.type === 'activity_log';
  if (isScoreGiven || isActivityLog) {
    let parsed = null;
    try {
      parsed = typeof msg.content === 'string' ? JSON.parse(msg.content) : msg.content;
    } catch {
      return null;
    }
    if (!parsed || !parsed.type) return null;
    const actor = parsed.actor || meta.actor;
    if (!actor) return null;
    const event = {
      ts: parsed.ts || msg.created_at,
      type: parsed.type,
      actor,
      payload: parsed.payload || {}
    };
    // mail_received 이벤트에 target 필드 복원
    if (parsed.type === 'mail_received' && parsed.payload?.target) {
      event.target = parsed.payload.target;
    }
    return event;
  }

  return null;
}

// Agent maturity level (별 1~5) — displayed on RA expert characters.
// @MX:NOTE: star mapping uses daily_growth_case cumulative count (learning VOLUME only,
// not accuracy). Balanced formula: 1~9→1, 10~19→2, 20~34→3, 35~59→4, 60+→5.
// Star 5 = "지구 최강 전문가" long-term goal.
const RA_PEERS = ['ra_us', 'ra_eu', 'ra_kr'];
function levelFromCount(count) {
  if (count >= 60) return 5;
  if (count >= 35) return 4;
  if (count >= 20) return 3;
  if (count >= 10) return 2;
  return 1;
}
// accuracy='pending': ra-advisory confidence is intentionally NOT used as an accuracy
// signal — the raspi5p advisory loop (25s-interval duplicate Yellow) contaminates it
// (e.g. ra_kr 2557 records / avg conf 0.01). Only human KB-eval (#69~72) will populate
// accuracy once those evaluations are completed.
function computeAgentLevels(events) {
  const counts = { ra_us: 0, ra_eu: 0, ra_kr: 0 };
  for (const ev of events) {
    if (ev.type === 'growth_case' && counts[ev.actor] !== undefined) counts[ev.actor]++;
  }
  return RA_PEERS.map(p => ({
    actor: p,
    growth_cases: counts[p],
    level: levelFromCount(counts[p]),
    accuracy: 'pending'
  }));
}

function postJson(apiUrl, payload) {
  return new Promise((resolve) => {
    const parsedUrl = new URL(apiUrl);
    const transport = parsedUrl.protocol === 'https:' ? https : http;
    const reqBody = JSON.stringify(payload);
    const options = {
      hostname: parsedUrl.hostname,
      port: parsedUrl.port || (parsedUrl.protocol === 'https:' ? 443 : 80),
      // @MX:NOTE: pathname ALONE drops the query string — Honcho v3 pagination (?page=N)
      // is transmitted via search. Omitting it silently makes every page request return page 1.
      path: parsedUrl.pathname + (parsedUrl.search || ''),
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(reqBody)
      }
    };
    const req = transport.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    });
    req.on('error', () => resolve(null));
    req.setTimeout(5000, () => { req.destroy(); resolve(null); });
    req.write(reqBody);
    req.end();
  });
}

// ===== Human→RA advisory: async in-process map (OD-5 Option 1) =====
// @MX:NOTE: request_id → state. Adapter owns async; Hermes server unchanged.
// @MX:SPEC: REQ-AC-004, REQ-AC-009 (OD-5 = Option 1)
const advisoryRequests = new Map(); // request_id → {status, result, error, created_at, query}
const ADVISORY_TTL_MS = 30 * 60 * 1000; // 30 min
// Purge stale entries every 5 min so the map can't grow unbounded.
// @MX:WARN: setInterval in long-lived server — unref'd so it never blocks exit.
setInterval(() => {
  const now = Date.now();
  for (const [id, r] of advisoryRequests) {
    if (now - r.created_at > ADVISORY_TTL_MS) advisoryRequests.delete(id);
  }
}, 5 * 60 * 1000).unref();

function readJsonBody(req) {
  return new Promise((resolve) => {
    let raw = '';
    req.on('data', (c) => { raw += c; if (raw.length > 65536) req.destroy(); });
    req.on('end', () => {
      try { resolve(JSON.parse(raw || '{}')); } catch { resolve(null); }
    });
    req.on('error', () => resolve(null));
  });
}

// @MX:ANCHOR: Hermes advisory client — adapter presents as a normal caller (raspi5p-like).
// @MX:REASON: never leak VO identity; identical shape to existing raspi5p advisory calls.
// @MX:SPEC: REQ-AC-003 (backend proxy), REQ-AC-001 (query-only)
function callHermesAdvisory(query, regionHint, requestId) {
  const payload = JSON.stringify({
    query,
    region_hint: regionHint || null,
    wp_context: {} // TV-1: query-only advisory, no WP context
  });
  const parsedUrl = new URL(`${HERMES_API_URL}/v1/ra/advisory`);
  const transport = parsedUrl.protocol === 'https:' ? https : http;
  const options = {
    hostname: parsedUrl.hostname,
    port: parsedUrl.port || (parsedUrl.protocol === 'https:' ? 443 : 80),
    path: parsedUrl.pathname,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(payload),
      // @MX:NOTE: no VO/virtual-office identifier — adapter is just another advisory client.
      'Authorization': `Bearer ${API_SERVER_KEY}`
    }
  };
  const req = transport.request(options, (res) => {
    let data = '';
    res.on('data', (c) => data += c);
    res.on('end', () => {
      const entry = advisoryRequests.get(requestId);
      if (!entry) return; // purged/expired
      if (res.statusCode >= 200 && res.statusCode < 300) {
        let parsed;
        try { parsed = JSON.parse(data); } catch { parsed = null; }
        if (parsed) {
          entry.status = 'completed';
          entry.result = parsed;
        } else {
          entry.status = 'failed';
          entry.error = `non-JSON response (HTTP ${res.statusCode})`;
        }
      } else {
        entry.status = 'failed';
        entry.error = `upstream HTTP ${res.statusCode}: ${data.slice(0, 500)}`;
      }
      entry.completed_at = Date.now();
    });
  });
  req.on('error', (err) => {
    const entry = advisoryRequests.get(requestId);
    if (entry) {
      entry.status = 'failed';
      entry.error = `adapter→hermes error: ${err.message}`;
      entry.completed_at = Date.now();
    }
  });
  req.setTimeout(ADVISORY_TIMEOUT_MS, () => {
    req.destroy();
    const entry = advisoryRequests.get(requestId);
    if (entry) {
      entry.status = 'failed';
      entry.error = `timeout after ${ADVISORY_TIMEOUT_MS}ms`;
      entry.completed_at = Date.now();
    }
  });
  req.write(payload);
  req.end();
}

async function fetchHonchoEvents() {
  // Honcho v3 API: POST /v3/workspaces/{workspace}/sessions/list
  // @MX:NOTE: sessions/list ALSO paginates via query string (?page=N&page_size=50) and
  // caps page_size at 50 — same trap as messages/list (#95). Page 1 alone returns only
  // 50 of 66+ sessions, hiding ~half the growth-ra_* daily learning sessions and making
  // agent maturity stars under-count. Page through ALL pages + dedup by session id
  // (Honcho occasionally returns overlapping items across pages).
  const base = `${HONCHO_API_URL}/v3/workspaces/${HONCHO_APP_NAME}/sessions/list`;
  const first = await postJson(`${base}?page=1&page_size=50`, {});
  if (!first) return MOCK_EVENTS;
  let parsed;
  try { parsed = JSON.parse(first); } catch { return MOCK_EVENTS; }
  const seen = new Set();
  const sessions = [];
  for (const s of (parsed.items || [])) {
    if (s.id && !seen.has(s.id)) { seen.add(s.id); sessions.push(s); }
  }
  const pages = parsed.pages || 1;
  for (let p = 2; p <= pages; p++) {
    const raw = await postJson(`${base}?page=${p}&page_size=50`, {});
    if (!raw) break;
    let pageItems;
    try { pageItems = JSON.parse(raw).items || []; } catch { break; }
    let added = 0;
    for (const s of pageItems) {
      if (s.id && !seen.has(s.id)) { seen.add(s.id); sessions.push(s); added++; }
    }
    if (added === 0) break; // no new sessions → stop (guards against bad pages metadata)
  }
  const results = await Promise.all(sessions.map(s => fetchSessionMessages(s.id)));
  return results
    .flat()
    .map(adaptHonchoMessage)
    .filter(Boolean)
    .sort((a, b) => new Date(a.ts) - new Date(b.ts));
}

// @MX:NOTE: 30s TTL cache so /api/events and /api/agent-levels share one Honcho fetch
// (avoiding double pagination walks on every dashboard poll). Cache only holds real
// Honcho events; mock mode bypasses it.
let _eventsCache = null;
let _eventsCacheAt = 0;
async function getEvents() {
  const now = Date.now();
  if (_eventsCache && now - _eventsCacheAt < 30000) return _eventsCache;
  _eventsCache = await fetchHonchoEvents();
  _eventsCacheAt = now;
  return _eventsCache;
}

// @MX:NOTE: display-side dedup for /api/events. The raspi5p advisory loop emits the
// SAME advisory (actor+type+payload) every ~25s — thousands of identical records flood
// the dashboard (8k+ advisory events, 1.7MB payload). This collapses near-duplicate
// bursts within a window to one representative record so the dashboard payload stays
// small while genuine varied activity (growth_case, score_given, distinct advisories)
// passes through untouched. DB is NOT modified — display policy only.
function dedupeForDisplay(events, windowMs = 300000) {
  const out = [];
  const lastByKey = new Map();
  for (const ev of events) {
    const key = `${ev.actor}|${ev.type}|${JSON.stringify(ev.payload || {})}`;
    const last = lastByKey.get(key);
    if (last !== undefined && (new Date(ev.ts) - last) < windowMs) continue;
    lastByKey.set(key, new Date(ev.ts));
    out.push(ev);
  }
  return out;
}

async function fetchSessionMessages(sessionId) {
  // @MX:NOTE: Honcho v3 paginates via QUERY STRING (?page=N&page_size=50), NOT request body.
  // Body {page} is silently ignored → only page 1 (oldest 50) ever returns, hiding the latest
  // activity. Server also caps page_size at 50 regardless of the requested value.
  // @MX:REASON: page through ALL pages so the dashboard shows recent RA advisory/feedback,
  // not just the oldest 50 records. See issue #95.
  const base = `${HONCHO_API_URL}/v3/workspaces/${HONCHO_APP_NAME}/sessions/${sessionId}/messages/list`;
  const first = await postJson(`${base}?page=1&page_size=50`, {});
  if (!first) return [];
  let parsed;
  try { parsed = JSON.parse(first); } catch { return []; }
  const out = [...(parsed.items || [])];
  const pages = parsed.pages || 1;
  for (let p = 2; p <= pages; p++) {
    const raw = await postJson(`${base}?page=${p}&page_size=50`, {});
    if (!raw) break;
    try { out.push(...(JSON.parse(raw).items || [])); } catch { break; }
  }
  return out;
}

// In Docker: __dirname=/app, HTML is at /app/virtual-office.html (same dir)
// In local dev: __dirname=virtual-office/, HTML is at virtual-office/../virtual-office.html
const HTML_PATH = fs.existsSync(path.join(__dirname, 'virtual-office.html'))
  ? path.join(__dirname, 'virtual-office.html')
  : path.join(__dirname, '..', 'virtual-office.html');

const server = http.createServer(async (req, res) => {
  const parsedUrl = url.parse(req.url, true);

  // CORS — GET for observation, POST for /api/chat advisory only
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // 읽기 전용 유지 — POST는 /api/chat* (자문 채널)만 허용, 나머지 쓰기는 여전히 405.
  // @MX:ANCHOR: read-only invariant preserved — only /api/chat POST is whitelisted.
  // @MX:REASON: REQ-AC-007; all other write paths stay blocked (was 405 for everything pre-#104).
  // @MX:SPEC: docs/specs/advisory-chat-channel-spec.md
  const isChatPath = parsedUrl.pathname === '/api/chat' || parsedUrl.pathname.startsWith('/api/chat/');
  const isAllowedWrite = req.method === 'POST' && isChatPath;
  if (req.method !== 'GET' && !isAllowedWrite) {
    res.writeHead(405, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Method not allowed. Virtual office is read-only (only POST /api/chat is accepted).' }));
    return;
  }

  // POST /api/chat — submit human→RA advisory (OD-2 sessionStorage token auth)
  // @MX:SPEC: REQ-AC-003, REQ-AC-004, REQ-AC-006
  if (req.method === 'POST' && parsedUrl.pathname === '/api/chat') {
    // Auth: single-user token (OD-2). Empty CHAT_AUTH_TOKEN = LAN-only POC bypass.
    if (CHAT_AUTH_TOKEN) {
      const auth = req.headers.authorization || '';
      const token = auth.replace(/^Bearer\s+/i, '');
      if (token !== CHAT_AUTH_TOKEN) {
        res.writeHead(401, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'unauthorized' }));
        return;
      }
    }
    if (!API_SERVER_KEY) {
      res.writeHead(503, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'API_SERVER_KEY not configured on adapter' }));
      return;
    }
    const body = await readJsonBody(req);
    if (!body || typeof body.query !== 'string' || !body.query.trim()) {
      res.writeHead(400, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'query (string) required' }));
      return;
    }
    const requestId = require('crypto').randomUUID();
    advisoryRequests.set(requestId, {
      status: 'pending',
      query: body.query.slice(0, 2000),
      region_hint: body.region_hint || null,
      created_at: Date.now()
    });
    // Fire-and-forget — adapter resolves the entry async.
    callHermesAdvisory(body.query.slice(0, 2000), body.region_hint, requestId);
    res.writeHead(202, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ request_id: requestId, status: 'pending' }));
    return;
  }

  // GET /api/chat/{request_id} — poll advisory status/result
  // @MX:SPEC: REQ-AC-009
  if (req.method === 'GET' && parsedUrl.pathname.startsWith('/api/chat/')) {
    const requestId = decodeURIComponent(parsedUrl.pathname.slice('/api/chat/'.length));
    const entry = advisoryRequests.get(requestId);
    if (!entry) {
      res.writeHead(404, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'unknown or expired request_id' }));
      return;
    }
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      request_id: requestId,
      status: entry.status,
      result: entry.result || null,
      error: entry.error || null,
      created_at: entry.created_at,
      completed_at: entry.completed_at || null
    }));
    return;
  }

  if (parsedUrl.pathname === '/api/events') {
    // @MX:NOTE: display dedup — collapse raspi5p advisory loop bursts (identical events
    // every ~25s). /api/agent-levels still uses the FULL unfiltered set so maturity stars
    // count every growth_case accurately.
    const all = DATA_SOURCE === 'honcho' ? await getEvents() : MOCK_EVENTS;
    const events = dedupeForDisplay(all);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(events));
    return;
  }

  if (parsedUrl.pathname === '/api/agent-levels') {
    const events = DATA_SOURCE === 'honcho' ? await getEvents() : MOCK_EVENTS;
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      levels: computeAgentLevels(events),
      // @MX:NOTE: accuracy is pending — ra-advisory confidence excluded (raspi5p loop
      // contamination). Only human KB-eval (#69~72) will activate accuracy later.
      accuracy_status: 'ra-advisory confidence excluded (raspi5p loop contamination); accuracy pending human KB-eval (#69~72)',
      star_formula: 'balanced: 1~9→1, 10~19→2, 20~34→3, 35~59→4, 60+→5 (daily_growth_case volume)'
    }));
    return;
  }

  if (parsedUrl.pathname === '/api/config') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ data_source: DATA_SOURCE, poll_interval_ms: POLL_INTERVAL_MS }));
    return;
  }

  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/index.html') {
    try {
      const html = fs.readFileSync(HTML_PATH, 'utf8');
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(html);
    } catch {
      res.writeHead(404);
      res.end('virtual-office.html not found');
    }
    return;
  }

  res.writeHead(404);
  res.end('Not found');
});

server.listen(PORT, () => {
  console.log(`RA Virtual Office adapter running on :${PORT}`);
  console.log(`DATA_SOURCE=${DATA_SOURCE}`);
  if (DATA_SOURCE === 'honcho') {
    console.log(`HONCHO_API_URL=${HONCHO_API_URL}`);
  }
});
