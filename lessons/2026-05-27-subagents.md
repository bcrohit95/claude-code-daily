# Subagents
_Day 11 — 2026-05-27_

> **TL;DR:** Subagents are Claude instances Claude spawns to handle a focused task in parallel — less waiting, less context bloat.

## What it is
When you give Claude a big task, it can delegate pieces to specialized "subagents" — fresh Claude instances that each tackle one focused job, then report back. Think of it like your main Claude being the project lead and spinning up contractors for specific work. Each subagent has its own clean context (the working memory of the conversation) so it doesn't get confused by unrelated details.

## Why a PM building voice AI / agents should care
When you're prototyping a voice agent flow, you might ask Claude to research three different API integrations at once — with subagents, those searches run in parallel instead of sequentially, cutting your wait time significantly. It also means Claude can read dozens of files without the main conversation getting overloaded with noise. Less context clutter = better answers.

## Try it in 60 seconds
Just ask Claude to do parallel work:
```
Research both the Twilio Voice API and Amazon Polly at the same time, 
then compare them for a frontline worker voice app. Use separate agents 
for each so they run in parallel.
```

## Walk-through
1. Claude receives your request and recognizes two independent research tasks.
2. It spawns two subagent instances — one per API — via the built-in `Agent` tool.
3. Both subagents run concurrently (at the same time), each doing its own search or file reads.
4. Each subagent returns a result to the main Claude.
5. Main Claude synthesizes both results into a single answer for you.

## Gotchas
- Subagents don't share context with each other — each starts fresh with only what the main Claude tells it.
- You can't directly control which subagent does what; Claude decides how to split the work.
- Spawning many subagents on large tasks can increase cost, since each runs its own model calls.
- Subagents only appear in the CLI (terminal) and API; the web UI handles parallelism differently.

## Takeaway
Subagents are Claude's way of multitasking — use them when your question has two or more independent parts that don't need each other's answers to proceed.
