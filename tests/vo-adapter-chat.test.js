// #104 — GET /api/chat/{request_id} auth gate + malformed-id handling.
// Codex review (2026-09-10): `/api/chat/%ZZ` with a valid token threw URIError out of the
// handler with no response. The adapter is started as a real child process on a free port
// (it calls server.listen at module load), and exercised with fetch. No Honcho/Hermes calls:
// the poll path only reads the in-process map.
const test = require('node:test');
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const net = require('node:net');
const path = require('node:path');

const ADAPTER = path.join(__dirname, '..', 'virtual-office', 'virtual-office-honcho-adapter.js');
const TOKEN = 'test-token';

function freePort() {
  return new Promise((resolve, reject) => {
    const s = net.createServer();
    s.listen(0, '127.0.0.1', () => { const p = s.address().port; s.close(() => resolve(p)); });
    s.on('error', reject);
  });
}

async function startAdapter() {
  const port = await freePort();
  const child = spawn(process.execPath, [ADAPTER], {
    env: { ...process.env, PORT: String(port), CHAT_AUTH_TOKEN: TOKEN, API_SERVER_KEY: 'k', DATA_SOURCE: 'honcho' },
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  await new Promise((resolve, reject) => {
    const t = setTimeout(() => reject(new Error('adapter did not start')), 8000);
    child.stdout.on('data', (d) => { if (String(d).includes('running on')) { clearTimeout(t); resolve(); } });
    child.on('exit', (c) => reject(new Error(`adapter exited ${c}`)));
  });
  return { child, base: `http://127.0.0.1:${port}` };
}

test('GET /api/chat/{id}: auth, malformed id, unknown id', async () => {
  const { child, base } = await startAdapter();
  try {
    const get = (p, headers = {}) => fetch(base + p, { headers });
    const ok = { Authorization: `Bearer ${TOKEN}` };
    const uuid = '123e4567-e89b-42d3-a456-426614174000';

    assert.equal((await get(`/api/chat/${uuid}`)).status, 401, 'no token');
    assert.equal((await get(`/api/chat/${uuid}`, { Authorization: 'Bearer nope' })).status, 401, 'bad token');
    assert.equal((await get(`/api/chat/${uuid}`, ok)).status, 404, 'valid token, unknown id');

    const bad = await get('/api/chat/%ZZ', ok);
    assert.equal(bad.status, 400, 'malformed percent escape must be 400, not an unhandled URIError');
    assert.equal((await bad.json()).error, 'malformed request_id');

    const notUuid = await get('/api/chat/not-a-uuid', ok);
    assert.equal(notUuid.status, 400);
    assert.equal((await notUuid.json()).error, 'request_id must be a UUID');

    // the process is still alive after the malformed request
    assert.equal((await get(`/api/chat/${uuid}`, ok)).status, 404);
    assert.equal(child.exitCode, null);
  } finally {
    child.kill();
  }
});

test('POST /api/chat still requires the token', async () => {
  const { child, base } = await startAdapter();
  try {
    const r = await fetch(base + '/api/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                                                body: JSON.stringify({ query: 'x' }) });
    assert.equal(r.status, 401);
  } finally {
    child.kill();
  }
});

// ── #104 Phase 1 DoD 검증 ─────────────────────────────────────────────────────
// 어댑터를 실제 자식 프로세스로 띄우고, Hermes 자문 서버는 **로컬 스텁**으로 대체한다.
// 운영 Hermes·Honcho 는 호출하지 않는다(HERMES_API_URL 을 스텁으로 가리킴).
const http = require('node:http');

async function startHermesStub() {
  const seen = [];
  const server = http.createServer((req, res) => {
    let body = '';
    req.on('data', (c) => { body += c; });
    req.on('end', () => {
      seen.push({ method: req.method, url: req.url, headers: req.headers, body });
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        actor: 'ra_us', region: 'US', confidence: 0.8, decision: 'yellow_review',
        summary: 's', recommended_comment: 'c', evidence: [], yellow_reason: null,
      }));
    });
  });
  const port = await freePort();
  await new Promise((r) => server.listen(port, '127.0.0.1', r));
  return { server, seen, url: `http://127.0.0.1:${port}` };
}

async function startAdapterWith(env) {
  const port = await freePort();
  const child = spawn(process.execPath, [ADAPTER], {
    env: { ...process.env, PORT: String(port), CHAT_AUTH_TOKEN: TOKEN, API_SERVER_KEY: 'k',
           DATA_SOURCE: 'honcho', ...env },
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  await new Promise((resolve, reject) => {
    const t = setTimeout(() => reject(new Error('adapter did not start')), 8000);
    child.stdout.on('data', (d) => { if (String(d).includes('running on')) { clearTimeout(t); resolve(); } });
    child.on('exit', (c) => reject(new Error(`adapter exited ${c}`)));
  });
  return { child, base: `http://127.0.0.1:${port}` };
}

test('#104 DoD: POST /api/chat 만 쓰기 허용, 그 외 메서드·경로는 405', async () => {
  const { child, base } = await startAdapter();
  try {
    const post = await fetch(`${base}/api/activity`, { method: 'POST' });
    assert.equal(post.status, 405);
    for (const m of ['PUT', 'DELETE', 'PATCH']) {
      const r = await fetch(`${base}/api/chat`, { method: m });
      assert.equal(r.status, 405, `${m} must be blocked`);
    }
    const noToken = await fetch(`${base}/api/chat`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{"query":"x"}' });
    assert.notEqual(noToken.status, 405);          // 경로는 허용되고 인증에서 걸린다
    assert.equal(noToken.status, 401);
  } finally { child.kill(); }
});

test('#104 DoD: request_id 발급 → 배경 자문 호출 → 폴링으로 결과 회신, VO 흔적 없음', async () => {
  const stub = await startHermesStub();
  const { child, base } = await startAdapterWith({ HERMES_API_URL: stub.url });
  try {
    const submit = await fetch(`${base}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${TOKEN}` },
      body: JSON.stringify({ query: 'FDA 510(k) 제출 준비 확인' }),
    });
    assert.equal(submit.status, 202);
    const { request_id: id } = await submit.json();
    assert.match(id, /^[0-9a-f-]{16,}$/i);

    let body = null;
    for (let i = 0; i < 60; i++) {                 // 폴링 — 스텁이라 곧 completed
      const r = await fetch(`${base}/api/chat/${id}`, { headers: { Authorization: `Bearer ${TOKEN}` } });
      assert.equal(r.status, 200);
      body = await r.json();
      if (body.status === 'completed' || body.status === 'failed') break;
      await new Promise((s) => setTimeout(s, 100));
    }
    assert.equal(body.status, 'completed', `polling never completed: ${JSON.stringify(body)}`);

    // 단방향 검증: Hermes 가 본 요청에 VO 를 식별할 만한 흔적이 없어야 한다.
    assert.equal(stub.seen.length >= 1, true);
    const call = stub.seen[0];
    assert.equal(call.method, 'POST');
    assert.equal(call.url, '/v1/ra/advisory');
    const wire = JSON.stringify({ h: call.headers, b: call.body }).toLowerCase();
    for (const leak of ['virtual-office', 'virtual_office', 'vo-adapter', 'honcho-adapter', 'request_id']) {
      assert.equal(wire.includes(leak), false, `Hermes 요청에 VO 흔적 노출: ${leak}`);
    }
    assert.equal(JSON.parse(call.body).wp_context && Object.keys(JSON.parse(call.body).wp_context).length, 0);
  } finally { child.kill(); stub.server.close(); }
});

test('#104 DoD: GATE 준수 — 어댑터에 WP close/reopen·KB repo 쓰기 경로 없음', () => {
  const fs = require('node:fs');
  const src = fs.readFileSync(ADAPTER, 'utf8');
  const code = src.split('\n').filter((l) => !l.trim().startsWith('//')).join('\n');
  for (const forbidden of ['/work_packages/', 'openproject', 'llm-wiki', 'ra-project', 'MD-process']) {
    assert.equal(code.toLowerCase().includes(forbidden.toLowerCase()), false,
      `어댑터가 금지 대상을 참조: ${forbidden}`);
  }
  assert.equal(/method:\s*['"](PUT|PATCH|DELETE)['"]/.test(code), false, '어댑터에 쓰기 메서드 호출이 있으면 안 된다');
});
