# Day 38: Prompt Caching — What It Is and How It Saves Money

**TL;DR:** Prompt caching lets you mark the stable parts of your prompt so Claude reuses them instead of re-processing them every request. Cache reads cost ~10% of normal; cache writes cost ~125%. If you send the same large system prompt on every turn, caching pays for itself on the second call.

---

## What it is

Every API call you make, Claude reads your entire prompt from scratch. If you have a 5,000-token system prompt describing your voice agent's persona, Claude re-reads all 5,000 tokens every single time — and you pay for them.

Prompt caching lets you mark a stable prefix (the part that doesn't change) with a `cache_control` flag. Claude stores it for 5 minutes. The next call that sends the same prefix hits the cache instead of re-processing, and you pay ~10× less for those tokens.

---

## Why a PM should care

If you're building voice AI that calls Claude dozens of times per conversation — for transcription, intent detection, response generation — your big system prompt is being charged at full price on every single call. Caching cuts that cost by up to 90% on repeated calls. At scale, this is the difference between a profitable product and an expensive one.

---

## Try it in 60 seconds

In your `messages.create()` call, add `cache_control` to your system prompt:

```python
client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system=[{
        "type": "text",
        "text": "You are a helpful voice assistant for Theatro...",
        "cache_control": {"type": "ephemeral"}
    }],
    messages=[{"role": "user", "content": "What's my shift schedule?"}]
)
```

Check the response: `response.usage.cache_read_input_tokens` — if it's greater than zero, the cache is working.

---

## Walk-through

**How it works:** Claude caches everything up to the marked block. The next request with that exact same prefix hits the cache. Any change before the marker — even a single character — invalidates it.

**Render order matters:** Claude processes `tools` → `system` → `messages`. Put stable content first, volatile content (the user's question) last.

**TTLs:** Default is 5 minutes. Add `"ttl": "1h"` for a 1-hour cache — useful if your traffic is bursty. Writing a 1-hour cache costs ~2× normal (vs 1.25× for 5-min), so you need at least 3 reads to break even.

**Minimum size:** The prefix must be at least 1,024–4,096 tokens to cache (varies by model). Short prompts simply won't cache — no error, just no savings.

---

## Gotchas

- **Any dynamic content in the cached block breaks it.** A timestamp, user name, or request ID embedded in your system prompt? The cache never hits. Move dynamic content to the user message.
- **Requires the Anthropic API directly.** Prompt caching isn't available on Amazon Bedrock or Vertex AI.
- **Cache writes cost more.** The first call after the cache expires pays the write premium. High-traffic workloads recover this quickly; very low-traffic ones may not.

---

## Takeaway

Add `cache_control` to your system prompt. Check `cache_read_input_tokens` to confirm it's working. Keep volatile content (the user's question) after the cache marker. That's 90% of the savings with 10% of the effort.
