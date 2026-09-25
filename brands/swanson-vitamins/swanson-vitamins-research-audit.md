# Swanson Vitamins CRO Research Audit

## Data Sources Used

**User-provided:** Meta Ads landing URLs, Meta ad creative/landing screenshots (visual summary), Google Ads Transparency screenshots (visual summary), PDP reviews (Triple Magnesium Complex, 22 reviews, dated Jun 12 - Sep 5, 2026), raw PageSpeed/Lighthouse JSON for homepage and PDP, site screenshots (homepage, staff-picks "stacks" page, PDP, cart drawer), non-data context note on homepage CTA.

**Self-researched:** Live verification of homepage, PDP, and all three Meta ad landing pages (WebFetch, 2026-09-12). Social & community research via `/last30days-ecom` (2026-09-12). Competitor research via WebSearch (2026-09-12).

## Source Findings

### Meta Ads & Landing Pages

Three active Meta ads (Swanson Health, running since Jul 26 - Sep 4, 2026), all using a "Shop now" CTA.

**Ad 1 (Probiotics):** Promises "no strain-count confusion" and clear science-backed options. Live-verified 2026-09-12: the landing page (`/pages/probiotics`) opens on "The Probiotic Collection" with GMP-Certified/Expertly Crafted/Science Backed badges and a hero product (Dr. Stephen Langer's Ultimate 16 Strain Probiotic, "5 million bottles sold"), then a 7-SKU grid. Message match is strong — ad promise and landing content align.

**Ad 2 (k2o hydration) and Ad 3 (Mellow Magnesium):** Both ads lead with a "100% Money Back Guarantee" claim in the ad copy. Live-verified 2026-09-12: both landing URLs (`/collections/brand-k2o`, `/collections/mellow-magnesium`) return an age-verification gate ("confirm you are at least 18") before any product content renders. This matches the screenshot finding that fold-1 on both landing pages shows only a single headline against a blank area — the age gate, not a slow-loading hero, is the likely cause. The money-back guarantee promised in both ads does not appear anywhere before this gate, and in the captured screenshots it only surfaces in Ad 2's footer (fold 3) and not at all in Ad 3's two captured folds.

**Gap:** Two of three active Meta campaigns route paid traffic into an interstitial that hides the product grid and the guarantee claim the ad just made, on the exact landing pages the ads paid to drive traffic to.

### Google Ads

Roughly 24 ad units (Google Ads Transparency Center, captured pre-audit) spanning sleep/stress, digestion, energy, recovery/hydration, and brand-heritage ("Since 1969") angles, with heavy use of "35% off" / "40% off first order" style discount offers and video testimonial formats.

Compared to Meta's tight three-SKU, guarantee-led messaging, Google's ad set is broader and discount-code-driven. Neither the "100% Money-Back Guarantee" language used on 2 of 3 Meta ads nor a single consistent value prop carries across to Google's creative set. This is a message-match inconsistency across channels rather than a single landing-page defect.

### Reviews & UGC

Source: 22 reviews on the Triple Magnesium Complex PDP, Jun 12 - Sep 5, 2026.

#### What Customers Love
- Multi-source formulation solving multiple needs at once: "it helps with several things... I take it before bed because magnesium glycinate helps calm me and promote sleep, the mag citrate help keep me regular" (Jeffrey M., Jul 25).
- Long-term repeat use: "I have been buying this magnesium for many years love it would not go a day without!" (Nona M., Jul 20).
- US-based manufacturing trust: "I love the fact that this is a US based company and not a questioonable Amazon brand" (Akin T., Jul 1).

#### What Frustrates Customers
- Ingredient-ratio transparency (recurring, 3+ reviews): "Swanson should however list the percentages of each" (Jeffrey M., Jul 25); "I suspect this is mostly mag oxide which isn't absorbed" (1-star review, Sep 5); "Not the best mix of Magnesium sources. Oxide has a ridiculously low bioavailability" (Charles R., Jun 12).
- Mismatch between shopper need and formula: "I was looking for a cognitive function magnesium, but this one has oxide and citrate for constipation relief which we do not need... Soooo I should have done my own research instead of trusting the label" (Cecilia B., 3-star, Sep 5).
- Efficacy uncertainty: "Not sure how to evaluate efficiency" (Marcy S., 3-star, Jun 28); "Biodigestibility unknown though" (Douglas D., 4-star, May 23).

#### Client-Actionable Insights
- Add the per-compound milligram or percentage breakdown (oxide / citrate / glycinate split) to the Supplement Facts panel and product copy — the current panel shows only total 400mg/95% DV magnesium with no split, and this is the single most repeated complaint.
- Consider a short "which magnesium type is this for?" use-case guide on the PDP, since multiple reviewers bought expecting a single-purpose effect (cognitive, sleep, or digestive) and got a blended formula.

### PageSpeed / Core Web Vitals

Source: Lighthouse reports run 2026-09-12, mobile.

| Page | Performance score | LCP | TBT | CLS | Speed Index |
|---|---|---|---|---|---|
| Homepage | 0.33 (poor) | 7.2s | 1,750ms | 0 | 8.9s |
| PDP (Triple Magnesium Complex) | 0.37 (poor) | 12.2s | 1,630ms | 0 | 7.0s |

Google's "good" LCP threshold is 2.5s. The PDP's 12.2s LCP is roughly 5x that threshold — on the page type paid traffic and organic search both land on to buy. CLS is 0 on both pages (no layout-shift problem here), so the failure is purely load speed and main-thread blocking (TBT >1.6s on both), not visual jank.

### Competitor Analysis

Self-researched via WebSearch, 2026-09-12. No user-provided competitor file existed.

| Competitor | Subscribe/Autoship discount | Free shipping threshold | Note |
|---|---|---|---|
| Swanson Vitamins | 40% off first Subscribe order + 30% future (per PDP, live-verified) | $35 (subscription orders only, per PDP) | Two purchase options display the same price on the PDP (see Site Screenshots) |
| Puritan's Pride | 20% off Subscribe & Save | $30 | Lower threshold, live discount is visible as a % off, not a same-price toggle |
| Vitacost (acquired by iHerb, Jan 2026) | 10% off Autoship + $10 welcome credit | $49 standard ($25 for Vitacost-brand items) | Highest threshold of the set |

Similarweb/Semrush (accessed 2026-09-12) rank Vitacost and iHerb as Swanson's closest competitors by traffic overlap, with Puritan's Pride and Vitamin Shoppe also in the top set. Swanson's headline 40% subscribe discount is the most aggressive of the three on paper, but it is the only one of the three where the discount is not reflected as a visible price difference on the product page (see PDP finding below) — a competitive advantage undermined by presentation.

### Social & Community Research

Source: `/last30days-ecom`, 2026-09-12. Directional/third-party — not corroborated by first-party review data except where noted.

- On-site and Amazon star ratings for Swanson products run consistently high (4.3-4.8 stars). The homepage itself displays "4.3 stars from 37,346 reviews via Trustpilot" (live-verified 2026-09-12), which is at the higher end of the range the third-party pull found for Trustpilot (sources cited 4.0/46K and 4.3/33K during the same run) — the live site figure is corroborated by the more favorable end of the third-party pull, not a red flag on its own.
- A Yelp listing for a physical Swanson location in Fargo, ND shows 2.4 stars (155 reviews). This is a brick-and-mortar/customer-service channel, not the ecommerce storefront, and is not corroborated by any onsite or Trustpilot signal — treat as unconfirmed and out of scope for storefront CRO.
- Reddit was skipped (no genuine on-topic discussion found).

### Current Site Screenshots

**Homepage:** Hero CTA reads "Shop Stacks" (live-verified 2026-09-12, confirming the discrepancy already flagged in the manifest against the "Shop Stacks Lands" description). It leads to a curated staff-endorsement page, not a standard filterable collection. Trust badges (500K+ Reviews, 750+ 3rd-Party Tested, 100% Money-Back Guarantee) sit in fold 2, below the hero — a shopper who doesn't scroll past the hero sees no trust signal at all.

**"Collection" page (staff-picks stacks):** Structured as a repeating pattern of staff photo/bio → 5-product grid → testimonial quote (Britta's Stack, then Dustin's Stack). No filter or sort controls appear in any of the three captured folds. This works as a curated discovery format but is not a substitute for category browsing — a shopper arriving here looking for, e.g., "protein" or "sleep support" specifically has no way to narrow results on this page.

**PDP (Triple Magnesium Complex):** Live-verified 2026-09-12 — confirms the screenshot finding exactly. "Subscribe to Save" ($23.19, labeled "Best Value," "40% off today") and "One-time purchase" ($23.19) display the identical price. The "40% off" and "Save 40% in cart" copy has no corresponding visible discount on the page itself; a shopper comparing the two boxes sees no reason to pick the pre-selected subscribe option over one-time purchase, since neither the price nor a strikethrough/compare-at price shows the claimed savings. Trust/certification badges (Gluten Free, Vegan, Halal, Money-Back Guarantee, etc.) sit below the product image gallery, separated from the price and buy box by the full image column.

**Cart:** Slide-out drawer with a single AOV mechanic — a free-shipping progress bar ("$25.81 away from free shipping"). The PDP's "Frequently Purchased Together" row (4 related products) does not carry into the cart drawer; a shopper who is $25.81 short of free shipping sees no in-cart product suggestion to help close that gap.

## Cross-Source Themes

1. **Subscribe pricing shows no visible discount** — PDP screenshot + live PDP verification both confirm identical $23.19 pricing for Subscribe vs. One-time despite "40% off" copy. Directly undermines Swanson's most aggressive competitive lever (a subscribe discount more generous on paper than Puritan's Pride or Vitacost).
2. **Paid traffic hits blocked or slow-loading pages** — 2 of 3 Meta ad landing pages are gated by an age-verification interstitial that hides the product grid and the guarantee claim the ad made (Ad 2, Ad 3); separately, the PDP itself loads in 12.2s (LCP), meaning even traffic that gets past the gate faces a near 5x-over-threshold load before the buy box is usable.
3. **Ingredient-ratio transparency is the most repeated review complaint** — at least 3 of 22 reviews independently ask for or complain about the missing oxide/citrate/glycinate split, a fixable PDP/product-copy gap, not a formulation issue.

## Top Test Opportunities

**Fix Subscribe-vs-One-time price display on PDP** — Both purchase options show $23.19 with no visible discount despite "40% off today" copy, so the claimed savings aren't visible where the purchase decision happens. Evidence: site-visual-summary.md, live PDP verification (2026-09-12), competitor comparison (Puritan's Pride/Vitacost show visible discounts). Est. lift: sessions/mo and baseline CR not collected — apply to PDP traffic once available; AOV reference point ~$23-45 based on observed PDP/collection pricing.

**Remove or defer the age-verification gate on non-restricted collections** — k2o and Mellow Magnesium landing pages show an 18+ age gate before any product content renders, blocking 2 of 3 active Meta ad campaigns' paid traffic from seeing the product grid or guarantee claim. Evidence: meta-ads-visual-summary.md (blank fold-1 on Ad 2 and Ad 3), live verification (2026-09-12). Est. lift: sessions/mo for these two ad campaigns not collected; conservative CR lift on landing-page bounce reduction.

**Compress PDP load time** — PDP LCP is 12.2s (Lighthouse, mobile, 2026-09-12), roughly 5x Google's 2.5s "good" threshold, with TBT of 1,630ms. This is the page both paid and organic PDP traffic must load before purchasing. Evidence: raw pagespeed JSON (`swanson vitamins -pdp-pagespeed.json`). Est. lift: sessions/mo not collected; industry LCP-to-conversion benchmarks support meaningful CR recovery from sub-3s improvements, to be sized once traffic data is available.

**Compress homepage load time** — Homepage LCP is 7.2s with TBT of 1,750ms (Lighthouse, mobile, 2026-09-12), also well over threshold. Evidence: raw pagespeed JSON (`swanson-pagespeed-homepage.json`). Est. lift: sessions/mo not collected.

**Add ingredient-ratio breakdown to Triple Magnesium Complex PDP** — Supplement Facts panel shows only a combined 400mg/95% DV magnesium figure; at least 3 of 22 reviews ask for or complain about the missing oxide/citrate/glycinate split, with one reviewer explicitly stating "Swanson should however list the percentages of each." Evidence: raw/reviews.md, site-visual-summary.md (Supplement Facts panel). Est. lift: sessions/mo and baseline return/complaint rate not collected; expected to reduce mismatch-driven negative reviews and returns more than to lift raw CR.

**Move trust/certification badges adjacent to the PDP buy box** — Gluten Free/Vegan/Halal/Money-Back Guarantee badges currently sit below the image gallery, separated from price and Add to Cart by the full image column. Evidence: site-visual-summary.md (PDP fold 1 layout). Est. lift: sessions/mo not collected.

**Surface homepage trust badges above the fold** — 500K+ Reviews, 750+ 3rd-Party Tested, and 100% Money-Back Guarantee badges sit in fold 2; a shopper who doesn't scroll past the hero sees zero trust signal. Evidence: site-visual-summary.md (homepage fold 1 vs. fold 2). Est. lift: sessions/mo not collected.

**Carry PDP cross-sell into the cart drawer** — The PDP's "Frequently Purchased Together" row (4 related SKUs) does not appear in the cart drawer, whose only AOV mechanic is a $25.81-to-free-shipping progress bar with no product suggestion to help close that gap. Evidence: site-visual-summary.md (PDP fold 2, cart drawer). Est. lift: sessions/mo not collected; AOV reference ~$23-55 based on observed product prices.

**Unify guarantee/value messaging across Google and Meta ad creative** — Meta ads lead with a specific "100% Money-Back Guarantee" claim on 2 of 3 creatives; the Google Ads set (24 units reviewed) instead leans on rotating discount codes (35-40% off) and broad category messaging with no consistent guarantee callout. Evidence: meta-ads-visual-summary.md, google-ads-visual-summary.md. Est. lift: sessions/mo not collected; this is a message-consistency test best measured on assisted-conversion/CTR rather than direct CR.

**Add filter/sort controls to the "Shop Stacks" staff-picks page** — The page the homepage's main CTA leads to is a sequential staff-endorsement format (photo/bio → 5-product grid → quote) with no filter or sort controls across all three captured folds, giving a shopper with a specific need (e.g., "protein," "sleep") no way to narrow results from this entry point. Evidence: site-visual-summary.md (collection-page layout notes). Est. lift: sessions/mo not collected.

**Reduce Ad 3 (Mellow Magnesium) SKU social-proof gap** — Ad 3's four landing-page products each show only 1 review despite a 5-star rating, a thin proof signal for a $22.99-$24.99 impulse-adjacent purchase reached via paid social. Evidence: meta-ads-visual-summary.md (Ad 3, fold 2). This is the narrowest example of the broader "trust signal placement/strength" theme above and is listed as a backup slot.

## Unused but Valuable Findings

- Ad 1's landing page (probiotics) is the one Meta campaign with strong message match and no age-gate friction — worth using as the internal template for how Ad 2 and Ad 3 landing experiences should behave.
- Google Ads' testimonial/behind-the-scenes video format is a different creative style than anything used on Meta; if it performs, it could inform Meta creative refreshes, but no performance data was collected to confirm this.

## Missing Data

- Sessions/month and baseline conversion rate were not provided anywhere in the collected sources, so every Est. lift above is a formula placeholder rather than a dollar figure. Provide GA4/Shopify analytics data to size these tests.
- PDP capture date, shopper geo/currency, and default-variant confirmation were not provided in the original collection (noted in the manifest); live verification on 2026-09-12 confirms USD pricing, 300 Vegan Caps as the currently-selected/default variant, and in-stock status, closing this gap for the current run.
- Ad 3's fold-3 landing page screenshot was not collected, so the guarantee-visibility question for that ad is based on only 2 of 3 folds.
