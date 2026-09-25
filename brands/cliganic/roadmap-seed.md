# Cliganic Roadmap Seed

**Store:** cliganic.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots (homepage, collection, cart), Reviews & UGC, Social & Community Research (last30days-ecom, directional)

## Key Insights

Mobile PDP load time is a severe, quantified blocker: the Organic Jojoba Oil PDP scores 33.9s LCP and 60.1s Time to Interactive (Performance score 0.28), against a homepage LCP of 7.2s on the same connection profile. This matters because two of the three collected Meta ads land traffic directly on this PDP — most paid clicks likely hit a page that hasn't rendered its main content by the time a typical mobile visitor would abandon.

Ad-to-page mismatches recur across both paid channels. On Meta, Ad 2's headline stat ("95% said hair looked shinier... after 14 days") never appears on its landing page, which instead discloses "93% felt stronger, 91% looked fuller" after 28 days — different numbers, different timeframe. Ad 3 promises "$12.99" and "#1 Best Seller on Amazon" but lands on the 16oz size at $28.89 with no Amazon reference anywhere on the page. On Google, roughly 20 ad units cite Amazon-sourced review counts as high as "42,000+," while the actual jojoba oil PDP shows "4.8/5 (279 Verified Reviews)" — a gap large enough to read as bait-and-switch to a skeptical visitor.

Default-selection patterns favor revenue over transparency at two separate funnel points: Subscribe & Save is pre-selected over one-time purchase in the PDP buy box (both ad-landing states), and a "SavedBy Package Protection" add-on ($2.47) is bundled into the cart checkout total by default, with opt-out only available via a small secondary text link rather than an unchecked box. Directional social research (PissedConsumer, small sample, 1.1-star) flags unwanted recurring charges as a live complaint pattern, though this is not corroborated in the first-party review set collected here. One social-research finding is corroborated by first-party evidence: plastic-bottle-vs-glass is the single most repeated complaint across the collected Amazon and on-site reviews ("was expecting a glass bottle," "just wish it came in a glass bottle instead of plastic," said independently by at least three reviewers) — this is a packaging/product issue for the client team, not a CRO test.

## Top Test Opportunities

### 1. Fix PDP Mobile Load Time
**What's broken:** The Organic Jojoba Oil PDP takes 33.9 seconds to reach Largest Contentful Paint and 60.1 seconds to become fully interactive on mobile (Performance score 0.28). The homepage on the same connection type scores far better (7.2s LCP), so the PDP's specific render-blocking resources are the outlier. CLS is 0 on both pages, ruling out layout shift as a factor — the bottleneck is load and script execution, reflected in a Total Blocking Time of 1,650ms.
**Evidence:** pagespeed-pdp.json, pagespeed-homepage.json
**Key data:** PDP LCP 33.9s vs. homepage LCP 7.2s; PDP TTI 60.1s; Google's "poor" LCP threshold is 2.5s+, so this PDP is roughly 13x that threshold.
**Est. lift:** Not calculable without sessions/AOV data (see Missing Data in audit). Directionally: recovering even a fraction of currently-bouncing paid mobile sessions on the PDP that both live Meta jojoba-oil ads (Ad 1, Ad 3) drive to would be the single highest-leverage fix available in this data set.

### 2. Align Google Ads Review-Count Claims With the PDP
**What's broken:** Google Ads Transparency Center shows ad copy citing Amazon-sourced review counts like "35,000+," "42,000+," and specific counts such as "(9,458)." The jojoba oil PDP that Meta traffic lands on shows "4.8/5 (279 Verified Reviews)" directly under the top nav, above the headline — no combined or Amazon-inclusive count appears anywhere on that page.
**Evidence:** raw/google-ads-visual-summary.md, raw/meta-ads-visual-summary.md (Ad 1, Ad 3 fold 1)
**Key data:** Google ad review counts range 9,000-42,000+; on-site PDP shows 279.
**Est. lift:** Not calculable without paid-traffic session data. Directionally: closing a two-order-of-magnitude trust gap at the exact page google traffic lands on should reduce bounce from visitors who feel misled.

### 3. Fix Ad 2's Stat Mismatch on the Rosemary Oil PDP
**What's broken:** Ad 2's headline claim is "In a consumer trial, after 14 days: 95% of consumers said their hair looked shinier with smoother ends." The Rosemary Repair Scalp & Strand Oil PDP it lands on instead discloses, in its fold-2 description accordion (open by default), "After 28 days of use, 93% of consumers said their hair felt visibly stronger, and 91% said their hair looked visibly fuller," with a methodology footnote. The specific number and timeframe promised in the ad is absent from the page entirely.
**Evidence:** raw/meta-ads-visual-summary.md (Ad 2, Landing Page Fold 1-2)
**Key data:** Ad claims 95%/14 days; page discloses 93% and 91%/28 days.
**Est. lift:** Not calculable without this SKU's session/AOV data.

### 4. Resolve Ad 3's Price and Positioning Mismatch
**What's broken:** Ad 3's creative shows a "$12.99" price and "#1 Best Seller on Amazon" badge overlay on the product image. The PDP it drives to defaults its size selector to 16oz at $28.89 (was $33.99, tagged "MOST POPULAR"), a different price point than advertised, with no Amazon best-seller reference anywhere on the page.
**Evidence:** raw/meta-ads-visual-summary.md (Ad 3, Landing Page Fold 1)
**Key data:** Ad price $12.99 vs. landed default price $28.89.
**Est. lift:** Not calculable without this ad's session/AOV data.

### 5. Un-Bundle the Default Package Protection Add-On in Cart
**What's broken:** In the cart drawer, a "SavedBy Package Protection" line item ($2.47) is bundled into the checkout total by default — the primary CTA reads "CHECKOUT+ • $12.34" (already including the add-on), and the only way to remove it is a small secondary text link below the button reading "Continue without package protection." There is no unchecked checkbox or opt-in toggle.
**Evidence:** raw/site-visual-summary.md (Cart Drawer — AOV elements)
**Key data:** Add-on is $2.47 on a single-item cart totaling $12.34; the add-on represents roughly 20% of the total order value in this captured state.
**Est. lift:** Not calculable without cart-to-checkout conversion baseline.

### 6. Add Guarantee/Trust Copy to the Cart Drawer
**What's broken:** The 60-Day Money-Back Guarantee appears directly below the Add to Bag button on every ad-landing PDP fold captured (Ad 1, Ad 2, Ad 3), alongside Free Shipping and HSA/FSA badges. None of this trust copy carries into the cart drawer — the drawer's only trust element is a "500,000+ 5-Star Reviews" line at the very bottom, with no guarantee or returns copy visible anywhere in the drawer.
**Evidence:** raw/meta-ads-visual-summary.md (PDP trust signals, all 3 ads), raw/site-visual-summary.md (Cart Drawer — Trust signals)
**Key data:** Guarantee badge present on PDP folds, absent from cart drawer entirely.
**Est. lift:** Not calculable without cart abandonment baseline.

### 7. Route the Homepage Hero Toward the Product Paid Traffic Actually Promotes
**What's broken:** The homepage hero is a full-bleed lifestyle photo promoting Rosemary Repair Scalp & Strand Oil, with headline "Make Every Day A Great Hair Day!" and a "TRY IT NOW!" button. Organic Jojoba Oil — the product 2 of 3 collected Meta ads drive to, and the one carrying the "BEST SELLER" badge in the homepage's own product carousel — only appears after scrolling past the hero into fold 2's Best Sellers module.
**Evidence:** raw/site-visual-summary.md (Homepage, Fold 1-2), raw/meta-ads-visual-summary.md (2 of 3 ads are jojoba oil)
**Key data:** Jojoba oil requires a fold-2 scroll to reach from the homepage hero.
**Est. lift:** Not calculable without homepage paid-vs-organic session share.

### 8. Surface Per-Card Review Counts on the Collection Page
**What's broken:** The Collection page ("Shop All," 172 products, 4-column grid) shows a star rating with numeric average on each product card, alongside BEST SELLER and SAVE % badges, but no review count. The review count (e.g., 279 for jojoba oil) only becomes visible after clicking into the individual PDP.
**Evidence:** raw/site-visual-summary.md (Collection Page — Price display)
**Key data:** Review count present on PDP fold 1, absent from all collection-grid cards.
**Est. lift:** Not calculable without collection-to-PDP click-through baseline.

### 9. Test the Subscribe & Save Default on the PDP Buy Box
**What's broken:** On both jojoba oil ad-landing states (Ad 1's 4oz/24%-off default, Ad 3's 16oz/15%-off default), the Subscribe & Save option is pre-selected over one-time purchase in the buy box, with no visual distinction calling out that a recurring subscription is the default choice rather than a one-time purchase.
**Evidence:** raw/meta-ads-visual-summary.md (Ad 1, Ad 3 — Landing Page Fold 1), raw/last30days-ecom.md (directional: PissedConsumer flags unwanted recurring charges, small sample, not corroborated by first-party reviews collected here)
**Key data:** Subscribe & Save pre-selected in both captured PDP states; discount tier varies by size (24% at 4oz, 15% at 16oz).
**Est. lift:** Not calculable without PDP add-to-cart baseline.

### 10. Surface the Free-Shipping Progress Bar Earlier in the Funnel
**What's broken:** The cart drawer includes a 3-tier progress bar (Free Shipping Over $40 / Free Gift Over $55 / Free Tumbler Cup Over $100) with live copy like "You are $30.13 away from FREE SHIPPING!" — a strong AOV mechanic. It only appears after a visitor has already added to cart. No equivalent element exists on the PDP itself in any of the three ad-landing folds captured.
**Evidence:** raw/site-visual-summary.md (Cart Drawer — AOV elements), raw/meta-ads-visual-summary.md (PDP folds, all 3 ads — no shipping-progress element present)
**Key data:** Progress bar exists only post-add-to-cart, not pre-add.
**Est. lift:** Not calculable without AOV data.

## Unused Findings

- Collection page shows "Filters (0)" applied by default across 172 products despite an 8-tile subcategory nav — a discovery-friction opportunity, lower priority than the items above.
- Homepage and Google ads cite review counts (500,000+, 35,000-42,000+) an order of magnitude larger than the 279 shown on the specific jojoba oil PDP, likely because they aggregate across the full catalog or Amazon storefront — worth a client-side clarification before treating these figures as interchangeable in any future test.
