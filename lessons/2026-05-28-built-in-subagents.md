# Built-in Subagents
_Day 12 — 2026-05-28_

> **TL;DR:** Claude Code ships with three ready-made subagents — Explore, Plan, and general-purpose — each optimized for a different kind of job so you get faster, cheaper, more focused results.

## What it is
A subagent (a separate Claude instance spun up to handle one focused task) comes in three built-in flavors. **Explore** is a fast read-only scout — it searches files and code but never edits anything. **Plan** is a software architect that designs an approach and lists trade-offs before any code is touched. **general-purpose** is the catch-all for everything else: research, multi-step tasks, writing, analysis.

## Why a PM building voice AI / agents should care
When you're iterating on a voice agent flow, Explore can quickly find where a specific intent or utterance is handled without wading through the whole codebase. Plan can lay out the implementation steps for a new skill before any engineer touches code — great for alignment in a standup. Using the right subagent keeps each response tight and on-point instead of sprawling.

## Try it in 60 seconds
In any Claude Code session, type this in the chat:

```
Use the Explore agent to find every file that mentions "wake word" in this repo.
```

Or to get a design before coding:

```
Use the Plan agent to sketch how I'd add a "shift handoff" intent to the voice agent.
```

## Walk-through
1. Open Claude Code in your project directory.
2. Ask Claude to use a specific built-in subagent by name: `Explore`, `Plan`, or `general-purpose`.
3. Explore returns file paths and matched lines — read-only, no side effects.
4. Plan returns a numbered implementation strategy with trade-offs — no code is written yet.
5. For anything else (summarizing, drafting, multi-step research), general-purpose takes over automatically or you can request it explicitly.

## Gotchas
- Explore reads file excerpts, not whole files — it can miss content deep in large files, so don't rely on it for exhaustive audits.
- Plan agent designs only; it won't write the code. You still need to tell Claude to implement after reviewing the plan.
- You can't customize built-in subagents (that's what custom subagents are for — coming in a future lesson).
- These subagents run inside your current session, so they share your existing permissions and model settings.

## Takeaway
Match the subagent to the job: Explore to find, Plan to design, general-purpose to do everything else.
