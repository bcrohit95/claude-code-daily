# Custom Subagents
_Day 13 — 2026-05-29_

> **TL;DR:** You can define your own specialized Claude subagent in a markdown file — give it a name, a persona, and specific tools — so it's always ready to handle one job really well.

## What it is
A custom subagent is a markdown file you drop in `.claude/agents/`. The frontmatter (the block at the top between `---` lines) names the agent and tells Claude when to use it. The body becomes the system prompt — the standing instructions that shape how it thinks and responds. Claude Code loads these automatically and can delegate to them by name.

## Why a PM building voice AI / agents should care
You could create a `transcript-reviewer` agent that knows your grading rubric and critiques every agent conversation the same way, every time. Or a `prompt-drafter` that always formats voice intents in your team's template. Instead of re-explaining context each session, you encode it once and reuse it forever — less repetition, more consistent output.

## Try it in 60 seconds
Create a file at `.claude/agents/transcript-reviewer.md`:

```markdown
---
name: transcript-reviewer
description: Reviews voice agent transcripts for missed intents and awkward phrasing
---

You review transcripts from a voice AI assistant for frontline workers.
Flag: missed intents, confusing responses, and any turn > 2 sentences.
Output a bullet list. Be blunt.
```

Then in Claude Code, type:
```
Use the transcript-reviewer agent to review this transcript: [paste transcript]
```

## Walk-through
1. Create the folder `.claude/agents/` in your project root if it doesn't exist.
2. Add a new `.md` file — the filename becomes the agent's slug (e.g., `transcript-reviewer.md`).
3. Write the frontmatter: `name` (display name), `description` (one line — Claude uses this to decide when to invoke the agent).
4. Write the body: plain English instructions, your rubric, your output format. Think of it as a permanent sticky note for that agent.
5. Ask Claude to use the agent by name, or let Claude pick it automatically when the task matches the description.

## Gotchas
- The `description` field is how Claude decides when to auto-route to your agent — write it like a rule, not a label. ("Reviews voice transcripts" beats "transcript stuff".)
- You can add `model: claude-haiku-4-5-20251001` to the frontmatter to use a cheaper, faster model for routine tasks like formatting or grading.
- Custom agents inherit your session's permissions by default; add a `tools` list in the frontmatter to restrict what they can do.
- Changes to the file take effect immediately — no restart needed.

## Takeaway
A custom subagent is just a markdown file: write it once, and Claude has a specialist on call forever.
