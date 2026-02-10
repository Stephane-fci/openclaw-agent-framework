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

### /help

Explain the system to your human. Show all available commands, what the % number means, how memory works. Keep it friendly and scannable. This IS the user manual — make it comprehensive enough that your human can understand the whole system from this one command.

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

### /mycommands

Quick reference list. One line per command, no explanations.

```
/save — Save everything + resume prompt
/resume — Pick up where you left off
/checkpoint — Mid-session quick save
/progress — Status snapshot
/help — How the system works (user manual)
/meeting {context} — Process a meeting transcript
/idea {idea} — Quick idea capture
/task {description} — Quick task capture
/create {project} {context} — Create new project
/projects — List all projects + focus recommendation
/close {project} — Archive and close project
/mycommands — This list
```

---

## 6. Context Configuration

Apply this config using `gateway config.patch` (after your human approves):

```json
{
  "agents": {
    "defaults": {
      "contextTokens": 1000000,
      "thinkingDefault": "medium",
      "compaction": {
        "memoryFlush": {
          "enabled": true,
          "softThresholdTokens": 4000
        }
      }
    }
  }
}
```

- **contextTokens: 1000000** — use the full context window your model supports
- **thinkingDefault: "medium"** — enables reasoning for complex tasks without burning too much context
- **memoryFlush: enabled** — auto-saves to memory before compaction (critical)

---

## 7. Credentials Convention

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

## 8. Implementation Order

When setting up, go in this order:

1. **Read this document with your human.** Discuss what makes sense for your setup.
2. **Create the folder structure** (knowledge/, projects/, meetings/, projects/_template/).
3. **Create COMMANDS.md** with the slash commands from Section 5.
4. **Add sections to SOUL.md** from Section 3.
5. **Add sections to AGENTS.md** from Section 4.
6. **Apply the config** from Section 6 (with human approval).
7. **Create credentials.md, WORKSPACE.md, IDEAS.md, TASKS.md.**
8. **Set up git** — `git init`, create a private GitHub repo, push.
9. **Test:** Type `/help` and verify it works. Type `/save` and verify it saves.

---

*This framework was built from real experience running multiple OpenClaw agents. Every rule here exists because skipping it caused problems.*
