# Claude Code Daily

A self-running learning agent that teaches me one Claude Code skill every day at 8am CST.

## How it works

1. GitHub Actions wakes up at 13:00 UTC (8am CDT / 7am CST after DST ends)
2. Claude Code reads `curriculum.md`, picks the next `[TODO]` topic
3. Writes a plain-English lesson with an example and how to try it
4. Saves the lesson to `lessons/YYYY-MM-DD-topic.md` and commits it
5. Marks the topic `[DONE]` in the curriculum and updates this README index — second commit
6. Emails the lesson to me

## Weekly summaries

- [Week of 2026-05-22](summaries/2026-05-22-week-of.md)
- [Week of 2026-05-18](summaries/2026-05-18-week-of.md)

## Lessons

<!-- LESSON_INDEX_START -->
- [2026-05-27 — Subagents](lessons/2026-05-27-subagents.md)
- [2026-05-26 — Stop Hook](lessons/2026-05-26-stop-hook.md)
- [2026-05-25 — PostToolUse Hook](lessons/2026-05-25-posttooluse-hook.md)
- [2026-05-24 — PreToolUse Hook](lessons/2026-05-24-pretooluse-hook.md)
- [2026-05-23 — Hooks](lessons/2026-05-23-hooks.md)
- [2026-05-22 — settings.json](lessons/2026-05-22-settings-json.md)
- [2026-05-21 — Permission Modes](lessons/2026-05-21-permission-modes.md)
- [2026-05-20 — Plan Mode](lessons/2026-05-20-plan-mode.md)
- [2026-05-19 — CLAUDE.md Files](lessons/2026-05-19-claude-md-files.md)
- [2026-05-18 — Custom Slash Commands](lessons/2026-05-18-custom-slash-commands.md)
- [2026-05-18 — Slash Commands](lessons/2026-05-18-slash-commands.md)
<!-- LESSON_INDEX_END -->

## Manually trigger a lesson

From the repo's **Actions** tab → **Daily Claude Code Lesson** → **Run workflow**.

Or from terminal:
```
gh workflow run daily-lesson.yml
```
