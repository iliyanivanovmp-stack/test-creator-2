# Sofas Exclusive CRO Research Brief

**Data Sources:** Google Ads (Transparency), PageSpeed/Core Web Vitals (Lighthouse 13.2.0, mobile, 2026-06-15), site screenshots (homepage, collection, PDP, cart drawer), live site fetch

## Insights

Trust is the primary conversion barrier across every funnel stage. The homepage leads with "4.91 ★ (11)" — 11 total reviews for a brand selling sofas up to $5,992. That number does active damage: a visitor evaluating a $1,000+ sofa sees the tally before anything else and registers thin social proof, not confidence. On the collection page, THE DAKOTA card shows a 2-star rating with no review count, displayed alongside normally priced products in a grid labeled "TOP SELLERS." On the PDP, no reviews appear in any of three captured folds. The four trust icons (Nationwide Shipping, Premium Quality, Dedicated Support, Secure Checkout) sit below both CTA buttons, arriving after the purchase decision has already been made or abandoned. Source: site screenshots, live site fetch.

Mobile performance sets the ceiling for all conversion work. The homepage scores 53/100 on Lighthouse mobile with LCP of 7.5s, Speed Index of 11.5s, and TTI of 24.3s. The PDP hit the Lighthouse time limit — its 30.8s TTI is flagged as incomplete, meaning the real number is higher. Google Ads are routing paid traffic to pages that take 25-30+ seconds to become interactive on mobile. CLS on the homepage is 0.163 (needs improvement band), meaning elements shift visibly during load at the moment first impressions are forming. These numbers cap the uplift available from any UX or copy test. Source: PageSpeed/Core Web Vitals (2026-06-15).

The cart drawer is empty of revenue mechanics. Between the single line item and the checkout button sits a blank section spanning roughly 40-50% of the drawer height with no free shipping threshold bar, no cross-sell, no bundle prompt, and no urgency messaging. The site-wide announcement bar confirms free shipping is available, but the cart makes no reference to it as a threshold incentive. Two stacked CTAs ("GO TO CHECKOUT" button and "GO TO CART" text link) split exit intent at the moment of highest purchase intent. Every order passing through without an upsell is a missed AOV opportunity against a zero baseline. Source: cart drawer screenshot, live site fetch.

Paid traffic is likely arriving at a message mismatch. Google Ads use aspirational copy around sophistication and exploration, but the Best Selling sort surfaces a $278 chair first on the Top Sellers collection page. A visitor clicking a premium positioning ad lands on a $278 price anchor. Source: Google Ads, site screenshots.

---

## Slot 1: Cart Free Shipping Bar + Cross-Sell

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sofasexclusive.com cart)
**Revenue potential:** Additive from $0 baseline. The current cart contains no upsell or threshold mechanic. Any cross-sell conversion is incremental revenue on top of an order already in progress.

**Hypothesis:** If we add a free shipping progress bar and a single cross-sell tile beneath the line item, AOV increases because the drawer's empty space becomes a revenue mechanic and the free shipping offer already stated in the announcement bar gets reinforced at the highest-intent moment in the funnel.

**Data:** The cart drawer shows a visually empty section spanning roughly 40-50% of the drawer height between the line item and the subtotal block. The site-wide announcement bar confirms free shipping exists, but the cart contains no reference to it. Two stacked CTAs ("GO TO CHECKOUT" full-width button and "GO TO CART" text link below) split exit intent at checkout entry. Source: cart drawer screenshot, live site fetch, Google Ads.

**V1:** Add a free shipping progress bar directly below the line item, spanning the full drawer width. The bar shows the shipping threshold as a fixed target and current cart value as the fill level, with copy such as "You're $X away from free shipping." Below the bar, add a single cross-sell tile: one complementary product priced well below the main item (e.g., a care kit or accessory), a one-tap add button, and a short descriptor. Remove the "GO TO CART" text link; retain only the "GO TO CHECKOUT" full-width button. Mobile: bar stacked above cross-sell tile, full-width. Desktop: same stacked layout centered within the drawer.

---

## Slot 2: PDP Trust Restructure Above Fold

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (sofasexclusive.com/products/*)
**Revenue potential:** 5-10% CR improvement on PDP sessions x sessions unknown x $278-$5,992 price range = uncalculated. Even a 5% lift on a high-AOV product page materially moves revenue.

**Hypothesis:** If we move the trust icons above the add-to-cart button and give the installment option visual prominence matching the price, PDP conversion rate increases because visitors receive reassurance and affordability signals before the buy decision rather than after it.

**Data:** On the Volos Chair PDP, four trust icons (Nationwide Shipping, Premium Quality, Dedicated Support, Secure Checkout) sit in a separate section below both the "ADD TO CART" and "Buy with SHOP" buttons, arriving well past the purchase decision point. No star rating or review count appears in any of three captured folds. The Shop Pay installment option ("4 INTEREST-FREE INSTALLMENTS, OR FROM $25.09/MO WITH Shop Pay") is present but rendered in small secondary text with no visual prominence — despite the product range extending to $5,992, where installments directly address purchase hesitation. Source: PDP screenshots (Folds 1-3), homepage review count.

**V1:** Reorder the buy box stack: product name, price, installment line (upsized to match the price font weight), trust icons row (four icons horizontal, spanning full buy box width), quantity stepper, "ADD TO CART" button, "Buy with SHOP" button, stock indicator. The installment line should carry the same visual weight as the price — not secondary text. Trust icons move from below the CTAs to between the price block and the quantity stepper. No new content is introduced; only the order and visual weight of existing elements change. Mobile: stack vertically in the order above, full-width. Desktop: right-side buy box, same order.

---

## Slot 3: Homepage Hero CTA Consolidation

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (sofasexclusive.com)
**Revenue potential:** 10-20% improvement in hero CTA click-through x homepage sessions unknown = uncalculated. Consolidating to one CTA removes split intent at the entry point for all traffic.

**Hypothesis:** If we replace the two identically styled hero CTAs with a single primary button carrying a clear destination label, click-through to product or collection pages increases because visitors no longer face an ambiguous choice between two undifferentiated options.

**Data:** The homepage hero presents two side-by-side buttons of identical size, color, weight, and styling: "VIEW MORE" on the left and "SHOP NOW" on the right. There is no visual hierarchy, color differentiation, or copy distinction between them. Neither label implies a destination. Source: homepage screenshot (Fold 1), live site fetch.

**V1:** Remove "VIEW MORE." Replace the dual-button layout with a single full-width CTA in a contrasting color, distinct from the current white-on-white treatment. Button copy: "Shop Sofas" or the name of the primary collection destination. The button spans the full width of the current two-button container. Mobile: single button, full-width, centered beneath the headline and subheadline. Desktop: single button, centered in the hero overlay.

---

## Future Slot Candidates

1. **Collection page: suppress the 2-star rating on THE DAKOTA card** - Displays a 2-star rating with no review count in a grid labeled "TOP SELLERS," alongside products showing no ratings. Creates a localized trust hazard that erodes confidence in adjacent products.
2. **PDP product description above buy box** - The Volos Chair buy box goes from product name directly to price with no description. Google Ads use aspirational copy that lands nowhere on the PDP. "Product Features" appears only at the bottom of the third fold.
3. **Shop Pay installment messaging in Google Ads** - Installment pricing exists on the PDP ("$25.09/mo") but is absent from all ad headlines. Surfacing this in ad copy could improve CTR and pre-qualify traffic before the click.
4. **White Glove Delivery reinforcement at cart and PDP** - Announced in the trust bar but missing from both the buy box and cart drawer, which are the two highest-friction decision points in the funnel.
