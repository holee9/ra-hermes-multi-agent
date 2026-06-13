#!/usr/bin/env node
const fs = require('fs');

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
  'n8n/workflows/feedback-recorder.json',
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
