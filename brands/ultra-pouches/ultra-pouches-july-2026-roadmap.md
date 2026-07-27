# Ultra Pouches CRO Research Brief

**Data Sources:** Meta Ads visual summary (Jul 18, 2026), Google Ads visual summary, PageSpeed (Lighthouse mobile, Jul 21, 2026), Reviews (Amazon, Nov 2025-Jul 2026, 60+ reviews), Site visual summary (homepage, PDP, cart), LP live fetch (Jul 21, 2026), Competitor web research (Jul 21, 2026)

---

## Insights

Ultra Pouches has a credential-heavy brand: tech company logos (Sequoia, OpenAI, Goldman Sachs), athlete endorsers (Nate Diaz, Rampage Jackson), and 52,032 self-reported happy customers. The product formula is genuinely differentiated (Enfinity® PX 100mg, L-Theanine, Alpha GPC, Ginseng, B6/B12). The CRO problem is structural friction in the funnel, not brand awareness.

Price is invisible everywhere except the cart. No pricing appears on the homepage, PDP, or landing page at any scroll depth. The first number a buyer sees is $48 struck through to $31.20, revealed in the cart drawer only after configuring flavor selections and adding items. Amazon reviews show price as the dominant reorder objection across multiple high-helpfulness entries: "$1 per pouch is too expensive," "$45 for 3 is a scam," and direct comparisons to Velo ($3-5/can) and Nyz (5 tins/$35) appear across reviews with 20-40 helpful votes each (Source: Amazon Reviews, Nov 2025-Jul 2026). The site resolves this objection at the worst moment: maximum commitment, zero risk coverage, and no guarantee or return policy visible anywhere in the funnel.

All three Meta ad creatives share one landing page (https://takeultra.com/pages/intro-offer-2), and that page loads at LCP 11.1s / TTI 40.4s on mobile, which is 4.4x over Google's 2.5s "good" threshold (Source: PageSpeed, Jul 21, 2026). Paid traffic is abandoning before the above-fold headline renders, which makes every other conversion fix on the LP irrelevant for that share of visitors.

The PDP purchase flow requires 4-6 user decisions before the CTA becomes active. All six flavor steppers default to 0 (CTA disabled on load), the primary CTA sits below the initial viewport, no price is shown, and subscription is presented as the only option with no visible one-time purchase toggle. For a product where roughly half of Amazon reviewers report no perceived effect (Source: Amazon Reviews, multiple high-helpfulness entries), first-time buyer friction is especially costly.

The paid funnel also has a discount integrity problem. The highest-volume Meta creative (Ad 3, 16 active ad variants) shows 35% OFF. The LP floating CTA shows 45% OFF. The LP inline CTA shows 50% OFF. A live fetch surfaced an additional 25% off promotion on the same page. Four different discount numbers across a single ad-to-LP path undermine offer credibility before users read a word of product copy (Source: Meta Ads visual summary, LP live fetch, Jul 21, 2026).

AOV: $31.20 (subscription) / $48.00 (one-time) for a 3-can order. Monthly sessions not collected. Provide Shopify Analytics or GA4 data to complete revenue calculations across all slots.

---

## Slot 1: Google Shopping Price Rendering Fix

**Type:** Immediate Fix
**Page:** Google Shopping (product feed)

**What's broken:** At least one shopping product card in the Google Shopping inventory shows "[Price]" as a literal text placeholder. The dynamic pricing variable is not rendering the product's actual dollar amount. Shopping users use price as a primary filter. A card showing "[Price]" instead of a real number generates near-zero clicks on affected SKUs and risks a Google Merchant Center product disapproval if flagged.

**Fix:** Audit the Google Merchant Center product feed for all active SKUs (Focus Pouches flavor variants + Sleep Pouches Honey Lemon). Identify the broken price field mapping, correct it so all SKUs surface actual pricing, and submit the feed for reprocessing. Verify all product cards show correct prices in the Shopping preview before marking complete.

No A/B test needed. This is a technical defect, not a hypothesis. Fix it and monitor click-through recovery on affected listings.

---

## Slot 2: Landing Page Speed Optimization

**Type:** A/B test (1 variation vs. control)
**Page:** Landing Page (https://takeultra.com/pages/intro-offer-2)
**Revenue potential:** Monthly sessions not collected. Formula: sessions x 7% conservative CR lift x $31.20 sub AOV = monthly revenue gain. This is the highest-priority slot in the roadmap. All paid Meta traffic passes through this page, and the current load time means a material share of clicks abandons before above-fold content is visible.

**Hypothesis:** If we reduce LCP from 11.1s to under 4s on mobile, paid traffic conversion will increase because users will reach the above-fold headline and CTA before the majority of current abandonment occurs.

**Data:** The primary paid landing page (intro-offer-2) scores LCP 11.1s, TTI 40.4s, Performance 47/100 on mobile Lighthouse. Google's "good" LCP threshold is 2.5s. The current page is 4.4x over it. All three Meta creatives, including the highest-volume Ad 3 (16 active ad variants), send to this URL. A 1s LCP improvement is estimated to yield 7-12% CR uplift on mobile commerce (Deloitte, 2020). Source: PageSpeed (Jul 21, 2026), Meta Ads visual summary.

**V1:** Performance-optimized version of the same LP. Changes: compress and lazy-load the hero image and horizontal 4-can product image row; defer non-critical third-party scripts; inline critical CSS for the above-fold headline ("A SMARTER WAY TO FOCUS"), the logo bar, and the two floating CTAs. All existing content preserved with no copy or offer changes. Mobile: above-fold text and CTA render within 3s. Desktop: no visual change.

---

## Slot 3: Price Reveal in PDP Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (https://takeultra.com/products/focus-pouches)
**Revenue potential:** Monthly sessions not collected. Formula: sessions x 5% conservative ATC lift x $31.20 sub AOV = monthly revenue gain.

**Hypothesis:** If we show subscription and one-time pricing directly in the buy box before any cart interaction, add-to-cart rate will increase because users process the price alongside the product rather than experiencing it as a reveal at maximum commitment.

**Data:** No price appears on the PDP at any scroll depth across folds 1-3. Price first surfaces in the cart drawer as $48 struck through to $31.20, only after users add items. Amazon reviews show price is the #1 reorder objection, with multiple 20-40 helpful-vote entries citing "$1/pouch" and "$45 for 3 cans" as reasons for no repeat purchase. A live fetch of the LP also shows the pricing field rendering as "$0.00." Source: Site visual summary, Reviews (Amazon, Nov 2025-Jul 2026), LP live fetch (Jul 21, 2026).

**V1:** Add a two-line price display directly above the "ADD 3 MORE CANS" CTA, visible without scroll on initial page load. Line 1: "Subscribe: $31.20 / 3 cans ($0.69/pouch)" in the brand's primary green. Line 2: "One-time: $48.00 / 3 cans" in muted gray. Position the "GET 45% OFF" savings call-out as a third line, making the discount concrete against a visible base price rather than a floating, context-free badge. Mobile: price block visible in fold 1 or top of fold 2 without scroll. Desktop: price block within the buy box column, above the CTA.

---

## Slot 4: Risk Reversal Near Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page
**Revenue potential:** Monthly sessions not collected. Formula: sessions x 10% conservative first-purchase CR lift x $31.20 sub AOV = monthly revenue gain.

**Hypothesis:** If we add a 30-day money-back guarantee directly below the "ADD 3 MORE CANS" CTA, first-purchase conversion will increase because it reduces the financial risk of committing to a product with documented efficacy variability at a $31-48 price point.

**Data:** No guarantee copy, return policy, or risk-reversal statement appears on the PDP, LP, or cart at any scroll depth. Below the CTA, the only copy is "REFILLS MONTHLY | CANCEL ANYTIME," which addresses subscription exit anxiety, not purchase risk. Multiple Amazon reviews with 20+ helpful votes describe paying $45 and feeling no effect, with no mention of a refund path. Competitors in the supplement category routinely offer 30-90 day guarantees at the point of purchase (Source: competitor research, Jul 21, 2026). Source: Site visual summary, Reviews (Amazon, Nov 2025-Jul 2026), LP live fetch.

**V1:** Replace the "REFILLS MONTHLY | CANCEL ANYTIME" microcopy below the CTA with a three-item trust bar: "30-Day Money-Back Guarantee | Free Shipping | Cancel Anytime." Add a small shield icon before the guarantee text. Mobile: trust bar sits on a single row below the CTA in readable type (14px minimum). Desktop: same layout within the buy box column. All other buy box elements (batch urgency calendar, floating discount pill) remain unchanged.

---

## Slot 5: PDP Default Buy Box Pre-Selection

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page
**Revenue potential:** Monthly sessions not collected. Formula: sessions x 10% conservative ATC lift x $31.20 sub AOV = monthly revenue gain.

**Hypothesis:** If we pre-select a 3-can starter configuration on page load so the CTA is active from first render, add-to-cart rate will increase because users face one decision (confirm or adjust) instead of 4-6 sequential actions before the CTA becomes available.

**Data:** All six flavor quantity steppers (Cool Mint, Wintergreen, Tropical, Watermelon, Blue Razz, Sleep Pouches) default to 0 on page load. The "ADD 3 MORE CANS" CTA is disabled until at least one stepper is non-zero. The CTA is positioned below the initial viewport in fold 2. A new visitor must understand the bundle mechanic, choose flavors, set individual quantities, and scroll to find the CTA before any purchase action is possible. Amazon reviews consistently praise Cool Mint and Wintergreen. Tropical has a recurring off-flavor quality complaint (metallic/baby powder taste on bad batches) across multiple reviews from different months, making it a poor default selection. Source: Site visual summary, Reviews (Amazon, Nov 2025-Jul 2026).

**V1:** On page load, pre-fill stepper values to: Cool Mint 1 / Wintergreen 1 / Watermelon 1 (total: 3 cans). CTA is active on load. Add a "Change flavors" text link below the stepper list for users who want a different configuration. Mobile: pre-filled stepper rows visible in fold 1 without scroll, with the CTA accessible in fold 2. Desktop: values pre-filled in the existing stepper UI with no layout changes.

---

## Slot 6: Discount Number Unification on LP

**Type:** A/B test (1 variation vs. control)
**Page:** Landing Page (https://takeultra.com/pages/intro-offer-2)
**Revenue potential:** Monthly sessions not collected. Formula: sessions x 4% conservative LP CVR lift x $31.20 sub AOV = monthly revenue gain.

**Hypothesis:** If we replace all percentage-based CTAs on the LP with a single, consistent dollar-anchor offer, LP conversion will increase because users see one coherent offer instead of four conflicting discount numbers that signal inauthenticity before they evaluate the product.

**Data:** Ad 3 (highest-volume creative, 16 active ad variants) shows 35% OFF in the creative. The LP floating CTA reads "GET 45% OFF." The LP inline CTA reads "GET 50% OFF + FREE SHIPPING." A live fetch of the LP shows "25% off" and "45% off + FREE SHIPPING" as separate listed promotions on the same page. The LP pricing field renders as "$0.00," so no dollar anchor exists to make any percentage concrete. Source: Meta Ads visual summary, LP live fetch (Jul 21, 2026).

**V1:** Set a single offer across all LP CTAs: "GET YOUR FIRST 3 CANS FOR $31.20." Remove the percentage-based variants (35%, 45%, 50%, 25%) from the floating pill CTA and the inline fold-3 CTA. Fix the $0.00 pricing field to render the correct subscription price. All other LP content and layout unchanged. Mobile: floating CTA and inline CTA text updated; pricing field shows $31.20. Desktop: same changes applied to the equivalent elements.

---

## Slot 7: Subscription vs. One-Time Purchase Toggle

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page
**Revenue potential:** Monthly sessions not collected. Formula: sessions x 7% conservative first-purchase CR lift x $39.60 blended AOV (mid-point of sub/OTP) = monthly revenue gain.

**Hypothesis:** If we add a visible subscription vs. one-time purchase selector in the buy box with subscription pre-selected as the default, first-purchase conversion will increase because hesitant buyers can commit to a single order without feeling locked into a recurring charge on an untested product.

**Data:** No toggle, radio button, or pricing row distinguishing subscription from one-time purchase appears anywhere in the PDP buy box across folds 1-3. The only subscription reference is "REFILLS MONTHLY | CANCEL ANYTIME" below the CTA. The cart drawer confirms the subscription-only default by showing "Every 4 Weeks" under the product name. Amazon reviews cite price as the top reorder objection, indicating buyers completed an initial purchase and chose not to continue, which suggests the subscription commitment is a meaningful first-purchase barrier for efficacy-skeptical buyers. Source: Site visual summary, Reviews (Amazon, Nov 2025-Jul 2026), LP live fetch.

**V1:** Add a two-option purchase type selector above the "SELECT YOUR FLAVORS" label. Option A (pre-selected by default): "Subscribe and Save - $31.20 / 3 cans (45% OFF)" with a highlighted border. Option B: "One-Time Purchase - $48.00 / 3 cans." Displayed as radio buttons or a segmented control. When Option A is active, the CTA reads "ADD 3 CANS + SUBSCRIBE." When Option B is active, the CTA reads "ADD 3 CANS." Mobile: selector full-width between the product title and the flavor list. Desktop: selector in the buy box column above the flavor steppers.

---

## Slot 8: Efficacy Proof Module Near Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page
**Revenue potential:** Monthly sessions not collected. Efficacy messaging near the CTA addresses both first-purchase hesitation and post-purchase disappointment, the two primary drivers of review score decline and LTV erosion. Provide Shopify Analytics data to complete revenue estimate.

**Hypothesis:** If we add a mechanism explanation and efficacy stat directly between the flavor selectors and the "ADD 3 MORE CANS" CTA, first-purchase conversion will increase and post-purchase disappointment will decrease because buyers enter with calibrated expectations about onset timing and effect duration.

**Data:** The PDP buy box shows "52,032 HAPPY CUSTOMERS" and a star rating in fold 1 but contains no explanation of how or when the product works near the purchase area. The "90% saw a significant improvement in their overall focus levels" stat appears in LP fold 3, after the CTA, and is absent from the PDP entirely. The majority of 2-3 star Amazon reviews (multiple with 20-40+ helpful votes) follow a consistent pattern: buyers expected a nicotine-like or caffeine-like sensation, felt no effect, and cite unmet advertising expectations as the reason for low ratings. Source: Amazon Reviews (Nov 2025-Jul 2026), Site visual summary, LP live fetch.

**V1:** Insert a compact proof block between the last flavor stepper row and the "ADD 3 MORE CANS" CTA. The block contains: (1) "90% of customers report improved focus" as a headline stat; (2) "Enfinity® PX starts working in 15 minutes. Effects last 1-2 hours. No crash." as a single-line mechanism description. Text only, no images, in the existing brand type hierarchy. Mobile: block sits between the stepper list and the CTA button, full-width, with sufficient padding to visually separate from both. Desktop: same block within the buy box column.

---

## Future Slot Candidates

1. **LP Headline Message Match** -- Ads 1 and 2 lead with "Flow state. No crash. Ultra isn't energy. It's clarity." The LP hero reads "A SMARTER WAY TO FOCUS," a generic claim that doesn't reflect the specific angle paid traffic was sold on. Testing a headline mirroring the flow-state/clarity framing for Ad 1-2 traffic could improve post-click relevance and LP CVR. Ad 3's masculine identity angle is a significant tone departure from the current LP, making a dedicated variant for Ad 3 traffic a secondary option. Estimated lift: 3-10% LP CVR improvement (VWO/Unbounce headline test range).

2. **Homepage Fold 2 CTA Addition** -- Homepage fold 2 contains the highest-trust social proof on the site (Jane Street, Anduril, Goldman Sachs, Solana, Sequoia logo bar) with no CTA. Users persuaded by the credential logos must scroll through an additional copy block about nicotine risk before reaching the "SHOP NOW" CTA in fold 3. Adding a CTA at the base of fold 2 captures intent at the peak trust moment. Estimated lift: 2-5% homepage-to-PDP improvement.

3. **Cart Trust Signal Addition** -- No guarantee, return policy, or security badge appears in the cart drawer at any visible scroll position. Adding "30-Day Money-Back Guarantee | Secure Checkout" above the "CHECK OUT" CTA addresses purchase risk at the final commit moment. Run after Slot 4 (PDP guarantee) to maintain message consistency across the funnel and avoid contradictory copy if guarantee terms differ by placement.
