# Ashley Stewart CRO Research Audit

## Data Sources Used

- Meta Ads and Landing Pages (3 ad creatives, live-page verification via WebFetch, screenshots)
- Google Ads Transparency Center (26 ad units across 2 screenshots)
- Reviews & UGC (20 reviews, Trustpilot-style pasted text)
- PageSpeed / Core Web Vitals (Lighthouse mobile, homepage + PDP)
- Current Site Screenshots (homepage, collection, PDP, cart) + live WebFetch of homepage and bridal LP

## Source Findings

### Meta Ads & Landing Pages

Three Meta campaigns are running with three different destination types, and message match quality varies sharply between them.

**Ad #1 — Crystal Face Gems (broken).** The ad promotes "Plus Size Crystal Face Gems, Small Container (Mixed Sizes)" with a static product shot and a "Shop Now" CTA. The user-reported issue is confirmed live: fetching `ashleystewart.com/products/rhinestone-face-gems-mixed-sizes` returns an HTTP 404. Anyone who clicks this ad lands on a broken page (or is redirected to the homepage, per the original Facebook-tracked link), with zero chance of finding the product they clicked for. This ad has been running since Nov 24, 2025 per its Meta Ad Library ID — meaning this gap has likely been live for months.

**Ad #2 — Berkshire Ultra Sheer Pantyhose (strong match).** Ad copy ("ultra sheer for everyday wear," "elasticized waistband," "cotton-blend gusset," "two-way stretch") matches the PDP almost verbatim. The landing PDP carries a 4.5-star rating (44 reviews), the exact color/size shown in the ad creative, and a "Hurry — Only 6 Left!" urgency badge. Buy box includes Klarna/Afterpay/Zip installment badges and a "30-Day Returns & Exchanges" trust box. This is the only one of the three ads with tight, verifiable message match.

**Ad #3 — Bridal Collection (partial match).** Ad copy is emotionally driven ("The Doors Open. Eyes Turn...") but names no specific product, so it correctly routes to a collection page rather than a PDP. Confirmed live via WebFetch: the bridal page carries a "40% Off New Arrivals," "Free Shipping $89+" promo stack, and no reviews, ratings, or press mentions are present — the "AS SEEN ON" press section noted in the screenshot did not appear in the live text fetch, suggesting it may load lower on the page or was specific to that capture. Visitors must browse further to find an actual gown; there's no single "the gown" to click through to from the ad.

### Google Ads

Google Ads run a completely different strategy from Meta: broad brand/category positioning ("plus size," "sizes 10-36," "Love Your Curves") and sitewide discount messaging (40-75% off), spread across roughly 26 ad units (text, shopping, video, and display). None of the ~26 units reference bridal or face gems — the two channels have zero visible creative overlap. This isn't inherently a problem (different channels can run different funnels), but it means there's no reinforcing message match for a visitor who sees a Google ad and a Meta ad from the same brand — the value props don't compound across channels.

### Reviews & UGC

#### What Customers Love

- Long-tenured customers recall a stronger past product line: multiple reviewers (10, 25+ years) describe once being loyal, frequent buyers who filled their closets with Ashley Stewart pieces.
- No specific "love" quotes about current products or experience appear in the 20 reviews collected — all 20 are negative (1-2 star). This is a sampling artifact of the source, not necessarily representative of the full review base, and should be flagged as such.

#### What Frustrates Customers

- **Refund and return failures, repeatedly and severely.** Multiple reviewers report waiting a month or more for refunds after returns were confirmed received ("received items on March 27th... still refusing to refund," "It is Now June 9th and not only have they not refunded me"). One reviewer alleges Ashley Stewart is "using stall tactics to keep money without fulfilling orders" post-bankruptcy.
- **Return shipping fee stacking.** One reviewer describes being charged both a $10 return-shipping deduction and a separate $9.95 shipping fee on the same return — "punishing you because you want to return something."
- **Customer service breakdowns.** Multiple reviewers describe being disconnected mid-call, denied access to a supervisor, or given contradictory information across repeated calls (one reviewer made 4 calls totaling 45+ minutes with no resolution).
- **Fulfillment errors.** Wrong items shipped (ordered a 2-piece suit, received 3 skirts and no blazer), damaged items shipped without protective packaging (hats "not in a box"), and stolen/lost packages with delayed or denied replacement.
- **Perceived decline in product quality/style** since a reported change in ownership — several reviewers use words like "frumpy," "cheesy," "generic," and contrast it with a better past product line.
- **Delivery carrier complaints** — specific dissatisfaction with a named third-party carrier (Veho) for lost/stolen packages, contrasted favorably against FedEx.

#### Client-Actionable Insights

- Refund SLA and communication process needs an operational fix — this is a support/ops issue independent of website design, but it is actively costing repeat customers and generating public complaints.
- Return shipping fee structure ($10 + $9.95 double-charge pattern described by at least one reviewer) should be audited for clarity — if intentional, it needs better upfront disclosure; if a billing error, it needs a fix.
- Damaged-goods-in-transit reports (hats shipped without a box) point to a packaging/fulfillment QA gap worth flagging to ops.

### PageSpeed / Core Web Vitals

Mobile Lighthouse runs collected 2026-09-08.

**Homepage** (`ashleystewart.com/`): Performance score 61/100. LCP 3.5s (score 0.62), TBT 790ms (score 0.37), Speed Index 8.0s (score 0.21), Time to Interactive 27.6s (score 0). CLS is a clean 0. Run flagged a possible IndexedDB storage issue affecting load performance.

**PDP** (`basiccami-041-ast-8385-cb`): Performance score 39/100 — significantly worse than the homepage. LCP 19.4s (score 0), TBT 930ms (score 0.3), Speed Index 22.8s (score 0), Time to Interactive 61.3s (score 0). Lighthouse flagged that the page loaded too slowly to finish within its time limit, so results may be incomplete — meaning real-world performance could be worse than what's captured here. CLS is low (0.005).

The PDP is the most performance-critical page in the funnel (where Meta Ad #2 sends traffic) and it is the worst-performing page measured — a near-20-second LCP is well outside acceptable range and will suppress conversion regardless of on-page CRO fixes.

### Competitor Analysis

No `raw/competitors.md` file was provided for this brand, and Competitor Insights was not selected as a source in the manifest ("Sources Skipped" lists Competitor Insights). This section is omitted per manifest scope — see Missing Data.

### Emails

Not collected — Email Campaigns was listed under "Sources Skipped" in the manifest. Omitted.

### Inspiration Sites

Not collected — Inspiration Sites was listed under "Sources Skipped" in the manifest. Omitted.

### Non-Data Context

The only non-data context captured is the user-flagged concern about Ad #1's landing page destination 404ing and redirecting to the homepage. This has been verified live during this audit (see Meta Ads section) — confirmed as a real, current defect, not a stale or resolved report.

### Current Site Screenshots

**Homepage.** Live WebFetch and screenshots agree: the page opens with three stacked promotional banners (free shipping $89+, $10+ clearance, 40% off new arrivals) before any hero or brand imagery appears, pushing the actual "Fall Edit" hero content below the fold on smaller viewports. A persistent "Get 20% off!" popup sits pinned bottom-left across all folds, partially overlapping content. No trust signals — no review count, star rating, guarantee badge, or security copy — appear anywhere across the three homepage folds captured. The page is pure promotion-stacking with no social proof.

**Collection page.** Filters (color, size, length, price range) sit in a left sidebar; product grid uses consistent strikethrough/compare-at pricing ("$74.50 → $44.70," "40% Off"). Tagging is inconsistent: some cards show "New," others "Online Exclusive," others just a discount percentage, with no legend explaining what each means — a visitor can't tell if "Online Exclusive" means something different from "40% Off" or if the two are mutually exclusive states.

**PDP.** Strong trust signals here relative to the rest of the site: 4.5-star rating and "67 Reviews" sit directly under the product title, above the price. A green "30-Day Returns & Exchanges" box and installment badges (Klarna/Afterpay/Zip) sit in the buy box. A "Ways to Wear It" carousel (fold 2) provides a genuine cross-sell mechanic with "Shop the Look" links. One layout defect: the breadcrumb reads "Home > CLOTHING > CLOTHING" — a duplicated category level. Buy box offers only single-purchase (no subscription/bundle), so no hierarchy problem there, but this is also the page measured at 39/100 PageSpeed with a 19.4s LCP — trust signals and cross-sell mechanics won't matter if the page doesn't finish loading.

**Cart.** Mobile cart page (not a drawer) with a free-shipping progress bar ("Spend $60 more to unlock free shipping") as the only AOV-driving element — no upsell, cross-sell, or bundle offer appears anywhere in the cart. CTA is a sticky bottom bar with a full-width pink "CHECKOUT" button. A "FREE RETURNS — TRY IT RISK-FREE" trust banner is visible but cut off at the top of the capture, suggesting it may not be fully visible without scrolling up.

## Cross-Source Themes

1. **PDP performance is a hard funnel blocker.** A 39/100 PageSpeed score with a 19.4s LCP on the exact page type Meta Ad #2 drives traffic to (product pages) means the highest-intent, best-message-match traffic in the account is landing on the slowest page on the site. This is evidenced by PageSpeed data directly and is the single highest-revenue-potential fix available — it affects every PDP visit, not one test variant.

2. **Trust signals are inconsistent across the funnel, and post-purchase trust is actively being broken.** The PDP has strong trust signals (ratings, reviews, returns box) but the homepage has none, and the reviews data shows the returns/refund promise ("30-Day Returns & Exchanges") is contradicted by real customer experience (refunds taking a month-plus, double-charged return shipping). This is both a site-design gap (homepage) and an operational credibility gap (reviews) pointing at the same theme from two independent sources.

3. **Message match is uneven across the paid funnel, with one outright broken ad.** Ad #2 shows what "good" looks like (near-verbatim copy match, right product, right urgency signal). Ad #1 is a confirmed dead link. Ad #3 intentionally routes to a collection page but offers no way to narrow toward "the gown" the ad talks about. Fixing message match is evidenced directly from ad creative vs. live landing page comparison across all three ads.

## Top Test Opportunities

**Fix Ad #1's broken landing page (Crystal Face Gems)** — The Meta ad has been running since Nov 24, 2025 and its destination URL returns a live HTTP 404, confirmed via direct fetch during this audit. Every click on this ad is wasted spend with zero chance of conversion. Evidence: meta-ads.md, live WebFetch 404 confirmation, context.md. Est. lift: this is ad spend recovery, not a CRO lift — cannot be sized without spend data, but represents 100% of clicks on this ad currently converting at 0%.

**Reduce PDP Largest Contentful Paint** — The PDP scores 39/100 on mobile PageSpeed with a 19.4s LCP and 61.3s Time to Interactive, the worst-performing page type measured and the exact page type paid traffic (Meta Ad #2) is sent to. Evidence: pagespeed.md, pagespeed-pdp.json. Est. lift: conservative 2-4% CR lift x [sessions/mo unknown] x [AOV unknown] = requires session/AOV data to size in dollars; directionally this is the single largest measured performance gap on the site.

**Reduce homepage banner stacking above the hero** — Three stacked promotional banners (free shipping, $10 clearance, 40% off) push the actual hero content below the fold before any brand imagery renders, per both screenshot and live WebFetch review. Evidence: site-visual-summary.md, live homepage WebFetch. Est. lift: conservative 1-2% CR lift on homepage sessions x [sessions/mo unknown] x [AOV unknown] = requires traffic data to size.

**Add trust signals to the homepage** — Zero review counts, star ratings, guarantee badges, or security copy appear anywhere across three homepage folds, despite the PDP successfully using a 4.5-star/67-review badge high in the buy box. Evidence: site-visual-summary.md. Est. lift: conservative 1-3% CR lift on homepage-entry sessions x [sessions/mo unknown] x [AOV unknown] = requires traffic data to size.

**Clarify product tag legend on collection pages** — "New," "Online Exclusive," and "40% Off" tags appear inconsistently on product cards with no legend, making it unclear whether tags are mutually exclusive or additive. Evidence: site-visual-summary.md (collection page folds 1-3). Est. lift: conservative 0.5-1% CR lift on collection-page sessions x [sessions/mo unknown] x [AOV unknown] = requires traffic data to size.

**Fix duplicated breadcrumb category on PDP** — Breadcrumb reads "Home > CLOTHING > CLOTHING," a duplicated category level that reads as a bug and undermines site polish. Evidence: site-visual-summary.md (PDP fold 1). Est. lift: low-effort fix, primarily a trust/polish gain rather than a direct CR driver — not separately sizable.

**Add cross-sell/upsell to cart** — The only AOV mechanic in the cart is the free-shipping progress bar; no upsell, cross-sell, or bundle offer appears, despite the PDP already having a working "Ways to Wear It" cross-sell mechanic that could extend into the cart. Evidence: site-visual-summary.md (cart), site-visual-summary.md (PDP fold 2). Est. lift: conservative 2-4% AOV lift on cart sessions x [sessions/mo unknown] x [AOV unknown] = requires traffic/AOV data to size.

**Give Ad #3 (Bridal) a narrower landing path** — The ad's emotional copy implies a specific gown ("You Step Into An Ashley Stewart Bridal Gown"), but it lands on a full collection page with no single hero product, requiring visitors to browse further to find what the ad promised. Evidence: meta-ads-visual-summary.md (Ad 3), live WebFetch of bridal page. Est. lift: conservative 1-3% CR lift on bridal-ad sessions x [sessions/mo unknown] x [AOV unknown] = requires ad-level traffic data to size.

**Address return/refund communication on-site** — Reviews reveal a consistent pattern of refund delays (1+ month) and disputed return shipping fees despite the site's "30-Day Returns & Exchanges" trust badge. While this is primarily an ops fix (see Client-Actionable Insights), a testable on-site component exists: proactively surfacing refund-timeline expectations near the returns badge to reduce post-purchase anxiety and support-contact volume. Evidence: reviews.md (7+ reviews referencing refund/return issues). Est. lift: not directly a CR lift test — more a support-cost and repeat-purchase retention play; flagged for client awareness alongside the testable component.

## Unused but Valuable Findings

- Google Ads and Meta Ads run entirely non-overlapping creative concepts (broad category/discount vs. single-SKU/collection) — not itself a test opportunity, but worth flagging to the client as a cross-channel strategy gap.
- Multiple reviewers explicitly attribute quality/style decline to a reported change in company ownership — useful qualitative context for any messaging or merchandising conversations, but not a CRO test.

## Missing Data

- **Sessions/mo and AOV are unknown** for this brand — no analytics or order data was collected. Every dollar-estimate in this audit is directional only; all Top Test Opportunities need real traffic/AOV numbers to size accurately.
- **Competitor Insights, Inspiration Sites, and Email Campaigns** were explicitly skipped per the manifest — no findings exist for these areas.
- **Ad #1 landing page screenshots** could not be collected because the destination doesn't resolve to a real page (confirmed 404 via live fetch during this audit).
- **Review sample skew:** all 20 reviews collected are negative (1-2 star). This may reflect a genuine trust/ops problem, or may be a collection artifact (e.g., a review source sorted by "most recent" during a bad operational stretch, or a source that surfaces complaints preferentially). Treat the "What Customers Love" section as thin for this reason.
