# Daily Lesson — Instructions

You are writing today's Claude Code lesson for Rohit, a Product Manager at Theatro (Motorola Solutions). He builds voice AI and agents but is **new to coding**. Plain English, no jargon, short paragraphs.

## Steps

1. **Pick today's topic.** Open `curriculum.md`. Find the **first** line that starts with `- [TODO]`. That's today's topic.

2. **Write the lesson** as a new file at `lessons/YYYY-MM-DD-slug.md` where:
   - `YYYY-MM-DD` = today's date (UTC)
   - `slug` = a short kebab-case version of the topic (e.g. `slash-commands`)

   The lesson must include these sections, in this order:

   ```markdown
   # <Topic Name>
   _Lesson for <YYYY-MM-DD> — Day <N>_

   ## What it is (in one paragraph)
   Plain English. No jargon. If you must use a technical term, define it in parentheses.

   ## Why it matters for a PM
   How this helps Rohit ship voice AI / agent prototypes faster, demo to stakeholders, or skip needing eng help.

   ## A real example
   A short, copy-pasteable example. Either a code snippet or an exact terminal command. Keep it under ~15 lines.

   ## How to try it yourself
   Numbered steps, like a recipe. Assume Rohit hasn't tried it before.

   ## Gotchas
   2–4 bullets on common mistakes or things that will surprise him.

   ## One-line takeaway
   A single sentence he can remember tomorrow.
   ```

3. **Mark the topic done** in `curriculum.md`: change the `- [TODO]` to `- [DONE]` on that exact line. Do not reorder.

4. **Update the README lesson index.** In `README.md`, replace everything between `<!-- LESSON_INDEX_START -->` and `<!-- LESSON_INDEX_END -->` with a markdown list of every file in `lessons/`, newest first, in this format:

   ```
   - [YYYY-MM-DD — Topic Name](lessons/YYYY-MM-DD-slug.md)
   ```

5. **Commit twice:**
   - First commit: just the new lesson file. Message: `Add lesson: <Topic Name>`
   - Second commit: the curriculum + README updates. Message: `Mark <Topic Name> done and update index`

6. **Print the path of the new lesson file** as the very last line of your output, on its own line, prefixed with `LESSON_PATH=`. Example:
   `LESSON_PATH=lessons/2026-05-19-slash-commands.md`

   The email script reads this path. Do not skip this step.

## Style rules

- Keep the whole lesson under ~400 words.
- Active voice. Short sentences.
- No "let's dive in" / "in today's lesson we will" filler.
- One-line takeaway should be memorable, not a summary.
- If the topic is something Rohit can't try without a paid plan or extra setup, say so honestly in Gotchas.
