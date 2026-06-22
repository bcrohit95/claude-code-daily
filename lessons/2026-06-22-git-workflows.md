# Git Workflows with Claude
_Day 37 — 2026-06-22_

> **TL;DR:** Claude Code handles branches, commits, and pull requests through plain English — you don't need to memorize a single git command.

## What it is
Git (the industry-standard version control system) normally requires terminal commands to create branches, save changes, and open pull requests. Claude Code can do all of that for you when you describe what you want in natural language, keeping you in one tool instead of switching between Claude, your terminal, and GitHub.

## Why a PM building voice AI / agents should care
When you're iterating on a voice agent prompt or flow, you want to checkpoint your work and share it without breaking what's already running. Claude can branch off the current state, make changes safely, then open a draft PR so an engineer can review it — without you touching the terminal. That loop (prototype → save → share) gets fast enough to happen mid-conversation.

## Try it in 60 seconds
In any Claude Code session where you've made changes, type:

```
Create a new branch called "rohit/update-greeting-prompt", commit my changes with a clear message, and open a draft pull request to main.
```

Claude will run the git commands, write the commit message, and hand you the PR link.

## Walk-through
1. Open Claude Code in a project folder that has a git repository (`.git` folder exists).
2. Make any change — edit a file, update a prompt, tweak a config.
3. Tell Claude: "Create a branch named `your-name/what-you-changed` and commit these changes."
4. Then say: "Open a pull request to main with a description of what I changed and why."
5. Claude runs `git checkout -b`, `git commit`, and `gh pr create` and returns the PR URL.

## Gotchas
- Claude won't push or open PRs without your approval — it asks first, which is the safe default.
- If the repo requires signed commits or branch protection rules, Claude will hit the same walls a human would.
- The `gh` CLI (GitHub's official tool) must be installed and authenticated for PR creation to work.
- Claude will never force-push or reset your history unless you explicitly ask — it defaults to safe operations.

## Takeaway
Tell Claude what you want to save and share; let it figure out which git commands that takes.
