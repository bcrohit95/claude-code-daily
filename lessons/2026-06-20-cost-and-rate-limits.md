# Cost and Rate Limits — Practical Tips to Stay Under
_Day 35 — 2026-06-20_

> **TL;DR:** Claude API usage costs real money and has speed caps — knowing a handful of habits keeps you from surprise bills and throttle errors.

## What it is
Every message you send through Claude Code burns tokens (words and word-fragments). Anthropic bills by the token and also caps how many you can send per minute (rate limits). Hit the cost limit on your API key and Claude stops. Hit the rate limit and you get a temporary "too many requests" error.

## Why a PM building voice AI / agents should care
When you prototype agent flows — looping through conversation transcripts, iterating on prompts, running automated tests — the token count compounds fast. A single mistaken loop can burn more than a week's experiment budget in minutes. Knowing the levers means you can prototype freely without a CFO conversation afterward.

## Try it in 60 seconds
Open the Anthropic Console to see real-time spend and set a monthly limit:

```
https://console.anthropic.com/settings/limits
```

Set a **monthly spend limit** (e.g., $20) so runaway scripts can't overdraft you.

## Walk-through
1. Go to `console.anthropic.com` → **Settings → Limits** and set a hard monthly spend cap.
2. In Claude Code, type `/model` and switch to **Haiku** for exploration tasks — it's 20–30× cheaper than Opus for the same context.
3. Use `/compact` when a session gets long — it summarizes history into fewer tokens without losing the thread.
4. Keep system prompts short and reuse them with prompt caching (yesterday's lesson) so repeated calls don't re-bill the same instructions.
5. If you hit a rate limit error, wait 60 seconds and retry — the limit resets per minute, not per day.

## Gotchas
- Rate limits are per API key, not per user — a shared team key hitting limits blocks everyone simultaneously.
- The spend limit in Console applies to your whole API key, not just Claude Code — any app using the same key counts.
- Haiku is fast and cheap but sometimes misses subtle nuance in complex agent reasoning; use it for retrieval/routing, Sonnet or Opus for decision steps.
- If you're on Bedrock at work, cost and limits are controlled by your AWS account, not the Anthropic Console — ask your infra team what guardrails are already in place.

## Takeaway
One `/model` switch to Haiku and a monthly spend cap in Console buys you freedom to experiment without fear.
