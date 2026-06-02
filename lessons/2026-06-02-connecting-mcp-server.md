# Connecting an MCP Server
_Day 17 — 2026-06-02_

> **TL;DR:** MCP servers plug real tools — your files, GitHub, Slack — directly into Claude, so it can act on them instead of just hearing about them.

## What it is
An MCP server is a small program that exposes tools (like "read a file" or "fetch a GitHub issue") using a standard protocol Claude understands. You connect one by adding a short JSON block to your `~/.claude/settings.json`. After that, Claude sees those tools alongside its built-in ones and can call them automatically.

## Why a PM building voice AI / agents should care
If you're iterating on voice agent flows, your context is scattered: GitHub has the specs, Slack has stakeholder feedback, your laptop has transcripts. An MCP server collapses that — Claude can pull the latest GitHub issue, read a Slack thread, and reference a local file all in one session, without you copy-pasting anything.

## Try it in 60 seconds
Add this to `~/.claude/settings.json` under `"mcpServers"`:

```json
"mcpServers": {
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/rohit/Documents"]
  }
}
```

Restart Claude Code, then ask: *"What files are in my Documents folder?"*

## Walk-through
1. Open `~/.claude/settings.json` in any text editor (create it if it doesn't exist).
2. Paste the `"mcpServers"` block above; update the folder path to something real on your machine.
3. Save, then restart Claude Code (`/quit`, then type `claude` again in terminal).
4. Ask Claude about your files — it'll call the filesystem server automatically.
5. For GitHub, replace the package with `@modelcontextprotocol/server-github` and add `"env": {"GITHUB_TOKEN": "ghp_..."}` inside that server block.

## Gotchas
- `npx -y` downloads the server package on first run — you need Node.js and internet access.
- Each MCP server runs as a real process; if Claude feels slow, check that it actually started (run `/mcp` inside Claude Code to see status).
- GitHub's server needs a personal access token; Slack's needs a bot token — both are free but take ~5 minutes to set up.
- If you're on a corporate machine using Bedrock, MCP itself works fine — but check with IT before pointing a server at internal data, as these servers make outbound connections.

## Takeaway
One JSON block is the difference between Claude knowing about your work and Claude being able to act on it.
