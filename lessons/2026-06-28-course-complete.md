# Course Complete — Your Claude Code Reference Card and What to Build Next
_Day 41 — 2026-06-28_

> **TL;DR:** You've covered the full Claude Code toolkit — here's a one-page cheat sheet and three concrete things to build next for your voice AI work.

## What it is
This is the final lesson. Over 40 days you went from slash commands to custom agents, MCP servers, hooks, and a full voice AI workflow. That's the whole surface area of Claude Code. Now the goal shifts from learning features to using them on real problems.

## Why a PM building voice AI / agents should care
You now have enough pieces to stop asking engineering for one-off scripts and start shipping your own prototypes — transcript analyzers, prompt iteration tools, demo builders. The gap between "PM with ideas" and "PM who ships" is just familiarity with the tools, and you have that now.

## Try it in 60 seconds
Open any project you're working on and run:

```
claude "/init"
```

If you haven't already, this generates a `CLAUDE.md` tuned to that project — the single fastest way to make Claude actually useful in a new codebase.

## Walk-through — Quick Reference

1. **Automate repetition** → Hooks (`PreToolUse`, `PostToolUse`, `Stop`) run shell commands around every tool call.
2. **Give Claude project memory** → `CLAUDE.md` at the root; `.claude/agents/` for custom subagents.
3. **Pull in live data** → MCP servers for GitHub, Slack, your database — no copy-paste.
4. **Run without babysitting** → Headless mode + GitHub Actions for nightly jobs (transcript summaries, prompt regression tests).
5. **Build a real agent** → Claude Agent SDK when you need something that loops, branches, or calls external APIs on its own.

## What to build next

Three starter projects sized for a PM, each buildable in a weekend:

**1. Transcript analyzer** — a custom skill that reads a call transcript, extracts missed intents, and outputs a markdown report. Combines `/init`, a custom skill, and the `Read` tool.

**2. Prompt regression suite** — a headless Claude job that runs your top 10 voice prompts against a fixed test set and flags regressions. Uses GitHub Actions + the Agent SDK.

**3. Demo builder** — a Claude agent that takes a feature spec and generates a simulated conversation flow for stakeholder demos. One custom subagent, one MCP connection to your notes tool.

## Gotchas
- Complexity compounds fast — start with one piece (a hook, a skill, an MCP server) before wiring them all together.
- `CLAUDE.md` is your most underused lever; most PMs skip it and then wonder why Claude forgets context.
- If something feels tedious (copy-pasting, re-explaining context every session), that's a signal to automate it — not to accept it.
- The curriculum covered the tools; the judgment of when to use each one only comes from building real things.

## Takeaway
The best next move isn't reading more — it's picking the most annoying part of your current voice AI workflow and automating it this week.
