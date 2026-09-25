# Kill Crew CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed / Core Web Vitals, Current Site Screenshots, Non-Data Context, Social & Community Research (last30days-ecom)

Two of Kill Crew's three active Meta ads, Ads 1 and 2, promote a specific reptile-print shorts set and both route to the same 34-item mixed collection page with no banner, header, or visual anchor connecting to the product shown in the ad, and no review count, star rating, or guarantee in the first three folds (Source: Meta Ads and Landing Pages). Ad 3 has the strongest message match of the three, its PDP copy echoes the ad's squat-proof, chafe-proof language nearly verbatim, but a live re-check on 2026-09-11 found that exact product is now out of stock. The best-matched ad in the account is currently sending paid clicks to a page with no purchase path (Source: Non-Data Context, live re-fetch).

Site speed compounds the problem on the same templates ads route to. Mobile PageSpeed shows homepage LCP at 6.4s and PDP LCP at 8.0s, both far past Google's 4s "poor" threshold, and the homepage Lighthouse run itself carries a warning that the page loaded too slowly to finish within the time limit (Source: PageSpeed / Core Web Vitals). PDP also shows a CLS of 0.144, bordering "needs improvement." This is a tax on every visitor who reaches the exact pages the ad budget is built to drive traffic to.

Trust signals are placed inconsistently across the funnel. The PDP shows 4.8 stars and 2,437 reviews twice plus a 6-icon trust bar, but that proof disappears entirely on the homepage, which leans on a round "500,000 orders" claim instead, and in the cart drawer, the last screen before checkout (Source: Current Site Screenshots). Google Ads separately cite "4.9 stars (10)" and "10,000+ verified reviews at 5 stars," a claim that appears in neither the Meta ads nor anywhere on site (Source: Google Ads Transparency). None of these three numbers agree with each other.

No sessions/mo or AOV figures were collected for Kill Crew this cycle (the only traffic figure available, ~196.6K monthly visits, is an unverified third-party estimate). Revenue potential below is stated qualitatively by funnel position and evidence strength rather than as a dollar estimate, since inventing a number would not be grounded in the data collected.

---

## Slot 1: Fix or Redirect Ad 3's Out-of-Stock PDP

**Type:** Immediate Fix
**Page:** Product Detail Page, Muay Thai Shorts Mid Thigh Cut Floral - Black (Ad 3 landing page)

**Why this is the priority:** Ad 3 is the strongest message-match ad in the account, its headline claims and PDP copy align nearly verbatim, and it carries the audit's strongest trust stack (4.8 stars/2,437 reviews shown twice, a 6-icon trust bar, financing options). A live re-fetch on 2026-09-11 found this exact product out of stock, with the Add to Cart button replaced by "Notify me when available." If the ad is still live, paid spend is landing on a page with no purchase path. This is a broken funnel step to fix, not a design hypothesis to test: either restock the product, swap the ad's destination to an in-stock colorway, or pause the ad until stock returns.

---

## Slot 2: Bridge Message Match on the Reptile-Shorts Collection Page

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page, killcrew.co/collections/reptile-shorts (Ad 1 & Ad 2 landing page)
**Revenue potential:** Not calculable, no sessions/AOV data collected for Kill Crew this round (see audit Missing Data). Directional priority: this page absorbs 2 of the 3 active Meta ads, 67% of Meta ad spend by unit count, with zero visible bridge to the product shown in either ad.

**Hypothesis:** If we add a hero banner at the top of the collection page that echoes the exact product and colorway shown in Ads 1 and 2, plus a star rating strip, bounce from paid traffic will drop because visitors see confirmation they landed in the right place instead of a generic mixed grid.

**Data:** Ads 1 and 2 both advertise a specific reptile-print shorts-and-tee set and route to the same URL, a collection page that opens on a mixed grid of shorts and t-shirts in assorted prints with the exact advertised colorway not the first product visible. No trust signal, review count, star rating, or guarantee appears anywhere in the first three folds, the only visible credibility element is a "Free Shipping $75+" promo bar (Source: Meta Ads and Landing Pages).

**V1:** Add a full-width banner directly under the top promo bar, before the filter sidebar and product grid, showing the product image and colorway from the ad creative with a line of copy naming it ("As seen in our ad: [Reptile Shorts]") and a star rating/review count strip beneath it. Everything below the banner, the filter sidebar, product grid, and sort options, stays unchanged. On mobile, the banner sits full-width above the collapsed filter toggle, image and copy stacked vertically; on desktop it spans the width of the grid above the sidebar-plus-grid layout.

---

## Slot 3: Reduce PDP Load Time

**Type:** Immediate Fix
**Page:** Product Detail Page template (Ad 3 landing page and all PDPs)

**Why this is the priority:** The PDP template, the same template Ad 3 lands on, scores 63/100 on mobile Lighthouse (data collected 2026-09-10) with Largest Contentful Paint at 8.0 seconds against a 2.5s "good" benchmark and Time to Interactive at 12.7 seconds (Source: PageSpeed / Core Web Vitals). CLS sits at 0.144, bordering "needs improvement." This is a page-health problem that caps every other PDP test's ceiling until it's fixed: no copy or layout change survives an 8-second load.

---

## Slot 4: Reduce Homepage Load Time

**Type:** Immediate Fix
**Page:** Homepage (killcrew.co)

**Why this is the priority:** The homepage scores 58/100 on mobile Lighthouse (data collected 2026-09-10), with LCP at 6.4 seconds and Time to Interactive at 12.4 seconds, and the Lighthouse run itself carries a warning that the page loaded too slowly to finish measurement within the time limit (Source: PageSpeed / Core Web Vitals). That run-warning is a severity signal beyond the raw score. The homepage is the default landing point for organic, social, and direct traffic, so this tax hits every visitor who isn't arriving through a paid ad's own landing page.

---

## Slot 5: Add a Sticky Nav Bar to the Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (killcrew.co)
**Revenue potential:** Not calculable, no sessions/AOV data collected for Kill Crew this round (see audit Missing Data). Directional priority: this closes the gap in the only funnel entry point with zero persistent path to purchase past the first fold.

**Hypothesis:** If we make the nav bar and primary CTAs sticky past the hero, add-to-collection clicks from the homepage will increase because visitors don't have to scroll back to the top to act once they've moved past fold 1.

**Data:** The homepage nav bar and both primary CTAs, "SHOP MENS" and "SHOP WOMENS," live only in fold 1, directly under the hero. The nav scrolls fully out of view by fold 2 and does not reappear in fold 3; once a visitor scrolls into the Featured Products or Shop by Category sections, there is no sticky header, sticky CTA bar, or persistent way to navigate or purchase without scrolling back up (Source: Current Site Screenshots).

**V1:** Make the existing nav bar sticky, pinned to the top of the viewport, from fold 2 onward, keeping its current logo, menu items, and cart icon unchanged. On mobile, collapse it to a slim sticky bar with the hamburger menu, logo, and cart icon; on desktop, keep the full nav bar sticky at its current height. No new elements are added, the existing fold-1 nav simply persists on scroll.

---

## Slot 6: Surface Review Proof in the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart Drawer
**Revenue potential:** Not calculable, no cart-to-checkout conversion baseline collected for Kill Crew this round (see audit Missing Data). Directional priority: this closes the one funnel step where the PDP's strongest trust asset is completely absent, at the last screen before checkout.

**Hypothesis:** If we add the 4.8-star/2,437-review count to the cart drawer, checkout starts will increase because the reassurance a visitor saw on the PDP is still visible at the moment they're about to pay.

**Data:** The PDP shows 4.8 stars and 2,437 reviews twice plus a 6-icon trust bar. The cart drawer, a right-side slide-in panel with a free-shipping progress bar, the cart line item, a "Check These Out!" upsell row, and a 4-icon trust row (Ships from USA, Ships within 24 Hours, Free Returns & Exchanges, Support Suicide Prevention) at the bottom, shows no star rating or review count anywhere (Source: Current Site Screenshots).

**V1:** Add a single line, "4.8 stars, 2,437 reviews," directly under the "KILL CREW" header at the top of the drawer, above the free-shipping progress bar. Everything else in the drawer, the progress bar, line item, upsell row, checkout button, and existing trust icon row, stays unchanged. On mobile and desktop the drawer layout and width are identical, so the same single-line placement applies to both.

---

## Slot 7: Align Homepage Trust Signal With the Site's Actual Review Volume

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (killcrew.co)
**Revenue potential:** Not calculable, no sessions/AOV data collected for Kill Crew this round (see audit Missing Data). Directional priority: this closes a three-way mismatch between what Google Ads promises, what the PDP shows, and what the homepage, the default landing point for most traffic, currently displays.

**Hypothesis:** If we replace the homepage's "500,000 orders" claim with the 4.8-star/2,437-review count already used on the PDP, trust at first landing will increase because the number matches both what a specific-review claim in Google Ads promises and what the PDP itself later confirms.

**Data:** The homepage hero shows a round "Over 500,000 orders from happy customers" claim with a 5-star icon but no specific star score or review count anywhere across the three captured folds (Source: Current Site Screenshots). Google Ads separately cite "4.9 stars (10)" and "10,000+ verified reviews at 5 stars," a claim not reflected on the homepage or in Meta ad creative (Source: Google Ads Transparency), while the PDP itself displays 4.8 stars/2,437 reviews (Source: Meta Ads and Landing Pages). Three different numbers currently represent the brand's review proof across three surfaces.

**V1:** Replace the existing "Over 500,000 orders from happy customers" line in the hero with "4.8 stars, 2,437 reviews," keeping the same position, font size, and 5-star icon treatment already in place. No other hero elements, the wordmark, hero image, nav, or CTAs, change. Mobile and desktop keep their current hero layout, only the claim text and underlying number change.

---

## Slot 8: Add Sale Badges to the Reptile-Shorts Collection Page

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page, killcrew.co/collections/reptile-shorts
**Revenue potential:** Not calculable, no AOV or add-to-cart baseline collected for Kill Crew this round (see audit Missing Data). Directional priority: this adds a documented-absent urgency lever to the same page 2 of 3 active Meta ads route to.

**Hypothesis:** If we add sale badges and compare-at pricing to products on the collection grid, add-to-cart rate will increase because visitors see a concrete discount instead of a flat price with no urgency signal.

**Data:** No sale badges or compare-at pricing appear anywhere across the collection page or the Ad 1/2 landing page, six folds observed in total (Source: Meta Ads and Landing Pages, Current Site Screenshots). One Google Ads Shopping unit separately promotes Muay Thai Flame Shorts at $50 with a "Free" shipping badge, confirming the brand runs discount-style messaging in ads but not on the collection grid itself (Source: Google Ads Transparency).

**V1:** Add a small red "SALE" badge to the top-left corner of each product tile currently carrying a discount, with compare-at pricing (strikethrough original price next to the sale price) directly under the product title. Grid layout, filter sidebar, and sort options stay unchanged. On mobile, the badge and compare-at price scale down with the smaller tile size; on desktop they appear at full size in the same corner and under-title position.

---

## Future Slot Candidates

1. **Reconcile the squat-proof claim against the Trustpilot "see-through when squatting" report** - The core performance claim in Ad 3, PDP copy, and most TikTok UGC is corroborated by two independent reviewers but directly contradicted by one Trustpilot complaint. Not a standard A/B test, recommend as a client-facing QA flag, potentially paired with PDP fit guidance if the client confirms a batch-specific cause.
2. **Investigate Trustpilot fulfillment and refund complaints** - A $24.85 unexplained refund deduction, a wrong item shipped with no offered free return, and an unmet expedited-shipping promise are documented on the same 6-review Trustpilot profile driving a 2.3 TrustScore outlier against the on-site 4.8+ widget. Operational/fulfillment issue, not a CRO test.
