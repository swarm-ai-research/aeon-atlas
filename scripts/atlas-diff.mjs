import { execSync } from "node:child_process";
import { readFileSync } from "node:fs";

const cur = JSON.parse(readFileSync("atlas.json", "utf8"));
let prev = null;
try {
  prev = JSON.parse(execSync("git show HEAD:atlas.json", { encoding: "utf8", maxBuffer: 64 * 1024 * 1024 }));
} catch (e) {
  console.log("NO_PREV");
}

const byId = (arr) => new Map((arr || []).map((n) => [n.id, n]));
const curNodes = byId(cur.nodes);
const prevNodes = prev ? byId(prev.nodes) : new Map();

const days = (a, b) => (new Date(a) - new Date(b)) / 86400000;

// new_forks
const new_forks = [...curNodes.keys()].filter((id) => prev && !prevNodes.has(id));
// archived_forks: false -> true
const archived_forks = [...curNodes.values()]
  .filter((n) => prevNodes.get(n.id) && prevNodes.get(n.id).archived === false && n.archived === true)
  .map((n) => n.id);
// dormant_now_active: pushedAt advanced > 7 days
const dormant_now_active = [...curNodes.values()]
  .filter((n) => {
    const p = prevNodes.get(n.id);
    return p && n.pushedAt && p.pushedAt && days(n.pushedAt, p.pushedAt) > 7;
  })
  .map((n) => ({ id: n.id, prev: prevNodes.get(n.id).pushedAt, now: n.pushedAt }));
// star_jumps: stars increased by >= 3
const star_jumps = [...curNodes.values()]
  .map((n) => ({ id: n.id, delta: (n.stars || 0) - ((prevNodes.get(n.id) || {}).stars || 0) }))
  .filter((x) => prevNodes.has(x.id) && x.delta >= 3)
  .sort((a, b) => b.delta - a.delta);

// new_high_overlap: skill-overlap pairs weight>=0.5 that didn't exist last run
const keyOf = (e) => [e.source, e.target].sort().join("::");
const prevOverlap = new Set(
  (prev ? prev.edges : []).filter((e) => e.kind === "skill-overlap" && e.weight >= 0.5).map(keyOf)
);
const new_high_overlap = (cur.edges || [])
  .filter((e) => e.kind === "skill-overlap" && e.weight >= 0.5 && !prevOverlap.has(keyOf(e)))
  .map((e) => ({ pair: `${e.source} ⇄ ${e.target}`, weight: e.weight }));

// verdict
let verdict;
if (new_forks.length > 0) verdict = `${new_forks.length} new fork(s) (top: ${new_forks[0]})`;
else if (star_jumps.length > 0) verdict = `${star_jumps[0].id} +${star_jumps[0].delta}★`;
else if (dormant_now_active.length > 0) verdict = `${dormant_now_active[0].id} resumed activity after dormancy`;
else verdict = `atlas refreshed (${cur.stats.repos}r / ${cur.stats.totalStars}★)`;

const out = {
  hasPrev: !!prev,
  verdict,
  new_forks,
  archived_forks,
  dormant_now_active,
  star_jumps,
  new_high_overlap,
  stats: cur.stats,
};
console.log(JSON.stringify(out, null, 2));
