# Eureka Pet Roadmap Seed

**Store:** https://eurekapet.co/
**AOV:** Unknown (product range: $6 sample → $359 variety pack; estimated blended AOV $80–120 for non-sample orders)
**Monthly sessions:** Unknown — not in collected data
**Data sources:** Meta Ads visual summary + live LP fetch, Google Ads visual summary, Trustpilot reviews (2026-06-15, 50k char sample), Lighthouse mobile PageSpeed (2026-06-15), Site visual summary (homepage, collection, PDP, cart), Live site fetch, Competitor research (self-researched 2026-06-15)

---

## Key Insights

Price sensitivity is the primary conversion barrier and a recurring churn driver. Multiple Trustpilot reviews (1-3 star) cite price as the reason customers won't continue despite loving the product: "for a Rottweiler X Great Dane at $300+ for about 5kgs — TOTALLY unaffordable." A separate complaint reports perceived price-gouging when a $97 first order (which included a $30 welcome discount not labeled as one-time) renewed at $126. Large breed owners, multi-dog households, and pensioners are the most explicitly price-blocked segments — none have a dedicated on-site solution (large-breed bundle, topper pricing frame, per-day cost framing).

The $6 sample funnel is the strongest acquisition path by evidence: the Taste Tester PDP has 335 Trustpilot reviews vs 75 on the Variety Pack, confirming where new customer volume concentrates. Yet the post-click infrastructure is thin. The Taste Tester PDP has no subscription widget despite a "Subscribe & Save 15%" announcement bar running at the top of the page. The cart following a $6 sample add has one static cross-sell ("Cluckin Good Chews $18.95"), no free-shipping bar (threshold $59, leaving $53 of untapped motivation), and no subscription upsell. The funnel driving the most new customers drops them at checkout with minimal LTV infrastructure.

Homepage prioritizes brand story over purchase intent. First three folds are origin story, mission ("starting from the seed of an idea on our family farm in Eureka, NSW"), and a "No fillers. No preservatives." manifesto block. The only above-fold CTA is "Discover More" — an outline (unfilled) button with no price, no product, and no social proof visible in the hero column. Google Ads sends intent-based traffic ("air dried dog food Australia") to this page. The why-air-dried landing page receiving Meta Ad 1 traffic runs a filled orange "Try a Sample - $6" CTA with star ratings in the same hero position — the homepage does not.

---

## Top Test Opportunities

### 1. Homepage Hero — Primary CTA Swap
**What's broken:** The homepage hero is a two-column layout. Left column: headline "All natural Aussie made air dried dog food," subtext "90% Aussie protein, 10% fruit, veg & seeds. No fillers, no preservatives, no nonsense!" followed by a single outline (unfilled/transparent) button labeled "Discover More" — no price, no product name, no star rating. Right column: lifestyle photo of a grey/white dog on a couch next to a yellow Eureka bag. Below the hero is a warm-amber brand story section — no product grid, no pricing, and no subscription offer appear until below fold 3. The why-air-dried page (Ad 1 landing page) runs a dual-CTA hero in the same layout: "Try a Sample - $6" (filled warm orange) + "Shop the Recipes" (outline), with a social proof bar (★★★★★ 4.8 | 6,000+ Happy Dogs) below the CTAs. The homepage has none of this.
**Evidence:** Site visual summary (homepage fold 1), live site fetch, Google Ads (intent keywords landing on homepage), meta-ads-visual-summary (Ad 1 landing page has conversion-optimized hero).
**Key data:** Homepage Lighthouse mobile score 46/100, TTI 35.7s. For visitors who do load the page, the only entry point is a low-weight outline button. Taste Tester PDP has 335 reviews — the $6 sample offer is the most-proven conversion entry point in the business.
**Est. lift:** Unknown sessions × $80+ blended AOV — even a 10% improvement in homepage CTR to product would be material given paid traffic volume.

### 2. Cart — Free Shipping Bar + Subscription Upsell
**What's broken:** The slide-out cart drawer shows: one line item (e.g., Taste Tester $6.00 with qty controls and delete icon), a large empty white space, then a single cross-sell product ("Cluckin Good Chews $18.95") under the label "I'm even better with" in a carousel — no explanation for why this product was recommended. Below that: a discount code field ("Got a discount code? Enter it here!"). Sticky checkout button at bottom: "Checkout • $6.00." There is no free-shipping progress bar. Free shipping unlocks at $59 (stated elsewhere on site) — a $6 sample order sits $53 below the threshold with no visual indicator. No subscription upsell, no bundle, no frequently-bought-together, no minimum order incentive.
**Evidence:** Site visual summary (cart), live site fetch ($59 free shipping threshold), Trustpilot reviews (5+ reviewers explicitly praise subscription flexibility — validates subscribe-and-save appeal).
**Key data:** $53 gap between sample price and free-shipping threshold. Cart has one cross-sell vs. zero subscription touchpoints.
**Est. lift:** 10–20% AOV increase on cart orders (industry benchmark for free-shipping bar implementations on DTC Shopify stores).

### 3. Taste Tester PDP — Add Subscribe & Save Option
**What's broken:** The Taste Tester PDP buy box shows: "Taste Tester" title, ★★★★★ 4.9 (335 reviews), short fussy-dog copy, price $6.00 (standalone, no compare-at), qty selector (−/+), and a black full-width "Add to cart" button. The "Subscribe & Save 15%" announcement bar runs persistently at the top of the page. There is no subscription widget in the buy box — no subscribe/one-time radio toggle, no frequency selector. By contrast, the Variety Pack PDP shows a subscribe/one-time toggle with subscription price ($305.15, "SAVE $53.85" badge) and frequency dropdown ("Every 2 Weeks") above the Add to Cart button. The tech is live on-site — it is simply not deployed on the primary sample PDP.
**Evidence:** Site visual summary (PDP fold 1, layout notes), meta-ads-visual-summary (Ad 3 sends highest-volume sample traffic to this page), Variety Pack PDP confirms subscription widget is active.
**Key data:** 335 Taste Tester reviews vs 75 Variety Pack reviews — sample funnel is primary acquisition. A $6 one-time buyer generates near-zero LTV without a subscription conversion path.
**Est. lift:** 3–5% of sample buyers converting to subscription from this page represents outsized LTV improvement vs a one-time $6 transaction.

### 4. Ad 2 — Savings Claim Alignment
**What's broken:** Meta Ad 2 copy: "save $77 and give your best mate 3 x different Eureka Recipes — the ultimate high protein, wild caught feast." Variety Pack landing page shows "SAVE $53.85" badge (subscription $305.15 vs one-time $359.00). The ad also uses "limited time only" urgency language; the landing page has no scarcity or urgency signal. The $23 discrepancy between the ad's savings claim and the page's savings display is a trust gap at the point of highest transaction value in the funnel.
**Evidence:** meta-ads-visual-summary (Ad 2, message match: partial), live fetch of variety-pack page (subscription $305.15 / regular $359.00 / $53.85 saving shown).
**Key data:** $77 claimed vs $53.85 shown — $23 gap. Variety Pack is the highest-ticket product ($359 one-time). Only 75 reviews vs Taste Tester's 335, suggesting this funnel underperforms.
**Est. lift:** 5–10% Variety Pack PDP conversion improvement by eliminating trust friction.

### 5. Taste Tester PDP — Trust Icons Above Buy Button
**What's broken:** On the Taste Tester PDP, the buy box order is: product title → rating → copy → price ($6.00) → qty selector → "Add to cart" (black full-width button) → [trust icons below]. The four trust icons — 100% Australian Made & Owned / 100% Money Back Guarantee / 68°C gentle air drying / No Fillers or Additives — appear after the CTA, not between the price and the button. A visitor deciding whether to click sees the price and the CTA before seeing any reassurance signals. On the Ad 1 landing page (why-air-dried), trust icons appear as a horizontal row directly between the buy copy and the CTAs.
**Evidence:** Site visual summary (PDP fold 1), meta-ads-visual-summary (Ad 1 LP positions trust icons above CTAs), Trustpilot reviews (Australian provenance and money-back guarantee cited as explicit purchase drivers by multiple reviewers).
**Key data:** "100% money back guarantee" and "100% Australian owned" are recurring decision factors in reviews. Positioning these above the CTA places reassurance at the point of decision rather than after it.
**Est. lift:** 3–8% PDP conversion improvement (per CRO placement benchmarks for trust icon positioning).

---

## Unused Findings

- "Smaller Poos, Better Guts" health-outcome language is used in Google Ads and is absent from every landing page — a proven-in-market headline not yet applied on-site.
- petfoodreviews.com.au 9.5/10 rating is used in Google Ad copy but does not appear on the website or any Meta landing page.
- Carbon-neutral claim (NOCO2 partnership, visible on live homepage) has not been tested in any ad creative — untested differentiator for eco-conscious segment.
- Large breed pricing gap: multiple 1-3 star reviews explicitly cite structural unaffordability for large dogs — no large-breed bundle, per-day cost frame, or topper-use positioning exists on site.
