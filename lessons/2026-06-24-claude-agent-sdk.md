# Day 39 — The Claude Agent SDK: Building Your Own Agent on Top of Claude

**Date:** 2026-06-24
**Topic:** The Claude Agent SDK — building your own agent on top of Claude

---

## TL;DR

The Claude Agent SDK is Anthropic's official Python/TypeScript library that lets you build Claude-powered agents in your own code. The key feature: a **tool runner** that automatically loops between Claude and your functions until the task is done.

---

## What it is

The Agent SDK wraps Anthropic's API so you can build agents without managing the conversation loop yourself. You define tools (functions Claude can call), hand them to the SDK, and it handles everything: calling Claude, detecting tool requests, running your function, feeding the result back, and repeating until Claude finishes.

Install it with:

```bash
pip install anthropic
```

---

## Why a PM building voice AI / agents should care

Your frontline voice agent needs to *do things* — look up a shift, check inventory, file a work order. Without the SDK, you'd hand-code the loop: call Claude → check if it wants a tool → run the tool → feed result back → repeat. The tool runner does that for you. You write the tools; the SDK writes the loop.

This also unlocks the Anthropic **Managed Agents** surface (`client.beta.agents`, `sessions`, `environments`) where Anthropic hosts the entire execution environment — your agent gets a container with bash, file access, and web search included.

---

## Try it in 60 seconds

```python
from anthropic import Anthropic, beta_tool

client = Anthropic()  # set ANTHROPIC_API_KEY in your environment

@beta_tool
def get_shift(worker_id: str) -> str:
    """Look up a worker's next shift."""
    return f"Worker {worker_id} is scheduled Tuesday 7am–3pm."

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[get_shift],
    messages=[{"role": "user", "content": "When does worker 42 work next?"}],
)

for message in runner:
    for block in message.content:
        if block.type == "text":
            print(block.text)
```

---

## Walk-through

1. **Install** the SDK: `pip install anthropic`
2. **Decorate** your function with `@beta_tool` — the SDK reads the docstring and type hints to build the tool definition automatically
3. **Pass the tool** to `tool_runner()` alongside a normal `messages.create()` call
4. **Iterate** over the runner — each item is a message; you stop when the loop ends naturally
5. **Read text blocks** from the final message for Claude's answer

The runner calls your function zero or more times before producing a final response. You never write the loop.

---

## Gotchas

- **`@beta_tool` is beta** — import from `anthropic`, not a sub-module; the API may shift
- **Model matters** — use `claude-opus-4-8` for agentic work; Haiku lacks the reasoning to use tools reliably
- **Secrets stay with you** — if your tool hits an internal API, your API keys live in your function, not in Claude's context
- **Managed Agents is a separate surface** — `client.beta.agents` + `sessions` is for Anthropic-hosted sandboxes; the tool runner above runs locally

---

## Takeaway

The Claude Agent SDK turns "call Claude, check if it needs a tool, run it, repeat" into two lines: a decorated function and a `tool_runner()` call. That loop — which is the core of any voice AI agent — is now the SDK's problem, not yours.
