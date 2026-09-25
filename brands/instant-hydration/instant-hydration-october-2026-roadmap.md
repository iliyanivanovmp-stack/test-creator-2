# Instant Hydration CRO Research Brief

**Data Sources:** Meta Ad Library (3 ads) and PDP landing folds, Google Ads Transparency, pasted reviews (25), PageSpeed JSON (homepage, PDP, mobile lab 2026-09-24), homepage/Energy+/cart screenshots, live fetch of homepage and PDP (2026-09-24), competitor web search (2026-09-24), last30days-ecom social research (directional, 2026-08-25 to 2026-09-24)

## Insights

Every buy path starts with a disabled button. The PDP shows "0 BOXES SELECTED" until the shopper picks from 15+ flavors, and the Energy+ page shows an inert "SELECT A FLAVOR". Reviewers ask for a shortcut: "this packet is the way to go if you just cannot decide what flavor to get" (Source: Reviews, Variety Pack). TikTok creators recommend the same entry point: "Grab the variety pack, which means I can switch" (Source: Social research, 2026-08-25 to 2026-09-24). The PDP is the single landing page for all three Meta ads, so this friction sits on every paid session.

Paid traffic also meets a mismatched page. Ad 1 sells Cotton Candy and Ad 3 sells P.O.G., but the PDP announcement bar and first gallery slide lead with Crisp Apple 50% OFF (Source: Meta ads, PDP folds). Ad 2 promises "Up to 50% OFF", yet 50% applies to Subscribe & Save only. One Time is 10% off at $49.50 (Source: PDP). All three ads started running Sep 10, 2026.

The page is slow for these visitors. PDP mobile lab performance is 45 with a 9.8 s LCP and 8,122 KiB page weight. Server response is 20 ms and CLS is 0, so the cost is front-end weight (Source: PageSpeed, mobile lab, 2026-09-24). Homepage scores 55 with a 5.4 s LCP.

Flavor is what customers talk about. About 20 of 25 pasted reviews name a favorite, led by Strawberry Lemon (7) and Luigi's Lemon Italian Ice (5) (Source: Reviews). The flavor cards in the selector carry no rating or quote.

Value lives inside the subscription. Subscribe & Save is $27.50 ($0.92/stick). One Time is $49.50 ($1.65/stick) (Source: PDP, live fetch 2026-09-24). The cart capture shows a $99.00 Energy+ line against a $55.00 subtotal with no explanation (Source: cart-drawer screenshot, desktop).

Revenue opportunity: baseline sessions, CR and AOV were not provided. Using a $55.00 AOV proxy, a +0.3 pp CR lift on the PDP is 10,000 sessions x 0.003 x $55 = $1,650 per 10,000 sessions. Figures in this brief are illustrative and scoped to desktop captures and the 2026-09-24 live checks. Mobile layout was not captured.

## Slot 1: PDP Default Flavor Selection

**Type:** A/B test (1 variation vs. control)
**Page:** Premium Electrolyte PDP (https://instanthydration.com/products/premium-electrolyte-drink-mix)
**Revenue potential:** 10,000 sessions x +0.3 pp CR x $55 = $1,650 per 10,000 sessions (illustrative, sessions/mo not provided).

**Hypothesis:** If we pre-select the Variety Pack so the button is active on load, more paid visitors will add to cart because they no longer have to choose from 15+ flavors first.

**Data:** The buy button reads "0 BOXES SELECTED" and stays disabled until a flavor stepper moves, and it sits below the selector. Source: PDP folds 1 to 2. Reviewers say "this packet is the way to go if you just cannot decide what flavor to get." Source: Reviews. A TikTok creator says "Grab the variety pack, which means I can switch." Source: Social research (directional).

**V1:** Variety Pack is pre-selected on load (per the 2026-09-24 live fetch, packs appear in the live flavor list; confirm placement with the client). The button reads "ADD TO CART" with the correct subtotal instead of "0 BOXES SELECTED" and $0.00. Individual flavor cards stay below with steppers so shoppers can swap. Desktop and mobile behave the same: pre-selected pack card first, active button, flavor scroller underneath. (KB: resources/kb/pdp-structure.md)

## Slot 2: Ad-to-PDP Flavor Match

**Type:** A/B test (1 variation vs. control)
**Page:** Premium Electrolyte PDP (https://instanthydration.com/products/premium-electrolyte-drink-mix)
**Revenue potential:** 10,000 Meta Ad 1 and Ad 3 sessions x +0.2 pp CR x $55 = $1,100 per 10,000 sessions (illustrative).

**Hypothesis:** If Cotton Candy and P.O.G. visitors see their own flavor and offer first, more will add to cart because the page confirms the ad promise.

**Data:** Ad 1 ("IT SOLD OUT FOR A REASON", Cotton Candy) and Ad 3 ("POG IS BACK. DON'T WAIT.") land on a PDP whose black bar reads "LIMITED TIME FLAVOR: Crisp Apple, 50% OFF + Free Water Bottle with 2+ Box Purchase". Source: Meta ads, PDP folds. Cotton Candy and P.O.G. are not visible in folds 1 to 3, though the live fetch confirms both exist. Source: Live fetch, 2026-09-24. All three ads started Sep 10, 2026 and reference Summer and Spring. Source: Meta Ad Library.

**V1:** For traffic from Ad 1 and Ad 3, the announcement bar and the first gallery slide name the ad's flavor (Cotton Candy or P.O.G.) in place of Crisp Apple. That flavor's card moves to the front of the flavor scroller. The offer terms stay as they are on the live page. Desktop and mobile follow the same order: bar, gallery slide 1, first flavor card. Non-Meta traffic sees the control.

## Slot 3: PDP Free Gift Clarity

**Type:** A/B test (1 variation vs. control)
**Page:** Premium Electrolyte PDP (https://instanthydration.com/products/premium-electrolyte-drink-mix)
**Revenue potential:** 10,000 sessions x +0.2 pp CR x $55 = $1,100 per 10,000 sessions (illustrative).

**Hypothesis:** If the free water bottle is explained once, in the buy box, shoppers will understand what they get and convert more because the two current conditions no longer compete.

**Data:** The bottle appears as a subscription perk "on first shipment" and again in a red bar and gallery slide as "FREE WATER BOTTLE WITH 2+ BOXES". Source: PDP folds 1 to 2. Subscribe & Save also lists a free 3-count sampler and free shipping, and One Time shows three red X marks. Source: PDP. Ad 1 says "FREE GIFT" without naming an item. Source: Meta ad 1. The Energy+ page shows the bottle at "$34.99 FREE". Source: Energy+ folds.

**V1:** Remove the duplicate bottle messaging from the red bar and gallery slide. In the buy box, list the bottle as one perk line with its value ("Water Bottle, $34.99 value") and its single true condition. Confirm that condition with the client before build. Desktop shows the perk list beside the gallery. Mobile shows the same list directly under the option prices.

## Slot 4: Cart Drawer Free Bottle Progress Bar

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (opens from any add to cart)
**Revenue potential:** 10,000 sessions x 3% assumed CR x $3 AOV lift = $900 per 10,000 sessions (assumption, illustrative).

**Hypothesis:** If the cart shows how close a one-box order is to the free bottle, more shoppers will add a second box and see one consistent price because the incentive and the total are both visible.

**Data:** The free bottle unlocks at 2+ boxes. Source: PDP, Energy+ page, cart-drawer screenshot. The cart lists no upsell, bundle or threshold. Source: Cart-drawer screenshot (desktop). The Energy+ line shows $110.00 struck and $99.00 (Save $11.00) while the subtotal shows 50% OFF, $110.00 struck and $55.00. The two figures do not reconcile on screen. The live cart was not re-run, so confirm the cause first. If it is a display bug, fix it before the test.

**V1:** When the cart holds one box, a progress bar at the top of the drawer reads "Add 1 more box to unlock your free Water Bottle ($34.99 value)". Each line item shows the same per-box price the subtotal uses. The bar disappears at 2+ boxes. Desktop places the bar above the line items in the drawer. Mobile keeps it pinned above the line items at full width. (KB: resources/kb/cro-system.md)

## Slot 5: Homepage Hero Trust Strip

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://instanthydration.com)
**Revenue potential:** 10,000 sessions x +0.15 pp CR x $55 = $825 per 10,000 sessions (illustrative).

**Hypothesis:** If cold visitors see rating, purchase count and guarantee under the hero and have a path to the core line, more will click through to a product page because proof appears before the ask.

**Data:** Fold 1 is a full-width red hero for one limited flavor ("CRISP APPLE", "SHOP NOW AND SAVE UP TO 50%"). No star rating, review count or guarantee appears in the three captured folds, and there is no sticky CTA. Source: Homepage folds (desktop). Live copy includes "4.5 out of 5", "2 Million+ customer purchases" and "50-Day Money-Back Guarantee" below those folds. Source: Live fetch, 2026-09-24.

**V1:** Add a one-line strip directly under the hero: "4.5 out of 5", "2 Million+ customer purchases", "50-Day Money-Back Guarantee". Add a secondary text link "Shop all Hydration flavors" beside the hero button. The review count is excluded until the 525,500+ vs 25,000+ conflict is verified. Desktop shows the strip as one row. Mobile stacks it as three short lines under the hero button.

## Slot 6: Per-Flavor Proof in the PDP Selector

**Type:** A/B test (1 variation vs. control)
**Page:** Premium Electrolyte PDP (https://instanthydration.com/products/premium-electrolyte-drink-mix)
**Revenue potential:** 10,000 sessions x +0.15 pp CR x $55 = $825 per 10,000 sessions (illustrative).

**Hypothesis:** If flavor cards show what customers say about them, shoppers will pick faster and convert more because they stop choosing blind.

**Data:** Strawberry Lemon is named in 7 of 25 pasted reviews and Luigi's Lemon Italian Ice in 5. Source: Reviews (small sample, no star ratings). The PDP shows one review card ("Tastes Incredible", Alyssa P.) and the flavor cards carry only name, "View Label" and a stepper. Source: PDP fold 2.

**V1:** Strawberry Lemon and Luigi's Lemon Italian Ice move to the front of the scroller with a "Customer favorite" badge and a one-line verified buyer quote taken from the review set. Confirm badge eligibility against the client's full review data before launch. Desktop shows the quote under the flavor name. Mobile shows the badge on the card and the quote on a second line.

## Slot 7: Energy+ Buy Box Proof and One-Time Path

**Type:** A/B test (1 variation vs. control)
**Page:** Energy+ page (https://instanthydration.com/products/energy-electrolyte-drink-mix)
**Revenue potential:** 10,000 sessions x +0.15 pp CR x $55 = $825 per 10,000 sessions (illustrative).

**Hypothesis:** If the Energy+ buy box shows proof and the one-time option next to the button, more visitors will start an order because the new, science-heavy product feels safer.

**Data:** The page has two flavor cards (Sour Green Apple, Tropical Crush) at 0, a locked perks list and an inert "SELECT A FLAVOR" button. No rating or review count appears in the captured folds. "TRY IT ONCE" ($49.50, "NO FREE GIFT", $6.99 shipping) sits below fold 2. Source: Energy+ folds (desktop). 2 of 25 pasted reviews are Energy+, for example "Love this flavor with an extra boost of energy." Source: Reviews. "Over 2M+ Orders" and "50 Day Happiness Guarantee" appear in the cart drawer. Source: Cart-drawer screenshot.

**V1:** Under the "SELECT A FLAVOR" button, add "50 Day Happiness Guarantee" and "Over 2M+ Orders" labeled as Instant Hydration orders, plus the verified Energy+ quote above. Move "TRY IT ONCE" into the buy box directly beneath the subscription option. Desktop places both in the right column above fold 2. Mobile places them directly under the flavor cards.

## Slot 8: PDP One Time to Subscribe Switch Line

**Type:** A/B test (1 variation vs. control)
**Page:** Premium Electrolyte PDP (https://instanthydration.com/products/premium-electrolyte-drink-mix)
**Revenue potential:** 10,000 sessions x +0.1 pp CR x $55 = $550 per 10,000 sessions (illustrative).

**Hypothesis:** If the One Time option shows what the same box costs on subscription, more shoppers will convert or switch because the per-stick gap is visible at the point of choice.

**Data:** Subscribe & Save is $27.50 ($0.92/stick) and One Time is $49.50 ($1.65/stick), a $22.00 gap per box. Source: PDP, live fetch 2026-09-24. Google sitelinks say "Daily Electrolytes < $1.00", which holds only for subscription. Source: Google Ads. Third-party figures put LMNT near $1.50 and Liquid I.V. near $1.56 per serving, unverified, so this test does not use them. Source: Competitor search.

**V1:** Under the One Time price, add a tappable line: "Subscribe & Save: $0.92/stick, save $22.00 per box". Tapping selects Subscribe & Save. Desktop shows the line under the One Time price. Mobile shows the same line, full-width and tappable. (KB: resources/kb/pdp-structure.md)

## Future Slot Candidates

1. **PDP mobile load speed** - Mobile LCP is 9.8 s and page weight 8,122 KiB (PageSpeed, mobile lab, 2026-09-24). This is a dev or theme fix, so ship it outside the test slots.
2. **Taste and salt expectation copy** - Reviews split between "not too sweet, not too salty" and one Amazon report of "Super salty!!" plus headaches. Test a taste and mix note near the buy box once the client confirms a mix ratio.
3. **Price-per-serving comparison vs. competitors** - Subscription at $0.92/stick sits below the LMNT and Liquid I.V. figures. Needs verified competitor prices before it goes on the page.
4. **Google landing consolidation** - Google sends five landing paths with ingredient claims, Meta sends one. Needs Google-side traffic data.
5. **Expired promo cleanup** - Google Ads still reference a Labor Day promo (valid Sep 2 to 10). Confirm with the client and refresh. This is a fix, not a test.
6. **Flavor count and review count consistency** - Homepage says 14 flavors, PDP says 15, and the live list shows more. The live fetch also returned "525,500+ reviews" against "25,000+" on the PDP. Verify in a browser and standardize.
