# Ashley Stewart Roadmap Seed

**Store:** https://www.ashleystewart.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, Reviews & UGC

## Key Insights

The PDP is both the highest-intent destination in the paid funnel and the worst-performing page measured. Meta Ad #2 (Berkshire Ultra Sheer Pantyhose) sends traffic to a PDP with near-verbatim message match, urgency messaging, and strong trust signals — but that same PDP template scores 39/100 on mobile PageSpeed with a 19.4s LCP and 61.3s Time to Interactive (Lighthouse flagged the page loaded too slowly to finish within its time limit, so real-world numbers may be worse). Every dollar spent driving traffic to a PDP is fighting a nearly 20-second load time before a visitor even sees the buy box.

Trust is inconsistent across the funnel and actively undermined post-purchase. The homepage shows zero trust signals (no ratings, reviews, or guarantee copy) across all three captured folds, while the PDP successfully uses a 4.5-star/67-review badge high in the buy box. Meanwhile reviews.md (20 reviews, all negative) shows a repeated pattern of refund delays exceeding a month and disputed double-charged return shipping ($10 + $9.95 on one return) — directly contradicting the site's own "30-Day Returns & Exchanges" trust badge.

Message match across the paid funnel is uneven, with one ad outright broken. Ad #1 ("Plus Size Crystal Face Gems") has been running since Nov 24, 2025 and its destination confirmed returns a live HTTP 404 (verified via direct fetch during this audit) — meaning months of spend on this ad have converted at 0%. Ad #2 shows what strong match looks like: copy, image, and PDP align almost verbatim. Ad #3 (Bridal) uses emotional copy implying a specific gown but lands on a full collection page with no single hero product to click through to.

## Top Test Opportunities

### 1. Fix Ad #1's broken landing page (Crystal Face Gems)
**What's broken:** The Meta ad "Plus Size Crystal Face Gems, Small Container (Mixed Sizes)" (Ad Library ID 2286431911877672, running since Nov 24, 2025) links to `ashleystewart.com/products/rhinestone-face-gems-mixed-sizes`. Fetching this URL live during this audit returned an HTTP 404 — no product page, no redirect target that resolves to the advertised item. The user's original report was that it 404s and then auto-redirects to the homepage; the live fetch confirms the underlying 404 is real and current. There is no landing page to describe visually because none exists — this is a dead link, not a design problem.
**Evidence:** raw/meta-ads.md, raw/meta-ads-visual-summary.md (Ad 1), raw/context.md, live WebFetch 404 confirmation during this audit.
**Key data:** Ad has run since Nov 24, 2025 — months of continuous spend against a non-resolving destination.
**Est. lift:** Cannot size in dollars without ad spend/click data. Directionally: 100% of clicks on this ad currently convert at 0%; fixing the link recovers the full value of existing spend on this creative.

### 2. Reduce PDP Largest Contentful Paint
**What's broken:** The PDP template (tested on `basiccami-041-ast-8385-cb`) scores 39/100 on mobile Lighthouse. LCP is 19.4 seconds (score 0), Total Blocking Time is 930ms, Speed Index is 22.8 seconds, and Time to Interactive is 61.3 seconds. Lighthouse flagged that the page loaded too slowly to finish within its time limit, meaning results may understate real-world severity. This is the exact page type Meta Ad #2 (pantyhose) sends its best-matched traffic to. The buy box itself (product image, 4.5-star rating, price, size grid, Add to Cart) is well-constructed per the site screenshots — the problem is entirely load performance, not layout.
**Evidence:** raw/pagespeed.md, raw/pagespeed-pdp.json.
**Key data:** PDP score 39/100 vs. homepage 61/100; PDP LCP 19.4s vs. homepage LCP 3.5s.
**Est. lift:** Conservative 2-4% CR lift x [sessions/mo unknown] x [AOV unknown] = requires session/AOV data to size in dollars. This is the single largest measured performance gap on the site and affects all PDP traffic, not one test variant.

### 3. Reduce homepage banner stacking above the hero
**What's broken:** On the homepage, three full-width promotional banners stack vertically before any hero or brand imagery appears: a black "FREE SHIPPING on orders $89+" bar with a truck icon, then a pink "$10+ almost gone clearance!" bar with a "SHOP NOW" button, then finally the "Fall Edit" hero image (two models in denim shirtdresses with a "SHOP NEW COLLECTION" button). On smaller viewports this pushes all brand/hero content below the fold. A persistent "Get 20% off!" popup is pinned bottom-left across all three captured folds, partially overlapping page content throughout.
**Evidence:** raw/site-visual-summary.md (Homepage fold 1), live homepage WebFetch confirming the same banner stack.
**Key data:** 3 stacked promotional banners before hero content in every capture; popup persists across all 3 folds.
**Est. lift:** Conservative 1-2% CR lift x [sessions/mo unknown] x [AOV unknown] = requires session/AOV data to size.

### 4. Add trust signals to the homepage
**What's broken:** Across all three captured homepage folds, there is no review count, star rating, guarantee badge, or security/trust copy anywhere on the page — only promotional/discount banners and the "Get 20% off!" popup. This is in direct contrast to the PDP, which places a 4.5-star rating and "67 Reviews" link directly under the product title, above the price, in a proven high-visibility position.
**Evidence:** raw/site-visual-summary.md (Homepage folds 1-3), raw/site-visual-summary.md (PDP fold 1, for contrast).
**Key data:** 0 trust elements across 3 homepage folds vs. rating+review badge present and prominent on PDP.
**Est. lift:** Conservative 1-3% CR lift on homepage-entry sessions x [sessions/mo unknown] x [AOV unknown] = requires session/AOV data to size.

### 5. Clarify product tag legend on collection pages
**What's broken:** On the "NEW ARRIVALS" collection page, product cards carry inconsistent combinations of a black "New" pill tag (top-left of image), an "Online Exclusive" text label, and a "40% Off" pink strikethrough-price label. Some cards show both "New" and "40% Off," others show "Online Exclusive" instead of a discount percentage, with no legend anywhere on the page explaining what each tag means or whether they're mutually exclusive.
**Evidence:** raw/site-visual-summary.md (Collection Page folds 1-3).
**Key data:** At least 3 distinct tag types observed across product cards in 3 folds with no explanatory legend.
**Est. lift:** Conservative 0.5-1% CR lift on collection-page sessions x [sessions/mo unknown] x [AOV unknown] = requires session/AOV data to size.

### 6. Add cross-sell/upsell to cart
**What's broken:** The mobile cart page shows a single line-item card (product image, name, variant, strikethrough price, quantity stepper) and an "ORDER SUMMARY" box with subtotal/shipping/tax/total. The only AOV-driving element present is a free-shipping progress bar ("Spend $60.00 more to unlock — FREE shipping"). No upsell, cross-sell, or bundle offer appears anywhere in the cart, despite the PDP already having a proven cross-sell mechanic — "WAYS TO WEAR IT," a styled outfit-pairing carousel with "SHOP THE LOOK" buttons — that isn't extended into the cart experience.
**Evidence:** raw/site-visual-summary.md (Cart), raw/site-visual-summary.md (PDP fold 2, for the existing cross-sell mechanic).
**Key data:** 1 AOV mechanic (shipping threshold) present in cart; 0 product cross-sell/upsell elements.
**Est. lift:** Conservative 2-4% AOV lift on cart sessions x [sessions/mo unknown] x [AOV unknown] = requires session/AOV data to size.

### 7. Give Ad #3 (Bridal) a narrower landing path
**What's broken:** Ad #3's copy is specific and emotional — "You Step Into An Ashley Stewart Bridal Gown... Say Yes To The Dress At Ashley Stewart" — implying a specific product moment. It links to `ashleystewart.com/pages/bridal`, a full collection landing page. Live WebFetch confirms this page opens with a "40% Off New Arrivals" / "$10+ Almost Gone Clearance" / "Free Shipping $89+" promo stack (the same sitewide banners as the homepage) rather than bridal-specific content, and has no reviews, ratings, or press mentions in the fetched text. A visitor who clicks expecting "the gown" must browse a full category page with no single hero product to land on.
**Evidence:** raw/meta-ads-visual-summary.md (Ad 3), live WebFetch of the bridal page during this audit.
**Key data:** Ad has run since Jul 22, 2025 ("4 ads use this creative and text" per Ad Library); landing page opens with generic sitewide promo banners, not bridal-specific content.
**Est. lift:** Conservative 1-3% CR lift on bridal-ad sessions x [sessions/mo unknown] x [AOV unknown] = requires ad-level session/AOV data to size.

### 8. Fix duplicated breadcrumb category on PDP
**What's broken:** The PDP breadcrumb reads "Home > CLOTHING > CLOTHING" — the same category level appears twice in sequence. This is a low-effort fix but reads as a visible bug on a page that otherwise carries the site's strongest trust signals (rating, reviews, returns badge).
**Evidence:** raw/site-visual-summary.md (PDP fold 1).
**Key data:** Confirmed on the "Basic Knit Cami Top" PDP capture.
**Est. lift:** Not separately sizable as a CR driver — primarily a trust/polish fix that removes a visible defect from the highest-trust page on the site.

## Unused Findings

- Return/refund process shows a repeated pattern in reviews (7+ of 20 reference refund delays of a month or more, or disputed double-charged return shipping) — primarily an ops/support fix rather than a CRO test, but directly undermines the site's "30-Day Returns & Exchanges" trust badge and is worth flagging to the client.
- Google Ads and Meta Ads run entirely non-overlapping creative strategies (broad category/discount vs. single-SKU/collection focus across ~26 Google units vs. 3 Meta creatives) — a cross-channel messaging gap worth client awareness, not itself a testable CRO mechanic.
