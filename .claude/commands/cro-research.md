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
