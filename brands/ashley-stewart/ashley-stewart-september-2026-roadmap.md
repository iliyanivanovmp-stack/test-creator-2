# Ashley Stewart CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, Reviews & UGC

## Insights

The PDP is the highest-intent page in the paid funnel and the worst-performing page on the site. Meta Ad #2 (Berkshire Ultra Sheer Pantyhose) sends its best-matched traffic straight to a product page that scores 39/100 on mobile PageSpeed, with a 19.4s Largest Contentful Paint and a 61.3s Time to Interactive — Source: PageSpeed / Core Web Vitals, Sep 2026. Lighthouse flagged that the page loaded too slowly to even finish measuring within its time limit, meaning real-world performance may be worse. Every dollar spent sending traffic to a PDP is fighting a near-20-second load before a shopper sees the buy box.

Trust is strong where it's proven and missing where it's needed most. The PDP carries a 4.5-star, 67-review badge high in the buy box plus a "30-Day Returns & Exchanges" box — Source: Current Site Screenshots. The homepage has none of that: no rating, no review count, no guarantee copy, across all three folds captured — Source: Current Site Screenshots. That gap matters more given what the reviews show: 7+ of 20 collected reviews (all 1-2 star) describe refund delays exceeding a month and one describes being double-charged on return shipping ($10 + $9.95 on a single return) — Source: Reviews & UGC. The site's own return promise is being contradicted in public.

Message match across the paid funnel is uneven, and one ad is dead. Ad #1 ("Plus Size Crystal Face Gems," running since Nov 24, 2025) points to a product URL that returns a live HTTP 404, confirmed by direct fetch during the audit — Source: Meta Ads and Landing Pages. Ad #2 shows what strong match looks like: copy, image, and PDP align almost verbatim. Ad #3 (Bridal, running since Jul 22, 2025) uses emotional, specific copy but lands on a generic collection page carrying the same sitewide promo banners as the homepage, with no single gown to click through to — Source: Meta Ads and Landing Pages.

Sessions/mo and AOV were not collected for this brand, so none of the estimates below can be converted to a dollar figure yet. Every lift range is directional, based on the evidence cited, and should be resized once traffic and AOV data are available.

## Slot 1: Fix Ad #1's Broken Landing Page (Crystal Face Gems)

**Type:** Immediate Fix
**Page:** Meta ad landing page (ashleystewart.com/products/rhinestone-face-gems-mixed-sizes)

**What's broken:** The Meta ad "Plus Size Crystal Face Gems, Small Container (Mixed Sizes)" has run since Nov 24, 2025 and points to a product URL that returns a live HTTP 404. There is no page to land on. This isn't a design problem, it's a dead link that has been live for months.

**Fix:** Either restore the product at that URL or repoint the ad to the correct live product page. No A/B test needed, this is broken regardless of who sees it.

**Why this matters:** 100% of clicks on this ad currently convert at 0%. Fixing the link recovers the full value of existing spend on this creative. Source: Meta Ads and Landing Pages, live WebFetch 404 confirmation.

## Slot 2: Fix PDP Load Performance

**Type:** Immediate Fix
**Page:** Product Detail Page (tested on basiccami-041-ast-8385-cb)

**What's broken:** The PDP scores 39/100 on mobile Lighthouse, with a 19.4s LCP, 930ms Total Blocking Time, and 61.3s Time to Interactive. Lighthouse flagged that the page loaded too slowly to complete measurement within its time limit, so real-world numbers may be worse. This is the exact page type Meta Ad #2's best-matched traffic lands on. The buy box itself (image, rating, price, size grid, Add to Cart) is well-built, Source: Current Site Screenshots — the problem is load time, not layout.

**Fix:** Diagnose and resolve the render-blocking cause of the 19.4s LCP (script/asset loading order, third-party tags, image weight) before running any PDP copy or layout tests. A test built on top of a page that takes 20 seconds to render will underperform regardless of what it says.

**Why this matters:** This is the largest measured performance gap on the site and it sits on the page type carrying the best-matched paid traffic. No PDP-level CRO test can outperform a 61.3s Time to Interactive. Source: PageSpeed / Core Web Vitals.

## Slot 3: Collapse Homepage Promo Banners Above the Hero

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (ashleystewart.com)
**Revenue potential:** Sessions/mo and AOV are not available for this brand. Directional estimate: conservative 1-2% CR lift on homepage-entry sessions. Dollar impact cannot be calculated until traffic and AOV data are provided.

**Hypothesis:** If we collapse the three stacked promo banners (free shipping, clearance, 40% off) into one combined bar, more shoppers will scroll into and engage with hero and brand content because the page reaches its point faster.

**Data:** Three full-width promotional banners stack vertically before any hero or brand imagery appears, pushing the "Fall Edit" hero below the fold on smaller viewports. A persistent "Get 20% off!" popup is also pinned bottom-left across all three captured folds, partially overlapping content. Source: Current Site Screenshots, live homepage WebFetch.

**V1:** Combine the three banners into a single rotating top bar (one line, auto-cycling between the free shipping, clearance, and new-collection messages) so only one banner height sits above the hero instead of three. The "Get 20% off!" popup stays as-is, this test does not touch it. Mobile: single-line bar directly above the hero image, hero visible without scrolling past three separate banners. Desktop: same single combined bar, hero moves up by the height of the two removed banners.

## Slot 4: Add Trust Signals to the Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (ashleystewart.com)
**Revenue potential:** Sessions/mo and AOV are not available for this brand. Directional estimate: conservative 1-3% CR lift on homepage-entry sessions. Dollar impact cannot be calculated until traffic and AOV data are provided.

**Hypothesis:** If we add a trust-badge row near the hero using the same "30-Day Returns & Exchanges" and installment-payment badges already proven on the PDP, homepage visitors will convert to browse/PDP at a higher rate because the returns promise and payment flexibility are visible before they've clicked into a product.

**Data:** Across all three captured homepage folds, there is no review count, star rating, guarantee badge, or trust copy anywhere on the page, only promotional banners and the discount popup. The PDP, by contrast, places a 4.5-star/67-review badge directly under the product title and a green "30-Day Returns & Exchanges" box with Klarna/Afterpay/Zip badges in the buy box. Source: Current Site Screenshots (Homepage folds 1-3, PDP fold 1).

**V1:** Add a slim trust-badge row directly beneath the hero, reusing the exact "30-Day Returns & Exchanges" copy and Klarna/Afterpay/Zip installment badges already used on the PDP. No new claims are introduced, only elements already live elsewhere on the site. Mobile: single row of 3 badges (Returns, Klarna, Afterpay/Zip) below the hero, horizontally scrollable if needed. Desktop: same 3 badges in a single static row, no scroll needed.

## Slot 5: Add a Tag Legend to Collection Pages

**Type:** A/B test (1 variation vs. control)
**Page:** Collection / Category page (e.g. "New Arrivals")
**Revenue potential:** Sessions/mo and AOV are not available for this brand. Directional estimate: conservative 0.5-1% CR lift on collection-page sessions. Dollar impact cannot be calculated until traffic and AOV data are provided.

**Hypothesis:** If we add a one-line legend explaining what each product-card tag means, shoppers will filter and click through with more confidence because they'll understand whether "New," "Online Exclusive," and "% Off" are separate or overlapping states.

**Data:** On the "New Arrivals" collection page, product cards carry inconsistent combinations of a black "New" pill, an "Online Exclusive" label, and a pink "% Off" strikethrough price, with no legend anywhere explaining what each means or whether they stack. At least 3 distinct tag types appear across the 3 captured folds. Source: Current Site Screenshots (Collection Page folds 1-3).

**V1:** Add a single-line legend key directly beneath the collection page header: "New = just added · Online Exclusive = web only · % Off = discount applied." No changes to the tags themselves or filter sidebar. Mobile: legend sits as one wrapping line below the page title, above the product grid. Desktop: same legend, single line, no wrap needed at that width.

## Slot 6: Add Cross-Sell to Cart

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (ashleystewart.com/cart)
**Revenue potential:** Sessions/mo and AOV are not available for this brand. Directional estimate: conservative 2-4% AOV lift on cart sessions. Dollar impact cannot be calculated until traffic and AOV data are provided.

**Hypothesis:** If we extend the PDP's existing "Ways to Wear It" cross-sell carousel into the cart, average order value will increase because shoppers see a proven styling mechanic at the exact moment they're deciding whether to add more before checking out.

**Data:** The cart currently shows one line-item card and an order summary box, with the only AOV mechanic being a free-shipping progress bar ("Spend $60.00 more to unlock free shipping"). No cross-sell or bundle offer appears anywhere in the cart, despite the PDP already running a working cross-sell carousel, "Ways to Wear It," with "Shop the Look" links on fold 2. Source: Current Site Screenshots (Cart, PDP fold 2).

**V1:** Add a "Complete the Look" carousel to the cart page, directly below the line-item card and above the order summary, using the same card format and "Shop the Look" mechanic already live on the PDP. The free-shipping progress bar stays in place unchanged. Mobile: horizontally scrollable carousel of 2-3 items below the cart line item. Desktop: same carousel, 3 items visible without scrolling, positioned in the same spot relative to the order summary.

## Slot 7: Give Ad #3 (Bridal) a Product-Led Landing Path

**Type:** A/B test (1 variation vs. control)
**Page:** Bridal landing page (ashleystewart.com/pages/bridal)
**Revenue potential:** Sessions/mo and AOV are not available for this brand. Directional estimate: conservative 1-3% CR lift on bridal-ad sessions. Dollar impact cannot be calculated until traffic and AOV data are provided.

**Hypothesis:** If we replace the generic sitewide promo banners at the top of the bridal page with a curated gown showcase that echoes the ad's language, visitors from Ad #3 will convert at a higher rate because the page immediately delivers what the ad promised instead of asking them to browse a generic category first.

**Data:** Ad #3's copy is specific and emotional ("You Step Into An Ashley Stewart Bridal Gown... Say Yes To The Dress At Ashley Stewart"), implying a specific product moment, but it lands on a full collection page. A live fetch during the audit confirmed the page opens with the same "40% Off New Arrivals / $10+ Almost Gone Clearance / Free Shipping $89+" promo stack used on the homepage, with no bridal-specific content, reviews, or press mentions in the fetched text. Source: Meta Ads and Landing Pages, live WebFetch of the bridal page.

**V1:** Replace the generic promo-banner stack at the top of the bridal page with a curated gown grid (3-4 featured gowns) topped by a headline echoing the ad's copy ("Say Yes To The Dress"). The generic sitewide banners move below this section instead of leading the page. Mobile: single-column gown grid with headline above, scroll to reach the moved promo banners. Desktop: 3-4 gowns in a row beneath the headline, same relocation of the generic banners below.

## Slot 8: Fix Duplicated PDP Breadcrumb

**Type:** Immediate Fix
**Page:** Product Detail Page (all products)

**What's broken:** The PDP breadcrumb reads "Home > CLOTHING > CLOTHING," the same category level repeated in sequence. Confirmed on the "Basic Knit Cami Top" PDP. Source: Current Site Screenshots (PDP fold 1).

**Fix:** Correct the breadcrumb template so each category level appears once.

**Why this matters:** This is a visible template bug on the page carrying the site's strongest trust signals (rating, reviews, returns badge). It's low-effort to fix and removes a defect that undercuts the polish those trust signals are meant to build.

## Future Slot Candidates

1. **Address return/refund communication on-site** - Reviews show a repeated pattern of refund delays over a month and disputed double-charged return shipping, directly contradicting the site's "30-Day Returns & Exchanges" badge. Primarily an ops fix, but a testable on-site component exists: surfacing refund-timeline expectations near the returns badge to reduce post-purchase anxiety. Source: Reviews & UGC (7+ of 20 reviews).
2. **Cross-channel message alignment between Meta and Google Ads** - Google Ads runs broad category/discount messaging across ~26 units while Meta runs single-SKU/collection creative, with zero overlap between the two. Not independently testable as a CRO mechanic, but worth resizing once ad-level performance data is available. Source: Meta Ads and Landing Pages, Google Ads Transparency.
