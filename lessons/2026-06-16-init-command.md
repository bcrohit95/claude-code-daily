# /init — Generating a CLAUDE.md for an Existing Project

_Day 31 — 2026-06-16_

> **TL;DR:** `/init` makes Claude read your whole project and write its own first draft of `CLAUDE.md` — so you skip the blank-page problem.

## What it is
`/init` is a built-in slash command (a `/`-prefixed shortcut typed into Claude Code). It scans your project's files — folder structure, README, package files, scripts — and drafts a `CLAUDE.md` (the standing briefing file Claude reads every session, covered in an earlier lesson) summarizing what it found.

## Why a PM building voice AI / agents should care
You jump between repos a lot — the voice agent backend, a prompt-template repo, a demo sandbox — and writing `CLAUDE.md` from scratch each time is friction you'll skip under deadline pressure. `/init` gives you a real draft in under a minute, so the project briefing actually gets written instead of staying a someday-task.

## Try it in 60 seconds
```
cd your-project
claude
/init
```
Claude reads the repo and proposes a `CLAUDE.md`. Review it, then accept.

## Walk-through
1. Open a terminal and `cd` into the project's root folder.
2. Start Claude Code by typing `claude`.
3. Type `/init` and press Enter.
4. Claude explores the codebase (reading files, listing folders) and writes a draft `CLAUDE.md`.
5. Read the draft, edit anything wrong or missing, then save and commit it.

## Gotchas
- The draft is a starting point, not gospel — it can misread intent from file names alone. Always skim it before trusting it.
- If a `CLAUDE.md` already exists, `/init` will revise it — check `git diff` afterward so you don't silently lose hand-written notes.
- It only sees what's in the repo. Context that lives in your head (why a workaround exists, what's off-limits) still needs to be added by hand.
- Large repos take longer and use more of the session's context — fine for a one-time setup step, but don't run it repeatedly out of habit.

## Takeaway
`/init` doesn't replace writing `CLAUDE.md` — it replaces staring at an empty one.
