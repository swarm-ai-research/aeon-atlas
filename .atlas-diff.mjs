import { execSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const cur = JSON.parse(readFileSync('atlas.json', 'utf8'));
let prev = null;
try {
  prev = JSON.parse(execSync('git show HEAD:atlas.json', { encoding: 'utf8', maxBuffer: 1 << 28 }));
} catch (e) {
  console.log('NO_PREV: could not read HEAD:atlas.json —', e.message);
}

const DAY = 86400e3;
const now = Date.now();

const curNodes = new Map(cur.nodes.map(n => [n.id, n]));
const prevNodes = new Map((prev?.nodes ?? []).map(n => [n.id, n]));

const lastCommit = n => (n.recentCommits && n.recentCommits.length ? Date.parse(n.recentCommits[0]) : null);

const new_forks = [];
const archived_forks = [];
const dormant_now_active = [];
const star_jumps = [];

for (const [id, n] of curNodes) {
  const p = prevNodes.get(id);
  if (!p) { if (!n.isRoot) new_forks.push({ id, stars: n.stars }); continue; }
  if (p.archived === false && n.archived === true) archived_forks.push({ id });
  const lc = lastCommit(n), lp = lastCommit(p);
  if (lc && lp && (lc - lp) > 7 * DAY) dormant_now_active.push({ id, advancedDays: Math.round((lc - lp) / DAY) });
  const ds = (n.stars ?? 0) - (p.stars ?? 0);
  if (ds >= 3) star_jumps.push({ id, delta: ds, stars: n.stars });
}

// new high-overlap skill pairs (weight >= 0.5)
const pairKey = e => [e.source, e.target].sort().join('::');
const isSkill = e => (e.kind || e.type) === 'skill-overlap';
const curHigh = new Map();
for (const e of (cur.edges ?? [])) {
  if (!isSkill(e)) continue;
  if (typeof e.weight === 'number' && e.weight >= 0.5) curHigh.set(pairKey(e), e.weight);
}
const prevHigh = new Set();
for (const e of (prev?.edges ?? [])) {
  if (!isSkill(e)) continue;
  if (typeof e.weight === 'number' && e.weight >= 0.5) prevHigh.add(pairKey(e));
}
const new_high_overlap = [...curHigh.keys()].filter(k => !prevHigh.has(k));

// sort
new_forks.sort((a, b) => (b.stars ?? 0) - (a.stars ?? 0));
star_jumps.sort((a, b) => b.delta - a.delta);
dormant_now_active.sort((a, b) => b.advancedDays - a.advancedDays);

// verdict
let verdict;
if (new_forks.length > 0) verdict = `${new_forks.length} new fork(s) (top: ${new_forks[0].id})`;
else if (star_jumps.length > 0) verdict = `${star_jumps[0].id} +${star_jumps[0].delta}★`;
else if (dormant_now_active.length > 0) verdict = `${dormant_now_active[0].id} resumed activity after dormancy`;
else verdict = `atlas refreshed (${cur.stats.repos}r / ${cur.stats.totalStars}★)`;

const out = {
  hasPrev: !!prev,
  prevRepos: prev?.stats?.repos ?? null,
  curRepos: cur.stats.repos,
  new_forks, archived_forks, dormant_now_active, star_jumps,
  new_high_overlap_count: new_high_overlap.length,
  verdict,
  bland: new_forks.length === 0 && star_jumps.length === 0 && dormant_now_active.length === 0,
  stats: cur.stats,
};
console.log(JSON.stringify(out, null, 2));
