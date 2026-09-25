# Kill Crew Roadmap Seed

**Store:** killcrew.co
**AOV:** unknown
**Monthly sessions:** unknown (third-party estimate only: ~196.6K monthly visits as of July 2026, unverified)
**Data sources:** Meta Ads Library, Google Ads Transparency, on-site reviews, PageSpeed API (mobile, homepage + PDP), site screenshots (homepage, collection, cart), live WebFetch of homepage and two ad landing pages, WebSearch competitor research, last30days-ecom social/community research

## Key Insights

Two of Kill Crew's three active Meta ads (Ads 1 and 2) advertise a specific reptile-print shorts set but both route to the same broad reptile-shorts collection page — a 34-item mixed grid of shorts and t-shirts with no visible bridge to the advertised product and no trust signals in the first three folds. Ad 3 has the strongest message match in the set (its PDP copy echoes the ad's squat-proof/chafe-proof language nearly verbatim), but a live re-check on 2026-09-11 found that exact PDP is now out of stock, meaning the best-matched ad may currently be sending paid clicks to a page with no purchase path.

Site speed compounds the problem on the same templates ads route to. Mobile PageSpeed shows homepage LCP at 6.4s and PDP LCP at 8.0s — both far past Google's "poor" threshold (4s+) — with the homepage Lighthouse run flagged incomplete ("page loaded too slowly to finish within the time limit"). PDP also carries a CLS of 0.144, bordering "needs improvement."

Trust signals are inconsistently placed: the PDP shows a 4.8★/2,437-review count twice plus a 6-icon trust bar, but that proof point disappears entirely on the homepage (which leans on a round "500,000 orders" claim instead) and in the cart drawer — the last screen before checkout. Meanwhile, Trustpilot shows a 2.3 TrustScore (6 reviews) with specific complaints (unexplained refund deduction, wrong item shipped, unmet expedited shipping, one "see-through when squatting" report) that stand in direct tension with the squat-proof claim used in ads, PDP copy, and most TikTok UGC. This is a real, evidenced conflict, not noise — two independent TikTok reviewers corroborate squat-proof/non-see-through performance, but at least one Trustpilot report contradicts it.

## Top Test Opportunities

### 1. Fix or redirect Ad 3's out-of-stock PDP
**What's broken:** Ad 3 promotes "Mid Thigh Cut Shorts" (floral-black colorway) and routes to https://killcrew.co/collections/shorts/products/muay-thai-shorts-mid-thigh-cut-floral-black-1. Live re-fetch on 2026-09-11 shows this exact product is out of stock, displaying a full-width "Notify me when available" button in place of "Add to Cart," alongside a "3,456 people are currently viewing this product" urgency banner and an "on sale" price flag. Any paid click landing here today has no purchase path.
**Evidence:** Live WebFetch of the PDP (2026-09-11), meta-ads-visual-summary.md Ad 3 section.
**Key data:** Ad 3 is otherwise the strongest message-match ad in the set (headline claims and PDP description language align nearly verbatim).
**Est. lift:** Not modelable without live spend/session data — flag as urgent operational fix.

### 2. Bridge message match on the reptile-shorts collection page (Ads 1 & 2)
**What's broken:** The collection page at killcrew.co/collections/reptile-shorts opens with a top promo bar ("Free Shipping $75+"), full nav, and a left sidebar filter panel (Sort By, Price, Type, Color), followed immediately by a product grid mixing shorts and t-shirts in assorted colors and prints — snake-print shorts, a brown tee, more snake shorts, a black tee — with no banner, header, or visual anchor connecting to the specific product shown in either ad. No review count, star rating, or guarantee appears anywhere in the first three folds.
**Evidence:** meta-ads-visual-summary.md (Ads 1 & 2 landing folds), live WebFetch confirming current grid contents, meta-ads.md (shared URL for both ads).
**Key data:** 2 of 3 active Meta ads (67% of Meta ad spend by unit count) point to this page.
**Est. lift:** Not sized — no sessions/AOV data collected this cycle.

### 3. Reduce PDP load time (8.0s LCP)
**What's broken:** The PDP template — the same template Ad 3 lands on — scores 63/100 on mobile Lighthouse performance, with Largest Contentful Paint at 8.0 seconds against a 2.5s "good" benchmark, plus a CLS of 0.144.
**Evidence:** killcrew-pdp-pagespeed.json.
**Key data:** LCP 8.0s (score 0.03/1), CLS 0.144 (score 0.78/1), Time to Interactive 12.7s.
**Est. lift:** Not sized — no sessions/AOV data collected this cycle.

### 4. Reduce homepage load time and resolve incomplete Lighthouse run
**What's broken:** Homepage scores 58/100 on mobile Lighthouse, LCP 6.4s, and the run itself carries a warning that the page loaded too slowly to complete measurement within the time limit — a severity signal beyond the raw score.
**Evidence:** homepage-pagespeed-killcrew.json (runWarnings field).
**Key data:** LCP 6.4s (score 0.09/1), Time to Interactive 12.4s, Speed Index 4.8s.
**Est. lift:** Not sized — no sessions/AOV data collected this cycle.

### 5. Add persistent navigation/CTA below the homepage hero
**What's broken:** The homepage nav bar and both primary CTAs ("SHOP MENS," "SHOP WOMENS") live only in fold 1, directly under the "KILL CREW" wordmark and hero image. The nav scrolls fully out of view by fold 2 and does not reappear in fold 3 — once a visitor scrolls into the Featured Products or Shop by Category sections, there is no sticky header, sticky CTA bar, or persistent way to navigate or purchase without scrolling back to the top.
**Evidence:** site-visual-summary.md (Homepage, "CTA behavior" note, folds 1-3).
**Key data:** No sticky element present in any of the 3 captured homepage folds.
**Est. lift:** Not sized — no sessions/AOV data collected this cycle.

### 6. Surface star rating/review count in the cart drawer
**What's broken:** The cart drawer is a right-side slide-in panel: "KILL CREW" header with close button, a free-shipping progress bar ("$25.00 away from free shipping"), the cart line item (product, size, quantity stepper, price, remove icon), a "Check These Out!" 3-product upsell row, a full-width black "Checkout · $[total]" button, and a 4-icon trust row (Ships from USA, Ships within 24 Hours, Free Returns & Exchanges, Support Suicide Prevention) at the very bottom. No star rating or review count appears anywhere in the drawer, despite the PDP showing 4.8★/2,437 reviews twice.
**Evidence:** site-visual-summary.md (Cart Drawer section).
**Key data:** PDP repeats 4.8★/2,437-review proof twice; cart drawer shows it zero times.
**Est. lift:** Not sized — no sessions/AOV data collected this cycle.

### 7. Address the squat-proof claim/complaint conflict
**What's broken:** The core performance claim ("squat proof, chafe proof, non sheer") appears in Ad 3's landing PDP copy and is corroborated independently by two TikTok UGC reviewers. A Trustpilot review describes the product as "see-through when squatting," directly contradicting that claim. This sits alongside a 2.3 Trustpilot TrustScore (6 reviews) that is a marked outlier against the on-site review widget (4.8+) and other third-party scores (Junip 4.81/9,454 reviews, Knoji 4.2/58).
**Evidence:** last30days-ecom.md (Trustpilot section), meta-ads-visual-summary.md (Ad 3 description), reviews.md.
**Key data:** 1 direct contradiction found against 2+ corroborating UGC sources and the on-site review base.
**Est. lift:** Not a standard A/B test — recommend as a client-facing quality/QA flag, potentially paired with PDP fit guidance if the client confirms a batch-specific cause.

### 8. Flag Trustpilot fulfillment/refund complaints for operational review
**What's broken:** Specific, named complaints on Trustpilot include a $40 return refunded at $15.15 after an unexplained $24.85 deduction, a wrong item shipped (plain hoodie instead of the cowprint ordered) with no offered free return, and a paid 2-4 day expedited shipping upgrade that was instead estimated at 8-9 days with unanswered emails.
**Evidence:** last30days-ecom.md (Trustpilot section).
**Key data:** 3 distinct complaint types documented from the same 6-review Trustpilot profile driving the 2.3 TrustScore.
**Est. lift:** Not applicable — operational/client-facing recommendation, not a CRO test.

## Unused Findings

- Google Ads use a "4.9 ★★★★★ (10)" / "10,000+ verified reviews at 5 stars" claim that doesn't appear on the homepage or in any Meta ad creative — a message-match/consistency candidate for a future slot.
- No sale badges or compare-at pricing appear anywhere across the collection page or Ad 1/2 landing page (6 folds observed) — a potential AOV/urgency lever not currently in the slot list.
