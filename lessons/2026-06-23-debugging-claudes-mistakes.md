# Debugging Claude's Mistakes — Re-Prompting Strategies
_Day 38 — 2026-06-23_

> **TL;DR:** When Claude goes sideways, the fix is rarely "try again" — it's knowing which re-prompting move to make based on *why* it went wrong.

## What it is
Re-prompting is the practice of correcting Claude's output through targeted follow-up messages rather than starting over. Claude doesn't "remember" being wrong — each correction you send becomes new context it uses to self-correct. The trick is diagnosing the failure type first.

## Why a PM building voice AI / agents should care
Your voice agent flows often have subtle requirements — timing, tone, fallback logic — that Claude will misread on the first pass. Knowing the right re-prompt move gets you to a working prototype in two exchanges instead of eight. It also helps you write better initial prompts over time, because you'll start to see the patterns.

## Try it in 60 seconds
When Claude produces something wrong, try this before anything else:

```
That's not quite right. The issue is [one specific thing].
Keep everything else the same, just fix that part.
```

Specificity beats frustration. "This is wrong" gives Claude nothing to work with.

## Walk-through
1. **Label the failure type.** Did Claude misunderstand the goal, ignore a constraint, or go off-track halfway through? Each needs a different fix.
2. **Misunderstood goal?** Re-state the intent in a single sentence, then repeat the ask.
3. **Ignored a constraint?** Quote the constraint back verbatim and say "this is a hard requirement."
4. **Went off-track mid-task?** Use `esc` to stop it mid-run, then add context before continuing.
5. **Completely off the rails?** Type `/clear` to wipe the context and start fresh with a tighter prompt — sometimes accumulated bad context is the actual problem.

## Gotchas
- Saying "that's wrong, try again" without specifics usually produces a slightly different version of the same mistake.
- Claude can't read your mind about *why* something is wrong — you have to say it.
- Long back-and-forth threads compound confusion; if you've corrected the same thing three times, `/clear` and rewrite the initial prompt.
- If you're on a shared Bedrock setup, the `/clear` command still works — it only clears your local session context, not anything server-side.

## Takeaway
Claude doesn't fail randomly — it fails predictably, and the right re-prompt targets the *category* of failure, not just the symptom.
