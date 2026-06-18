# Model Selection — When to Use Opus vs Sonnet vs Haiku
_Day 37 — 2026-06-18_

> **TL;DR:** Claude has three tiers of models; picking the right one for the task saves money and speeds up your workflow without sacrificing quality.

## What it is
Anthropic ships three model tiers under the Claude 4.x family: **Haiku** (fastest, cheapest), **Sonnet** (balanced — the Claude Code default), and **Opus** (most capable, slower, pricier). There's also **Fable 5** for creative/narrative work. Claude Code defaults to Sonnet, but you can switch per-session or per-command.

## Why a PM building voice AI / agents should care
When you're iterating fast on prompts for a voice agent — tweaking intents, testing edge-case transcripts, checking rephrasing — running Opus on every attempt burns time and budget. Haiku handles quick "does this response sound right?" checks; save Opus for the tricky reasoning tasks like analyzing a 50-call transcript or deciding on agent architecture.

## Try it in 60 seconds
Start a Claude Code session on a specific model:

```bash
claude --model claude-haiku-4-5-20251001
```

Or switch mid-session by typing `/model` at the Claude Code prompt to pick interactively.

## Walk-through
1. Open a Claude Code session normally — it defaults to `claude-sonnet-4-6`.
2. Type `/model` and press Enter to see available models and select one.
3. For a quick one-off task, pass `--model claude-haiku-4-5-20251001` when launching.
4. For the hardest tasks (long doc analysis, complex agent design), pass `--model claude-opus-4-8`.
5. Toggle **Fast mode** with `/fast` — it runs Opus at higher throughput when you need power without the wait.

## Gotchas
- Haiku is great for speed but will miss nuance on complex multi-step reasoning — don't use it to audit agent logic.
- Switching models mid-session resets some context optimizations; try to pick before a long task.
- Opus costs roughly 5–10x more per token than Haiku — watch this if Claude Code is on a shared team budget.
- If your company uses Bedrock (AWS-hosted Claude), model availability depends on what your AWS admin has enabled; not all tiers may be accessible.

## Takeaway
Default to Sonnet, drop to Haiku when you're just spot-checking, and reach for Opus only when the task genuinely needs it — your token budget will thank you.
