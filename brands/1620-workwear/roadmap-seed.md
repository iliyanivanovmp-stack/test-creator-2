# 1620 Workwear Roadmap Seed

**Store:** https://www.1620usa.com/
**AOV:** $228 (flagship Double Knee Utility Pant 2.0; lower-tier items start at $36)
**Monthly sessions:** Unknown
**Data sources:** Meta Ads visual summary, Meta Ads landing page URLs, Google Ads visual summary, PageSpeed/Core Web Vitals (Lighthouse mobile, July 25 2026), Site visual summary (homepage, collection, cart), Non-data context, Live site fetch (July 25 2026)

---

## Key Insights

The entire 1620 Workwear funnel is built around a sale promise that never delivers at the product level. Every channel entry point — the announcement bar ("UP TO 50% OFF SELECT STYLES FOR OUR RETIREMENT SALE"), the homepage hero, and Google search ads ("Labor Day Sale — 20% Off") — signals discounts. But the homepage product grid and collection page show full prices across the vast majority of cards. The six CLOSEOUT - FINAL SALE items in the collection have no visual differentiation — their sale status is communicated only via a title suffix, not a badge, ribbon, or strikethrough price. The one exception — a single product in fold 3 showing a compare-at price — proves the theme. The brand is sitting on sale credibility it isn't converting.

Cross-channel messaging compounds this. Google runs "Labor Day Sale — 20% Off." The homepage runs "Retirement Sale — Up to 50% Off." Meta runs no sale copy. Ad 1 (active paid campaign) sends "Shop Now" traffic to a preorder variant with three expired production dates — March 2026: SOLD OUT / Mid April 2026: 25% RESERVED / June 2026: IN PRODUCTION — none of which have been updated as of July 25, 2026. Ad 3 uses a UGC loyalty angle ("1620 is my go-to from here on out") and lands on a CLOSEOUT - FINAL SALE product with multiple sizes crossed out. Each touchpoint tells a different story. For a brand whose conversion case rests on premium quality and loyalty signals, this inconsistency creates friction at exactly the moment customers are deciding whether to trust the price.

The PDP is the most technically broken page in the funnel. Mobile Lighthouse scores it at 41/100 — LCP 42.9s (threshold 2.5s), TBT 710ms (threshold 200ms), TTI 43.4s, page size 8MB. This is the primary paid traffic destination for all three Meta ads and a likely top-traffic organic page. Ad spend is feeding a page that most mobile users on average connections cannot interact with before bouncing. Once users who stay reach the buy box: no sticky ATC, trust badges below the fold on the preorder variant, a bundle offer buried mid-page, and an email capture popup competing for attention in the lower left. The cart adds no AOV mechanics — the "BUY 3 & GET 1 FREE" offer visible on the PDP disappears entirely in the cart drawer.

---

## Top Test Opportunities

### 1. Sale Price Visibility on Product Cards
**What's broken:** On the homepage, directly below the full-width "RETIREMENT SALE / UP TO 50% OFF" hero, a four-column product grid displays: Field Tech Short Sleeve Shirt $135, Foundation Utility Pant $135, NYCO Work T-Shirt $36, Double Knee Utility Pant 2.0 $228. All prices are in standard black text with no compare-at or strikethrough. On the collection page (3-column grid), six products are labeled "- CLOSEOUT - FINAL SALE" via title text only — no badge, no ribbon, no crossed-out original price. The single exception in fold 3 (Full Tech Sweatpant) shows a strikethrough price and is the only product on the page where sale savings are visible. A customer scanning for retirement sale deals has no visual path to identifying discounted items.
**Evidence:** site-visual-summary.md (homepage fold 2-3, collection fold 2-3), google-ads-visual-summary.md (sale headline), meta-ads-visual-summary.md (no sale messaging in ads — baseline contrast)
**Key data:** 6 of ~12 visible collection page products are CLOSEOUT; only 1 shows compare-at pricing. Google ads cite "up to 20% off"; homepage cites "up to 50% off" — both promises go unverified at the product card level.
**Est. lift:** 8% CR lift x unknown sessions x $228 AOV = high priority regardless of session volume

### 2. Stale Preorder Block on Ad 1 LP (Size 38 Variant)
**What's broken:** Ad 1 is an active Meta campaign (started May 12, 2026) targeting the Double Knee Utility Pant 2.0 in Size 38/Meteorite. The buy box for this variant shows a red preorder scheduling block with three stacked rows: "March 2026: SOLD OUT / Mid April 2026: 25% RESERVED / June 2026: IN PRODUCTION." The CTA button reads "PREORDER" in dark red. There is no current estimated ship date, no restock notification option, and no indication of whether the June production batch has shipped. As of July 25, 2026, all three dates are in the past. Trust badges (Made in USA, Guaranteed for Life, Free Exchanges) appear below the preorder block in fold 2. An email capture popup ("GET 10% OFF!") overlaps content in the lower left.
**Evidence:** meta-ads-visual-summary.md (Ad 1, LP fold 1), context.md (stale date note)
**Key data:** Active paid campaign sending traffic to a page with three expired production milestones. Trust badges not visible in fold 1 for this variant.
**Est. lift:** Any improvement is incremental revenue from existing ad spend; removing a trust-breaking element from an active paid destination.

### 3. PDP Performance — LCP and TBT Reduction
**What's broken:** The Double Knee Utility Pant 2.0 PDP (primary destination for all three Meta ads) scores 41/100 on mobile Lighthouse (July 25, 2026). LCP: 42.9s. TBT: 710ms. TTI: 43.4s. Page size: 7,986 KiB. 20 long tasks. One layout shift (CLS 0.081). The page is 17x over the LCP threshold and 3.5x over the TBT threshold. The buy box, product images, and ATC button are all below the LCP threshold — meaning a meaningful share of mobile users on average connections see a blank or partial page before the primary CTA loads. The homepage is also slow (LCP 11.7s, performance 62/100, page size 5,012 KiB) but is secondary to the PDP in paid traffic priority.
**Evidence:** pagespeed.md (PDP row, July 25 2026 Lighthouse data)
**Key data:** PDP 41/100, LCP 42.9s, TBT 710ms, TTI 43.4s, 8MB page, 20 long tasks. Homepage 62/100, LCP 11.7s, 5MB page.
**Est. lift:** Industry benchmarks suggest 100ms load improvement correlates with 1-7% CR lift; at current severity (43s TTI), meaningful remediation could yield 10-20%+ lift on mobile traffic.

### 4. Cart — Bundle Reinforcement and AOV Mechanic
**What's broken:** The mobile cart drawer contains a single product (Double Knee Utility Pant 2.0, Color: Meteorite, Size: 38, Inseam Hemmed to Order: 32, $228). The only elements present are: a "GUARANTEED FOR LIFE" strip at the top of the drawer, the item details, a full-width red "Checkout • $228" button, and Shop Pay / PayPal buttons below it. There are no upsell suggestions, no cross-sell recommendations, no bundle reinforcement, no free-shipping threshold prompt, and no "You might also like" or "Complete the look" section. The "BUY 3 & GET 1 FREE" bundle offer visible on the PDP (fold 1, below the ATC on the in-stock variant) does not appear anywhere in the cart drawer. The catalog includes pants, shirts, hoodies, tees, shorts, and outerwear — multiple natural add-on opportunities at lower price points ($36 tee, $78 hoodie) that go unused at the highest-intent moment in the funnel.
**Evidence:** site-visual-summary.md (cart section), meta-ads-visual-summary.md (Ad 2 LP fold 1 — bundle offer on PDP)
**Key data:** Zero AOV mechanics in cart. Bundle offer exists on PDP but is absent at cart. Catalog depth supports multiple add-on categories.
**Est. lift:** Cart upsell/bundle reinforcement benchmarks 5-15% AOV lift; at $228 base, even 5% is ~$11/order.

### 5. Ad 3 Message Match — Align Ad to LP or Redirect to Full-Price Product
**What's broken:** Ad 3 is an active Meta campaign (started July 10, 2026) using a UGC testimonial: "Tougher than a tire swing... Best pants I own. I have about 6 pairs of Duluth pants with blown-out knees after 6 months. 1620 is my go-to from here on out." Image: muddy work pants, real job site. Headline: "American Made Workwear." The ad communicates loyalty, durability, and "go-to" brand status. The LP is the Single Knee Utility Pant 2.0 — CLOSEOUT - FINAL SALE at $132. The second phrase in the product title is "CLOSEOUT - FINAL SALE." Multiple sizes are crossed out and unavailable (34, 38, 44 shown with strikethrough X). No trust badges are visible in fold 1. The message — "I own 6 pairs of this brand" — clashes with a clearance destination signaling product discontinuation and limited availability.
**Evidence:** meta-ads-visual-summary.md (Ad 3, all folds)
**Key data:** LP product title leads with "CLOSEOUT - FINAL SALE." 3+ sizes unavailable. Trust badges absent in fold 1. UGC reviewer (Joseph) is the first review on the LP — one authentic continuity signal in an otherwise misaligned experience.
**Est. lift:** Message match alignment benchmarks 10-20% LP CR improvement.

### 6. Collection Page — Visual Sale Badge on Closeout Items
**What's broken:** The collection page (3-column grid) mixes 6 CLOSEOUT - FINAL SALE items with 6+ full-price items in the same visual grid. Product cards are identical in layout — square product image, product name, price, star rating. The only way to identify a closeout item is to read the full product title, which includes the suffix "- CLOSEOUT - FINAL SALE" in the same font and color as the product name. There is no badge, sticker, ribbon, or highlighted price treatment on closeout cards. The Full Tech Sweatpant in fold 3 is the single exception — it shows a crossed-out original price. A shopper scanning the grid for retirement sale deals cannot identify discounted products without reading every product title in full.
**Evidence:** site-visual-summary.md (collection fold 2-3)
**Key data:** 6 closeout items in grid, 1 showing compare-at price. No visual badge system present.
**Est. lift:** Visual sale signaling on collection pages benchmarks 5-15% improvement in PDP click-through.

### 7. Cross-Channel Offer Alignment — Google Ads to Match Site Sale
**What's broken:** Google search ads run the headline "Rated Best Overall Work Pants — Labor Day Sale — 20% Off." The 1620usa.com announcement bar and homepage hero run "RETIREMENT SALE / UP TO 50% OFF SELECT STYLES." Two different sale names ("Labor Day Sale" vs. "Retirement Sale"), two different discount levels ("20% Off" vs. "Up to 50% Off"), across the same funnel. A customer who clicks a Google search ad expecting a specific 20% Labor Day discount lands on a page promoting a higher-discount Retirement Sale under a different name. Additionally, the Full Tech Work Hoodie (Hi Vis) Shopping ad shows "[Price]" as the product price — a rendering error in the Google Shopping feed that removes the price field from the product tile, which typically reduces CTR on Shopping placements.
**Evidence:** google-ads-visual-summary.md, site-visual-summary.md (homepage fold 1)
**Key data:** "Labor Day Sale 20% Off" in Google search ad vs. "Retirement Sale Up to 50% Off" on site. "[Price]" placeholder on hoodie Shopping ad.
**Est. lift:** Operational fix (not a split test); correcting the Google feed and unifying sale naming removes a trust gap at the top of the paid funnel.

### 8. Trust Signal Placement — Fold 1 on All PDP Variants
**What's broken:** On the in-stock Ad 2 LP (Size 40/Meteorite, "ADD TO CART"), three trust badges appear in fold 1 directly below the ATC button: "Proudly Made in the U.S.A.," "Guaranteed for Life," "Free Exchanges." On the preorder Ad 1 LP (Size 38/Meteorite, "PREORDER"), the same trust badges appear in fold 2 — below the preorder scheduling block, below the product description text. On the Ad 3 LP (closeout), no trust badges are visible in fold 1 at all. The pattern is consistent: the more hesitation-inducing the purchase context (preorder, clearance), the further the trust signals are from the CTA. Moving the trust badge row to a fixed position immediately below the CTA button on all PDP variants would deliver consistent reassurance at the decision point.
**Evidence:** meta-ads-visual-summary.md (Ad 1 LP fold 1 vs. Ad 2 LP fold 1 vs. Ad 3 LP fold 1)
**Key data:** Trust badges in fold 1 on in-stock variant; fold 2 on preorder variant; absent in fold 1 on closeout variant. Lifetime guarantee visible only in fold 2+ on all three ad LPs.
**Est. lift:** Trust signal proximity to CTA benchmarks 3-8% CR lift on hesitation-prone decisions (preorder, clearance, premium price).

---

## Unused Findings

- Google Shopping broken price ("[Price]" placeholder on Full Tech Work Hoodie) suppresses CTR on that Shopping placement — operational fix to submit to client immediately, not a test.
- Email capture popup ("GET 10% OFF!") appears on both tested ad LPs and overlaps buy box content; the 10% offer may compete with in-session conversion — worth monitoring alongside CR data.
- "Pant Comparison Guide" banner on homepage fold 3 suggests lineup complexity is a known purchase barrier — a comparison or quiz tool on the collection page is a medium-term opportunity for returning visitors navigating 9 pant SKUs.
- Sticky ATC bar absent on all observed PDPs — adding a persistent CTA bar (product name + price + ATC button) that appears on scroll past the buy box is a high-signal default improvement for content-heavy PDPs with reviews below fold 2.
