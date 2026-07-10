# Tropical Fruit Box Roadmap Seed

**Store:** https://tropicalfruitbox.com/
**AOV:** ~$109 (flagship Taste the Tropics at $109; Create Your Own at $119)
**Monthly sessions:** unknown
**Data sources:** Meta Ads (3 ads + landing pages), Google Ads (Shopping), Site Screenshots (homepage, collection, PDP, cart drawer), PageSpeed Lighthouse (homepage + Best Sellers, 2026-06-23), Customer Reviews (33 reviews, REVIEWS.io, Taste the Tropics Fruit Box), Live site fetch (2026-06-24), Competitor research (Miami Fruit, The Fruit Company, 2026-06-24)

## Key Insights

Two of three active Meta ads (Ads 2 and 3) are built around specific $15-off discount codes — META15 and SWEET15. Neither code appears on the landing page after the click. Ad 2 sends traffic to the Create Your Own PDP ($119) with "Save $15 with code META15" as the sole hook; the PDP shows no code confirmation. Ad 3 sends traffic to Best Sellers with "Use SWEET15 to get $15 OFF" plus a gifting message; the Best Sellers page shows no SWEET15 mention and no gifting angle. Visitors who clicked specifically to redeem an offer arrive with no confirmation it works. This is the highest-certainty conversion leak on the site because the fix is a single banner per page.

Site performance on mobile is at fail-level on both primary pages. Best Sellers (the main paid traffic landing page) records LCP 8.6s, TTI 43.6s, and TBT 330ms. The homepage is worse: LCP 12.0s, TTI 51.6s, TBT 420ms. Google's "Poor" threshold for LCP is 4s; both pages exceed it by 2-3x. Server response is fast (10-20ms), so the bottleneck is JavaScript on the client — chat widget, social proof popup, and app download prompts all load before the product grid is interactive. These scores represent a pre-conversion leak — a percentage of paid traffic bounces before any CRO element can engage them.

Reviews on the flagship product (192 reviews, 4.78 stars) reveal gifting as the dominant use case — multiple reviewers describe giving the box as a gift with strong recipient reactions, referencing fast shipping and gift-appropriate packaging. The pink pineapple is the single most emotional product mentioned. One detailed review specifically called out the fruit identification cards ("so we knew how to cut into the fruits and when they were ripe enough to eat") as the feature that made the exotic experience accessible. This differentiator is absent from every ad, the homepage, and the PDP buy box.

## Top Test Opportunities

### 1. Discount Code Welcome Banner — Best Sellers (SWEET15 traffic)
**What's broken:** The Best Sellers collection page (https://tropicalfruitbox.com/collections/best-sellers) has a single announcement bar at the very top of the page that currently reads "PROMO: 20% OFF $89+" with code PRIME20. When visitors arrive via Meta Ad 3 (which promises "Use SWEET15 to get $15 OFF"), this bar shows no reference to SWEET15. There is no hero banner, no sticky bar, and no in-page callout confirming the discount exists. The page title "Best Sellers" is centered below the nav in a plain serif font on a white background, followed immediately by a sort dropdown and the product grid. The entire page gives no visual acknowledgment that the visitor came with a specific offer in mind.
**Evidence:** Meta Ads visual summary (Ad 3), live site fetch of Best Sellers (2026-06-24)
**Key data:** Ad 3 has been active since Jan 19, 2026 (5+ months of potentially wasted code-motivated traffic); SWEET15 code not visible anywhere on the landing page
**Est. lift:** +8–12% CR on SWEET15 Meta traffic segment × sessions × $109 AOV

### 2. Discount Code Confirmation Banner — Create Your Own PDP (META15 traffic)
**What's broken:** The Create Your Own Tropical Fruit Box PDP at $119 is the landing page for Meta Ad 2, whose entire headline reads "Save $15 with code META15." The buy box on this PDP stacks, from top to bottom: product title, price ($119), size variants (Regular 10lbs / Large 14lbs as two buttons), greeting card selector (6 options in a dropdown), a purchase toggle showing "$119.00 one-time" vs. "$98.10 Subscribe & Save 10%", a quantity stepper, a teal full-width "Add to Cart" button, and a trust badge row (Satisfaction Guarantee, Free Shipping, Premium Quality, A+ Rating). There is no mention of META15 in the announcement bar, in the buy box, or anywhere on the visible page. The announcement bar on this page shows the same general PRIME20 promo as the rest of the site.
**Evidence:** Meta Ads visual summary (Ad 2), site-visual-summary (PDP)
**Key data:** Only 1 review with no written text on this PDP — low social proof at the highest price point on the site; code offer that motivated the click is invisible on arrival
**Est. lift:** +10–15% CR on META15 Meta traffic segment × sessions × $119 AOV

### 3. Occasions-Based Editorial Row on Best Sellers
**What's broken:** The Best Sellers collection page opens with a centered "Best Sellers" title in plain text, a sort dropdown (defaulting to Featured), and a 3-column product grid with 14+ items. There is no filter panel — no way to narrow by price range, fruit type, or occasion. No editorial section divides the grid (e.g., "Great for Gifting" or "Under $100"). Product cards show product name, star rating, and price with struck-through sale pricing; no short descriptor or weight is visible on the card. The gifting angle that drives Ad 3 traffic and the majority of positive reviews finds no expression in the collection layout.
**Evidence:** Site-visual-summary (collection page), reviews (gifting dominant use case), Meta Ad 3 creative (gifting copy)
**Key data:** Multiple reviews describe gift-purchase scenarios; Miami Fruit competitor prices from $147 vs. TFB from $109 — the price advantage is never framed as a gifting value proposition on-site
**Est. lift:** +5–10% CR on Best Sellers traffic × sessions × $109 AOV

### 4. Fruit ID Cards Called Out in PDP Buy Box
**What's broken:** The Taste the Tropics PDP buy box (fold 1) contains: "1 LEFT IN STOCK" scarcity badge, product title, price with strikethrough, size selector, greeting card dropdown, subscribe/save toggle, quantity stepper, Add to Cart, and a trust badge row with four icons (Satisfaction Guarantee, Free Shipping, Premium Quality, A+ Rating). There is no mention of the fruit identification cards physically included in each box. These cards tell customers how to cut each fruit and when it is ripe — a feature that directly addresses the anxiety of ordering exotic fruits for the first time.
**Evidence:** Review (Brian F, 3 years ago: "The identification cards were especially helpful so we knew how to cut into the fruits and when they were ripe enough to eat"), site-visual-summary (PDP — no ID card mention visible)
**Key data:** Feature is physically present in the product but has zero on-site visibility; directly reduces the #1 barrier for first-time exotic fruit buyers
**Est. lift:** +2–4% CR on PDP × sessions × $109 AOV

### 5. Performance Fix — Best Sellers Mobile LCP and TTI
**What's broken:** The Best Sellers collection page renders its first product image (LCP element) at 8.6 seconds on a mobile device emulation. Total Blocking Time is 330ms, indicating the main thread is occupied by JavaScript during this window. The page is not interactive (TTI) for 43.6 seconds after navigation. The product grid, sort controls, and Add to Cart buttons are all non-functional during this window. Server response time is fast (10ms), ruling out hosting issues — the bottleneck is client-side JS execution. Third-party scripts visible on the page (live chat widget, social proof popup, shipping protection widget, loyalty program) are likely candidates for deferral.
**Evidence:** PageSpeed Lighthouse — Best Sellers (2026-06-23, mobile emulation)
**Key data:** LCP 8.6s (Google "Poor" threshold: 4s), TTI 43.6s, TBT 330ms, Performance score 52/100
**Est. lift:** +15–25% bounce rate reduction on mobile paid traffic, proportional revenue uplift (industry benchmark for LCP improvements from ~8s to ~4s)

## Unused Findings

- TropiRewards loyalty program is referenced only at the bottom of the cart drawer. No homepage, collection, or PDP placement. Email capture and repeat purchase conversion candidate.
- Subscribe & Save (10%) is surfaced on PDPs only — not visible on collection cards or as a collection-level callout. Subscription acquisition upstream of the cart could lift LTV.
- Miami Fruit's entry price is $147 vs. Tropical Fruit Box's $109 — a 26% price advantage that is never stated as a competitive value frame in any ad or on-site copy.
