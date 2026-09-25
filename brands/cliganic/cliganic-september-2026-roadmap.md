# Cliganic CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots (homepage, collection, cart), Reviews & UGC, Social & Community Research (last30days-ecom, directional)

The Organic Jojoba Oil PDP takes 33.9 seconds to reach Largest Contentful Paint and 60.1 seconds to become fully interactive on mobile, against a homepage LCP of 7.2s on the same connection profile (Source: PageSpeed, mobile, Sep 2026). This matters because two of the three collected Meta ads land traffic directly on this page. Most paid clicks are likely hitting a page that hasn't rendered its main content before a typical mobile visitor gives up.

Ad-to-page mismatches show up on both paid channels. Ad 2's headline stat, "95% said hair looked shinier after 14 days," never appears on its landing page, which instead discloses "93% felt stronger, 91% looked fuller" after 28 days (Source: Meta Ads). Ad 3 promises "$12.99" and "#1 Best Seller on Amazon" but lands on the 16oz size at $28.89 with no Amazon reference on the page (Source: Meta Ads). On Google, roughly 20 ad units cite Amazon-sourced review counts as high as "42,000+," while the jojoba oil PDP itself shows "4.8/5 (279 Verified Reviews)" (Source: Google Ads Transparency, Site Screenshots) — a gap large enough to read as bait-and-switch to a skeptical visitor.

Default-selection patterns favor revenue over transparency at two points in the funnel. Subscribe & Save is pre-selected over one-time purchase in the PDP buy box on both jojoba oil ad-landing states, and a "SavedBy Package Protection" add-on ($2.47) is bundled into the cart checkout total by default, with opt-out only available via a small secondary text link rather than an unchecked box (Source: Meta Ads, Site Screenshots). Directional social research (PissedConsumer, small sample, 1.1-star) flags unwanted recurring charges as a live complaint pattern, though this is not corroborated in the first-party review set collected here (Source: last30days-ecom).

One social-research finding is corroborated by first-party evidence: plastic-bottle-vs-glass is the single most repeated complaint across the collected Amazon and on-site reviews, said independently by at least three reviewers (Source: Reviews). This is a packaging and product issue for the client team, not a CRO test, and is flagged here for visibility only.

No monthly sessions or AOV figures were collected for Cliganic in this round, so revenue impact below is directional rather than dollar-estimated. The math should be run once traffic and AOV data are available.

## Slot 1: Fix PDP Mobile Load Time

**Type:** Immediate Fix
**Page:** Product Detail Page — Organic Jojoba Oil (mobile)

**Why this is the priority:** The PDP that carries the majority of paid traffic (2 of 3 Meta ads) is effectively broken on mobile: 33.9s to Largest Contentful Paint and 60.1s to become interactive, roughly 13x Google's "poor" LCP threshold of 2.5s. This is a page-health problem, not a design hypothesis, and it caps every other test's ceiling until it's fixed.

**What's broken:** Organic Jojoba Oil PDP scores Performance 0.28 on mobile PageSpeed: LCP 33.9s, FCP 18.4s, Total Blocking Time 1,650ms, Time to Interactive 60.1s. CLS is 0, ruling out layout shift — the bottleneck is render-blocking load and script execution. The homepage on the same connection profile scores far better (LCP 7.2s, Performance 0.32), confirming the PDP has its own outlier resources.

**Evidence:** pagespeed-pdp.json, pagespeed-homepage.json (mobile, collected Sep 2026).

**Recommended fix:** Audit and reduce the PDP's render-blocking scripts and Total Blocking Time (1,650ms) to bring LCP toward the sub-10s range at minimum, ideally under Google's 2.5s "good" threshold. Prioritize this over every other slot below — no ad, copy, or default-selection fix pays off if the majority of paid mobile clicks abandon before the page renders.

## Slot 2: Align Review-Count Claims With the PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page — Organic Jojoba Oil (organic.jojoba-oil PDP)
**Revenue potential:** Not calculable — no monthly sessions or AOV data collected for Cliganic in this round (see audit Missing Data). Directional priority: this closes a two-order-of-magnitude trust gap at the exact page a large share of Google traffic lands on.

**Hypothesis:** If we show a review count that matches the volume Google ad traffic was promised, trust-driven bounce will drop because visitors won't hit a page that looks like it under-delivers on the claim that brought them there.

**Data:** Google Ads Transparency Center shows roughly 20 ad units citing Amazon-sourced review counts of "35,000+," "42,000+," and "(9,458)." The jojoba oil PDP that this traffic lands on shows only "4.8/5 (279 Verified Reviews)" directly under the top nav, above the headline, with no combined or Amazon-inclusive count anywhere on the page (Source: raw/google-ads-visual-summary.md, raw/meta-ads-visual-summary.md).

**V1:** Add a second, clearly labeled trust line next to the existing "4.8/5 (279 Verified Reviews)" showing the combined review count across site and Amazon (e.g. "4.8/5 · 279 site reviews · 35,000+ across Amazon"), placed at the same above-the-fold prominence as the existing rating. Mobile: stack the two counts on separate lines directly under the product title to avoid crowding the fold. Desktop: keep them on one line beside the star rating. Same placement logic used across trust-badge treatments in pdp-structure.md — putting store-level trust signals at the very top of the page (KB: resources/kb/pdp-structure.md). Do not change any other PDP element.

## Slot 3: Fix Ad 2's Stat Mismatch on the Rosemary Oil PDP

**Type:** Immediate Fix
**Page:** Product Detail Page — Rosemary Repair Scalp & Strand Oil

**Why this is the priority:** A visitor who clicks on a specific stat and lands on a page that discloses a different stat and timeframe hits an immediate credibility break at the moment of arrival. This is a factual mismatch to correct, not a design variant to test.

**What's broken:** Ad 2's headline claim is "In a consumer trial, after 14 days: 95% of consumers said their hair looked shinier with smoother ends." The Rosemary Repair Scalp & Strand Oil PDP it lands on instead discloses, in its fold-2 description accordion, "After 28 days of use, 93% of consumers said their hair felt visibly stronger, and 91% said their hair looked visibly fuller." The specific number and timeframe promised in the ad does not appear on the page.

**Evidence:** raw/meta-ads-visual-summary.md (Ad 2, Landing Page Fold 1-2).

**Recommended fix:** Reconcile the two data sets — either surface the ad's exact 95%/14-day stat on the PDP fold 1 (if it is a real, disclosable trial result), or update the ad copy to match the page's disclosed 93%/91% at 28 days. Whichever number is accurate should appear in both places, verbatim.

## Slot 4: Resolve Ad 3's Price and Positioning Mismatch

**Type:** Immediate Fix
**Page:** Product Detail Page — Organic Jojoba Oil (Ad 3 landing state)

**Why this is the priority:** Advertising one price and landing on a page defaulted to a different, higher price point is a direct trust break at the exact moment a visitor is deciding whether to buy. This needs a default-state correction, not a test.

**What's broken:** Ad 3's creative shows a "$12.99" price and "#1 Best Seller on Amazon" badge overlay. The PDP it drives to defaults its size selector to 16oz at $28.89 (was $33.99, tagged "MOST POPULAR"), with no Amazon best-seller reference anywhere on the page.

**Evidence:** raw/meta-ads-visual-summary.md (Ad 3, Landing Page Fold 1).

**Recommended fix:** Default the size selector to the size/price combination that matches Ad 3's advertised $12.99 when a visitor arrives via this ad's UTM or creative ID, so the landed price matches what was promised. If the "#1 Best Seller on Amazon" claim is accurate, carry it onto the page; if it isn't verifiable for the site listing, remove it from the ad.

## Slot 5: Un-Bundle the Default Package Protection Add-On

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer
**Revenue potential:** Not calculable — no cart-to-checkout conversion baseline collected for Cliganic in this round (see audit Missing Data). Directional priority: the add-on represents roughly 20% of order value in the single-item cart captured, and social research directionally flags unwanted recurring/add-on charges as a live complaint pattern.

**Hypothesis:** If we make the "SavedBy Package Protection" add-on opt-in instead of opt-out by default, checkout abandonment from visitors who feel surprised by the total will drop because the total they see matches what they intended to buy.

**Data:** In the cart drawer, "SavedBy Package Protection" ($2.47) is bundled into the checkout total by default — the primary CTA reads "CHECKOUT+ • $12.34," already including the add-on — with removal only possible via a small secondary text link reading "Continue without package protection." There is no unchecked checkbox or opt-in toggle (Source: raw/site-visual-summary.md, Cart Drawer). Directional social research (PissedConsumer, small sample) flags unwanted recurring or add-on charges as a complaint pattern, though this is not corroborated by the first-party reviews collected for this audit.

**V1:** Replace the auto-bundled add-on with an unchecked checkbox labeled "Add Package Protection — $2.47" placed above the CTA, so the button total reflects only the cart's actual items until the shopper opts in. Mobile: place the checkbox directly under the free-shipping progress bar, full-width and easy to tap. Desktop: place it in the same position, inline with the order subtotal line. No other cart drawer element changes.

## Slot 6: Add Guarantee Copy to the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer
**Revenue potential:** Not calculable — no cart abandonment baseline collected for Cliganic in this round (see audit Missing Data). Directional priority: this closes the one funnel step where the PDP's strongest anxiety-removal signal is absent.

**Hypothesis:** If we carry the 60-Day Money-Back Guarantee into the cart drawer, cart abandonment will drop because the anxiety-reducing signal a visitor saw on the PDP is still visible at the last screen before checkout.

**Data:** The 60-Day Money-Back Guarantee appears directly below the Add to Bag button on every ad-landing PDP fold captured (Ad 1, Ad 2, Ad 3), alongside Free Shipping and HSA/FSA badges. None of this trust copy carries into the cart drawer — the drawer's only trust element is a "500,000+ 5-Star Reviews" line at the very bottom, with no guarantee or returns copy visible anywhere (Source: raw/meta-ads-visual-summary.md, raw/site-visual-summary.md).

**V1:** Add a single-line guarantee badge ("60-Day Money-Back Guarantee") directly above the checkout CTA, next to or below the existing "500,000+ 5-Star Reviews" line. Mobile: stack the guarantee line above the CTA button, full-width. Desktop: place it inline with the reviews line in the same trust row. Anxiety is handled at the exact point it can still change the outcome, the last screen before checkout (KB: resources/kb/cro-system.md). No other cart drawer element changes.

## Slot 7: Route the Homepage Hero Toward the Product Paid Traffic Promotes

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** Not calculable — no homepage paid-vs-organic session share collected for Cliganic in this round (see audit Missing Data). Directional priority: 2 of the 3 collected Meta ads drive to jojoba oil, and it's the homepage's own "BEST SELLER" carousel item.

**Hypothesis:** If we feature Organic Jojoba Oil in the homepage hero instead of a scroll away, visitors arriving from jojoba oil ads or navigating back to the homepage will convert at a higher rate because the first thing they see matches what brought them to the site.

**Data:** The homepage hero is a full-bleed lifestyle photo promoting Rosemary Repair Scalp & Strand Oil, headline "Make Every Day A Great Hair Day!" with a "TRY IT NOW!" button. Organic Jojoba Oil, the product 2 of 3 collected Meta ads drive to and the one carrying the "BEST SELLER" badge in the homepage's own product carousel, only appears after scrolling past the hero into fold 2's Best Sellers module (Source: raw/site-visual-summary.md, Homepage Fold 1-2).

**V1:** Replace the hero photo, headline, and CTA with a jojoba oil variant ("BEST SELLER" badge carried into the hero, product shot, and a headline built from the same "clean, natural" positioning used in Ad 1), linking directly to the jojoba oil PDP. Mobile: single full-bleed hero image with headline and CTA stacked below, same layout pattern as the current hero. Desktop: same hero structure, image and copy swapped only. Handing visitors what they already came for reduces the friction of digging through the menu or scrolling to find it (KB: resources/kb/cro-system.md). Keep the rest of the homepage, including the existing Best Sellers carousel, unchanged.

## Slot 8: Strengthen the Subscribe & Save Default on the PDP Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page — Organic Jojoba Oil (both ad-landing states)
**Revenue potential:** Not calculable — no PDP add-to-cart baseline collected for Cliganic in this round (see audit Missing Data). Directional priority: this is the pattern most directly aligned with the recurring-charge complaints flagged directionally in social research.

**Hypothesis:** If we keep Subscribe & Save as the pre-selected default but add a clear "Subscription" label and explicit benefit copy under it, add-to-cart will hold steady or improve while unwanted-charge confusion drops, because visitors can see plainly that they've selected a recurring option and what they get for it.

**Data:** On both jojoba oil ad-landing states (Ad 1's 4oz/24%-off default, Ad 3's 16oz/15%-off default), Subscribe & Save is pre-selected over one-time purchase in the buy box, with no visual distinction calling out that a recurring subscription is the default choice rather than a one-time purchase (Source: raw/meta-ads-visual-summary.md, Ad 1 and Ad 3 Fold 1). Directional social research (PissedConsumer, Trustpilot) flags unwanted recurring-charge complaints, though this is not corroborated in the first-party review set collected here (Source: raw/last30days-ecom.md).

**V1:** Keep Subscribe & Save pre-selected (removing the default is not supported by this data set and runs against it being the highest-leverage AOV lever on the page), but add a visible "Subscription" tag on the selected option plus one line of benefit copy underneath it: "Save 24% + free shipping + more subscriber benefits," scaled to whichever discount tier is live for that size. Mobile: tag and benefit line sit directly under the selected radio option, full-width. Desktop: same copy, positioned inline to the right of the option. Making the higher-AOV default clearer and more attractive, rather than removing it, is the standard PDP buy-box pattern (KB: resources/kb/pdp-structure.md). No other buy box element changes.

## Future Slot Candidates

1. **Surface per-card review counts on the collection page** - Collection cards show a star rating but no review count; the count only appears after clicking into the PDP, missing a chance to reinforce trust before the click. (Source: raw/site-visual-summary.md)
2. **Surface the free-shipping progress bar earlier, on the PDP** - The cart drawer's 3-tier free-shipping/free-gift/free-tumbler progress bar is a strong AOV mechanic, but it only appears after add-to-cart. No equivalent exists on the PDP itself in any of the three ad-landing folds captured. (Source: raw/site-visual-summary.md, raw/meta-ads-visual-summary.md)
3. **Default collection-page filtering** - The Collection page shows "Filters (0)" applied by default across 172 products despite an 8-tile subcategory nav, a discovery-friction opportunity. (Source: raw/site-visual-summary.md)
4. **Reconcile review-count figures across the catalog** - The homepage marquee and Google ads cite "500,000+" and "35,000-42,000+" review figures, an order of magnitude above the 279 shown on the jojoba oil PDP, likely because they aggregate across the full catalog or Amazon storefront. Needs client-side clarification before any test treats these as interchangeable. (Source: raw/site-visual-summary.md, raw/google-ads-visual-summary.md)
