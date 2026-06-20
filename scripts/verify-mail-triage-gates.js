// Verify mail-triage safety gates (#43 SAFETY-1 / #44 SAFETY-2).
// Runs the actual n8n code-node jsCode against sample inputs with n8n deps stubbed.
// No production side-effects (no RA/GX10/OP/Honcho calls) — deterministic gate-logic check.
// Run: node scripts/verify-mail-triage-gates.js
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const wf = JSON.parse(fs.readFileSync(path.join(ROOT, 'n8n/workflows/mail-triage.json'), 'utf8'));
const codeOf = (name) => wf.nodes.find(n => n.name === name).parameters.jsCode;

function runNode(name, inputItem, opts = {}) {
  const code = codeOf(name);
  const $input = { item: { json: inputItem } };
  const $ = (n) => ({ first: () => ({ json: (opts.refs || {})[n] || {} }) });
  const proc = { env: opts.env || {} };
  const fn = new Function('$input', '$', 'process', code);
  return fn($input, $, proc);
}

let pass = 0, fail = 0;
const ok = (label, cond, detail = '') => {
  if (cond) { pass++; console.log('  PASS', label); }
  else { fail++; console.log('  FAIL', label, detail); }
};

const env070 = { YELLOW_CONFIDENCE_THRESHOLD: '0.70' };
const flat = (o) => ({ choices: [{ message: { content: JSON.stringify(o) } }] });
const refsRA = (analysis) => ({ 'RA 응답 파싱': analysis });
let r;

console.log('#43 SAFETY-1 — RA 응답 파싱 (confidence 게이트)');

r = runNode('RA 응답 파싱', flat({ actor: 'ra_us', wp: 'WP-1', match: 'existing', confidence: 0.85, region: 'US', comment: 'ok' }), { env: env070 })[0].json;
ok('1. high 0.85 → Green (yellow_required=false)', r.yellow_required === false, JSON.stringify({ yr: r.yellow_reason }));

r = runNode('RA 응답 파싱', flat({ actor: 'ra_us', wp: null, match: 'new', confidence: 0.50, region: 'US', comment: 'low' }), { env: env070 })[0].json;
ok('2. low 0.50 → Yellow low_confidence', r.yellow_required === true && r.yellow_reason === 'low_confidence', JSON.stringify({ yr: r.yellow_reason }));

r = runNode('RA 응답 파싱', { choices: [{ message: { content: 'not-json-garbage' } }] }, { env: env070 })[0].json;
ok('3. parse error → Yellow parse_error', r.yellow_required === true && r.yellow_reason === 'parse_error', JSON.stringify({ yr: r.yellow_reason }));

r = runNode('RA 응답 파싱', flat({ actor: 'ra_us', wp: 'WP-1', match: 'existing', confidence: 0.85, region: '', comment: 'ok' }), { env: env070 })[0].json;
ok('4. missing region → Yellow missing_fields', r.yellow_required === true && r.yellow_reason === 'missing_fields' && (r.missing_fields || []).includes('region'), JSON.stringify({ mf: r.missing_fields }));

r = runNode('RA 응답 파싱', flat({ actor: 'ra_us', wp: 'WP-1', match: 'existing', confidence: 1.5, region: 'US', comment: 'bad' }), { env: env070 })[0].json;
ok('5. invalid confidence 1.5 → Yellow invalid_confidence', r.yellow_required === true && r.yellow_reason === 'invalid_confidence', JSON.stringify({ yr: r.yellow_reason }));

r = runNode('RA 응답 파싱', flat({ actor: 'ra_us', wp: 'WP-1', match: 'existing', confidence: 0.85, region: 'US', comment: 'ok' }), { env: {} })[0].json;
ok('6. threshold unconfigured → Yellow threshold_unconfigured', r.yellow_required === true && r.yellow_reason === 'threshold_unconfigured', JSON.stringify({ yr: r.yellow_reason, gate: r.yellow_gate }));

console.log('\n#44 SAFETY-2 — 기존 WP 상태 검증');

r = runNode('기존 WP 상태 검증', { status: { title: 'In Progress' }, id: '123' }, { refs: refsRA({ wp: 'WP-1' }) })[0].json;
ok('7. open WP → allowed (자율 코멘트)', r.wp_status_allowed === true && r.yellow_required === false, JSON.stringify({ a: r.wp_status_allowed }));

r = runNode('기존 WP 상태 검증', { status: { title: 'Closed' }, id: '123' }, { refs: refsRA({ wp: 'WP-1' }) })[0].json;
ok('8. closed WP → Yellow wp_closed_or_done', r.wp_status_allowed === false && r.yellow_reason === 'wp_closed_or_done', JSON.stringify({ yr: r.yellow_reason }));

r = runNode('기존 WP 상태 검증', { error: 'connection refused' }, { refs: refsRA({ wp: 'WP-1' }) })[0].json;
ok('9. lookup failed → Yellow wp_status_lookup_failed', r.wp_status_allowed === false && r.yellow_reason === 'wp_status_lookup_failed', JSON.stringify({ yr: r.yellow_reason }));

r = runNode('기존 WP 상태 검증', { status: { title: 'Open' }, id: '123' }, { refs: refsRA({ wp: null }) })[0].json;
ok('10. wp id missing → Yellow wp_id_missing', r.wp_status_allowed === false && r.yellow_reason === 'wp_id_missing', JSON.stringify({ yr: r.yellow_reason }));

r = runNode('기존 WP 상태 검증', { status: { title: 'Rejected' }, id: '123' }, { refs: refsRA({ wp: 'WP-1' }) })[0].json;
ok('11. unknown status → Yellow wp_status_unknown', r.wp_status_allowed === false && r.yellow_reason === 'wp_status_unknown', JSON.stringify({ yr: r.yellow_reason }));

console.log('\nYellow 게이트 (사람 검토 payload 매핑)');

r = runNode('Yellow 게이트 (사람 질의)', { yellow_reason: 'low_confidence', confidence: 0.5 })[0].json;
ok('12. low_confidence → 사람 payload reason 매핑', /임계값 미만/.test(r.reason), JSON.stringify({ reason: r.reason }));

r = runNode('Yellow 게이트 (사람 질의)', { yellow_reason: 'wp_closed_or_done', yellow_detail: 'WP-9 Closed' })[0].json;
ok('13. wp_closed_or_done → detail 전파', /WP-9 Closed/.test(r.reason), JSON.stringify({ reason: r.reason }));

console.log('\n=== ' + pass + ' passed, ' + fail + ' failed ===');
process.exit(fail ? 1 : 0);
