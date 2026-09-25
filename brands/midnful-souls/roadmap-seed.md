# Mindful Souls Roadmap Seed

**Store:** https://mindfulsouls.com/
**AOV:** Unknown (subscription entry $25.99-$39.97; talisman PDP $39.97)
**Monthly sessions:** Unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency Center, PageSpeed/Core Web Vitals, Current Site Screenshots, live site fetch, competitor research (self-researched)

## Key Insights

Trust metrics disagree across every surface: homepage shows "12k+ reviews" and "500k+ Happy Customers," the trust strip claims "2M+ Boxes Delivered," Meta landing pages cite "13,000 reviews," the collection page cites "3k+ Trustpilot reviews / 11,388 happy customers," and the Google ad snippet shows "3.9 ★ (966)." No two surfaces agree, and all are shown with equal visual weight.

Ad-to-landing-page message match breaks down on Ad 2: the ad promises "Code applied automatically. No code. No fuss," but the landing page requires manually entering code MYBOX35 in a dashed callout box, and the main CTA button displays the full $39.97 price rather than the discounted $25.99. Five discount codes are simultaneously live across Google and Meta (LABOR35, SPRING35, MYBOX35, an unlabeled 35% code, a 50% OFF banner).

Performance is a critical, isolated failure on the exact page Meta Ad 3 sends paid traffic to: the Magnetic Energy Talisman PDP scores 0.13 Performance (Lighthouse mobile), with LCP 13.3s, CLS 0.897, and TTI 48.3s, versus a moderate 0.63 Performance on the homepage.

## Top Test Opportunities

### 1. Fix PDP Core Web Vitals on the Ad 3 landing page
**What's broken:** The Magnetic Energy Talisman product page (mindfulsouls.com/products/magical-energy-talisman), the direct click destination for Meta Ad 3's paid traffic, loads with a Lighthouse mobile Performance score of 0.13. Largest Contentful Paint is 13.3s, Cumulative Layout Shift is 0.897 (severe visual jumping as images/price/buy-box load), Total Blocking Time 730ms, and Time to Interactive 48.3s, meaning the buy box and CTA are effectively unusable for most of the load window on mobile.
**Evidence:** raw/pagespeed.md, meta-ads-visual-summary.md
**Key data:** Performance 0.13, LCP 13.3s, CLS 0.897, TTI 48.3s (mobile, fetched 2026-09-01)
**Est. lift:** Not calculable without sessions/mo and AOV; flag as highest priority given direct paid-traffic exposure.

### 2. Make Ad 2's discount automatic or rewrite the ad
**What's broken:** Ad 2's headline reads "Code applied automatically. No code. No fuss." Its landing page hero shows a green "ADD TO CART — $39.97" button at full price, with the actual discount buried below in a separate dashed-border box reading "Use code at checkout & get your 1st Box for only $25.99! [MYBOX35]," requiring the shopper to notice, copy, and manually apply a code the ad said wouldn't exist.
**Evidence:** meta-ads-visual-summary.md (Ad 2, LP Fold 1)
**Key data:** Ad copy vs. LP CTA price direct contradiction ($25.99 promised, $39.97 shown)
**Est. lift:** Not calculable; message-match fixes on paid landing pages typically recover meaningful bounced-click conversion.

### 3. Unify the trust-metric number shown site-wide
**What's broken:** Homepage hero shows "4.9 (12k+ reviews)," the trust strip below it shows "2M+ Boxes Delivered," a section further down shows "Trusted by 500k+ Happy Customers," the collection page's Trustpilot badge shows "3k+ reviews... by 11,388 happy customers," and Meta landing pages show "Rated 4.9/5 | 13,000 reviews." Each number is presented with the same visual prominence, so no single figure reads as authoritative.
**Evidence:** site-visual-summary.md (homepage, collection), meta-ads-visual-summary.md (all 3 LPs)
**Key data:** 5+ distinct trust numbers across 4 surfaces
**Est. lift:** Not calculable without a baseline; four-source evidence strength makes this a top-priority theme.

### 4. Consolidate the live discount code stack
**What's broken:** LABOR35 (homepage announcement bar, repeated 3x in fold 1), SPRING35 and MYBOX35 (Meta LPs), plus an unlabeled 35% code and a separate "50% OFF + FREE GIFT" banner (Google Ads) are all live at once, none reconciling to one clear offer a shopper can trust across channels.
**Evidence:** google-ads-visual-summary.md, meta-ads-visual-summary.md, site-visual-summary.md
**Key data:** 5 distinct codes/offers identified across Google, Meta, and site
**Est. lift:** Not calculable; recommend as ops/strategy fix alongside CRO test.

### 5. Add guarantee and trust copy to the cart drawer
**What's broken:** The right-side slide-out cart drawer shows a free-shipping/free-gift progress bar, a quantity stepper, a "You May Also Like" carousel, and one line of text: "Have a discount code? Add it at checkout." No guarantee badge, no returns copy, and no shipping-time reassurance appear before the full-width green "SECURE CHECKOUT" button, despite the homepage and Meta LPs both featuring a 30-day money-back guarantee prominently.
**Evidence:** site-visual-summary.md (Cart Drawer)
**Key data:** Zero guarantee/trust copy in cart drawer vs. prominent guarantee elsewhere
**Est. lift:** Not calculable; cart-stage guarantee reinforcement commonly lifts checkout-initiation modestly.

### 6. Strengthen trust signals on talisman-style PDP/landing pages
**What's broken:** Ad 3's landing page (the talisman PDP) shows one customer review card ("Sidney L.," 5 stars) and a Trustpilot "Excellent" badge in its first two folds, no review count, no guarantee copy, and no repeated shipping-threshold badge near the CTA, a visibly thinner trust stack than the subscription-box LPs' review counts, 4-icon trust strips, and sticky CTA bars.
**Evidence:** meta-ads-visual-summary.md (Ad 3 folds, contrasted with Ad 1/Ad 2)
**Key data:** 1 review shown vs. 13,000-review claims on subscription LPs
**Est. lift:** Not calculable; second priority behind the CWV fix on the same page.

### 7. Reconcile Google's broad SKU catalog with matching landing pages
**What's broken:** Google Ads promote individual jewelry and crystal SKUs (rings, phone cases, water bottles, pendulums, incense) across 5 regional entities, none represented in the Meta creative set or landing pages collected, so this traffic's landing experience is unverified.
**Evidence:** google-ads-visual-summary.md
**Key data:** 25+ Google ad units across formats vs. 3 Meta creatives collected
**Est. lift:** Not calculable from data collected; flag for a Google-specific landing-page data pass.

### 8. Standardize review-count display so low-sample SKUs don't borrow high-sample authority
**What's broken:** On the collection page product grid, every card shows identical 5-star iconography regardless of review count, e.g. a product with 12 reviews (The Manifestation Guidebook) renders visually the same as one with 886 (Magnetic Energy Talisman).
**Evidence:** site-visual-summary.md (Collection Fold 2)
**Key data:** Review counts range 12-886 across the grid, same icon treatment
**Est. lift:** Not calculable; single-source evidence, lower priority.

## Unused Findings

- Live PDP fetch shows a "Buy 1 Get 1 50% OFF" bundle option not visible in the screenshotted folds, suggesting undocumented buy-box structure worth a dedicated PDP screenshot pass.
- Google's ad snippet shows 3.9/966, well below the 4.9/12k-13k figures elsewhere; may be a stale Google Business/Merchant listing rather than a page-level fix, worth a client conversation before scoping as a test.
