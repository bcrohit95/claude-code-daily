# settings.json
_Day 6 — 2026-05-22_

> **TL;DR:** The config file where Claude Code remembers your preferences — set it once, stop clicking "Allow" every session.

## What it is
A JSON (plain-text key/value format) file that controls Claude Code's behavior: which tools it can run without asking, which model to use, how it formats output. Two files exist: a global one at `~/.claude/settings.json` (your machine defaults) and a per-project one at `.claude/settings.json` (overrides for one repo). Project settings win when both exist.

## Why a PM building voice AI / agents should care
Committing a `.claude/settings.json` to your voice agent repo means every engineer on the team gets the same Claude Code behavior — same auto-approved tools, same model. For your own experiments, locking in a faster model in global settings means you're not waiting on Opus for a quick prompt tweak.

## Try it in 60 seconds
```bash
cat ~/.claude/settings.json
```
Or use the interactive config editor inside Claude Code:
```
/config
```

## Walk-through
1. Run `cat ~/.claude/settings.json` in terminal to see your current global settings (missing or empty is fine — defaults apply).
2. The `permissions.allow` list controls what Claude runs without prompting — e.g., `"Bash(git log:*)"` lets it run git log freely.
3. Add `"model": "claude-sonnet-4-6"` to default to Sonnet instead of Opus for this project.
4. Use `/config` inside Claude Code to edit settings safely — it handles JSON formatting so you don't break the file.
5. Restart Claude Code; new settings take effect on the next session start.

## Gotchas
- JSON is unforgiving — one missing comma breaks the file silently. Prefer `/config` over hand-editing.
- The project file (`.claude/settings.json`) always overrides global (`~/.claude/settings.json`), not merges — a key in the project file shadows the global value entirely.
- If you're using Claude via AWS Bedrock at work, the `model` key may require a Bedrock-specific model ID or be ignored by your setup.
- Settings written by the UI or `/config` may conflict if you also edit the file manually — pick one method and stick to it.

## Takeaway
Anything you find yourself approving or retyping every session belongs in settings.json — that's what it's for.
