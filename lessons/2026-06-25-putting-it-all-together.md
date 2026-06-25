# Putting It All Together
_Day 40 — 2026-06-25_

> **TL;DR:** Every skill from this curriculum becomes more powerful when you wire them together — here's the short stack that matters most for voice AI PM work.

## What it is

You've now seen 39 individual Claude Code features. The real unlock is combining them: a CLAUDE.md that primes Claude with your product context, an MCP server that pulls live data, hooks that enforce quality, and a custom skill that wraps your most-used workflow into one command.

## Why a PM building voice AI / agents should care

A voice AI prototype has moving parts — prompt design, transcript analysis, agent flow iteration, stakeholder demos. Each of those is a job Claude can do, but only if it has the right context, tools, and guardrails wired up. The stack below cuts your setup time from "explain everything every session" to "open and go."

## Try it in 60 seconds

```
# The four-file starter kit for a voice AI project
.claude/
  settings.json        ← permissions + model choice
  commands/analyze.md  ← /analyze custom slash command for transcripts
  agents/pm-assistant.md ← agent tuned for product decisions
CLAUDE.md              ← project context (product, users, constraints)
```

## Walk-through

1. **Start with CLAUDE.md.** Write two paragraphs: what the product does and who the end users are (e.g., "frontline retail workers using push-to-talk devices"). This primes every session.
2. **Add a custom skill or slash command for your most repeated task.** For voice AI, that's usually `/analyze` — paste a call transcript, get a structured summary with intent, errors, and suggested prompt fixes.
3. **Configure a stop hook** to run a lint or format check after every edit, so you're not shipping broken JSON configs to your agent pipeline.
4. **Create a custom subagent** (`pm-assistant.md`) that knows your product vocabulary — intents, wake words, escalation flows — so it gives relevant answers without re-explaining every time.
5. **Connect the GitHub MCP server** so Claude can open PRs and comment on issues directly, cutting the loop between "Claude wrote the fix" and "fix is in review."

## Gotchas

- CLAUDE.md is the highest-leverage file — a vague one means Claude guesses your context every session. Spend 10 minutes writing a good one; it pays back daily.
- Don't try to set everything up at once. Wire one thing per week: CLAUDE.md first, then a custom command, then a hook.
- MCP servers require the server binary to be installed locally — check the server's docs before expecting it to just work.
- This lesson assumes the Claude.ai or local CLI setup; Bedrock users: confirm which features your company's deployment exposes before building a workflow around them.

## Takeaway

The curriculum ends, but the toolkit compounds — each piece you wire up makes every future session faster and more context-aware.
