# Evo CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, live homepage WebFetch, Competitor research (self-researched)

evo's biggest conversion problem isn't copy or layout. It's speed. The homepage scores 34/100 on Lighthouse with a 12.9s Largest Contentful Paint and a 45.5s Time to Interactive. The PDP scores 30/100, with an 11.1s LCP and a 49.8s Time to Interactive (Source: PageSpeed/Core Web Vitals, fetched 2026-08-21). Every paid click from Meta and Google lands on one of these two templates. A shopper can't tap Add to Cart for the better part of a minute after the page starts rendering. This suppresses every other test on this list before a shopper sees the offer.

Trust signals are strong but hidden. evo's free shipping threshold ($50), 366-day return window, and lowest price guarantee already beat or match its closest competitors: Backcountry.com (90-day returns) and Christy Sports ($99 free shipping threshold) (Source: Competitor research). But that text sits below Add to Cart on the PDP and disappears entirely from the cart drawer, the exact moment a shopper is deciding whether to buy.

Ad messaging is inconsistent across channels. Google ads state price, discount percentage, and guarantee terms directly in the ad copy: "Up To 50% Off," "We Beat Prices by 5%," "366 Day No Hassle Returns" (Source: Google Ads Transparency). The three Meta ads reviewed use generic seasonal copy with no price or offer detail, including on a $14.99 Burton toe strap accessory where the copy's scope doesn't match the product (Source: Meta Ads & Landing Pages). Google is training shoppers to expect price and guarantee terms up front. Meta isn't delivering them, and the site's load time delays that information even further once a shopper does click through.

Session volume, PDP/collection AOV, and channel traffic splits were not available in any collected source, so revenue estimates for each slot below are shown as conservative lift ranges, not dollar figures. Once traffic and AOV data are available, applying a 5-10% CR lift to paid landing traffic on the load time fix alone gives the clearest picture of the opportunity size, since that fix touches 100% of paid clicks.

## Slot 1: Homepage & PDP Load Time Remediation

**Type:** Immediate Fix

**Why this is the priority:** Every paid click from Meta and Google lands on the homepage or a PDP, and neither is interactive for 45+ seconds, per Lighthouse data captured 2026-08-21. Homepage: 34/100 Lighthouse score, 12.9s LCP, 1,110ms Total Blocking Time, 45.5s TTI. PDP: 30/100, 11.1s LCP, 1,610ms TBT, 49.8s TTI. Both pages report CLS of 0, so the problem is load and interactivity, not layout shift (Source: PageSpeed/Core Web Vitals, fetched 2026-08-21). This is systemic, not a single-element bug, and it suppresses conversion on every test below it. Fix it directly rather than testing it.

**What we're building:** A performance remediation pass on the homepage and PDP templates targeting Time to Interactive and Total Blocking Time. Scope (script deferral, image/asset loading, third-party tag audit) should be defined by a developer audit of both templates, since the seed data flags this as systemic rather than isolated to one component.

**Key requirements:**
- Reduce PDP and homepage Time to Interactive from 45-50s toward Google's "good" threshold (under 3.8s)
- Reduce Total Blocking Time on both templates
- Re-run Lighthouse on both templates post-fix to confirm score improvement

**Success metrics:**
- Lighthouse performance score improvement on homepage and PDP (baseline: 34/100 and 30/100)
- TTI reduction on both templates (baseline: 45.5s and 49.8s)
- Paid-traffic conversion rate lift once resolved

## Slot 2: Surface Trust Signals in the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (right-side slide-out drawer)
**Revenue potential:** Sessions/mo and average cart value not available in current data. Conservative estimate: 1-2% CR lift on cart-to-checkout.

**Hypothesis:** If we add evo's free shipping, returns, and price guarantee text to the cart drawer, cart-to-checkout conversion increases because the shopper loses access to that reassurance at the exact moment they're deciding whether to buy.

**Data:** The cart drawer shows a product thumbnail, title, SKU, color, size, sale price, a "Sell Out Risk: Medium (4 remaining)" scarcity note, quantity stepper, and a "Checkout" button, but no free shipping threshold, return policy, or price guarantee text, even though that exact block exists one screen up on the PDP (Source: Current Site Screenshots, cart drawer).

**V1:** Add a compact trust-signal row below the line item and above the "Promo Code" field: free shipping over $50, 366-day returns, lowest price guarantee. Mobile: single-line icon + text row, collapsible if space is tight. Desktop: same row, full width, no collapse needed given more available space. The scarcity note, quantity stepper, and Checkout button stay unchanged.

## Slot 3: Move PDP Trust-Signal Block Above the Fold

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages (PDP)
**Revenue potential:** Sessions/mo and AOV not available in current data. Conservative estimate: 1-2% CR lift on PDP-to-cart.

**Hypothesis:** If we move the rewards/shipping/price-guarantee/returns text block into fold 1 next to the Add to Cart button, PDP-to-cart conversion increases because shoppers see the answer to "what if I don't like it" and "is this a good deal" before they decide, not after.

**Data:** On all three ad landing pages (PDPs), fold 1 shows the product gallery and a buy box with price, PayPal financing, a sale banner, variant selectors, and Add to Cart. The trust-signal text block ("Earn X in rewards," free shipping over $50, lowest price guarantee, 366-day returns) only appears in fold 2, after Add to Cart (Source: Meta Ads & Landing Pages, Ads 1-3 fold comparison).

**V1:** Add a condensed one-line version of the trust block ("Free shipping $50+ · 366-day returns · Price match guarantee") directly beneath the Add to Cart button in fold 1, on both mobile and desktop. The full trust-signal block stays in fold 2 as-is; this adds a summary line, it doesn't remove the existing content.

## Slot 4: Add Review Proof to the Kids' Bundle PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages (PDP) — bundle/kit products
**Revenue potential:** Sessions/mo not available in current data. Conservative estimate: 0.5-1% CR lift, scoped to bundle/kit product pages.

**Hypothesis:** If we add a star rating and review count to the kids' snowboard bundle PDP (and other bundle/kit pages missing this element), conversion increases because the highest-priced product in the ad set currently shows the least proof.

**Data:** The GNU Young Money bundle landing page ($537.64) shows no star rating or review count in fold 1 or fold 2. The two other ad landing pages reviewed both show a star rating and review count directly under the product title: 4/5 with "Read 3 Reviews" ($14.99 product) and 5/5 with "Read 59 Reviews" ($201.99 product) (Source: Meta Ads & Landing Pages, Ad 1 vs. Ad 2/Ad 3 comparison).

**V1:** Add a star rating and "Read N Reviews" link directly under the product title, in the same position and format used on Ad 2 and Ad 3's landing pages. Same placement on mobile and desktop. If a bundle SKU has no review count of its own, roll up the component products' review counts rather than leaving the space blank.

## Slot 5: Simplify the Multi-Component Bundle Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages (PDP) — bundle/kit products
**Revenue potential:** Sessions/mo not available in current data. Conservative estimate: 1-2% CR lift on bundle PDP traffic (bundle price ~$538).

**Hypothesis:** If we visually group the bundle's three variant selectors under numbered steps, bundle PDP conversion increases because shoppers can see they're configuring three products as one purchase instead of scrolling through an undifferentiated block.

**Data:** The kids' bundle landing page stacks three variant selectors (snowboard size, binding color, boot size) plus a quantity selector in one scrolling block with no visual grouping, numbering, or step indicator before the shopper reaches Add to Cart (Source: Meta Ads & Landing Pages, Ad 1, folds 1-3).

**V1:** Group the three selectors under labeled steps ("1. Snowboard size," "2. Binding color," "3. Boot size") with light visual separation (divider lines or numbered badges) between each. Mobile: stack steps vertically with the same numbering. Desktop: same vertical stack, no layout change beyond adding the grouping. Add to Cart button position and the "Explore Similar Packages" carousel stay unchanged.

## Slot 6: Align Meta Ad Copy with Google's Price/Offer-Led Approach

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ads & Landing Pages
**Revenue potential:** Meta spend/sessions not available in current data. Conservative estimate: 5-10% CTR/CVR lift on the Meta ad set.

**Hypothesis:** If Meta ad copy states price, discount percentage, and guarantee terms the way Google ad copy already does, Meta CTR and post-click conversion increase because shoppers arrive pre-qualified on price and offer instead of discovering it after a 45+ second page load.

**Data:** Google ads state explicit terms in the ad text itself: "Up To 50% Off," "We Beat Prices by 5%," "366 Day No Hassle Returns," "Lowest Price Guarantee" (Source: Google Ads Transparency). The three Meta ads reviewed use generic seasonal copy with no price or discount stated, including on Ad 2, where broad "latest skis, snowboards & more" copy is applied to a $14.99 Burton toe strap accessory, a scope mismatch between the ad promise and the product (Source: Meta Ads & Landing Pages).

**V1:** Rewrite Meta ad copy to lead with the specific price, discount percentage, and one guarantee term relevant to the product shown, matching Google's pattern. For accessory-tier products like the toe strap, scope the copy to the specific product rather than the broader seasonal category. Applies to ad copy only; landing pages and creative stay unchanged. Same copy used across mobile and desktop placements, since Meta ad copy doesn't differ by device.

## Slot 7: Add a Shipping-Threshold Progress Bar to the Cart

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (right-side slide-out drawer)
**Revenue potential:** Sessions/mo and average cart value not available in current data. Conservative estimate: 2-4% AOV lift on cart sessions.

**Hypothesis:** If we add a progress bar showing distance to the $50 free-shipping threshold in the cart drawer, average order value increases because shoppers see a concrete, actionable reason to add one more item before checking out.

**Data:** evo's homepage states "Fast, free shipping to get your gear on time" as a brand promise, with a $50 threshold (Source: live homepage WebFetch). The cart drawer's "You May Also Like" carousel shows cross-sell products but no shipping-threshold indicator and no bundle discount (Source: Current Site Screenshots, cart drawer).

**V1:** Add a thin progress bar above the "You May Also Like" carousel showing "$X away from free shipping" or "You've unlocked free shipping" once the $50 threshold is met, recalculating as quantity changes. Same placement and copy on mobile and desktop. The "You May Also Like" carousel and Checkout button stay unchanged.

## Slot 8: Test a Non-Sale, Brand-Promise-Led Homepage Hero

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (evo.com)
**Revenue potential:** Sessions/mo and AOV not available in current data. Conservative estimate: 1-3% CR lift on homepage sessions.

**Hypothesis:** If the homepage hero leads with evo's brand-promise callouts instead of only sale messaging, homepage conversion increases because shoppers see differentiation (shipping, returns, price match, perks) instead of a discount claim they can find on any competitor's site.

**Data:** The current hero is a full-width lifestyle photo overlaid with "UP TO 50% OFF — SUMMER & SNOW GEAR," directly beneath a sitewide "LABOR DAY SALE" banner, with no product or brand-differentiation messaging in the hero itself. A live WebFetch of the homepage confirms four brand-promise callouts exist ("Fast, free shipping," "Return gear easily," "Find a lower price, we'll match it," "Unlock exclusive perks") but sit below the folds captured in screenshots (Source: Current Site Screenshots, live homepage WebFetch, 2026-08-21).

**V1:** Add the four brand-promise callouts as a compact row directly beneath the hero image, above the category carousel. Mobile: horizontal scroll row of 4 icon + short-text callouts. Desktop: static 4-column row, no scroll needed. The hero image and sale banner stay unchanged; this is scoped as an evergreen addition, not a sale-specific one, so it should keep running after the Labor Day promo ends.

## Future Slot Candidates

1. **FAQ accordion from AI chat widget questions** - The AI chat widget on PDPs surfaces preset questions (e.g. "Does this bundle include bindings and boots?") that could inform an FAQ accordion test, but no engagement data was collected to size this opportunity.
2. **Collection page pagination clarity** - The "Labor Day Sale" collection shows "9758 Items" with no visible pagination control in any captured fold, which risks decision paralysis. Only the sale collection was captured, so this needs confirmation on an evergreen category page before testing.
