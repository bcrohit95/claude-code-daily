# Creating a Custom Skill
_Day 15 — 2026-05-31_

> **TL;DR:** Write a markdown file in `.claude/skills/` and you get a reusable slash command that runs a whole workflow — tailored to your exact project.

## What it is
A custom skill is a plain markdown file with a short YAML header (called frontmatter — the block between `---` lines at the top). The header names the skill and describes when to use it. The body is plain English instructions Claude follows every time you invoke the skill. No code required.

## Why a PM building voice AI / agents should care
You probably repeat the same review tasks constantly: pull a transcript, flag agent errors, suggest a prompt fix. Wrapping that in a skill means one command instead of re-explaining the steps every session. You can also hand skills to teammates so they run your workflow exactly, every time.

## Try it in 60 seconds
Create this file at `.claude/skills/transcript-review.md`:

```markdown
---
description: Review the latest voice agent transcript for errors and suggest a prompt fix
---

Read the most recent file in `transcripts/`.
Summarize the conversation in 3 bullets.
List any turns where the agent misunderstood the user.
Suggest one prompt change to reduce errors.
```

Then in Claude Code, type `/transcript-review`.

## Walk-through
1. Create the folder if it doesn't exist: `.claude/skills/` inside your project root.
2. Add a new `.md` file — the filename becomes the slash command name (e.g. `transcript-review.md` → `/transcript-review`).
3. Write the YAML frontmatter block with at least a `description:` field.
4. Below the frontmatter, write plain English steps exactly as you'd prompt Claude manually.
5. Open Claude Code in that project and type `/` — your skill appears in the list.

## Gotchas
- The skill file must live inside `.claude/skills/` relative to your project root, or in `~/.claude/skills/` for global use.
- Filename = command name, so use lowercase kebab-case (words joined by hyphens) — spaces and capitals cause issues.
- Skills run in the current session context, so they can read files in your project — point them at the right paths in the instructions.
- There's no "skill debugger" — if it misbehaves, read the file and tighten the instructions like you'd refine any prompt.

## Takeaway
A custom skill is just a prompt you wrote once, stored in a file, so you never have to repeat yourself.
