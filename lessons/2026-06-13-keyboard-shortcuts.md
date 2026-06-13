# Keyboard Shortcuts Worth Memorizing
_Day 28 — 2026-06-13_

> **TL;DR:** Five keystrokes eliminate the most common friction in a Claude Code session — learn them and you'll stop reaching for the mouse.

## What it is
Claude Code is a terminal app, so almost everything is keyboard-driven. A handful of shortcuts handle the situations that come up every session: stopping a runaway response, writing a multi-line prompt, and jumping back to something you typed earlier.

## Why a PM building voice AI / agents should care
When you're iterating on prompts for a voice agent, you often need to mid-course-correct — Claude starts going in the wrong direction and you want to stop it without waiting. Or you're drafting a long, structured prompt and need line breaks without accidentally submitting. These shortcuts keep that loop tight.

## Try it in 60 seconds
```
# While Claude is generating a response, press:
Escape          # stops generation immediately

# When typing a prompt that needs multiple lines:
Shift+Enter     # new line without submitting

# To revisit a prompt you sent earlier:
↑ (up arrow)    # cycles back through your history
```

## Walk-through
1. Start a Claude Code session and type a long prompt to Claude.
2. While it's responding, press `Escape` — generation stops instantly.
3. Next, start typing a multi-line prompt (e.g., a structured instruction). Press `Shift+Enter` after each line instead of `Enter`.
4. When your multi-line prompt is ready, press `Enter` alone to submit it.
5. Press `↑` to pull your last prompt back into the input box for editing and re-sending.

## Gotchas
- `Ctrl+C` also stops generation, but in some terminals it clears your input too — `Escape` is safer.
- `↑` navigates your session history, not your shell history — it only shows prompts from the current Claude Code session.
- `Tab` autocompletes slash commands (type `/` then `Tab` to see options), but won't autocomplete file paths in plain prose.
- Custom keybindings can be set in `~/.claude/keybindings.json` if the defaults conflict with your terminal — type `/keybindings` inside Claude Code to explore.

## Takeaway
`Escape` to stop, `Shift+Enter` to expand — those two get you 80% of the way there.
