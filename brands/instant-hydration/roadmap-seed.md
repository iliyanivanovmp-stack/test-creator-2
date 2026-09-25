# Instant Hydration Roadmap Seed

**Store:** https://instanthydration.com
**AOV:** unknown (proxy $55.00: two subscription boxes at $27.50, or one box at $55.00 list)
**Monthly sessions:** unknown (lift figures are per 10,000 sessions, illustrative)
**Data sources:** Meta Ad Library (3 ads) and PDP landing folds, Google Ads Transparency, pasted reviews (25), PageSpeed JSON (homepage, PDP, mobile lab 2026-09-24), homepage/Energy+/cart screenshots, live fetch of homepage and PDP (2026-09-24), competitor web search (2026-09-24), last30days-ecom social research (directional)

## Key Insights

Every buy path starts with a disabled button. The PDP shows "0 BOXES SELECTED" until the shopper picks from 15+ flavors, and the Energy+ page shows an inert "SELECT A FLAVOR". Reviewers ask for a shortcut ("this packet is the way to go if you just cannot decide what flavor to get", Variety Pack review) and TikTok creators recommend the variety pack as the entry point. Flavor dominates the sample: about 20 of 25 pasted reviews name a favorite (Strawberry Lemon 7, Luigi's 5).

Paid traffic meets a mismatched, slow page. Ad 1 sells Cotton Candy and ad 3 sells P.O.G., but the PDP announcement bar and gallery lead with Crisp Apple 50% OFF. Ads reference Summer and Spring; Google references a Labor Day promo (Sep 2 to 10, expired). PDP mobile lab data (2026-09-24): performance 45, LCP 9.8 s, weight 8,122 KiB, TBT 790 ms, CLS 0. Homepage: performance 55, LCP 5.4 s.

Value depends on the subscription. Subscribe & Save is $27.50 ($0.92/stick); One Time is $49.50 ($1.65/stick). Third-party search figures put LMNT near $1.50 and Liquid I.V. near $1.56 per serving (unverified). The cart shows $99.00 on the Energy+ line against a $55.00 subtotal with no explanation.

## Top Test Opportunities

### 1. PDP flavor selection and CTA state
**What's broken:** On the premium electrolyte PDP, the right column stacks the Subscribe & Save option (pre-selected, 50% OFF, $27.50, $0.92/stick, perks list) over the One Time option ($49.50, $1.65/stick, red X marks for no bottle, sampler or free shipping). Below it sits "Select Your Hydration": a black "Add Energy+" panel (Sour Green Apple, Tropical Crush with steppers), then a horizontal scroller of flavor cards (Crisp Apple limited flavor, Luigi's Lemon Ice, more cut off), each with "View Label" and a quantity stepper. Under that: DELIVERY "Every 30 Days", SUBTOTAL $0.00, and a disabled button "0 BOXES SELECTED" with "50 Day Happiness Guarantee" beneath. Nothing is selected by default, so the buyer must choose from 15+ flavors before the button activates.
**Evidence:** PDP folds 1 to 2, reviews, social research
**Key data:** "this packet is the way to go if you just cannot decide what flavor to get" (Variety Pack review); TikTok: "Grab the variety pack, which means I can switch"
**Est. lift:** +0.3 pp CR x 10,000 sessions x $55 = $1,650 per 10k sessions (illustrative)

### 2. Ad-to-PDP flavor and offer match
**What's broken:** Ad 1 (Cotton Candy, "IT SOLD OUT FOR A REASON", "Try Risk Free for 50 Days + FREE GIFT") and Ad 3 (P.O.G., Max Holloway, "7x Electrolytes") land on a PDP whose black announcement bar reads "LIMITED TIME FLAVOR: Crisp Apple, 50% OFF + Free Water Bottle with 2+ Box Purchase" and whose first gallery slide repeats that offer. Cotton Candy and P.O.G. are not visible in the first three folds; the flavor scroller is cut off. Ad 2 promises "Up to 50% OFF" spring savings while One Time is only 10% off.
**Evidence:** Meta ads, PDP folds, live fetch (Cotton Candy and P.O.G. exist), Google Ads
**Key data:** All three ads started Sep 10, 2026; ad copy references Summer Sale and Spring; Ads 1 and 2 say 6x electrolytes, Ad 3 says 7x
**Est. lift:** +0.2 pp CR x 10,000 sessions x $55 = $1,100 per 10k sessions (illustrative)

### 3. PDP mobile load speed
**What's broken:** The PDP, which is the sole Meta landing page, loads at mobile performance 45. LCP is 9.8 s, Speed Index 8.9 s, total weight 8,122 KiB, estimated image savings 935 KiB and unused JavaScript 1,051 KiB. CLS is 0 and server response is 20 ms, so the cost is front-end weight. Buy box renders late for paid mobile visitors.
**Evidence:** PageSpeed JSON (lab, 2026-09-24)
**Key data:** Homepage: perf 55, LCP 5.4 s, TBT 660 ms, 6,357 KiB. No field data or desktop run collected.
**Est. lift:** +0.2 pp CR x 10,000 sessions x $55 = $1,100 per 10k sessions (illustrative)

### 4. PDP offer stack clarity
**What's broken:** The PDP describes the free water bottle two ways: as a subscription perk "on first shipment" and via a red bar "FREE WATER BOTTLE WITH 2+ BOXES" plus a gallery slide with the same text. The subscription option also lists a free 3-count sampler and free shipping. The One Time option shows three red X marks. Ad 1 says "FREE GIFT" without naming an item.
**Evidence:** PDP folds 1 to 2, Ad 1, live fetch
**Key data:** Subscribe $27.50 (50% off) vs One Time $49.50 (10% off); Energy+ page shows locked perks "Water Bottle with 2+ Boxes ($34.99 FREE)"
**Est. lift:** +0.2 pp CR x 10,000 sessions x $55 = $1,100 per 10k sessions (illustrative)

### 5. Cart drawer AOV and price consistency
**What's broken:** The "Your Cart" drawer lists a Water Bottle (Black, $34.99 struck, FREE) and Energy+ Sour Green Apple x2, every 30 days, with a $110.00 struck price, $99.00 and "Save $11.00". The subtotal row shows a 50% OFF badge, $110.00 struck and $55.00. The $99.00 line and $55.00 subtotal do not reconcile on screen. A static black "SECURE CHECKOUT" button follows; no upsell, bundle, or free-shipping threshold appears. Under it: "Over 2M+ Orders" and "50 Day Happiness Guarantee". Not re-run live.
**Evidence:** cart-drawer.png
**Key data:** Free bottle unlocks at 2+ boxes
**Est. lift:** +$3 AOV (about 5%) x 10,000 sessions x assumed 3% CR = $900 per 10k sessions (assumption, illustrative)

### 6. Homepage hero and trust strip
**What's broken:** Fold 1 is a full-width red hero for one limited flavor ("CRISP APPLE", cream button "SHOP NOW AND SAVE UP TO 50%") under a black announcement bar. The header shows MENU, logo, SHOP, CART. No star rating, review count, guarantee or shipping copy appears in the three captured folds; no sticky CTA. Fold 2 splits Hydration and Energy+ cards, then a long Energy+ paraxanthine explainer.
**Evidence:** Homepage folds, live fetch
**Key data:** Live copy: "4.5 out of 5", "2 Million+ customer purchases", "50-Day Money-Back Guarantee" exist below the captured folds; live fetch also returned "525,500+ reviews" (likely extraction error, verify)
**Est. lift:** +0.15 pp CR x 10,000 sessions x $55 = $825 per 10k sessions (illustrative)

### 7. Per-flavor social proof in the flavor selector
**What's broken:** The PDP shows a single review card ("Tastes Incredible", Alyssa P., 5 stars) under the gallery. The flavor cards in the selector carry only name, "View Label" and a stepper, with no rating or quote.
**Evidence:** PDP fold 2, reviews
**Key data:** Strawberry Lemon named in 7 of 25 pasted reviews, Luigi's Lemon Italian Ice in 5; reviews carry benefit tags (Increased Energy, Fewer Headaches, Clearer Thinking)
**Est. lift:** +0.15 pp CR x 10,000 sessions x $55 = $825 per 10k sessions (illustrative)

### 8. Energy+ page proof and one-time path
**What's broken:** The dark Energy+ page offers two flavor cards (Sour Green Apple, Tropical Crush) with steppers at 0, a locked perks list, and a button "SELECT A FLAVOR". "TRY IT ONCE" ($49.50) sits below fold 2 with "NO FREE GIFT" and $6.99 shipping. No rating or review count appears in the captured folds. The sticky bar appears only at fold 3.
**Evidence:** Energy+ folds, reviews, social research
**Key data:** 2 of 25 pasted reviews are Energy+; "Love this flavor with an extra boost of energy"
**Est. lift:** +0.15 pp CR x 10,000 sessions x $55 = $825 per 10k sessions (illustrative)

### 9. Price-per-serving framing vs competitors
**What's broken:** The PDP shows $0.92/stick for subscription and $1.65/stick for one-time. Google sitelinks say "Daily Electrolytes < $1.00", true only for subscription. No competitor comparison appears on the PDP folds.
**Evidence:** PDP, Google Ads, competitor search (third-party, unverified)
**Key data:** LMNT about $1.50, Liquid I.V. about $1.56, Ultima about $0.47 per serving
**Est. lift:** +0.1 pp CR x 10,000 sessions x $55 = $550 per 10k sessions (illustrative)

### 10. Taste and salt expectation copy
**What's broken:** No mixing guidance or taste expectation appears near the buy box. Reviewers split: "not too sweet, not too salty" versus one Amazon review ("Super salty!! ... headaches. Not worth the price") and "I think the powders are a bit strong".
**Evidence:** Reviews, Amazon (single item, directional)
**Key data:** Paloma "borderline too sweet"; request for a larger mixing bottle
**Est. lift:** +0.1 pp CR x 10,000 sessions x $55 = $550 per 10k sessions (illustrative)

## Unused Findings

- Google Ads still reference an expired Labor Day promo (Sep 2 to 10); confirm and refresh.
- Flavor count is inconsistent (14 on homepage card, 15 on PDP sticky bar, more in the live list).
- Amazon ratings (4.0 to 4.6) trail on-site 4.5/5; Trustpilot 4.0 from 309 reviews.
- Google sends five landing paths with ingredient claims versus one Meta PDP; needs Google traffic data.
- Client fixes: larger bottle SKU, mix-ratio guide, share star ratings and negative reviews.
