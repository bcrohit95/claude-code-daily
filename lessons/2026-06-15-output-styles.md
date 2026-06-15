# Output Styles
_Day 30 — 2026-06-15_

> **TL;DR:** You control how talkative Claude is — ask for a one-liner or a deep dive, set a default in CLAUDE.md, or toggle the verbose tool-call display with `/verbose`.

## What it is
Claude Code doesn't have a single fixed response style — it adjusts based on how you ask. You can request a short answer, a detailed breakdown, or a structured list. Separately, `/verbose` controls whether you see the internal tool calls (file reads, shell commands) Claude runs behind the scenes.

## Why a PM building voice AI / agents should care
When you're prototyping a voice agent flow, you often want quick answers: "does this intent match?" not a four-paragraph essay. Pinning a concise style in CLAUDE.md means every session starts lean — you only go detailed when you ask. That's faster iteration and less noise when you're moving fast.

## Try it in 60 seconds
Add this to your `.claude/CLAUDE.md` to make concise the default for a project:

```
Respond concisely by default. Use bullet points over paragraphs.
Only give a detailed explanation when I ask for one.
```

Or just type it inline any time:
```
in one sentence: what does this function do?
```

## Walk-through
1. Open any Claude Code session and ask a question the normal way — note the response length.
2. Ask the same question prefixed with "in one sentence:" — the answer shrinks immediately.
3. Type `/verbose` and press Enter to toggle verbose mode on. You'll now see every tool call (read, edit, bash) Claude makes as it works.
4. Type `/verbose` again to turn it off — cleaner output for sharing or demos.
5. Open (or create) `.claude/CLAUDE.md` and add a style line to lock your preferred default across all sessions.

## Gotchas
- `/verbose` controls *tool call* display, not response length — they're independent dials.
- A one-line instruction in your message always wins over CLAUDE.md defaults for that turn.
- Asking for "brief" doesn't suppress code blocks — Claude will still show full code when it's editing files.
- This is all prompt-level behavior, not a settings.json key — there's no `outputStyle: "concise"` config option.

## Takeaway
One line in CLAUDE.md sets the tone for every session; one prefix in your message overrides it for one turn.
