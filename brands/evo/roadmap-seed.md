# Evo Roadmap Seed

**Store:** evo.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, live homepage WebFetch, Competitor research (self-researched)

## Key Insights

evo's homepage and PDP fail Lighthouse performance thresholds by a wide margin: homepage scores 34/100 (12.9s LCP, 45.5s TTI), PDP scores 30/100 (11.1s LCP, 49.8s TTI). Every paid click from both the Meta and Google ad sets lands on one of these two templates, and neither is interactive for 45+ seconds. This is the single highest-evidence, highest-blast-radius issue in the dataset — it suppresses conversion on every other test on this list before a shopper even sees the page.

evo's trust-signal terms (free shipping over $50, 366-day returns, lowest price guarantee) are competitive with or better than its two closest competitors, Backcountry.com (90-day returns, beats price by 5%) and Christy Sports (free shipping over $99, 367-day returns). But the text carrying those terms sits below Add to Cart on the PDP and is completely absent from the cart drawer, the moment closest to the purchase decision.

Ad messaging is inconsistent between channels: Google ads state price, discount %, and guarantee terms directly in ad copy ("Up To 50% Off," "We Beat Prices by 5%," "366 Day No Hassle Returns"), while the three Meta ads reviewed use generic seasonal copy ("Make your powder dreams come true with the latest skis, snowboards & more") with no price or offer detail — including on a $14.99 Burton toe strap accessory, where the copy's scope mismatches the product entirely.

## Top Test Opportunities

### 1. Homepage & PDP Load Time Remediation
**What's broken:** The homepage (https://www.evo.com/) and PDP template both load extremely slowly. Homepage: 34/100 Lighthouse score, 12.9s Largest Contentful Paint, 1,110ms Total Blocking Time, 45.5s Time to Interactive. PDP (tested on the Patagonia Nano Puff Hoodie page): 30/100, 11.1s LCP, 1,610ms TBT, 49.8s TTI. Both pages report CLS of 0 — layout is stable, but nothing is clickable or interactive for the better part of a minute after the page starts rendering. This is a systemic, site-wide performance problem, not a single-element fix.
**Evidence:** Lighthouse JSON reports (pagespeed.md), fetched 2026-08-21.
**Key data:** Homepage 34/100 (12.9s LCP, 45.5s TTI); PDP 30/100 (11.1s LCP, 49.8s TTI). Both in Lighthouse's "poor" band on every timing metric.
**Est. lift:** conservative 5-10% CR lift on paid landing traffic x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data.

### 2. Surface Trust Signals in the Cart Drawer
**What's broken:** The cart is a right-side slide-out drawer (not a full page), header "Cart(1)" with a close icon. It shows one line item: product thumbnail, title, SKU, color, size, sale price with strikethrough original, a "Sell Out Risk: Medium (4 remaining)" scarcity note, quantity stepper, and a "Remove" link. Below that, a "You May Also Like" carousel with 2+ alternate products (image, title, price — no bundle discount, no cross-sell incentive). A collapsible "Promo Code" field sits above a full-width black "Checkout - $[price]" button. Nowhere in the drawer does the free-shipping threshold, return policy, or price guarantee appear — text that exists one screen up on the PDP disappears at the exact moment the shopper is deciding whether to complete the purchase.
**Evidence:** site-visual-summary.md (cart drawer), meta-ads-visual-summary.md (PDP trust-signal blocks for comparison).
**Key data:** PDP trust block includes: rewards points, free shipping over $50, lowest price guarantee, 366-day return policy — none of it repeated in cart.
**Est. lift:** conservative 1-2% CR lift on cart-to-checkout x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data.

### 3. Move PDP Trust-Signal Block Above the Fold
**What's broken:** On all three Meta ad landing pages (PDPs), fold 1 shows the product image gallery on the left and a buy box on the right with price, strikethrough original, PayPal financing line, a "Labor Day Sale" banner, variant selectors (color/size), and a black "Add to Cart" button. The trust-signal text block — "Earn X in rewards," "Free shipping on orders over $50," "Lowest price guarantee," "366 Day Return Policy" — only appears in fold 2, after the shopper has scrolled past Add to Cart. On the Patagonia Nano Puff Hoodie page, a "Sell Out Risk: Medium (4 remaining)" scarcity line and 5-star/"Read 59 Reviews" rating do appear in fold 1, but the policy terms that answer "what if I don't like it" or "is this a good deal" do not.
**Evidence:** meta-ads-visual-summary.md (Ads 1-3, fold 1 vs fold 2 comparison).
**Key data:** Trust block consistent across all 3 PDPs but positioned in fold 2 on every one.
**Est. lift:** conservative 1-2% CR lift on PDP-to-cart x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data.

### 4. Add Review Proof to the Kids' Bundle PDP
**What's broken:** Ad 1's landing page (GNU Young Money C2E Snowboard + Bent Metal BMX Bindings + Union Cadet Boots, kids' bundle, $537.64) shows no star rating or review count anywhere in fold 1 or fold 2 — the buy box goes straight from price and financing to three stacked variant pickers (board size, binding color, boot size) with no social proof. Ads 2 and 3, by contrast, both show a star rating with a "Read N Reviews" link directly under the product title ("4/5, Read 3 Reviews" and "5/5, Read 59 Reviews" respectively). This bundle carries the highest price point of the three ad products and the least proof.
**Evidence:** meta-ads-visual-summary.md (Ad 1 vs Ad 2/Ad 3 direct comparison).
**Key data:** Ad 1 (bundle, $537.64): no rating shown. Ad 2 ($14.99): 4/5, 3 reviews. Ad 3 ($201.99): 5/5, 59 reviews.
**Est. lift:** conservative 0.5-1% CR lift on this SKU's landing traffic — narrow single-SKU case; strongest example of a broader review-proof-consistency fix across bundle/kit product pages.

### 5. Simplify the Multi-Component Bundle Buy Box
**What's broken:** Ad 1's landing page buy box stacks three separate variant selectors — snowboard size, binding color, boot size (with a size range shown, "5-13.5K") — plus a quantity selector, one after another in a single scrolling block, with no visual grouping, numbering, or step indicator to show the shopper they're configuring three distinct products as one purchase. The black "Add to Cart" button follows all three selectors. A "Explore Similar Packages" carousel with 5+ alternate bundle configurations appears in fold 3, adding further choice complexity before checkout.
**Evidence:** meta-ads-visual-summary.md (Ad 1, folds 1-3).
**Key data:** Bundle price $537.64 (from $739.93); 3 stacked variant pickers with no grouping.
**Est. lift:** conservative 1-2% CR lift on bundle PDP traffic x sessions/mo (unknown) x AOV (~$538 bundle price) = revenue estimate blocked on traffic data.

### 6. Align Meta Ad Copy with Google's Price/Offer-Led Approach
**What's broken:** Google Ads Transparency Center screenshots show 20+ live ad units where headline/body copy states explicit price and policy terms: "Up To 50% Off 2025 Gear," "We Beat Prices by 5%," "366 Day No Hassle Returns," "Enjoy Fast FREE SHIPPING." The three Meta ads reviewed use generic seasonal lifestyle copy instead — "Looking for adventure? evo is your one stop shop..." and "Make your powder dreams come true with the latest skis, snowboards & more from evo this season!" (the latter reused verbatim across Ads 2 and 3) — with no price, discount percentage, or guarantee mentioned anywhere in the ad text. That information only surfaces once the shopper reaches a landing page that takes 45+ seconds to become interactive.
**Evidence:** google-ads-visual-summary.md, meta-ads-visual-summary.md (cross-channel comparison). Includes the specific case of Ad 2, where the broad seasonal copy is applied to a $14.99 Burton toe strap accessory — a scope mismatch between ad promise and product specificity.
**Key data:** Google ad copy states "Up To 50% Off," "Beat Prices by 5%," "366 Day No Hassle Returns" in-text; 0 of 3 Meta ads reviewed state price or discount in ad copy.
**Est. lift:** conservative 5-10% CTR/CVR lift on Meta ad set x current Meta spend/sessions (unknown) = revenue estimate blocked on ad spend/sessions data.

### 7. Add a Shipping-Threshold Progress Bar to the Cart
**What's broken:** The cart drawer's "You May Also Like" carousel shows 2+ alternate products with image, title, and price, but no bundle discount, no cross-sell incentive copy, and no visual indicator of progress toward evo's stated $50 free-shipping threshold — a threshold confirmed as a headline brand promise on the live homepage ("Fast, free shipping to get your gear on time") but never surfaced at the cart stage where an AOV nudge would be most actionable.
**Evidence:** site-visual-summary.md (cart drawer), live homepage WebFetch (brand promise callouts).
**Key data:** Free shipping threshold: $50 (vs. Christy Sports' $99). Not mentioned anywhere in the cart drawer.
**Est. lift:** conservative 2-4% AOV lift on cart sessions x sessions/mo (unknown) x average cart value (unknown) = revenue estimate blocked on traffic/AOV data.

### 8. Test a Non-Sale, Brand-Promise-Led Homepage Hero
**What's broken:** The homepage hero is a full-width lifestyle photo (two people with mountain bikes on a grassy hillside) overlaid with a large sale graphic reading "UP TO 50% OFF — SUMMER & SNOW GEAR," directly beneath a sitewide red "LABOR DAY SALE - UP TO 50% OFF!" top banner. No product differentiation or brand-promise messaging appears in the hero itself. A live WebFetch of the current homepage confirms evo does have four brand-promise callouts — "Fast, free shipping," "Return gear easily," "Find a lower price, we'll match it," "Unlock exclusive perks" — but they sit further down the page, below the captured fold-3 screenshots (category carousel, product picks, brand logos).
**Evidence:** site-visual-summary.md (homepage fold 1), live homepage WebFetch, 2026-08-21.
**Key data:** Brand-promise callouts exist site-wide but are not visible in homepage folds 1-3.
**Est. lift:** conservative 1-3% CR lift on homepage sessions x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data. Time-bound: scope as an evergreen hero test, not a sale-specific one.

## Unused Findings

- The AI chat widget on PDPs surfaces preset questions ("Does this bundle include bindings and boots?") that could inform an FAQ-accordion test — no engagement data collected, hypothesis only.
- The captured collection page ("Labor Day Sale," 9,758 items, no visible pagination in 3 folds) may hide a decision-paralysis issue, but only the sale collection was captured — no evergreen category page exists to confirm the pattern holds outside the promo window.
