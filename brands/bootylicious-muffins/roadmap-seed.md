# Bootylicious Muffins Roadmap Seed

**Store:** https://bootyliciousmuffins.com/
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads Library screenshots, Google Ads Transparency Center screenshots, on-site reviews, PageSpeed/Core Web Vitals (mobile, homepage + PDP), site screenshots (homepage, build-your-box, PDP, cart), live homepage/PDP WebFetch verification (2026-09-21), competitor research (Kodiak Cakes, Premier Protein), last30days-ecom social/community research (TikTok, Instagram, YouTube, Pinterest, Amazon, web)

## Key Insights

Subscribe & Save is structurally the default on every purchase surface that has one — build-a-box (fold 1: "$48.00 → $40.80," radio-marked) and the single-flavor PDP (dark-card emphasis, "$79.00 → $67.15" vs. a plain-bordered one-time option) — but the cart drawer has no equivalent AOV mechanic and instead leads with a cross-sell item marked "OUT OF STOCK." Live WebFetch on 2026-09-21 confirmed the subscription-first structure is still current on the build-a-box page.

Message match between paid ads and the shared homepage landing page is inconsistent by ad, not by channel: Ads 1-2 ("25g of Protein / 180-200 Calories / Zero Guilt," running since Aug 5, 2025) match the homepage headline and subhead closely, but Ad 3's "cheat day" framing and "RESTOCKED AFTER SELLING OUT" badge (running since Apr 14, 2026) appear nowhere in the three homepage folds collected. Google Ads add fiber ("14-18g dietary fiber," "Stay Full Longer") and payment/shipping claims absent from both Meta and the homepage.

Flavor inconsistency is corroborated by two independent sources: on-site reviews name carrot cake, lemon poppy seed, and blueberry as underperforming flavors, and Amazon's Variety Pack SKU sits at 3.7/5 (1,120 ratings) versus 4.2/5 for single-flavor SKUs — suggesting the sampling/discovery experience, not the product, drives dissatisfaction. Mobile performance is a hard constraint on every page: homepage and PDP both score 54/100 with LCP at 7.3s and 6.8s (roughly 3x Google's "Good" threshold), driven by ~800KB of unused JavaScript and up to 17.9s of main-thread work rather than server latency (10ms response time on both pages).

## Top Test Opportunities

### 1. Cart Upsell Replacement
**What's broken:** The cart is a dark-themed slide-out drawer (not a full page). Below the line item (e.g., "Double Chocolate Protein Muffins, 12-Pack, $46" with a Subscribe & Save toggle and quantity stepper), an "UPGRADE YOUR CART" horizontal carousel with arrow controls shows add-on products. The first visible item, a "1/8 Measuring Cup" priced at $5, carries a red/visible "OUT OF STOCK" label. A second, partially visible item ("Bake Better Buns," a recipe guide) sits next to it. Below the carousel, a red "Checkout+" CTA button spans the full width, with a smaller "No thanks, continue" text link beneath it.
**Evidence:** site screenshots (cart-drawer.png), site-visual-summary.md.
**Key data:** The dead-stock item occupies the first, most visible slot in the only AOV mechanic in the cart.
**Est. lift:** Not calculable without sessions/mo and AOV (see Missing Data in audit); qualitatively, replacing a dead-stock first slot with a live, relevant add-on is a low-effort, high-certainty fix.

### 2. Checkout+ Default-State Disclosure
**What's broken:** In the cart drawer, between the "Add discount code" expandable field and the Subtotal/Checkout button, a "Checkout+" line item reads "Loss, theft & damage" protection priced at $1.95. The captured screenshot does not show a checkbox or toggle control next to this line, so it's unknown whether the charge is bundled into the total by default or requires active opt-in.
**Evidence:** site-visual-summary.md (cart), manifest open questions (flagged at collection time).
**Key data:** This ambiguity was flagged as unresolved by both the collection step and this audit; a live add-to-cart test is required before building a test around it.
**Est. lift:** Not calculable until default state is confirmed live — recommend this as a verification step, then a test only if the charge is pre-selected.

### 3. PDP Accordion Default State
**What's broken:** On the PDP, directly below the full-width "Add to Cart" button, four collapsible sections stack vertically: "PRODUCT DESCRIPTION," "HOW TO MAKE IT," "NUTRITION HIGHLIGHTS," "NUTRITIONAL INFO." All four are collapsed by default with no visible teaser text or icon indicating content inside — a shopper sees only the section titles and must tap each one individually to see any content, including nutrition facts central to the brand's own ad claims (25g protein, 7g net carbs).
**Evidence:** site-visual-summary.md (PDP fold 2).
**Key data:** Ad copy across Meta and Google leads with these exact nutrition numbers, making their absence from the default PDP view a message-match gap between ad and page, not just a UX issue.
**Est. lift:** Not calculable without traffic data; directionally, surfacing key nutrition facts inline (expanded by default, or a summary line above the accordions) reduces the click-to-inform gap for ad-driven traffic already primed on those numbers.

### 4. Homepage/PDP Dual-Path Purchase Flow
**What's broken:** On the homepage, fold 2 ("OUR BEST SELLERS") is a horizontal carousel of four cards on colored circular backgrounds: "Build Your Box" ($48, "Choose Flavors" button) sits alongside three single-flavor cards (Double Chocolate, Birthday Cake, Cinnamon Bun, each $46 with a direct "Add to Cart" button). A shopper can add a single flavor straight to cart without ever entering the flavor-picker the hero CTA ("Build Your Box," the only CTA in fold 1) is designed to drive them toward. The PDP then reverses this: its buy box includes a "Want to Mix & Match Muffins?" prompt with a "Build Your Box" button positioned directly below the case-size selector, cross-selling shoppers back into the box-builder from a single-flavor page.
**Evidence:** site-visual-summary.md (homepage fold 2, PDP fold 1).
**Key data:** Two competing purchase paths exist on both the homepage and the PDP simultaneously, with no visible hierarchy indicating which the brand wants a shopper to take.
**Est. lift:** Not calculable without traffic data; directionally, resolving which path is primary (single-flavor speed vs. box-builder AOV) and demoting the other could reduce path-switching friction and abandonment.

### 5. Ad 3 Message-Match Gap
**What's broken:** Meta Ad 3 (Library ID 974220355004409, active since Apr 14, 2026) uses the headline "What if Cheat Day Was Every Day? 😋😋" over a video showing a muffin cup with an on-video badge reading "RESTOCKED AFTER SELLING OUT." All Meta ads route to the shared homepage. None of the three collected homepage folds contain "cheat day" language, a restock badge, or any acknowledgment of prior stock-outs — a shopper who clicks specifically because of the restock urgency or cheat-day framing lands on a page that doesn't continue either hook.
**Evidence:** meta-ads-visual-summary.md (Ad 3), homepage folds 1-3 (site-visual-summary.md).
**Key data:** Ads 1-2 (same start date range, different copy) do match the homepage closely by contrast — this is an ad-specific gap, not a channel-wide one.
**Est. lift:** Message-match improvements on ad-driven landing content commonly report meaningful bounce-rate reductions for the affected segment; brand-specific lift requires the client's own ad-level traffic and conversion data.

### 6. Case-Size-Before-Flavor Sequencing
**What's broken:** On the build-a-box page, "STEP 1 - Select Case Size" appears before "STEP 2 - Select Flavors." Step 1 shows three case-size cards (12-Pack $40.80/$3.40 per cup at 15% off; 24-Pack $67.15/$2.80 per cup at 29% off; 36-Pack $90.95/$2.53 per cup at 36% off, labeled "Best Value"). Only after selecting a case size does the shopper reach the flavor grid in Step 2, where each flavor tile has a quantity stepper starting at 0. A progress bar and "Add 12 more items to continue" button track progress toward the chosen case's item count, meaning the spend commitment happens before the shopper knows whether their preferred flavors are available or how many they actually want.
**Evidence:** site-visual-summary.md (collection/build-a-box fold 1), live WebFetch confirmation of Step 1/Step 2 structure (2026-09-21).
**Key data:** On-site reviews (Shane S. J.) describe first-order dissatisfaction from picking flavors before understanding preferences — consistent with a flow that asks for commitment before flavor discovery.
**Est. lift:** Not calculable without funnel/abandonment data; directionally, flavor-first sequencing (or a smaller trial case size before the case-size commitment) targets a friction point independently described in reviews.

### 7. Mobile Page Speed / LCP
**What's broken:** Both the homepage and PDP (build-your-box) load slowly on mobile: homepage LCP is 7.3s (Lighthouse score 0.05) and PDP LCP is 6.8s (score 0.07), both roughly 3x Google's 2.5s "Good" threshold. Time to Interactive is 33.5s (homepage) and 25.3s (PDP). Server response time is fast (10ms root document) on both, meaning the delay is client-side: ~794-816 KiB of unused JavaScript per page and 2.9-3.9s of JS bootup time, with main-thread work reaching 17.9s on the PDP. Cumulative Layout Shift is not an issue (0 and 0.048, both near-perfect).
**Evidence:** raw/pagespeed.md, homepage and PDP Lighthouse JSON reports (collected 2026-09-20, mobile only — desktop not collected).
**Key data:** Performance score 54/100 on both pages; unused JS ~800KB per page is the largest identifiable single lever.
**Est. lift:** Not calculable without conversion/session data tied to load time; directionally, LCP reductions in this range are commonly associated with meaningful mobile conversion recovery industry-wide.

### 8. Missing Trust Signals Near the Buy Box
**What's broken:** Across all three purchase surfaces — homepage hero (fold 1, CTA "Build Your Box" below the subhead), PDP buy box (fold 1, next to the Subscribe & Save/One-time selector), and the cart drawer — no guarantee badge, shipping-time promise, or returns/refund copy appears near the CTA or line items. The live homepage fetch (2026-09-21) confirms "Returns & Refunds," "Shipping Policy," and "Cancellation Policy" links exist on the site, but none surface near the point of purchase in the folds and pages captured.
**Evidence:** site-visual-summary.md (homepage fold 1, PDP fold 1, cart drawer), live homepage WebFetch (2026-09-21).
**Key data:** Only trust signal near any CTA is the 4.7★/4,900-4,957-review line; no guarantee or shipping-time copy appears alongside it anywhere in the funnel.
**Est. lift:** Not calculable without baseline conversion data; adding a concise guarantee/shipping line under the primary CTA is a low-effort test with a well-documented industry pattern.

## Unused Findings

- Variety Pack flavor-discovery guidance: Amazon's Variety Pack rating (3.7/5, 1,120 ratings) trails single-flavor SKUs (4.2/5), corroborated by on-site reviews describing trial-and-error before finding favorite flavors — a flavor-recommendation or "start here" prompt in the picker could reduce first-order mismatch, though it leans product/UX as much as CRO.
- Prep-texture expectation-setting: cross-platform creator commentary (TikTok, Instagram) repeatedly describes the pre-microwave texture as wet/"gooey" ("It looks raw 😭"), with no matching expectation-setting copy found in the collected PDP folds — directional only, not corroborated by first-party site reviews.
