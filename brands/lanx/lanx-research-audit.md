# LANX (lanxshoes.com) CRO Research Audit

## Data Sources Used

**User-provided (first-party collection):**
- Meta Ads and Landing Pages (3 ad creatives, all landing on homepage)
- Google Ads Transparency Center (2 screenshots, ~30+ ad units)
- Reviews & UGC (73 first-party reviews, raw/unedited)
- PageSpeed / Core Web Vitals (Lighthouse JSON, homepage + PDP)
- Current Site Screenshots (homepage, collection, PDP, cart)

**Third-party / self-researched:**
- Non-Data Context: sales brief + social/web research run, collected by the user outside the normal flow. Contains review-theme claims (Trustpilot 4.8, sizing complaints) that are directional, not first-party verified, until cross-checked against `raw/reviews.md`.
- Live homepage fetch (this audit) — supplements screenshot folds with full-page text content.
- Competitor research (this audit) — WebSearch, dated 2026-08-22.

**Skipped at collection:** Competitor Insights (self-researched instead, see below), Inspiration Sites, Email Campaigns.

## Source Findings

### Meta Ads & Landing Pages

All three Meta ads currently running land on the homepage — there is no dedicated landing page. Message match fails on all three, and fails the same way each time: the ad sells a specific in-person experience, the homepage sells generic online shopping.

- **Ad 1** ("Whalley Warehouse Shop," running since Apr 24, 2026): promises a physical shop visit with address and hours ("pop in and say hello, kettle's always on"). Homepage delivers the AXIS collection hero and Shop Men/Women CTAs — no shop address, hours, or visit messaging anywhere in the first three folds.
- **Ad 2** ("Northern Quarter Shop, Manchester," running since Jun 26, 2026): promises a visit to the Manchester shop. Homepage has zero reference to a Manchester location in the first three folds — the only shop imagery shown (fold 3) is the Whalley location, not Manchester.
- **Ad 3** ("Full walk through Whalley HQ with Marv, our founder"): promises founder-led factory/workshop video content. Homepage delivers a standard product-shopping hero, no founder story or workshop footage in the first three folds.

A live fetch of the full homepage (this audit, 2026-08-22) confirms the site does have a "FIND A STORE" section and "STORES & EVENTS" banner — but it sits well below the three folds captured, and below the review carousel and shop-interior lifestyle photo. Store-visit-intent traffic from three active ad campaigns is landing on a page where the thing the ad promised exists, but only after multiple scrolls past unrelated content.

### Google Ads

Google Ads Transparency Center (advertiser "LANX GROUP LIMITED") shows a completely different strategy from Meta: Shopping ads (product photo, price, rating), text search ads with sitelinks, and heritage-angle display ads ("Proud English company," "Proudly Northern," "Located in the beautiful Ribble Valley, Lancashire"). One ad promotes a loyalty program with "Buy Now, Pay Later" and "up to 50% off" benefits. Sitelinks include "Shoe Sizing Advice" and "Visit Our Lancashire Factory."

Google drives toward purchase intent and specific product categories; Meta drives toward physical store visits and brand story content, then routes that traffic to a generic ecommerce homepage. The two channels are not reinforcing a single value proposition — a visitor could see either message and land on a page that doesn't confirm what they just read. The BNPL offer shown in a Google ad is not visible anywhere in the PDP buy box (see Current Site Screenshots, PDP).

### Reviews & UGC

73 first-party reviews reviewed (raw/reviews.md), overwhelmingly UK-based, 5-star pattern.

#### What Customers Love

- Comfort out of the box, repeatedly described as needing no break-in: "fitted like Cinderellas slipper from the beginning" (Brian Hutton), "no need for easing in gently" (Emma Barnes), "comfortable straight from the box" (Peter, Andy, David, Philip).
- Durability and all-weather performance: worn in Andes mud, -20°C in Norway, snow in Poland, Alps skiing trips, "12 hrs a day in every condition."
- Repeat purchase behavior is strong: multiple reviewers cite owning 3, 4, 6, even 8 pairs (Ian: "Owner of 6 pairs," Patrick Willink: "I now have 8 pairs").
- In-store experience praised where mentioned: "knowledgeable sales staff," "Excellent customer service in the shop."

#### What Frustrates Customers

- **Sizing variance across models** — a real, first-party-confirmed friction point, not just a third-party claim. Multiple reviewers needed to size up or down from their normal size: Gareth ("normally wear a size 8 but it was too large... had to reorder a slightly smaller pair"), Emyr Jones ("Usually take size 8 but have found need a size 9"), Andy ("As a size 9.25 I found the size 9s a little tight"), Ammanford reviewer ("usually wear a size 10.5... they are slightly on the larger side"), Charlotte Price ("slightly tight around the tops of my feet... impossible to find a boot that accommodates that").
- **Aftercare support gap**: Patrick Willink explicitly asks LANX to "give your own after care advice" rather than referring customers to third-party aftercare partners he found subpar, despite owning 8 pairs.
- One reviewer (Sarah) wanted a colorway that isn't offered ("wish you did a navy in this style") — a merchandising note, not a site friction point.

#### Client-Actionable Insights

- Sizing variance is model-dependent and real (confirmed first-party) — worth a product/ops review of size-chart accuracy per model, separate from any PDP UI fix.
- Aftercare/care-partner referral process is a named pain point for a repeat, high-LTV customer. Worth a support/ops review of the current aftercare partner relationship.

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON reports, fetched 2026-08-22.

- **Homepage** (lanxshoes.com/): Performance score 61/100. FCP 3.1s, **LCP 6.6s**, TBT 190ms, CLS 0, Speed Index 8.6s, **Time to Interactive 31.2s**.
- **PDP** (Ribchester Conker Distressed): Performance score 55/100. FCP 3.3s, **LCP 18.4s**, TBT 260ms, CLS 0, Speed Index 10.3s, **Time to Interactive 31.8s**. Best Practices audit did not complete (runtime error); ImageElements artifact collection hit a PROTOCOL_TIMEOUT — the audit itself could not fully load the page.
- Both reports carry a warning about possible IndexedDB-stored data skewing results; an incognito re-test is recommended to confirm these numbers before committing budget against them.

Even accounting for that caveat, an 18.4s LCP and 31+ second Time to Interactive on the PDP — the page every ad in this audit ultimately drives toward — is severe. A visitor from a paid ad is unlikely to wait 18 seconds to see the largest content element render.

### Competitor Analysis

`raw/competitors.md` was not collected (skipped at intake). The comparison below is self-researched via WebSearch, dated 2026-08-22.

| Brand | Position | Notable difference from LANX |
|---|---|---|
| Cheaney | Family-owned, Northamptonshire, since 1886 | Longer heritage claim (139 years vs. LANX's <10), full in-house factory production story |
| Crockett & Jones | Northampton, since 1879, Goodyear welted | Established craftsmanship pedigree, higher average price point |
| Solovair | Heritage to 1881, handmade Goodyear welted | Similar handmade/heritage positioning, older brand story |

LANX's own positioning (young brand, <10 years, "Something solid at the centre," bridging formal/outdoor) sits in a market where competitors lean on multi-generation heritage claims. LANX's differentiators — active social-proof volume (6,352-6,612 reviews depending on snapshot date), an RE-LANX repair/trade-in program, and a founder-accessible brand story (Ad 3) — are underused on-site relative to how hard the ads push them.

### Emails

Not collected (skipped at intake — not selected as a source in the manifest).

### Inspiration Sites

Not collected (skipped at intake).

### Non-Data Context

Third-party research (sales brief + social/web scan, prepared 2026-08-21, provided outside the normal collection flow) flags:

- **AXIS collection launched 13 August 2026**, 8 days before this audit — traffic is actively being driven to new PDPs, making this a live optimization window.
- Trustpilot reports 4.8 stars / ~2,000 reviews / 93% five-star (third-party source; not the same as the on-site 4.79/6,612 shown in first-party screenshots — different review platforms, consistent directionally).
- RE-LANX (repair/trade-in for loyalty credits) is flagged as an underused conversion asset — confirmed by this audit's own PDP screenshot review, which shows no RE-LANX or care/repair messaging near the buy box.
- Social listening (Reddit, last 30 days) returned no relevant evidence — LANX is not part of active organic community conversation. This is a coverage gap, not a finding; it means CRO impact is more directly tied to the paid/CRM-driven traffic this audit's ad and speed data already covers.

### Current Site Screenshots

**Homepage:** Hero is 100% lifestyle photography (street scene) with AXIS branding and Shop Men/Women CTAs — no product imagery until well past fold 3. Reviews (4.79 stars, 6,612 reviews) appear starting fold 2, ahead of any product grid. A live fetch confirms the page does contain "FIND A STORE," free shipping/returns banners, and a "NEW: MEN'S SCORTON TAUPE" callout, but none of this appears in the three folds captured, meaning ad traffic scrolling only partway sees none of it.

**Collection page:** 4-column grid, 112 products in Men's. A "GET 10% OFF" floating banner persists bottom-right across all three folds captured, overlapping the same screen region on every scroll. Star ratings and review counts appear under price starting fold 2 — fold 1 product cards show only color swatches, no rating. No sale/compare-at pricing visible on any card.

**PDP:** Single-purchase buy box only (no subscription/bundle tiers). Sticky right-column buy box holds price, rating, color/size selectors, and a "SELECT SIZE" primary CTA that starts in a disabled/placeholder state. The "SIZING ADVICE" link sits as a small pencil-icon text link positioned far to the right of the size-grid header — easy to miss, and disconnected from the size grid it's meant to support. This directly matches the sizing-variance friction confirmed in first-party reviews above. Free shipping/returns and shoe-care messaging appear as a checklist below the CTA (fold 2 onward) — not adjacent to the size selector or CTA button itself, where sizing anxiety is highest. No RE-LANX or BNPL messaging anywhere in the buy box, despite both being active selling points elsewhere (RE-LANX in third-party context, BNPL in a live Google ad).

**Cart:** Slide-out drawer with one AOV mechanic already in place — a 20%-off "Shoe Care Bundle" upsell (€36,85 struck through to €29,48) and a sock cross-sell. "CHECKOUT" CTA is full-width and clear, but sits at the very bottom of the drawer, after the recommended-products block, and is not sticky.

## Cross-Source Themes

1. **Ad-to-site message match failure (highest evidence strength).** All 3 active Meta ads (visual summary, live homepage fetch) promise a specific in-person or founder-story experience; the homepage delivers none of it in the visible fold range. This is evidenced by every Meta ad reviewed plus a same-day live fetch confirming the content exists but is buried. Funnel importance: highest — this is the very first thing paid traffic sees.
2. **Sizing variance is real and under-addressed at the point of decision.** Confirmed independently by first-party reviews (5+ reviewers describing model-dependent size adjustments) and by the PDP screenshot review (sizing-advice link visually disconnected from the size grid). Third-party context corroborates from a separate data source (Trustpilot). Revenue potential: high — sizing uncertainty is a documented purchase-blocker for a £180-240 product with free returns but real return-process friction.
3. **Critical page load performance on the exact pages ads drive to.** PDP LCP of 18.4s and homepage LCP of 6.6s (PageSpeed, single source but severe) sit directly in the path of every ad reviewed in this audit. Funnel importance: highest, though evidence strength is single-source and carries a data-quality caveat (IndexedDB warning) that should be re-verified before large investment.

## Top Test Opportunities

**Store-visit ad landing experience** — Three active Meta ads (running since April/June 2026) promise a physical shop visit or founder walkthrough with zero mention of it in the first three homepage folds visitors land on; the "FIND A STORE" content that would fulfill the promise exists but sits multiple scrolls below. Evidence: meta-ads-visual-summary.md (Ads 1-3), live homepage fetch (2026-08-22). Est. lift: sessions/mo, AOV, and current CVR not collected — cannot estimate $ without these inputs (see Missing Data).

**PDP sizing advice repositioning** — On the Ribchester PDP, "SIZING ADVICE" is a small pencil-icon text link positioned far right of the size-grid header, disconnected from the 18-option size grid itself. Move a per-model fit guide inline, directly above or beside the size selector. Evidence: site-visual-summary.md (PDP layout anomaly), raw/reviews.md (5+ reviewers reporting model-dependent size adjustments), raw/context.md (third-party sizing-complaint corroboration). Est. lift: inputs not collected — see Missing Data.

**PDP and homepage load speed** — PDP Largest Contentful Paint measured at 18.4s, homepage at 6.6s (Lighthouse, 2026-08-22); Time to Interactive exceeds 31s on both. These are the exact pages every ad in this audit routes to. Evidence: raw/pagespeed.md. Note: reports flag a possible IndexedDB skew — recommend an incognito re-test before scoping engineering work. Est. lift: inputs not collected — see Missing Data.

**RE-LANX objection-handling block on PDP** — RE-LANX (repair/trade-in for loyalty credits) is a differentiator not shown anywhere in the buy box on the Ribchester PDP screenshots reviewed. Add a compact "buy once, we'll maintain it" block near the CTA. Evidence: raw/context.md (sales brief flags this as underused), site-visual-summary.md (confirms absence from PDP buy box in folds 1-3). Est. lift: inputs not collected.

**Trust signals repositioned near PDP CTA** — Free UK shipping/returns and shoe-care messaging currently appear as a checklist below the buy box (visible from fold 2 onward), not adjacent to the size selector or "SELECT SIZE" button where purchase hesitation peaks. Evidence: site-visual-summary.md (PDP fold 1 vs. fold 2 comparison). Est. lift: inputs not collected.

**Homepage product visibility for ad traffic** — First three homepage folds are 100% lifestyle/location photography and reviews; no product grid or bestsellers module appears until below fold 3. Ad traffic (both Meta and Google) that scrolls only partway never sees a product. Evidence: site-visual-summary.md (Homepage folds 1-3), meta-ads-visual-summary.md. Est. lift: inputs not collected.

**BNPL message match on PDP** — A live Google ad promotes "Buy Now, Pay Later," but the PDP buy box (Ribchester, single price €219.95) shows no BNPL option or badge. Evidence: raw/google-ads-visual-summary.md (loyalty ad), site-visual-summary.md (PDP buy box detail — single price, no installment messaging). Est. lift: inputs not collected.

**PDP primary CTA default state** — The "SELECT SIZE" button, the PDP's primary CTA, is captured in a disabled/placeholder state on load, requiring a size selection before it activates. Test clearer visual affordance or a pre-selection prompt tied to the sizing-advice fix above. Evidence: site-visual-summary.md (PDP fold 1, buy box detail). Est. lift: inputs not collected.

**Cart drawer checkout CTA position** — The "CHECKOUT" button sits at the very bottom of the cart drawer, after the Recommended-products upsell block, and is not sticky. Evidence: site-visual-summary.md (Cart section). Est. lift: inputs not collected.

**Collection page persistent discount banner** — A "GET 10% OFF" banner floats bottom-right and persists across all three collection-page folds captured, occupying the same screen region on every scroll (fold 1 through fold 3). Untested whether this aids or competes with product-card CTAs at this frequency. Evidence: site-visual-summary.md (Collection page folds 1-3). Est. lift: inputs not collected.

## Unused but Valuable Findings

- Google and Meta campaigns promote entirely different value props (purchase-intent/heritage vs. brand-story/store-visit) with no unifying message reinforced anywhere on-site — a brand-messaging alignment project, not a single test.
- First-party reviews show strong repeat-purchase behavior (customers with 3-8 pairs) — an under-leveraged loyalty/VIP messaging angle not currently visible in the screenshots reviewed.
- Aftercare support is a named gap for a high-LTV repeat customer (Patrick Willink review) — an ops/support fix, not a CRO test.

## Missing Data

- **Monthly sessions and AOV**: not present in manifest or any collected source. Every Est. lift line above is qualitative only — the roadmap step will need these figures (or explicit placeholders) to produce dollar estimates.
- **Competitor Insights**: skipped at collection; this audit's competitor table is self-researched (WebSearch, 2026-08-22) and limited to positioning, not pricing or feature-level detail.
- **PDP Best Practices score**: Lighthouse audit did not complete for the PDP (PROTOCOL_TIMEOUT on ImageElements collection) — no Best Practices score available for that page.
