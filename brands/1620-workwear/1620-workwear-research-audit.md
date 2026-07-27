# 1620 Workwear CRO Research Audit

**Date:** July 25, 2026
**Store:** https://www.1620usa.com/
**Slots:** 8

---

## Data Sources Used

**User-provided:**
- Meta Ads visual summary (raw/meta-ads-visual-summary.md) — 3 ad creatives + 9 LP screenshots
- Meta Ads landing page URLs (raw/meta-ads.md)
- Google Ads visual summary (raw/google-ads-visual-summary.md)
- PageSpeed / Core Web Vitals (raw/pagespeed.md — Lighthouse JSON, mobile simulation, July 25, 2026)
- Site visual summary (raw/site-visual-summary.md) — homepage, collection, cart screenshots
- Non-data context (raw/context.md)

**Self-researched:**
- Live fetch: https://www.1620usa.com/ (July 25, 2026)
- Live fetch: https://www.1620usa.com/products/stretch-nyco-double-knee-utility-pant (July 25, 2026)

**Not collected:**
- Customer reviews (client confirmed none available)
- Competitor data (skipped per manifest)
- Email campaigns (skipped)
- Inspiration sites (skipped)
- PDP screenshots (data sourced from Meta Ad LP screenshots only)

---

## Source Findings

### Meta Ads & Landing Pages

Three ads running as of audit date (May 12 and July 10, 2026 start dates). All run on Facebook, Instagram, Messenger, and Audience Network.

**Ad 1 — Testimonial, Preorder Variant**
Creative: Long-form testimonial from A.J. Gorder ("loyal customer since day one... I don't own any other brands anymore"). Flat-lay product image of black pants. CTA: "Shop Now." LP: Double Knee Utility Pant 2.0, $228, Size 38/Meteorite — sold out. The buy box shows a red preorder scheduling block with three timeline rows: "March 2026: SOLD OUT / Mid April 2026: 25% RESERVED / June 2026: IN PRODUCTION." As of late July 2026, all three dates have passed. The CTA reads "PREORDER." The preorder block has not been updated and the dates reference a production run that has either shipped or stalled — the page gives no indication. Trust badges (Made in USA, Guaranteed for Life, Free Exchanges) appear below the preorder block in fold 2, not in fold 1. An email capture popup ("GET 10% OFF!") overlaps content in the lower left.

Message match: Partial. The testimonial implies in-stock purchase of a flagship product. The LP delivers a stale preorder experience with expired dates. Significant trust risk for paid traffic.

**Ad 2 — Same Creative, In-Stock Variant**
Virtually identical creative to Ad 1 (same testimonial copy, same image, same CTA). Targets size 40/Meteorite — this variant is in stock. LP shows "ADD TO CART" instead of "PREORDER." Trust badges appear in fold 1 below the ATC button. Bundle offer ("BUY 3 & GET 1 FREE") visible in fold 1. Email popup still present.

Message match: Good. Ad implies a premium in-stock product; LP delivers one. Best-performing message match of the three ads.

**Ad 3 — UGC Durability, Closeout LP**
Creative: UGC-style testimonial about extreme durability ("tougher than a tire swing... Best pants I own... 6 pairs of Duluth with blown-out knees after 6 months"). Photo: person in visibly dirty/muddy pants on a worksite. Headline: "American Made Workwear." CTA: "Shop Now." LP: Single Knee Utility Pant 2.0 — **CLOSEOUT - FINAL SALE**, $132. Multiple sizes crossed out. No trust badges in fold 1. "CLOSEOUT - FINAL SALE" is the second word of the product title.

Message match: Weak. The ad's entire angle is "this is my go-to brand, I own 6 pairs" — loyalty and durability. The LP immediately signals product discontinuation and limited size availability. The UGC reviewer (Joseph, 06/17/2026) whose words appear in the ad is visible in the LP reviews, which is a positive continuity signal — but the discontinuation context undercuts the brand loyalty message.

---

### Google Ads

Multiple formats observed: search text ads, display image ads, shopping/product listing ads.

**Headline themes:** "Guaranteed for Life — Pants Last Up to 5x Longer," "1620 Workwear — The Best Workwear. Period.," "American Made Workwear and Gear," "Rated Best Overall Work Pants — Labor Day Sale — 20% Off."

**Channel conflicts:**
- Google search ads feature "Labor Day Sale — 20% Off." The homepage and site-wide announcement bar show "Retirement Sale up to 50% off." Two different sale names, two different discount levels, running simultaneously across channels. A customer who clicks from Google expecting a specific 20% Labor Day discount lands on a page announcing a 50% Retirement Sale — different framing, different discount depth.
- Meta ads run no sale messaging at all. Google is the only channel actively promoting a discount.

**Broken price rendering:** The Full Tech Work Hoodie (Hi Vis) Shopping ad shows "[Price]" as the price, rendered as "[Price] / By Google." Broken price placeholder means this product is appearing in Shopping without a price, which typically suppresses CTR on Shopping placements.

**Rating discrepancy:** Google search ads cite "4.8 advertiser rating" (554 reviews in one instance). PDP star ratings show 4.5 across products. The Google rating is a brand/seller aggregate; the discrepancy is not inherently deceptive but may create a mismatch in customer expectations at the product level.

**Visual approach:** Shopping and display ads use clean product-on-white imagery across multiple colorways. One text-heavy display ad lists product categories (Men's Work Pants, Workwear, Tops, Trousers, Utility Workwear Pants) — purely navigational, no conversion hook.

---

### Reviews & UGC

No standalone customer review file was collected. Client confirmed no reviews were available for collection.

**PDP-level review data observed in screenshots (ad landing pages):**
- Double Knee Utility Pant 2.0: 4.5 stars, 419 reviews. Rating distribution: 75% 5-star, 10% 4-star, 5% 3-star, 5% 2-star, 5% 1-star. Recent reviews (Jul 3, Jun 27, Jun 12, Jun 6, Apr 20, 2026): all 5-star, praising durability, pocket design, and comfort for construction work.
- Single Knee Utility Pant 2.0: 4.5 stars, 311 reviews. Rating distribution: 84% 5-star, 9% 4-star, 4% 3-star, 3% 2-star, 1% 1-star. Notable review: Tony (03/17/2026) — "If Chuck Norris were pants... first product review I have ever written in my 50+ years... completely changed the way I work." Another: Chris (02/14/2026) noted need to size up.

**What Customers Love**
- Extreme durability — lasting years vs. competitor pants failing in months ("6 pairs of Duluth with blown-out knees after 6 months")
- Utility and pocket design for construction/trade work ("a lot of pockets and well thought out for construction work")
- Long-term brand loyalty once purchased ("don't even own any other brands anymore")
- American-made quality and lifetime guarantee

**What Frustrates Customers**
- Sizing variability — Chris noted needing to size up; inseam customization adds complexity
- Price point — $228 for a pant is a high initial commitment, likely creating hesitation even among convinced buyers
- Preorder/availability issues — size-specific stockouts visible in screenshots with no clear restock timeline

**Client-Actionable Insights**
- Sizing guidance at purchase (a fit quiz or "customers who bought X also bought Y size" note) could reduce exchanges driven by sizing variability
- Restock notification on out-of-stock sizes would capture demand that otherwise bounces from PDPs
- The lifetime guarantee is a strong differentiator but appears below the fold on the preorder variant — surfacing it earlier in the buy box could reduce price-resistance abandonment

---

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON, mobile simulation, Chrome 150, July 25, 2026.

**Homepage (https://www.1620usa.com/)**
- Performance: 62/100
- FCP: 2.7s
- LCP: 11.7s (failing — threshold 2.5s)
- Speed Index: 8.1s
- TBT: 130ms
- CLS: 0 (passing)
- TTI: 21.9s
- Page size: 5,012 KiB
- Long tasks: 9

**PDP / Ad Landing Page (https://www.1620usa.com/products/stretch-nyco-double-knee-utility-pant)**
- Performance: 41/100
- FCP: 3.2s
- LCP: 42.9s (critically failing — 17x above threshold)
- Speed Index: 12.4s
- TBT: 710ms (failing — threshold 200ms)
- CLS: 0.081 (approaching threshold of 0.1, 1 layout shift noted)
- TTI: 43.4s
- Page size: 7,986 KiB
- Long tasks: 20

The PDP score of 41/100 with a 42.9s LCP is critically broken. A page that takes 43 seconds to become interactive on mobile will lose a significant share of paid ad traffic before the buy box is ever visible. The 710ms TBT means the main thread is heavily blocked — heavy JavaScript bundles, likely third-party scripts (email capture popup, analytics, ad pixels). The 8MB page size is excessive. The homepage is in poor shape (62/100, 11.7s LCP) but the PDP is the higher-priority fix given it receives direct paid traffic.

---

### Competitor Analysis

No competitor data was provided by the client and this source was skipped per the manifest. No competitor research conducted for this audit.

---

### Emails

Not collected.

---

### Inspiration Sites

Not collected.

---

### Non-Data Context

- No customer reviews available — the client confirmed there are no accessible review sources for this brand outside of on-site PDP reviews.
- Ad 1 landing page contains stale preorder dates referencing March, April, and June 2026 production batches. As of late July 2026, all three dates have passed. The preorder scheduling block has not been updated, which will read to first-time visitors as either: (a) the product is permanently unavailable, or (b) the brand doesn't manage its storefront actively. Either perception is damaging for paid ad traffic with commercial intent.
- The brand is running a "Retirement Sale" — suggesting this may be a wind-down of certain product lines (consistent with the volume of CLOSEOUT - FINAL SALE items in the collection).

---

## Cross-Source Themes

**1. The sale promise has no proof at the product level (strongest evidence: site screenshots + Meta ads + Google ads)**
Every channel entry point — the announcement bar, the hero, Google search ads — signals sale pricing. But the product grid shows full prices with no strikethrough. CLOSEOUT items are identified only by title text ("- CLOSEOUT - FINAL SALE"), not by visual price contrast. The one exception (Full Tech Sweatpant) in fold 3 of the collection page shows a compare-at price. The disconnect between a loud sale announcement and invisible sale savings across 90%+ of product cards is the highest-funnel conversion leak.

**2. Cross-channel messaging is inconsistent, creating trust fragility (evidence: Google ads + Meta ads + homepage + LP screenshots)**
Google runs "Labor Day Sale — 20% Off." The homepage announces "Retirement Sale — Up to 50% Off." Meta runs no sale copy at all. Ad 3 sends loyalty/durability traffic to a closeout product. Ad 1 sends "Shop Now" traffic to a stale preorder. Each channel tells a different story. A customer exposed to multiple touchpoints sees conflicting offers and unclear product status — damaging the premium brand perception the testimonial creative is trying to build.

**3. The PDP is critically slow and structurally under-optimized for paid traffic conversion (evidence: PageSpeed + LP screenshots)**
A 42.9s LCP and 43.4s TTI on the primary paid traffic destination (Double Knee Utility Pant 2.0 PDP) means many ad clicks bounce before the page loads. For those who stay: trust badges are below the fold on the preorder variant, the bundle offer appears mid-page, no sticky ATC is present, and an email capture popup competes with the buy box in the lower left. The performance failure amplifies every UX problem — a slow page with a good buy box loses more users than a fast page with a mediocre one.

---

## Top Test Opportunities

Ranked by evidence strength x revenue potential x fixability. Written for 8 slots (10 entries, 2 backups).

**1. Sale Price Visibility on Product Cards** — The announcement bar, hero, and Google ads all promise "Retirement Sale up to 50% off," but product cards across the homepage grid and collection page show only full prices. CLOSEOUT - FINAL SALE items have no visual price differentiation — their sale status is communicated only via a text suffix in the product title. Shoppers who arrived expecting to see discounts see a full-price grid and may conclude the sale doesn't apply to what they want, or that the brand is misleading them. Evidence: site-visual-summary.md (homepage fold 2-3, collection fold 2-3), Google Ads (sale headline), Meta Ads (no sale messaging — baseline contrast). Est. lift: 8% CR lift x unknown sessions x $228 AOV = uncalculated without traffic data; high priority regardless.

**2. Fix Stale Preorder Block on Ad 1 LP (Size 38 Variant)** — Ad 1 is an active paid campaign that lands on a PDP variant showing a preorder scheduling block with three expired dates: "March 2026: SOLD OUT / Mid April 2026: 25% RESERVED / June 2026: IN PRODUCTION." As of July 25, 2026, all dates have passed. The CTA reads "PREORDER" and gives no indication of current order status, estimated ship date, or whether the batch has already shipped. This page is receiving paid traffic today. Evidence: meta-ads-visual-summary.md (Ad 1 LP fold 1), context.md. Est. lift: removing a hard trust-breaker from an active paid destination; any CR improvement is incremental revenue from existing spend.

**3. PDP Performance — LCP and TBT Reduction** — The Double Knee Utility Pant 2.0 PDP scores 41/100 on mobile Lighthouse. LCP is 42.9s (threshold: 2.5s), TBT is 710ms (threshold: 200ms), TTI is 43.4s, page size is 8MB. This is the primary destination for Meta ad traffic and likely a top-traffic organic page. At this performance level, a substantial share of mobile clicks — especially those on slower connections — never reach an interactive buy box. Evidence: pagespeed.md (PDP row). Est. lift: industry benchmark suggests 100ms improvement in load time correlates with 1-7% CR lift; at this severity level, a meaningful improvement could be significantly higher.

**4. Cart — Bundle Reinforcement and AOV Mechanic** — The cart drawer contains one product (Double Knee Utility Pant 2.0, $228) with a full-width checkout button and no additional elements. The "BUY 3 & GET 1 FREE" bundle offer visible on the PDP does not appear in the cart. There are no upsells, cross-sells, complementary product suggestions, or free-shipping threshold prompts. For a brand with a broad catalog (shirts, hoodies, shorts, tees starting at $36), the cart is a dead AOV zone. Evidence: site-visual-summary.md (cart section), meta-ads-visual-summary.md (Ad 2 LP fold 1 showing bundle offer). Est. lift: cart upsell/bundle reinforcement typically lifts AOV 5-15%; at $228 baseline, even a 5% AOV lift is meaningful at volume.

**5. Ad 3 Message Match — Align Ad to LP or Redirect** — Ad 3 uses a UGC durability testimonial ("6 pairs of Duluth with blown-out knees... 1620 is my go-to from here on out") and sends traffic to Single Knee Utility Pant 2.0 CLOSEOUT - FINAL SALE at $132 with multiple sizes crossed out. The ad's loyalty angle is contradicted by a clearance destination. Two possible fixes: repoint the ad to a full-price in-stock equivalent, or reframe the ad creative to acknowledge the sale context ("Same legendary durability, now on clearance"). Evidence: meta-ads-visual-summary.md (Ad 3), site-visual-summary.md (collection fold 2 — closeout items). Est. lift: message match alignment typically yields 10-20% LP CR improvement.

**6. Collection Page — Visual Sale Badge on Closeout Items** — The collection page lists six CLOSEOUT - FINAL SALE items mixed with full-price products in the same grid. The only visual distinction is the title suffix "- CLOSEOUT - FINAL SALE." No sale badge, no ribbon, no strikethrough price is shown on these cards. A shopper scanning for retirement sale deals cannot quickly identify which items are discounted. A high-contrast "SALE" or "CLOSEOUT" badge on the product card image (top-left corner), combined with a compare-at strikethrough price, would make the sale promise tangible and likely improve click-through from collection to PDP. Evidence: site-visual-summary.md (collection fold 2-3). Est. lift: visual sale signaling on collection pages typically improves PDP click-through 5-15%.

**7. Cross-Channel Offer Alignment — Retire "Labor Day Sale" from Google** — Google search ads currently run "Labor Day Sale — 20% Off" while the homepage announces "Retirement Sale — Up to 50% Off." These are different sale names with different discount depths. A customer clicking a Google ad expecting a 20% Labor Day discount lands on a page announcing a 50% Retirement Sale — higher discount, different framing. This creates confusion rather than delight. The Google copy should align with the site's current sale name and discount structure. Additionally, the broken price rendering ("[Price]" placeholder) on the Full Tech Work Hoodie Shopping ad suppresses CTR and should be fixed separately. Evidence: google-ads-visual-summary.md, site-visual-summary.md (homepage fold 1). Est. lift: offer consistency reduces click-to-purchase friction; difficult to isolate in testing but operationally correct.

**8. Fold 1 Trust Signal Placement on Preorder/OOS PDP Variants** — On the Ad 2 LP (in-stock, "ADD TO CART"), trust badges (Made in USA, Guaranteed for Life, Free Exchanges) and the bundle offer appear in fold 1 below the ATC button. On the Ad 1 LP (preorder, sold-out), trust badges appear in fold 2 — below the preorder scheduling block. The customer most in need of reassurance (the one facing a preorder or backorder decision) sees the trust signals last. Moving the trust badge row to immediately below the CTA button on all PDP variants (not just in-stock ones) would deliver consistent trust context at the moment of decision. Evidence: meta-ads-visual-summary.md (Ad 1 LP fold 1 vs. Ad 2 LP fold 1). Est. lift: trust signal proximity to CTA typically improves conversion 3-8% on hesitation-prone decisions like preorders.

**9. Sticky ATC Bar on PDP** — No sticky header or ATC bar is visible on the PDP screenshots. The buy box and CTA appear in fold 1; as the user scrolls through product description, features, and reviews (3+ folds of content), the CTA disappears. A sticky bar containing the product name, price, selected variant, and an ATC button would allow users who become convinced during feature/review reading to convert without scrolling back. Evidence: meta-ads-visual-summary.md (LP fold 1-3 for all three ads — no sticky bar observed). Est. lift: sticky ATC bars on content-heavy PDPs typically lift CR 2-6%.

**10. Homepage — Remove Sale Announcement/Product Price Mismatch** — The homepage hero dominates fold 1 with "RETIREMENT SALE / UP TO / 50% OFF / SELECT STYLES" and the announcement bar repeats the same message. Fold 2 immediately below shows the product grid — Foundation Utility Pant $135, Double Knee Utility Pant 2.0 $228 — at full prices with no indication of which styles are on sale or what the discounted prices are. A shopper who clicked through on sale intent and sees a full-price grid has no path to the sale without navigating away. Adding a direct "SHOP THE SALE" CTA below the hero (linking to a filtered sale/retirement collection) or displaying compare-at prices on hero-adjacent products would close the loop. Evidence: site-visual-summary.md (homepage fold 1-2). Est. lift: sale funnel continuity improvement; backs up opportunity #1 at the homepage level.

---

## Unused but Valuable Findings

- Google Shopping broken price on Full Tech Work Hoodie ("[Price]" placeholder) is suppressing CTR on that product's Shopping ad — operational fix, not a test, but worth flagging to the client immediately.
- The "Pant Comparison Guide" banner on the homepage fold 3 suggests the product lineup complexity is known internally. A quiz or comparison tool embedded on the collection page could reduce decision paralysis for first-time buyers navigating 9 pant SKUs at similar price points.
- The email capture popup ("GET 10% OFF!") appears on both ad LPs tested and overlaps content in the lower left corner. The 10% offer competes with the in-page conversion flow — an arriving buyer being asked to subscribe before they've decided to buy may be net-negative on session CR, even if list growth is positive.

---

## Missing Data

- **No customer reviews:** The client confirmed no reviews were available. Only on-site PDP review data observed in screenshots was used. Without a standalone review file, themes around pricing objections, sizing confusion, and purchase triggers are underrepresented in this audit. A reviews collection pass (Amazon if product is listed there, or scraping on-site reviews) would strengthen the test prioritization for all messaging-related opportunities.
- **No PDP standalone screenshots:** PDP data was inferred from Meta Ad landing page screenshots. The PDP in a non-ad context (direct URL, organic traffic) may render differently — particularly for variant selection default state and popup behavior.
- **No competitor data:** The Competitor Analysis section is empty. Competitive pricing and feature benchmarking would be useful context for testing the $228 price point and the bundle offer mechanics.
