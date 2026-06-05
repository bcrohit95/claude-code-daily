# The Read, Edit, and Write Tools
_Day 20 — 2026-06-05_

> **TL;DR:** Claude has three distinct tools for working with files — Read, Edit, and Write — and picking the wrong one wastes tokens or risks overwriting your work.

## What it is
**Read** opens a file so Claude can see its contents. **Edit** makes a targeted change inside an existing file (like find-and-replace with context). **Write** overwrites the entire file from scratch. They're not interchangeable — each has a specific job.

## Why a PM building voice AI / agents should care
When you ask Claude to tweak a prompt in your agent config, you want Edit — not Write, which would nuke every other setting in the file. Understanding which tool Claude is reaching for tells you how risky an operation is: Read is always safe, Edit is surgical, Write is a full replacement.

## Try it in 60 seconds
Open Claude Code and ask it to change one word in any existing file:

```
In my README.md, change the word "simple" to "straightforward" on line 3.
```

Watch the tool call it makes. You'll see Edit — not Write — because only one line changes.

## Walk-through
1. Claude always runs **Read** first before Edit or Write — it needs to see the file before touching it.
2. **Edit** finds your exact `old_string`, replaces it with `new_string`, and leaves everything else alone.
3. If the `old_string` appears more than once, Edit fails and asks for more context — it won't guess which instance you meant.
4. **Write** is used when creating a brand-new file or when rewriting the whole thing is genuinely the right call.
5. In permission prompts, Edit shows a diff (the before/after); Write shows the entire new content — use that as a signal to double-check.

## Gotchas
- If you ask Claude to "rewrite" something, it may reach for Write. Say "update" or "change" to nudge it toward Edit.
- Read only loads up to 2,000 lines by default — very large files get truncated.
- Write will silently overwrite unsaved work. If a file has uncommitted edits, commit first.
- These tools work on local files only. They can't reach URLs or attached documents.

## Takeaway
Edit is a scalpel; Write is a sledgehammer — the right one depends on how much of the file you actually want to change.
