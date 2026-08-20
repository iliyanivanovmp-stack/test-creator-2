# Revival CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, Current Site Screenshots, live homepage fetch, competitor research

## Insights

Revival's biggest structural gap isn't any single page. It's that the primary CTA is static on every page type in the funnel: homepage, PDP, and all three Meta landing page templates. Trust content (press logos, athlete endorsement, UGC, tabbed education) stacks below the fold on each of these, so the buy action disappears from view exactly while shoppers are reading the content meant to convince them to buy — Source: site-visual-summary.md, meta-ads-visual-summary.md.

Paid media has one clean break in message match. Ad 2's "2026 Travel Hack" hook (hot-climate hydration, packing for a getaway) sends to the generic "Your Best Day, Every Day" homepage template with zero travel imagery, copy, or offer, and Google Ads has no travel-angle counterpart at all — this creative is running in complete isolation. Ads 1 and 3 (hangover/late-night recovery) match tightly with both their landing pages and Google's search themes — Source: meta-ads-visual-summary.md, google-ads-visual-summary.md.

Pricing transparency drops off at the exact moment it matters most. The PDP buy box shows only per-stick pricing (£1.07 vs £1.33) with no discount anchor, while the cart displays a clear struck-through £39.99 → £31.99 for the identical product. The stronger price anchor already exists as a built asset — it's just placed one step too late — Source: site-visual-summary.md.

Competitor research adds a second layer to the PDP story: Revival's "3x electrolytes" claim is category-standard, matched by both SOS Rehydrate and Liquid I.V. The athlete endorsement and press logos are Revival's less-matched, stronger differentiators, and they currently sit in fold 2, after the hero — Source: competitor analysis.

Revenue opportunity: PDP-to-cart conversion is touched by three of the top opportunities here (sticky ATC, compare-at pricing, buy box hierarchy). Even a conservative 2% CR lift on £30-40 AOV compounds fast once traffic data confirms session volume. Sessions/mo were not collected, so all lift estimates below are directional pending that data.

## Slot 1: Sticky Add-to-Cart Bar on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (revivalshots.com PDP)
**Revenue potential:** Sessions/mo unknown x 2-4% CR lift (conservative, per seed) x £30 AOV = directional estimate pending traffic data.

**Hypothesis:** If we add a persistent sticky Add to Cart bar that appears once a shopper scrolls past the buy box, add-to-cart rate and orders will increase because the purchase action stays reachable through the trust and education content that currently pushes it off-screen.

**Data:** The PDP's full-width "ADD TO CART" button is static in fold 1. Once a shopper scrolls into fold 2 (trust icon row, video module, tabbed Description/Benefits/Research content) or fold 3 (Subscribe & Save promo, UGC carousel), there's no persistent bar bringing the CTA back into view — the only way back is scrolling up. Source: site-visual-summary.md (PDP fold 1-3, CTA behavior). Industry precedent supports this: GoodUI reports 4 tests in favor of sticky mobile CTAs, and a comparable supplement ecommerce case study saw a 5.2% increase in orders (98% significance) from a sticky add-to-cart bar.

**V1:** Add a sticky bar (product thumbnail, name, price, Add to Cart button) that slides in from the bottom once the user scrolls past the existing buy box, and stays pinned through folds 2-3. Mobile: full-width bar pinned to the bottom viewport edge, condensed to thumbnail + price + button. Desktop: slim horizontal bar pinned to the top of the viewport on scroll, same fields. Control keeps the current static, non-sticky buy box with no persistent CTA.

## Slot 2: Compare-At Pricing in PDP Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (revivalshots.com PDP)
**Revenue potential:** Sessions/mo unknown x 1-3% CR lift (conservative, per seed) on PDP-to-cart conversion x £30-40 AOV = directional estimate pending traffic data.

**Hypothesis:** If we show the struck-through compare-at price (£39.99 → £31.99) directly in the PDP buy box instead of only per-stick pricing, add-to-cart rate will increase because shoppers see the discount anchor at the moment they're deciding, not after.

**Data:** The PDP buy box currently shows only per-stick unit pricing (£1.07 vs £1.33) for the two purchase options, with no strikethrough or compare-at price. The cart drawer already displays a clear £39.99 → £31.99 struck-through price for the identical product — the discount asset exists, it's just placed one step too late in the funnel. Source: site-visual-summary.md (PDP buy box detail, Cart line items).

**V1:** Add the struck-through £39.99 → £31.99 pricing (already used in the cart) directly beneath the price on both the Subscribe & Save and One-time purchase buy box options, keeping per-stick pricing as secondary text. Mobile: struck-through price stacks directly under the bold price, above the per-stick line. Desktop: same hierarchy, inline next to the price. Control keeps the current per-stick-only pricing with no compare-at price shown.

## Slot 3: Rebuild Ad 2 Landing Page to Match Travel Hook

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 2 landing page (travel angle)
**Revenue potential:** Ad 2 traffic x 10-20% relative CVR lift (per seed, directional) x £30-40 AOV = directional estimate pending ad-level spend/CVR data.

**Hypothesis:** If we rebuild Ad 2's landing page to carry the travel hook (headline, imagery, copy) through from ad to page, conversion rate on Ad 2 traffic will increase because message match will no longer break at the click.

**Data:** Ad 2's creative and copy are travel-themed: headline "2026 Travel Hack," body copy "Stay hydrated in the hottest climates / Accelerate recovery / Wake up fresh," travel/airport-setting thumbnail. It currently lands on the same generic template as Ad 1: full-width blue banner, product lineup image, headline "Your Best Day, Every Day," white "Shop Now" button, with no travel imagery, hot-climate copy, or travel-specific offer. Google Ads has no travel-angle ad either, so this creative runs with zero cross-channel or on-site support. Source: meta-ads-visual-summary.md (Ad 2), google-ads-visual-summary.md.

**V1:** Rebuild the Ad 2 landing page hero to carry the travel hook: replace the generic blue banner and product lineup image with travel/hot-climate imagery, headline matching the ad ("2026 Travel Hack" or close variant), and body copy on hot-climate hydration and recovery, keeping the same CTA button and buy box structure below the hero. Mobile: single-column hero with travel image above headline and CTA. Desktop: image and copy side by side, same structural template as the current LP below the hero. Control keeps the current generic brand hero landing page.

## Slot 4: Neutral-Hierarchy Buy Box Test (Subscribe vs. One-Time)

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (revivalshots.com PDP)
**Revenue potential:** Diagnostic test. Per seed, directional only, could move AOV or CR in either direction — primary value is data on true subscribe-vs-one-time preference.

**Hypothesis:** If we give Subscribe & Save and One-time purchase equal visual weight in the buy box, we'll learn whether current subscription volume reflects genuine preference or is driven by the default's visual emphasis, because removing the asymmetric styling isolates the effect of the nudge itself.

**Data:** The buy box pre-selects "Subscribe & Save 20%" (£31.99) with a blue border and visual emphasis, while "One-time purchase" (£39.99) sits below in a plain, unselected, unhighlighted border. Subscribe & Save includes 20% off first order, 10% off for life, and free gifts worth £35.99 plus a free steel water bottle worth £19.99 — a heavily incentivized default with asymmetric visual weight against the alternative. Source: site-visual-summary.md (PDP buy box detail). Includes free shipping + more subscriber benefits under the selected option to keep the value clear without overstating unverified perks.

**V1:** Give both purchase options equal border weight and no default pre-selection, requiring the shopper to actively choose Subscribe & Save or One-time purchase before Add to Cart activates. Keep the existing Subscribe & Save benefit list (20% off first order, 10% off for life, free gifts) visible under that option when selected. Mobile: both options stacked with identical styling, neither pre-checked. Desktop: same stacked layout, equal visual treatment. Control keeps the current pre-selected, blue-bordered Subscribe & Save default.

## Slot 5: Differentiate Ad 3 Advertorial CTA Placement

**Type:** A/B test (1 variation vs. control)
**Page:** Meta Ad 3 advertorial landing page
**Revenue potential:** Ad 3 traffic x 5-10% relative CVR lift (per seed, directional) x £30-40 AOV = directional estimate pending ad-level spend/CVR data.

**Hypothesis:** If we add an earlier CTA touchpoint in the advertorial (near the top, alongside the header link) while keeping the mid-article CTA, conversion rate on Ad 3 traffic will increase because readers who don't scroll deep into the listicle still get a clear path to purchase.

**Data:** Ad 3's landing page uses a long-form advertorial template: headline "7 Reasons You Still Feel Off After a Late Night," byline "Hannah Phillips, 4 minute read," numbered listicle sections on dehydration and coffee-as-diuretic. The primary CTA, a full-width blue "Get 15% Off Revival Shots" button, is embedded mid-article after section 2, with only a small header text link as the earlier alternative. Source: meta-ads-visual-summary.md (Ad 3, LP CTA).

**V1:** Add a secondary CTA button (same "Get 15% Off Revival Shots" styling) directly under the headline and byline, before section 1 begins, while keeping the existing mid-article CTA after section 2 unchanged. Mobile: full-width button below byline, same styling as the mid-article one. Desktop: same button placement, centered under the headline block. Control keeps the current header-link-only CTA before section 1.

## Slot 6: Per-SKU Ratings on Collection Page

**Type:** A/B test (1 variation vs. control)
**Page:** Collection page ("Explore Our Ranges")
**Revenue potential:** Sessions/mo unknown x 1-2% CR lift (per seed) on collection-to-PDP click-through x £30-40 AOV = directional estimate pending traffic data.

**Hypothesis:** If we show product-level (not category-level) ratings and review counts on collection cards, click-through to PDP will increase because shoppers can judge a specific SKU's social proof before clicking in.

**Data:** The collection page shows a 2-row category grid (Rehydration & Recovery, Zero Sugar Rehydration, Natural Energy & Performance, Super Greens & Vitamins, Kids Multi-Vitamin Squash, Bundle & Save, Taster Packs) where each card displays one star rating and review count aggregated for the entire category (e.g. "Rehydration & Recovery, from £11.99, 11,648 reviews"), not the specific product or flavor. Some categories show as low as "1 review" at the category level despite the brand's overall 10,000+ review claim. Source: site-visual-summary.md (Collection page, Fold 1, Price display).

**V1:** Replace the category-level rating and review count on each card with the rating and review count of that category's top-selling or featured SKU. Mobile: single-column card grid, rating/review line updated to SKU-level data. Desktop: same grid layout, same field swap. Control keeps the current category-aggregated rating and review count.

## Slot 7: Trust Block Placement on Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (revivalshots.com)
**Revenue potential:** Sessions/mo unknown x 1-2% CR lift (per seed) on homepage-to-collection click-through x £30-40 AOV = directional estimate pending traffic data.

**Hypothesis:** If we add a condensed athlete/press trust signal to fold 1 near the hero CTA, click-through to collection will increase because Revival's strongest differentiators (versus SOS Rehydrate and Liquid I.V.) become visible before the first scroll instead of after it.

**Data:** The athlete endorsement (Hannah Cook) and press-as-seen-in logos currently sit in fold 2, after the static "Shop Now" hero. Competitor research shows Revival's "3x electrolytes" claim is category-standard (matched by SOS Rehydrate and Liquid I.V.), while the athlete endorsement and press logos are differentiators not matched by SOS Rehydrate. Source: site-visual-summary.md (Homepage fold 1-2), competitor analysis.

**V1:** Add a condensed trust strip (press logo row, small athlete quote or badge) directly beneath the hero CTA in fold 1, keeping the full athlete endorsement and press section in fold 2 unchanged. Mobile: single horizontal scroll strip of press logos under the CTA. Desktop: inline row of press logos under the CTA, same width as the hero. Control keeps trust content starting in fold 2 only.

## Slot 8: Consolidate Redundant Discount Messaging on Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (revivalshots.com)
**Revenue potential:** Minor engagement/scroll-depth lift, not independently revenue-quantifiable from available data, per seed.

**Hypothesis:** If we remove the duplicate floating "Get 15% Off" pill and keep the offer only in the header trust bar, scroll depth and on-page focus will improve because shoppers no longer see the same offer competing with itself in two places at once.

**Data:** The header trust bar states "15% Off For New Customers" on every fold. A separate floating bottom-left pill reading "Get 15% Off" persists across all three homepage folds, layered on top of page content independent of scroll position, advertising the identical offer a second time. Source: site-visual-summary.md (Homepage, CTA behavior).

**V1:** Remove the floating "Get 15% Off" pill and keep the offer stated once, in the header trust bar only. Mobile: header trust bar unchanged, floating pill removed from all folds. Desktop: same removal, no floating element on scroll. Control keeps both the header trust bar offer and the floating pill active simultaneously.

## Future Slot Candidates

1. **Fix or confirm PDP fold 2 video module** - The video/image module on PDP fold 2 renders mostly blank with only a partial visual in one corner. Needs live-site verification before it can be scoped as a fix or ruled out as a capture artifact.
2. **Add hot-climate/travel-specific messaging module sitewide** - Broader version of the Ad 2 landing page fix: a standalone travel/hot-climate content block or bundle, since the travel angle currently has zero on-site presence beyond the isolated ad.
3. **Replicate cart's "Still Thirsty?" cross-sell on PDP** - The cart's one-click cross-sell add-on module is a well-executed existing AOV pattern worth extending to the PDP rather than a problem to fix.
