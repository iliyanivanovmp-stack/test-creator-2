# Baked Bags CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads Transparency Center, PageSpeed / Core Web Vitals, Current Site Screenshots, Reviews & UGC, Competitor Analysis (self-researched)

Site speed is the single largest, best-evidenced problem in the funnel. Lighthouse mobile data (2026-08-21) shows the PDP loading with an 18.5s LCP and a 53.3s Time to Interactive; the homepage isn't far behind at 8.1s LCP and 49.2s TTI. Performance scores sit at 0.34 (homepage) and 0.39 (PDP), against Google's 2.5s "good" LCP threshold. Every dollar spent on Meta and Google ads is landing traffic on pages that take the better part of a minute to become tappable on mobile.

Message match breaks down between the two highest-volume Meta ads and the page they send traffic to. Ad 1 (running since 2026-07-19) and Ad 2 (since 2026-07-22) both sell a subscription program: "Subscribe and unlock 10+ tiers of free gifts, surprise rewards and exclusive perks." The landing page at bakedbags.life/packs/ never mentions subscription in any of the three folds captured, and the PDP buy box for the same CONED product line shows only one-time purchase plus quantity-based Bundle & Save, no subscribe-and-save option — Source: Meta ads visual summary, live WebFetch. Competitor Delta Munchies runs a live subscription flow at 15% off with free shipping and pause/edit anytime — Source: competitor research. Ad 3 shows the opposite pattern and proves the model works: "Save 33% on Cones Variety Packs. 4 flavors for $39.99" lands on a page headlined "SAVE 33% ON THE CONES STARTER PACK," word-for-word match.

Reviews surface two signals not reflected anywhere in ad or site copy. At least three of 20 verified CONED reviews independently describe pairing the product with real ice cream ("put it in my ice cream and it hit like no other" — Dae S.) — Source: Reviews & UGC. Separately, one verified reviewer over-consumed because serving size wasn't clear at the point of decision: "The serving size said 1, so I ate an entire cone and was zonked for the rest of the day" — Robert Y., Reviews & UGC. The buy box already carries "Two 25MG THC Cones Per Bag" and "200 MG THC Total" as bullets, but no explicit "1 cone = 1 serving" statement.

No sessions or AOV data was provided for Baked Bags, so revenue potential cannot be sized in dollars for any slot below. Every test is prioritized on evidence strength and severity instead. The two Core Web Vitals fixes are treated as the top priority regardless: a Time to Interactive near 50 seconds on both landing pages means a meaningful share of paid mobile traffic is arriving on pages that aren't yet tappable.

---

## Slot 1: PDP Core Web Vitals Emergency Fix

**Type:** Immediate Fix
**Page:** Product Detail Page (extra-strength-variety-pack-edibles-800mg)

**What's broken:** Mobile Lighthouse (2026-08-21) shows the PDP loading with an 18.5s LCP, 690ms TBT, and 53.3s Time to Interactive. A visitor from a paid ad lands on the buy box (star rating, price, benefit bullets, flavor selector) and can tap Add to Cart with no visible response for the better part of a minute.

**Data:** Performance score 0.39, LCP 18.5s, TTI 53.3s, CLS 0.002 — Source: PageSpeed / Core Web Vitals (bakedbags-pdp-speedtest.json). LCP is roughly 7x over Google's 2.5s "good" threshold.

**Why now:** This is a page-breaking performance issue, not a hypothesis to test. It sits under every other PDP test on this roadmap: no buy box copy or layout change matters if the page isn't interactive.

---

## Slot 2: Homepage Core Web Vitals Fix

**Type:** Immediate Fix
**Page:** Homepage (bakedbags.com)

**What's broken:** Mobile Lighthouse (2026-08-21) shows the homepage loading with an 8.1s LCP, 790ms TBT, and 49.2s Time to Interactive.

**Data:** Performance score 0.34, LCP 8.1s, CLS 0.153, TBT 790ms — Source: PageSpeed / Core Web Vitals (bakedbags-homepage-speedtest.json). LCP is roughly 3x over Google's 2.5s "good" threshold.

**Why now:** Homepage is a top entry point for branded and Google Search traffic. A 49-second Time to Interactive means most of that traffic bounces before the page responds to a tap.

---

## Slot 3: Close the Subscription Message-Match Gap

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page — CONED buy box (extra-strength-variety-pack-edibles-800mg)
**Revenue potential:** Not calculable — sessions and AOV data not provided. Priority is set by cross-source confirmation: the exact hook driving clicks on two active ad campaigns has no matching purchase option anywhere on site.

**Hypothesis:** If we add a subscribe-and-save purchase option to the CONED buy box, conversion rate will improve because two active Meta ads (running since 2026-07-19 and 2026-07-22) are selling subscription as the core hook and currently send that traffic to a buy box with no way to act on it.

**Data:** Meta Ad 1 and Ad 2 both promise "10+ tiers of free gifts, surprise rewards and exclusive perks" for subscribing, but the landing page at bakedbags.life/packs/ never mentions subscription in any of the three folds captured, and the PDP buy box for the same product line shows one-time purchase plus quantity-based Bundle & Save only — Source: Meta ads visual summary, live WebFetch of bakedbags.life/packs/, PDP screenshots. Competitor Delta Munchies runs a live subscribe-and-save flow at 15% off with free shipping, pause/edit anytime — Source: competitor research (self-researched, not client-provided).

**V1:** Add a subscribe-and-save toggle to the buy box, positioned above the existing one-time/Bundle & Save selector, on both mobile and desktop. Below the selected subscription option, add benefit microcopy: "Includes free shipping + more subscriber benefits" (exact perk tiers are not yet documented, so copy stays broad rather than inventing specific numbers). Control keeps the current one-time-purchase-plus-Bundle&Save layout with no subscription option.

---

## Slot 4: Serving-Size Callout in Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page — CONED buy box (extra-strength-variety-pack-edibles-800mg)
**Revenue potential:** Not calculable — sessions and AOV data not provided. Primary value is reduced overconsumption and support risk; secondary value is trust-building copy at the point of decision.

**Hypothesis:** If we add an explicit "1 cone = 1 serving" line to the PDP buy box, customer confidence and satisfaction will improve because current bullets state potency ("Two 25MG THC Cones Per Bag," "200 MG THC Total") without stating serving size in plain language at the point of purchase.

**Data:** A verified reviewer reported eating a whole cone believing it was one serving: "The serving size said 1, so I ate an entire cone and was zonked for the rest of the day. 10/10 and nice flavoring." — Robert Y., verified review. The existing buy box already lists "Two 25MG THC Cones Per Bag," "4 Different Flavors," and "200 MG THC Total" as bullets directly under price, without a serving-size statement — Source: PDP screenshots.

**V1:** Add a fourth bullet to the existing benefit-bullet list, directly under price: "1 Cone = 1 Serving (25MG)." Same placement and bullet styling as the existing three bullets, on both mobile and desktop. Control keeps the current three-bullet list.

---

## Slot 5: Reposition the Federal-Ban Countdown Timer

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (bakedbags.com)
**Revenue potential:** Not calculable — sessions and AOV data not provided.

**Hypothesis:** If we move the federal-ban countdown banner below the hero headline and CTA, first-view conversion will improve because the banner currently occupies the top position and competes with the primary offer message before a visitor has seen any product value proposition.

**Data:** The homepage's first-view order is: countdown banner ("Starting December 11th '26, the US Federal government has banned all intoxicating hemp... stock up now" with a live running timer), then hero headline "THE LEADING CAUSE OF RED EYES," then the "SHOP LEGAL THC" CTA — Source: site-visual-summary.md, live homepage WebFetch.

**V1:** Move the countdown banner to sit directly below the hero CTA instead of above the headline, so the fold order becomes headline, subhead, CTA, countdown banner. No copy changes to the banner itself. Same reorder on mobile and desktop. Control keeps the current banner-first order.

---

## Slot 6: Sticky Add-to-Cart Bar on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (extra-strength-variety-pack-edibles-800mg)
**Revenue potential:** Not calculable — sessions and AOV data not provided.

**Hypothesis:** If we add a sticky Add to Cart bar that appears after a visitor scrolls past the buy box, conversion rate will improve because the current Add to Cart button is inline in fold 2 with no persistent CTA in any of the three PDP folds captured.

**Data:** The primary "ADD TO CART" button sits inline below the star rating, price, benefit bullets, and flavor selector in fold 1/2, with no sticky or persistent CTA observed in any PDP fold — Source: site-visual-summary.md (PDP "CTA behavior" notes). Combined with the page's 53.3s Time to Interactive (Slot 1), a visitor who scrolls past the buy box currently has no fast path back to purchase.

**V1:** Add a sticky bottom bar on mobile (product thumbnail, price, "Add to Cart" button) that appears once the visitor scrolls past the existing buy box, and a sticky right-rail summary on desktop with the same elements. Bar persists through product description and reviews sections. Control has no sticky element.

---

## Slot 7: Ice-Cream-Pairing Content Test

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (extra-strength-variety-pack-edibles-800mg)
**Revenue potential:** Not calculable — sessions and AOV data not provided. Low-cost content test using existing customer language, no new claims introduced.

**Hypothesis:** If we add a pairing suggestion to the PDP using customers' own language, add-to-cart rate will improve because at least three of 20 collected reviews independently describe pairing CONED products with real ice cream, an angle absent from all ad, landing page, and PDP assets collected.

**Data:** "put it in my ice cream and it hit like no other" (Dae S.); "put real ice cream on it and it was amazing" (Azaera T.); "Goes great with ice cream" (Robert Y.) — Source: Reviews & UGC. No ad, landing page, or PDP copy in the collected assets references this pairing.

**V1:** Add one line of pairing copy near the existing benefit-bullet list in the buy box: "Customer favorite: pair with real ice cream." Same copy and placement on mobile and desktop. Control keeps the current bullet list with no pairing mention.

---

## Slot 8: Align Google Search Ad Copy with Meta's Pricing Specificity

**Type:** A/B test (1 variation vs. control)
**Page:** Google Search Ads (Google Ads Transparency Center)
**Revenue potential:** Not calculable — sessions and AOV data not provided. Paid-media copy test, not an on-site change.

**Hypothesis:** If Google Search ad copy includes specific pricing and discount numbers, click-through rate will improve because the three Google Search ads reviewed use generic "shop now" framing with no price or discount shown, while Meta ads leading with specific numbers are the higher message-match performers on this roadmap.

**Data:** All three Google Search ads reviewed use generic framing ("Baked Bags: Shop The Drop," "Baked Bags - Shop Now") with no discount or price in headline or description — Source: google-ads-visual-summary.md. Meta ads lead with $39.99, 33% off, and 50% off — Source: meta-ads-visual-summary.md.

**V1:** Rewrite Google Search ad headlines and descriptions to include the same pricing specificity used in Meta Ad 3, the strongest message-match ad on this roadmap: e.g. "4 Flavors for $39.99 — Save 33%." Control keeps current generic "shop now" copy.

---

## Future Slot Candidates

1. **Consolidate the repeated PDP trust-badge strip** - The same five-icon trust strip (Made in USA, Fast Shipping, Quality Ingredients, Lab Tested, Hemp Derived) appears three separate times across the three PDP folds captured, diluting its impact versus one well-placed instance near the buy box.
2. **Standardize collection page pricing presentation** - Multi-flavor pack cards show strikethrough pricing with a red "% Savings" badge while single-flavor cards show flat pricing with no badge, creating an inconsistent value signal on the same grid.
3. **Add a mix-and-match bundle option on PDP** - Bundle & Save is currently quantity-based only (1x/2x/3x of one flavor), despite reviews confirming customers value variety ("I like the idea of having a variety and not getting bored" — Loveyy S.).
