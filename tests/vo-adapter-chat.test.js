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
