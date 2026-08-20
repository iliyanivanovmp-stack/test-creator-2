# Hale Roadmap Seed

**Store:** https://halesupplement.com/
**AOV:** Unknown (pricing tiers range $39.99-$134.99 depending on subscription/multi-buy tier; client should confirm actual AOV)
**Monthly sessions:** Unknown
**Data sources:** Google Ads Transparency, PageSpeed/Core Web Vitals (Lighthouse, mobile), Current Site Screenshots (homepage, PDP, cart), Reviews & UGC (live widget fetch), self-researched competitor analysis

## Key Insights

Hale's mobile Core Web Vitals fail badly on both key pages: homepage LCP is 7.5s and PDP LCP is 5.9s, both roughly 3x the "good" 2.5s threshold, with Time to Interactive near 20 seconds on both. Since Google Ads is Hale's primary paid channel, this tax hits every dollar of ad spend before any other test can show its true effect — it's the ceiling on everything else in this roadmap.

Trust signals are inconsistently distributed across the funnel. The PDP carries a strong 4.8-star, 1,342-review rating directly above the buy box, plus a "Trusted by 16,000+ customers" strip — but none of this appears on the homepage, which instead relies on retailer logos (Walgreens, Walmart, Target) and a numbered claims list. The homepage hero itself (fold 1) has no CTA button at all; the first path to purchase doesn't appear until fold 2.

Pricing shows a mismatch worth resolving before testing: a live homepage fetch (Aug 2, 2026) shows $44.99/$89.99/$134.99 for the 30/90/150-day tiers, while the PDP buy box screenshot shows $39.99/mo, $79.99, $119.99 against a $44.99/mo reference. Google Ads also lead with flat "-33%"/"-60%" discount badges that don't map cleanly to either page's multi-buy framing ("Buy 2 Get 1 Free," "Buy 3 Get 2 Free"). This may reflect a genuine pricing update between collection dates rather than a bug, but it needs client confirmation before any price-related test runs.

Reviews (fetched live, since no raw export was collected) surface strong quantified testimonials — "BP went from 152/92 to 121/78," "last scan showed no progression" — but no negative themes, which is more likely a widget-curation artifact than proof of a friction-free product. Competitor Toku Health runs a structured "Heart Health Journey" (baseline tracking, 90-day retest, reward for completion) that directly targets the same "gradual results" pattern visible in Hale's reviews — a retention mechanic Hale doesn't appear to have.

## Top Test Opportunities

### 1. Homepage Hero CTA and Trust Signal
**What's broken:** The homepage fold-1 hero shows a lifestyle image of an older couple outdoors with overlay text "Transform Your Health With Hale" — no CTA button anywhere in the fold. The first CTA ("Get Started →," maroon button) doesn't appear until fold 2, alongside retailer logos (Walgreens, Walmart, Target). No star rating or review count appears in any of the three homepage folds, despite the PDP carrying a 4.8-star, 1,342-review rating directly above its buy box.
**Evidence:** site-visual-summary.md (homepage), live homepage fetch
**Key data:** 4.8 stars / 1,342 reviews exists and is used on PDP but absent from homepage; no fold-1 CTA
**Est. lift:** Not calculable without sessions/AOV data. Directional: adding a fold-1 CTA and surfacing the review count typically improves top-of-funnel CTR to PDP.

### 2. Cart Cross-Sell
**What's broken:** The cart is a slide-out drawer showing a single line item ("Hale Heart, 90 Day Supply," $79.99 vs. struck-through $179.99), a reservation countdown timer, and an unpopulated "Discount" field. No cross-sell, bundle, or free-shipping progress bar appears, despite two other product lines (Hale Preserve, Hale Longevity) existing in the site nav.
**Evidence:** site-visual-summary.md (cart)
**Key data:** Zero cross-sell mechanics in a drawer with two unlinked product lines available
**Est. lift:** AOV-focused; not calculable without attach-rate assumptions from client.

### 3. Page Speed Remediation
**What's broken:** This is a performance fix, not a UI test. Homepage scores 68/100 Performance (mobile) with LCP 7.5s; PDP scores 69/100 with LCP 5.9s. Time to Interactive is 19.7s (homepage) and 20.9s (PDP).
**Evidence:** raw/pagespeed.md (Lighthouse JSON, both pages)
**Key data:** LCP 3x the "good" threshold on both pages; this gates the ceiling on every other test run on paid traffic
**Est. lift:** Not a CR-lift test; industry-standard LCP fixes of this magnitude often correlate with 5-10% mobile CR gains, but not calculable for Hale specifically without sessions/AOV.

### 4. Pricing Message-Match Verification
**What's broken:** Live homepage pricing ($44.99/$89.99/$134.99 for 30/90/150-day) does not match the PDP buy box screenshot ($39.99/mo, $79.99, $119.99 vs. a $44.99/mo reference). Google Ads lead with flat percentage discounts ("-33%," "-60%") that don't map to either page's multi-buy tier structure.
**Evidence:** raw/google-ads-visual-summary.md, live homepage fetch, site-visual-summary.md (PDP)
**Key data:** Two different price sets found for the same tiers across two touchpoints
**Est. lift:** Not calculable until the client confirms whether this is a live pricing change or a genuine defect; resolving it is a message-match fix, not an A/B test.

### 5. Review Widget Complaint Data Verification
**What's broken:** No raw review export was collected; a live widget fetch for this audit surfaced only positive-themed reviews (specific BP and imaging improvements), which likely reflects review-widget curation rather than a complaint-free product.
**Evidence:** raw/reviews.md, live PDP reviews fetch
**Key data:** 4.8 stars / 1,342 reviews, zero negative themes surfaced
**Est. lift:** Not a test opportunity as-is; recommend the client pull raw review data from their review platform's admin panel before building any friction-reduction test around an assumed complaint theme.

## Unused Findings

- The Google Ads "10,000 FU Dose" graphic conflicts with the "10,800 FU" figure used everywhere else in ads and on-site — worth a quick client check for a stale ad asset.
- Toku Health's "Heart Health Journey" (health tracking + 90-day reward) targets the same "gradual results" churn risk visible in Hale's reviews — a retention-mechanic idea outside standard CRO testing scope.
