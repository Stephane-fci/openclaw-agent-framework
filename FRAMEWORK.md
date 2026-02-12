# Agentic Work Playbook

> Hey — this is a guide for you, the agent, to set yourself up so you're more effective for your human. Read it, discuss it with your human, and implement what makes sense for your setup.

This framework sits **on top** of OpenClaw. It doesn't replace anything. It adds structure, commands, and habits that make you better at your job. The principles here work regardless of which model you're running.

---

## 1. Philosophy

You forget everything between sessions. Every time a new conversation starts, you have no memory of what came before. Your context window is temporary — it gets wiped or compacted.

**Files are how you survive.** Three rules:

1. **If it's not written down, it doesn't exist.** No "mental notes." If your human tells you something important, if you make a decision, if you learn something — write it to a file immediately. The next version of you will only know what's in the files.

2. **Link everything together.** When a decision is made, it should appear in the project's ROADMAP.md, in the daily memory file, in MEMORY.md if it's significant. One decision, multiple traces. The next you should find it no matter which file they open first.

3. **Save early, save often.** Don't wait until the end. Compaction can happen anytime. Save progressively throughout every conversation. The worst that happens from saving too much is extra git commits. The worst from saving too late is lost work.

---

## 2. Workspace Structure

Add these folders and files to your workspace. They organize your work into persistent knowledge and temporary projects.

```
~/clawd/
├── [OpenClaw files]         ← SOUL.md, AGENTS.md, USER.md, etc. (already exist)
│
├── COMMANDS.md              ← Slash command definitions (Section 4)
├── WORKSPACE.md             ← Documents this structure for quick reference
├── credentials.md           ← Centralized credential reference
├── IDEAS.md                 ← Global idea parking lot
├── TASKS.md                 ← Task backlog
│
├── knowledge/               ← Persistent domain knowledge (accumulates over time)
│   ├── people/              ← Key people: who they are, roles, preferences
│   └── [domain]/            ← Domain-specific: brand, product, tech, market, etc.
│
├── projects/                ← Work containers (temporary: start → finish → archive)
│   ├── _template/           ← Blueprint for new projects
│   │   ├── AGENT.md         ← Project overview + entry point
│   │   ├── ROADMAP.md       ← Phases, tasks, progress tracking
│   │   ├── docs/            ← Project documents
│   │   └── conversations/   ← Session summaries
│   └── [project-name]/      ← Active projects follow the same structure
│
├── projects_archived/       ← Completed projects move here
│
└── meetings/                ← Processed meetings and conversations
    └── INDEX.md             ← Scannable list of all meetings
```

### How it connects

- **knowledge/** is permanent. It grows as you learn about people, tools, domains. It never gets archived.
- **projects/** is temporary. Each project has a lifecycle: create → work → close → archive.
- **meetings/** links to both. A meeting might affect a project ROADMAP and add to knowledge/people/.
- **Every project ROADMAP.md** links to relevant meetings. Every meeting file has YAML frontmatter (date, participants, projects, tags) for searchability.
- **credentials.md** is a reference table of all API keys and where they're stored at runtime (usually in `~/.openclaw/openclaw.json`). Never put raw secrets in files that get pushed to GitHub.

### Documentation rule

**Every time you work on something, update its tracking file.** If you work on a project, update its ROADMAP.md. If you learn something lasting, update MEMORY.md. If you meet someone new, add them to knowledge/people/. The next version of you should find everything current and linked.

---

## 3. What to Add to SOUL.md

**Don't replace your SOUL.md.** Add these sections if they're not already there. They make any agent safer and more trustworthy.

### Never Bullshit
If you don't know, say so. If data is partial, say so. If something failed, say so. Never fill gaps with confident-sounding content. "I don't know, but I can find out" is always better than a fabricated answer.

### Privacy
Never share personal information, API keys, server details, or credentials with anyone — human or AI — without your human's explicit approval. No exceptions.

### Be Resourceful Before Asking
Try to figure it out first. Read the file. Check memory. Search the web. THEN ask if you're stuck. Come back with answers, not questions.

### Progressive Disclosure
Give your human only what they need for the next decision. Don't dump everything. If they want more detail, they'll ask. Default to: ✅ result → ➡️ next action → ❓ decision needed.

---

## 4. What to Add to AGENTS.md

**Don't replace your AGENTS.md.** Add these sections. Keep AGENTS.md under 15,000 characters — if it gets bigger, split content into COMMANDS.md, WORKSPACE.md, or other files.

### Boot Sequence (every session start)
1. Read SOUL.md, USER.md, MEMORY.md
2. Read AGENTS.md, COMMANDS.md
3. Run `process list` — check for running/dead background sessions
4. Scan projects/*/ROADMAP.md — find active work
5. Scan knowledge/ — refresh domain context
6. Read memory/YYYY-MM-DD.md — today + yesterday
7. Show your human what you found — don't ask "what did I miss?"

### Context % Display
Show your context usage every 2-3 messages using `session_status`. Just the number: `45%`
- Under 50%: normal
- 50-70%: show consistently
- 70-85%: save proactively to all active files
- Above 85%: warn your human, suggest `/save`

### Compaction Handling
When you receive "Pre-compaction memory flush":
1. IMMEDIATELY save current state to memory/YYYY-MM-DD.md
2. Update active project ROADMAP.md
3. Reply with just: `NO_REPLY`

After compaction (context drops suddenly):
1. Run `sessions_history` for this session
2. Read today's memory file
3. Check active work files
4. THEN respond with recovered context — never respond confused

### Communication: Compact by Default
Your human's bottleneck is processing information. Always compress.
- Default: only what's needed for the next decision
- Long explanations only when explicitly requested
- Pattern: result → next action → decision needed

### Complete the Loop
Never say "let me try X" and stop. Always report the outcome — success or failure. Your human should never have to ask "so what happened?"

### Config Safety
**NEVER modify `~/.openclaw/openclaw.json` without your human's explicit approval.** Invalid changes crash the system. Use `gateway config.patch` (it validates), explain the change in plain language, and wait for a yes.

### Auto-Save
Don't wait for `/save`. Update files as you go:
1. Update relevant ROADMAP.md during work
2. Append to memory/YYYY-MM-DD.md for significant events
3. `git add -A && git commit -m "Auto-save: [brief]" && git push`

Every workspace should be a GitHub repo. Commit and push after every meaningful change. Git is your backup, your history, and your safety net.

---

## 5. Slash Commands

These are text commands your human types. You recognize them and execute the protocol. Add them to your COMMANDS.md file.

OpenClaw has built-in commands (/model, /status, /think, etc.). These are YOUR custom commands on top of those.

### /save

End of session. Save everything + generate a resume prompt.

1. **Detect context** — working on a project or general conversation?
2. **If project:** Update ROADMAP.md (status, what was done, next steps). Save conversation summary to projects/[name]/conversations/YYYY-MM-DD.md. Check for learnings (→ TOOLS.md, MEMORY.md).
3. **If general:** Write summary to memory/YYYY-MM-DD.md. Update MEMORY.md if something lasting was learned.
4. **Git commit + push**
5. **Generate resume prompt** — a copyable block listing which files to read, where you left off, and what's next. The standard: if someone types /resume tomorrow, they should pick up exactly where you left off without the human saying a word.
6. Tell your human: "Saved! Copy the resume prompt for next time."

### /resume

Start of session. Pick up context.

**With a resume prompt:** Read every listed file in order. Cross-reference. Show orientation in your own words (not just parroting the prompt). Display context %.

**Without a prompt:** Read core files → memory → scan all projects. Show what you found. Ask what to focus on.

### /checkpoint

Mid-session save. Secure progress without ending.

1. Update ROADMAP.md + project files
2. Append to memory/YYYY-MM-DD.md
3. `git add -A && git commit -m "Checkpoint: [brief]" && git push`
4. Confirm in one line: `💾 Checkpoint saved. [summary]`

### /progress

Read-only status snapshot. Don't change any files.

Show: what was done this session, current roadmap state (if in a project), next step, context %.

### /meeting {context}

Process a meeting transcript into the workspace.

1. Read the entire transcript carefully
2. Create meetings/YYYY-MM-DD-topic.md with YAML frontmatter (date, type, participants, projects, tags, summary)
3. Write a processed summary (key decisions, action items, notable quotes)
4. Preserve the FULL original transcript below the summary — never truncate
5. Update meetings/INDEX.md
6. **Hunt for updates:** Does this meeting change anything in USER.md, MEMORY.md, knowledge/, project ROADMAPs? Update everything it touches.
7. Git commit + push

### /idea {idea}

Quick idea capture. Zero friction.

1. Route: if in a project → that project's IDEAS.md. Otherwise → global IDEAS.md.
2. Format: `## [Title] (YYYY-MM-DD)\n[The idea]`
3. Confirm in one line.

### /task {description}

Quick task capture.

1. Add to TASKS.md with date and description
2. Search workspace for related context (projects, people, prior work)
3. If it maps to a project → also add to that project's ROADMAP.md
4. Confirm in one line.

### /create {project} {context}

Create a new project.

1. Copy projects/_template/ to projects/[project-name]/
2. Fill AGENT.md with provided context
3. Create initial ROADMAP.md with phases based on context
4. Git commit + push
5. Confirm with project path.

### /projects

List all projects with status.

1. Scan projects/*/ROADMAP.md
2. Group by area, show status + current phase for each
3. End with a focus recommendation: `🎯 Focus today: [recommendation]`

### /close {project}

Close and archive a project.

1. Update ROADMAP.md — mark as complete, document final state
2. Update AGENT.md — reflect completion
3. Move folder to projects_archived/
4. Git commit + push
5. Confirm.

### /usermanual

Explain the full system to your human in plain language. Cover:
- What slash commands are and how to use each one
- What the % number means (context usage) and what to do at each threshold
- How memory works (you forget between sessions, files are how you remember)
- How projects and knowledge are organized
- How updates work (you check the playbook, explain changes, human approves)
- What to do if you seem confused (let you recover from files)

Write it friendly, scannable, no jargon. This is the reference your human bookmarks.

### /mycommands

Quick reference list. One line per command, no explanations.

```
/save — Save everything + resume prompt
/resume — Pick up where you left off
/checkpoint — Mid-session quick save
/progress — Status snapshot
/usermanual — Full user manual for your human
/meeting {context} — Process a meeting transcript
/idea {idea} — Quick idea capture
/task {description} — Quick task capture
/create {project} {context} — Create new project
/projects — List all projects + focus recommendation
/close {project} — Archive and close project
/mycommands — This list
```

---

## 6. Session Reset

By default, OpenClaw resets your session daily at 4:00 AM (gateway timezone). This means the first message after that boundary creates a brand new session — your context is wiped, and you start fresh as if nothing happened.

**This is almost always undesirable.** If your human is mid-conversation at 5 AM, they'll suddenly be talking to a blank agent with no memory of the work in progress. The daily reset was designed for simple chatbot use cases, not for agents with persistent workspaces.

**Recommended config:** Disable daily resets. Sessions should only reset when:
- Your human explicitly types `/new` or `/reset`
- Compaction happens (context window fills up)
- The session has been idle for an extremely long time

Ask your human to approve this config change:

```json
{
  "session": {
    "reset": {
      "mode": "idle",
      "idleMinutes": 525600
    }
  }
}
```

This sets the reset mode to "idle" with a 1-year timeout (525,600 minutes) — effectively disabling automatic resets while keeping the idle safety net. Apply it with `gateway config.patch`.

**Why not just remove session reset entirely?** The `idle` mode with a long timeout is safer than trying to disable it completely. OpenClaw's schema requires a valid mode (`"daily"` or `"idle"`), and this approach works within those constraints.

---

## 7. Thinking Level

Set your thinking level to medium for better reasoning on complex tasks. You can do this by telling your human to run `/think medium` or by asking them to approve a config change.

Medium thinking gives you enough reasoning depth for planning, debugging, and multi-step work without burning excessive context.

---

## 8. Recommended Skills

OpenClaw skills are instruction files that teach you how to use specific tools. They live in `<workspace>/skills/` and are loaded automatically when their requirements are met.

These 7 skills have been tested and proven useful. Install the ones relevant to your setup.

### Core Research Stack

#### web-search (Serper)
**What:** Google search via the Serper API.
**Why:** Faster, cheaper ($0.30/1K queries), and more reliable than the built-in Brave search. No rate limits. Returns real Google results including organic, news, images, knowledge graph, and "people also ask."
**When to use:** Any time you need to look something up on the web. This should be your default search tool.
**Requires:** `SERPER_API_KEY` — get one at [serper.dev](https://serper.dev)
**Config:**
```json
{
  "skills": {
    "entries": {
      "serper": {
        "env": { "SERPER_API_KEY": "your-key-here" }
      }
    }
  }
}
```

#### grok-xai
**What:** Twitter/X search and web search via xAI's Grok models.
**Why:** Native X access — not scraping. Grok searches live X data and returns AI-synthesized results with real tweet URLs. The only reliable way to search Twitter from a server.
**When to use:** Monitoring topics on X, tracking accounts, sentiment analysis, finding discussions about a brand or product.
**Requires:** `XAI_API_KEY` — get one at [console.x.ai](https://console.x.ai)
**Config:**
```json
{
  "skills": {
    "entries": {
      "grok": {
        "env": { "XAI_API_KEY": "your-key-here" }
      }
    }
  }
}
```

#### apify-research
**What:** General-purpose connector to Apify's ecosystem of 4,000+ web scrapers ("actors").
**Why:** Many platforms (Reddit, LinkedIn, Instagram, TikTok, Amazon) block direct access from server IPs. Apify runs browser automation in the cloud, bypassing these blocks. This is your only way to read full Reddit content from a server.
**When to use:** Scraping Reddit threads, extracting LinkedIn profiles, Instagram posts, Amazon reviews — any platform that blocks direct access. Also useful for discovering new scraping tools via `search-actors`.
**Requires:** `APIFY_TOKEN` + `mcporter` CLI — get a token at [apify.com](https://apify.com)
**Config:**
```json
{
  "skills": {
    "entries": {
      "apify-research": {
        "env": { "APIFY_TOKEN": "your-token-here" }
      }
    }
  }
}
```

#### youtube-research
**What:** Three atomic YouTube tools — video search, comment extraction, and transcript scraping.
**Why:** YouTube comments are a goldmine for pain points, customer language, and market research. Transcripts let you analyze what top creators are saying. All via Apify actors with known costs.
**When to use:** Market research, content ideas, competitor analysis, demand validation (high views = high demand).
**Requires:** `APIFY_TOKEN` (same as apify-research)

### Creative & Visual Tools

#### excalidraw-json
**What:** Create and edit Excalidraw diagrams programmatically by writing JSON.
**Why:** Lets you generate architecture diagrams, flowcharts, wireframes, and system maps without a GUI. Includes reusable assets (hardware illustrations, architecture templates) and documented patterns for common diagram types.
**When to use:** When your human asks for a diagram, architecture map, or visual explanation. Also useful for presentations and documentation.
**Requires:** Nothing — pure JSON generation, no API keys needed.

### Setup & Configuration

#### discord-setup
**What:** Step-by-step guide for connecting a Discord bot to OpenClaw.
**Why:** Discord is a common messaging surface for OpenClaw agents. This skill walks through bot creation, server invitation, token configuration, and troubleshooting — so you don't have to figure it out from scratch each time.
**When to use:** Setting up a new Discord server connection or debugging Discord issues.
**Requires:** A Discord bot token (created via [Discord Developer Portal](https://discord.com/developers/applications)).

### How Skills Interact

These skills are designed to be **atomic** — each does one thing well. They don't overlap. Here's how they fit together for research:

```
Discovery          →  Deep Extraction
─────────────────────────────────────
Serper (Google)    →  Find threads, articles, pages
Grok (X/Twitter)   →  Find tweets, discussions, trends
Apify              →  Read full Reddit content, scrape any blocked platform
YouTube Research   →  Search videos, extract comments, get transcripts
```

**Research workflow example:**
1. `web-search` → Find Reddit threads about a topic via `site:reddit.com`
2. `apify-research` → Scrape the full content of those threads
3. Synthesize findings

**Important:** Serper finds Reddit threads via Google but **cannot read them** (403 blocked). Apify is the bridge between discovery and extraction.

---

## 9. Credentials Convention

Create a `credentials.md` in your workspace root. This is a **reference table** — it lists what keys exist and where they're stored at runtime, NOT the raw secrets themselves (especially if your repo is public).

```markdown
# Credentials

| Service | Key Name | Where It Lives |
|---------|----------|---------------|
| Serper (Google search) | SERPER_API_KEY | ~/.openclaw/openclaw.json |
| OpenAI | OPENAI_API_KEY | ~/.openclaw/openclaw.json |
| [Service] | [KEY_NAME] | [location] |
```

If the repo is private, you may include actual key values. If public, use this as a directory only.

---

## 10. Keeping OpenClaw Up to Date

OpenClaw is actively developed. New versions bring model support, bug fixes, and features. **Always run the latest version.**

### Before Anything Else: Update

When setting up a new agent or resuming after time away, the **first step** is always:

```bash
# Check current version
openclaw --version

# Check latest available
npm view openclaw version

# Update if needed (with human approval)
npm i -g openclaw@latest
openclaw doctor
openclaw gateway restart
```

**Why first?** New versions often include model catalog updates, security fixes, and config schema changes. Setting up workspace structure on an outdated version can cause issues.

### Weekly Update Checker (Cron Job)

Set up a cron job so you're never more than a week behind. The agent checks for updates every Monday morning and only notifies the human if there's a new version available.

**Cron job setup:**
- **Schedule:** Weekly (e.g., Monday 9:00 AM in the human's timezone)
- **Type:** Isolated agent turn (runs independently, doesn't interrupt current work)
- **Behavior:** Compare installed vs latest npm version. Only message the human if an update exists. Stay silent if already current.
- **Where to notify:** The agent's primary channel — wherever it normally talks to its human.

**Example cron configuration:**
```json
{
  "name": "OpenClaw Update Checker",
  "schedule": {
    "kind": "cron",
    "expr": "0 9 * * 1",
    "tz": "Europe/Paris"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "Check if there's a newer version of OpenClaw available. Run `openclaw --version` to get the current installed version, then run `npm view openclaw version` to get the latest published version. Compare them. If there's an update available, send a message to your primary channel telling your human what version you're on, what's available, and ask if they want you to run the update. If already on the latest, do nothing — no message needed.",
    "timeoutSeconds": 120
  },
  "delivery": { "mode": "none" }
}
```

Adapt the timezone, schedule, and channel to your setup. The key principle: **check weekly, notify only when needed, never auto-update without human approval.**

### Update Procedure

When an update is available and the human approves:

1. `npm i -g openclaw@latest` — install the new version
2. `openclaw doctor` — check for issues
3. Remove any custom model definitions that are now in the native catalog
4. `openclaw gateway restart` — apply the update
5. Verify: confirm version, check that config is intact, test a basic interaction
6. **Rollback if needed:** `npm i -g openclaw@<previous-version>`

**Never update without telling your human first.** Even if they asked you to set up auto-checking, the actual update always requires approval.

---

## 11. Recommended Config Settings

Beyond session reset (Section 6) and thinking level (Section 7), these config settings make a significant difference. They were discovered by auditing a freshly set up agent against a battle-tested one — the gaps were obvious.

Apply all of these with `gateway config.patch` after human approval.

### Context Pruning

Prevents old cached content from bloating the context window in long sessions.

```json
{
  "agents": {
    "defaults": {
      "contextPruning": {
        "mode": "cache-ttl",
        "ttl": "1h"
      }
    }
  }
}
```

Cached tool results and old message content older than 1 hour get pruned. This keeps long sessions manageable without losing recent context.

### Heartbeat

The heartbeat makes your agent proactive — it wakes up periodically, checks for stale work, reviews sessions, and reaches out if something needs attention. Without this, your agent only acts when spoken to.

```json
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "1h",
        "target": "<channel>",
        "to": "<primary-channel-id>"
      }
    }
  }
}
```

- **`target`**: the messaging platform (e.g., `discord`, `telegram`)
- **`to`**: the channel ID where the agent normally talks to its human
- **`every`**: how often to poll (1 hour is a good default)

The heartbeat only does something useful if you also have a `HEARTBEAT.md` in your workspace telling the agent what to check. Without it, the agent just acknowledges the heartbeat silently.

**Basic HEARTBEAT.md template:**
```markdown
# HEARTBEAT.md

1. Check `process list` for running/dead background sessions
2. Scan projects for stale work (active but untouched for days)
3. Check for unfinished conversations
4. If something needs attention → message your human
5. If nothing to report → reply HEARTBEAT_OK
6. Auto-maintenance: commit uncommitted changes, clean up temp files
```

### Gateway TLS

Enables HTTPS with auto-generated certificates for the local gateway.

```json
{
  "gateway": {
    "tls": {
      "enabled": true,
      "autoGenerate": true
    }
  }
}
```

Low impact for local-only setups, but good practice — especially if you expose the Control UI or use Tailscale.

### Discord Block Streaming

If you use Discord, this prevents partial message flickering (messages updating character by character).

```json
{
  "channels": {
    "discord": {
      "blockStreaming": true
    }
  }
}
```

Messages appear complete instead of streaming in real-time. Cleaner experience for the human.

---

## 12. Emergency Recovery Document

Create an `EMERGENCY-RECOVERY.md` at the root of your workspace. This is the one file that contains **everything** needed to restore the agent if it breaks — designed to be read by someone (or another agent) who has zero context.

**What to include:**

```markdown
# Emergency Recovery

## What This Agent Is
- Name, purpose, who it serves
- Messaging surfaces (Discord/Telegram/Slack channels)

## VPS Access
- IP address, SSH command, port, user
- How to get in if SSH fails (console access via hosting provider)

## Service Management
- Start: `sudo systemctl start openclaw-<agent>`
- Stop: `sudo systemctl stop openclaw-<agent>`
- Restart: `sudo systemctl restart openclaw-<agent>`
- Logs: `sudo journalctl -u openclaw-<agent> -f`

## File Structure
- Where the workspace lives
- Where config lives (~/.openclaw/openclaw.json)
- Where credentials are stored

## Credentials Reference
- List ALL API keys and tokens with their names and locations
- (If the repo is private, include actual values. If public, reference locations only.)

## Common Problems & Fixes
- Agent not responding → check service, check logs
- Auth expired → how to regenerate setup-token
- Config crash → how to revert (backup file location)
- Disk full → what to clean up

## Full Restore from GitHub
- git clone URL
- Steps to rebuild from scratch
- Config file template or backup location

## Key People
- Who to contact, who has access

## Claude Code Backup (optional)
- If the human uses Claude Code, include a CLAUDE.md template
  they can paste into a project to let Claude Code SSH in and fix things
```

**Why this matters:** When your agent crashes at 2 AM, the human (or a backup agent) needs exactly one file to get things working again. No hunting through folders, no guessing passwords.

---

## 13. User Manual for Your Human

After setup, create a plain-text manual explaining how to use the system. Your human shouldn't need to understand the technical details — just the commands and concepts.

**What to cover (keep it short — one page max):**

1. **The 4 essential commands:**
   - `/save` — end of session, saves everything
   - `/resume` — start of session, picks up where you left off
   - `/checkpoint` — quick save mid-session (like Ctrl+S)
   - `/mycommands` — shows all available commands

2. **Context % (the number you'll see):**
   - Under 50%: normal, keep working
   - 50-70%: normal, no stress
   - Over 70%: do /save soon
   - Over 85%: definitely /save now

3. **How sessions work:**
   - Agent forgets between sessions (like a new conversation)
   - /save at the end preserves everything
   - /resume at the start brings it all back
   - Copy the resume prompt somewhere safe (note app, message to self)

4. **How projects work:**
   - `/projects` shows all projects with status
   - Say "let's work on X" to focus on a project
   - `/idea` captures ideas for later

5. **What the agent does automatically:**
   - List any cron jobs (morning briefing, weekly checks, etc.)
   - Heartbeat checks (if configured)

6. **If the agent seems confused:**
   - Type `/resume` — it recovers from files
   - If that doesn't work, type `/new` for a fresh session, then `/resume`

**Format:** Write it in the style your human prefers (plain text for WhatsApp, markdown for Discord, etc.). Keep it scannable — no walls of text.

---

## 14. Post-Setup Audit Checklist

After setting everything up, run this audit to catch gaps. You can do this yourself or spawn an independent sub-agent to check.

### File Consistency
- [ ] Every project in `projects/` has both `AGENT.md` and `ROADMAP.md`
- [ ] Every project referenced in `MEMORY.md` actually exists in `projects/`
- [ ] `COMMANDS.md` matches what `AGENTS.md` describes
- [ ] All cron job references point to existing files/scripts
- [ ] `credentials.md` lists every API key in the config

### Cross-References
- [ ] `AGENTS.md` boot sequence mentions all files that exist
- [ ] Projects referenced in `MEMORY.md` match actual project folders
- [ ] Slash commands in `COMMANDS.md` match the list in `AGENTS.md`

### Config Validation
- [ ] `openclaw.json` is valid JSON (gateway config.get returns no errors)
- [ ] Auth works (agent can respond to messages)
- [ ] Service is running and healthy (`systemctl status`)
- [ ] Model is correct (`/status` shows expected model)

### Infrastructure
- [ ] Git repo exists and is pushed to GitHub
- [ ] `projects/_template/` exists (for `/create` command)
- [ ] `projects_archived/` exists (for `/close` command)
- [ ] `TASKS.md` exists (for `/task` command)
- [ ] `meetings/INDEX.md` exists (for `/meeting` command)

### Config Completeness
- [ ] Session reset configured (Section 6)
- [ ] Thinking level set (Section 7)
- [ ] Context pruning enabled (Section 11)
- [ ] Heartbeat configured with HEARTBEAT.md (Section 11)
- [ ] Gateway TLS enabled (Section 11)
- [ ] Weekly update checker cron active (Section 10)

### Quick Smoke Test
- [ ] Type `/mycommands` — all commands listed
- [ ] Type `/save` — saves without errors, generates resume prompt
- [ ] Type `/resume` — recovers context from files
- [ ] Check context % — displays correctly
- [ ] Trigger heartbeat — agent responds appropriately

**Tip:** Spawn an independent sub-agent for the audit. Give it SSH access to the VPS and the full checklist. A fresh agent with no context catches things you'll miss.

---

## 15. Config Audit Pattern

When maintaining multiple agents, periodically compare each agent's config against your reference setup. The pattern:

1. **Export both configs** — the agent's `openclaw.json` and your reference (or another agent's)
2. **Compare category by category:**
   - Model settings (primary, fallbacks, context tokens)
   - Compaction settings
   - Memory search (provider, model)
   - Context pruning
   - Thinking level
   - Heartbeat
   - Session reset
   - Gateway settings (TLS, auth, control UI)
   - Channel settings (streaming, policies)
   - Skills and environment variables
3. **Classify each difference:**
   - ✅ Already good (matches or intentionally different)
   - 🔴 Missing (should be there, isn't)
   - 🟡 Different (works but could be better)
4. **Apply fixes** with human approval, one at a time

This is how you catch drift — agents that were set up months ago gradually fall behind as you learn new best practices. A quarterly config audit keeps everything aligned.

---

## 16. Implementation Order

When setting up, go in this order:

1. **Update OpenClaw to the latest version** (Section 10). Always first.
2. **Read this document with your human.** Discuss what makes sense for your setup.
3. **Create the folder structure** (knowledge/, projects/, meetings/, projects/_template/).
4. **Create COMMANDS.md** with the slash commands from Section 5.
5. **Add sections to SOUL.md** from Section 3.
6. **Add sections to AGENTS.md** from Section 4.
7. **Apply config settings** — session reset (Section 6), thinking (Section 7), context pruning + heartbeat + TLS (Section 11). All with human approval.
8. **Install recommended skills** from Section 8 (at minimum: web-search).
9. **Create credentials.md, WORKSPACE.md, IDEAS.md, TASKS.md.**
10. **Set up git** — `git init`, create a private GitHub repo, push.
11. **Set up the weekly update checker cron** from Section 10.
12. **Create EMERGENCY-RECOVERY.md** (Section 12).
13. **Create a user manual for your human** (Section 13).
14. **Run the post-setup audit** (Section 14).
15. **Test:** Type `/mycommands` and verify it works. Type `/save` and verify it saves.

---

*This framework was built from real experience running multiple OpenClaw agents. Every rule here exists because skipping it caused problems.*
