# evo CRO Research Audit

## Data Sources Used

- Meta Ads & Landing Pages (3 ads, visual summary + live WebFetch of Ad #3's landing page — blocked, see gap note)
- Google Ads Transparency Center (2 screenshots, visual summary)
- PageSpeed / Core Web Vitals (Lighthouse JSON, homepage + PDP, fetched 2026-08-21)
- Current Site Screenshots (homepage, "Labor Day Sale" collection, cart drawer)
- Live homepage (WebFetch, 2026-08-21)
- Competitor research (WebSearch, self-researched, 2026-08-21)
- Reviews & UGC — **not collected**, see Missing Data

## Source Findings

### Meta Ads & Landing Pages

Three static-image ads, all active since Aug 13-14, 2026, all "Shop Now" CTA, all landing on evo PDPs during the sitewide Labor Day Sale.

- **Ad 1** (kids' snowboard bundle): Copy is broad ("Looking for adventure? evo is your one stop shop for ski, snowboard, bike and more") and the product image matches the landing page exactly — direct message match. The landing page buy box stacks three separate variant pickers (board size, binding color, boot size) for the three bundled components, plus quantity, in a single scrolling block. No star rating or review count is visible for this bundle SKU on fold 1 or 2, unlike Ads 2 and 3.
- **Ad 2** (Burton toe strap accessory, $14.99): Copy is a broad seasonal line ("Make your powder dreams come true with the latest skis, snowboards & more") applied to a single low-price accessory. Product image and link title match the landing page, but the ad's seasonal breadth oversells a $14.99 binding part — the copy doesn't age well against the literal product.
- **Ad 3** (Patagonia Nano Puff Hoodie, women's): Same generic seasonal copy as Ad 2, this time applied to apparel rather than the "skis, snowboards" the copy names. Landing page shows 5-star rating, "Read 59 Reviews," and "Sell Out Risk: Medium (4 remaining)" scarcity messaging near the size selector — the strongest proof/urgency stack of the three landing pages.
- Ad #1 and Ad #2 landing page URLs were not provided, so only Ad #3's landing page could be WebFetched for text-level analysis (WebFetch returned HTTP 403; visual summary data used instead).
- All three landing pages carry the same "Labor Day Sale" top banner, identical trust-signal block (rewards points, free shipping over $50, lowest price guarantee, 366-day returns), and an AI chat widget with preset questions — consistent across ads.

### Google Ads

Google search/Shopping/Display ads lead with explicit price and policy claims in the ad copy itself: "Up To 50% Off," "We Beat Prices by 5%," "366 Day No Hassle Returns," "Lowest Price Guarantee," "Fast FREE SHIPPING." Google search headlines also name specific products and brands (Arc'teryx, Salomon, Atomic, Round Fit Ski Helmets) more consistently than the three Meta ads reviewed.

Gap vs. Meta: the three Meta ads analyzed carry generic seasonal lifestyle copy with no price, discount percentage, or guarantee stated in the ad text — that detail only appears once the shopper lands on the PDP. Google is training shoppers to expect price/guarantee messaging up front; Meta isn't delivering it, which likely under-qualifies clicks and depresses on-page conversion once the site's severe load time (see PageSpeed below) is factored in.

### Reviews & UGC

Not collected. See Missing Data.

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON reports, fetched 2026-08-21.

**Homepage** (`https://www.evo.com/`)
- Performance score: 34/100
- LCP: 12.9s (score 0)
- TBT: 1,110ms (score 0.23)
- FCP: 4.4s
- Speed Index: 12.4s
- TTI: 45.5s (score 0)

**PDP** (`https://www.evo.com/products/102232-patagonia-nano-puff-hoodie-women-s`)
- Performance score: 30/100
- LCP: 11.1s (score 0)
- TBT: 1,610ms (score 0.12)
- FCP: 4.5s
- Speed Index: 15.8s
- TTI: 49.8s (score 0)

Both pages score in Lighthouse's "poor" band on every timing metric that matters for conversion. TTI near 45-50 seconds means the page is technically "loaded" long before it's actually interactive — every paid click (Meta and Google alike) is landing on a page that isn't clickable for the better part of a minute on a throttled connection. CLS is 0 on both pages, so layout stability isn't the problem; load and interactivity are.

### Competitor Analysis

Self-researched via WebSearch, 2026-08-21 (no user-provided competitor data in `raw/competitors.md`). Backcountry.com and Christy Sports (christysports.com) are evo's two closest competitors by site-similarity data (Backcountry ~highest overlap, Christy Sports ~91% similarity per Similarweb).

| | evo | Backcountry | Christy Sports |
|---|---|---|---|
| Shipping | Free over $50 | Standard/Economy paid tiers; free-shipping threshold not confirmed in this search | Free over $99 (account holders only; oversized items excluded) |
| Returns | 366 days | 90 days (free if refunded as store credit; $8.99 flat rate otherwise) | 367 days |
| Price match | "Lowest price guarantee" | Beats competitor price by 5% | Price match, case-by-case |

evo's free-shipping threshold ($50) is lower than Christy Sports' ($99), and its return window (366 days) matches Christy Sports and beats Backcountry (90 days) by a wide margin — evo's trust-signal terms are already competitive or better. The gap isn't the policy, it's that the policy text sits in a small, easy-to-skim block on the PDP (see Site Screenshots below) rather than being surfaced earlier or reinforced in the cart, where Backcountry's more aggressive "beat by 5%" language creates a sharper price objection to preempt.

### Emails

Not collected (skipped in manifest — no source data available).

### Inspiration Sites

Not collected (skipped in manifest — no source data available).

### Non-Data Context

Not collected (skipped in manifest — no call notes or strategic priorities provided).

### Current Site Screenshots

**Homepage:** Sitewide red "LABOR DAY SALE — UP TO 50% OFF!" banner sits above a sticky nav (logo, search, utility links, full sport/demographic category nav, cart/account icons). Hero is a full-width lifestyle photo with an overlaid "UP TO 50% OFF — SUMMER & SNOW GEAR" sale graphic — no product-specific or brand-differentiation messaging in the hero itself. Below the fold: a 5-tile sale-category carousel, then a 6-product "Labor Day Sale Top Picks" carousel with per-product star ratings, then a brand-logo carousel. No sticky purchase CTA anywhere on the homepage — the only sticky element is the top nav/search bar. Live WebFetch of the current homepage confirms the same sale-led framing plus four brand-promise callouts (fast free shipping, easy returns, price match, VIP perks) that don't appear in the captured screenshot folds, meaning that trust content lives further down the page than fold 3.

**Collection page:** Only the "Labor Day Sale" promotional collection was captured — no evergreen/standard category page exists in the dataset, so baseline (non-sale) browsing behavior can't be assessed. The captured page shows a 4-column grid, left-sidebar filters, and a "9758 Items" count with no visible pagination control in any of the three captured folds. Every card is stamped with a red "LABOR DAY SALE" badge and shows a strikethrough price range plus star rating.

**PDP:** No dedicated PDP screenshots were captured; the closest available PDP data is the Ad landing page folds (Ads 1-3, detailed above). Common pattern across all three: buy box on the right with price/strikethrough, PayPal financing line, Labor Day banner, variant selectors, black "Add to Cart" button, and a trust-signal text block (rewards, $50 free shipping, lowest price guarantee, 366-day returns) that appears only after scrolling past Add to Cart — not visible at first glance in fold 1.

**Cart (drawer, not full page):** Right-side slide-out, single line item shown with thumbnail, title, SKU, color, size, price, and the same "Sell Out Risk" scarcity note carried over from the PDP. A "You May Also Like" carousel offers cross-sell, but with no bundle discount or shipping-threshold progress bar. No guarantee, return policy, or shipping-cost information is visible inside the cart drawer itself — the trust signals present everywhere else on the PDP disappear at the exact moment the shopper is deciding whether to check out. Full-width black "Checkout - $[price]" button anchors the bottom.

## Cross-Source Themes

1. **Catastrophic page speed is the highest-evidence, highest-revenue-risk issue.** Homepage (34/100, 12.9s LCP, 45.5s TTI) and PDP (30/100, 11.1s LCP, 49.8s TTI) both fail Lighthouse's performance thresholds by a wide margin. Every paid click from both Meta and Google ad sets lands on one of these two page types. This isn't a single-page fix — it's systemic and it undercuts every other test on this list, since a page that isn't interactive for 45+ seconds suppresses conversion regardless of copy or layout changes.
2. **Trust signals and policy terms are competitive but poorly placed.** evo's free-shipping threshold, return window, and price guarantee all match or beat Backcountry and Christy Sports, but the text block carrying them sits below Add to Cart on the PDP and is entirely absent from the cart drawer — the two moments closest to purchase decision and price-objection handling.
3. **Meta ad copy underperforms Google ad copy on message specificity.** Google ads state price, discount percentage, and guarantee terms directly in ad text; the three Meta ads reviewed use generic seasonal copy with no price or offer detail, pushing that information to the landing page — where load time then delays it further.

## Top Test Opportunities

**Homepage & PDP Load Time Remediation** — Homepage scores 34/100 (12.9s LCP, 45.5s TTI) and PDP scores 30/100 (11.1s LCP, 49.8s TTI) in Lighthouse; every ad click lands on one of these two templates and can't be interacted with for 45+ seconds. Evidence: pagespeed.md (Lighthouse JSON, both pages). Est. lift: conservative 5-10% CR lift on paid landing traffic x sessions/mo (unknown — see Missing Data) x AOV (unknown) = high-priority, revenue estimate blocked on traffic/AOV data.

**Surface Trust Signals in the Cart Drawer** — The cart drawer shows product, price, scarcity note, and a bare "Checkout" button with no free-shipping threshold, return policy, or guarantee copy, even though that exact text block exists one screen up on the PDP. Evidence: site-visual-summary.md (cart drawer), meta-ads-visual-summary.md (PDP trust-signal blocks). Est. lift: conservative 1-2% CR lift on cart-to-checkout x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data.

**Move PDP Trust-Signal Block Above the Fold** — On all three ad landing pages, the rewards/shipping/price-guarantee/returns text block sits in fold 2, after Add to Cart, not alongside the price and CTA in fold 1. Evidence: meta-ads-visual-summary.md (Ads 1-3, fold 1 vs fold 2). Est. lift: conservative 1-2% CR lift on PDP-to-cart x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data.

**Add Review Proof to the Kids' Bundle PDP (Ad 1)** — Ad 1's landing page (GNU Young Money bundle) shows no star rating or review count anywhere in folds 1-2, unlike Ads 2 and 3, which both display prominent star ratings ("Read 3 Reviews," "Read 59 Reviews") directly under the product title. Evidence: meta-ads-visual-summary.md (Ad 1 vs Ad 2/Ad 3 comparison). Est. lift: conservative 0.5-1% CR lift on this SKU's landing traffic — narrow single-SKU scope, best treated as the strongest example of a broader "review proof consistency" fix rather than a standalone test.

**Simplify the Multi-Component Bundle Buy Box** — Ad 1's landing page stacks three separate variant pickers (board size, binding color, boot size) plus quantity in one scrolling buy box block, with no visual grouping or step indicator distinguishing the three products from one purchase decision. Evidence: meta-ads-visual-summary.md (Ad 1, fold 1-2). Est. lift: conservative 1-2% CR lift on bundle PDP traffic x sessions/mo (unknown) x AOV (unknown, bundle price ~$538) = revenue estimate blocked on traffic data.

**Align Meta Ad Copy with Google's Price/Offer-Led Approach** — Google ads state explicit price, discount %, and guarantee terms in ad text ("Up To 50% Off," "We Beat Prices by 5%," "366 Day No Hassle Returns"); the three Meta ads reviewed use generic seasonal copy with no price or offer detail, deferring that information to a landing page that takes 45+ seconds to become interactive. Evidence: google-ads-visual-summary.md, meta-ads-visual-summary.md (cross-comparison). Est. lift: conservative 5-10% CTR/CVR lift on Meta ad set x current Meta spend/sessions (unknown) = revenue estimate blocked on ad spend/sessions data.

**Fix Ad 2's Copy-to-Product Specificity Gap** — Ad 2 uses the same broad "latest skis, snowboards & more" copy as Ad 3, applied to a $14.99 Burton toe strap accessory — the copy's scope doesn't match a low-consideration, low-price accessory purchase, which likely inflates cost-per-click relative to intent. Evidence: meta-ads-visual-summary.md (Ad 2). Est. lift: narrow single-ad scope, best treated as the strongest example of the broader Meta ad copy-alignment fix above rather than a standalone test.

**Add a Shipping-Threshold Progress Bar to the Cart** — The cart drawer's "You May Also Like" carousel offers cross-sell with no bundle discount or free-shipping-threshold progress indicator, despite evo's $50 free-shipping threshold being a stated brand promise. Evidence: site-visual-summary.md (cart drawer), live homepage WebFetch (brand promise callouts). Est. lift: conservative 2-4% AOV lift on cart sessions x sessions/mo (unknown) x average cart value (unknown) = revenue estimate blocked on traffic/AOV data.

**Test a Non-Sale Homepage Hero Variant** — The current homepage hero is entirely sale-led ("UP TO 50% OFF — SUMMER & SNOW GEAR") with no product- or brand-differentiation messaging, while the live site's four brand-promise callouts (fast shipping, easy returns, price match, VIP perks) sit below the visible fold. Evidence: site-visual-summary.md (homepage fold 1), live homepage WebFetch. Est. lift: conservative 1-3% CR lift on homepage sessions x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data. Note: this test is time-bound to the Labor Day promo window and should be scoped as evergreen hero design, not a sale-specific change.

**Reduce Collection Page Grid Size or Add Pagination/Load-More Clarity** — The captured "Labor Day Sale" collection shows "9758 Items" with no visible pagination control in any of the three captured folds, risking decision paralysis on an already-slow-loading site. Evidence: site-visual-summary.md (collection page fold 1-3). Note: only the sale collection was captured — no evergreen category page exists in the dataset to confirm this pattern holds outside the promo. Est. lift: conservative 1-2% CR lift on collection-to-PDP click-through x sessions/mo (unknown) x AOV (unknown) = revenue estimate blocked on traffic/AOV data and evergreen-collection confirmation.

## Unused but Valuable Findings

- The AI chat widget on PDPs uses preset questions ("Does this bundle include bindings and boots?") that could double as an FAQ-accordion CRO test if chat engagement data were available — no engagement data was collected, so this is a hypothesis only.
- Christy Sports' 367-day return window and evo's 366-day window are effectively tied — evo's differentiation opportunity is speed and cart-stage trust-signal visibility, not policy terms themselves.

## Missing Data

- **Reviews & UGC:** Not collected. Manifest confirms the only product with a confirmed available review source is Ad #3's landing page (Patagonia Nano Puff Hoodie, 59 reviews per the visual summary), but no qualitative review content (themes, complaints, quotes) was gathered. This blocks a "What Customers Love / What Frustrates Customers" section entirely for this audit.
- **PDP-specific screenshots:** No standalone `pdp-fN.png` screenshots exist beyond the ad landing page PDPs (Ads 1-3). PDP findings in this audit are drawn entirely from those three ad-linked products, not a general/representative PDP sample.
- **Standard collection/category page:** Only the "Labor Day Sale" promotional collection was captured. Findings on grid size, filtering, and card layout may not generalize to evergreen (non-sale) browsing.
- **Site sessions, PDP/collection AOV, and traffic split by channel:** Not available in any collected source. Every "Est. lift" dollar figure above is blocked on this data — revenue estimates could not be calculated and are flagged rather than invented.
- **Ad #1 and Ad #2 landing page URLs:** Not provided, so live WebFetch text-level analysis could only be performed for Ad #3 (and that WebFetch returned HTTP 403 — findings for Ad #3's PDP rely on the visual summary, not live text).
- **Competitor data:** No user-provided `raw/competitors.md` existed; the competitor table above is entirely self-researched via WebSearch and should be verified against evo's own competitive intelligence if available.
