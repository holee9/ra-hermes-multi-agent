/**
 * Vote Aggregator [IF]
 *
 * 인터페이스 자리만 구현 — 집계 규칙은 의도적 공백.
 * config/vote-rules.json에서 읽은 규칙으로 동작.
 * config가 비어 있으면 단순 다수결로 fallback (명시적으로 기록).
 *
 * Input:  [{ actor: string, vote: "approve"|"reject"|"abstain", topic: string }]
 * Output: { topic: string, result: "approved"|"rejected"|"pending", method: string, tally: object }
 */

const fs = require('fs');
const path = require('path');

function loadRules() {
  const configPath = path.join(__dirname, 'config', 'vote-rules.json');
  try {
    return JSON.parse(fs.readFileSync(configPath, 'utf8'));
  } catch {
    return {};
  }
}

/**
 * @param {Array<{actor: string, vote: string, topic: string}>} votes
 * @returns {{ topic: string, result: string, method: string, tally: object }}
 */
function aggregate(votes) {
  if (!votes || votes.length === 0) {
    return { topic: '', result: 'pending', method: 'no_votes', tally: {} };
  }

  const topic = votes[0].topic;
  const rules = loadRules();

  const quorum = rules.quorum ?? null;
  const weights = rules.weights ?? {};
  const majorityThreshold = rules.majority_threshold ?? null;
  const fallbackMethod = rules.fallback_method ?? 'simple_majority';

  // 입력 무결성 (#82 리뷰 재현: 동일 actor 2표로 quorum 충족, 다른 topic 표가 섞여 가결).
  // 정족수·비율에는 (a) 같은 topic, (b) 유효한 vote 값, (c) actor당 1표(첫 표만),
  // (d) weights가 정의돼 있으면 명단 안의 actor만 포함한다. 제외분은 ignored로 보고한다.
  const allowed = Object.keys(weights);
  const ignored = { topic_mismatch: [], invalid_vote: [], duplicate_actor: [], unknown_actor: [] };
  const seenActors = new Set();
  const counted = [];
  for (const v of votes) {
    const normalized = v?.vote?.toLowerCase();
    if (v?.topic !== topic) { ignored.topic_mismatch.push(v); continue; }
    if (!(normalized === 'approve' || normalized === 'reject' || normalized === 'abstain')) { ignored.invalid_vote.push(v); continue; }
    if (!v.actor) { ignored.unknown_actor.push(v); continue; }
    if (allowed.length > 0 && !allowed.includes(v.actor)) { ignored.unknown_actor.push(v); continue; }
    if (seenActors.has(v.actor)) { ignored.duplicate_actor.push(v); continue; }
    seenActors.add(v.actor);
    counted.push({ actor: v.actor, vote: normalized, topic });
  }
  votes = counted;

  const tally = { approve: 0, reject: 0, abstain: 0 };
  for (const v of votes) tally[v.vote]++;

  // 정족수 미충족 → pending (고유 actor의 유효표 기준)
  if (quorum !== null && votes.length < quorum) {
    return { topic, result: 'pending', method: 'quorum_not_met', tally, quorum_required: quorum, votes_received: votes.length, ignored };
  }

  // 가중치 적용 (설정된 경우)
  let weightedApprove = tally.approve;
  let weightedReject = tally.reject;
  if (Object.keys(weights).length > 0) {
    weightedApprove = votes
      .filter(v => v.vote?.toLowerCase() === 'approve')
      .reduce((sum, v) => sum + (weights[v.actor] ?? 1), 0);
    weightedReject = votes
      .filter(v => v.vote?.toLowerCase() === 'reject')
      .reduce((sum, v) => sum + (weights[v.actor] ?? 1), 0);
  }

  const totalDecisive = weightedApprove + weightedReject;
  if (totalDecisive === 0) {
    return { topic, result: 'pending', method: 'all_abstained', tally, ignored };
  }

  const approveRatio = weightedApprove / totalDecisive;

  // 가결 임계 적용 (설정된 경우), 미설정 시 단순 다수결
  const threshold = majorityThreshold ?? 0.5;
  const method = majorityThreshold !== null
    ? `threshold_${threshold}`
    : `fallback_${fallbackMethod}`;

  const result = approveRatio > threshold ? 'approved' : 'rejected';

  return {
    topic,
    result,
    method,
    tally,
    weighted: { approve: weightedApprove, reject: weightedReject },
    approve_ratio: Math.round(approveRatio * 100) / 100,
    voters: votes.map(v => v.actor),
    ignored
  };
}

module.exports = { aggregate };

// n8n Function 노드에서 직접 실행 시:
// const { aggregate } = require('./vote-aggregator');
// return [{ json: aggregate($input.all().map(i => i.json)) }];
