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

async function fetchHonchoEvents() {
  // Honcho v3 API: POST /v3/workspaces/{workspace}/sessions/list
  const raw = await postJson(
    `${HONCHO_API_URL}/v3/workspaces/${HONCHO_APP_NAME}/sessions/list`,
    { page: 1, page_size: 100 }
  );
  if (!raw) return MOCK_EVENTS;
  try {
    const parsed = JSON.parse(raw);
    const sessions = parsed.items || [];
    const results = await Promise.all(sessions.map(s => fetchSessionMessages(s.id)));
    return results
      .flat()
      .map(adaptHonchoMessage)
      .filter(Boolean)
      .sort((a, b) => new Date(a.ts) - new Date(b.ts));
  } catch {
    return MOCK_EVENTS;
  }
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

  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // 읽기 전용 — POST/PUT/DELETE 차단
  if (req.method !== 'GET') {
    res.writeHead(405, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Method not allowed. Virtual office is read-only.' }));
    return;
  }

  if (parsedUrl.pathname === '/api/events') {
    let events;
    if (DATA_SOURCE === 'honcho') {
      events = await fetchHonchoEvents();
    } else {
      events = MOCK_EVENTS;
    }
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(events));
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
