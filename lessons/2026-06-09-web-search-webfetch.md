# Web Search and WebFetch
_Day 24 — 2026-06-09_

> **TL;DR:** Two tools that let Claude pull live information from the internet mid-session, so your AI isn't stuck on what it knew at training time.

## What it is
WebSearch runs a search query and returns results. WebFetch (fetch = retrieve) downloads a specific URL and hands the contents to Claude. Both run inside your session — Claude reads the results and uses them to answer you, write code, or update a file.

## Why a PM building voice AI / agents should care
Voice AI moves fast. New Whisper models, updated Alexa/Copilot APIs, competitor launches — your Claude session has a knowledge cutoff and will confidently give you stale answers without these tools. Use WebSearch to pull current docs before writing an integration, or WebFetch to read a vendor's changelog before deciding if a feature exists yet.

## Try it in 60 seconds
Type this directly in Claude Code:

```
Search the web for "Amazon Nova Sonic API released 2025" and summarize what's new.
```

Or to fetch a specific page:

```
Fetch https://docs.anthropic.com/en/docs/about-claude/models/overview and tell me the latest model names.
```

## Walk-through
1. Open Claude Code in any project (the tools work in any session).
2. Type a question that needs current info — mention "search the web" or "fetch this URL."
3. Claude calls WebSearch or WebFetch automatically, retrieves the content, and reads it.
4. Claude answers based on the live content, not its training data.
5. You can chain it: "Search for X, then fetch the first result and extract the pricing table."

## Gotchas
- WebSearch isn't Google — it uses a search API (Brave by default) and returns summaries, not full pages. For full content, follow up with WebFetch on a specific URL.
- WebFetch can't log in. Password-protected pages, Slack, Notion — anything behind auth returns nothing or an error.
- Some pages block automated fetches (HTTP 403). If it fails, try the raw docs URL instead of the marketing page.
- If you're running Claude Code via AWS Bedrock at work, check whether your organization has enabled these tools — they make outbound network calls, which some security policies restrict.

## Takeaway
When Claude sounds confident but could be outdated, ask it to search first — real-time data beats training data every time.
