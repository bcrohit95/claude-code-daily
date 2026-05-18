# Custom Slash Commands
_Day 2 — 2026-05-18_

> **TL;DR:** You can create your own `/commands` that give Claude a standing prompt with one keystroke — great for tasks you repeat every session.

## What it is
A custom slash command is a Markdown file you drop in `.claude/commands/`. Whatever you write in that file becomes a reusable prompt you can trigger by typing `/your-command-name` in any Claude Code session. No code, no plugins — just a text file.

## Why a PM building voice AI / agents should care
You likely re-run the same prompts constantly: "summarize the latest agent test transcripts," "draft release notes for this sprint," "check this prompt for edge cases." Turning those into one-word commands removes the copy-paste loop and makes Claude feel like a personalized tool rather than a blank slate.

## Try it in 60 seconds
```bash
mkdir -p .claude/commands
echo "Summarize the key user intents found in the most recent test transcripts in /transcripts. Flag any intents the agent mishandled." > .claude/commands/review-transcripts.md
```
Then in Claude Code, type:
```
/review-transcripts
```

## Walk-through
1. Open your project folder in the terminal (or VS Code).
2. Run `mkdir -p .claude/commands` to create the commands folder if it doesn't exist.
3. Create a `.md` file inside it — the filename (minus `.md`) becomes the slash command name.
4. Write your prompt in plain English inside that file. Claude reads the whole file as your instruction.
5. In Claude Code, type `/` followed by your command name and press Enter.

## Gotchas
- The command name must match the filename exactly — `review-transcripts.md` → `/review-transcripts`. No spaces allowed in filenames; use hyphens.
- Commands live in `.claude/commands/` inside your project. They're project-specific, not global — they won't appear in a different repo.
- You can commit this folder to git so your whole team gets the same commands.
- To pass dynamic input, use `$ARGUMENTS` anywhere in the file — e.g., `Analyze the transcript at $ARGUMENTS for missed intents.` Then type `/review-transcripts path/to/file.txt`.

## Takeaway
A 10-second text file can save you from retyping the same prompt every single session — and it travels with the repo.
