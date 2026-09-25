# Oneshotminer CRO Research Brief

**Data Sources:** Current Site Screenshots (homepage, collection, PDP, cart), PageSpeed / Core Web Vitals, Reviews & UGC

The PDP is actively blocking conversion before any messaging or layout fix can matter. Mobile LCP on the product page is 22.0s and TTI is 22.1s, against 4.5s LCP and 16.8s TTI on the homepage (PageSpeed / Core Web Vitals, September 8 2026 collection). That gap means the buy box, variant selector, and Add to Cart button on the store's only conversion page are likely non-interactive well past the point most mobile visitors abandon. Every other PDP finding in this brief is downstream of this one.

Trust signals sit on the wrong page. The homepage opens with a "BANKRUPT SALE | ENDS WHEN STOCK RUNS OUT" banner and shows no reviews, ratings, or guarantee badges across its first three folds, while the PDP carries a "★★★★★ (1420+ reviews)" line directly above its buy box. This gap matters more than usual here: Trustpilot reviews (November 2025 to May 2026) show a sharp bimodal split, where nearly every 1-star review centers on broken refund or cancellation promises ("keep you talking exactly long enough so that you miss the refund date") while 5-star reviews cluster around smooth delivery and a working product. An audience already primed by public reviews to read inconsistency as manipulation is more sensitive than most to small credibility gaps elsewhere on-site: a footer link labels the flagship product "(2025 Edition)" while the PDP and homepage both call it "(2026 Edition)," and collection-page discount badges vary 40% to 72% across near-identical hardware tiers with no visible reason.

The strongest, most specific proof point on the site is a testimonial referencing a named $373,000 solo-mining win with a specific date. It sits in PDP fold 3, below where the 22.1s TTI suggests most mobile visitors have already disengaged.

No sessions/mo, AOV, or baseline conversion rate was collected for this brand, so every lift estimate below is directional only. A dollar figure can't be attached until traffic and AOV data are supplied.

---

## Slot 1: Fix PDP Page Speed (LCP/TTI)

**Type:** Immediate Fix
**Page:** Product Detail Page (https://oneshotminer.com/products/one-shot-pro-edition/)

**What's broken:** Mobile LCP is 22.0s and TTI is 22.1s on the PDP, versus 4.5s LCP and 16.8s TTI on the homepage. Performance score is 63/100 on the PDP versus 79/100 on the homepage. The buy box (product image, variant selector, bundle tiers, Add to Cart) sits in fold 1 and is unlikely to be fully rendered or interactive before most mobile visitors leave.

**Data:** PageSpeed / Core Web Vitals, mobile, collected September 8 2026.

**Fix:** Diagnose and cut PDP load time toward the homepage's own 4.5s LCP baseline before running any other PDP test. Likely candidates given the score gap: unoptimized hero product image, render-blocking scripts tied to the buy box (variant selector, bundle tier widget), or app/theme bloat specific to the product template. This is not testable as an A/B test since a non-rendering page has no valid control.

---

## Slot 2: Add Review Trust Signal Above the Homepage Fold

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://oneshotminer.com/)
**Revenue potential:** Sessions/mo (unknown) x 5-10% conservative CR lift x AOV (unknown) = undetermined pending traffic and AOV data.

**Hypothesis:** If we add the "★★★★★ (1420+ reviews)" line near the hero headline, more visitors will continue into the product grid instead of bouncing, because early trust proof counters the "BANKRUPT SALE" urgency framing that currently opens the page with no supporting credibility.

**Data:** The homepage shows zero star ratings, review counts, or guarantee badges across its first three folds, opening instead with a "BANKRUPT SALE | ENDS WHEN STOCK RUNS OUT" banner (site screenshots, live homepage fetch). The PDP carries a "★★★★★ (1420+ reviews)" line directly above its buy box, an identical asset the homepage doesn't use (site screenshots).

**V1:** Add the "★★★★★ (1420+ reviews)" line directly beneath the hero headline, above the "CHOOSE YOUR MINER" CTA. Hero headline, BTC-reward copy, and CTA stay unchanged. Mobile: stack the trust line as its own row between headline and CTA so it doesn't compress tap target size. Desktop: place it inline beneath the headline at the same width as the CTA.

---

## Slot 3: Move Named Social Proof Above the PDP Fold

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (https://oneshotminer.com/products/one-shot-pro-edition/)
**Revenue potential:** Sessions/mo (unknown) x 3-6% conservative CR lift x AOV (unknown) = undetermined pending traffic and AOV data.

**Hypothesis:** If we surface the "$373,000 solo miner win" testimonial in fold 1 near the buy box instead of fold 3, more mobile visitors will see the strongest proof point on the page before they disengage, because a 22.1s TTI means most never reach fold 3.

**Data:** The PDP's most concrete proof point, a testimonial naming a $373,000 solo-mining win on a specific date (July 26 2025), currently sits in fold 3 (site screenshots). PDP TTI is 22.1s, well past typical mobile engagement drop-off (PageSpeed / Core Web Vitals).

**V1:** Add a condensed version of the testimonial (the dollar figure and date, one line) as a callout directly beside or below the buy box in fold 1, near the existing "★★★★★ (1420+ reviews)" line. Leave the full fold-3 testimonial section in place for visitors who scroll. Mobile: place the condensed callout as a single line under the price, above the variant selector. Desktop: place it in the right column beneath the "1420+ reviews" line, above the bundle tiers.

---

## Slot 4: Show Per-Unit Price on PDP Bundle Tiers

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (https://oneshotminer.com/products/one-shot-pro-edition/)
**Revenue potential:** Sessions/mo (unknown) x 2-4% conservative AOV lift x AOV (unknown) = undetermined pending traffic and AOV data.

**Hypothesis:** If we show a per-unit price under each of the three bundle tiers, more shoppers will choose the pre-selected "Best value" tier, because the savings claim becomes visible math instead of a badge claim they have to take on faith. (KB: resources/kb/cold-friendly-offer-positioning.md)

**Data:** The buy box offers three tiers, Buy 1 ($59.99), Buy 2 ($119.98, free shipping), Buy 3 & get 1 Free ($179.97), with the third tier pre-selected and labeled "Best value," but no per-unit price is shown across tiers to substantiate that label (site screenshots, PDP buy box detail).

**V1:** Add a small per-unit price line under each tier's total price, calculated from the existing listed prices: $59.99/unit on Buy 1, $59.99/unit on Buy 2, $44.99/unit on Buy 3 & get 1 Free. Tier layout, pre-selection, and "Best value" label stay unchanged. Mobile: per-unit line sits directly under each tier's price in smaller type. Desktop: same placement, aligned across all three tier cards.

---

## Slot 5: Standardize Discount Logic on Collection Page

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page (https://oneshotminer.com/collections/all or equivalent)
**Revenue potential:** Sessions/mo (unknown) x 2-4% conservative CR lift x AOV (unknown) = undetermined pending traffic and AOV data.

**Hypothesis:** If we replace the collection page's unexplained 40-72% discount spread with one consistent discount logic tied to bundle size, shoppers will trust the pricing more and convert at a higher rate, because reviews show this audience is already primed to read pricing inconsistency as manipulation. (KB: resources/kb/pdp-structure.md)

**Data:** Collection page "SAVE X%" badges vary 40%, 70%, 65%, 67%, and 72% across near-identical hardware tiers with no visible basis (site screenshots). Trustpilot reviews from the same period repeatedly use "scam" and describe deliberately confusing pricing and refund practices, raising the cost of any unexplained inconsistency on-site.

**V1:** Apply one consistent discount logic across all 9 collection products, tied to the same tier structure already used in the PDP buy box (quantity/bundle size), so every badge reflects an explainable reason rather than a per-product number. Mobile and desktop: same badge position and styling, updated percentages only.

---

## Slot 6: Fix Version-Label Mismatch

**Type:** Immediate Fix
**Page:** Collection page footer / Product Detail Page

**What's broken:** The collection page footer's Menu section links to "One Shot Miner PRO (2025 Edition)," while the homepage and PDP both title the same product "(2026 Edition)."

**Data:** Site screenshots, collection page footer versus PDP and homepage titles.

**Fix:** Update the footer link text to "(2026 Edition)" to match the live product title. A small inconsistency, but a visible one in a store already facing scam accusations in public reviews.

---

## Slot 7: Add Security and Return Copy to Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer
**Revenue potential:** Sessions/mo (unknown) x 1-3% conservative checkout completion lift x AOV (unknown) = undetermined pending traffic and AOV data.

**Hypothesis:** If we add payment/security icons and a return-policy link inside the cart drawer, checkout completion will increase, because shoppers currently lose the PDP-level trust cues right at the step where they commit to paying.

**Data:** The cart drawer shows a "24/7 Support - Lifetime Warranty" banner and a "Last units left" urgency banner sandwiching the checkout button, but no payment/security icons or return-policy link, while the PDP shows payment icons directly under Add to Cart (site screenshots).

**V1:** Add a payment icon row (matching the PDP's existing icon set) and a return-policy link directly above the checkout button. Keep the existing warranty and urgency banners and upsell cards unchanged. Mobile: icons and link sit as one compact row above the button. Desktop: same row, full width of the drawer.

---

## Slot 8: De-Duplicate Homepage Product Grid Badge Copy

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://oneshotminer.com/)
**Revenue potential:** Sessions/mo (unknown) x 1-2% conservative CR lift x AOV (unknown) = undetermined pending traffic and AOV data.

**Hypothesis:** If each of the 10 homepage product cards carries its own distinguishing line instead of identical overlay text, shoppers will differentiate between models faster and disengage less from the grid.

**Data:** All 10 product cards in the homepage grid carry the identical overlay text "Join the race of solo mining 3.125 BTC by yourself," regardless of which of the 6+ distinct miner models is shown (site screenshots, homepage folds 1-2).

**V1:** Replace the repeated overlay text on each card with a short, product-specific line drawn from that product's own title/spec already shown on the card. Card layout, image, and pricing stay unchanged. Mobile and desktop: same overlay position and styling, text varies per card.

---

## Future Slot Candidates

No additional findings met the data support, revenue potential, and actionability bar for this list. The two remaining unused findings, repeated single-point-of-contact support ("Mia" named in 3+ negative reviews) and the stated 1-hour cancellation policy being cited as violated, are operational and policy-enforcement issues outside CRO scope, worth flagging to the client directly rather than testing.
