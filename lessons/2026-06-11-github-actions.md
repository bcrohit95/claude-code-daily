# GitHub Actions Integration
_Day 26 — 2026-06-11_

> **TL;DR:** The official `claude-code-action` lets Claude respond to pull request comments on GitHub — no terminal required, no eng needed to trigger it.

## What it is
A GitHub Action (an automated task that runs inside GitHub's servers) that runs Claude Code on your repo. You drop a YAML config file into `.github/workflows/`, and from that point forward anyone on your team can type `@claude fix this` in a PR comment and Claude will make the change, commit it, and reply.

## Why a PM building voice AI / agents should care
You're already reviewing PRs and filing issues — now you can loop Claude in without touching a terminal. Type `@claude add error handling to this voice webhook` in a PR comment, and it edits the code and pushes the fix. Good for rapid iteration on agent prompts or config files where you spot issues in review but don't want to block on eng availability.

## Try it in 60 seconds
Add this file to your repo (swap in your actual branch name and secrets):

```yaml
# .github/workflows/claude.yml
name: Claude Code
on:
  issue_comment:
    types: [created]

jobs:
  claude:
    if: contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@beta
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Walk-through
1. Create the file at `.github/workflows/claude.yml` using the snippet above.
2. Add your Anthropic API key as a GitHub secret named `ANTHROPIC_API_KEY` (repo Settings → Secrets → Actions).
3. Open any pull request on that repo.
4. Comment `@claude explain what this file does` (or any instruction).
5. Watch the Actions tab — Claude runs, then replies in the PR thread.

## Gotchas
- **Costs real tokens**: every `@claude` comment triggers an API call billed to your Anthropic account. Set a budget alert.
- **Needs `ANTHROPIC_API_KEY`**: this uses Anthropic's API directly, not AWS Bedrock. If your company only allows Bedrock, you'll need the `aws_bedrock` config variant instead.
- **Write permissions**: the action needs `contents: write` and `pull-requests: write` permissions in the YAML or it can't commit or comment.
- **Beta**: the action is still tagged `@beta` — API shape may shift.

## Takeaway
`@claude` in a PR comment is the shortest path from "I spotted a bug" to "it's fixed and committed" — without opening a terminal.
