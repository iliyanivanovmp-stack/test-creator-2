---
name: cro-collect
description: Collect CRO source data for a Shopify prospect — intake only, no analysis
---

You are collecting CRO source data for a Shopify prospect. Your job is to intake source data, save it to disk, generate visual summary files from collected screenshots at the end, and write the manifest. Do not form CRO opinions or test ideas during collection.

Run `/cro-audit` after this command to generate the research audit.

---

## Data Integrity

- Save exactly what the user provides. Do not interpret, summarize, or analyze text inputs.
- During Step 1 through Step 3, never load or view any screenshot.
- During Step 4 only, load collected screenshots to write neutral visual summaries. Describe only what is visible; do not create CRO findings, hypotheses, or test ideas.
- Never run WebFetch. Save URLs to disk only.
- If a source is skipped, do not create a file for it.

---

## Step 1: Context

Say in chat (one message):

"To get started, send me:
- Store name
- Store URL
- Number of slots (default: 3)
- Any slots reserved for dev or project work
- Variations per test (default: 1 variation vs. control)
- Any specific areas of focus or concern

You can send all of this in one message."

Wait for reply. Save to `brands/[brand-name]/manifest.md` (create folder first).

Brand folder name: lowercase the store name, replace spaces with hyphens, remove special characters. Example: "Defender Shield" → `defender-shield`. Use this as `[brand-name]` throughout.

---

## Step 2: Create Folder + Print Naming Convention

After receiving the Step 1 reply, create:

```
brands/[brand-name]/
brands/[brand-name]/raw/
brands/[brand-name]/raw/screenshots/
```

Then say in chat:

"Folder created at `brands/[brand-name]/raw/screenshots/`. Drop all screenshots into that folder before we start — use these names:

**Meta Ads**
- `meta-ad-1.png`, `meta-ad-2.png`, `meta-ad-3.png`
- `meta-ad-1-lp-f1.png`, `meta-ad-1-lp-f2.png`, `meta-ad-1-lp-f3.png`
- `meta-ad-2-lp-f1.png`, `meta-ad-2-lp-f2.png`, `meta-ad-2-lp-f3.png`
- `meta-ad-3-lp-f1.png`, `meta-ad-3-lp-f2.png`, `meta-ad-3-lp-f3.png`

**Google Ads**
- `google-ads.png`

**Site pages**
- `homepage-f1.png`, `homepage-f2.png`, `homepage-f3.png`
- `collection-f1.png`, `collection-f2.png`, `collection-f3.png`
- `pdp-f1.png`, `pdp-f2.png`, `pdp-f3.png` (optional)
- `landing-page-f1.png`, `landing-page-f2.png`, `landing-page-f3.png`
- `cart.png`

**Emails**
- `email-1.png`, `email-2.png`, etc.

**Competitors / Inspiration**
- `competitor-[brand-name].png`
- `inspiration-[site-name].png`

Close names are okay. I will normalize common screenshot names at the summary step, including `ad-creative-1.png`, `ad1-landing-f1.png`, `google-ads-1.png`, `collections-f1.png`, and `cart-drawer.png`.

Now — which of these data sources do you have available?

1. Meta Ads and Landing Pages
2. Google Ads Transparency
3. Reviews & UGC
4. PageSpeed / Core Web Vitals
5. Competitor Insights
6. Inspiration Sites
7. Email Campaigns
8. Non-Data Context (call notes, strategic priorities)
9. Current Site Screenshots (homepage, collection, PDP)"

Wait for reply. Note selected sources. Record under `## Sources Selected` in the manifest.

---

## Step 3: Collect Text and URL Data

Only collect sources the user confirmed. Skip all others without asking. User can type `skip` at any point.

Do not ask for screenshots in chat. Screenshots go in the folder only. Do not load or analyze any screenshot.

**Meta Ads and Landing Pages**

Say: "For Meta Ads — send me the URL for Ad #1's landing page."
After reply: "URL for Ad #2, or `skip`."
After reply: "URL for Ad #3, or `skip`."

Save all URLs to `brands/[brand-name]/raw/meta-ads.md` under `## Landing Page URLs`. Do NOT WebFetch them — they will be fetched during `/cro-audit`.

**Google Ads Transparency**

Say: "For Google Ads — go to adstransparency.google.com, search [brand name], and drop the screenshots in the folder as `google-ads.png`. Anything else you can tell me about their Google Ads (messaging themes, offers, targeting)?"

Save any text to `brands/[brand-name]/raw/google-ads.md`. Do not analyze.

**Reviews & UGC**

Say: "Send me reviews — paste them directly, share a link, or type `skip`. Raw text is best."

Save as-is to `brands/[brand-name]/raw/reviews.md`. Do not summarize or interpret.

**PageSpeed / Core Web Vitals**

Say: "For PageSpeed — paste your mobile and desktop scores and any metrics (LCP, CLS, FID/INP), or give me the store URL and I'll fetch it during the audit. Or type `skip`."

If scores pasted: save to `brands/[brand-name]/raw/pagespeed.md`.
If URL provided: save URL to `brands/[brand-name]/raw/pagespeed.md` with note `[fetch during audit]`.

**Competitor Insights**

Say: "Any competitor data — names, pricing, weaknesses, UX patterns? Or type `skip` and I'll research during the audit."

If provided: save to `brands/[brand-name]/raw/competitors.md` labeled `[user-provided]`.

**Inspiration Sites**

Say: "Any inspiration sites? Send URLs and what caught your eye. Or type `skip`."

Save to `brands/[brand-name]/raw/inspiration.md`.

**Email Campaigns**

Say: "Send email copy, subject lines, CTAs, and performance data if you have it. Or drop screenshots as `email-1.png`, etc. into the folder. Type `done` when finished, or `skip`."

Wait for `done` or `skip`. Save any pasted text to `brands/[brand-name]/raw/emails.md`.

**Non-Data Context**

Say: "Any call notes, strategic priorities, known objections, or internal context? Or type `skip`."

Save to `brands/[brand-name]/raw/context.md`.

**Current Site Screenshots**

Say: "Drop homepage, collection, and PDP screenshots (top 3 folds each) into the folder using the naming convention above. PDP is optional. Type `done` when they're in place."

Wait for `done`.

---

## Step 4: Analyze and Summarize Screenshots

Run `ls brands/[brand-name]/raw/screenshots/` to capture all files present. Use this list to determine which image groups to load — only load files confirmed by the `ls` output.

Analyze only the three groups below. Do not load email, competitor, or inspiration screenshots.

Before loading screenshots, build a filename map from the actual `ls` output. Accept canonical names and close/legacy names. Do not rename user files unless the user explicitly asks; use the mapped actual filenames when loading.

**Accepted filename aliases**

Use these patterns case-insensitively. Treat hyphens, underscores, and spaces as equivalent where practical.

**Meta ad creatives**
- Canonical: `meta-ad-N.png`
- Also accept: `ad-creative-N.png`, `meta-ad-creative-N.png`, `facebook-ad-N.png`, `fb-ad-N.png`, `ad-N.png`

**Meta ad landing page folds**
- Canonical: `meta-ad-N-lp-fM.png`
- Also accept: `adN-landing-fM.png`, `ad-N-landing-fM.png`, `adN-lp-fM.png`, `meta-ad-N-landing-fM.png`, `meta-ad-N-lp-fold-M.png`
- Accept obvious typo variants such as `ladning` for `landing`.

**Google Ads**
- Canonical single screenshot: `google-ads.png`
- Also accept multiple screenshots: `google-ads-1.png`, `google-ads-2.png`, `google-ads-3.png`, `google-ads-f1.png`, `google-ads-f2.png`, `google-ads-f3.png`, `google-ad-1.png`

**Site screenshots**
- Homepage canonical: `homepage-fM.png`; also accept `home-fM.png`, `home-page-fM.png`
- Collection canonical: `collection-fM.png`; also accept `collections-fM.png`, `collection-page-fM.png`, `plp-fM.png`
- PDP canonical: `pdp-fM.png`; also accept `product-fM.png`, `product-page-fM.png`
- Landing page canonical: `landing-page-fM.png`; also accept `lp-fM.png`, `landing-fM.png`
- Cart canonical: `cart.png`; also accept `cart-drawer.png`, `cart-page.png`, `checkout-cart.png`

When multiple files map to the same canonical slot, use the closest canonical match first; otherwise use the lowest numbered matching file. Record any alias mapping uncertainty under `## Open Questions` in the manifest.

**Meta Ads (if any canonical or accepted Meta ad creative files are present):**

Load one ad group at a time. For each ad: load the mapped creative, then its mapped landing page folds 1-3 if present. Write the neutral visual summary entry, then move to the next ad.

Write `brands/[brand-name]/raw/meta-ads-visual-summary.md`:

```markdown
# Meta Ads Visual Summary

## Ad [N]
**Creative:** [Headline, visual content, format, CTA, offer visible in the ad]
**Landing Page Fold 1:** [Hero layout, primary headline, main CTA, above-fold offer]
**Landing Page Fold 2:** [Trust signals, product details, secondary elements visible]
**Landing Page Fold 3:** [Social proof, lower-funnel content, secondary CTAs]
**Message Match:** [Does the ad promise match what the landing page delivers? Note specific gaps.]

[Repeat for each ad present. If a landing page fold is missing, write "Not collected."]
```

**Google Ads (if any canonical or accepted Google Ads screenshot files are present):**

Load each mapped Google Ads screenshot in numeric order. Write `brands/[brand-name]/raw/google-ads-visual-summary.md`:

```markdown
# Google Ads Visual Summary

**Screenshots reviewed:** [Actual filenames loaded]
**Ads visible:** [Count and format types — search, display, shopping, etc.]
**Headline themes:** [Messaging angles and copy patterns across ads]
**Offers and CTAs:** [Specific offers, discounts, or CTAs visible]
**Visual approach:** [For display/shopping ads: imagery, layout style]
**Gaps vs. Meta:** [Any messaging inconsistencies with the meta ads summary]
```

**Site Pages (if any homepage, collection, PDP, cart, or landing page screenshots are present):**

Load mapped files in this canonical order, skipping any slot not present: `homepage-f1.png`, `homepage-f2.png`, `homepage-f3.png`, `collection-f1.png`, `collection-f2.png`, `collection-f3.png`, `pdp-f1.png`, `pdp-f2.png`, `pdp-f3.png`, `landing-page-f1.png`, `landing-page-f2.png`, `landing-page-f3.png`, `cart.png`. Write one summary file after loading all available files.

Write `brands/[brand-name]/raw/site-visual-summary.md`:

```markdown
# Site Visual Summary

## Homepage
**Fold 1:** [Hero layout, primary headline, CTA placement, trust signals above the fold]
**Fold 2:** [Navigation, featured sections, secondary offers visible]
**Fold 3:** [Social proof, product grid or content blocks, additional CTAs]
**Layout notes:** [Specific elements, their position, visual treatment — describe what exists, not what should change]

## Collection Page
**Fold 1:** [Header, filter controls, product card layout and content]
**Fold 2:** [Card density, imagery style, price display, CTA buttons]
**Fold 3:** [Pagination, sorting UI, anything below the initial grid]
**Layout notes:** [Specific layout details]

## PDP (if present)
**Fold 1:** [Product images, buy box structure, price display, primary CTA]
**Fold 2:** [Description, specs, trust signals, secondary CTAs]
**Fold 3:** [Reviews placement, upsells, related products, FAQ if visible]
**Layout notes:** [Specific buy box and conversion element details]

## Cart (if present)
**Layout:** [Cart structure — drawer or page, item summary, upsell placement, CTA]
**AOV elements:** [Any upsell, cross-sell, bundle, or threshold mechanics visible]

## Landing Pages (if present)
**Fold 1:** [Hero, headline, primary CTA]
**Fold 2:** [Offer details, trust signals, secondary elements]
**Fold 3:** [Social proof, lower-funnel content]
**Message match:** [Does the LP deliver on what the ad promised?]
```

---

## Step 5: Write Manifest

Run `ls brands/[brand-name]/raw/screenshots/` to capture all files present.

Use the same alias map from Step 4 when deciding which sources were collected. If screenshots exist for a source, record that source as collected even when the user did not use canonical filenames.

If neither `cart.png` nor an accepted cart alias such as `cart-drawer.png` is present, record `MISSING_DATA: cart_drawer` in the manifest. If `cart-drawer.png` or another cart alias is present, record it as cart collected and note the actual filename.

Write `brands/[brand-name]/manifest.md`:

```markdown
# [Brand Name] CRO Collection Manifest

## Brand Info

- Store name: [name]
- Store URL: [url]
- Slots: [N] total, [N] dev/project slots
- Variations per test: [N]
- Areas of focus: [any specific concerns]

## Sources Selected

- [List sources the user confirmed having]

## Sources Collected

- [Source name] → raw/[filename].md
- [Source name] → screenshots in folder
- Meta Ads (if collected) → raw/meta-ads-visual-summary.md
- Google Ads (if collected) → raw/google-ads-visual-summary.md
- Site Screenshots (if collected) → raw/site-visual-summary.md
- [If screenshots used accepted aliases, add: Screenshot aliases mapped → [actual filename] used as [canonical slot]]

## Screenshots Present

- [List files from ls output]

## Sources Skipped

- [Source name]

## Missing Data Warnings

- [MISSING_DATA: cart_drawer — not captured. Cart/AOV opportunities cannot be evaluated.]
- [Remove this section if no gaps.]

## Open Questions

- [any uncertainty]

## Next Step

Run `/cro-audit` to generate the research audit.
```

---

## Final Response

Say only:

```
Collection complete.

Files saved:
- brands/[brand-name]/manifest.md
- brands/[brand-name]/raw/[source files]
- brands/[brand-name]/raw/screenshots/ ([N] files)
- brands/[brand-name]/raw/meta-ads-visual-summary.md (if collected)
- brands/[brand-name]/raw/google-ads-visual-summary.md (if collected)
- brands/[brand-name]/raw/site-visual-summary.md (if collected)

Next step: Run /cro-audit.
```
