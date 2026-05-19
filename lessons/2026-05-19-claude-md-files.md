# CLAUDE.md Files
_Day 3 — 2026-05-19_

> **TL;DR:** A `CLAUDE.md` file is a standing briefing document Claude reads at the start of every session — so you never have to re-explain your project from scratch.

## What it is
`CLAUDE.md` is a plain text file you put at the root of your project. Claude Code automatically loads it before you type a single message. Think of it as the "context I'd give a new engineer on day one" — written once, read every time.

## Why a PM building voice AI / agents should care
Your agent has a personality, a user base (frontline workers), constraints (short voice responses, no jargon), and a file structure that a blank Claude session knows nothing about. Without `CLAUDE.md`, you repeat that briefing every session. With it, Claude starts every conversation already knowing what your agent is, who it serves, and what words to avoid.

## Try it in 60 seconds
```bash
cat > CLAUDE.md << 'EOF'
# Project: Theatro Voice Agent

This is a voice AI assistant for frontline retail workers.
- Responses must be under 15 words (they get read aloud).
- Avoid jargon. Workers may not be tech-literate.
- Test transcripts are in /transcripts. Prompts live in /prompts.
EOF
```

## Walk-through
1. Open your project folder in the terminal.
2. Run the command above (or create `CLAUDE.md` in any text editor).
3. Write whatever context Claude needs: what the project does, key folder paths, style rules, things to avoid.
4. Start a new Claude Code session — it reads the file automatically, no extra steps.
5. Ask Claude something project-specific; notice it already has context.

## Gotchas
- `CLAUDE.md` is not secret — if you commit it to git, everyone (and every CI run) shares the same context. That's usually a feature, not a bug.
- You can also place a `CLAUDE.md` inside a subfolder; Claude loads it when working in that directory. Useful for monorepos (a codebase with multiple projects in one repo).
- Claude *reads* the file but doesn't update it — if your project changes, you update it manually.
- Keep it under ~200 lines. Very long files slow the session start and dilute what matters.

## Takeaway
One well-written `CLAUDE.md` is worth more than a hundred repeated prompts — it makes Claude a teammate who already knows the project.
