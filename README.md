# Agentic Work Playbook

A playbook that sits on top of OpenClaw to make any agent more effective. It adds structure, workflow, and habits that OpenClaw doesn't provide out of the box.

**This is additive.** It doesn't replace anything — it adds to what's already there.

---

## If you're setting up a new agent

Read `FRAMEWORK.md`. It walks you through everything: philosophy, workspace structure, slash commands, what to add to SOUL.md and AGENTS.md, and configuration.

## If you're an existing agent checking for updates

Read `UPDATE-PROTOCOL.md`, then check for new commits or releases since your last check.

## What's in this repo

| File | What it is |
|------|-----------|
| `FRAMEWORK.md` | The complete playbook — everything an agent needs to set itself up |
| `UPDATE-PROTOCOL.md` | How to check for and apply updates safely |
| `scripts/` | Utility scripts (skill-audit, skill-install) |
| `skills/` | Bundled skills that ship with the playbook |

### Bundled Skills

| Skill | Description |
|-------|-------------|
| `skills/pil-diagrams/` | Generate visual diagrams as PNG using Python PIL — no browser needed |
