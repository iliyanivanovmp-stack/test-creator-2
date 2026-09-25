# Baked Bags Roadmap Seed

**Store:** https://www.bakedbags.com/
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency Center, PageSpeed / Core Web Vitals, Current Site Screenshots, Reviews & UGC, Competitor Analysis (self-researched)

## Key Insights

Site speed is the single largest, best-evidenced problem in the funnel. Lighthouse mobile data (2026-08-21) shows the PDP loading with an 18.5s LCP and a 53.3s Time to Interactive; the homepage isn't far behind at 8.1s LCP and 49.2s TTI. Performance scores sit at 0.34 (homepage) and 0.39 (PDP). Every dollar spent on Meta and Google ads is landing traffic on pages that take the better part of a minute to become tappable on mobile.

Message match breaks down between Meta Ad 1/2 and their landing page. Both ads sell a subscription/rewards program ("Subscribe and unlock 10+ tiers of free gifts, surprise rewards and exclusive perks"), but bakedbags.life/packs/ never mentions subscription in any of the three folds captured, and the PDP buy box for the same CONED product line shows only one-time purchase plus quantity-based Bundle & Save — no subscribe-and-save option. Competitor Delta Munchies has a live subscription flow (15% off, free shipping, pause/edit anytime). Ad 3, by contrast, shows strong match: "Save 33% on Cones Variety Packs. 4 flavors for $39.99" lands on a page headlined "SAVE 33% ON THE CONES STARTER PACK."

Reviews surface two actionable, non-obvious signals. Customers organically pair CONED products with real ice cream — an unprompted pattern across at least three of 20 reviews ("put it in my ice cream and it hit like no other" — Dae S.) — that appears nowhere in ad or PDP content. Separately, one verified reviewer over-consumed because serving-size wasn't clear at the point of purchase ("The serving size said 1, so I ate an entire cone and was zonked for the rest of the day" — Robert Y.), despite the buy box already showing "Two 25MG THC Cones Per Bag" and "200 MG THC Total" as bullets.

## Top Test Opportunities

### 1. PDP Core Web Vitals Emergency Fix
**What's broken:** The Coned Variety Pack PDP (extra-strength-variety-pack-edibles-800mg) loads with an 18.5s LCP, 690ms TBT, and 53.3s Time to Interactive on mobile Lighthouse. A visitor from a paid ad lands on the buy box — star rating and customer count at top, then price ($60.00 struck to $39.99), three benefit bullets, a 7-option flavor selector defaulted to Variety Pack — and can tap Add to Cart with no visible response for the better part of a minute.
**Evidence:** PageSpeed (bakedbags-pdp-speedtest.json)
**Key data:** Performance score 0.39, LCP 18.5s, TTI 53.3s, CLS 0.002
**Est. lift:** Not calculable — sessions/AOV not provided. Treat as top priority given severity relative to Google's 2.5s "good" LCP threshold (~7x over).

### 2. Homepage Core Web Vitals Fix
**What's broken:** The homepage hero — headline "THE LEADING CAUSE OF RED EYES" below a running federal-ban countdown banner, "SHOP LEGAL THC" CTA, star rating/customer-count line, then a press-logo row — loads with an 8.1s LCP and 49.2s Time to Interactive on mobile.
**Evidence:** PageSpeed (bakedbags-homepage-speedtest.json)
**Key data:** Performance score 0.34, LCP 8.1s, CLS 0.153, TBT 790ms
**Est. lift:** Not calculable — sessions/AOV not provided.

### 3. Close the Subscription Message-Match Gap
**What's broken:** Meta Ad 1 and Ad 2 (running since Jul 19 and Jul 22, 2026) both drive to bakedbags.life/packs/, promising "10+ tiers of free gifts, surprise rewards and exclusive perks" for subscribing. The landing page hero instead reads "VARIETY PACKS UP TO 50% OFF" with no subscription mention in any of the three folds captured. The PDP buy box for the same product line shows one purchase option per flavor (one-time) plus a 1x/2x/3x quantity Bundle & Save tier selector — no subscribe-and-save toggle anywhere.
**Evidence:** Meta ads visual summary, live WebFetch of bakedbags.life/packs/, PDP screenshots, competitor research
**Key data:** Delta Munchies (direct competitor) has a live subscription flow: 15% off every order, free shipping, pause/edit anytime
**Est. lift:** Not calculable — sessions/AOV not provided.

### 4. Serving-Size / Dosing Clarity in Buy Box
**What's broken:** PDP fold 1 buy box lists three checkmark bullets ("Two 25MG THC Cones Per Bag," "4 Different Flavors," "200 MG THC Total") directly under the price, but none explicitly states "1 cone = 1 serving" at the point of decision.
**Evidence:** reviews.md (Robert Y. verified review), PDP screenshots
**Key data:** "The serving size said 1, so I ate an entire cone and was zonked for the rest of the day. 10/10 and nice flavoring." — Robert Y., verified
**Est. lift:** Not calculable — sessions/AOV not provided. Primary value is reduced overconsumption/support risk.

### 5. Reposition the Federal-Ban Countdown Timer
**What's broken:** Above the homepage hero headline sits a full-width banner with a live running countdown clock: "Starting December 11th '26, the US Federal government has banned all intoxicating hemp — including the Delta-9 THC used in Baked Bags products... stock up now." It occupies the first-view position before any product value proposition is shown.
**Evidence:** site-visual-summary.md, live homepage WebFetch
**Key data:** Banner sits directly above "THE LEADING CAUSE OF RED EYES" hero headline in fold 1
**Est. lift:** Not calculable — sessions/AOV not provided.

### 6. Add a Sticky Add-to-Cart Bar on PDP
**What's broken:** The primary "ADD TO CART" button (light blue, full width) sits inline in PDP fold 2, below the star rating, price, benefit bullets, and flavor selector from fold 1. No sticky or persistent CTA was observed in any of the three PDP folds captured.
**Evidence:** site-visual-summary.md (PDP "CTA behavior" notes)
**Key data:** Combined with 18.5s LCP / 53.3s TTI, a visitor who scrolls past the buy box has no fast path back to purchase
**Est. lift:** Not calculable — sessions/AOV not provided.

### 7. Test the Ice-Cream-Pairing Angle in PDP/Ad Content
**What's broken:** No ad, landing page, or PDP asset collected references pairing CONED products with ice cream, despite this being an organic, repeated customer behavior.
**Evidence:** reviews.md
**Key data:** "put it in my ice cream and it hit like no other" (Dae S.); "put real ice cream on it and it was amazing" (Azaera T.); "Goes great with ice cream" (Robert Y.)
**Est. lift:** Not calculable — sessions/AOV not provided. Low-cost content test using existing customer language.

### 8. Align Google Ads Copy with Meta's Pricing Specificity
**What's broken:** All three Google Search ads reviewed use generic "shop now" framing ("Baked Bags: Shop The Drop," "Baked Bags - Shop Now") with no discount or price shown anywhere in headline or description.
**Evidence:** google-ads-visual-summary.md, meta-ads-visual-summary.md
**Key data:** Meta ads lead with $39.99, 33% off, 50% off; Google ads show none of this
**Est. lift:** Not calculable — sessions/AOV not provided. Paid-media copy test, not on-site.

## Unused Findings

- The Google Ads Transparency Center screenshot shows three different verified advertiser names on Baked Bags' own ad cards, none matching the brand — a compliance flag for the client's Google Ads account team, not a CRO test.
- Collection page pricing presentation is inconsistent: multi-flavor packs show strikethrough + red savings badge, single-flavor cards show flat pricing with no badge.
- PDP shows the same five-icon trust strip three separate times across three folds — a consolidation opportunity.
- Bundle & Save on the PDP is quantity-based only (1x/2x/3x of one flavor selection); no mix-and-match bundle exists despite reviews confirming customers value variety.
- The cart drawer already has strong AOV mechanics (free-shipping bar, inline upsell, cross-sell module, Rush Order toggle, Sezzle installments) — this funnel stage is ahead of the rest of the site and doesn't need a test.
