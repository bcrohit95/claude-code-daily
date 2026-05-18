# Daily Lesson — Instructions

You are writing today's Claude Code lesson for **Rohit**, a Product Manager at **Theatro (a Motorola Solutions company)**. He builds **voice AI and AI agents** for frontline workers but is **new to coding**. Plain English, no jargon. If a technical term is unavoidable, define it inline in parentheses.

Goal: he reads this for 3 minutes over coffee, learns one thing, and tries it the same day.

## Steps

1. **Pick today's topic.** Open `curriculum.md`. Find the **first** line that starts with `- [TODO]`. That's today's topic.

2. **Write the lesson** as a new file at `lessons/YYYY-MM-DD-slug.md` where:
   - `YYYY-MM-DD` = today's date (UTC)
   - `slug` = a short kebab-case version of the topic (e.g. `slash-commands`)

   Use exactly this structure:

   ```markdown
   # <Topic Name>
   _Day <N> — <YYYY-MM-DD>_

   > **TL;DR:** one sentence — what this is and why he should care.

   ## What it is
   2–3 short sentences. No throat-clearing. Define jargon inline.

   ## Why a PM building voice AI / agents should care
   2–3 sentences max. Concrete connection to his world: prototyping voice agent flows, demoing to stakeholders, analyzing transcripts, iterating on prompts, reducing eng dependency. **If the topic genuinely doesn't connect to voice AI work, say so honestly in one line and pivot to a general PM benefit — don't force it.**

   ## Try it in 60 seconds
   A single copy-pasteable command, snippet, or click-path. Under 10 lines. If terminal: show the exact command. If Claude Code: show the exact thing to type.

   ## Walk-through
   3–5 numbered steps. Each step = one short sentence. Assume he hasn't tried it before.

   ## Gotchas
   2–4 bullets, each one line. Things that will surprise him or trip him up.

   ## Takeaway
   One sentence he can repeat tomorrow. Make it memorable, not a summary.
   ```

3. **Mark the topic done** in `curriculum.md`: change `- [TODO]` to `- [DONE]` on that exact line. Do not reorder.

4. **Update the README lesson index.** In `README.md`, replace everything between `<!-- LESSON_INDEX_START -->` and `<!-- LESSON_INDEX_END -->` with a markdown list of every file in `lessons/`, **newest first**, in this format:

   ```
   - [YYYY-MM-DD — Topic Name](lessons/YYYY-MM-DD-slug.md)
   ```

5. **Commit twice:**
   - First commit (just the new lesson file): `Add lesson: <Topic Name>`
   - Second commit (curriculum + README): `Mark <Topic Name> done and update index`

6. **Print the path of the new lesson file** as the very last line of your output, on its own line, prefixed with `LESSON_PATH=`. Example:
   `LESSON_PATH=lessons/2026-05-19-custom-slash-commands.md`

## Style rules

- **Whole lesson under 350 words.** Brevity is a feature.
- Active voice. Short sentences. No filler ("In this lesson we will…", "Let's dive in…").
- Skip the marketing tone. Talk to Rohit like a senior friend explaining a tool over Slack.
- Show, don't tell — when there's a command, show the command.
- The TL;DR and Takeaway should never be the same sentence rephrased.
- If the topic requires a paid plan, extra setup, or doesn't apply to his Bedrock-at-work setup, call it out honestly in Gotchas.
