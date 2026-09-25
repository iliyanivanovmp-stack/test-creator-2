# Bon Charge Roadmap Seed

**Store:** https://boncharge.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed/Core Web Vitals, Current Site Screenshots (homepage, collection, cart), Social & Community Research, live WebFetch re-verification (2026-09-12), competitor WebSearch

## Key Insights

Live re-verification on 2026-09-12 found all three active Meta ad landing pages sold out: Tortoise Shell Computer Glasses, Crystal Computer Glasses, and the Red Light Face Mask. The Red Light Face Mask page shows "Sold out" while its own copy still reads "In Stock | Limited Quantities Available" — a contradiction on the same page. Ads 1 and 2 promise "the full BON CHARGE wellness collection" but land on a single eye-strain SKU, with no mention of the product shown or the 25% sitewide discount live on the page.

Real Lighthouse data (2026-09-12) shows the homepage scoring 0.16 (LCP 14.7s, TBT 3,410ms) and the PDP scoring 0.32 (LCP 13.2s) — 3-4x past Google's "poor" threshold, with Time to Interactive over 44s on each. A currency bug recurs on three surfaces: the homepage banner shows "$125" free shipping while PDP/ad pages show "€115," and the cart prices its upsell in USD ($356.21) against an otherwise EUR cart.

Trust signals split: boncharge.com carries a 2.4 TrustScore (6 reviews, as of 2026-09-11), while legacy domain blublox.com holds 4 stars from 1,400+ reviews — directional, from automated research, unconfirmed by the 5 first-party reviews collected (all positive, too few to weigh in).

## Top Test Opportunities

### 1. Fix or message out-of-stock ad landing pages
**What's broken:** All three Meta-ad-driven PDPs are sold out, live-verified 2026-09-12. The Red Light Face Mask PDP shows "Sold out" while buy-box copy above it still reads "In Stock | Limited Quantities Available" — both messages at once.
**Evidence:** meta-ads-visual-summary.md, live WebFetch re-check
**Key data:** 3 of 3 active Meta creatives point to sold-out PDPs
**Est. lift:** unknown (no sessions/AOV); blocks 100% of tracked ad traffic while active

### 2. Align glasses ad copy to landing page reality
**What's broken:** Ads 1 (Tortoise Shell) and 2 (Crystal) both use "Enhance your wellbeing. Shop the full BON CHARGE wellness collection." Both land on a single-SKU eye-strain PDP with no collection framing, no product name from the ad, and no mention of the 25% sitewide discount already live on the page.
**Evidence:** meta-ads-visual-summary.md (Ads 1 & 2)
**Key data:** same copy across 2 creatives, both mismatched to single-SKU pages
**Est. lift:** unknown (no sessions/AOV)

### 3. Reduce homepage and PDP load weight
**What's broken:** Homepage hero is a full-width autoplaying video plus more autoplaying testimonial video in fold 3; PDP carries a 4-clip video testimonial grid. Lighthouse: homepage 0.16 (LCP 14.7s, CLS 0.234, TBT 3,410ms), PDP 0.32 (LCP 13.2s, TBT 900ms). Both exceed 44s Time to Interactive.
**Evidence:** raw/pagespeed.md (real Lighthouse JSON, 2026-09-12)
**Key data:** LCP 14.7s / 13.2s vs. Google's 4s "poor" threshold
**Est. lift:** unknown (no sessions/AOV)

### 4. Fix the currency/locale display bug
**What's broken:** Homepage banner reads "Free Shipping on Orders Over $125" (live, 2026-09-12); the same banner on PDP/ad pages reads "€115." In the cart, the face mask line item is EUR while the upsell below it shows "$356.21" USD, unflagged.
**Evidence:** site-visual-summary.md, live WebFetch re-check
**Key data:** mismatch recurs on 3 separate surfaces
**Est. lift:** unknown; risk is checkout trust, not raw CR

### 5. Add a sticky CTA to the homepage
**What's broken:** Homepage's only CTA is one non-sticky red "Shop Best Sellers" button; no sticky header/CTA exists across its three folds. PDP and Ad 3's landing page both carry a persistent sticky bar (product, price, Add to Cart) on every fold.
**Evidence:** site-visual-summary.md (homepage vs. PDP/LP CTA comparison)
**Key data:** sticky CTA on 2 of 3 page types, absent on the homepage
**Est. lift:** unknown (no sessions/AOV)

### 6. Add trust signal inside the cart drawer
**What's broken:** The cart drawer shows only a free-shipping banner, the line item, an upsell, and "Checkout Securely" — no guarantee, returns, or warranty badge, despite the PDP showing "30-Day Easy Returns · 1-Year Warranty" under its own Add to Cart.
**Evidence:** site-visual-summary.md (Cart section)
**Key data:** 0 trust badges in cart vs. 4-icon trust row on PDP
**Est. lift:** unknown (no sessions/AOV)

### 7. Verify and fix Google Ads Transparency 500-error units
**What's broken:** Multiple units in the Google Ads Transparency Center screenshots render "500. That's an error" instead of creative, across a 30+-unit set spanning glasses, face mask, toothbrush, and hair-growth lines.
**Evidence:** google-ads-visual-summary.md
**Key data:** error state on multiple units in the set that also showed live OOS PDPs on Meta
**Est. lift:** unknown; needs a live click-through of the specific units, not done here

### 8. Reconcile the Trustpilot domain split
**What's broken:** boncharge.com shows a 2.4 TrustScore from only 6 reviews (2026-09-11); legacy domain blublox.com carries 4 stars from 1,400+ reviews. A prospect searching independently likely lands on the low-scoring result first.
**Evidence:** last30days-ecom.md (directional, single automated source; unconfirmed by the 5 first-party reviews collected)
**Key data:** 2.4/5 (6 reviews) vs. 4/5 (1,400+ reviews), same brand
**Est. lift:** unknown; reputation risk, not a directly testable on-site mechanic

## Unused Findings

- The Face, Neck and Chest Bundle shows "Save 30%" in the collected screenshot but "7% savings" on live re-check — unreconciled, verify before citing either figure.
- Ad 2's collected fold-3 screenshot shows a different product (Tortoise Shell) than folds 1-2 (Crystal) — may be a capture-time issue, not confirmed as live site behavior.
- Only 5 reviews were collected for the Red Light Face Mask despite the homepage claiming "5,700+ Reviews" store-wide — expand the sample before drawing product-quality conclusions in future audits.
