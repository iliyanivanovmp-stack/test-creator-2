# Soulffee CRO Research Audit

## Data Sources Used

**User-provided:**
- PageSpeed / Core Web Vitals — homepage and PDP (collected Jul 8, 2026)
- Site screenshots — homepage (4 folds), PDP (3 folds), cart drawer

**Self-researched:**
- Live site fetch: soulffee.com (homepage + PDP), Jul 8, 2026

**Not available:**
- Meta Ads (brand does not run Meta ads)
- Google Ads (brand does not run Google ads)
- Reviews & UGC (not collected)
- Competitor data (not collected)
- Email campaigns (not collected)
- Inspiration sites (not collected)

---

## Source Findings

### Meta Ads & Landing Pages

Not collected. Brand confirmed not running Meta ads at time of collection.

### Google Ads

Not collected. Brand confirmed not running Google ads at time of collection.

### Reviews & UGC

Not collected. The live PDP shows 38 reviews at 4.8+ stars. The live homepage references "24+ verified customer testimonials." Review content was not collected for deep analysis.

**Available from live site fetch (sample themes):**
- "Smooth and rich, without the bitterness regular coffee often has"
- "Gives me steady energy boost that lasts all day"
- "Gentle on my stomach" — recurring across multiple reviews

These signals suggest taste/texture satisfaction and digestive tolerance are primary drivers. Without full review data, sentiment analysis is limited.

#### What Customers Love

- Taste and texture: smooth, nutty, not bitter
- Energy without jitters or crashes
- Stomach-friendly vs. coffee

#### What Frustrates Customers

- Not captured (no full review dataset)

#### Client-Actionable Insights

- "Gentle on my stomach" is a recurring differentiator — product messaging should lead with this, not just "no jitters"
- 38 reviews is a thin social proof base for a health/wellness product; a structured review collection campaign would accelerate trust

---

### PageSpeed / Core Web Vitals

Collected: Jul 8, 2026. Mobile (Lighthouse simulation).

**Homepage (soulffee.com)**

| Metric | Value | Score |
|--------|-------|-------|
| Performance | 59/100 | Needs Improvement |
| LCP | 10.3 s | 0/1 (Failing) |
| FCP | 4.8 s | 0.11 |
| Speed Index | 5.3 s | 0.57 |
| TTI | 13.8 s | 0.10 |
| TBT | 180 ms | 0.92 |
| CLS | 0 | 1.0 (Pass) |

**PDP (/products/soulffee)**

| Metric | Value | Score |
|--------|-------|-------|
| Performance | 65/100 | Needs Improvement |
| LCP | 14.9 s | 0/1 (Failing) |
| FCP | 2.8 s | 0.56 |
| Speed Index | 5.2 s | 0.60 |
| TTI | 17.5 s | 0.04 |
| TBT | 160 ms | 0.94 |
| CLS | 0.013 | 1.0 (Pass) |

**Interpretation:** Both pages fail LCP at the critical threshold. A 10.3s LCP on the homepage means most mobile users are staring at an unloaded hero for 10+ seconds. The PDP is worse at 14.9s LCP — the product image carousel is the likely culprit. TTI of 13.8s (homepage) and 17.5s (PDP) means the page is unresponsive to user input for a very long time on mobile. CLS is clean on both pages.

---

### Competitor Analysis

Not collected. No user-provided competitor data. Self-research not conducted at this audit stage — recommend running competitor fetch in roadmap phase.

---

### Emails

Not collected.

---

### Inspiration Sites

Not collected.

---

### Non-Data Context

Not collected.

---

### Current Site Screenshots

**Live site fetch supplement:** The homepage confirms 24+ reviews, a "Learn" section (Formula, Recipes, Articles), founder story, and a newsletter CTA. The funnel is single-product: homepage → PDP. No collection page exists.

**Homepage**

Fold 1 loads the full hero (headline: "Calm Mind, Clear Focus, No Jitters") but the primary CTA ("TRY NOW →") is cut off below the visible viewport. Users must scroll to find the button. The star rating "Rated 4.8+ stars" appears in fold 1 but has no review count — the social proof is unquantified.

Fold 2 surfaces the CTA and a "Happiness Guaranteed" badge, along with a dual scrolling trust marquee ("Made in the USA", "100% Natural", "2,200mg of Mushrooms", "Lab Tested" / "No Artificial Flavoring", "Vegan"). A product feature section begins: "It's Not Coffee. It's Better." with "38mg caffeine" chip.

Fold 3 expands the feature section with four benefit bullets and six icon badges (Scientifically Proven, Sharper Clarity, Sustained Energy, Happiness Booster, Optimized Digestion, Laser Focus). A "Try Soulffee Today →" CTA appears here — the second CTA on the page.

Fold 4 shows a comparison table: Soulffee vs. Mushroom Coffee across 6 attributes. Soulffee wins 5/6. No CTA appears below the table. Users who scroll to the bottom of the homepage have no next action visible.

**Conversion friction on homepage:**
- Hero CTA is below the fold — the most motivated visitors have to scroll to act
- Social proof count hidden ("4.8+ stars" with no review number)
- Comparison table terminates with no CTA — high-intent visitors who read this far have nowhere to click

**PDP**

Fold 1: Two-column layout. Buy box shows "Mushroom Orzo", $32.00, "Only $1.07 per cup!", star rating "★★★★★ 38 reviews", and a purchase toggle. The one-time purchase option ($32.00) is pre-selected. Subscribe & Save (19% off, $25.92) is visible but unselected. The size selector (30 vs 60 servings) uses a filled vs. outlined treatment — 30 servings is the selected default.

Fold 2: "TRY IT NOW" full-width CTA in dark green. "Why Soulffee?" accordion (open by default). Subscription Perks and How to Use accordions are collapsed.

Fold 3: Trust ticker, repeat benefit section ("It's Not Coffee. It's Better."), and a sticky product widget overlay showing: product thumbnail, "Mushroom Orzo | 30 servings | $32.00", and a "TRY IT NOW" button. The sticky widget follows the user through all PDP content.

**Conversion friction on PDP:**
- Subscribe & Save is unselected by default — the highest-LTV option is deprioritized
- Product URL is `/products/soulffee` but in-page title reads "Mushroom Orzo" — naming inconsistency may erode trust ("Is this the right product?")
- No reviews section visible in 3 collected folds — 38 reviews exist but are not surfaced near the buy box
- No upsells or cross-sells visible anywhere on the PDP

**Cart**

Mobile cart (not a drawer). Single line item: Mushroom Orzo, 30 servings, qty 2, $64.00 subtotal. Free shipping already unlocked ("CONGRATS YOU'VE UNLOCKED FREE SHIPPING!" with full green progress bar). Announcement bar: "Limited Inventory - Save Up to 38% Today!" — but no discount mechanism is visible within the cart. No upsells, cross-sells, bundle prompts, or product recommendations visible. The checkout CTA is cut off below the screenshot boundary — button not captured.

**Conversion friction in cart:**
- No AOV optimization mechanic — zero path to increase order value from cart
- Scarcity/discount messaging ("Save Up to 38% Today") has no corresponding offer in cart — creates broken promise
- 60-serving upgrade prompt absent — natural upsell to a 2x order is untapped
- Free shipping already unlocked with no next threshold — the progress bar mechanic has no further use

---

## Cross-Source Themes

**Ranked by evidence strength x revenue potential x funnel importance:**

**1. Subscribe & Save is buried while one-time purchase leads**
Every data source that touches the PDP confirms OTP is the default. The subscription option (19% discount, recurring revenue) is visible but unselected, with no visual treatment distinguishing it as the higher-value choice. For a single-SKU brand, subscription rate is the primary business metric — this is the most revenue-critical gap.

**2. Critical page speed failures on mobile (LCP 10.3s + 14.9s)**
Both pages score 0/1 on LCP. Homepage takes 10.3 seconds to paint its largest element on mobile; PDP takes 14.9 seconds. At these load times, a significant portion of mobile traffic bounces before the product is ever seen. Google benchmarks suggest 53% of mobile sessions are abandoned when load time exceeds 3 seconds.

**3. Multiple CTA dead zones across the funnel**
The hero CTA is below viewport on load. The comparison table has no CTA below it. The cart has no upsell path. The PDP reviews section is not visible in the first 3 folds. Across the full funnel — homepage, PDP, and cart — there are repeated points where high-intent visitors have no clear next action.

---

## Top Test Opportunities

**1. Subscribe & Save as Default PDP Selection** — One-time purchase is pre-selected; the subscription option (19% discount = $25.92 vs $32.00) is visible but unselected. For a single-SKU brand, every OTP buyer who should have subscribed is a recurring revenue miss. Evidence: PDP screenshot (fold 1 buy box), live site fetch. Est. lift: flipping default to subscription + adding benefit callout could convert 15-25% of current OTP buyers to subscribers; at any reasonable LTV multiple, this is the highest-value test available.

**2. Hero CTA Above the Fold** — On mobile and most desktop viewports, the "TRY NOW →" button is cut off below the visible area of fold 1. The headline and subtext are visible, but the action is hidden. Users who arrive with intent have to scroll to convert. Evidence: homepage-f1.png, homepage-f2.png. Est. lift: 5-10% increase in homepage-to-PDP CTR; sessions x current CTR baseline unknown, but above-fold CTA access is a consistently validated test.

**3. 60-Serving Upgrade Prompt in Cart** — Cart contains zero upsell mechanics. The 60-serving variant exists on the PDP (shown in size selector) but is never presented in cart. A cart upgrade prompt ("Get 2x the supply and save — upgrade to 60 servings") is a direct AOV lever. Evidence: cart screenshot (no upsells visible), PDP screenshot (60-serving variant available). Est. lift: 10-15% of single-unit cart visitors upgrade; at $32 AOV → ~$53+ upgrade AOV = approx. +$21 per converted upsell.

**4. Comparison Table CTA (Homepage Fold 4)** — The comparison table is the deepest content on the homepage and represents the highest-intent scroll position. Users who reach it have read through all the benefit and feature content. The table ends with no CTA. Adding a CTA ("Try Soulffee Today →") directly below the table captures high-intent visitors at their peak consideration moment. Evidence: homepage-f4.png. Est. lift: 3-7% increase in homepage-to-PDP CVR from scroll-depth cohort.

**5. Reviews Block Above the Buy Box Fold** — 38 reviews with 4.8 stars exist but are not visible within the first 3 folds of the PDP. The star rating appears in the buy box on fold 1 (clickable), but no review content is surfaced near the purchase decision. For a health/wellness product where trust is the purchase barrier, surfacing 2-3 top reviews near the buy box is a standard high-impact CRO move. Evidence: PDP screenshots (folds 1-3), live fetch (confirms reviews exist). Est. lift: 4-8% PDP CVR improvement typical for social proof placement optimization.

---

## Unused but Valuable Findings

- Product naming inconsistency: URL is `/products/soulffee` but page title reads "Mushroom Orzo" — may suppress branded search click-through and creates a trust gap for returning visitors.
- "Save Up to 38% Today" announcement bar in cart references a discount with no corresponding cart-level mechanism — this is a broken promise that erodes trust at the final conversion step.
- "Rated 4.8+ stars" on homepage shows no review count — the social proof claim is unverifiable to visitors; adding the count ("4.8 stars from 38 reviews") converts a vague signal into a concrete one.

---

## Missing Data

- **Reviews & UGC** — Not collected. Only 38 reviews total; qualitative themes cannot be fully mapped. This limits identification of objections that should be addressed in PDP copy or FAQ content.
- **Competitor data** — Not collected. No benchmark for pricing, positioning, or subscription offer structure against rivals (Four Sigmatic, Ryze, MudWtr, etc.).
- **Traffic/session volume** — No analytics access. Revenue impact estimates are directional only (lift % x unknown sessions).
- **Cart screenshot completeness** — Checkout CTA not captured (mobile screenshot cut off). Cannot confirm button copy, color, or sticky behavior.
