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
    // 금지 토큰 부재는 그 토큰만 증명한다 — 일반 증명이 아니다(codex 지적).
    // 대신 **허용 필드 집합을 양성으로 고정**한다: 요청은 정확히 3필드다.
    const sent = JSON.parse(call.body);
    assert.deepEqual(Object.keys(sent).sort(), ['query', 'region_hint', 'wp_context']);
    assert.equal(sent.query, 'FDA 510(k) 제출 준비 확인');   // 사용자 질의 원문 그대로
    assert.equal(sent.region_hint, null);
    assert.deepEqual(sent.wp_context, {});

    // 헤더도 양성 고정 — 표준 인증/콘텐츠 헤더 외에는 싣지 않는다.
    const hdr = Object.keys(call.headers).map((k) => k.toLowerCase());
    for (const h of hdr) {
      assert.equal(['authorization', 'content-type', 'content-length', 'host', 'connection',
        'accept', 'accept-encoding', 'user-agent'].includes(h), true, `예상 밖 헤더: ${h}`);
    }
    // 관측된 **모든** 요청에 같은 계약을 적용한다(첫 건만이 아니라).
    for (const c of stub.seen) {
      assert.deepEqual(Object.keys(JSON.parse(c.body)).sort(), ['query', 'region_hint', 'wp_context']);
    }
  } finally { child.kill(); stub.server.close(); }
});

test('#104 GATE 직접 참조 정적 회귀 — 어댑터 소스에 WP close/reopen·KB repo 쓰기 직접 경로 없음', () => {
  const fs = require('node:fs');
  const html = fs.readFileSync(path.join(__dirname, '..', 'virtual-office', 'virtual-office.html'), 'utf8');
  // 함수 경계를 중괄호 균형으로 정확히 잘라낸다. 다음 함수 이름을 가정해 slice 하면
  // (이전 시도: 존재하지 않는 sendChat) 페이지 나머지 전체가 딸려 들어와, 다른 함수의
  // fetch 까지 이 테스트의 단언에 걸린다.
  const at = html.indexOf('async function pollAdvisory');
  assert.ok(at >= 0, 'pollAdvisory 를 찾지 못했다');
  let depth = 0, end = -1, started = false;
  for (let i = at; i < html.length; i++) {
    if (html[i] === '{') { depth++; started = true; }
    else if (html[i] === '}') { depth--; if (started && depth === 0) { end = i + 1; break; } }
  }
  assert.ok(end > at, 'pollAdvisory 의 끝을 찾지 못했다');
  const fn = html.slice(at, end);

  assert.match(fn, /r\.status\s*===\s*401/, '401 종료 분기 없음');
  assert.match(fn, /r\.status\s*===\s*404/, '404 종료 분기 없음');
  assert.match(fn, /!r\.ok/, '비정상 상태 일반 분기 없음');

  // 상태 검사가 본문 파싱보다 먼저여야 한다 — 나중이면 이미 계속 폴링한 뒤다
  assert.ok(fn.indexOf('r.status === 401') < fn.indexOf('await r.json()'),
    '상태 검사가 본문 파싱보다 뒤에 있다');

  // 사용자에게 보이는 문구만 검사한다 — 주석은 제외한다(주석의 설명 문구가 단언을 깨는 것을 막는다)
  const shown = (fn.match(/textContent\s*=\s*'([^']*)'/g) || []).join(' ');
  assert.ok(!/백그라운드에서 계속 처리/.test(shown),
    '확인한 적 없는 서버 처리를 단정하는 문구가 화면에 남아 있다');
  assert.match(shown, /확인하지 못|알 수 없/, '타임아웃 상태를 미확인으로 표기하지 않는다');

  // 서버가 이미 처리 중일 수 있으므로 무작정 재전송을 권하지 않는다(중복 요청 위험).
  // 상태 확인과 재전송을 구분해 안내해야 한다.
  assert.ok(!/재전송하세요|다시 시도하세요/.test(shown),
    '서버 처리 여부를 모르는 상태에서 재전송을 권하고 있다');
  assert.match(shown, /상태를 (다시 )?확인/, '상태 확인 안내가 없다');

  // 폴링이 스스로 재전송하지 않는다 (중복 요청 방지) — POST 를 만들지 않는다
  assert.ok(!/method\s*:\s*'POST'/.test(fn), '폴링이 재전송을 시도한다');
  assert.ok(fn.length < 4000, '추출 범위가 너무 넓다 — 함수 경계가 잘못됐다');
});
