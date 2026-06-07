# CRO Research Workflow Overhaul — Design Spec

**Date:** 2026-05-14
**Status:** Approved by user

---

## Context

The current CRO workflow (cro-research.md + cro-research-roadmap.md) has two compounding inefficiencies:

1. `AskUserQuestion` is called for every data source during collection — a token-intensive tool invocation per asset that slows the session and burns limits faster than necessary.
2. Screenshots are sent through chat, landing in context permanently. The roadmap command then loads all of them upfront before analysis begins, carrying maximum image token load throughout the entire session.

Additionally, the roadmap command writes both the full audit and the roadmap in the same running context — meaning the roadmap is written when context is at its heaviest (all sources + all images + completed audit already loaded).

---

## Upgrade 1: Remove AskUserQuestion Entirely

Every interaction moves to regular chat. Claude speaks, user replies. No tool invocations for data collection.

**Collection flow for Meta Ads (example pattern):**
- Claude in chat: "Send me Ad #1 — creative screenshot, landing page screenshot (top 3 folds if long), and the URL."
- User replies with content.
- Claude in chat: "Got it. Send Ad #2, or type `skip`."
- Repeat through Ad #3.
- Same pattern for every source: Claude asks in chat, user replies or types `skip`.

**Context gathering (Step 1):**
- Claude asks in one chat message for all context at once: store name, URL, slot count, dev slots, variations per test, areas of focus.
- User can send everything in one reply.

**Source selection (Step 2):**
- Claude lists all available sources in chat and asks user to confirm which they have.
- User replies with their selection (e.g., "Meta Ads, Reviews, PageSpeed, Site Screenshots").

No `AskUserQuestion` calls anywhere in the workflow.

---

## Upgrade 2: Folder-First Screenshots + Two-Command Split (Option B)

### Command 1: `/cro-research` — Collection + Audit

**Phase A: Context + folder setup**
- Collect context via chat (one message exchange).
- Create `brands/[brand-name]/raw/screenshots/` immediately.
- Print the full naming convention in chat so the user can rename and drop files before data collection begins.

**Phase B: Text data collection**
- Collect all text-based sources via chat: reviews, call notes, PageSpeed scores, Google Ads text, email copy, competitor notes.
- Save each to `brands/[brand-name]/raw/[source-name].md` as raw input only — no analysis yet.
- Screenshots are never sent through chat. User drops files directly into the screenshots folder.

**Phase C: Audit generation (lazy image loading)**
- Read manifest, load text source files.
- For each audit section, load only the relevant screenshot(s) from disk at that moment. Analyze, write the section, move on.
- Do web research (competitor, community, ebook grep) during relevant sections only.
- Write the audit MD incrementally, section by section.
- End with: audit MD saved, manifest updated.

**Output:** `brands/[brand-name]/[brand-name]-research-audit.md`

---

### Command 2: `/cro-research-roadmap` — Roadmap Only

- Reads manifest + audit MD. Nothing else. No raw source files, no images.
- Writes roadmap MD from the audit as its sole input.
- Clean, light context throughout.

**Output:** `brands/[brand-name]/[brand-name]-[month]-[year]-roadmap.md`

---

## Files to Modify

- `.claude/commands/cro-research.md` — full rewrite
- `.claude/commands/cro-research-roadmap.md` — rewrite to roadmap-only (reads audit MD, no raw sources)

---

## Token Efficiency Summary

| Phase | Before | After |
|---|---|---|
| Context gathering | AskUserQuestion per field | One chat exchange |
| Source selection | AskUserQuestion | One chat exchange |
| Screenshot intake | Sent through chat (permanent context) | Dropped to folder, never in chat |
| Audit image loading | All upfront, all in context simultaneously | One at a time, per section |
| Roadmap writing | Full source context + images + audit in memory | Audit MD only |

---

## Verification

1. Run `/cro-research` on a test brand — confirm no `AskUserQuestion` tool is invoked at any point.
2. Confirm folder + naming convention is printed before text collection begins.
3. Drop test screenshots into the folder, confirm command reads them on-demand during audit writing.
4. Confirm audit MD is saved before command ends.
5. Run `/cro-research-roadmap` — confirm it reads only the audit MD and produces a valid roadmap.
