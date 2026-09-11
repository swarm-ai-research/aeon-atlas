#!/usr/bin/env node
/**
 * Aeon MCP Server
 *
 * Exposes all Aeon skills as MCP tools so any Claude Desktop or Claude Code
 * user can invoke them directly from their Claude interface.
 *
 * Tool naming: aeon-{slug} (e.g. aeon-article, aeon-hacker-news-digest)
 * Each tool accepts a single optional `var` argument (the skill's variable input).
 *
 * Skill execution: spawns `claude -p -` with the skill prompt, exactly as
 * GitHub Actions does, so local runs are identical to scheduled runs.
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { readFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { spawnSync } from "child_process";
import { randomUUID } from "crypto";
import type { Session } from "@amplitude/ai";
import { ai, skillRunnerAgent } from "./amplitude.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// mcp-server/dist/index.js → mcp-server/ → repo root
const REPO_ROOT = join(__dirname, "..", "..");

interface Skill {
  slug: string;
  name: string;
  description: string;
  category: string;
  schedule: string;
  var: string;
}

interface SkillsManifest {
  version: string;
  repo: string;
  skills: Skill[];
}

function loadSkills(): Skill[] {
  const manifestPath = join(REPO_ROOT, "skills.json");
  if (!existsSync(manifestPath)) {
    process.stderr.write(
      `[aeon-mcp] skills.json not found at ${manifestPath}\n`
    );
    return [];
  }
  const manifest: SkillsManifest = JSON.parse(
    readFileSync(manifestPath, "utf-8")
  );
  return manifest.skills ?? [];
}

function skillToToolName(slug: string): string {
  return `aeon-${slug}`;
}

function toolNameToSlug(toolName: string): string {
  return toolName.replace(/^aeon-/, "");
}

function buildTools(skills: Skill[]) {
  return skills.map((skill) => ({
    name: skillToToolName(skill.slug),
    description: buildDescription(skill),
    inputSchema: {
      type: "object" as const,
      properties: {
        var: {
          type: "string",
          description: buildVarDescription(skill),
        },
      },
      required: [],
    },
  }));
}

function buildDescription(skill: Skill): string {
  const categoryLabel = categoryName(skill.category);
  const scheduleLabel =
    skill.schedule === "on-demand"
      ? "on-demand"
      : `cron: ${skill.schedule}`;
  return `[Aeon · ${categoryLabel}] ${skill.description} (${scheduleLabel})`;
}

function buildVarDescription(skill: Skill): string {
  if (skill.var) return skill.var;
  const defaults: Record<string, string> = {
    research: "Topic or keyword to focus the skill on (e.g. 'AI agents'). Leave empty for auto-selection.",
    dev: "Repo in owner/repo format to narrow scope. Leave empty to scan all watched repos.",
    crypto: "Token symbol or contract address to focus on. Leave empty for all tracked tokens.",
    social: "Topic, handle, or keyword. Leave empty to use configured defaults.",
    productivity: "Focus area or goal. Leave empty for general operation.",
  };
  return (
    defaults[skill.category] ??
    `Optional variable input for the ${skill.name} skill.`
  );
}

function categoryName(category: string): string {
  const labels: Record<string, string> = {
    research: "Research",
    dev: "Dev",
    crypto: "Crypto",
    social: "Social",
    productivity: "Productivity",
  };
  return labels[category] ?? category;
}

interface ClaudeCliResult {
  result?: string;
  is_error?: boolean;
  total_cost_usd?: number;
  usage?: {
    input_tokens?: number;
    output_tokens?: number;
    cache_read_input_tokens?: number;
    cache_creation_input_tokens?: number;
  };
}

async function runSkill(slug: string, varValue: string): Promise<string> {
  const skillFile = join(REPO_ROOT, "skills", slug, "SKILL.md");
  if (!existsSync(skillFile)) {
    return [
      `Error: skill '${slug}' not found.`,
      `Expected SKILL.md at: ${skillFile}`,
      `Make sure you're running the MCP server from inside an Aeon repo clone.`,
    ].join("\n");
  }

  const today = new Date().toISOString().split("T")[0];
  let prompt = `Today is ${today}. Read and execute the skill defined in skills/${slug}/SKILL.md`;

  if (varValue.trim()) {
    prompt += `\n\nUse this variable (override the default in the skill file):\nvar=${varValue.trim()}`;
  }

  process.stderr.write(`[aeon-mcp] Running skill: ${slug}${varValue ? ` (var=${varValue})` : ""}\n`);

  if (!skillRunnerAgent) {
    return spawnClaudeCli(slug, prompt);
  }

  // Each MCP tool call is a single, self-contained skill run — not a
  // continued conversation — so it gets its own session.
  const session = skillRunnerAgent.session({ sessionId: randomUUID() });
  try {
    return await session.run(async (s) => {
      s.trackUserMessage(`Run skill: ${slug}`, {
        context: { slug, var: varValue.trim() || null },
      });
      return spawnClaudeCli(slug, prompt, s);
    });
  } finally {
    await ai!.flush();
  }
}

function spawnClaudeCli(slug: string, prompt: string, session?: Session): string {
  const start = Date.now();
  const result = spawnSync("claude", ["-p", "-", "--output-format", "json"], {
    input: prompt,
    cwd: REPO_ROOT,
    timeout: 600_000, // 10 minutes — same as GitHub Actions timeout
    maxBuffer: 10 * 1024 * 1024, // 10 MB
    encoding: "utf-8",
  });
  const latencyMs = Date.now() - start;

  if (result.error) {
    const msg = (result.error as NodeJS.ErrnoException).code === "ENOENT"
      ? `'claude' command not found. Install it with: npm install -g @anthropic-ai/claude-code`
      : `Failed to spawn claude: ${result.error.message}`;
    session?.trackAiMessage("", "claude-code-cli", "anthropic", latencyMs, {
      isError: true,
      errorMessage: msg,
    });
    return `Error: ${msg}`;
  }

  const stdout = (result.stdout || "").trim();
  const parsed = parseClaudeCliOutput(stdout);

  if (result.status !== 0) {
    const output = (result.stderr || stdout || "").trim();
    session?.trackAiMessage(parsed?.result ?? "", "claude-code-cli", "anthropic", latencyMs, {
      ...usageFields(parsed),
      isError: true,
      errorMessage: `Skill '${slug}' failed (exit ${result.status})`,
    });
    return `Skill '${slug}' failed (exit ${result.status}):\n${output}`;
  }

  if (!stdout) {
    session?.trackAiMessage("", "claude-code-cli", "anthropic", latencyMs, {
      isError: true,
      errorMessage: "empty output",
    });
    return `Skill '${slug}' produced no output.`;
  }

  session?.trackAiMessage(parsed?.result ?? stdout, "claude-code-cli", "anthropic", latencyMs, {
    ...usageFields(parsed),
    isError: parsed?.is_error === true,
  });

  return parsed?.result ?? stdout;
}

// The claude CLI with --output-format json wraps the reply in { result: "..." },
// plus usage/cost fields when the run succeeds.
function parseClaudeCliOutput(stdout: string): ClaudeCliResult | null {
  try {
    return JSON.parse(stdout) as ClaudeCliResult;
  } catch {
    return null;
  }
}

// Anthropic's raw `input_tokens` excludes cache tokens — the AI SDK expects
// the cache-inclusive total. total_cost_usd comes straight from the CLI, so
// it's passed through rather than re-derived from a (possibly unrecognized) model name.
function usageFields(parsed: ClaudeCliResult | null) {
  const usage = parsed?.usage;
  if (!usage) return {};
  const inputTokens =
    (usage.input_tokens ?? 0) + (usage.cache_read_input_tokens ?? 0) + (usage.cache_creation_input_tokens ?? 0);
  return {
    inputTokens,
    outputTokens: usage.output_tokens,
    totalTokens: usage.output_tokens !== undefined ? inputTokens + usage.output_tokens : undefined,
    cacheReadTokens: usage.cache_read_input_tokens,
    cacheCreationTokens: usage.cache_creation_input_tokens,
    totalCostUsd: parsed?.total_cost_usd,
  };
}

// ---- Server setup ----

const server = new Server(
  { name: "aeon-mcp", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

const skills = loadSkills();
const tools = buildTools(skills);

process.stderr.write(
  `[aeon-mcp] Loaded ${skills.length} skills from ${REPO_ROOT}\n`
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools }));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const toolName = request.params.name;
  const slug = toolNameToSlug(toolName);
  const skill = skills.find((s) => s.slug === slug);

  if (!skill) {
    return {
      content: [
        {
          type: "text" as const,
          text: `Unknown Aeon tool: ${toolName}\nAvailable tools: ${tools.map((t) => t.name).join(", ")}`,
        },
      ],
      isError: true,
    };
  }

  const varValue = (request.params.arguments?.var as string) ?? "";
  const output = await runSkill(slug, varValue);

  return {
    content: [{ type: "text" as const, text: output }],
  };
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  process.stderr.write("[aeon-mcp] Server running on stdio\n");
}

main().catch((err: unknown) => {
  process.stderr.write(`[aeon-mcp] Fatal error: ${err}\n`);
  process.exit(1);
});
