# CRO Research Workflow Overhaul Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the two-command CRO workflow with a leaner version: a combined collection+audit command that uses only chat (no AskUserQuestion) and folder-based screenshots, plus a roadmap-only command that reads the audit MD and nothing else.

**Architecture:** `/cro-research` handles everything from context gathering to audit generation using chat-only interaction and lazy on-demand image loading from disk. `/cro-research-roadmap` is a clean, light command that reads only the saved audit MD and writes the roadmap.

**Tech Stack:** Claude command markdown files (`.claude/commands/`). No code. Verification is manual end-to-end runs.

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `.claude/commands/cro-research.md` | Full rewrite | Chat-based collection + lazy audit generation |
| `.claude/commands/cro-research-roadmap.md` | Full rewrite | Roadmap-only from audit MD |

---

### Task 1: Rewrite `/cro-research` — Chat-Based Collection + Audit

**Files:**
- Modify: `.claude/commands/cro-research.md`

- [ ] **Step 1: Read the current file before editing**

Read `.claude/commands/cro-research.md` in full to confirm current content, then proceed.

- [ ] **Step 2: Overwrite cro-research.md with the new command**

Replace the entire file with:

```markdown
---
description: Collect CRO source data for a Shopify prospect and generate the research audit
---

You are a senior CRO strategist collecting source data and generating a research audit for a Shopify prospect.

Your job in this command: gather inputs, create the brand folder, and write the full research audit.

Do not write the roadmap. Do not output the audit in chat. Do not invent facts.

---

## Data Integrity

- Only record what the user provides or you fetch directly.
- Never describe UI you have not seen.
- Use WebFetch to view the store URL when provided.
- Always include time periods on metrics.
- If a source is skipped, do not create a file for it.

---

## Step 1: Context

Say this in chat (one message):

"To get started, send me:
- Store name
- Store URL
- Number of slots (default: 3)
- Any slots reserved for dev or project work
- Variations per test (default: 1 variation vs. control)
- Any specific areas of focus or concern

You can send all of this in one message."

Wait for the user's reply. Save to `brands/[brand-name]/manifest.md`.

---

## Step 2: Create Folder + Print Naming Convention

Immediately create:

```
brands/[brand-name]/
brands/[brand-name]/raw/
brands/[brand-name]/raw/screenshots/
```

Then say in chat:

"Folder created at `brands/[brand-name]/raw/screenshots/`. Drop your screenshots into that folder using these names before we start:

**Meta Ads**
- `meta-ad-1.png`, `meta-ad-2.png`, `meta-ad-3.png`
- `meta-ad-1-lp.png`, `meta-ad-2-lp.png`, `meta-ad-3-lp.png`

**Google Ads**
- `google-ads.png`

**Site pages**
- `homepage-f1.png`, `homepage-f2.png`, `homepage-f3.png`
- `landing-page-f1.png`, `landing-page-f2.png`
- `pdp-f1.png`, `pdp-f2.png`
- `collection-f1.png`
- `cart.png`

**Emails**
- `email-1.png`, `email-2.png`, etc.

**Competitors / Inspiration**
- `competitor-[brand-name].png`
- `inspiration-[site-name].png`

Let me know when you've dropped the files in, or just tell me which sources you have and we'll start."

---

## Step 3: Source Selection

Say in chat:

"Which of these sources do you have?

1. Meta Ads and Landing Pages
2. Google Ads Transparency
3. Reviews & UGC
4. PageSpeed / Core Web Vitals
5. Competitor Insights
6. Inspiration Sites
7. Email Campaigns
8. Non-Data Context (call notes, strategic priorities)
9. Current Site Screenshots"

Wait for reply. Note selected sources.

---

## Step 4: Collect Text Data (Chat Only)

For each selected source that involves text input, ask in chat one source at a time. The user can type `skip` at any point.

Do not ask the user to send screenshots in chat. Screenshots go into the folder only.

**Meta Ads and Landing Pages**

Say: "For Meta Ads — send me the URL for Ad #1's landing page."
After reply: "Send the URL for Ad #2, or type `skip`."
After reply: "Send the URL for Ad #3, or type `skip`."

Save URLs to `brands/[brand-name]/raw/meta-ads.md` under `## Raw Input`.

**Google Ads Transparency**

Say: "For Google Ads — search adstransparency.google.com for [brand name] and drop the screenshots in the folder as `google-ads.png`. Is there anything else you can tell me about their Google Ads (messaging themes, targeting, etc.)?"

Save any text to `brands/[brand-name]/raw/google-ads.md`.

**Reviews & UGC**

Say: "Send me reviews — paste them directly, or share a link, or type `skip`. The more raw review text the better."

Save to `brands/[brand-name]/raw/reviews.md`.

When collecting, structure notes in two parts:
1. What customers love — differentiators, emotional outcomes, purchase drivers, verbatim praise.
2. What frustrates customers — product-level specifics, sizing issues, quality complaints, compatibility failures, strong verbatim complaints.

Flag client-actionable insights (product, ops, support fixes) separately.

**PageSpeed / Core Web Vitals**

Say: "Send me PageSpeed data — mobile/desktop scores, LCP, CLS, FID/INP if available, any slow pages. Or type `skip`."

Save to `brands/[brand-name]/raw/pagespeed.md`.

**Competitor Insights**

Say: "Any competitor data to share? Names, pricing, features, weaknesses. Or type `skip` and I'll research them myself."

Save user-provided data to `brands/[brand-name]/raw/competitors.md`. Mark it as user-provided. Note that self-research will supplement during audit.

**Inspiration Sites**

Say: "Any inspiration sites? Send URLs and what specifically caught your eye. Or type `skip`."

Save to `brands/[brand-name]/raw/inspiration.md`.

**Email Campaigns**

Say: "Send email copy or paste subject lines, CTAs, and any performance data (open rate, click rate, revenue per email). Or drop screenshots as `email-1.png`, `email-2.png`, etc. and type `done` when ready."

Save to `brands/[brand-name]/raw/emails.md`.

**Non-Data Context**

Say: "Any call notes, strategic priorities, known objections, or internal context I should know? Or type `skip`."

Save to `brands/[brand-name]/raw/context.md`.

**Current Site Screenshots**

Say: "Drop your site screenshots into the folder using the naming convention from earlier (homepage-f1.png, pdp-f1.png, etc.). Type `done` when they're in place."

Wait for confirmation. Note that cart drawer is a high-value AOV opportunity. If cart.png is missing after the user signals done, record `MISSING_DATA: cart_drawer` in the manifest.

---

## Step 5: Update Manifest (Pre-Audit)

Write `brands/[brand-name]/manifest.md`:

```markdown
# [Brand Name] CRO Collection Manifest

## Brand Info

- Store name: [name]
- Store URL: [url]
- Slots: [N] total, [N] dev/project slots
- Variations per test: [N]
- Areas of focus: [any specific concerns]

## Sources Collected

- [Source name] → raw/[filename].md

## Screenshots Available

- [List files found in raw/screenshots/ via Bash ls]
- [or: none]

## Sources Skipped

- [Source name]

## Missing Data Warnings

- [MISSING_DATA: cart_drawer — cart screenshot not captured. Cart/AOV opportunities cannot be evaluated.]
- [Remove this section if no gaps.]

## Open Questions

- [any uncertainty]
```

---

## Step 6: Generate Research Audit

Now analyze. Read source files. Load screenshots on-demand — one at a time, only when writing the section that requires them. Do not load all screenshots upfront.

Do web research (competitors, CRO community, ebook) during the relevant sections only.

Write the audit to `brands/[brand-name]/[brand-name]-research-audit.md`:

```markdown
# [Store Name] CRO Research Audit

## Data Sources Used

[All sources: user-provided and self-researched]

## Source Findings

### Meta Ads & Landing Pages

[Load meta-ad-1.png, meta-ad-1-lp.png. Analyze. Write findings. Then meta-ad-2, meta-ad-3 if available.]

[Key findings: message match, ad angles, gaps between ad promise and landing page delivery.]

### Reviews & UGC

#### What Customers Love

- [Positive themes with representative quotes]

#### What Frustrates Customers

- [Friction points by theme, verbatim quotes]

#### Client-Actionable Insights

- [Product, ops, support fixes — not test ideas]

### PageSpeed / Core Web Vitals

[Mobile and desktop scores, LCP, CLS, FID/INP, slow pages. Include collection date.]

### Competitor Analysis

[Load competitor-[name].png if available. Then use WebSearch to find top 2-3 direct competitors. Table comparing price, key features, weaknesses. Note what came from user vs. self-research. Include research date.]

### Google Ads

[Load google-ads.png. Message match with Meta ads, consistency, gaps.]

### Emails

[Load email-1.png, email-2.png, etc. Subject lines, CTAs, messaging themes, message match with landing pages.]

### Inspiration Sites

[Load inspiration-[site-name].png if available. Relevant UX/conversion patterns only.]

### Non-Data Context

[Strategic priorities, call notes, known objections.]

### Current Site Screenshots

[Load homepage-f1.png, homepage-f2.png, etc. one at a time. Describe what's visible. Analyze conversion friction, hierarchy, trust signals, CTAs.]

[Load pdp-f1.png, pdp-f2.png. Same.]

[Load collection-f1.png. Same.]

[Load cart.png. Same. If missing, note the gap.]

### CRO Ebook Reference

[Grep resources/cro-ebook/cro-ebook.md for the top themes. Read matching sections only. Pull short relevant passages with chapter references.]

### CRO Community Research

[WebSearch for relevant CRO ideas from Reddit (r/ecommerce, r/shopify, r/CRO) and X/Twitter. Real practitioner discussions, not generic blog posts. Include source links and dates.]

## Cross-Source Themes

Rank top 3 themes by:
1. Evidence strength (how many sources point to it)
2. Revenue potential
3. Funnel importance

## Unused but Valuable Findings

[Only if high-value evidence exists that won't fit the slots — one bullet per finding, one sentence each.]

## Missing Data

[Only if manifest has MISSING_DATA warnings — name the gap and why it matters.]
```

---

## Step 7: Update Manifest (Post-Audit)

Add to manifest:

```markdown
## Audit

- [brand-name]-research-audit.md

## Next Step

Run `/cro-research-roadmap` to generate the testing roadmap.
```

---

## Final Response

Say only:

```
Collection and audit complete.

Files created:
- brands/[brand-name]/manifest.md
- brands/[brand-name]/raw/[source files]
- brands/[brand-name]/[brand-name]-research-audit.md

Next step: Run /cro-research-roadmap.
```
```

- [ ] **Step 3: Verify the file saved correctly**

Read back `.claude/commands/cro-research.md` and confirm:
- No `AskUserQuestion` anywhere in the file
- Folder creation happens in Step 2 before any data collection
- Naming convention is printed in chat
- Screenshots are never requested via chat — only folder drops
- Images are loaded one at a time in Step 6, per section, not upfront

- [ ] **Step 4: Commit**

```bash
git add ".claude/commands/cro-research.md"
git commit -m "refactor: rewrite cro-research as chat-only collection + audit command"
```

---

### Task 2: Rewrite `/cro-research-roadmap` — Roadmap Only from Audit MD

**Files:**
- Modify: `.claude/commands/cro-research-roadmap.md`

- [ ] **Step 1: Read the current file before editing**

Read `.claude/commands/cro-research-roadmap.md` in full to confirm current content.

- [ ] **Step 2: Overwrite cro-research-roadmap.md with the new command**

Replace the entire file with:

```markdown
---
description: Generate a CRO testing roadmap from a completed research audit
---

You are a senior CRO strategist writing a client-facing testing roadmap.

Run `/cro-research` before this command. This command reads the audit it produced. It does not re-read raw source files or screenshots.

---

## Data Integrity

- Every claim must trace back to the audit.
- Do not open raw source files. Do not open screenshots. Do not re-run web research.
- If a claim cannot be sourced to the audit, omit it.
- Always include time periods on metrics.
- No em dashes anywhere.

---

## Writing Style

Write like a clear CRO strategist pitching a prospective client.

- Every word earns its place. Cut filler, hedging, fluff.
- Be direct. Short sentences. One idea per sentence.
- Lead with the insight.
- Specific numbers: "2.05% CR" not "low conversion rate."
- Active voice.
- Tables over paragraphs when comparing data.
- Bullets over prose when listing items.

The reader should understand the problem, the solution, and why it matters in under 60 seconds per test.

---

## Step 1: Load Manifest and Audit

Ask the user for the brand name in chat: "What's the brand name?"

Read `brands/[brand-name]/manifest.md`.

Then read `brands/[brand-name]/[brand-name]-research-audit.md`.

Do not open any other files. Do not open raw/ source files. Do not open screenshots.

If no audit file is found, tell the user to run `/cro-research` first.

Confirm from the manifest: slot count, dev slots, variations per test, areas of focus.

---

## Step 2: Fill the Slots

Use the slot count and dev slots from the manifest.

**Dev/project slots first.** Write those before A/B test slots.

**A/B test selection criteria:**
- Data support: multiple sources in the audit point to the same issue
- Opportunity size: traffic volume x conversion gap = revenue potential
- Actionability: can be clearly tested

**Go where the money is.** A 1% lift on 500K sessions beats a 5% lift on 10K sessions.

**Each slot must be distinct.** Different page, different element, or different user segment.

**Variation rules:**
- 1-2 changes per variation, no more.
- When stacking makes sense: V1 adds change A, V2 adds A+B, V3 adds A+B+C.
- Use the variation count from the manifest.

**Always specify mobile and desktop.** Design mobile-first.

**Variation descriptions must be grounded in the audit.** Only describe UI elements documented in the audit's screenshot analysis or site fetch notes. If a page is not described in the audit, do not write a variation spec for it.

**Spread slots across funnel stages.** Do not place all slots on the same page. Aim for at least 2 different pages or funnel stages.

Funnel stages:
- Landing Page
- Homepage
- Collection / Category pages
- Product Detail Pages (PDP)
- Cart
- Checkout

---

## Step 3: Write the Roadmap File

**File:** `brands/[brand-name]/[brand-name]-[month]-[year]-roadmap.md`

Date rule: if today is the 23rd or later, use next month.

---

### Roadmap Format

**Header:** `# [Store Name] CRO Research Brief`

Do NOT include store URL, period, or generated date lines.

**Data Sources line:**

```
**Data Sources:** [List only sources that were collected — from audit's "Data Sources Used" section]
```

**Insights section:**

- Lead with the single biggest insight from the audit.
- Highlight 2-3 converging findings across sources. Be specific, use numbers, quote customers directly when verbatims are strong.
- Close with a revenue opportunity estimate if enough data exists. Show the math in one line.
- 4-6 short paragraphs max. No bullet points. Write it like a brief to a CEO who has 60 seconds.

---

### Slot Format: A/B Test

```markdown
## Slot [N]: [Short, Clear Test Name]

**Type:** A/B test ([N] variation vs. control)
**Page:** [Page name] ([URL])
**Revenue potential:** [Sessions/mo] x [conservative CR lift] x [AOV] = [estimated monthly revenue]. Show the math.

**Hypothesis:** If we [specific change], [measurable outcome] because [data-backed reason]. One sentence. Two max.

**Data:** [Evidence inline, citing sources with "Source:" prefix. One or two flowing sentences. No bullet points.]

**V[N]:** [One clear prose description. What changes, what stays the same, mobile and desktop behavior. Specific enough for a designer to mock up without further clarification.]
```

---

### Slot Format: Dev/Project

```markdown
## Slots [N & M]: [Short, Clear Project Name]

**Type:** [Custom Shopify app / Theme modification / Integration] ([N] slots)

**Why this is the priority:** [1-2 sentences]

**What we're building:** [High-level description.]

**Key requirements:**
- Requirement 1
- Requirement 2

**Success metrics:**
- Metric 1
- Metric 2
```

---

### Future Slot Candidates

If strong ideas didn't fit the allocated slots:

```markdown
## Future Slot Candidates

1. **[Idea]** - [One concise sentence on the opportunity.]
```

---

## Step 4: Pre-Publish Checklist

Run silently. Fix any issues before saving.

- [ ] Data Sources line lists every collected source from the audit.
- [ ] No UI assumptions. Every element in hypotheses and variations was documented in the audit.
- [ ] No hallucinated data. Every metric and quote traces to the audit.
- [ ] Time periods on all metrics.
- [ ] No em dashes anywhere.
- [ ] Revenue potential on every A/B test slot.
- [ ] Mobile and desktop specified in every variation.
- [ ] Each slot is distinct.
- [ ] Slots span at least 2 different pages or funnel stages.
- [ ] Variation count matches manifest.
- [ ] Total slot count matches manifest.

---

## Final Response

Say only:

```
Done.

1. brands/[brand-name]/[brand-name]-[month]-[year]-roadmap.md
```
```

- [ ] **Step 3: Verify the file saved correctly**

Read back `.claude/commands/cro-research-roadmap.md` and confirm:
- Step 1 reads manifest + audit MD only — no raw source files, no screenshots
- Step 2 fills slots using audit as sole reference
- No web research calls anywhere
- No screenshot loading anywhere
- Pre-publish checklist references audit, not raw sources

- [ ] **Step 4: Commit**

```bash
git add ".claude/commands/cro-research-roadmap.md"
git commit -m "refactor: rewrite cro-research-roadmap as audit-only roadmap command"
```

---

### Task 3: End-to-End Verification

- [ ] **Step 1: Dry-run `/cro-research` mentally**

Read `.claude/commands/cro-research.md` and trace through the flow with a hypothetical brand:
- Confirm Step 1 asks for all context in one chat message
- Confirm Step 2 creates folder and prints naming convention before asking for any data
- Confirm Step 3 asks for source selection in one chat message
- Confirm Step 4 collects text via chat, never asks for screenshots via chat
- Confirm Step 6 loads images one at a time per section (not upfront)
- Confirm no `AskUserQuestion` appears anywhere

- [ ] **Step 2: Dry-run `/cro-research-roadmap` mentally**

Read `.claude/commands/cro-research-roadmap.md` and trace:
- Confirm it reads manifest + audit only
- Confirm it references no raw/ files
- Confirm it references no screenshot loading
- Confirm it does no web research

- [ ] **Step 3: Run `/cro-research` on a real or test brand**

Execute the command. Verify:
- No `AskUserQuestion` tool is invoked at any point
- Folder is created and naming convention is printed before data collection
- Command ends with audit MD saved

- [ ] **Step 4: Run `/cro-research-roadmap` on the same brand**

Execute the command. Verify:
- Reads only manifest + audit MD
- Produces a valid roadmap MD
- Does not open any raw/ files or screenshots
