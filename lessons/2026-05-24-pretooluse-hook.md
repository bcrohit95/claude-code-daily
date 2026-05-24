# PreToolUse Hook
_Day 8 — 2026-05-24_

> **TL;DR:** A PreToolUse hook runs a shell script *before* Claude executes any tool — and if your script exits with a non-zero code (meaning "failed"), Claude is blocked from running that tool at all.

## What it is
Yesterday's Hooks lesson introduced the concept. PreToolUse is the type that acts as a gatekeeper. Claude passes the pending tool call to your script as JSON (structured data) on stdin (standard input — the way programs feed data to each other). Your script reads it, decides allow or deny, and exits `0` to allow or anything else to block.

## Why a PM building voice AI / agents should care
When you hand Claude access to a live system — a transcript database, a staging API, a voice agent config — one bad command can overwrite real data. A PreToolUse hook is a one-time config that silently enforces rules you'd otherwise have to remember to say in every prompt.

## Try it in 60 seconds
Add this to `.claude/settings.json` to block any Bash command containing `rm -rf`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'input=$(cat); echo \"$input\" | grep -q \"rm -rf\" && exit 1 || exit 0'"
          }
        ]
      }
    ]
  }
}
```

## Walk-through
1. Open `.claude/settings.json` (or create it at the root of your project).
2. Add a `"PreToolUse"` entry under `"hooks"`.
3. Set `"matcher"` to `"Bash"` to target only shell commands (or `"Edit"` for file edits, or `""` for everything).
4. Write a shell command that reads stdin, checks for a dangerous pattern, and exits non-zero if it should be blocked.
5. Test by asking Claude to run `rm -rf tmp/` — it should refuse and explain it was blocked.

## Gotchas
- Your hook script must read stdin (`cat` or `read`) even if you don't use it — otherwise the pipe hangs and Claude stalls.
- Exit code `2` is special: Claude receives your script's stderr as an error message and can tell you *why* it was blocked. Exit code `1` blocks silently.
- Hooks run locally; they won't protect a teammate who doesn't have the same `settings.json`.
- Overly broad matchers (blocking all Bash) will frustrate you fast — start narrow, like matching only specific dangerous patterns.

## Takeaway
A PreToolUse hook is a seat belt: you configure it once, forget about it, and it saves you the one time Claude would have done something you couldn't undo.
