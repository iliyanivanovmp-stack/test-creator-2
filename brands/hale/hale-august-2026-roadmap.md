# Hale CRO Research Brief

**Data Sources:** Google Ads Transparency, PageSpeed/Core Web Vitals (Lighthouse, mobile), Current Site Screenshots (homepage, PDP, cart), Reviews & UGC (live widget fetch), self-researched competitor analysis

---

## Insights

Hale's mobile Core Web Vitals fail badly on both key pages. Homepage LCP is 7.5 seconds and PDP LCP is 5.9 seconds, both roughly 3x the "good" 2.5-second threshold. Time to Interactive sits near 20 seconds on both pages. Source: PageSpeed, Aug 2, 2026. Since Google Ads is Hale's primary paid channel, this load tax hits every dollar of ad spend before any other test can show its true effect. It's the ceiling on everything else in this roadmap.

Trust signals are inconsistently distributed across the funnel. The PDP carries a strong 4.8-star, 1,342-review rating directly above the buy box, plus a "Trusted by 16,000+ customers" strip. Source: Site screenshots (PDP). None of this appears on the homepage, which instead relies on retailer logos (Walgreens, Walmart, Target) and a numbered claims list. The homepage hero itself (fold 1) has no CTA button at all; the first path to purchase doesn't appear until fold 2. Source: Site screenshots (homepage).

Pricing shows a mismatch worth resolving before testing anything price-related. A live homepage fetch on Aug 2, 2026 shows $44.99/$89.99/$134.99 for the 30/90/150-day tiers, while the PDP buy box screenshot shows $39.99/mo, $79.99, $119.99 against a $44.99/mo reference. Source: Live homepage fetch, PDP screenshot. Google Ads also lead with flat "-33%"/"-60%" discount badges that don't map cleanly to either page's multi-buy framing ("Buy 2 Get 1 Free," "Buy 3 Get 2 Free"). Source: Google Ads visual summary. This may reflect a genuine pricing update between collection dates rather than a defect, but it needs confirmation before any price test runs.

Reviews, fetched live since no raw export was collected, surface strong quantified testimonials: "BP went from 152/92 to 121/78," "last scan showed no progression." Source: Reviews (live widget fetch). No negative themes surfaced, which is more likely a widget-curation artifact than proof of a friction-free product, and is flagged as a data gap rather than a finding.

No sessions or AOV data was provided for Hale, so revenue potential below is directional (lift percentage) rather than a dollar figure. The client should supply this to size each slot precisely.

---

## Slot 1: Fix Homepage & PDP Page Speed

**Type:** Immediate Fix
**Page:** Homepage (https://halesupplement.com/) and Product Detail Page

**Why this is the priority:** On Aug 2, 2026, mobile Performance scored 68/100 on the homepage (LCP 7.5s, Time to Interactive 19.7s) and 69/100 on the PDP (LCP 5.9s, Time to Interactive 20.9s). Both LCP scores run 2.4-3x over Google's 2.5-second "good" threshold. Source: PageSpeed/Lighthouse JSON, mobile. Google Ads is Hale's primary acquisition channel, so this tax hits 100% of paid traffic before any other test can show its true effect.

**What to fix:** Identify and remediate the root cause of slow LCP and Time to Interactive on both mobile templates (likely render-blocking scripts, unoptimized hero imagery, or theme/app bloat). Target LCP under 2.5s and Time to Interactive under 5s on both pages.

**Success metrics:**

- Mobile homepage and PDP LCP
- Mobile homepage and PDP Time to Interactive
- Mobile bounce rate and conversion rate after release

---

## Slot 2: Homepage Hero CTA and Trust Signal

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://halesupplement.com/)
**Revenue potential:** Not calculable, sessions/mo and AOV were not provided. Directional: adding a fold-1 CTA and surfacing an existing review count typically improves top-of-funnel click-through to the PDP.

**Hypothesis:** If we add a CTA button and the site's 4.8-star, 1,342-review count to the homepage's fold-1 hero, more visitors click through to the PDP because the current hero is image and headline only, with no path to purchase and no credibility signal until fold 2, where the first CTA appears.

**Data:** The homepage fold-1 hero shows a lifestyle image with overlay text "Transform Your Health With Hale" and no CTA button anywhere in the fold. The first CTA ("Get Started →") doesn't appear until fold 2, alongside retailer logos. No star rating or review count appears in any of the three homepage folds, despite the PDP carrying a 4.8-star, 1,342-review rating directly above its buy box. Source: Site screenshots (homepage, PDP).

**V1 (Mobile and Desktop):** Add a CTA button ("Get Started →," matching the existing maroon button style used in fold 2) directly into the fold-1 hero, and add the "4.8 ★ | 1,342 Reviews" line beneath the hero headline. Hero image, headline copy, and fold 2 content stay unchanged. On mobile, stack the rating line above the CTA button to keep both visible without pushing content below the fold.

---

## Slot 3: Cart Cross-Sell

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (slide-out drawer, site-wide)
**Revenue potential:** Not calculable, sessions/mo, AOV, and attach-rate data were not provided. Directional: AOV-focused, sized against the cart's current single-item, zero-cross-sell state.

**Hypothesis:** If we add a one-click cross-sell tile for Hale Preserve and Hale Longevity to the cart drawer, average order value increases because the drawer currently shows a single line item with no cross-sell, bundle, or free-shipping mechanic, despite two other product lines existing in the site nav.

**Data:** The cart is a slide-out drawer showing a single line item ("Hale Heart, 90 Day Supply"), a reservation countdown timer, and an unpopulated "Discount" field. No cross-sell, bundle, or free-shipping progress bar appears, despite Hale Preserve and Hale Longevity existing as separate product lines in the site nav. Source: Site screenshots (cart drawer).

**V1 (Mobile and Desktop):** Add a single one-click cross-sell tile below the line item, showing Hale Preserve or Hale Longevity (whichever the client confirms as the stronger complement to Hale Heart) with a one-click "Add" button. Countdown timer, discount field, and checkout button position stay unchanged. On mobile, the tile sits as a horizontally scrollable card below the line item to avoid pushing the checkout button off-screen.

---

## Slot 4: Fix Homepage vs. PDP Pricing Mismatch

**Type:** Immediate Fix
**Page:** Homepage (https://halesupplement.com/) and Product Detail Page

**Why this is the priority:** A live homepage fetch on Aug 2, 2026 shows $44.99/$89.99/$134.99 for the 30/90/150-day tiers, while the PDP buy box screenshot shows $39.99/mo, $79.99, $119.99 against a $44.99/mo reference. Two different price sets exist for the same tiers across two touchpoints. Source: Live homepage fetch, PDP screenshot. Price confusion at the moment of highest intent, moving from homepage to PDP, directly suppresses conversion.

**What to fix:** Confirm with the client whether this reflects a live pricing update or a genuine defect, then align homepage and PDP pricing to a single correct set. While resolving this, also verify that the Google Ads "-33%"/"-60%" discount badges map clearly to the resulting multi-buy tier structure ("Buy 2 Get 1 Free," "Buy 3 Get 2 Free").

**Success metrics:**

- Homepage and PDP tier pricing match exactly
- Ad discount badges reconcile to the live multi-buy structure

---

## Slot 5: Correct Google Ads FU Dose Claim

**Type:** Immediate Fix
**Page:** Google Ads creative

**Why this is the priority:** One Google Ads graphic states "10,000 FU Dose," while every other ad, the PDP, and the homepage cite "10,800 FU." Source: Google Ads visual summary. A conflicting dosage figure on the exact clinical claim driving ad clicks is a message-match risk on Hale's core differentiator.

**What to fix:** Confirm which figure is correct, then update or pause the "10,000 FU Dose" ad asset so all ad creative matches the "10,800 FU" figure used on-site.

**Success metrics:**

- Zero active ads with a conflicting FU dose figure
- Ad dosage claim matches PDP and homepage copy on all active ads

---

## Future Slot Candidates

No additional findings met the data support, revenue potential, and actionability bar this cycle. The audit flags one open item worth client follow-up outside this roadmap: no raw review export was collected, and the live widget fetch surfaced only positive-themed reviews. This is a data gap, not a confirmed complaint-free product. If the client pulls raw review data from their review platform's admin panel, a future pass could surface a friction-reduction test opportunity.
