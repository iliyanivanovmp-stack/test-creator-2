# Soulffee CRO Research Brief

**Data Sources:** PageSpeed / Core Web Vitals (mobile, Jul 8 2026), site screenshots (homepage 4 folds, PDP 3 folds, cart mobile), live site fetch (homepage + PDP)

---

## Insights

The single biggest revenue opportunity on this site is structural: the PDP defaults to one-time purchase ($32.00) over Subscribe & Save ($25.92, 19% off). For a brand built around a daily ritual, this is backwards. Every visitor who buys once without subscribing represents an LTV gap that no amount of additional traffic can fix. Source: PDP-f1 screenshot, live PDP fetch.

Mobile performance compounds the problem before any visitor reaches the buy box. Homepage LCP is 10.3 seconds (score 0/1) and PDP LCP is 14.9 seconds (score 0/1) on mobile (PageSpeed, Jul 8 2026). At these load times, the majority of mobile traffic bounces before the hero renders. Every test in this roadmap runs in a degraded environment until the underlying performance issues are addressed.

Three CTA dead zones kill conversion across the funnel. The homepage hero CTA ("TRY NOW") is cut off below the fold on load. The comparison table -- the deepest homepage content, where Soulffee wins 5 of 6 attributes vs. Mushroom Coffee -- ends with no conversion action. The cart shows no path to the 60-serving variant despite it being available on the PDP. Source: homepage-f1.png, homepage-f2.png, homepage-f4.png, cart-drawer screenshot, PDP-f1 screenshot.

Social proof exists but is stranded. Thirty-eight reviews at 4.8 stars sit far below the PDP buy box -- invisible in the first 3 folds. The buy box shows a "38 reviews" link but no quote or customer voice near the purchase decision. Customers say: "Smooth and rich, without the bitterness" and "Gentle on my stomach" (live PDP fetch). At 4.8 stars the product satisfies -- the gap is surfacing proof at the moment of decision.

Monthly session data is unavailable, so revenue estimates are expressed per 1,000 sessions. The subscription default test stands apart: any OTP-to-subscription shift produces compounding LTV gains that a single-order AOV lens cannot fully capture.

---

## Slot 1: Subscribe & Save Default Selection

**Type:** A/B test (1 variation vs. control)
**Page:** PDP (https://www.soulffee.com/products/soulffee)
**Revenue potential:** Monthly sessions unknown. Per 1,000 PDP sessions: if 15-25% of purchasers shift from OTP ($32.00) to Subscribe & Save ($25.92), initial AOV decreases by $6.08 per subscriber but recurring monthly orders eliminate the need to re-acquire the customer. LTV gains are not calculable without churn data, but any subscription attach rate increase is the highest-leverage outcome available on a single-SKU store.

**Hypothesis:** If we pre-select Subscribe & Save as the default buy box option and visually distinguish it from OTP, subscription attach rate increases because the current layout requires users to opt into the highest-LTV action rather than opt out of it.

**Data:** PDP fold 1 shows two stacked radio buttons in the right buy box column. The bottom radio -- "One Time Purchase $32.00" -- is pre-selected with a filled circle indicator. Above it sits "Subscribe & Save SAVE 19% $25.92 ~~$32.00~~", unselected, with no badge, highlight, or "most popular" label. Both options carry identical visual weight. Subscription perks (free cancellation, free North American shipping, 30-day guarantee, early access) are hidden inside a collapsed "Subscription Perks +" accordion below the buy box. Source: PDP-f1 screenshot, live PDP fetch.

**V1:** Switch the default radio selection from "One Time Purchase $32.00" to "Subscribe & Save SAVE 19% $25.92". Add a "Best Value" or "Most Popular" badge inline with the Subscribe & Save label on both mobile and desktop. The OTP option remains visible and selectable but unselected on page load. The "Subscription Perks +" accordion stays in its current position. No other buy box elements change.

---

## Slot 2: Hero CTA Above the Fold

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://www.soulffee.com/)
**Revenue potential:** Monthly sessions unknown. Per 1,000 homepage sessions: a 5-10% CTR lift to the PDP = 50-100 additional PDP arrivals. Downstream purchase impact depends on PDP CVR (no analytics data available), but removing the scroll requirement on the only homepage action is the minimum viable fix.

**Hypothesis:** If we reposition the "TRY NOW" CTA button to be fully visible on page load without scrolling, homepage-to-PDP CTR increases because the current layout pushes the only clickable action below the viewport on most mobile devices.

**Data:** Homepage fold 1 shows a full-viewport hero with a left-aligned headline ("Calm Mind, Clear Focus, No Jitters"), 3-line subtext, and a star rating row. The "TRY NOW" white pill button is cut off at the bottom of fold 1 and only becomes fully visible in fold 2. A vertical sticky tab ("LIMITED SOULFFEE - UP TO 45% OFF") on the right edge and an announcement bar ("FREE shipping on all orders!") consume additional vertical space, pushing the CTA further down. No above-fold action is available on load without scrolling. Source: homepage-f1.png, homepage-f2.png.

**V1:** Reduce the vertical gap between the star rating row and the "TRY NOW" button so the button is fully visible above the fold on a 375px mobile viewport without scrolling. If needed, tighten the subtext line-height or reduce the headline font size by one step. Desktop: apply the same vertical compression to the hero section to maintain proportional layout. The announcement bar, sticky tab, headline text, subtext, and button label remain unchanged.

---

## Slot 3: 60-Serving Upgrade Prompt in Cart

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (https://www.soulffee.com/cart)
**Revenue potential:** Monthly sessions unknown. Per 1,000 cart sessions: 10-15% upgrade acceptance rate = 100-150 upgrades x ~$22 AOV lift (30-serving to 60-serving, estimated) = $2,200-$3,300 estimated lift per 1,000 cart sessions. Note: 60-serving price is an estimate from the seed; confirm before launching.

**Hypothesis:** If we surface a 60-serving upgrade prompt inside the cart, AOV increases because the 60-serving variant is available on the PDP but is never shown after a 30-serving unit is added.

**Data:** Mobile cart shows a single line item (Mushroom Orzo, 30 servings, qty 2, $32.00 each, $64.00 subtotal). Free shipping is already unlocked, shown as a full dark green progress bar with "CONGRATS YOU'VE UNLOCKED FREE SHIPPING!" The cart contains no upsell widget, product recommendation, or upgrade prompt. The 60-serving variant is confirmed in the PDP fold 1 size selector row. The announcement bar in cart reads "Save Up to 38% Today" with no corresponding discount mechanism. Source: cart-drawer screenshot, PDP-f1 screenshot.

**V1:** Add a product upgrade widget between the cart line item and the shipping estimate collapsible on both mobile and desktop. The widget displays: product image, "Upgrade to 60 Servings", estimated price, and a "Switch" button. Clicking "Switch" replaces the 30-serving line item with the 60-serving variant at the same quantity. The existing "CONGRATS YOU'VE UNLOCKED FREE SHIPPING!" bar and all other cart elements remain in place.

---

## Slot 4: Comparison Table CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://www.soulffee.com/)
**Revenue potential:** Monthly sessions unknown. Scroll-depth cohort reaching fold 4 not measurable without analytics. Estimated 3-7% CVR lift from users who complete the full homepage reading flow -- these are the highest-intent homepage visitors.

**Hypothesis:** If we add a CTA directly below the comparison table, CVR from high-scroll visitors increases because the table is currently the final homepage content with no conversion action at the natural end of the reading flow.

**Data:** Homepage fold 4 shows a two-column comparison table (Soulffee vs. Mushroom Coffee) with 6 attribute rows. Soulffee wins 5 of 6 rows. Below the last table row the page ends with no CTA, trust signal, or section break. A sticky nav is visible at the top and a sticky side tab is on the right, but neither provides a clear, contextual conversion action at this scroll depth. Source: homepage-f4.png.

**V1:** Add a CTA block directly below the comparison table's final row on both mobile and desktop. The block contains the "TRY NOW" button (same pill style and color as the hero CTA) and a single supporting line -- reuse either the subscription savings message ("Save 19% with Subscribe & Save") or the star rating line from the buy box. No new design elements. The comparison table itself is unchanged.

---

## Slot 5: Reviews Block Near Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** PDP (https://www.soulffee.com/products/soulffee)
**Revenue potential:** Monthly sessions unknown. Per 1,000 PDP sessions: 4-8% relative CVR improvement x $32.00 AOV = estimated $1.28-$2.56 additional revenue per session at whatever the baseline CVR is. Exact monthly impact requires session volume.

**Hypothesis:** If we surface 2-3 customer review snippets directly below the buy box, PDP CVR increases because the current layout buries 4.8-star reviews far below the point of purchase decision.

**Data:** PDP fold 1 shows "38 reviews" as a clickable star rating link in the buy box column. The "Why Soulffee?" accordion (open by default) contains 5 brand-authored bullet points but no customer voice. The reviews section does not appear in PDP folds 1, 2, or 3 -- only below significant scroll. Live site fetch confirms review samples: "Smooth and rich, without the bitterness"; "Gentle on my stomach". Average rating: 4.8/5, 38 reviews. Top themes: taste, smooth energy, stomach-friendly. Source: PDP-f1, PDP-f2, PDP-f3 screenshots, live PDP fetch.

**V1:** Insert a 2-3 review snippet block directly below the "TRY IT NOW" button in the buy box on both mobile and desktop. Each snippet shows: 5-star icon row, reviewer first name, one-sentence quote. Select snippets covering the top 3 themes (taste, smooth energy, stomach-friendly). The full review section remains in its original position below. The "Why Soulffee?" accordion and all other buy box elements are unchanged.

---

## Future Slot Candidates

1. **Mobile performance sprint** - Homepage LCP 10.3s and PDP LCP 14.9s (both score 0/1, Jul 8 2026) will suppress baseline CVR across all tests; image optimization and JS deferral should run before or in parallel with the testing program.
2. **"Save Up to 38% Today" cart bar** - The announcement bar promises a discount with no corresponding cart-level mechanism; removing or replacing the copy eliminates a broken promise at the final conversion step.
3. **Homepage review count** - The homepage shows "4.8+ stars" with no review count; replacing with "4.8 stars, 38 reviews" converts a vague claim into a verifiable signal.
4. **Product naming alignment** - URL slug /products/soulffee vs. in-page title "Mushroom Orzo" may suppress branded search CTR and creates a trust gap at the URL level.
