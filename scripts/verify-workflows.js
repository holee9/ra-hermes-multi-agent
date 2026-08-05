#!/usr/bin/env node
const fs = require('fs');
const { aggregate } = require('../voting/vote-aggregator');

const jsonFiles = [
  'package.json',
  'voting/config/vote-rules.json',
  'bridge/config/bridge-config.json',
  'feedback/config/weight-adjustment-config.json',
  'feedback/config/growth-trigger-config.json',
  'scripts/cold-start-config.json',
  'scripts/growth-targets.json',
  'scripts/device-map.json',
  'n8n/workflows/mail-triage.json',
  'n8n/workflows/infra-to-work-bridge.json',
  'n8n/workflows/infra-vote-broadcast.json',
  'n8n/workflows/feedback-recorder.json',
  'n8n/workflows/form-triage-draft.json',
  'n8n/workflows/wp-close-recorder.json',
];

for (const file of jsonFiles) {
  JSON.parse(fs.readFileSync(file, 'utf8'));
  console.log(`JSON OK ${file}`);
}

for (const file of jsonFiles.filter((file) => file.startsWith('n8n/workflows/'))) {
  const workflow = JSON.parse(fs.readFileSync(file, 'utf8'));
  for (const node of workflow.nodes || []) {
    if (node.type !== 'n8n-nodes-base.code') continue;
    try {
      new Function(node.parameters.jsCode);
      console.log(`Code OK ${file} :: ${node.name}`);
    } catch (error) {
      console.error(`Code FAIL ${file} :: ${node.name}`);
      throw error;
    }
  }
}

const mailTriage = JSON.parse(fs.readFileSync('n8n/workflows/mail-triage.json', 'utf8'));
const mailNodeNames = new Set((mailTriage.nodes || []).map((node) => node.name));
for (const requiredNode of ['Layer 4 조회 준비', 'Layer 4 규제 DB 조회', 'Layer 4 컨텍스트 주입']) {
  if (!mailNodeNames.has(requiredNode)) {
    throw new Error(`mail-triage missing ${requiredNode}`);
  }
}
const mailText = JSON.stringify(mailTriage);
// Secret-leak guard. The literal key must NOT live here: this file is committed,
// so embedding the value to detect it is itself the leak it guards against (the
// value was exposed in git history until 2026-08-05). Check the env-provided key
// when available, and always run a shape-based scan so the guard still works when
// API_SERVER_KEY is unset.
const secretsToReject = [process.env.API_SERVER_KEY].filter(Boolean);
for (const forbidden of secretsToReject) {
  if (mailText.includes(forbidden)) {
    throw new Error('mail-triage contains hardcoded API bearer token');
  }
}
// Shape-based: a Bearer header carrying a long opaque literal instead of an
// n8n expression ({{...}} / credential reference).
const bearerLiteral = /Bearer\s+(?!\{\{)[A-Za-z0-9._-]{32,}/;
if (bearerLiteral.test(mailText)) {
  throw new Error('mail-triage contains a hardcoded Bearer literal — use a credential or expression');
}
if (!mailText.includes('/v1/knowledge/fetch')) {
  throw new Error('mail-triage does not call Layer 4 knowledge endpoint');
}
if (!mailText.includes('layer4_context')) {
  throw new Error('mail-triage does not inject layer4_context into RA prompt');
}
console.log('Layer 4 workflow wiring OK n8n/workflows/mail-triage.json');

const hermesApiServer = fs.readFileSync('scripts/hermes-api-server.py', 'utf8');
if (!hermesApiServer.includes('@app.route("/v1/knowledge/fetch"')) {
  throw new Error('hermes-api-server.py missing /v1/knowledge/fetch endpoint');
}
console.log('Layer 4 API endpoint OK scripts/hermes-api-server.py');

const growthTriggerConfig = JSON.parse(fs.readFileSync('feedback/config/growth-trigger-config.json', 'utf8'));
const knownMetrics = new Set([
  'correction_rate',
  'first_pass_match_accuracy',
  'confidence_calibration',
  'warmstart_lift',
  'escalation_precision',
  'autonomous_study_sessions',
  'study_insights_count',
  'absence_pattern_signals',
  'duplicate_wp_rate_7d_ma',
]);
for (const [name, trigger] of Object.entries(growthTriggerConfig.triggers || {})) {
  if (!knownMetrics.has(trigger.metric)) {
    throw new Error(`Trigger ${name} references unknown metric: ${trigger.metric}`);
  }
  if (!['above', 'below'].includes(trigger.direction)) {
    throw new Error(`Trigger ${name} has invalid direction: ${trigger.direction}`);
  }
  if (trigger.threshold !== null && (typeof trigger.threshold !== 'number' || trigger.threshold < 0)) {
    throw new Error(`Trigger ${name} threshold must be null or non-negative number`);
  }
}
const webhookUrl = growthTriggerConfig.notification?.n8n_webhook_url;
if (webhookUrl !== null && webhookUrl !== undefined && !/^https?:\/\//.test(String(webhookUrl))) {
  throw new Error('growth-trigger-config notification.n8n_webhook_url must be null or http(s) URL');
}
console.log('Growth trigger config OK feedback/config/growth-trigger-config.json');

const pending = aggregate([{ actor: 'infra_t3610', vote: 'approve', topic: 'disk-alert' }]);
if (pending.result !== 'pending' || pending.method !== 'quorum_not_met') {
  throw new Error('Vote aggregator quorum fixture failed');
}
const approved = aggregate([
  { actor: 'infra_t3610', vote: 'approve', topic: 'disk-alert' },
  { actor: 'infra_gx10', vote: 'approve', topic: 'disk-alert' },
  { actor: 'infra_rpi', vote: 'reject', topic: 'disk-alert' },
]);
if (approved.result !== 'approved' || approved.method !== 'threshold_0.66') {
  throw new Error('Vote aggregator approval fixture failed');
}
console.log('Vote rules OK voting/config/vote-rules.json');
