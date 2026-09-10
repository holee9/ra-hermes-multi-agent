// #82 review (2026-09-09) reproduced two aggregation defects against the real aggregate():
//   1. the same actor submitting "approve" twice satisfied quorum=2 -> approved
//   2. one vote on topic A plus one vote on topic B -> topic A approved
// These tests pin the input-integrity rules: same topic, valid vote, one vote per actor,
// allow-listed actors (when weights are configured), with exclusions reported in `ignored`.
const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('path');
const { aggregate } = require(path.join(__dirname, '..', 'voting', 'vote-aggregator.js'));

// Live rules: quorum 2, weights for infra_t3610/gx10/rpi, majority 0.66.
const T = 'topic-restart-honcho';

test('duplicate actor votes count once — quorum not met', () => {
  const r = aggregate([
    { actor: 'infra_t3610', vote: 'approve', topic: T },
    { actor: 'infra_t3610', vote: 'approve', topic: T },
  ]);
  assert.equal(r.result, 'pending');
  assert.equal(r.method, 'quorum_not_met');
  assert.equal(r.votes_received, 1);
  assert.equal(r.ignored.duplicate_actor.length, 1);
});

test('votes on another topic are excluded, not merged', () => {
  const r = aggregate([
    { actor: 'infra_t3610', vote: 'approve', topic: T },
    { actor: 'infra_gx10', vote: 'approve', topic: 'other-topic' },
  ]);
  assert.equal(r.result, 'pending');
  assert.equal(r.ignored.topic_mismatch.length, 1);
});

test('unknown actor (not in weights allow-list) is excluded', () => {
  const r = aggregate([
    { actor: 'infra_t3610', vote: 'approve', topic: T },
    { actor: 'ra_us', vote: 'approve', topic: T },
  ]);
  assert.equal(r.result, 'pending');
  assert.equal(r.ignored.unknown_actor.length, 1);
});

test('invalid vote values are excluded', () => {
  const r = aggregate([
    { actor: 'infra_t3610', vote: 'yes', topic: T },
    { actor: 'infra_gx10', vote: 'approve', topic: T },
  ]);
  assert.equal(r.result, 'pending');
  assert.equal(r.ignored.invalid_vote.length, 1);
});

test('two distinct allowed actors approving on the same topic is approved', () => {
  const r = aggregate([
    { actor: 'infra_t3610', vote: 'approve', topic: T },
    { actor: 'infra_gx10', vote: 'approve', topic: T },
  ]);
  assert.equal(r.result, 'approved');
  assert.deepEqual(r.voters, ['infra_t3610', 'infra_gx10']);
  assert.deepEqual(r.ignored, { invalid_record: [], topic_mismatch: [], invalid_vote: [], duplicate_actor: [], unknown_actor: [] });
});

test('2 approve vs 1 reject meets 0.66 threshold; 1 vs 1 does not', () => {
  assert.equal(aggregate([
    { actor: 'infra_t3610', vote: 'approve', topic: T },
    { actor: 'infra_gx10', vote: 'approve', topic: T },
    { actor: 'infra_rpi', vote: 'reject', topic: T },
  ]).result, 'approved');
  assert.equal(aggregate([
    { actor: 'infra_t3610', vote: 'approve', topic: T },
    { actor: 'infra_gx10', vote: 'reject', topic: T },
  ]).result, 'rejected');
});

test('empty input stays pending/no_votes', () => {
  assert.equal(aggregate([]).method, 'no_votes');
});

// #82 review round 2 (2026-09-10): topic-less approvals were approved; null / non-string
// records threw TypeError out of aggregate().
test('votes without a topic never approve', () => {
  const r = aggregate([
    { actor: 'infra_t3610', vote: 'approve' },
    { actor: 'infra_gx10', vote: 'approve' },
  ]);
  assert.equal(r.result, 'pending');
  assert.equal(r.method, 'no_topic');
  assert.equal(r.topic, '');
});

test('empty-string topic is treated as no topic', () => {
  assert.equal(aggregate([{ actor: 'infra_t3610', vote: 'approve', topic: '  ' }]).method, 'no_topic');
});

test('null / non-object records are excluded, not thrown', () => {
  assert.equal(aggregate([null]).method, 'no_topic');
  const r = aggregate([null, 'str', 42, { actor: 'infra_t3610', vote: 'approve', topic: T },
                       { actor: 'infra_gx10', vote: 'approve', topic: T }]);
  assert.equal(r.result, 'approved');
  assert.equal(r.ignored.invalid_record.length, 3);
});

test('non-string vote / actor / topic are excluded, not thrown', () => {
  const r = aggregate([
    { actor: 'infra_t3610', vote: 1, topic: T },
    { actor: 42, vote: 'approve', topic: T },
    { actor: 'infra_gx10', vote: 'approve', topic: { x: 1 } },
    { actor: 'infra_rpi', vote: 'approve', topic: T },
  ]);
  assert.equal(r.result, 'pending');            // only infra_rpi counts → quorum 2 not met
  assert.equal(r.ignored.invalid_vote.length, 1);
  assert.equal(r.ignored.unknown_actor.length, 1);
  assert.equal(r.ignored.topic_mismatch.length, 1);
});

test('non-array input returns a structured invalid_input result', () => {
  assert.equal(aggregate(null).method, 'no_votes');
  assert.equal(aggregate({ actor: 'x' }).result, 'invalid_input');
  assert.equal(aggregate('approve').result, 'invalid_input');
});
