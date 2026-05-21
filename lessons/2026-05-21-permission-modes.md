# Permission Modes
_Day 5 — 2026-05-21_

> **TL;DR:** Permission modes control how much Claude can do without asking you first — picking the right one is the difference between a fast demo and an accidental file deletion.

## What it is
When Claude Code wants to run a command or edit a file, it can either ask your permission each time or just do it. The two main modes are **default (ask)** — Claude pauses and waits for your approval on risky actions — and **auto-accept** — Claude runs everything without stopping. You switch modes with the `--dangerously-skip-permissions` flag (CLI) or by pressing `Shift+Tab` in the interactive session to cycle through permission levels.

## Why a PM building voice AI / agents should care
When you're rapidly prototyping a voice agent flow or demoing to stakeholders, constant permission prompts break your momentum. Auto-accept mode lets Claude iterate fast through a safe, throwaway folder. But in your actual agent codebase — the one connected to Theatro's systems — you want the default ask mode so nothing gets overwritten without your eyes on it.

## Try it in 60 seconds
```bash
# Start a session where Claude auto-accepts all actions (use in throwaway folders only)
claude --dangerously-skip-permissions

# Or toggle mid-session: press Shift+Tab to cycle through permission levels
```

## Walk-through
1. Open a terminal in a test folder (not your real project).
2. Run `claude --dangerously-skip-permissions` to start a session where Claude acts without asking.
3. Give Claude a task like "create a hello.py file and run it."
4. Notice it creates and runs the file without stopping for approval.
5. In your real project, start Claude normally (`claude`) so it pauses before risky actions like running shell commands or deleting files.

## Gotchas
- `--dangerously-skip-permissions` is named that way on purpose — Claude can delete files, run network calls, and execute code without warning.
- The flag is meant for sandboxed CI/CD environments, not your work laptop in a live repo.
- `Shift+Tab` cycles between three levels: normal → auto-accept edits → auto-accept everything. It's easy to leave on auto-accept by accident.
- Your Bedrock-at-work setup supports this flag — no extra plan needed.

## Takeaway
Use auto-accept in a sandbox to move fast; use ask-mode in production to stay in control — same rule as root access on a server.
