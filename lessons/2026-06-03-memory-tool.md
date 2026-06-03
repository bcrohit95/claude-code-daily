# Memory Tool
_Day 18 — 2026-06-03_

> **TL;DR:** Claude can save notes about you and your project to disk and recall them in future sessions — so you don't re-explain context every time.

## What it is
Claude Code has a file-based memory system stored at `~/.claude/projects/<your-project>/memory/`. Each memory is a tiny markdown file with a category (user, feedback, project, reference). Claude reads these automatically at the start of each session, so it already knows your preferences, quirks, and project context before you type a word.

## Why a PM building voice AI / agents should care
Every time you start a new Claude session, you'd normally re-explain "I'm a PM at Theatro, we build voice AI for frontline workers, we use Bedrock." Memory eliminates that. More practically: when you tell Claude how you like prompts structured for your agent flows, or which stakeholders it should never mention in commit messages, it remembers. That's real time saved across dozens of sessions.

## Try it in 60 seconds
Type this directly in Claude Code:

```
Remember: I prefer agent responses in under 150 words for our voice UI —
frontline workers hear these, they can't read a wall of text.
```

Claude saves a memory file. Next session, that constraint is already loaded.

## Walk-through
1. Open Claude Code in any project session.
2. Say `Remember: <something about your preferences or project>`.
3. Claude writes a markdown file under `~/.claude/projects/.../memory/`.
4. End the session. Start a new one in the same project.
5. Claude silently loads those memories — your constraint is active without you repeating it.

## Gotchas
- Memories are **per-project** (scoped by working directory path), not global across all your repos.
- Claude decides what's worth saving — it won't memorize every passing comment, only things it judges as durable. You can force it by saying "remember this."
- Stale memories can mislead Claude if your project changes significantly. Periodically say `forget that I said X` or ask Claude to review its memories.
- This is Claude Code's own system, not an official "Memory tool" you'll find in API docs — the name varies by context.

## Takeaway
One `Remember:` sentence today saves you two minutes of re-explaining context in every future session.
