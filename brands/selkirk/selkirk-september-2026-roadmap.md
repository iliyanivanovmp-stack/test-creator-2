# Selkirk CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed / Core Web Vitals, Non-Data Context, Current Site Screenshots, Social & Community Research (last30days-ecom)

The homepage's single hero CTA, "Buy Now," routes every visitor to a 3-SKU, bags-only collection page with zero paddles on it. Paddles are Selkirk's core product. The client flagged this directly, and independent screenshot capture of both the homepage and the destination collection page confirms it. A visitor has to scroll past two full homepage folds before reaching a paddle-specific entry point. This is the single highest-confidence, highest-funnel-position issue in the audit: the core product category is effectively unreachable from the site's main entry point.

Paid traffic carries its own message-match problem. All three captured Meta ads promise something the landing page doesn't deliver. Ad 1 promises "deals" and "markdowns," but its landing page shows the paddle at full price with no discount indicator anywhere in the captured folds. Ad 2 shows "$130.00" with a "Shop Now" CTA; the landing page lists "$100.99" and the buy button is disabled, reading "Out of stock." Ad 3 opens with a 5-star testimonial about paddle quality to sell a $7 grip towel, and the towel's own landing page shows a 2-star "I do not recommend this product" review directly below the fold. Every dollar spent on these three campaigns is currently landing on a page that contradicts the ad that earned the click.

Mobile performance compounds both problems. Lighthouse mobile data from 2026-09-10 shows homepage LCP at 12.0s and Project Boomstik PDP LCP at 9.9s, roughly 4-5x Google's 2.5s "good" threshold, with Time to Interactive exceeding 12 seconds on both templates (Source: PageSpeed / Core Web Vitals). This is a tax on every visitor, paid or organic, regardless of which page they land on first.

Customer sentiment is a bright spot with one caveat. Reviews describe strong value at the entry tier ("excellent value... made the game much more enjoyable," Source: Reviews & UGC) and this is corroborated by broader Amazon paddle-line ratings in the 4.4-4.5 star range (Source: Social & Community Research). The caveat: one reviewer called the entry-tier material "low par," planning to upgrade "once these fall apart," and two independent sources, Trustpilot and the Boomstik PDP's own "Exchanges are unavailable" copy, point at unresolved warranty and exchange friction (Source: Social & Community Research).

No sessions/mo or AOV figures exist in any collected source. Revenue potential below is stated qualitatively by funnel position and evidence strength rather than as a dollar estimate, since inventing a number would not be grounded in the data collected.

---

## Slot 1: Fix Homepage Hero CTA Routing

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (selkirk.com)
**Revenue potential:** Sessions/mo and AOV were not collected (see Missing Data), so a dollar estimate cannot be calculated. This is the highest-funnel-position finding in the audit: the primary homepage CTA currently blocks access to the brand's core product category for every visitor who clicks it.

**Hypothesis:** If the hero's "Buy Now" CTA routes to a paddles or general-shop destination instead of the bags-only collection, paddle-category entry rate from the homepage will increase because the core product is currently unreachable from the main CTA.

**Data:** The hero banner ("THESE BAGS KNOW BALL / PRO LINE 2.0 BAG SERIES") carries one "Buy Now" button that routes to a confirmed 3-SKU, bags-only collection (Tour Backpack $298, Team Backpack $248, Duffle $198) with no paddles, apparel, or other product types on it. This is client-flagged and independently confirmed by both the homepage and collection screenshots. Source: Non-Data Context, Current Site Screenshots.

**V1:** Change the hero "Buy Now" button destination from the Pro Line 2.0 Bags collection to the Paddles collection (or a mixed best-seller collection that includes paddles). Hero imagery and headline stay as-is; only the CTA link target changes. Desktop: same hero layout, updated link. Mobile: same single-column hero, button remains in the same thumb-reachable position with the updated destination.

---

## Slot 2: Recover Out-of-Stock Ad Traffic on Vanguard Power Air

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 2 Landing Page, Vanguard Power Air - S2 PDP
**Revenue potential:** Sessions/mo and AOV were not collected. Priority is driven by the fact that this is live, paid traffic hitting a disabled buy button on arrival, a dead end at the exact page paid spend is sending people to.

**Hypothesis:** If the out-of-stock buy box shows an active recovery path (comparable in-stock paddles) instead of only a passive "Notify me" option, fewer visitors arriving from Ad 2 will leave without adding anything to cart.

**Data:** Meta Ad 2 shows "$130.00" with a "Shop Now" CTA implying live purchase. The landing page lists "$100.99" and the primary buy button is disabled, reading "Out of stock," with only "Notify me when back in stock" active. Source: meta-ads-visual-summary (Ad 2).

**V1:** Below the disabled "Notify me" button, add a "Shop similar in-stock paddles" module showing 2-3 comparable in-stock SKUs. Also sync the displayed price to whatever price the live ad is showing so the two match. Desktop: module sits directly under the CTA in the buy box column. Mobile: module appears as a horizontal scroll row directly below the disabled button, visible without added scrolling.

---

## Slot 3: Match "Deals" Ad Copy to Landing Page Reality on AMPED Pro Air

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 1 Landing Page, AMPED Pro Air - Epic PDP
**Revenue potential:** Sessions/mo and AOV were not collected. Priority is driven by direct message-match failure on live paid traffic.

**Hypothesis:** If the "Free Gift With Purchase" badge is reframed to explicitly state the deal's value, visitors arriving expecting "deals" and "markdowns" will see a concrete match to that promise instead of a full price with no discount cue.

**Data:** Ad 1 headline promises "Deals on select Selkirk paddles... Limited quantities, so don't sleep on it." The landing page shows the paddle at $100 flat with a "Free Gift With Purchase" badge but no strikethrough price, sale badge, or discount code anywhere in the captured folds. Source: meta-ads-visual-summary (Ad 1).

**V1:** Update the existing "Free Gift With Purchase" badge copy to state the gift explicitly (e.g., "Free [Gift Name] Included") directly under the price, so the deal is visible at a glance instead of implied. No discount or price change, in line with the no-large-discount pattern for margin and perceived value (KB: resources/kb/pdp-structure.md). Desktop: badge sits directly under price in the buy box. Mobile: same badge, same position, no layout change.

---

## Slot 4: Reduce Mobile Load Time on Homepage and PDP

**Type:** Immediate Fix
**Page:** Homepage and PDP (Project Boomstik)

Lighthouse mobile data from 2026-09-10 shows Performance 64/100 on the homepage (LCP 12.0s, TTI 12.6s) and Performance 63/100 on the Boomstik PDP (LCP 9.9s, TTI 13.5s), both roughly 4-5x Google's 2.5s "good" LCP threshold. Source: pagespeed.md. This is not a hypothesis to test, it is a load-time failure affecting 100 percent of mobile traffic on both templates regardless of entry point or segment. Recommend a direct technical fix (hero and product image compression, deferring render-blocking scripts) rather than an A/B test.

---

## Slot 5: Re-pair Towel Ad's Testimonial With Matching Reviews

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 3 Landing Page, Tacky Grip Towel PDP

**Revenue potential:** Sessions/mo and AOV were not collected. Priority is driven by a direct trust contradiction visible within one scroll of the ad click.

**Hypothesis:** If the towel's landing page defaults to showing its highest-rated reviews first, visitors arriving on Ad 3's 5-star testimonial framing will not immediately see the 2-star and 3-star reviews currently visible below the fold, closing the trust gap between the ad's promise and the page's first impression.

**Data:** Ad 3 opens with a 5-star testimonial about paddle quality and service to promote a $7 grip towel. Directly below the fold on the towel's own landing page, the first visible reviews are a 2-star "I do not recommend this product" review and a 3-star durability complaint. Source: meta-ads-visual-summary (Ad 3).

**V1:** Change the default review sort on the towel PDP to highest-rating-first, with all reviews still accessible via a "see all reviews" toggle. Ad 3's creative is unchanged; only the landing page's default review order updates. Desktop: review list re-sorts under the existing review section. Mobile: same default sort, reviews stack vertically in the same section.

---

## Slot 6: Pair Cart Shipping-Delay Warning With a Trust Signal

**Type:** A/B test (1 variation vs. control)
**Page:** Cart

**Revenue potential:** Sessions/mo and AOV were not collected. Priority is driven by funnel position: this sits directly before checkout with no offsetting trust copy anywhere in the drawer.

**Hypothesis:** If a guarantee or returns badge sits directly beneath the existing shipping-delay warning, cart abandonment triggered by the unmitigated warning will decrease because shoppers see reassurance alongside the friction notice.

**Data:** The cart drawer opens with a red banner: "Some items in your cart have a shipping delay & will delay your entire order. Please place two separate orders if you would like your other items sooner." No guarantee, returns copy, or trust badge appears elsewhere in the drawer. Source: site-visual-summary (cart).

**V1:** Add a single trust-badge line (e.g., "30-Day Guarantee") directly beneath the red shipping-delay banner, without removing or softening the warning's existing copy. Desktop: badge row appears as an inline strip below the banner, above the cart line items. Mobile: same badge row, full width, directly under the banner before the line items.

---

## Slot 7: Reframe "Ships in 2-3 Weeks" Note on Boomstik PDP

**Type:** A/B test (1 variation vs. control)
**Page:** PDP, Project Boomstik ($333)

**Revenue potential:** Sessions/mo and AOV were not collected. Priority is driven by this note sitting on the flagship product receiving the heaviest Google Ads emphasis.

**Hypothesis:** If the bare red "Ships in 2-3 weeks" note is reframed with a reason and an estimated delivery date, checkout intent on the $333 flagship paddle will hold steadier because the delay reads as intentional craftsmanship rather than a fulfillment problem.

**Data:** The Boomstik PDP shows a red "Ships in 2-3 weeks" note directly above the Add to Cart button, on the product receiving the heaviest Google Ads emphasis (Boomstik-focused search/Shopping ads). Source: site-visual-summary (PDP), google-ads-visual-summary (Boomstik emphasis).

**V1:** Replace the bare red "Ships in 2-3 weeks" text with a neutral-toned line that pairs a reason with an estimated delivery date, for example "Made to order, ships in 2-3 weeks, arrives by [date]," in the same position above Add to Cart. Desktop: single-line note directly above the CTA. Mobile: same copy and position, wraps to two lines if needed.

---

## Slot 8: Combine Frequently Bought Together Into One Bundle CTA

**Type:** A/B test (1 variation vs. control)
**Page:** PDP, AMPED Pro Air and Project Boomstik

**Revenue potential:** Sessions/mo and AOV were not collected. Priority is driven by this pattern repeating across the two most ad-supported PDPs.

**Hypothesis:** If the 4-item "Frequently Bought Together" row has one combined "Add all to cart" action instead of 4 separate Quick Add buttons, attach rate will increase because the current flow requires 4 separate clicks to bundle.

**Data:** Both the AMPED Pro Air and Boomstik PDPs show a 4-item "Frequently Bought Together" row (paddle cover, glove, backpack/balls), each with its own "Quick Add" button rather than one combined action. Source: meta-ads-visual-summary (Ad 1, Ad 2 LP folds), site-visual-summary (PDP fold 3).

**V1:** Add one primary "Add all to cart" button to the FBT row, with each item defaulting to checked (shoppers can deselect individual items). Keep the existing per-item Quick Add buttons as a secondary option. Desktop: combined button sits at the top-right of the FBT row. Mobile: combined button is full-width, stacked above the item thumbnails.

---

## Future Slot Candidates

1. **Add review count/star rating to the homepage** - PDPs carry 623-2,664 reviews and a 4.7-star aggregate, but none of that signal appears anywhere on the homepage in the captured folds.
2. **Surface a clearer warranty/exchange policy on PDP and cart** - Trustpilot reports of being charged shipping for a warranty assessment and the Boomstik PDP's own "Exchanges are unavailable" copy point at the same unresolved friction, with no exchange terms visible up front on PDP or cart.
