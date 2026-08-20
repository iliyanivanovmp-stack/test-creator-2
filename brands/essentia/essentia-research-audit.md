# Essentia CRO Research Audit

## Data Sources Used

- Meta Ads and Landing Pages (screenshots, pre-collected + visual summary)
- Google Ads Transparency Center (screenshots, pre-collected + visual summary)
- PageSpeed / Core Web Vitals (raw Lighthouse JSON, mobile — homepage and PDP)
- Current Site Screenshots (homepage, collection, PDP, cart) + live homepage fetch
- Competitor research (self-researched, WebSearch, August 5, 2026)

Not collected for this project: Reviews & UGC (explicitly skipped by client), Email Campaigns, Inspiration Sites, Non-Data Context/call notes.

## Source Findings

### Meta Ads & Landing Pages

**Ad 1 — "Grateful Bed Eight" mattress:** Headline claims "top marks from leading independent reviewers." The linked landing page shows the "Grateful Bed Jr" kids' mattress, not the "Grateful Bed Eight" named in the ad — a product mismatch between ad and destination. LP shows only 5 reviews, which undercuts the ad's "top marks from leading independent reviewers" claim. Ad carries no discount messaging; the LP's top bar shows a 20% off sitewide sale not mentioned anywhere in the ad creative.

**Ad 2 — HSA/FSA / Truemed:** Headline "Save 30% on average when you qualify to pay... with HSA/FSA" lands on the Tatami™ PDP, which repeats "HSA/FSA eligible — Save an average of 30%" directly below the Add to Cart button — strong message match. Gap: the ad does not mention the EMF Protection Foam Upgrade option shown in the buy box, so shoppers encounter an unexplained upsell decision at the point of purchase.

**Ad 3 — Affirm financing:** Headline promises "pay over time... 0% APR... never pay a single hidden fee." The landing page is a dedicated financing explainer, not a product page — no Add to Cart CTA is visible in any of the three captured folds. A shopper who clicks this ad intending to buy a mattress lands on informational content with no direct path to a buy box.

**Cross-ad pattern:** All three ads route to pages carrying a 20% sitewide sale banner that is absent from the ad creative itself. This is a recurring message-match gap, not a one-off.

### Google Ads

Advertiser "Organic Exchange Inc" (Verified) runs 20+ ad units across search, display, video, and shopping formats. Headline themes cluster around certification/authority ("Rated #1 Foam Mattress 2026 – GOLS & GOTS Certified"), "Made in USA," non-toxic/health claims, financing/savings (HSA/FSA, "Save up to 30%"), and a call-focused CTA ("Call... Get Help Choosing The Right Mattress").

Discount inconsistency within Google's own ad set: one unit says "Save up to 30% on Essentia," another static creative says "Save up to 22% on eco-friendly mattresses." Neither figure matches the on-site 20% sitewide sale banner. None of the reviewed Google ads reference the "REST & RECHARGE SALE" by name.

Gap vs. Meta: Google leans heavily on certification/authority and "Made in USA" claims that don't appear in any of the three Meta creatives reviewed — the two channels are running different value propositions to different audiences.

### Reviews & UGC

Not collected — explicitly skipped by the client for this project. No review-sourced insights are available for this audit.

### PageSpeed / Core Web Vitals

Data collected: mobile only, homepage and PDP, via Lighthouse JSON export, August 5, 2026.

**Homepage (mobile):** Performance score 31/100. LCP 11.8s (score 0), FCP 11.6s (score 0), Speed Index 15.5s (score 0), Time to Interactive 37.1s (score 0), Total Blocking Time 1,200ms (score 0.2). CLS is 0 (score 1) — no layout shift issue. Total page weight 11.2 MB; unused JavaScript accounts for an estimated 1.5 MB in potential savings; main-thread work totals 8.8s.

**PDP — Stratami (mobile):** Performance score 38/100. LCP 33.8s (score 0), FCP 16.1s (score 0), Speed Index 16.1s (score 0), Time to Interactive 42.6s (score 0), Total Blocking Time 680ms (score 0.43). CLS 0.007 (score 1, negligible). Total page weight 6.4 MB; unused JavaScript ~1.4 MB; main-thread work 20.6s; JS bootup time 7.5s.

Both pages fail every mobile Core Web Vital tied to load speed (LCP, FCP, TTI) while layout stability (CLS) is not an issue on either page. A PDP LCP of 33.8 seconds on mobile means the primary product image or buy box is very unlikely to be visible before a meaningful share of mobile visitors abandon — this lands directly on the funnel stage the client flagged (add-to-cart happens, but purchase completion drops off), since the checkout path likely inherits the same JS-heavy, render-blocking pattern.

No desktop PageSpeed data was collected for this project.

### Competitor Analysis

Sources: `raw/competitors.md` was not provided by the client. The following is self-researched via WebSearch, August 5, 2026.

| Brand | Entry price (queen) | Trial | Warranty | Certifications |
|---|---|---|---|---|
| Essentia (Stratami) | ~$3,000 MSRP, $3,850 at full MSRP | 120 nights | 20 years | GOLS, GOTS |
| Avocado Green | $1,999 MSRP (~$1,849 with regular discounts) | 365 nights | 25 years | GOLS, GOTS |
| Naturepedic (Concerto) | $2,799 MSRP | 100 nights | 25 years | GOLS, GOTS |

Essentia prices 20–30% above similarly certified competitors, per third-party comparison coverage (Toms Guide, Mattress Nerd). Both Avocado and Naturepedic offer longer warranties (25 years vs. Essentia's 20), and Avocado's 365-night trial is more than 3x Essentia's 120-night trial. Essentia's differentiators per third-party reviews: patented Beyond Latex™ foam and EMF protection, features not offered by Avocado or Naturepedic. On-site, Essentia does not surface its trial/warranty terms until deep in the PDP (accordion items below the buy box) — competitors' longer terms are a source of anchoring risk if a comparison-shopping visitor doesn't see Essentia's terms early.

Sources: [Avocado Green vs Essentia Stratami — Tom's Guide](https://www.tomsguide.com/wellness/mattresses/avocado-green-vs-essentia-stratami-which-organic-mattress-suits-your-sleep), [Naturepedic vs. Avocado Mattress Comparison — Mattress Nerd](https://www.mattressnerd.com/naturepedic-vs-avocado-mattress-comparison/)

### Emails

Not collected — not provided by the client for this project.

### Inspiration Sites

Not collected — not provided by the client for this project.

### Non-Data Context

Not collected — no call notes or strategic context provided. Client-stated area of focus (from manifest): strong add-to-cart activity, but a large drop-off in the percentage of shoppers who complete purchase after adding to cart. This audit's findings are read through that lens throughout.

### Current Site Screenshots

**Homepage:** Sitewide sale bar ("REST & RECHARGE SALE | 20% OFF") sits above a full-bleed video/image hero with a single CTA ("SHOP ORGANIC MATTRESSES"). No star rating, review count, or guarantee badge appears anywhere in the first three folds. Certification badges (7 logos) and the founder story don't appear until fold 3 — trust and credibility content is pushed well below the fold. Product carousel in fold 2/3 requires horizontal scroll interaction to see all 4+ products, and each carousel item shows full price with no indication of the active 20% sale.

**Collection page:** Product grid cards (Venti $1,699, Grateful Eight $1,999, Tatami™ $2,999, Stratami™ $3,599) show "Starting at $X" pricing with no compare-at/strikethrough pricing, despite the sitewide 20% off promotion running in the top bar. No filter or sort controls, no review stars, and no price-drop indicators are visible on any card.

**PDP (Stratami):** Star rating (4.5, 36 reviews) sits directly below price, above all buy box options — good proximity to the CTA. Buy box has three dropdowns (Size, Height, EMF Foam Protection Upgrade) with no visual hierarchy and no pre-selected/highlighted upsell — EMF Protection defaults to "No EMF Foam Protection." No compare-at pricing on the PDP itself despite the sitewide sale; only an Affirm monthly estimate is shown. Trial (120-night), warranty (20-year), and financing details are pushed into collapsed accordions below the Add to Cart button rather than surfaced near the CTA. No bundle, frequently-bought-together, or cross-sell module is present. Add to Cart is not observed as sticky on scroll.

**Cart:** Single line item, static full-width "Checkout" button. The site's 20% sitewide discount is auto-applied and itemized ("Discount Applied -$719.80"), which is a positive signal of message match between the promo bar and cart. No upsell, cross-sell, bundle, or free-shipping-threshold mechanic anywhere on the cart page — no related-products or frequently-bought-together module. No guarantee, returns policy, or trust badge is visible in the cart, which is the last page shown before checkout and closest to the drop-off point the client flagged.

## Cross-Source Themes

1. **Speed is likely the dominant driver of the add-to-cart-to-purchase drop-off.** Mobile PDP LCP of 33.8s and homepage LCP of 11.8s both fail Core Web Vitals by a wide margin, with ~1.4-1.5MB of unused JavaScript on each page. This sits upstream of every other finding and directly maps to the client's stated problem: if checkout inherits similar JS weight, slow rendering after add-to-cart is a strong candidate for the purchase-completion drop-off.
2. **Trust and reassurance content is present but consistently misplaced relative to purchase-decision moments.** Star ratings sit well on the PDP, but trial/warranty terms sit in collapsed accordions below Add to Cart, certification badges don't appear until homepage fold 3, and the cart — the page closest to checkout — has zero trust signals at all.
3. **Promotion and pricing messaging is inconsistent across every touchpoint.** The sitewide 20% off promo is invisible in all three Meta ad creatives and all Google ad copy reviewed; collection and PDP prices don't reflect it either (only the cart applies it); and Google's own ad set shows two different discount percentages (30% vs. 22%) that don't match the 20% shown on-site.

## Top Test Opportunities

**PDP mobile page-speed remediation** — PDP mobile LCP is 33.8s and Time to Interactive is 42.6s, both catastrophic Core Web Vitals failures; ~1.4MB of unused JS and 20.6s of main-thread work are the likely cause. This is the funnel stage the client flagged for drop-off, and a checkout path inheriting this weight would explain it directly. Evidence: raw/essentia-pdp-pagespeed.json. Est. lift: conservative 5-10% CR lift on mobile PDP sessions x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

**Homepage mobile page-speed remediation** — Homepage mobile LCP is 11.8s and TTI is 37.1s, with 1.5MB of unused JavaScript; this is the entry point for the majority of paid traffic (Meta and Google ads both land users here or on PDPs with the same JS weight). Evidence: raw/essentia-homepage-pagespeed.json. Est. lift: conservative 3-6% CR lift on mobile sessions x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

**Surface the sitewide discount on collection and PDP pricing** — Collection cards and the PDP show only "Starting at $X" full price with no compare-at/strikethrough pricing, even though the 20% "REST & RECHARGE SALE" is active and auto-applies at cart. A shopper who adds to cart without seeing the discount reflected until checkout may perceive a bait-and-switch or simply not feel the urgency the sale is meant to create, which plausibly contributes to the add-to-cart-to-purchase drop-off the client flagged. Evidence: raw/site-visual-summary.md (collection and PDP price display notes), raw/meta-ads-visual-summary.md. Est. lift: conservative 2-4% CR lift x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

**Add trust signals to the cart page** — The cart page (the step immediately before checkout, and closest to the client-flagged drop-off point) has zero trust signals: no guarantee, returns policy, warranty, or trial mention anywhere. Evidence: raw/site-visual-summary.md (Cart section). Est. lift: conservative 2-4% CR lift on cart-to-checkout rate x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

**Surface trial and warranty terms near the Add to Cart button on PDP** — Trial (120-night) and warranty (20-year) terms are pushed into collapsed accordions below Add to Cart, while competitors Avocado (365-night trial, 25-year warranty) and Naturepedic (25-year warranty) offer stronger terms. A shopper comparison-shopping who doesn't expand the accordion may perceive Essentia as offering weaker terms than it does, right before the add-to-cart decision. Evidence: raw/site-visual-summary.md (PDP section), competitor research. Est. lift: conservative 2-3% CR lift on PDP add-to-cart rate x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

**Fix the Ad 1 product mismatch (Grateful Bed Eight vs. Grateful Bed Jr)** — Meta Ad 1 names the "Grateful Bed Eight" mattress but links to the "Grateful Bed Jr" kids' mattress landing page — a wrong-product landing experience that likely produces immediate bounce or confusion for anyone clicking with adult-mattress intent. This is a fix, not an A/B test, but it directly affects the top of the funnel this audit was scoped around. Evidence: raw/meta-ads-visual-summary.md (Ad 1). Est. lift: not sizeable without Ad 1's spend/click data; flagged as a priority fix regardless of slot allocation.

**Add a highlighted upsell/cross-sell module to the buy box or cart** — The EMF Foam Protection Upgrade dropdown on the PDP defaults to "No EMF Foam Protection" with no visual emphasis, and the cart has no bundle, cross-sell, or frequently-bought-together module at all. Evidence: raw/site-visual-summary.md (PDP and Cart sections). Est. lift: conservative 3-5% AOV lift on completed orders x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

**Route the Affirm financing ad (Ad 3) to a transactional page** — Ad 3 promises 0% APR financing but its landing page is an informational Affirm explainer with no Add to Cart CTA visible in any of the three captured folds, meaning a shopper motivated by financing has no direct path to buy. Evidence: raw/meta-ads-visual-summary.md (Ad 3). Est. lift: not sizeable without Ad 3's spend/click data; flagged as a message-match/funnel-leak fix.

**Reconcile discount percentage across ad channels and site** — Google Ads reference both "up to 30%" and "up to 22%" savings, neither matching the on-site 20% sitewide sale, and Meta's HSA/FSA ad (Ad 2) references "30% on average" via a separate financing mechanism (Truemed) that is a different offer from the sitewide discount. A shopper arriving expecting one discount and seeing another at checkout is a trust and conversion risk. Evidence: raw/google-ads-visual-summary.md, raw/meta-ads-visual-summary.md. Est. lift: conservative 1-3% CR lift x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

**Move certification/trust badges above the fold on homepage** — Certification badges (GOLS, GOTS, Well Living Lab, ISO, Hippocrates Approved) and the founder credibility story don't appear until homepage fold 3, despite Google Ads' heavy emphasis on certification/authority messaging ("GOLS & GOTS Certified," "#1 Rated Organic Foam Mattress") — a visitor arriving from a certification-led Google ad has to scroll past two folds before seeing the proof. Evidence: raw/site-visual-summary.md (Homepage section), raw/google-ads-visual-summary.md. Est. lift: conservative 1-3% CR lift on Google-ad-sourced sessions x unknown sessions/mo x unknown AOV = requires sessions/AOV data to size in dollars.

## Unused but Valuable Findings

- The Meta HSA/FSA ad (Ad 2) achieves strong message match with its landing page — a pattern worth preserving/replicating in future ad creative rather than testing against.
- Cart-level discount application is accurate and well itemized (shows exact dollar amount saved), which is a positive control worth keeping as-is while testing earlier-funnel discount visibility.

## Missing Data

- No monthly sessions or AOV figures were provided or collected, so every Est. lift line in this audit is directional (percentage lift only) rather than dollarized. The roadmap step should flag this and request these figures from the client, or use placeholder ranges.
- Reviews & UGC were explicitly skipped for this project — no customer-voice evidence (love/frustration themes) is available to corroborate or challenge the findings above.
- No desktop PageSpeed data was collected — all CWV findings are mobile-only; desktop performance is unknown.
- No Non-Data Context (call notes, known objections, stated priorities beyond the add-to-cart-to-purchase drop-off) was provided.
