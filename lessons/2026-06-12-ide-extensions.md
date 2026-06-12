# IDE Extensions

_Day 27 — 2026-06-12_

> **TL;DR:** The VS Code and JetBrains extensions bring Claude Code into your editor so you never need a separate terminal window.

## What it is
Claude Code ships official extensions for VS Code and JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.). Install the extension and a Claude Code panel appears inside your editor. Claude sees the file you have open, can propose edits inline, and you review diffs (side-by-side change previews) without leaving the IDE.

## Why a PM building voice AI / agents should care
If you've been running Claude Code in a separate terminal, the extension cuts the window-switching. Highlight a confusing block of agent code, ask Claude what it does — no copy-paste, no context switch. It's the fastest path from "I don't understand this" to a working change when you're iterating on a voice flow.

## Try it in 60 seconds
In VS Code:

Press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux) to open Extensions, search **"Claude Code"**, and click **Install**. The Claude panel appears in the Activity Bar (left sidebar) immediately.

## Walk-through
1. Open the Extensions panel in VS Code using the keyboard shortcut above.
2. Search "Claude Code" and click Install on the Anthropic-published extension.
3. Sign in when prompted — uses the same API key as the CLI.
4. Open any file, then highlight a snippet you want to understand and type a question in the Claude panel.
5. When Claude suggests an edit, click **Accept** or **Reject** in the inline diff view.

## Gotchas
- The extension wraps the CLI — you still need Claude Code installed first (`npm install -g @anthropic-ai/claude-code`).
- JetBrains users: install through **Settings → Plugins → Marketplace**, not a browser download.
- If your team uses AWS Bedrock, the extension picks up the same environment variables as the CLI — no separate auth config.
- Feature parity lags slightly; a few advanced CLI options aren't exposed in the UI yet.

## Takeaway
The extension doesn't give Claude new powers — it removes the tax of switching windows, which is often enough to double how often you actually use it.
