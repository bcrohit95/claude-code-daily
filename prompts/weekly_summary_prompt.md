# Weekly Summary — Instructions

You are writing this week's Claude Code recap for **Rohit**, a PM at Theatro (Motorola Solutions) building voice AI and agents.

## Steps

1. **Find this week's lessons.** List files in `lessons/` whose dates fall in the last 7 days (UTC). Use `ls -t lessons/*.md` and the YYYY-MM-DD prefix in filenames.

2. **Read each lesson.** Pull out: the topic name, the TL;DR (or first paragraph), and one concrete thing he can now do.

3. **Write the summary file** at `summaries/YYYY-MM-DD-week-of.md` (use today's date). Create the `summaries/` folder if it doesn't exist.

   Use exactly this structure:

   ```markdown
   # Week of <YYYY-MM-DD>
   _<N> lessons covered_

   > **The thread:** one sentence linking the week's lessons. What's the bigger picture he should walk away with?

   ## Lessons this week

   ### 1. <Topic Name> — [YYYY-MM-DD]
   - **What it is:** one line
   - **What he can now do:** one line, action-oriented

   ### 2. <Topic Name> — [YYYY-MM-DD]
   ...

   ## Suggested next steps
   2–3 bullets. Things to try this weekend or next week to cement the learning. Tie to voice AI / agent prototyping where natural.

   ## Quick reference card
   A markdown table of every command/concept covered, so he can scan it in 10 seconds:

   | Topic | Command/Idea | When to use it |
   |---|---|---|
   ```

4. **Update the README.** Add a `## Weekly summaries` section (if it doesn't already exist) above the `## Lessons` section, with a link to the new summary file. Newest first.

5. **Commit twice:**
   - First commit (just the new summary file): `Add weekly summary: week of <YYYY-MM-DD>`
   - Second commit (README update): `Update README with weekly summary link`

6. **Print the summary path** as the very last line: `SUMMARY_PATH=summaries/YYYY-MM-DD-week-of.md`

## Style rules

- Whole summary under 500 words.
- Don't repeat the lessons verbatim — synthesize.
- Highlight patterns ("three of this week's topics were about controlling Claude's behavior — hooks, permission modes, and settings.json").
- The "thread" is the most important part. It's why he reads recaps.
