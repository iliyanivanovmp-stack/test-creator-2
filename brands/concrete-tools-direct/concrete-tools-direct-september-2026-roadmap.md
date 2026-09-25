# Concrete Tools Direct CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, live site WebFetch, self-researched competitor data

## Insights

The single biggest problem in this dataset is page speed. Mobile homepage LCP is 28.0 seconds and PDP LCP is 12.8 seconds, 11x and 5x over Google's 2.5-second "good" threshold, with Performance scores of 32/100 and 34/100. CLS is 0 on both pages, so this isn't a layout problem, it's raw load time. Every visitor to these two page types, including paid traffic from Meta, waits half a minute for the homepage to render — Source: PageSpeed / Core Web Vitals.

Paid traffic and landing experience don't match. All three active Meta ads lead with "Our best price guarantee ensures you get the best value without compromise," but the PDPs for Ad 1 (Imer Minuteman II, $809) and Ad 2 (Imer Workman II 250, $3,199) don't carry a Best Price Guarantee badge in the buy box, even though that badge appears on homepage and collection top-seller cards — Source: Meta Ads and Landing Pages. Ad 3 promotes a Core Cut 11.7HP walk-behind saw and sends traffic straight to the homepage, where the top three folds show MudMixer bundles and a Husqvarna saw with zero Core Cut branding — Source: Meta Ads and Landing Pages, Current Site Screenshots.

On the PDP, the purchase path works against itself. The Add To Cart button is static, not sticky, and sits at the bottom of fold 2 — once a visitor reads into "Product Details" in fold 3, the button is gone. Trust badges, a testimonial, and the 90-day return line all live in fold 3, a scroll below the CTA rather than beside it — Source: Current Site Screenshots. Neither competitor (Concrete Tool Supply, Contractors Direct) visibly matches this site's 90-day return/1-year warranty stack or its $100,000 financing offer, so the trust advantage is real, it's just buried below the decision point — Source: Competitor Analysis.

Smaller gaps compound the above: the homepage carries no visible star rating despite a real 4.90/61-review standing sitewide, the Equipment collection (641 products) defaults to Price High-to-Low instead of Best Selling, and the only captured checkout screen shows zero upsell or cross-sell messaging on a $4,095 order — Source: Current Site Screenshots, live site WebFetch.

Monthly sessions and AOV were not collected for this account, so no dollar-value revenue estimate can be calculated for any slot below. Every lift figure is a conservative, directional percentage only.

---

## Slot 1: Fix Homepage and PDP Page Speed (LCP)

**Type:** Immediate Fix

**Why this is the priority:** Homepage LCP is 28.0 seconds and PDP LCP is 12.8 seconds on mobile, 11x and 5x over Google's 2.5-second "good" threshold, with Performance scores of 32/100 and 34/100. CLS is 0 on both, so this is purely a load-time problem, not a layout one. This affects every visitor to these two page types regardless of traffic source, including paid clicks from Meta landing directly on the PDP. This is not a hypothesis to test, it's a broken experience to fix.

**What's broken:** Homepage TBT is 1,330ms and Time to Interactive is 28.4s. PDP TBT is 960ms and Time to Interactive is 24.9s. Source: PageSpeed / Core Web Vitals (mobile, homepage + PDP).

**Fix direction:** Diagnose and reduce render-blocking resources and largest-contentful-element load time on both templates (hero image on homepage, product gallery on PDP). No desktop PageSpeed data was collected, so desktop scores and any device-specific gap are unknown and should be checked before scoping the fix.

---

## Slot 2: Route Ad 3 to a Relevant Landing Destination

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage / Landing Page (concretetoolsdirect.com)
**Revenue potential:** Sessions/mo and AOV not collected for this account. Directional estimate: conservative 10% CR lift on Ad 3 traffic.

**Hypothesis:** If Ad 3 traffic lands on a page showing walk-behind saw products instead of the generic homepage, conversion on that ad's traffic will improve because the landing experience will match what the ad promised.

**Data:** Ad 3 (Core Cut 11.7HP walk-behind gas saw, running since Aug 10, 2026) currently links to the homepage. The homepage's first three folds show a giveaway block, then MudMixer bundles and a Husqvarna saw as top sellers, with no Core Cut product or brand mention visible. Source: Meta Ads and Landing Pages, Current Site Screenshots.

**V1:** Change Ad 3's destination link from the homepage to the Equipment collection filtered to the walk-behind saws subcategory pill, so the first products a clicking visitor sees are saws, not mixers. Mobile and desktop: same destination change, no new page build. Control stays on the current homepage destination.

---

## Slot 3: Add Best Price Guarantee Badge to Ad 1 and Ad 2 PDPs

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages (Imer Minuteman II, Imer Workman II 250)
**Revenue potential:** Sessions/mo and AOV not collected. Directional estimate: conservative 3-5% CR lift on Meta ad traffic to these two PDPs.

**Hypothesis:** If the Best Price Guarantee badge that already appears on homepage and collection top-seller cards is added to the buy box on Ad 1 and Ad 2's PDPs, conversion on that traffic will improve because the page will reinforce the exact promise the ad made.

**Data:** All three Meta ads share the primary text "Our best price guarantee ensures you get the best value without compromise." Ad 1's PDP ($809, Imer Minuteman II) and Ad 2's PDP ($3,199 from $3,649, Imer Workman II 250) both show In Stock/Free Shipping/No Taxes badges and pricing, but neither shows a Best Price Guarantee badge, while homepage and collection top-seller cards do. Source: Meta Ads and Landing Pages, Current Site Screenshots.

**V1:** Add the existing Best Price Guarantee badge (same visual treatment used on homepage/collection top-seller cards) to the buy box on both PDPs, placed next to the price. Mobile and desktop: badge sits directly under or beside the price block on both. Bundled as one test since it's the same mechanic applied to two products.

---

## Slot 4: Sticky Add To Cart on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages (represented by MudMixer Evolution Bundle)
**Revenue potential:** Sessions/mo and AOV not collected. Directional estimate: conservative 2-4% CR lift on PDP sessions.

**Hypothesis:** If the Add To Cart button becomes sticky as a visitor scrolls past fold 2, conversion will improve because buyers reading "Product Details" copy in fold 3 won't have to scroll back up to purchase.

**Data:** On the MudMixer Evolution Bundle PDP, the orange Add To Cart button sits at the bottom of fold 2, below a five-item "Complete Your Bundle" checkbox list. It's static, not sticky, and scrolls out of view once a visitor reaches fold 3's testimonial, trust badges, and Product Details copy. Source: Current Site Screenshots.

**V1:** Make the Add To Cart button sticky (persistent bar at the bottom of the viewport on mobile, persistent within the buy box on desktop) once a visitor scrolls past its original fold 2 position. Control keeps the current static button.

---

## Slot 5: Move Trust Badges and Guarantee Language Beside the CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages (represented by MudMixer Evolution Bundle)
**Revenue potential:** Sessions/mo and AOV not collected. Directional estimate: conservative 2-3% CR lift on PDP sessions.

**Hypothesis:** If the testimonial, trust badges, and 90-day return line move from fold 3 to directly beside the Add To Cart button in fold 2, conversion will improve because buyers will see the trust signals at the moment they decide to buy, not after.

**Data:** On the PDP, the testimonial quote ("Trusted by contractors nationwide"), three trust badges (Authorized Dealer, Google Top Quality Store, BBB Accredited), the "Talk to an expert" phone CTA, and the secure checkout/90-day returns line all sit in fold 3, below the Add To Cart button and bundle line-item checklist. The same fold-3 placement repeats on both Meta ad landing PDPs. Neither competitor (Concrete Tool Supply, Contractors Direct) visibly matches this site's 90-day return/1-year warranty stack. Source: Current Site Screenshots, Meta Ads and Landing Pages, Competitor Analysis.

**V1:** Relocate the trust badge row and the 90-day returns line into fold 2, directly beneath the Add To Cart button, ahead of the bundle checkbox list. Testimonial and phone CTA remain in fold 3. Mobile and desktop: same reordering, badges stack horizontally on desktop and wrap on mobile. This is a distinct mechanic from Slot 4 (content reordering, not scroll behavior).

---

## Slot 6: Add Sitewide Star Rating to Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** Sessions/mo and AOV not collected. Directional estimate: conservative 1-2% CR lift on homepage entries.

**Hypothesis:** If the site's real 4.90-star, 61-review rating is shown near the hero headline, conversion on homepage entries will improve because visitors will see a credibility signal immediately instead of only a floating popup on fold 2.

**Data:** Live homepage carries a 4.90-star rating across 61 verified reviews per WebFetch, but the captured homepage screenshots show no star rating or review count in the header or hero. The only review-related element is a floating popup card on fold 2. Source: Current Site Screenshots, live site WebFetch.

**V1:** Add a static "4.90★ (61 reviews)" badge near the hero headline, above the "Shop Equipment" CTA. Mobile and desktop: badge sits directly under the headline on both, sized to not push the CTA below the fold. Control keeps the current fold-2 popup as the only review signal.

---

## Slot 7: Default Collection Sort to Best Selling

**Type:** A/B test (1 variation vs. control)
**Page:** Collection / Category page (Equipment, 641 products)
**Revenue potential:** Sessions/mo and AOV not collected. Directional estimate: conservative 2-3% CR lift on collection-entry sessions.

**Hypothesis:** If the Equipment collection defaults to Best Selling instead of Price High-to-Low, browse-to-cart conversion will improve because visitors will see popular products first instead of the most expensive bundles in the catalog.

**Data:** The Equipment collection (641 products, ~60 subcategory pill-buttons) currently loads with "Sort by: Price, high to low" as the default, surfacing the most expensive bundles ($4,095, $3,995, $3,695) first. Source: Current Site Screenshots.

**V1:** Change the default sort from Price High-to-Low to Best Selling. Mobile and desktop: same default sort change, sort control and subcategory pills stay in their current position. Control keeps Price High-to-Low as default.

---

## Slot 8: Add Trust and Cross-Sell Messaging to Checkout Entry

**Type:** A/B test (1 variation vs. control)
**Page:** Cart / Checkout entry (order-summary / Express Checkout screen)
**Revenue potential:** Sessions/mo and AOV not collected. Directional estimate: conservative 1-3% AOV lift on checkout sessions.

**Hypothesis:** If the order-summary screen reinforces the site's free shipping and 90-day return guarantee alongside a single cross-sell prompt, average order value will improve because buyers will see reasons to add to the order and confidence to complete it at the one funnel point built for it.

**Data:** The only cart-adjacent screen collected (an Express Checkout / order-summary screen, not a true cart drawer) shows a cart total of $5,044.95 struck through to $4,095.00, three trust icons, and Express checkout buttons (Shop Pay, PayPal, Apple Pay), followed by a Contact/Delivery form. No upsell, cross-sell, or free-shipping-threshold messaging appears anywhere in this screen. Free shipping and a 90-day return/1-year warranty are documented brand differentiators used elsewhere on the site. Source: Current Site Screenshots.

**V1:** Add one cross-sell prompt above the Contact/Delivery form (surfacing a related accessory or add-on) and restate the 90-day return guarantee next to the existing trust icons. Mobile and desktop: cross-sell prompt is a single collapsed row on mobile, expanded inline on desktop. Note: true cart line-item view was not captured for this project, so this variation is scoped to the order-summary screen only.

---

## Future Slot Candidates

1. **Unify Google Shopping and Meta ad messaging** - Google Shopping ads carry none of Meta's "best price guarantee" copy and span a far wider product range (mixers, saws, drills, grinders, generators, wheelbarrows, gloves, blades) than Meta's two-mixer/one-saw set, suggesting the two paid channels aren't running a coordinated message strategy.
2. **Move product discovery above the giveaway block on homepage** - The homepage leads with brand storytelling and a giveaway ("Win a $2,369 Concrete Compaction Bundle") before any product appears; specific products don't show until fold 2-3, a broader pattern than any single slot above.
3. **Surface the $100,000 financing offer sitewide** - Financing currently appears via a separate CTA button on PDPs but is absent from the homepage hero and the collection page, despite being a differentiator neither competitor (Concrete Tool Supply, Contractors Direct) visibly offers.
