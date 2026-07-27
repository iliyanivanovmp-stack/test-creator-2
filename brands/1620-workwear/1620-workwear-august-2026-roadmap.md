# 1620 Workwear CRO Research Brief

**Data Sources:** Meta Ads visual summary, Meta Ads landing page URLs, Google Ads visual summary, PageSpeed/Core Web Vitals (Lighthouse mobile, July 25 2026), Site visual summary (homepage, collection, cart), Non-data context, Live site fetch (July 25 2026)

---

## Insights

The entire 1620 Workwear funnel is built around a sale promise that never materializes at the product level. The announcement bar, hero image, and Google search ads all lead with discounts ("UP TO 50% OFF SELECT STYLES" and "Labor Day Sale 20% Off"), but the product grid directly below the hero shows full prices across the majority of cards. Six of approximately twelve visible collection products are CLOSEOUT - FINAL SALE, yet five of those six carry no visual price differentiation: no badge, no ribbon, no strikethrough price. One product (Full Tech Sweatpant) is the lone exception. A shopper who arrived expecting discounts scans a full-price grid with no clear path to the savings they were promised (Source: Site visual summary).

Channel inconsistency compounds the problem. Google search ads run "Labor Day Sale 20% Off." The homepage and announcement bar promote "Retirement Sale Up to 50% Off." Meta ads show no sale copy. These are three different signals from the same brand, reachable within a single purchase session. Ad 1 (active paid campaign, started May 12, 2026) sends "Shop Now" traffic to the Double Knee Utility Pant 2.0, Size 38, which shows a preorder scheduling block with three production milestones: "March 2026: SOLD OUT / Mid April 2026: 25% RESERVED / June 2026: IN PRODUCTION." As of July 25, 2026, all three dates have passed with no update to the page (Source: Meta Ads visual summary, Non-data context). Ad 3 (started July 10, 2026) uses a UGC loyalty testimonial and sends that traffic to a CLOSEOUT - FINAL SALE product with multiple sizes crossed out (Source: Meta Ads visual summary).

The primary paid traffic destination, the Double Knee Utility Pant 2.0 PDP, scores 41/100 on mobile Lighthouse (July 25, 2026). LCP is 42.9s against a 2.5s threshold. TTI is 43.4s. Page size is 7,986 KiB across 20 long tasks. A meaningful share of mobile users on typical connections bounce before reaching an interactive buy box. For those who stay: trust badges appear in fold 2 on the preorder variant, compared to fold 1 on the in-stock variant; the bundle offer disappears from the cart; no sticky ATC bar is present on any observed PDP. The homepage scores 62/100 with an 11.7s LCP. It is also failing, but secondary in priority to the PDP given paid traffic routing (Source: PageSpeed/Core Web Vitals, Meta Ads visual summary).

Where the experience does work, it works well. The Double Knee Utility Pant 2.0 carries 4.5 stars across 419 reviews, with 75% five-star ratings and recent praise for durability and pocket design in trade use (Source: PDP reviews via Meta Ad LP screenshots). The in-stock Ad 2 LP shows what the funnel can be: trust badges in fold 1, bundle offer visible, ATC available. The UGC creative for Ad 3 is legitimately strong ("6 pairs of Duluth with blown-out knees after 6 months... 1620 is my go-to from here on out"): a real job site, a named reviewer, a direct competitor takedown. The brand has conviction behind its product. The CRO problem is structural: the funnel is not showing shoppers what they need to see, in the right order, to act on that conviction.

Session volume data was not available for this audit. Revenue potential calculations below are expressed per 1,000 monthly paid sessions. Exact figures should be updated once traffic data is confirmed. Flagship AOV is $228; catalog items start at $36 (Source: Site visual summary, roadmap seed).

---

## Slot 1: Fix Stale Preorder Block on Ad 1 LP

**Type:** Immediate Fix
**Page:** Double Knee Utility Pant 2.0 PDP, Size 38/Meteorite variant (https://www.1620usa.com/products/stretch-nyco-double-knee-utility-pant)

Ad 1 is an active paid Meta campaign that has been driving traffic since May 12, 2026. The Size 38/Meteorite buy box shows a red preorder scheduling block with three expired production milestones: "March 2026: SOLD OUT / Mid April 2026: 25% RESERVED / June 2026: IN PRODUCTION." The CTA reads "PREORDER." As of July 25, 2026, all three dates are in the past. The page gives no indication whether the June batch has shipped, is delayed, or has been cancelled. A first-time visitor reading this block has no basis to trust the brand will fulfill the order.

**Fix:** Remove the stale preorder scheduling block from the Size 38/Meteorite variant. If the size is available: update to "ADD TO CART." If it remains unavailable: replace the preorder block with a "Notify me when back in stock" email capture in the buy box, and remove the "PREORDER" CTA. Update the page before the next ad spend cycle.

---

## Slot 2: Fix PDP Mobile Performance

**Type:** Immediate Fix
**Page:** Double Knee Utility Pant 2.0 PDP (https://www.1620usa.com/products/stretch-nyco-double-knee-utility-pant)

The PDP scores 41/100 on mobile Lighthouse (July 25, 2026): LCP 42.9s (threshold 2.5s), TBT 710ms (threshold 200ms), TTI 43.4s, page size 7,986 KiB, 20 long tasks. This is the primary destination for all three active Meta ad campaigns. At 43s TTI, most mobile users on average connections cannot interact with the buy box before the page qualifies as abandoned. The homepage (62/100, LCP 11.7s) is also failing but is secondary in paid traffic priority.

**Fix:** Audit and defer or remove third-party scripts loading synchronously (email capture popup, ad pixels, analytics). Compress and lazy-load product images below fold 1. Reduce JavaScript bundle size. Target: LCP below 4s, TBT below 200ms on mobile. Retest with Lighthouse post-remediation.

---

## Slot 3: Fix Google Ads Sale Name and Shopping Feed Price

**Type:** Immediate Fix
**Channel:** Google Ads (search + Shopping)

Google search ads run "Labor Day Sale 20% Off." The site homepage and announcement bar promote "Retirement Sale Up to 50% Off." These are different sale names with different discount depths running simultaneously from the same brand. A customer who clicks through Google expecting a 20% Labor Day discount lands on a page announcing a 50% Retirement Sale, under a different sale name with a different discount depth. Separately, the Full Tech Work Hoodie (Hi Vis) Shopping ad renders the price as "[Price]", a broken template variable displaying in the product tile instead of the actual price (Source: Google Ads visual summary, Site visual summary).

**Fix:** Update Google search ad headlines to reflect the current active sale name ("Retirement Sale") and the correct discount depth ("Up to 50% Off"). Fix the broken price feed variable on the Full Tech Work Hoodie Shopping listing so the actual price renders in the product tile.

---

## Slot 4: Sale Badge and Strikethrough Price on Product Cards

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage product grid + Collection page (https://www.1620usa.com/ and https://www.1620usa.com/collections/)
**Revenue potential:** Sessions unknown. At a conservative 5% CR lift across paid traffic landing on sale-promise pages, at $228 AOV: 5% x 1,000 sessions x $228 = $11,400 per 1,000 monthly sessions.

**Hypothesis:** If we add a high-contrast sale badge and compare-at strikethrough price to every discounted product card, sale-intent shoppers will click through to PDPs at a higher rate because they can identify deals without reading every product title.

**Data:** The announcement bar, homepage hero, and Google search ads all promise "Retirement Sale Up to 50% Off," but the product grid below the hero shows all items at full price in standard black text. On the collection page, six products are CLOSEOUT - FINAL SALE but show no visual differentiation from full-price cards; the only signal is the title suffix "- CLOSEOUT - FINAL SALE" in the same font and color as the product name. One product (Full Tech Sweatpant, fold 3) shows a compare-at strikethrough. This is the lone exception on both pages. A shopper scanning for retirement sale deals has no visual path to discounted items (Source: Site visual summary).

**V1:** Add a "CLOSEOUT" or "SALE" badge to the top-left corner of the card image on every discounted product (homepage grid and collection grid). Display the original price as strikethrough text alongside the current sale price below the product name. Both homepage and collection page receive the same treatment simultaneously. On mobile: badge remains visible on the compressed card at single-column layout. On desktop: badge and strikethrough render on all grid sizes.

---

## Slot 5: Trust Signal Row on All PDP Variants

**Type:** A/B test (1 variation vs. control)
**Page:** Double Knee Utility Pant 2.0 PDP, all variants (https://www.1620usa.com/products/stretch-nyco-double-knee-utility-pant)
**Revenue potential:** Sessions unknown. At a conservative 4% CR lift on preorder and closeout variants, at $228 AOV: 4% x 1,000 sessions x $228 = $9,120 per 1,000 monthly sessions.

**Hypothesis:** If we move the trust badge row to a fixed position immediately below the CTA button on all PDP variants, hesitation-prone shoppers (preorder, closeout) will convert at a higher rate because the brand's strongest reassurance signals ("Guaranteed for Life," "Made in USA") are visible at the decision point rather than below it.

**Data:** On the Ad 2 LP (Size 40, in-stock, "ADD TO CART"), three trust badges appear in fold 1 directly below the ATC button: "Proudly Made in the U.S.A.," "Guaranteed for Life," "Free Exchanges." On the Ad 1 LP (Size 38, preorder, "PREORDER"), the same trust badges appear in fold 2, below the preorder scheduling block and product description. On the Ad 3 LP (closeout), no trust badges are visible in fold 1 at all. The customer most in need of reassurance sees the trust signals last (Source: Meta Ads visual summary, Ad 1 LP fold 1 vs. Ad 2 LP fold 1 vs. Ad 3 LP fold 1).

**V1:** Pin the three trust badges ("Proudly Made in the U.S.A.," "Guaranteed for Life," "Free Exchanges") as a static row immediately below the primary CTA button on all PDP variants, regardless of stock status (in-stock, preorder, closeout). The trust row position should not shift when the buy box content changes between variants. On mobile: trust badges display as icons with short labels in a single row below the CTA, visible without scrolling. On desktop: same fixed position below the buy box CTA in a horizontal row.

---

## Slot 6: Cart Bundle Reinforcement

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (https://www.1620usa.com/)
**Revenue potential:** Sessions unknown. At a conservative 5% AOV lift on cart conversions, at $228 base AOV: 5% x $228 = $11.40 additional revenue per converting order.

**Hypothesis:** If we surface the "BUY 3 & GET 1 FREE" bundle offer and complementary product suggestions in the cart drawer, AOV will increase because buyers are reminded of the bundle deal at the highest-intent moment in the funnel.

**Data:** The cart drawer currently shows one product (Double Knee Utility Pant 2.0, $228), a "GUARANTEED FOR LIFE" strip, a full-width red "Checkout $228" button, and Shop Pay/PayPal buttons. No upsell, cross-sell, bundle reinforcement, or free-shipping threshold prompt is present. The "BUY 3 & GET 1 FREE" bundle offer visible on the Ad 2 LP PDP (fold 1, below the ATC button) disappears entirely when the user enters the cart. The catalog includes tees from $36, hoodies, shorts, and outerwear. Multiple natural add-on categories go unused at the highest-intent point in the funnel (Source: Site visual summary, Meta Ads visual summary).

**V1:** Add a "Complete the Bundle" section below the checkout button in the cart drawer. This section displays the "BUY 3 & GET 1 FREE" offer headline with a brief explanation ("Add 2 more items, get 1 free"), followed by two to three complementary product suggestions (e.g., NYCO Work T-Shirt $36, Field Tech Short Sleeve $135) with quick-add buttons. On mobile: section appears below the checkout and payment buttons, scrollable within the drawer. On desktop: section appears within the same cart drawer layout below payment options.

---

## Slot 7: Ad 3 LP Redirect to In-Stock Flagship

**Type:** A/B test (1 variation vs. control)
**Page:** Ad 3 Meta campaign landing page (current: Single Knee Utility Pant 2.0 CLOSEOUT, test destination: Double Knee Utility Pant 2.0 in-stock)
**Revenue potential:** Sessions unknown. At a conservative 10% LP CR lift from message match alignment, at $228 AOV: 10% x 1,000 sessions x $228 = $22,800 per 1,000 Ad 3 monthly sessions.

**Hypothesis:** If we repoint Ad 3 to the Double Knee Utility Pant 2.0 in-stock PDP, conversion rate will increase because the LP delivers on the loyalty and durability story the ad sets up, rather than a clearance product with limited size availability.

**Data:** Ad 3 (started July 10, 2026) features UGC testimonial copy: "Tougher than a tire swing... Best pants I own... 6 pairs of Duluth with blown-out knees after 6 months. 1620 is my go-to from here on out." Headline: "American Made Workwear." Image: muddy work pants on a real job site. The LP is the Single Knee Utility Pant 2.0, CLOSEOUT - FINAL SALE at $132, where the second phrase of the product title is "CLOSEOUT - FINAL SALE" and multiple sizes are crossed out (34, 38, 44). The ad communicates brand loyalty and "go-to" status; the LP communicates product discontinuation and limited availability. These are opposite messages (Source: Meta Ads visual summary).

**V1:** Repoint the Ad 3 click URL to the Double Knee Utility Pant 2.0 PDP (the flagship product, $228, in-stock for the available size range). No changes to the ad creative or copy. The destination LP is the same page tested in Ad 2, which showed trust badges in fold 1, the bundle offer below the ATC, and an in-stock CTA. On mobile and desktop: the LP experience is the standard PDP. No landing page customization is required for this test.

---

## Slot 8: Sticky ATC Bar on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Double Knee Utility Pant 2.0 PDP (https://www.1620usa.com/products/stretch-nyco-double-knee-utility-pant)
**Revenue potential:** Sessions unknown. At a conservative 3% CR lift, at $228 AOV: 3% x 1,000 sessions x $228 = $6,840 per 1,000 monthly sessions.

**Hypothesis:** If we add a sticky ATC bar that persists as users scroll past the buy box, conversion rate will increase because shoppers who become convinced while reading features or reviews can act immediately without scrolling back.

**Data:** No sticky header or ATC bar is visible on any of the three observed PDP variants (Ad 1, Ad 2, Ad 3 landing pages). The buy box and CTA are in fold 1; the PDP contains product description, features, bundle offer, and a reviews section spanning fold 2 and beyond. A user who becomes convinced during feature or review reading must scroll back to fold 1 to access the ATC button. The PDP is content-heavy by design: the lifetime guarantee, pocket descriptions, and material specs all require scrolling. No persistent CTA is available during that scroll (Source: Meta Ads visual summary, LP fold 1-3 for all three ads).

**V1:** Add a sticky bar fixed to the bottom of the screen on mobile that appears when the user scrolls past the buy box. The bar contains: product name, selected variant (size + color), current price, and a red ATC button matching the existing CTA style. On desktop: implement as a sticky sidebar or top bar that appears on downward scroll past the buy box, with the same product name, variant, price, and ATC. The bar dismisses if the user scrolls back up to the buy box. No change to the existing buy box layout.

---

## Future Slot Candidates

1. **Homepage Sale Funnel CTA** - The homepage hero ("RETIREMENT SALE / UP TO 50% OFF") has no direct "SHOP THE SALE" CTA linking to a filtered sale or retirement collection. Shoppers with sale intent who land on the homepage have no guided path to discounted items.

2. **Comparison Tool or Quiz on Collection Page** - The "Pant Comparison Guide" banner on homepage fold 3 signals the brand knows lineup complexity is a barrier. With 9 pant SKUs at similar price points, a comparison tool or recommendation quiz could reduce decision paralysis for first-time buyers (Source: Site visual summary).

3. **Email Capture Popup Timing Audit** - The "GET 10% OFF!" popup appears on active ad LPs and overlaps buy box content. A 10% discount prompt before the visitor has decided to buy may suppress session CR even if it grows the list. Test delayed trigger (60+ seconds or exit intent) vs. current on-load behavior.

4. **Sticky ATC and PDP Trust Signal Test on Homepage as Well** - Once the PDP fixes are validated, the same trust signal and ATC patterns may apply to any PDP that receives organic traffic at meaningful volume.
