# Hollow Socks Roadmap Seed

**Store:** https://hollowsocks.com/
**Primary LP:** https://hollowsocks.com/pages/10r-compression-g1
**AOV:** ~$100 (4-pair bundle at $25/pair; single pair $49.99)
**Monthly sessions:** Unknown
**Data sources:** Meta ads visual summary, Google ads visual summary, Amazon reviews (80, collected 2026-06-02), Lighthouse PageSpeed (homepage + compression LP), site visual summary (homepage, collection, PDP, cart drawer), live site fetch, self-researched competitor data (June 6, 2026)

## Key Insights

Hollow Socks is running a high-volume paid acquisition engine — Meta ads across Facebook/Instagram/Reels, Google search/shopping/display — all feeding into long-form "10 Reasons" landing pages with a Buy 2 Get 2 Free offer. Message match is strong on the compression angle (Ad 1 → primary LP) and the material/fiber angle (Ad 3 → alpaca vs. merino LP). The Father's Day gift ad (Ad 2, active since May 29) has no captured LP, so its message match cannot be evaluated.

The biggest conversion problem is at the PDP. The buy box stacks three pricing tiers vertically — 1-pair at $49.99, 2-pair at $37.49/pair, 4-pair at $25/pair — between the size selector and the Add to Cart button, forcing a bundle decision before a visitor has committed to buying. The 4-pair tier carries a "BEST VALUE" label but is not pre-selected. Meanwhile, 6,333 reviews appear only as a linked number — no star breakdown, no snippet, nothing to reinforce purchase confidence at the moment of decision. The sticky footer ATC partially mitigates scroll friction but doesn't solve the decision paralysis in the buy box.

The most common 1–2 star review theme (10+ of 27 negative reviews) is sizing failure for large calves — "If you have any circulation problem, your legs are probably going to be bigger and these are not for you." The irony is direct: edema, post-surgery, and DVT patients are the primary medical audience, and they statistically have larger legs. The LP addresses this in Reason 5 ("Wide Calf & Women's Sizes Included") but the PDP buy box shows only "Standard/Wide" labels with no calf circumference ranges. Buyers who land on the PDP without reading the LP never see the reassurance. The cart has a well-designed AOV mechanic (progress bar: "ADD 1 PAIR MORE TO UNLOCK 2 FREE PAIRS") but the cart body below the single item is blank — no cross-sell widget renders, so the prompt has no payoff.

## Top Test Opportunities

### 1. PDP Buy Box — Pre-Select 4-Pair Best Value Tier
**What's broken:** On the Compression Socks PDP, the buy box shows three pricing tiers stacked vertically in a radio-button group: "1 Pair — $49.99/pair," "2 Pairs — $37.49/pair (BUY 1 GET 1 50% OFF)," and "4 Pairs — $25.00/pair (BUY 2 GET 2 FREE — BEST VALUE)." The 1-pair option is pre-selected by default. The tiers sit between the size/width selector above and the dark green "ADD TO CART" button below, meaning a visitor must process and choose between three price points before they can add to cart. The "BEST VALUE" label on the 4-pair tier is text-only and carries no visual emphasis — it does not stand out from the other options.
**Evidence:** PDP visual summary (Fold 2), live site fetch
**Key data:** 4-pair bundle at $25/pair vs. 1-pair at $49.99/pair — $50 AOV gap. No CR data available.
**Est. lift:** 8% add-to-cart improvement × [sessions/mo unknown] × $100 AOV = TBD

### 2. PDP Wide-Calf Fit Reassurance in Buy Box
**What's broken:** The width selector in the PDP buy box shows two radio options: "Standard" and "Wide," with a "Width Guide" link. No calf circumference ranges appear adjacent to the selector. No copy addresses the fit concern for buyers with edema or larger legs. The width selector is positioned above the pricing tiers and ATC button but has no supporting context — a buyer with a large calf cannot confirm fit from this page without clicking the Width Guide (a modal or separate page, adding a navigation step).
**Evidence:** 10+ Amazon reviews (1-2 star), LP Reason 5 copy ("Wide Calf & Women's Sizes Included"), PDP visual summary
**Key data:** "If you have any circulation problem, your legs are probably going to be bigger and these are not for you" — Amazon reviewer. Multiple reviews cite XL as too small for calves.
**Est. lift:** 5–10% CR improvement for wide-calf segment + reduction in returns

### 3. Cart Cross-Sell Widget (implement or repair)
**What's broken:** The cart drawer shows a 4-step progress bar at the top with the label "ADD 1 PAIR MORE TO UNLOCK 2 FREE PAIRS" and sock icons for each milestone. Below the single cart item (Compression Socks $49.99, with quantity stepper and Remove link), there is a large blank white area that occupies roughly 40% of the cart drawer height. No product recommendation tiles, complementary SKU suggestions, or bundle prompts render in this space. The checkout footer (Subtotal, Shipping note, Secure Checkout CTA) sits below the blank area.
**Evidence:** Cart visual summary, site-visual-summary.md note: "likely missing implementation"
**Key data:** AOV gap between 1-pair ($49.99) and 4-pair bundle ($100) is $50. Progress bar is present but has no product to act on.
**Est. lift:** 10–15% AOV lift on single-item carts × [sessions/mo unknown]

### 4. Landing Page LCP Optimization (8.4s → under 3s)
**What's broken:** The primary compression landing page (hollowsocks.com/pages/10r-compression-g1) has an LCP of 8.4s and a TTI of 33.2s on mobile (Lighthouse, performance score 42/100). This is the destination URL for all Meta compression ads and Google search ads targeting compression/edema queries. The above-the-fold content includes a full-width hero, announcement bar with countdown timer, author byline image, and a comparison table — likely causing the LCP through unoptimized hero image loading and render-blocking scripts.
**Evidence:** pagespeed.md (LCP 8.4s, TTI 33.2s, performance 42/100)
**Key data:** Google's benchmark: 53% of mobile visitors abandon pages that take over 3s to load. LP LCP is 2.8× that threshold.
**Est. lift:** 10–20% paid traffic conversion recovery × paid session volume × AOV

### 5. PDP Review Snippet Near ATC
**What's broken:** The Compression Socks PDP buy box shows "★★★★★ (6333 REVIEWS)" as a linked line near the product name. No star rating breakdown (5-star %, 1-star %), no review snippet, and no featured quote appear in the buy box or between the pricing tiers and the ATC button. The next review content visible on the page is a pair of UGC video thumbnails in Fold 3, which is below the sticky footer bar and requires scrolling past the spec table.
**Evidence:** PDP visual summary (Fold 1, Fold 3), review pool (strong medical outcome quotes available)
**Key data:** Available high-credibility quote: "After having quadruple heart surgery... my swelling has totally gone away!!" — Joe Stinger. "These are the first compression socks I can actually put on easily." — Joe B.
**Est. lift:** 3–6% CR improvement at ATC × [sessions/mo unknown] × AOV

## Unused Findings

- Google Shopping ad shows 4.0 stars / 28 reviews — far below the 6,383-review corpus on-site. Fixing the Merchant Center feed could improve Shopping CTR at no creative cost.
- Ad 3 LP countdown reads "THIS WEEKEND" on a 4th of July-framed ad — if countdown is static or misconfigured post-holiday, it signals expired urgency to retargeted visitors.
- Amazon buyers who paid full price then saw Buy 2 Get 2 Free promotion appear felt price-burned — a loyalty/early-access email to direct-site past buyers could reduce churn to lower-priced competitors like Clohill ($7/pair in sets).
