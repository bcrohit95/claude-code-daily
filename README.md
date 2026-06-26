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

- [Week of 2026-06-26](summaries/2026-06-26-week-of.md)
- [Week of 2026-06-19](summaries/2026-06-19-week-of.md)
- [Week of 2026-06-12](summaries/2026-06-12-week-of.md)
- [Week of 2026-06-05](summaries/2026-06-05-week-of.md)
- [Week of 2026-05-29](summaries/2026-05-29-week-of.md)
- [Week of 2026-05-22](summaries/2026-05-22-week-of.md)
- [Week of 2026-05-18](summaries/2026-05-18-week-of.md)

## Lessons

<!-- LESSON_INDEX_START -->
- [2026-06-25 — Putting It All Together](lessons/2026-06-25-putting-it-all-together.md)
- [2026-06-24 — The Claude Agent SDK](lessons/2026-06-24-claude-agent-sdk.md)
- [2026-06-23 — Debugging Claude's Mistakes — Re-Prompting Strategies](lessons/2026-06-23-debugging-claudes-mistakes.md)
- [2026-06-22 — Git Workflows with Claude](lessons/2026-06-22-git-workflows.md)
- [2026-06-21 — Worktrees — Running Claude on an Isolated Copy of the Repo](lessons/2026-06-21-worktrees.md)
- [2026-06-20 — Cost and Rate Limits — Practical Tips to Stay Under](lessons/2026-06-20-cost-and-rate-limits.md)
- [2026-06-19 — Prompt Caching — What It Is and How It Saves Money](lessons/2026-06-19-prompt-caching.md)
- [2026-06-18 — Model Selection — When to Use Opus vs Sonnet vs Haiku](lessons/2026-06-18-model-selection.md)
- [2026-06-17 — /review — Using Claude to Review a Pull Request](lessons/2026-06-17-review-command.md)
- [2026-06-16 — /init — Generating a CLAUDE.md for an Existing Project](lessons/2026-06-16-init-command.md)
- [2026-06-15 — Output Styles](lessons/2026-06-15-output-styles.md)
- [2026-06-14 — Status Line](lessons/2026-06-14-status-line.md)
- [2026-06-13 — Keyboard Shortcuts Worth Memorizing](lessons/2026-06-13-keyboard-shortcuts.md)
- [2026-06-12 — IDE Extensions](lessons/2026-06-12-ide-extensions.md)
- [2026-06-11 — GitHub Actions Integration](lessons/2026-06-11-github-actions.md)
- [2026-06-10 — Headless Mode](lessons/2026-06-10-headless-mode.md)
- [2026-06-09 — Web Search and WebFetch](lessons/2026-06-09-web-search-webfetch.md)
- [2026-06-08 — Image Input](lessons/2026-06-08-image-input.md)
- [2026-06-07 — Parallel Tool Calls](lessons/2026-06-07-parallel-tool-calls.md)
- [2026-06-06 — The Bash Tool](lessons/2026-06-06-bash-tool.md)
- [2026-06-05 — The Read, Edit, and Write Tools](lessons/2026-06-05-read-edit-write-tools.md)
- [2026-06-04 — Tasks](lessons/2026-06-04-tasks.md)
- [2026-06-03 — Memory Tool](lessons/2026-06-03-memory-tool.md)
- [2026-06-02 — Connecting an MCP Server](lessons/2026-06-02-connecting-mcp-server.md)
- [2026-06-01 — MCP (Model Context Protocol)](lessons/2026-06-01-mcp.md)
- [2026-05-31 — Creating a Custom Skill](lessons/2026-05-31-custom-skills.md)
- [2026-05-30 — Skills](lessons/2026-05-30-skills.md)
- [2026-05-29 — Custom Subagents](lessons/2026-05-29-custom-subagents.md)
- [2026-05-28 — Built-in Subagents](lessons/2026-05-28-built-in-subagents.md)
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
