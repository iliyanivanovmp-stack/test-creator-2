# Mindful Souls CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads Transparency Center, PageSpeed/Core Web Vitals, Current Site Screenshots, live site fetch, competitor research (self-researched)

## Insights

No two surfaces on this site agree on how trusted it is. The homepage hero shows "4.9 (12k+ reviews)," the trust strip below it claims "2M+ Boxes Delivered," a section further down says "Trusted by 500k+ Happy Customers," the collection page's Trustpilot badge shows "3k+ reviews... 11,388 happy customers," Meta landing pages cite "13,000 reviews," and the Google ad snippet shows "3.9 ★ (966)" — Source: site-visual-summary.md, meta-ads-visual-summary.md, google-ads-visual-summary.md. Five numbers, same visual weight, zero reconciliation. That inconsistency is the single most evidence-backed issue in this audit, touching four independent sources.

Ad 2 makes it worse in a specific, fixable way. The ad headline promises "Code applied automatically. No code. No fuss." The landing page it sends traffic to shows a green "ADD TO CART — $39.97" button at full price, with the real discount buried in a dashed callout box requiring the shopper to manually enter MYBOX35 — Source: meta-ads-visual-summary.md. That is a direct contradiction of the ad's central promise, on the exact page paid traffic lands on.

Performance failure compounds the problem on a different page. The Magnetic Energy Talisman PDP, the direct click destination for Meta Ad 3, scores 0.13 on Lighthouse mobile Performance with a 13.3s LCP, 0.897 CLS, and 48.3s TTI, against a moderate 0.63 on the homepage — Source: pagespeed.md. A CLS of 0.897 is nearly four times Google's "poor" threshold of 0.25. Paid traffic is landing on the single worst-performing page measured, and the buy box is effectively unusable during most of the load window on mobile.

Offer confusion runs in parallel. LABOR35, SPRING35, MYBOX35, an unlabeled 35% code, and a separate "50% OFF + FREE GIFT" banner are all live at once across Google and Meta, with no single consistent discount a shopper can trust — Source: google-ads-visual-summary.md, meta-ads-visual-summary.md. Mindful Souls' $25.99-$39.97 entry price already undercuts competitor Goddess Provisions' $55 stated price; that advantage is being diluted by code stacking rather than protected.

Sessions/mo and AOV were not provided for this pass, so a blended revenue estimate can't be shown here. Each slot below states its own math where the seed supports it, and flags where it doesn't.

## Slot 1: Fix PDP Core Web Vitals on the Talisman Landing Page

**Type:** Immediate Fix
**Page:** Magnetic Energy Talisman PDP / Meta Ad 3 landing page (mindfulsouls.com/products/magical-energy-talisman)

This page scores 0.13 Performance on Lighthouse mobile, with LCP 13.3s, CLS 0.897, TBT 730ms, and TTI 48.3s (fetched 2026-09-01) — Source: pagespeed.md. A CLS this severe means images, price, and buy-box elements are visibly jumping as they load. TTI of 48.3s means the page is not reliably interactive for most of the load window. This is the direct click destination for Meta Ad 3's paid traffic, so every dollar spent on that ad is currently landing on a page most mobile visitors can't use in time to buy. Fix load-blocking assets, image sizing, and layout-shift sources on this template before running any A/B test on its buy box or trust signals — a winning variation can't be measured accurately against a page this unstable.

## Slot 2: Fix Ad 2's Broken "No Code" Promise

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 2 landing page, subscription box
**Revenue potential:** Not calculable. Sessions/mo and AOV were not provided for this landing page.

**Hypothesis:** If the landing page auto-applies the MYBOX35 discount and shows the $25.99 price on the main CTA button, checkout starts from this ad will increase because the page will match the promise that earned the click instead of contradicting it.

**Data:** Ad 2's headline reads "Code applied automatically. No code. No fuss," but the landing page shows a green "ADD TO CART — $39.97" button at full price, with the actual $25.99 discount buried in a separate dashed-border callout requiring the shopper to manually copy and enter MYBOX35. Source: meta-ads-visual-summary.md (Ad 2, LP Fold 1).

**V1:** Auto-apply the MYBOX35 discount at page load so no code entry is required, and update the main CTA button to read "ADD TO CART — $25.99" (with $39.97 shown struck through), removing the separate dashed callout box now that the discount is reflected in the primary button. Mobile: sticky CTA bar shows the same struck-through pricing. Desktop: same treatment in the main buy box, above the fold.

## Slot 3: Unify the Trust Number Shown Site-Wide

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (mindfulsouls.com/)
**Revenue potential:** Not calculable. Sessions/mo not provided; four-source evidence strength makes this a top-priority theme regardless.

**Hypothesis:** If the homepage shows one consistent, verified trust number instead of three different ones in the first three folds, visitor trust in the storefront will increase because shoppers won't see conflicting claims with equal visual weight.

**Data:** The homepage hero shows "4.9 (12k+ reviews)," the trust-icon strip below it shows "2M+ Boxes Delivered," and a further section shows "Trusted by 500k+ Happy Customers" — three different numbers in three folds of the same page. The collection page's Trustpilot badge separately shows "3k+ reviews... 11,388 happy customers." Source: site-visual-summary.md (homepage, collection).

**V1:** Replace the hero's "12k+ reviews," the trust strip's "2M+ Boxes Delivered," and the "500k+ Happy Customers" line with a single verified figure, matched to the Trustpilot badge already used on the collection page ("3k+ reviews... 11,388 happy customers"), repeated identically in all three homepage placements. Mobile: same single figure in the hero and trust strip, stacked. Desktop: same figure in all three original locations.

## Slot 4: Consolidate the Homepage Discount Code Messaging

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (mindfulsouls.com/)
**Revenue potential:** Not calculable. Sessions/mo not provided; seed data supports this as a strategic/ops fix as much as a CRO test.

**Hypothesis:** If the homepage shows one discount code once, instead of repeating it three times alongside other live codes elsewhere in the funnel, shoppers will trust the offer more because they won't need to reconcile conflicting savings claims before checking out.

**Data:** The code LABOR35 is repeated three times within the homepage's first fold alone (announcement bar, headline, subhead), while Meta and Google ads simultaneously run SPRING35, MYBOX35, an unlabeled 35% code, and a separate "50% OFF + FREE GIFT" banner. Source: site-visual-summary.md, google-ads-visual-summary.md, meta-ads-visual-summary.md.

**V1:** Show LABOR35 once in the announcement bar only, removing the repeated headline and subhead mentions of the same code on the homepage. Mobile: single code in the sticky announcement bar. Desktop: same single placement, code removed from the hero headline and subhead.

## Slot 5: Add Guarantee Copy to the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (slide-out drawer)
**Revenue potential:** Not calculable. Sessions/mo not provided.

**Hypothesis:** If the cart drawer shows the 30-day money-back guarantee above the checkout button, checkout-initiation rate will increase because shoppers get risk-reversal reassurance at the exact point they decide to proceed.

**Data:** The cart drawer's only reassurance line is "Have a discount code? Add it at checkout." No guarantee badge, returns copy, or shipping reassurance appears before the "SECURE CHECKOUT" button, despite the homepage and Meta landing pages both featuring a 30-day money-back guarantee prominently. Source: site-visual-summary.md (Cart Drawer).

**V1:** Add a one-line guarantee badge ("30-Day Money-Back Guarantee") directly above the "SECURE CHECKOUT" button, below the existing discount-code line. Mobile: badge sits full-width above the checkout button in the drawer. Desktop: same placement, same drawer layout.

## Slot 6: Strengthen Trust Signals on the Talisman Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** Magnetic Energy Talisman PDP / Meta Ad 3 landing page
**Revenue potential:** Not calculable. Second priority behind the Core Web Vitals fix on the same page (Slot 1) — sequence this test after the performance fix ships.

**Hypothesis:** If this page shows a review count and a trust-icon strip near the CTA, matching the trust stack already used on the subscription-box landing pages, click-to-cart rate will increase because shoppers get the same reassurance they see elsewhere on the site.

**Data:** This landing page shows one customer review card ("Sidney L.," 5 stars) and a Trustpilot "Excellent" badge in its first two folds, no review count, and no guarantee or shipping-threshold copy near the CTA. The subscription-box landing pages (Ad 1, Ad 2) show review counts, star ratings, and 4-icon trust strips by comparison. Source: meta-ads-visual-summary.md (Ad 3 folds, contrasted with Ad 1/Ad 2).

**V1:** Add a review count next to the existing star rating and Trustpilot badge, and add a 4-icon trust strip (guarantee, shipping, cancel/return terms, as used on the homepage) directly above the CTA button. Mobile: trust strip sits in the sticky CTA bar. Desktop: trust strip sits directly beneath the buy box.

## Slot 7: Weight Review Display by Sample Size on the Collection Grid

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page (product grid)
**Revenue potential:** Not calculable. Single-source evidence; lower priority than Slots 1-6.

**Hypothesis:** If product cards show the actual review count and scale the star-rating treatment by that count, shoppers will trust the grid's ratings more overall, because a product with 12 reviews won't visually claim the same authority as one with 886.

**Data:** On the collection grid, every card shows identical full-size 5-star iconography regardless of review count. The Manifestation Guidebook (12 reviews) and the Magnetic Energy Talisman (886 reviews) render with the same visual weight. Source: site-visual-summary.md (Collection Fold 2).

**V1:** Show the review count directly beside the star icons on every card, and reduce the star icon size/opacity for products under a fixed review-count threshold. Mobile: same treatment in the single/double-column grid. Desktop: same treatment in the 4-column grid.

## Slot 8: Build Matching Landing Pages for Google's SKU Catalog

**Type:** Custom landing pages (1 slot)

**Why this is the priority:** Google Ads Transparency Center shows 25+ ad units promoting individual jewelry and crystal SKUs (rings, phone cases, water bottles, pendulums, incense) across five regional entities, none of which are represented in the Meta creative set or the three landing pages collected. This traffic's landing experience is currently unverified, and the discount-code fragmentation already documented (Slot 4) is worse on Google, with LABOR35, SPRING35, an unlabeled 35% code, and a "50% OFF + FREE GIFT" banner all live. Source: google-ads-visual-summary.md.

**What we're building:** Dedicated landing pages, or a verified matching PDP experience, for the individual SKUs actively advertised on Google, so each ad's claimed product, price, and discount code is reflected on the page it sends traffic to.

**Key requirements:**
- Audit each live Google ad's claimed SKU, price, and discount code against its current landing destination
- Build or verify one landing page per SKU group that reflects the ad's specific claims
- Apply the same discount-code consolidation approach used in Slot 4 to Google-specific offers

**Success metrics:**
- Message-match rate (ad claim vs. landing page) across sampled Google SKU ads
- Bounce rate on Google Ads landing traffic

## Future Slot Candidates

1. **Reconcile the Google star-rating snippet with on-site figures** - Google's ad snippet shows 3.9/966, well below the 4.9/12k-13k figures used elsewhere on the site. This may reflect a stale Google Business/Merchant listing rather than a page-level fix, worth a client conversation before scoping as a CRO test. Source: google-ads-visual-summary.md.
2. **Dedicated PDP screenshot pass for the "Buy 1 Get 1 50% OFF" bundle option** - The live PDP fetch surfaces a bundle offer not visible in the three screenshotted folds, suggesting more buy-box structure than currently documented. A screenshot pass is needed before this can be scoped as a test. Source: live PDP fetch.
