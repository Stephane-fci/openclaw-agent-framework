# Agentic Work Playbook

A playbook that sits on top of OpenClaw to make any agent more effective. It adds structure, workflow, and habits that OpenClaw doesn't provide out of the box.

**This is additive.** It doesn't replace anything — it adds to what's already there.

---

## ⚠️ For Agents: How to Use This Repo

**Do NOT just read this repo and move on.** This is a guided setup process. Walk your human through every step, explain what each setting does, and apply them together.

### If your human says "apply this playbook" or "set up from this repo":

**Follow this exact process:**

1. **Update OpenClaw first.** Check your version (`openclaw --version`), compare with latest (`npm view openclaw version`). If outdated, explain to your human and update with their approval. (Details: FRAMEWORK.md Section 10)

2. **Set up Serper for web search.** This is **mandatory — not optional.** Serper replaces the built-in Brave search with real Google results at 1/10th the cost. Ask your human to create a free API key at [serper.dev](https://serper.dev), then apply the config. Do NOT skip this. (Details: FRAMEWORK.md Section 8)

3. **Walk through FRAMEWORK.md section by section** with your human. For each section:
   - **Explain** what it does and why it matters — in plain language
   - **Ask** if they want to apply it
   - **Apply** the setting or create the file
   - **Confirm** it worked before moving to the next section

4. **The sections, in order:**
   - §1 Philosophy — read and understand (no action needed)
   - §2 Workspace Structure — create folders and files
   - §3 SOUL.md additions — add safety and honesty sections
   - §4 AGENTS.md additions — add boot sequence, compaction, auto-save
   - §5 Slash Commands — create COMMANDS.md with all commands
   - §6 Session Reset — disable daily resets (config change, needs approval)
   - §7 Thinking Level — set to medium (config change, needs approval)
   - §8 Skills — install Serper (mandatory), then other relevant skills
   - §9 Credentials — create credentials.md
   - §10 Update Management — set up weekly update checker cron
   - §11 Config Settings — context pruning, heartbeat, TLS, Discord streaming
   - §12 Emergency Recovery — create EMERGENCY-RECOVERY.md
   - §13 User Manual — create a guide for your human
   - §14 Post-Setup Audit — run the checklist to catch gaps
   - §15 Config Audit Pattern — understand how to maintain settings over time

5. **After completing all sections**, run the post-setup audit (§14) to verify everything is solid.

**Key principle: never auto-apply anything.** Explain every change, wait for approval, apply one at a time.

---

## If you're an existing agent checking for updates

Read `UPDATE-PROTOCOL.md`, then check for new commits or releases since your last check.

---

## What's in this repo

| File | What it is |
|------|-----------|
| `FRAMEWORK.md` | The complete playbook — every section with instructions and config |
| `UPDATE-PROTOCOL.md` | How to check for and apply updates safely |

That's it. Two files plus this README. Everything the agent needs is in FRAMEWORK.md.
