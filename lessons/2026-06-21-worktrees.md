# Worktrees — Running Claude on an Isolated Copy of the Repo
_Day 36 — 2026-06-21_

> **TL;DR:** A worktree lets Claude experiment on a separate copy of your repo while your main work stays untouched — like having two desks open at once.

## What it is
A git worktree (a built-in git feature) checks out a branch into a second folder on disk — no cloning, no duplication of the full history. You get two live views of the same repo. Claude Code can work in one while you keep editing in the other.

## Why a PM building voice AI / agents should care
If you're iterating on a voice agent prompt or testing a config change, worktrees let Claude make edits in a sandbox while your stable version stays open and runnable. No more "I need to undo everything Claude just did." It's also how Claude Code's built-in `isolation: worktree` mode works — agents that mutate files spin up in their own worktree automatically so they can't stomp on each other.

## Try it in 60 seconds
```bash
# Create a worktree for a new branch called "experiment"
git worktree add ../my-repo-experiment -b experiment

# Run Claude inside that isolated copy
cd ../my-repo-experiment && claude
```

## Walk-through
1. In your project folder, run `git worktree add ../my-repo-experiment -b experiment` — this creates a new folder and a new branch in one shot.
2. `cd ../my-repo-experiment` to move into the isolated copy.
3. Open Claude Code here (`claude`) — it only sees this folder's files.
4. Let Claude make changes, test things, even break things. Your original folder is completely unaffected.
5. When done, either merge the branch or discard it: `git worktree remove ../my-repo-experiment`.

## Gotchas
- The two folders share git history, so a commit in the worktree still shows up in `git log` in your main folder — they're not fully independent.
- You can't check out the same branch in two worktrees at once; each branch can only live in one place at a time.
- If you're on Bedrock at work, this is a local git feature — no special Anthropic setup needed.
- Running `claude` inside a worktree is the same command as always; Claude doesn't need to know it's in a worktree.

## Takeaway
When you want Claude to experiment freely without risk, give it its own room — that's a worktree.
