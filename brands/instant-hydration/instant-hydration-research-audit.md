# Instant Hydration CRO Research Audit

Audit date: 2026-09-24. All screenshots are desktop only. Live checks were text fetches of the homepage and PDP on 2026-09-24. Cart behavior could not be re-run live (no add-to-cart in this environment), so cart findings are capture-sourced.

## Data Sources Used

User-provided: Meta Ad Library screenshots (3 ads, all "Started running Sep 10, 2026") plus shared PDP landing folds; Google Ads Transparency screenshots (24 tiles); pasted reviews (25 entries, no star ratings); PageSpeed JSON for homepage and PDP (mobile, fetched 2026-09-24); homepage, Energy+ page and cart-drawer screenshots.

Self-researched: live text fetch of homepage and PDP (2026-09-24); last30days-ecom social research (window 2026-08-25 to 2026-09-24, directional); web search for competitor pricing (2026-09-24).

## Source Findings

### Meta Ads & Landing Pages

All three ads send traffic to one PDP (premium-electrolyte-drink-mix). Each ad promises something the PDP folds do not lead with.

| Ad | Promise | What the PDP shows |
|---|---|---|
| 1 | "IT SOLD OUT FOR A REASON", Cotton Candy is back, Summer Sale, "50 Days Risk Free + FREE GIFT" | Announcement bar and hero gallery slide push Crisp Apple 50% OFF. Cotton Candy not visible in captured folds 1 to 3. Live fetch confirms Cotton Candy exists in the flavor list. |
| 2 | "OUR BIGGEST DISCOUNT EVER", Up to 50% OFF, early spring framing | 50% applies to Subscribe & Save only. One Time is 10% off ($49.50). Spring framing absent. |
| 3 | "POG IS BACK. DON'T WAIT.", Max Holloway partnership, "7x Electrolytes" | P.O.G. not visible in captured folds (scroller cut off). Live fetch lists P.O.G. as available. Holloway not on the LP folds. |

Other observations:
- Seasonal framing is stale against the live site: ads say Summer and Spring, site says Crisp Apple 50% OFF (all three ads started Sep 10, 2026).
- Ads 1 and 2 say "6x Electrolytes", Ad 3 says "7x Electrolytes". The PDP says "1 Stick = 1,240 mg of Electrolytes". Three different claim framings.
- "FREE GIFT" (Ad 1) maps to two different LP perks with different conditions (see PDP below).
- Ad 1 promises "50 Days Risk Free". On the PDP the 50 Day Happiness Guarantee sits below the disabled CTA (fold 2), not near the price.

### Google Ads

Source: Transparency Center, 24 tiles, advertiser Instant Hydration Inc. Capture date not confirmed.

- Google leads with ingredients and claims: "Real Hydration. No Junk", "3x The Minerals With 0 Sugar", "French Gray Sea Salt", "Nothing Artificial. Ever", "Scientifically Better Than Other Electrolyte Brands". Meta leads with flavor drops and discounts. Two different value propositions reach the same PDP for Meta and five different destination paths for Google (/premium/ingredients, /better/hyrdation, /premium/electrolytes, /electrolyte/powder, root).
- Sitelink "Daily Electrolytes < $1.00" and "Every stick under $1.00 with 50% off of subscription" match the PDP only for subscription ($0.92/stick). One-time is $1.65/stick.
- Promotion extension "Labor Day - 50% off Subscription Orders, Valid Sep 2 - Sep 10" is expired as of 2026-09-24. Whether it still serves is unknown.
- Comparison claim ("Scientifically Better Than Other Electrolyte Brands") is not evidenced in the captured PDP folds. The site does publish comparison blog posts (for example instanthydration.com/blogs/science/instant-hydration-vs-lmnt).

### Reviews & UGC

Source: 25 pasted product reviews (all "Verified buyer", 2 to 3 days old at paste time, no star ratings). 19 Premium Electrolyte Drink Mix, 3 Variety Pack, 2 Energy+ Sour Green Apple, 1 Water Bottle. Treat as a small sample.

#### What Customers Love

- Flavor is the dominant theme (about 20 of 25 mention a favorite flavor). Named: Strawberry Lemon (7 entries), Luigi's Lemon Italian Ice (5), Mango Pineapple (3), Paloma (2), Cherry Limeade (2).
- Not overly sweet or salty: "Love that this product is not sickly sweet like so many other hydration drinks", "Taste is true to form, not too sweet, not too salty!"
- Habit formation: "turned a task (getting enough water down first thing in the AM) into something I truly look forward to every morning."
- Benefit tags used by reviewers: Increased Energy, Fewer Headaches, Clearer Thinking, Immunity, Workout Recovery, Healthier Skin.
- Variety pack solves indecision: "this packet is the way to go if you just cannot decide what flavor to get."
- Discovery via creators: "I actually found Instant Hydration because of Shawn Johnson's Instagram."
- Energy+: "Love this flavor with an extra boost of energy."
- Water bottle praised: "Thick sturdy glass with a nice heavy lid", "love, love, love the glass water bottle."

#### What Frustrates Customers

- Bottle size: "I just wish the mixing bottle was larger. I think the powders are a bit strong."
- Sweetness on one flavor: Paloma "borderline too sweet for me."
- From Amazon (last30days-ecom, directional): "Super salty!! ... After drinking I would also get headaches. Not worth the price."
- Trustpilot (309 reviews, 4.0 TrustScore, 2026-09-23): the summary text was truncated before the complaint themes, so complaint themes are not verified.

#### Client-Actionable Insights

- Publish a "mix ratio and bottle size" guide (one stick per 16 to 20 oz is my suggestion, confirm with the client's label) to preempt "too strong/salty" feedback.
- Bottle offer is a loved item. Consider a larger bottle SKU as the free gift.
- Review widget shows benefit tags and flavor per review. Confirm it can filter by flavor for on-page use.
- Ask the client for star ratings and 1 to 3 star reviews. The pasted sample contains none, so negative themes are underrepresented.

### PageSpeed / Core Web Vitals

Source: raw PageSpeed JSON, mobile lab run, fetched 2026-09-24. No field (CrUX) data in the files. Desktop not collected.

| Page | Perf | FCP | LCP | TBT | CLS | Speed Index | TTI | Weight |
|---|---|---|---|---|---|---|---|---|
| Homepage | 55 | 2.3 s | 5.4 s | 660 ms | 0.017 | 6.1 s | 37.5 s | 6,357 KiB |
| PDP | 45 | 2.4 s | 9.8 s | 790 ms | 0 | 8.9 s | 40.9 s | 8,122 KiB |

- PDP LCP of 9.8 s is far past the 2.5 s "good" threshold. It is the paid landing page for all Meta traffic.
- Unused JavaScript est. savings: 1,197 KiB (home), 1,051 KiB (PDP). Bootup time 3.8 s and 4.6 s.
- PDP image delivery est. savings: 935 KiB.
- CLS is fine on both. Server response is fast (10 to 20 ms), so the problem is front-end weight, not hosting.
- Energy+ page not tested.

### Competitor Analysis

Research date 2026-09-24 via web search (third-party blogs, not verified against brand sites). No competitor data was provided by the user. Verify prices before client use.

| Brand | Price per serving (per search results) | Sugar | Note |
|---|---|---|---|
| Instant Hydration | $0.92 subscription, $1.65 one-time (live PDP) | Zero | 470 mg potassium, 100 mg magnesium, 10 calories per stick (live PDP) |
| LMNT | about $1.50 per packet | None | 1,000 mg sodium per serving |
| Liquid I.V. | about $1.56 retail (about $1.00 at Costco) | 11 g (original), sugar-free version exists | 520 mg sodium, 370 mg potassium |
| Ultima Replenisher | about $0.47 (90-serving tub) | None | 55 mg sodium |

Takeaway: one-time $1.65 is priced above LMNT and Liquid I.V. per the search figures, while subscription $0.92 undercuts both. The site's real price advantage exists only inside the subscription. Ultima is the value threat. Sources: treelinereview.com, thebalancednutritionist.com, shopsmartlivingfinds.com, doineedelectrolytes.com. Also electrolytedaily.com publishes IH vs Nectar and IH vs DripDrop comparisons (formula and cost), unverified.

### Emails

Not collected. Gap.

### Inspiration Sites

Not collected.

### Non-Data Context

Not collected. Manifest states: no collection page; Energy+ page stands in as the third key page; 8 slots, 0 dev slots; 1 variation vs control.

### Social & Community Research

Directional (last30days-ecom, 2026-08-25 to 2026-09-24). Reddit, X and Pinterest returned no brand results.

- Trustpilot 4.0 (309 reviews) and Amazon listings at 4.0 to 4.6 out of 5 (for example Lemon Lime 4.6 with 576 ratings, Variety Pack 12 sticks 4.0 with 544 ratings, Raspberry 30 sticks 4.2 with 513 ratings). Amazon ratings run lower than the on-site "4.5/5". Standalone, not corroborated by the pasted reviews (which have no ratings).
- TikTok creators promote taste and flavor novelty (Luigi's Lemon Italian Ice tastes "just like the water ice"), and Energy+ as "goodbye energy drinks". Corroborated by first-party reviews: Luigi's and flavor dominate the pasted reviews.
- Variety pack recommended as the starting point on TikTok ("grab the variety pack, which means I can switch"). Corroborated by the pasted "Cannot decide" variety pack review.
- One Amazon review reports saltiness and headaches. Single item, unconfirmed.
- A YouTube podcast (2025-12-24, Operators Podcast) discusses the brand's affiliate-driven growth. Not relevant to conversion.

### Current Site Screenshots

**Homepage.** Full-width red hero sells one limited flavor (Crisp Apple), not the core line. Hero CTA "SHOP NOW AND SAVE UP TO 50%" is the only CTA in fold 1. No star rating, review count or guarantee visible in the three captured folds, and no sticky CTA. The live fetch shows rating and purchase counts exist somewhere on the page, so they sit below the captured folds. Live copy shows "14 delicious flavors" on the card while the PDP says "SELECT FROM 15 FLAVORS" and the live flavor list contains more than 15 entries (Energy+ and packs included). The live fetch returned "525,500+ reviews", which conflicts with "25,000+ Reviews" on the PDP. Likely an extraction error, verify in browser. Homepage then splits into Hydration vs Energy+ cards and a long Energy+ education block before any Hydration proof.

**Energy+ page (collection substitute).** Only two flavors (Sour Green Apple, Tropical Crush) with steppers at 0. Primary button reads "SELECT A FLAVOR" and is inert until a stepper moves. "TRY IT ONCE" is below fold 2 with "NO FREE GIFT" and $6.99 shipping. Locked perks list is a strong mechanic ("SELECT A FLAVOR TO UNLOCK"). No rating or review count in the captured folds. Product is new and science-heavy (paraxanthine). Sticky bar appears only at fold 3.

**PDP.** Buy box stacks Subscribe & Save (pre-selected, $27.50, $0.92/stick) over One Time ($49.50, $1.65/stick) with red X marks on three missing perks. Below it the flavor selector: an "Add Energy+" panel first, then a scroller of flavor cards with steppers. The purchase button reads "0 BOXES SELECTED" and is disabled until a flavor is chosen. It only appears below the selector, so the buyer scrolls past 15+ flavor choices before the buy action. Only one review card is shown (left, under the gallery). The guarantee sits under the button. Sticky bar (fold 3) carries 4.5/5, 25k+ reviews, 2M+ orders and "SELECT FROM 15 FLAVORS". Free bottle appears with two conditions: "on first shipment" (subscription perk) and "with 2+ boxes" (red bar and gallery slide). Mobile behavior not captured.

**Cart drawer.** Two lines: free water bottle ($34.99 struck, FREE) and Energy+ Sour Green Apple x2 subscription. The Energy+ line shows $110.00 struck and $99.00 (Save $11.00) while the subtotal shows 50% OFF, $110.00 struck, $55.00. The $99.00 vs $55.00 gap is unexplained on screen and could read as a pricing error. No upsell, cross-sell, bundle or free-shipping threshold. Trust: "Over 2M+ Orders" and "50 Day Happiness Guarantee" under the checkout button. Live cart could not be rerun.

## Cross-Source Themes

1. **Choice friction before purchase (Meta, PDP, Energy+, reviews, social).** Every buy path starts with a disabled button and a flavor picker of 15+ options. Reviewers ask for the variety pack ("Cannot decide") and creators recommend it as the entry point. Highest revenue impact because it sits on the single page all paid traffic lands on.
2. **Ad promise vs landing delivery (Meta, Google, PDP).** Flavor-specific ads (Cotton Candy, P.O.G.) land on a Crisp Apple-led PDP. Seasonal claims (Summer, Spring, Labor Day) do not match the live offer. Google sends five paths with ingredient claims, Meta sends one with flavor and discount claims.
3. **Slow, heavy paid landing page (PageSpeed, PDP).** Mobile LCP 9.8 s and 8.1 MB on the PDP. Affects all paid sessions before any CRO change can pay off. Desktop screenshots only, so mobile impact on layout is unverified.

## Top Test Opportunities

Ranked by evidence strength x revenue potential x fixability. Lift math is illustrative: baseline CR, sessions/mo and AOV were not provided. AOV proxy is $55.00 (two subscription boxes at $27.50, or one box at the $55.00 list price). Figures are per 10,000 sessions, not monthly.

1. **PDP flavor selection and CTA state**: The buy button is disabled ("0 BOXES SELECTED") until the shopper picks from 15+ flavors, and the button sits below the selector. Cost: choice paralysis on the page all paid traffic lands on. Evidence: PDP folds 1 to 2, reviews ("Cannot decide"), social (variety pack recommendations). Est. lift: +0.3 pp CR x 10,000 sessions x $55 = $1,650 per 10k sessions (illustrative). Strongest example inside this test: pre-selecting the Variety Pack with an active CTA.
2. **Ad-to-PDP flavor and offer match**: Cotton Candy and P.O.G. ads land on a Crisp Apple-led PDP, and ad seasons (Summer, Spring) do not match the live offer. Cost: scent break for flavor-specific traffic. Evidence: Meta ads, PDP folds, live fetch, Google Ads. Est. lift: +0.2 pp x 10,000 x $55 = $1,100 per 10k sessions (illustrative).
3. **PDP mobile load speed**: PDP mobile LCP is 9.8 s, weight 8,122 KiB, performance 45. Cost: paid visitors bounce before the buy box renders. Evidence: PageSpeed JSON (lab, 2026-09-24). Est. lift: +0.2 pp x 10,000 x $55 = $1,100 per 10k sessions (illustrative). Needs a dev or theme change, so check slot fit.
4. **PDP offer stack clarity**: The free water bottle is described as "on first shipment" (subscription) and "with 2+ boxes" (red bar, gallery slide). One-time shows three red X marks and 10% off, and Ad 1 says "FREE GIFT" without naming it. Cost: unclear what the shopper gets. Evidence: PDP folds 1 to 2, Ad 1, live fetch. Est. lift: +0.2 pp x 10,000 x $55 = $1,100 per 10k sessions (illustrative).
5. **Cart drawer AOV and price consistency**: Cart shows $99.00 line vs $55.00 subtotal with no explanation, and no upsell or threshold. Cost: pricing doubt at checkout entry and no AOV lever. Evidence: cart-drawer.png (live rerun not possible). Est. lift: +$3 AOV (5%) x 10,000 sessions x assumed 3% CR = $900 per 10k sessions (assumption, illustrative). Strongest example: a progress bar to the 2-box free-bottle unlock.
6. **Homepage hero and trust strip**: The hero sells one limited flavor to all traffic, and no rating, review count or guarantee appears in the three captured folds. Cost: cold visitors get no proof or core-product path. Evidence: homepage folds, live fetch. Est. lift: +0.15 pp x 10,000 x $55 = $825 per 10k sessions (illustrative).
7. **Per-flavor social proof in the flavor selector**: The PDP shows one review card while reviewers name flavors and benefits. Flavor cards carry no rating or quote. Cost: shoppers choose blind among 15. Evidence: reviews (Strawberry Lemon 7 of 25, Luigi's 5 of 25), PDP fold 2. Est. lift: +0.15 pp x 10,000 x $55 = $825 per 10k sessions (illustrative). Overlaps test 1 in location, differs in mechanic (proof vs default).
8. **Energy+ page proof and one-time path**: No rating or reviews in captured folds, inert "SELECT A FLAVOR" button, "TRY IT ONCE" below fold 2. Cost: new, science-heavy product with no visible proof. Evidence: Energy+ folds, reviews (2 Energy+ entries), social. Est. lift: +0.15 pp x 10,000 x $55 = $825 per 10k sessions (illustrative).
9. **Price-per-serving framing vs competitors**: The site headlines $0.92/stick (subscription) and $1.65 one-time. Per search figures LMNT is about $1.50 and Liquid I.V. about $1.56. Cost: one-time buyers compare and see a premium. Evidence: PDP, Google sitelinks, competitor search (third-party, unverified). Est. lift: +0.1 pp x 10,000 x $55 = $550 per 10k sessions (illustrative).
10. **Taste and salt expectation copy**: Reviewers say "not too salty" (several) while one Amazon reviewer reports "super salty" and headaches, and one asks for a bigger bottle. Cost: first-order regret and refunds under a 50-day guarantee. Evidence: reviews, Amazon (single item, directional). Est. lift: +0.1 pp x 10,000 x $55 = $550 per 10k sessions (illustrative).

## Unused but Valuable Findings

- Google Ads still reference an expired Labor Day promo (Sep 2 to 10); confirm with the client and refresh.
- Homepage says "14 flavors", PDP "15 flavors", live list shows more; standardize the count.
- Live fetch showed "525,500+ reviews" on the homepage vs "25,000+" on the PDP; verify in a browser.
- Amazon ratings (4.0 to 4.6) trail the on-site 4.5/5; consider the trust mismatch if shoppers cross-check.
- Google ads send five different landing paths; a landing consolidation test needs Google-side traffic data.

## Missing Data

- No mobile screenshots. Mobile is where the PDP performs worst (LCP 9.8 s) and layout claims are unverified.
- No separate PDP fold captures; the Meta landing folds stand in.
- Energy+ page not run through PageSpeed.
- No traffic, CR or AOV data. Lift figures are illustrative per 10,000 sessions.
- No star ratings or negative reviews in the pasted sample; Trustpilot complaint themes were truncated.
- No emails, no user competitor list, no non-data context.
- Cart not re-run live; $99 vs $55 discrepancy unexplained.
