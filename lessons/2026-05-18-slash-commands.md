# Slash Commands
_Lesson for 2026-05-18 — Day 1_

## What it is (in one paragraph)
A slash command is a shortcut you type directly in the Claude Code chat prompt, starting with `/`. Instead of describing what you want in plain English, you type something like `/help` and Claude Code runs a specific built-in action. Think of them like keyboard shortcuts, but for AI — fast, repeatable, and available without opening any settings.

## Why it matters for a PM
Slash commands let you control Claude Code without writing a prompt. You can switch modes, clear context, review code, or get help in two keystrokes. When you're demoing to a stakeholder or racing to test an idea, these save you the mental overhead of remembering how to phrase a request.

## A real example

```
/help           → shows a list of all available slash commands
/clear          → wipes the conversation and starts fresh (keeps your files)
/review         → asks Claude to review the code changes on your current branch
/init           → generates a CLAUDE.md file that documents your project
/fast           → toggles a faster (but less thorough) response mode
/config         → opens the settings menu inside Claude Code
```

## How to try it yourself

1. Open Claude Code in your terminal: `claude` (or open it in VS Code via the extension).
2. At the prompt, type `/help` and press Enter.
3. Read through the list — notice which commands appear. These are your built-ins.
4. Type `/clear` to reset the conversation (nothing on disk is deleted).
5. Try `/config` to see your current settings without editing any files.

## Gotchas

- `/clear` wipes the chat history Claude can see, but does **not** delete any files you created together. It's safe to use whenever context feels bloated.
- Some slash commands (like `/review`) work best inside a git repo. Running them in a plain folder may give you an error or do nothing.
- Slash commands are not the same as terminal shell commands. `/ls` won't list files — type `/help` to see only what Claude Code recognizes.
- Custom slash commands exist too (covered in a future lesson). If you see `/` commands not on the `/help` list, someone added them to `.claude/commands/`.

## One-line takeaway
`/help` is always your first move — it shows you every shortcut you didn't know you had.
