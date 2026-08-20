# Instant Hydration CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed / Core Web Vitals, Current Site Screenshots

## Insights

The biggest problem is message match, and it breaks in three places at once. The homepage hero CTA, "GET UP TO 50% OFF," links to /products/premium-electrolyte-drink-mix, a different product than the ICEE card sitting directly below it in fold 2, and different from the ICEE product nearly all Meta ads land on. A visitor who clicks the hero button ends up somewhere the rest of the page never mentioned.

The mismatch continues on the page that actually receives the paid traffic. All three active Meta ads use the identical offer line, "Try Risk Free for 50 Days + FREE GIFT," but that exact phrase isn't in the landing page's above-the-fold buy box — only "50 Day Happiness Guarantee" appears there, one fold down (Source: Meta ads, live landing page fetch). Google Ads adds a third, inconsistent layer: roughly 30 ad units running 35-55% off messaging that doesn't match Meta's risk-free framing at all (Source: Google Ads Transparency).

That same landing page is also the site's worst performer technically. Mobile PageSpeed scores it at 36/100 with a 7.0s LCP and a 0.546 CLS, more than double the "poor" threshold of 0.25, versus the homepage's 60/100 score and CLS of 0 (Source: PageSpeed, Aug 2026). The CLS points to visible shifting in the buy box or pricing table exactly when a paid visitor is deciding whether to buy.

Customer feedback surfaces a separate, product-level issue. Across 45 reviews spanning 1 to 5 stars, saltiness is the most repeated complaint: "tasted like straight salt water" (1-star), "Tastes like the ocean" (2-star), and even 4 and 5-star reviewers report needing to double or triple the recommended water ratio (Source: Reviews & UGC). No page captured in this audit, landing page, homepage, or collection, offers dilution guidance.

Sessions and AOV data weren't available for this account, so revenue estimates below are conservative CR lift ranges, not dollarized. The two highest-confidence fixes, offer message match and Core Web Vitals, both sit on the page carrying nearly all paid traffic, making them the highest-leverage starting point regardless of exact volume.

## Slot 1: Fix Homepage Hero CTA Product Mismatch

**Type:** Immediate Fix

The homepage hero (fold 1) shows a green pill CTA reading "GET UP TO 50% OFF" that links to /products/premium-electrolyte-drink-mix. Directly below it in fold 2, under the headline "Hydration Starts Here," two cards read "ICEE x Instant Hydration" and "Shop Electrolytes." The hero CTA's destination matches neither card, and doesn't match the ICEE product that nearly all paid ad traffic lands on (Source: site-visual-summary.md, homepage fold 1 URL overlay).

**Fix:** Point the hero CTA to the ICEE product page (or to whichever product the current promo is actually running on), so the destination matches the ICEE card immediately below it and the product paid traffic already expects. Mobile and desktop: same link change, no layout change required.

## Slot 2: Surface the Ad's Exact Offer Above the Fold on the ICEE Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** ICEE Landing Page / PDP (instanthydration.com/products/icee-electrolyte-drink-mix)
**Revenue potential:** Sessions/mo and AOV not provided in collected data. Conservative CR lift on paid landing traffic: 0.5-1.5%.

**Hypothesis:** If we restate the ad's exact offer phrase, "Try Risk Free for 50 Days + FREE GIFT," inside the above-the-fold buy box, conversion rate on paid traffic will increase because visitors will see the promise that brought them to the page confirmed immediately, instead of having to scroll to find it.

**Data:** All three active Meta ads use the identical offer line "Try Risk Free for 50 Days + FREE GIFT." The landing page buy box (fold 1) shows only "50 Day Happiness Guarantee," with the exact ad phrase appearing one fold down under the CTA, not inside the buy box a visitor from the ad first sees (Source: Meta ads, live landing page fetch).

**V1:** Add a single line directly under the pricing table in the buy box that restates the ad's exact phrase, "Try Risk Free for 50 Days + FREE GIFT," matching the ad copy verbatim. No other buy box elements change. Mobile: line sits below the 3-tier pricing table, above the "SELECT FROM 14 FLAVORS" CTA. Desktop: same placement, buy box column.

## Slot 3: Fix Core Web Vitals on the ICEE Landing Page

**Type:** Immediate Fix

Mobile Lighthouse on the ICEE landing page scores 36/100, with LCP at 7.0s and CLS at 0.546, more than double the 0.25 "poor" threshold. The homepage, by comparison, scores 60/100 with CLS of 0 (Source: PageSpeed, Aug 2026). The CLS score indicates visible layout shift, likely in the buy box, pricing table, or comparison table as the page loads, on the exact page nearly all paid traffic lands on.

**Fix:** Reserve fixed space (width/height or aspect-ratio) for the buy box, pricing table, and comparison table elements so they don't shift as content loads, and address the LCP element (likely the hero image or buy box) with proper preload/sizing. This is a technical fix, not a design hypothesis, do not A/B test it.

## Slot 4: Add Pricing to Collection Page Product Cards

**Type:** A/B test (1 variation vs. control)
**Page:** Collection / Category ("Top Rated Electrolytes")
**Revenue potential:** Sessions/mo and AOV not provided in collected data. Conservative collection-to-PDP click-through lift: 1-2%.

**Hypothesis:** If we add price to each product card on the collection page, click-through to product pages will increase because shoppers can compare offers without clicking into each product individually.

**Data:** Both captured collection folds show a 3-column grid of 6 products (Premium Electrolyte Drink Mix, LUIGI'S Lemon Italian Ice, ICEE Blue Raspberry & Cherry, Electrolyte Variety Pack 30ct/12ct, MVP Bundle). None of the 6 cards show a price, compare-at price, or per-unit cost in either fold (Source: site-visual-summary.md, collection page).

**V1:** Add price (and compare-at price where a discount applies) below the product title on every card. Mobile: price sits directly under the title, above the badge if one exists, in the existing card layout. Desktop: same placement, 3-column grid unchanged.

## Slot 5: Address "Too Salty" Perception on the Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** ICEE Landing Page / PDP (instanthydration.com/products/icee-electrolyte-drink-mix)
**Revenue potential:** Sessions/mo and AOV not provided in collected data. Conservative CR lift: 0.5-1%; primary value is reducing post-purchase 1-star reviews.

**Hypothesis:** If we add serving/dilution guidance near the ingredient benefit section, perceived value will increase and post-purchase dissatisfaction will decrease because customers will know upfront how to adjust the mix instead of discovering the saltiness after purchase.

**Data:** Saltiness is the most repeated complaint across all 45 reviews and every star rating, from "tasted like straight salt water" (1-star) to 4 and 5-star reviewers who needed to double or triple the recommended water ratio (Source: reviews.md). The landing page's benefit section (fold 2) lists "French Grey Sea Salt (Hand-Harvested Sel Gris)" as a premium ingredient callout but includes no serving or dilution guidance anywhere on the page.

**V1:** Add a short serving-guidance line, e.g. "Mix with 24-32oz of water for a milder taste," next to the French Grey Sea Salt callout in the fold 2 benefit row. Mobile: line sits below the icon+label callout, same row. Desktop: same placement within the 6-item benefit row.

## Slot 6: Add a Sticky Mobile Add-to-Cart Bar on the ICEE Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** ICEE Landing Page / PDP (instanthydration.com/products/icee-electrolyte-drink-mix)
**Revenue potential:** Sessions/mo and AOV not provided in collected data. Conservative CR lift on mobile paid traffic: 1-2%.

**Hypothesis:** If we add a sticky add-to-cart bar that persists as the visitor scrolls, conversion rate on mobile paid traffic will increase because the primary CTA stays reachable on a long, slow-loading page instead of requiring a scroll back up or down to find it.

**Data:** The primary CTA, "SELECT FROM 14 FLAVORS," is manually repeated at least 3 times across the buy box, below the accordion, and at the end of the comparison section, rather than persisting as a fixed bar. The header shows only a static cart icon, no add-to-cart bar (Source: meta-ads-visual-summary.md). Mobile time-to-interactive on this page is 35.3s, extending how long a visitor scrolls before the next CTA repeat loads.

**V1:** Add a sticky bottom bar on mobile only, showing product name, price, and an "ADD TO CART" button, that appears once the visitor scrolls past the main buy box. Desktop: no sticky bar, existing repeated CTAs remain unchanged.

## Slot 7: Clarify the Auto-Added Free Sampler in the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart
**Revenue potential:** Sessions/mo and AOV not provided in collected data. Conservative CR lift from reduced cart-stage confusion: 0.5-1%.

**Hypothesis:** If we label the auto-added "3 Pack Sampler" line item as the ad's free gift, cart abandonment will decrease because shoppers will connect it to the offer they expected instead of seeing an unexplained free item.

**Data:** The cart drawer shows a "3 Pack Sampler" line item marked "FREE" with no visible action that added it, alongside the main product with its subscription label. No text in the drawer connects the sampler to the ad's "FREE GIFT" promise (Source: site-visual-summary.md, cart drawer).

**V1:** Add a small label under the "3 Pack Sampler" line item reading "Your free gift, added automatically." Mobile and desktop: same drawer layout, label added directly under the existing line item, no other cart drawer elements change.

## Slot 8: Promote the Competitor Comparison Table Higher on the Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** ICEE Landing Page / PDP (instanthydration.com/products/icee-electrolyte-drink-mix)
**Revenue potential:** Sessions/mo and AOV not provided in collected data. Conservative CR lift: 0.5-1%.

**Hypothesis:** If we move the Instant Hydration vs. Liquid I.V. vs. LMNT comparison table higher on the page, conversion rate will increase because price-comparing shoppers will see the brand's favorable calorie, sugar, and sodium-type positioning before deciding to leave and compare elsewhere.

**Data:** The comparison table currently sits in fold 3, the last section before the page's final CTA, after the buy box, accordion, review callout, and three lifestyle photo cards. It already shows favorable rows (10 cal vs. 45, 0g sugar vs. 11g) but is reached only after 2+ folds of scrolling (Source: meta-ads-visual-summary.md, fold 3).

**V1:** Move the comparison table to directly below the buy box, ahead of the accordion and review callout. Mobile: table becomes a horizontally scrollable card set immediately after the buy box. Desktop: same repositioning, full table width below the buy box.

## Future Slot Candidates

1. **Disclose stevia content explicitly near the sweetener callout** - Marketing emphasizes "sweetened with organic monk fruit," but multiple reviewers report stevia sensitivity or aftertaste and appear unaware the product also contains stevia (Source: reviews.md). Adding "monk fruit and stevia" to the benefit callout would pre-qualify sensitive buyers and reduce post-purchase 1-2 star reviews.
2. **Align Google Ads discount messaging with Meta's offer** - Google Ads runs 35-55% off messaging across ~30 ad units, while Meta consistently uses "Try Risk Free for 50 Days + FREE GIFT" (Source: Google Ads Transparency vs. meta-ads-visual-summary.md). Standardizing the primary discount claim across channels would reduce cross-channel trust erosion for retargeted shoppers.
3. **Reframe price objections with per-stick value messaging on the PDP** - "$37 for 20 packs" and "a little pricey" recur across otherwise satisfied 3-5 star reviews (Source: reviews.md). The buy box already shows per-stick pricing but doesn't connect it to a value comparison against bottled sports drinks.
4. **Reuse athlete endorsements in the paid funnel** - The homepage's athlete endorsement row (Max Holloway, Shawn Johnson, Jameis Winston) doesn't appear in any captured Meta ad creative or on the ICEE landing page (Source: site-visual-summary.md). This trust asset is unused in the highest-traffic funnel.
