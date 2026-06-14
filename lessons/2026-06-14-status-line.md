# Status Line
_Day 29 — 2026-06-14_

> **TL;DR:** The status line is the info bar above Claude Code's input prompt — you can customize it to show exactly what you need at a glance.

## What it is
The status line sits at the top of the Claude Code terminal UI. By default it shows the current model, token count, and a few other stats. You can change what it displays by setting `statusLine` in your `settings.json` (the config file at `~/.claude/settings.json`).

## Why a PM building voice AI / agents should care
When you're iterating on a voice agent prompt, you're burning tokens fast. Having the token count or cost visible at a glance tells you when a session is getting expensive before you hit a limit. If you work across multiple projects (different agent configs, different models), showing the working directory or current model in the status line means you always know which context you're in.

## Try it in 60 seconds
Open Claude Code and type:
```
/config
```
Navigate to **Status Line** and pick a preset, or set it manually in `~/.claude/settings.json`:
```json
{
  "statusLine": "model tokens"
}
```
Restart Claude Code — the status bar updates immediately.

## Walk-through
1. Open `~/.claude/settings.json` in any text editor (or via `/config` inside Claude Code).
2. Add or update the `"statusLine"` key with the fields you want.
3. Available tokens you can include: `model`, `tokens`, `cost`, `cwd` (current working directory), `git` (branch name), `duration`.
4. Separate multiple fields with a space: `"statusLine": "model tokens cost git"`.
5. Save the file and restart Claude Code to see the change.

## Gotchas
- `cost` tracking is approximate — it estimates based on token count, not the actual Bedrock invoice.
- The `/config` UI lets you pick presets; to mix-and-match fields, edit `settings.json` directly.
- If the status line shows nothing after your edit, check for a JSON syntax error in `settings.json` (a missing comma will silently break it).
- Status line is terminal-only — no equivalent in the VS Code extension sidebar.

## Takeaway
Pin `model` and `tokens` to your status line so you always know what you're running and what it's costing — before a session surprises you.
