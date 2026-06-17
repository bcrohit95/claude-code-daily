# /review — Using Claude to Review a Pull Request

_Day 36 — 2026-06-17_

> **TL;DR:** `/review` points Claude at the current branch's diff (the list of changes) and gives you a code review in seconds — no engineer required.

## What it is

`/review` is a built-in skill that reads the uncommitted or unmerged changes on your branch and produces a structured code review: correctness bugs, logic issues, and simplification opportunities. It reads the actual diff (what changed, line by line) rather than the whole codebase, so it's fast and focused.

## Why a PM building voice AI / agents should care

When you ship a prompt change, a new agent flow, or a config tweak, `/review` catches mistakes before they reach an engineer's inbox. For voice AI work specifically, it can flag things like a hardcoded response string that should be dynamic, or a missing error branch in an agent tool call. It reduces your dependency on eng for "does this look right?" checks.

## Try it in 60 seconds

```
/review
```

Type that in Claude Code after making any change on a branch. Claude reviews the diff and reports findings immediately.

## Walk-through

1. Make a change to any file in your repo — edit a prompt, tweak a config, update an agent definition.
2. Open Claude Code in that repo's directory.
3. Type `/review` and press Enter.
4. Claude reads the diff of your current branch vs. main and lists issues by category (bugs, simplifications, etc.).
5. Ask a follow-up like "fix the bug in step 2" and Claude applies it inline.

## Gotchas

- `/review` looks at the current branch diff — if you haven't committed anything yet, it reviews your uncommitted changes. Both work.
- It skips files you've told Claude to ignore via `.claudeignore` or `.gitignore`.
- For large diffs (hundreds of files), use `--effort low` to get a quicker, lighter pass: `/review --effort low`.
- This is a Claude Code skill, not a GitHub feature — it runs locally and doesn't post comments to your PR automatically (add `--comment` to do that).

## Takeaway

Before you ask an engineer "does this look okay?", ask `/review` first — it costs zero social capital.
