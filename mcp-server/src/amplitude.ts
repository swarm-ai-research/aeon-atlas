/**
 * Amplitude Agent Analytics bootstrap.
 *
 * This server has no in-process LLM SDK call site — `runSkill()` spawns the
 * `claude` CLI as a subprocess and parses its `--output-format json` reply.
 * There's no OpenAI/Anthropic client object for @amplitude/ai to wrap, so
 * each skill run is tracked manually as a one-turn agent session, using the
 * usage/cost fields the CLI itself reports.
 */
import { AmplitudeAI, AIConfig } from "@amplitude/ai";

const apiKey = process.env.AMPLITUDE_AI_API_KEY;

if (!apiKey) {
  process.stderr.write(
    "[aeon-mcp] AMPLITUDE_AI_API_KEY missing — agent analytics disabled\n"
  );
}

export const ai = apiKey
  ? new AmplitudeAI({
      apiKey,
      config: new AIConfig({ contentMode: "full", redactPii: true }),
    })
  : null;

// Module-level singleton — re-creating this per call would give every turn
// a different Agent ID and break session grouping in Agent Analytics.
export const skillRunnerAgent = ai
  ? ai.agent("aeon-skill-runner", {
      description:
        "Spawns the Claude Code CLI (`claude -p`) to execute an Aeon skill and returns its result.",
    })
  : null;
