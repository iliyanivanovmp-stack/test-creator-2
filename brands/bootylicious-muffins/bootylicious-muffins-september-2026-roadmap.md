# Bootylicious Muffins CRO Research Brief

**Data Sources:** Meta Ads Library screenshots, Google Ads Transparency Center screenshots, on-site reviews, PageSpeed/Core Web Vitals (mobile, homepage + PDP), site screenshots (homepage, build-your-box, PDP, cart), live homepage/PDP WebFetch verification (2026-09-21), competitor research (Kodiak Cakes, Premier Protein), last30days-ecom social/community research (TikTok, Instagram, YouTube, Pinterest, Amazon, web)

## Insights

Subscribe & Save is the default on every purchase surface that has one, except the one that matters most for order value. The build-a-box flow and the single-flavor PDP both pre-select the subscription option and visually emphasize it (dark card, struck-through price on the PDP: "$79.00 → $67.15"), but the cart drawer has no equivalent AOV mechanic at all. Instead, the cart's only cross-sell slot shows a $5 measuring cup marked "OUT OF STOCK" as the first item a shopper sees (Source: site screenshots, cart-drawer.png). Every shopper who opens the cart is shown dead inventory before any live offer.

Message match between paid ads and the shared homepage is inconsistent by ad, not by channel. Ads 1 and 2 ("25g of Protein / 180-200 Calories / Zero Guilt," running since Aug 5, 2025) match the homepage headline and subhead closely. Ad 3 ("What if Cheat Day Was Every Day?" with a "RESTOCKED AFTER SELLING OUT" badge, running since Apr 14, 2026) introduces messaging that appears nowhere in the three homepage folds collected (Source: Meta Ads visual summary). Google Ads add two more claims absent from both Meta and the homepage: fiber content ("14-18g dietary fiber") and payment/shipping copy (Source: Google Ads visual summary).

Flavor inconsistency is corroborated by two independent sources. On-site reviews name carrot cake, lemon poppy seed, and blueberry as underperforming flavors (Source: Reviews). Amazon's Variety Pack SKU sits at 3.7/5 across 1,120 ratings, versus 4.2/5 for single-flavor SKUs (Source: last30days-ecom, Amazon). The gap points to the sampling/discovery experience, not the product itself.

Mobile performance is a hard constraint on every page in the funnel. Homepage and PDP both score 54/100 on Lighthouse mobile, with LCP at 7.3s and 6.8s respectively, roughly 3x Google's 2.5s "Good" threshold (Source: PageSpeed/Core Web Vitals, collected 2026-09-20). Server response time is fast (10ms) on both pages, so the delay is entirely front-end: ~800KB of unused JavaScript and up to 17.9s of main-thread work on the PDP.

Sessions/mo, AOV, and conversion rate were not collected for this engagement (no analytics source was in scope). The revenue potential lines below are directional, grounded in the evidence above, not dollarized estimates. Once analytics access is available, each slot can be re-scored against real traffic and AOV.

## Slot 1: Fix Mobile Load Speed on Homepage and PDP

**Type:** Immediate Fix
**Page:** Homepage and Build-a-Box PDP (https://bootyliciousmuffins.com/)

**What's broken:** Both pages score 54/100 on Lighthouse mobile. Homepage LCP is 7.3s (score 0.05) and PDP LCP is 6.8s (score 0.07), both roughly 3x Google's 2.5s "Good" threshold. Time to Interactive is 33.5s on the homepage and 25.3s on the PDP. Server response is fast (10ms) on both, so the delay is client-side: ~794-816 KiB of unused JavaScript per page and up to 17.9s of main-thread work on the PDP.

**Data:** PageSpeed/Core Web Vitals reports, collected 2026-09-20 (mobile only, homepage + PDP). Source: raw/pagespeed.md.

**Fix:** Audit and remove unused JavaScript bundles on both pages, prioritizing anything not required for the initial render (est. 800KB/page in savings identified). This is a performance defect, not a hypothesis to test, since a slower and a faster version of the same page have no meaningful "control vs. variant" comparison. Confirming impact requires before/after mobile conversion data once fixed. Desktop Core Web Vitals were not collected and should be checked as part of this fix.

## Slot 2: Cart Upsell Replacement

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (https://bootyliciousmuffins.com/)
**Revenue potential:** Sessions/mo and AOV were not collected for this brand, so a dollar estimate isn't calculable (see Missing Data in the audit). Directionally: every shopper who opens the cart sees the same dead-stock item first, making this a full-funnel-width fix with no traffic segment excluded.

**Hypothesis:** If we replace the first cross-sell slot in the "UPGRADE YOUR CART" carousel with an in-stock, relevant add-on, add-to-cart rate on that slot will increase because shoppers currently see "OUT OF STOCK" as their first and most visible option.

**Data:** The cart drawer's "UPGRADE YOUR CART" carousel shows a $5 measuring cup marked "OUT OF STOCK" in the first, most visible slot, with a partially visible recipe guide ("Bake Better Buns") next to it. Source: site screenshots (cart-drawer.png), site-visual-summary.md.

**V1:** Reorder the carousel so the in-stock "Bake Better Buns" recipe guide (or another in-stock add-on) occupies the first slot, and remove or de-prioritize the out-of-stock measuring cup until it's restocked. No other cart elements change: the line item, Subscribe & Save toggle, quantity stepper, "Checkout+" line, and red "Checkout+" CTA button stay as-is. Mobile: drawer slides in from the right as in the current build, carousel remains swipeable with arrow controls. Desktop: same drawer behavior, carousel arrows remain click-controlled.

## Slot 3: Surface Nutrition Facts on PDP Load

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (build-a-box, single-flavor variant)
**Revenue potential:** Not calculable without sessions/AOV data. Directionally: this affects 100% of PDP traffic, including all Meta and Google ad clicks, since both channels lead with the exact numbers hidden behind the collapsed accordion.

**Hypothesis:** If we expand the "Nutrition Highlights" accordion by default (or add a summary line above the accordions), shoppers arriving from ads will convert at a higher rate because the numbers they clicked on ("25g protein," "7g net carbs") will be visible without an extra tap.

**Data:** Below the "Add to Cart" button, four sections ("Product Description," "How to Make It," "Nutrition Highlights," "Nutritional Info") are collapsed by default with no teaser text, so a shopper must tap each one individually to see any content. Meta and Google ads both lead with exact nutrition numbers (25g protein, 7g net carbs, 14-18g fiber) that live inside these collapsed sections. Source: site screenshots (PDP fold 2), meta-ads-visual-summary.md, google-ads-visual-summary.md.

**V1:** Expand "Nutrition Highlights" by default on page load, keeping "Product Description," "How to Make It," and "Nutritional Info" collapsed as they are today. Mobile: expanded section sits directly below the buy box, pushing remaining accordions down; no change to tap targets on the still-collapsed sections. Desktop: same expansion behavior in the single-column content area below the buy box.

## Slot 4: Resolve the Homepage and PDP Dual-Path Purchase Flow

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage and Product Detail Page (https://bootyliciousmuffins.com/)
**Revenue potential:** Not calculable without sessions/AOV data. Directionally: this affects the two highest-traffic surfaces in the funnel (homepage and PDP) and touches every visitor choosing between the box-builder and a single-flavor purchase.

**Hypothesis:** If we demote the single-flavor "Add to Cart" cards on the homepage's "OUR BEST SELLERS" carousel below the "Build Your Box" entry point, more shoppers will enter the box-builder flow because the hero's single CTA ("Build Your Box") won't be undercut by a faster path one fold down.

**Data:** The homepage hero (fold 1) has one CTA, "Build Your Box." Fold 2 ("OUR BEST SELLERS") is a carousel where "Build Your Box" sits alongside three single-flavor cards, each with a direct "Add to Cart" button, letting a shopper skip the box-builder entirely. The PDP reverses this: its buy box includes a "Want to Mix & Match Muffins?" prompt with its own "Build Your Box" button, cross-selling shoppers back into the box-builder from a single-flavor page. Source: site screenshots (homepage fold 2, PDP fold 1), site-visual-summary.md.

**V1:** On the homepage carousel, move "Build Your Box" to the first position and visually distinguish it (larger card or badge) from the three single-flavor cards, which stay functional but visually secondary. No change to the PDP's "Want to Mix & Match Muffins?" cross-sell in this variation. Mobile: carousel keeps its horizontal swipe behavior, with "Build Your Box" as the first card a thumb reaches. Desktop: same reordering, arrows/scroll behavior unchanged.

## Slot 5: Fix Ad 3 Message-Match Gap

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (landing page for all Meta ads, https://bootyliciousmuffins.com/)
**Revenue potential:** Not calculable without ad-level traffic and conversion data. Directionally: this affects only the Ad 3 traffic segment, not the full homepage audience, since Ads 1-2 already match closely.

**Hypothesis:** If we add "cheat day" framing and restock acknowledgment to a homepage section shown to Ad 3 traffic, bounce rate for that segment will decrease because the page will continue the specific hook the shopper clicked on.

**Data:** Meta Ad 3 (Library ID 974220355004409, active since Apr 14, 2026) uses the headline "What if Cheat Day Was Every Day? 😋😋" with a "RESTOCKED AFTER SELLING OUT" badge. None of the three homepage folds collected contain "cheat day" language, a restock badge, or any stock-out acknowledgment. Ads 1-2, by contrast, match the homepage closely. Source: meta-ads-visual-summary.md (Ad 3), site screenshots (homepage folds 1-3).

**V1:** For traffic arriving from Ad 3's campaign (URL parameter or ad-level targeting), swap the homepage hero subhead to reference the restock ("Back in stock after selling out") and add "cheat day" framing to the existing subhead copy, without altering the hero's layout, image grid, or CTA. Ads 1-2 traffic sees the current, unchanged homepage. Mobile: same single-CTA hero layout, subhead copy only changes. Desktop: same hero layout, subhead copy only changes.

## Slot 6: Flavor-Before-Case-Size Sequencing

**Type:** A/B test (1 variation vs. control)
**Page:** Build-a-Box configurator (https://bootyliciousmuffins.com/)
**Revenue potential:** Not calculable without funnel/abandonment data. Directionally: this affects every shopper who enters the box-builder, the site's primary purchase path per the hero CTA.

**Hypothesis:** If we let shoppers select flavors before committing to a case size, build completion will increase because shoppers won't commit spend before knowing their preferred flavors are available.

**Data:** The build-a-box flow requires "STEP 1 - Select Case Size" (12/24/36-pack, priced $40.80-$90.95 with Subscribe & Save) before "STEP 2 - Select Flavors," where each flavor tile has a quantity stepper starting at 0. A progress bar tracks toward the case's item count. On-site reviewer Shane S. J. described disliking flavors from a first order before support helped recalibrate, consistent with a flow that asks for commitment before flavor discovery. Source: site screenshots (build-a-box fold 1), live WebFetch confirmation of Step 1/Step 2 structure (2026-09-21), reviews (Shane S. J.).

**V1:** Reverse the step order so flavor selection happens first (shoppers pick flavors and quantities freely), then case size and pricing tiers are presented based on the total items selected, using the same progress-bar mechanic. The Subscribe & Save default and pricing tiers stay unchanged. Mobile: same vertical step flow, flavor grid now appears first with the same quantity steppers. Desktop: same layout, step order only.

## Slot 7: Add Trust Signals Near Every Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage, Product Detail Page, and Cart (https://bootyliciousmuffins.com/)
**Revenue potential:** Not calculable without baseline conversion data. Directionally: this is a single bundled change (same copy, same placement pattern) applied to all three purchase surfaces, not three separate tests.

**Hypothesis:** If we add a concise guarantee and shipping-time line directly under the CTA on the homepage hero, PDP buy box, and cart drawer, conversion will increase because shoppers currently see no trust signal beyond the review count at any of the three purchase points.

**Data:** The homepage hero, PDP buy box, and cart drawer show no guarantee badge, shipping-time promise, or returns/refund copy near the CTA or line items. The only trust signal present anywhere in the funnel is the 4.7★/4,900-4,957-review line. The live homepage fetch (2026-09-21) confirms "Returns & Refunds," "Shipping Policy," and "Cancellation Policy" links exist on the site, but none surface near the point of purchase in the folds and pages captured. Source: site-visual-summary.md (homepage fold 1, PDP fold 1, cart drawer), live homepage WebFetch (2026-09-21).

**V1:** Add one line of guarantee/shipping copy (e.g., referencing the existing Returns & Refunds and Shipping Policy already live on the site) directly beneath the CTA in all three locations: homepage hero (below "Build Your Box"), PDP buy box (below the Subscribe & Save/One-time selector), and cart drawer (below the "Checkout+" button). No other layout changes on any of the three surfaces. Mobile: single line of text, no icon required to avoid adding vertical space to already-tall mobile folds. Desktop: same single line, positioned identically relative to each CTA.

## Slot 8: Flavor Recommendation Prompt in Build-a-Box

**Type:** A/B test (1 variation vs. control)
**Page:** Build-a-Box configurator (https://bootyliciousmuffins.com/)
**Revenue potential:** Not calculable without sessions/AOV data. Directionally: this targets first-time box-builders specifically, the segment most likely to churn after a mismatched first order.

**Hypothesis:** If we add a "Start Here" flavor recommendation to the Step 2 flavor grid, first-order flavor satisfaction will increase because shoppers currently pick without guidance and land on underperforming flavors at a higher rate.

**Data:** Amazon's Variety Pack SKU sits at 3.7/5 (1,120 ratings) versus 4.2/5 for single-flavor SKUs. On-site reviews independently name carrot cake, lemon poppy seed, and blueberry as underperforming, and reviewer Shane S. J. described disliking flavors from a first order before support intervened. Source: last30days-ecom.md (Amazon), reviews.md (Shane S. J., Bonnie E., Marsha M.).

**V1:** Add a small "Start Here: Customer Favorites" label above 3-4 flavor tiles in the Step 2 flavor grid (Double Chocolate, Birthday Cake, Red Velvet, Cinnamon Bun, the flavors named as favorites in reviews), with no change to the grid layout, quantity steppers, or remaining flavor tiles. Mobile: label sits above the flavor grid, same scroll behavior. Desktop: same label placement, same grid.

## Future Slot Candidates

1. **Checkout+ default-state disclosure** - The cart's $1.95 "Loss, theft & damage" line item has no visible checkbox or toggle in the captured screenshot, so it's unknown whether it's bundled by default. Requires a live add-to-cart test to confirm the default state before a test can be specced; if confirmed pre-selected, this becomes a high-priority slot.
2. **Prep-texture expectation-setting on PDP** - Cross-platform creator commentary (TikTok, Instagram) repeatedly describes the pre-microwave texture as wet or "gooey," with no matching expectation-setting copy found on the PDP. Directional only, not corroborated by first-party site reviews, so it's held back pending stronger first-party evidence.
3. **Announcement bar / FIRST15 code verification** - The Meta ad screenshots show a FIRST15 announcement bar that the live homepage WebFetch (2026-09-21) did not return. Could be removed, or rendered client-side and missed by an automated fetch. Needs a manual browser check before treating as a message-match finding.
