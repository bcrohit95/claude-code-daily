# Image Input
_Day 23 — 2026-06-08_

> **TL;DR:** You can paste or drag a screenshot directly into Claude Code and it will read and reason about whatever is on screen.

## What it is
Claude Code is multimodal — it can process images, not just text. Paste a screenshot (PNG, JPEG, GIF, or WebP) into the chat and Claude sees it as clearly as you do. No upload step, no extra command.

## Why a PM building voice AI / agents should care
When you're demoing a voice agent flow and something looks off, grab a screenshot of the agent dashboard, the transcript viewer, or an error message and paste it right in. Claude can read the UI, spot the bug, or explain what the error means — no need to copy-paste text or describe the screen in words.

## Try it in 60 seconds
In Claude Code (terminal or desktop app), press **Ctrl+V** (Mac: **Cmd+V**) to paste a screenshot you copied to your clipboard. Then type:

```
What's happening in this screenshot? Is anything wrong?
```

Hit Enter. Claude describes what it sees and answers your question.

## Walk-through
1. Take a screenshot of anything — an error, a UI, a transcript, a diagram.
2. Copy it to your clipboard (on Mac: Cmd+Shift+4, then Ctrl+click to copy instead of save).
3. Open Claude Code and paste with Cmd+V or Ctrl+V.
4. Type your question on the same line or the next line.
5. Claude responds with observations, explanations, or suggested next steps.

## Gotchas
- **Desktop app and web only for paste.** The terminal CLI doesn't support Ctrl+V image paste — use the desktop app or provide a file path instead (drag the file into the chat or type the path).
- **File path works in the terminal:** `claude --image ./screenshot.png "What's wrong here?"` — but check your version supports `--image`.
- **Sensitive data:** screenshots of internal dashboards or PII go to Anthropic's API. Check your company's data policy before pasting anything confidential.
- **Image size:** very large images (4K screenshots) may be resized automatically; Claude will still read them but fine print might blur.

## Takeaway
Stop describing what's on your screen — just paste it.
