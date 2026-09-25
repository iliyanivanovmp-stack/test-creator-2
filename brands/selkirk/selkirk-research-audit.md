# Selkirk Sport CRO Research Audit

## Data Sources Used

- Meta Ads and Landing Pages (3 ads, screenshot-based visual summary + captured landing page folds)
- Google Ads Transparency Center (2 screenshots, visual summary)
- Reviews & UGC (Amazon reviews, client-provided, SLK Neo Pickleball Paddle Set)
- PageSpeed / Core Web Vitals (Lighthouse mobile, homepage + Project Boomstik PDP, fetched 2026-09-10)
- Non-Data Context (client note on homepage CTA routing)
- Current Site Screenshots (homepage, collection, PDP, cart)
- Live homepage fetch (WebFetch, selkirk.com, 2026-09-10)
- Social & Community Research, last30days-ecom engine (window: 2026-08-11 to 2026-09-10)

Not collected/skipped: Competitor Insights, Inspiration Sites, Email Campaigns (not selected in manifest).

## Source Findings

### Meta Ads & Landing Pages

Three active ads captured, all showing message-match gaps between ad promise and landing page delivery:

- **Ad 1 (AMPED Pro Air - Epic):** Ad copy promises "deals" and "markdowns... limited quantities." The landing page shows the paddle at full price ($100) with a "Free Gift With Purchase" badge but no discount, sale price, or strikethrough pricing anywhere in the captured folds. The "deal" framing is not visually confirmed on-site.
- **Ad 2 (Vanguard Power Air - S2):** Two mismatches. Price: ad creative overlays "$130.00," landing page shows "$100.99." Availability: ad's CTA is "Shop Now" implying purchasable stock; landing page's primary button reads "Out of stock" (disabled, gray) with only a "Notify me when back in stock" option. A minor stat mismatch also appears (ad shows Control 6.5, on-page slider shows Control 7).
- **Ad 3 (Tacky Grip Towel, $7):** Ad headline is a 5-star testimonial about paddle quality and "outstanding" customer service, used to promote a $7 grip towel — the testimonial content doesn't reference the towel. Price and product image match between ad and landing page. Directly below the fold on the landing page, the first visible individual reviews are mixed: a 2-star "Not great... I do not recommend this product" review and a 3-star durability complaint, sitting alongside 5-star reviews — visitors arriving on a 5-star-testimonial ad see negative reviews within one scroll.

All three landing pages share the same trust-badge stack (Limited Lifetime Warranty, Free Shipping $55+, 30-Day Guarantee) directly under the CTA, and an embedded chat widget.

### Google Ads

Google Ads Transparency shows 30+ active ad units (Shopping/image, video, and search/sitelink formats) across Selkirk Sport, LLC, Selkirk Sport, and a Malaysia-region entity. Headline focus is the Selkirk LABS Project Boomstik and the new OMNI paddle launch, plus pro/competitive brand positioning and product education. Two Shopping ads carry explicit percentage-off badges (-37% on Legacy Pro shoes, -30% x2 on an apparel bundle).

**Gap vs. Meta:** No discount codes or percentage-off badges appear anywhere in the captured Meta ad set, despite Google Ads showing them for other product lines. Featured products do not overlap between the two channels captured (Google: Boomstik/OMNI/shoes/apparel; Meta: AMPED Pro Air, Vanguard Power Air, towel). One error-state ad card ("Google 500... There was an error") was visible in the transparency grid — not actionable for CRO, noted for completeness only.

### Reviews & UGC

#### What Customers Love

- Large, forgiving sweet spot and easy topspin generation from the textured face — repeated across multiple reviewers of the SLK Neo set.
- Comfortable, cushioned grip that stays easy on the hand over multiple games.
- Strong perceived value at entry-level price point: "excellent value," "nice quality for beginners to intermediate players."
- Bundled carrying case/bag called out positively as a nice inclusion.

#### What Frustrates Customers

- One reviewer noted the entry-tier set's material felt "low par," planning to "move up to a better product once these fall apart" — a signal that the base tier is viewed as a stepping-stone rather than a durable long-term purchase.
- No major complaints beyond that in the client-supplied Amazon review set (all other reviews 4-5 stars).

#### Client-Actionable Insights

- The reviewed product (SLK Neo Pickleball Paddle Set) is positioned and purchased almost entirely as a beginner/gift/raffle-prize item ("Perfect set for a beginner," "raffle prizes for a pickleball club tournament") — product marketing for this SKU could lean further into the beginner/gift use case rather than performance framing used elsewhere in the catalog.
- No support or fulfillment complaints appear in this review set; this is a narrower signal than the Trustpilot/warranty findings below and should not be read as evidence that support is friction-free brand-wide.

### PageSpeed / Core Web Vitals

Lighthouse mobile, collected 2026-09-10:

- **Homepage (selkirk.com):** Performance 64/100. LCP 12.0s, FCP 3.3s, Speed Index 5.7s, Time to Interactive 12.6s, TBT 20ms, CLS 0.
- **PDP (Project Boomstik):** Performance 63/100. LCP 9.9s, FCP 3.5s, Speed Index 6.4s, Time to Interactive 13.5s, TBT 40ms, CLS 0.

Both pages pass on layout stability (CLS 0) and low blocking time, but LCP is severely degraded on both — roughly 4-5x Google's "good" threshold (2.5s) — and Time to Interactive exceeds 12 seconds on both templates. This is a mobile-specific finding; no desktop scores were collected.

### Competitor Analysis

Not selected as a source in this collection (manifest: "not provided; not selected"). Skipped.

### Emails

Not selected as a source in this collection. Skipped.

### Inspiration Sites

Not selected as a source in this collection. Skipped.

### Non-Data Context

Client flagged one specific issue directly: the homepage's main CTA button routes to the Pro Line 2.0 Bags collection page, not to paddles — the brand's core product. This is treated as a confirmed client priority, not a hypothesis, and is corroborated independently by the site screenshots below.

### Social & Community Research

Window: 2026-08-11 to 2026-09-10, via last30days-ecom engine. Findings below are directional (third-party/community data) unless noted as corroborated.

- **Durability/performance retention (Boomstik):** A TikTok video ("My Boomstik is STILL going strong," 4,135 views, 96 likes) and its top comment both describe the paddle holding power and spin after 6-12+ months of use. This is **corroborated** by Amazon's broader paddle-line ratings (LUXX Control 4.4/5 at 596 ratings, SLK ERA Power 4.5/5 at 264 ratings, Amped 4.4/5 at 351 ratings) — a consistent quality signal beyond the beginner-tier reviews the client supplied directly.
- **Warranty/returns friction:** Trustpilot (580+ reviews, ~4 stars) surfaces reports of paddles warping/developing dead spots and friction in the warranty claims process (customers asked to pay shipping for a warranty assessment). Independently, the official Project Boomstik product page's own web copy states "Exchanges are unavailable" alongside its "30-Day Free Returns" messaging. These are two independent sources pointing at the same theme (post-purchase support terms) — this is corroborated directionally, though neither the client review set nor the site screenshots directly confirm the warranty-shipping-cost complaint.
- **Price skepticism:** A single YouTube comment thread challenges paddle cost-to-manufacture ratio ("$100 CEO / $100 marketing... $30 to make the paddle"); this drew both agreement and pushback (25-37 likes each side) — a minority signal, not corroborated elsewhere, flagged as unconfirmed.
- **Counterfeit awareness:** TikTok search surfaced "real vs. fake Boomstik" comparison content, indicating counterfeit product is a known issue in the community. Not a CRO test opportunity; flagged for client awareness only.
- Reddit was skipped (precheck returned zero brand/category-relevant results). X returned 0 posts in the 30-day window despite active branded accounts — no fresh signal.

### Current Site Screenshots

**Homepage:** The single hero CTA ("Buy Now") is entirely bag-focused — banner reads "THESE BAGS KNOW BALL / PRO LINE 2.0 BAG SERIES." The fold-2 product carousel's first two slots are also a backpack and a paddle rather than a mixed best-seller set. The four-tile category grid in fold 3 (Paddles, Clothing, Gear, Footwear) is the first point on the homepage offering a direct path to Paddles specifically — meaning a visitor must scroll past two full folds before reaching a paddle-specific entry point. No sticky header/CTA observed. No review count or star rating visible anywhere on the homepage itself, despite paddle PDPs showing hundreds to thousands of reviews. A live fetch of the homepage (2026-09-10) shows the underlying nav does include a full Paddles category and rotating hero sections — but the specific hero state captured in screenshots, which is what most visitors landing from ads or direct traffic will see first, is bags-only.

**Collection page:** This is confirmed to be the exact destination of the homepage's "Buy Now" CTA, and it is a 3-SKU, bags-only collection (Tour Backpack $298, Team Backpack $248, Duffle $198) with no paddles, apparel, or other product types. This directly confirms the client-flagged issue: a visitor clicking the primary homepage CTA to browse Selkirk's core product (paddles) lands on a page with zero paddles.

**PDP (Project Boomstik):** Clear breadcrumb and 2,664-review star rating above the title. Buy box is single-purchase only (no subscription/bundle toggle). A red "Ships in 2-3 weeks" shipping note sits directly above the Add to Cart button — a friction point for a $333 purchase with immediate-gratification expectations. "Frequently Bought Together" uses four separate "Quick Add" buttons rather than one combined bundle CTA. No layout anomalies observed.

**Cart:** A red warning banner sits at the top of the cart drawer: "Some items in your cart have a shipping delay & will delay your entire order. Please place two separate orders if you would like your other items sooner." This compounds the PDP's "Ships in 2-3 weeks" note and appears with no trust badge, guarantee, or returns copy anywhere in the cart drawer to offset it. A "$45 off premium paddle case" AOV module appears below the order summary.

## Cross-Source Themes

Ranked by evidence strength, revenue potential, and funnel importance:

1. **Homepage-to-collection message match for paddles.** Evidence: client context note, site screenshots (homepage + collection page), live homepage fetch. This is the highest-confidence, highest-funnel-position issue — the core product category is effectively unreachable from the primary homepage CTA.
2. **Ad-to-landing-page message match failures (Meta).** Evidence: meta-ads-visual-summary across all 3 captured ads (pricing mismatch, stock mismatch, unrelated testimonial, no-discount-shown "deal" framing). Directly affects paid-traffic conversion on the exact pages driving spend.
3. **Mobile site performance (LCP).** Evidence: PageSpeed data for both homepage and PDP, independently. 9.9-12.0s LCP on mobile is a top-of-funnel and PDP-level conversion tax that touches every visitor regardless of entry point.

## Top Test Opportunities

**Fix homepage hero CTA to route to paddles or general shop, not bags-only collection** — The homepage hero banner and its single "Buy Now" CTA are 100% bag-focused, sending traffic to a 3-SKU bags-only collection with zero paddles, apparel, or other products. Selkirk's core product is paddles. Evidence: context.md (client-flagged), site-visual-summary (homepage fold 1, collection page fold 2). Est. lift: conservative CR lift on paddle-category entry rate; sessions/mo and AOV not available in collected data — cannot quantify $ without inventing figures.

**Restore purchasability or remove "Shop Now" framing for the out-of-stock Vanguard Power Air ad** — Meta Ad 2 shows "Shop Now" and a purchasable-looking $130 paddle; the landing page's primary CTA is disabled ("Out of stock") with only a "Notify me" option, and the price shown ($100.99) doesn't match the ad ($130.00). Every click from this ad currently lands on a dead-end buy box. Evidence: meta-ads-visual-summary (Ad 2).

**Add visible discount/sale pricing to match "deals" and "markdowns" ad copy on AMPED Pro Air LP** — Ad 1 promises markdowns and limited-quantity deals; the landing page shows the paddle at full price ($100) with no strikethrough, sale badge, or discount code applied. Visitors clicking on a deal promise see full price. Evidence: meta-ads-visual-summary (Ad 1).

**Reduce mobile LCP on homepage and PDP templates** — Homepage LCP is 12.0s and PDP (Boomstik) LCP is 9.9s on mobile Lighthouse, roughly 4-5x Google's 2.5s "good" threshold, with Time to Interactive exceeding 12-13 seconds on both. Evidence: pagespeed.md (homepage + PDP, Lighthouse mobile, 2026-09-10).

**Re-pair or reframe the towel ad's testimonial with product-relevant social proof** — Ad 3 leads with a 5-star testimonial about paddle quality to sell a $7 towel; the towel's own landing page shows a 2-star "I do not recommend this product" review and a 3-star durability complaint directly below the fold, visible within one scroll of arriving from a 5-star-framed ad. Evidence: meta-ads-visual-summary (Ad 3).

**Soften or relocate the cart's shipping-delay warning banner** — The cart drawer opens with a red warning telling shoppers to "place two separate orders" to avoid delay, with no trust badge or returns copy anywhere in the drawer to offset it. This sits at the bottom of the funnel, directly before checkout. Evidence: site-visual-summary (cart).

**Address the PDP's "Ships in 2-3 weeks" friction on a $333 purchase** — The Boomstik PDP shows a red 2-3 week shipping note directly above the Add to Cart button for the flagship $333 paddle — the same paddle receiving the heaviest Google Ads spend (Boomstik-focused search/Shopping ads). Evidence: site-visual-summary (PDP), google-ads-visual-summary (Boomstik ad emphasis).

**Convert "Frequently Bought Together" from individual Quick Adds to one combined bundle CTA** — Both the AMPED Pro Air and Boomstik PDPs show 4-item "Frequently Bought Together" rows requiring a separate Quick Add click per item, rather than one combined "Add all to cart" action. Evidence: meta-ads-visual-summary (Ad 1, Ad 2 LP folds), site-visual-summary (PDP fold 3).

**Add review count/star rating to the homepage** — PDPs carry hundreds to thousands of reviews (623-2,664) and a 4.7-star aggregate, but none of that trust signal appears anywhere on the homepage itself in the captured folds. Evidence: site-visual-summary (homepage, no review signal noted across all 3 folds), contrasted with PDP/LP review counts in meta-ads-visual-summary and site-visual-summary.

**Surface a clearer warranty/exchange policy on PDP and cart** — Two independent sources point at the same friction theme: Trustpilot reports of being charged shipping for a warranty assessment, and the official Boomstik product page's own copy noting "Exchanges are unavailable" alongside "30-Day Free Returns." Neither the PDP nor cart screenshots show exchange/warranty-claim terms up front. Evidence: last30days-ecom (Trustpilot, Web), site-visual-summary (PDP, cart — policy language absent from captured folds).

## Unused but Valuable Findings

- Amazon paddle-line ratings (LUXX Control, SLK ERA Power, Amped) show hundreds of ratings each at 4.4-4.5 stars, indicating broad sell-through beyond the beginner SLK Neo set the client supplied reviews for — useful context for future review-sourcing but not a standalone test.
- Counterfeit "real vs. fake Boomstik" content exists in the TikTok community — a brand-protection issue, not a CRO test.
- Google Ads Transparency shows a Malaysia-region advertiser entity with no equivalent regional variant observed in the Meta set — worth a follow-up scope question for the client, not a test.

## Missing Data

- No sessions/mo or AOV figures were available in any collected source, so dollar-value lift estimates could not be calculated for any Top Test Opportunity above without inventing numbers. The roadmap should carry conservative CR-lift ranges only.
- No desktop PageSpeed data was collected — mobile Lighthouse only.
- Meta Ads landing page URLs were not provided as text (only screenshots), so live-fetch verification of current LP state (e.g., whether Vanguard Power Air is still out of stock) was not possible; findings reflect the screenshot capture only.
- Competitor Insights, Inspiration Sites, and Email Campaigns were not selected as sources in this collection and are not covered in this audit.
