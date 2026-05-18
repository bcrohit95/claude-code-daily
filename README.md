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

- [Week of 2026-05-18](summaries/2026-05-18-week-of.md)

## Lessons

<!-- LESSON_INDEX_START -->
- [2026-05-18 — Slash Commands](lessons/2026-05-18-slash-commands.md)
<!-- LESSON_INDEX_END -->

## Manually trigger a lesson

From the repo's **Actions** tab → **Daily Claude Code Lesson** → **Run workflow**.

Or from terminal:
```
gh workflow run daily-lesson.yml
```
