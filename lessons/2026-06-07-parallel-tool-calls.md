# Parallel Tool Calls
_Day 22 — 2026-06-07_

> **TL;DR:** Claude can run multiple independent actions at the same time — cutting wait time roughly in half when tasks don't depend on each other.

## What it is
By default, Claude does one thing, waits for the result, then does the next. Parallel tool calls let it kick off several independent actions simultaneously — reading three files at once, running two searches at the same time — and gather all the results before moving on.

## Why a PM building voice AI / agents should care
When you're iterating on a voice agent, you often need to pull context from multiple places at once — a transcript file, a prompt config, a schema. Without parallelism, Claude reads them one by one. With it, it reads all three in a single round trip, so your feedback loop is noticeably faster when prototyping.

## Try it in 60 seconds
Just ask Claude to do two independent things in one message:

```
Read both `prompts/greeting.txt` and `logs/last-session.json` and tell me if they're consistent.
```

Claude will fetch both files in parallel automatically — no special syntax needed.

## Walk-through
1. Open a Claude Code session in your project folder.
2. Ask for two independent pieces of information in a single message (e.g., read two files, search two terms).
3. Watch the tool-call panel — you'll see both calls fire nearly simultaneously.
4. Claude combines the results and responds once both are done.
5. Compare the time to doing it in two separate messages — the parallel version is faster.

## Gotchas
- Claude decides whether calls can run in parallel — if task B depends on task A's result, it will still wait.
- You can't force parallelism; you can only set it up by asking for truly independent things at once.
- Very large parallel reads can hit rate limits (API request caps) faster than sequential ones.
- In headless/CI mode the speedup matters more; in interactive sessions you'll mostly just notice it's snappier.

## Takeaway
Group independent questions into one message — Claude will parallelize them so you wait less.
