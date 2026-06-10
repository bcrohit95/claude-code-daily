# Headless Mode
_Day 25 — 2026-06-10_

> **TL;DR:** Run Claude Code from a script or CI pipeline — no keyboard, no prompts, just input in and output out.

## What it is
Headless mode means running Claude Code non-interactively: you pass a prompt via a flag and Claude responds to stdout (your terminal's output stream), then exits. No chat interface, no waiting for your keystrokes. It's Claude as a command-line tool you can wire into other tools.

## Why a PM building voice AI / agents should care
If you're analyzing call transcripts or testing prompts at scale, you don't want to paste each one into a chat window by hand. Headless mode lets you loop over a folder of transcripts and run the same analysis on all of them in one go — no engineering help needed. It also powers automated review pipelines: run a quality check on every new conversation log as part of a nightly job.

## Try it in 60 seconds
```bash
claude -p "Summarize this in one sentence: The agent greeted the customer, confirmed their order, and closed the ticket."
```

## Walk-through
1. Open your terminal anywhere Claude Code is installed.
2. Run the command above — the `-p` flag (short for `--print`) sends the prompt and exits.
3. Claude prints its response to the terminal and returns you to the shell prompt.
4. To process a file, pipe it in: `cat transcript.txt | claude -p "What was the customer's main complaint?"`.
5. To get structured output for scripting, add `--output-format json` and Claude returns a JSON object instead of plain text.

## Gotchas
- By default, headless mode still enforces permissions — it will pause and ask for approval on file edits. Add `--dangerously-skip-permissions` only in trusted, sandboxed CI environments.
- Long prompts work better as a file passed via stdin than stuffed into the `-p` string.
- If you're on Bedrock at work, confirm your AWS credentials are exported in the shell environment where the script runs — headless mode has no UI to prompt you to re-auth.
- Output goes to stdout; errors go to stderr. If you're piping output to a file with `>`, errors will still print to the screen.

## Takeaway
Once Claude can run in a script, it stops being a chat tool and starts being a reusable step in any workflow you can automate.
