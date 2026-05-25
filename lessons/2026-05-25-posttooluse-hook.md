# PostToolUse Hook
_Day 9 — 2026-05-25_

> **TL;DR:** Run a shell command automatically after Claude edits a file — great for auto-formatting or writing an audit trail of every change Claude makes.

## What it is
PostToolUse hooks fire after a specific tool completes. You wire up a shell command in `settings.json` and Claude Code runs it every time that tool finishes. Unlike PreToolUse (which can block a tool), PostToolUse just reacts — it can't stop the action, but it can log it, format it, or kick off a follow-up.

## Why a PM building voice AI / agents should care
When you're iterating on prompt files or agent configs, a PostToolUse hook can automatically log every file Claude touches to a simple text file — giving you a change diary without having to remember to write anything down. It's also useful when demoing: auto-format on save means the code you show stakeholders always looks clean, even if Claude wrote it messily.

## Try it in 60 seconds
Add this to your `.claude/settings.json` (inside the `hooks` object):

```json
"PostToolUse": [
  {
    "matcher": "Write",
    "hooks": [
      {
        "type": "command",
        "command": "echo \"$(date): wrote $CLAUDE_TOOL_INPUT_FILE_PATH\" >> ~/claude-changes.log"
      }
    ]
  }
]
```

Now every file Claude writes gets logged to `~/claude-changes.log`.

## Walk-through
1. Open `.claude/settings.json` (create it if it doesn't exist).
2. Add a `hooks` key if it's not already there.
3. Under `PostToolUse`, set `matcher` to the tool you want to watch — `Write`, `Edit`, or `Bash` are the most common.
4. Set `command` to any shell command; Claude Code passes tool details as environment variables like `CLAUDE_TOOL_INPUT_FILE_PATH`.
5. Save the file, then ask Claude to edit something — your hook runs silently after.

## Gotchas
- PostToolUse **cannot** cancel or undo a tool call — it only runs after the fact. Use PreToolUse if you need to block.
- Environment variables available in the hook depend on which tool fired; not every tool exposes a file path.
- The hook runs in a subprocess — if it exits non-zero, Claude Code surfaces an error in the transcript but continues.
- Heavy hooks (e.g. running a full test suite) will slow down every edit. Save that for Stop hooks instead.

## Takeaway
PostToolUse is your silent co-pilot: it can't steer, but it takes notes — use it to log, format, or notify without interrupting Claude's flow.
