# Hollow Socks CRO Research Brief

**Data Sources:** Meta ads visual summary, Google ads visual summary, Amazon reviews (80, collected 2026-06-02), Lighthouse PageSpeed (homepage + compression LP), site visual summary (homepage, collection, PDP, cart drawer), live site fetch, self-researched competitor data (June 6, 2026)

## Insights

The core conversion problem is at the PDP buy box. The buy box stacks three pricing tiers vertically between the width selector and the Add to Cart button: 1 pair at $49.99, 2 pairs at $37.49/pair, and 4 pairs at $25.00/pair. The 1-pair option is pre-selected by default. The 4-pair "BEST VALUE" tier carries no visual distinction beyond a text label and sits unselected. A visitor must make a three-way pricing decision before committing to a purchase. That $50 AOV gap between the lowest and highest option is the single largest lever available without touching the product. Source: site visual summary (PDP), live site fetch.

The LP feeding this funnel has a serious load problem. Lighthouse scores the compression landing page at 42/100 on mobile with an 8.4s LCP and 33.2s TTI. This is the destination for all Meta compression ads and all Google search ads targeting edema and compression queries. Google's benchmark: 53% of mobile visitors abandon pages that take over 3 seconds to load. The current LCP is 2.8x that threshold. Revenue is leaving before the page renders. Source: Lighthouse PageSpeed (compression LP).

The brand has 6,333 reviews. None of them appear as proof at the moment of purchase. The buy box shows "★★★★★ (6333 REVIEWS)" as a linked line near the product title with no star breakdown, no snippet, and no featured quote. The next review content visible on the page is a pair of UGC video thumbnails in Fold 3, below the sticky footer bar, past the spec table. Buyers who decide at the buy box never see: "After having quadruple heart surgery... my swelling has totally gone away!!" (Joe Stinger). Source: Amazon reviews, site visual summary.

Sizing failure is the dominant negative review theme. Over 10 of 27 negative Amazon reviews cite calf fit failure for buyers with edema, DVT, or post-surgery conditions. This is the primary medical audience for compression socks, and they statistically have larger legs. The LP addresses wide calf in Reason 5. The PDP width selector shows only "Standard" and "Wide" radio options with no calf circumference ranges inline. Buyers who skip the LP and land directly on the PDP have no fit reassurance without clicking the Width Guide link. Source: Amazon reviews, site visual summary.

The cart progress bar prompts visitors to add one more pair to unlock two free pairs. Below the single cart item, roughly 40% of the cart drawer height is blank white space. No product tiles, no cross-sell widget, and no bundle prompt render there. The prompt exists; the payoff does not. Session volume data is unavailable, so revenue impact cannot be calculated precisely. The directional case is clear: a paid acquisition model at $100 AOV with LCP at 2.8x Google's threshold, a buy box defaulting to the lowest-value option, and a broken cart mechanic means revenue is leaking at three high-volume touchpoints at once. Source: site visual summary (cart drawer).

---

## Slot 1: PDP Buy Box — Pre-Select 4-Pair Best Value Tier

**Type:** A/B test (1 variation vs. control)
**Page:** Compression Socks PDP
**Revenue potential:** PDP sessions/mo [unknown] x 8% conservative ATC improvement x $100 AOV = monthly impact TBD. AOV upside per order if bundle shift occurs: $50.

**Hypothesis:** If we pre-select the 4-pair "BEST VALUE" tier in the buy box, add-to-cart rate and AOV improve because removing the default anchor on the lowest-value option eliminates the three-way pricing decision at the moment of commitment.

**Data:** The buy box currently defaults to 1 pair at $49.99. The 4-pair tier at $25.00/pair carries a "BEST VALUE" text label but is not pre-selected and has no visual distinction from the other two options. The $50 AOV gap between 1-pair and 4-pair is the single largest per-order lever available without adding new product. Source: site visual summary (PDP Fold 2), live site fetch.

**V1:** Pre-select the 4-pair tier radio button on page load. Add a highlighted border or background tint to the 4-pair option row to visually separate it from the 1-pair and 2-pair options. The "ADD TO CART" button copy updates to reflect 4 pairs at $100. Mobile: pre-selection applies identically on mobile load. Desktop: same behavior. Width selector and all other buy box elements remain unchanged.

---

## Slot 2: PDP Wide-Calf Fit Reassurance in Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Compression Socks PDP
**Revenue potential:** PDP sessions/mo [unknown] x 5% conservative CR improvement for wide-calf segment x $100 AOV = monthly impact TBD. Reduction in returns is an additional unmeasured benefit.

**Hypothesis:** If we add calf circumference ranges directly beside the "Standard" and "Wide" radio options in the width selector, conversion improves for large-calf buyers because they can confirm fit without clicking through to the Width Guide.

**Data:** Over 10 of 27 negative Amazon reviews cite calf fit failure for buyers with edema or larger legs. The LP addresses this in Reason 5 ("Wide Calf and Women's Sizes Included") but the PDP width selector shows only "Standard" and "Wide" labels with a Width Guide link. Buyers who arrive at the PDP directly have no inline fit guidance. "If you have any circulation problem, your legs are probably going to be bigger and these are not for you." Source: Amazon reviews, site visual summary.

**V1:** Add calf circumference measurements inline beside each width option in the buy box (e.g., "Standard: up to 15 in" and "Wide: up to 20 in," or equivalent based on product specs). The Width Guide link remains present. No other buy box elements change. Mobile: measurements appear on the same line as the radio label or directly below it. Desktop: same display.

---

## Slot 3: Cart Cross-Sell Widget

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer
**Revenue potential:** Cart sessions/mo [unknown] x 10% conservative AOV lift on single-item carts x $50 gap between 1-pair ($49.99) and 4-pair bundle ($100) = monthly impact TBD.

**Hypothesis:** If we populate the blank cart drawer area with product recommendation tiles, visitors act on the "ADD 1 PAIR MORE TO UNLOCK 2 FREE PAIRS" progress bar because the prompt now has a product to act on.

**Data:** The cart drawer shows a progress bar at the top with "ADD 1 PAIR MORE TO UNLOCK 2 FREE PAIRS" and milestone icons. Below the single cart item and quantity stepper, roughly 40% of the cart drawer height is blank white space. No product recommendation tiles, complementary SKUs, or bundle prompts render. The progress bar mechanic is designed and present; the implementation is broken or unpopulated. Source: site visual summary (cart drawer).

**V1:** Render 1-2 product recommendation tiles in the blank area directly below the cart item and above the Subtotal footer. Tiles should surface additional Hollow Socks SKUs or complementary products to help visitors reach the next progress bar milestone. Mobile: tiles stack vertically within the drawer. Desktop: same layout within the drawer column. Progress bar, cart item, quantity stepper, and checkout footer remain unchanged.

---

## Slot 4: Landing Page LCP Optimization

**Type:** A/B test (1 variation vs. control)
**Page:** Compression LP (https://hollowsocks.com/pages/10r-compression-g1)
**Revenue potential:** LP sessions/mo [unknown] x 10% conservative paid traffic conversion recovery x $100 AOV = monthly impact TBD. Benchmark: 53% of mobile visitors abandon pages loading over 3 seconds. Current LCP is 8.4 seconds.

**Hypothesis:** If we reduce the compression LP's LCP from 8.4s to under 3s, paid traffic conversion improves because fewer visitors abandon before the page renders.

**Data:** Lighthouse mobile audit: LCP 8.4s, TTI 33.2s, performance score 42/100. Above-the-fold content includes a full-width hero, announcement bar with countdown timer, author byline image, and comparison table. These elements are consistent with an unoptimized hero image load and render-blocking scripts. The compression LP is the destination for all Meta compression ads and Google search ads targeting compression and edema queries. Source: Lighthouse PageSpeed (compression LP).

**V1:** Optimized version of the compression LP: hero image loading prioritized or lazy-loaded correctly, non-critical scripts deferred, announcement bar countdown timer decoupled from render-blocking execution. Mobile LCP target: under 3 seconds (current: 8.4s). Desktop: same optimizations applied. No changes to copy, offer structure, or visual layout.

---

## Slot 5: PDP Review Snippet Near ATC

**Type:** A/B test (1 variation vs. control)
**Page:** Compression Socks PDP
**Revenue potential:** PDP sessions/mo [unknown] x 3% conservative CR improvement x $100 AOV = monthly impact TBD.

**Hypothesis:** If we add a featured review quote directly below the pricing tiers and above the Add to Cart button, conversion improves because medical-outcome proof appears at the moment of purchase decision rather than below the fold.

**Data:** The buy box shows "★★★★★ (6333 REVIEWS)" as a linked line near the product title. No star breakdown, no snippet, and no featured quote appear in the buy box. The next review content is a pair of UGC video thumbnails in Fold 3, below the sticky footer bar and the spec table. Available high-credibility quotes: "After having quadruple heart surgery... my swelling has totally gone away!!" (Joe Stinger). "These are the first compression socks I can actually put on easily." (Joe B.). Source: site visual summary (PDP Fold 1, Fold 3), Amazon reviews.

**V1:** Insert a single review block directly between the pricing tier radio buttons and the "ADD TO CART" button in the buy box. Block includes a star rating (★★★★★), a 1-2 sentence verified buyer quote, and reviewer first name with brief context (e.g., "Joe S., post-surgery"). Mobile: full-width within the buy box column. Desktop: same placement at buy box width.

---

## Slot 6: Landing Page Countdown Urgency

**Type:** A/B test (1 variation vs. control)
**Page:** Compression LP (https://hollowsocks.com/pages/10r-compression-g1)
**Revenue potential:** LP sessions/mo [unknown] x 5% conservative conversion improvement x $100 AOV = monthly impact TBD.

**Hypothesis:** If we replace the current static or misconfigured countdown timer in the announcement bar with a dynamic deadline tied to a real promotion window, urgency becomes credible and LP conversion improves for retargeted visitors.

**Data:** The compression LP above-the-fold area includes an announcement bar with a countdown timer. A countdown on a related Hollow Socks LP was observed reading "THIS WEEKEND" on a 4th of July-framed ad after the holiday had passed. A static or post-expiry countdown signals low authenticity to retargeted visitors who have seen the same creative multiple times. Source: site visual summary (LP), site-observed countdown behavior (Unused Findings).

**V1:** Replace the announcement bar countdown content with a dynamic timer showing a real rolling deadline (e.g., "Offer ends Sunday at midnight," refreshed weekly). The announcement bar position and design remain unchanged. Mobile: announcement bar visible above the fold as currently positioned. Desktop: same behavior. All LP copy and offer terms below the announcement bar remain unchanged.

---

## Slot 7: PDP UGC Video Above the Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Compression Socks PDP
**Revenue potential:** PDP sessions/mo [unknown] x 3% conservative CR improvement x $100 AOV = monthly impact TBD.

**Hypothesis:** If we move the UGC video thumbnails from Fold 3 to directly below the Add to Cart button, conversion improves because social video proof appears within the buying context rather than after significant scroll.

**Data:** UGC video thumbnails currently appear in Fold 3 on the Compression Socks PDP, below the sticky footer bar and below the spec table. A buyer who decides at the buy box and does not scroll never encounters this proof. The thumbnails are the strongest visual social proof on the PDP; their placement below the fold limits their influence to visitors who scroll past the spec table. Source: site visual summary (PDP Fold 3).

**V1:** Move the UGC video thumbnail strip from Fold 3 to directly below the "ADD TO CART" button, above the spec table. Mobile: thumbnails display as a horizontally scrollable strip below the ATC button. Desktop: same placement in the single-column buy box flow. The spec table and all existing Fold 3 content remain on the page, shifted down.

---

## Slot 8: Cart Social Proof Strip

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer
**Revenue potential:** Cart sessions/mo [unknown] x 2% conservative cart abandonment reduction x $100 AOV = monthly impact TBD.

**Hypothesis:** If we add a featured review quote in the blank white area of the cart drawer, cart-to-purchase rate improves because medical-outcome social proof appears at the last point of hesitation before checkout.

**Data:** The cart drawer has roughly 40% blank white space below the single cart item and above the Subtotal and checkout footer. No content renders in this area. High-credibility quotes from the review pool: "After having quadruple heart surgery... my swelling has totally gone away!!" (Joe Stinger). Placing proof at this stage addresses last-moment hesitation without additional ad spend. Source: site visual summary (cart drawer), Amazon reviews.

**V1:** Add a single review block in the blank area below the cart item and above the Subtotal footer. Block includes a star rating, a 1-2 sentence verified buyer quote on a medical outcome theme, and reviewer name with brief context. Mobile: displays as a full-width strip within the cart drawer, above the Secure Checkout CTA. Desktop: same placement within the drawer column. Progress bar, cart item, quantity stepper, and checkout footer remain unchanged.

---

## Future Slot Candidates

1. **Google Shopping Review Feed** - The Shopping ad shows 4.0 stars from 28 reviews vs. 6,383 reviews on-site. A Merchant Center feed fix could improve Shopping CTR at no creative cost.
2. **Father's Day Ad Message Match** - Ad 2 (active since May 29) has no captured LP. If traffic routes to a generic page, a dedicated gift-framed LP is the highest-priority missing asset.
3. **Past Buyer Price-Burn Retention** - Amazon buyers who paid full price then encountered the BOGO promotion represent a churn risk to lower-priced competitors. A loyalty or early-access email sequence could recover this segment.
