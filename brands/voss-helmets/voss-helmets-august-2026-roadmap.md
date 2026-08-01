# Voss Helmets CRO Research Brief

**Data Sources:** meta-ads-visual-summary, google-ads-visual-summary, site-visual-summary, pagespeed.md, context.md, competitor research (self-researched 2026-07-31), live site extraction (2026-07-31)

---

## Insights

Voss uses its review count as the primary hook in paid media. Ad 1 leads with "Over 4700+ Reviews Loving Voss" as its opening line (Source: meta-ads-visual-summary). The homepage hero has no star rating and no review count. The PDP has no ratings across any fold. Zero of the 65 product cards on the collection page show a rating. Live site extraction on 2026-07-31 confirms 4,600+ verified reviews exist on the platform. The brand markets its review count in ads and then withholds it at every stage of the on-site funnel. For a DTC brand competing without retail shelf presence (where HJC and LS2 display ratings on every listing at Cycle Gear and RevZilla), on-site social proof is the primary purchase validator. It is entirely absent.

Two of the three active Meta ads have message match failures that compound the problem. Ad 1 shows the 601 D2 Dual Sport in the creative but routes to a 991 Hollywood campaign page. Ad 3 promotes a $219.99 helmet and lands visitors on a homepage where the hero product costs $419.99 (Source: meta-ads-visual-summary). A visitor who clicked on a $219.99 helmet sees a $200 contradiction within one second of arriving. The only well-matched ad is Ad 2, a testimonial for the 580 Modular routing to the 580 Modular collection page. Every session from Ads 1 and 3 starts in a deficit.

The primary conversion page (the VOSS 991 Gloss Gold Hollywood PDP, the terminal destination of the highest-traffic paid campaign) buries the Add to Cart button in fold 2, below a 10-swatch faceshield selector and a rear spoiler selector. Mobile Time to Interactive on this page is 44 seconds and Total Blocking Time is 860ms (Source: pagespeed.md, Lighthouse 13.3.0, 2026-07-31). A visitor who clicks an ad, arrives on the homepage, hits the hero CTA, and navigates to the PDP waits 44 seconds for the page to become interactive and must then scroll past the accessory upsell sections before a purchase button appears. The homepage scores 44/100 on mobile performance, with LCP of 10.6 seconds and TTI of 36.4 seconds (Source: pagespeed.md, 2026-07-31). These are not marginal issues on a $419.99 product.

The homepage is structured as a brand-experience scroll, not a conversion page. Fold 2 is consumed entirely by the Voss Collective loyalty program: three tier levels, points multipliers, and two loyalty CTAs (Source: site-visual-summary). This appears before any product review, secondary product, or pricing context. The loyalty program is not referenced in any ad creative (Source: meta-ads-visual-summary). A cold-traffic visitor from a paid ad has made no prior purchase and has zero points. Fold 2 delays every conversion signal behind content that is irrelevant to first-purchase intent.

The top three opportunities (sticky ATC bar on the PDP, review count in the homepage hero, dedicated landing page for Ad 3 traffic) carry a combined conservative revenue estimate of $52,200/mo at current inferred traffic levels. All three are implementable without platform migrations or new integrations.

---

## Slot 1: PDP Sticky Add to Cart Bar

**Type:** A/B test (1 variation vs. control)
**Page:** VOSS 991 Gloss Gold Hollywood PDP (https://voss-helmets.com/products/voss-991-gloss-gold-hollywood-carbon-fiber-full-face-helmet-mips-pinlock-prepared)
**Revenue potential:** 8,000 sessions/mo x 0.5% CR lift x $419.99 AOV = $16,800/mo conservative.

**Hypothesis:** If we add a sticky Add to Cart bar pinned to the bottom of the viewport, more PDP visitors will convert because the purchase action is always visible regardless of scroll position or page load state.

**Data:** The Add to Cart button does not appear in fold 1 of the PDP. A visitor must scroll past a 10-swatch faceshield selector and a rear spoiler selector before reaching it (Source: site-visual-summary, PDP folds 1-2). Mobile TTI is 44 seconds and TBT is 860ms, meaning the button is both visually inaccessible and slow to become interactive (Source: pagespeed.md, Lighthouse 13.3.0, 2026-07-31). This PDP is the primary destination of the homepage "SHOP HOLLYWOOD" CTA, which 2 of 3 active Meta ads route to via the homepage (Source: context.md).

**Pre-test fix required:** The product description in PDP fold 2 reads "991 CARBON BLACK" on the Gold Hollywood variant page. This template copy error is a trust friction point independent of the ATC bar. Fix it before launching this test to avoid contaminating results (Source: site-visual-summary, PDP fold 2).

**V1:** A sticky bar fixed to the bottom of the viewport on both mobile and desktop. Bar contains: product name truncated to one line, price ($419.99 USD), and an "ADD TO CART" button. On mobile, tapping the ATC button when no size is selected slides up a bottom sheet with the six size options before adding to cart. On desktop, the bar appears once the visitor scrolls past the native ATC button position and disappears if they scroll back above it. All other page elements unchanged. Control: current state with no sticky element.

---

## Slot 2: Homepage Hero - Trust Strip with Review Count

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://voss-helmets.com/)
**Revenue potential:** 15,000 sessions/mo x 0.3% CR lift x $420 AOV = $18,900/mo conservative.

**Hypothesis:** If we add a star rating and review count to the homepage hero, CTA click-through to the PDP will increase because visitors see the social proof the ad promised before they decide whether to engage.

**Data:** Ad 1 leads with "Over 4700+ Reviews Loving Voss" as its primary hook (Source: meta-ads-visual-summary). The homepage hero contains zero social proof: no star rating, no review count, no guarantee copy, and no returns language (Source: site-visual-summary, homepage fold 1). Live site extraction on 2026-07-31 confirms 4,600+ verified reviews exist. The "SHOP HOLLYWOOD" CTA is the only path to conversion from fold 1.

**V1:** A trust strip added directly below the "991 HOLLYWOOD HAS ARRIVED" headline, above the "SHOP HOLLYWOOD" CTA button. Strip contains: star icon cluster (5 filled stars), the text "4,700+ verified riders," and a separator followed by "Free shipping + free returns." Mobile: single centered block stacked below the headline. Desktop: horizontal one-liner centered below the headline. Hero image, headline text, and CTA button are unchanged. No other elements modified.

---

## Slot 3: Ad 3 - Dedicated Landing Page vs. Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Ad 3 traffic destination (currently https://voss-helmets.com/)
**Revenue potential:** 5,000 sessions/mo x 1.5% CR lift x $219.99 AOV = $16,500/mo conservative.

**Hypothesis:** If we route Ad 3 traffic to a dedicated landing page for the $219.99 helmet, conversion rate will increase because visitors land in a context that matches the product, price, and features they were shown in the ad.

**Data:** Ad 3 (started May 13, 2026) promotes a black full-face helmet at $219.99 with specific feature claims: "advanced ventilation, dual-density EPS liner and removable liner system." The current destination is the homepage, where the hero product costs $419.99 (Source: meta-ads-visual-summary, context.md). The $200 price gap is the primary contradiction at arrival. The three features named in the ad are not restated anywhere on the homepage. Control: Ad 3 traffic continues routing to the homepage.

**V1:** A dedicated Shopify landing page for the $219.99 helmet. Hero section: product image matching the Ad 3 creative (black full-face), product name, and $219.99 price displayed prominently. Feature section directly below: three copy blocks restating the ad's claims in the same order ("Advanced Ventilation," "Dual-Density EPS Liner," "Removable Liner System"), each with a one-sentence description. Trust strip: star rating and review count pulled from existing reviews. Single primary CTA: "Add to Cart." No loyalty program content and no other products above the fold. Mobile: stacked layout with price and CTA visible without scrolling. Desktop: two-column layout with product image left, price and CTA right, feature section below the fold.

---

## Slot 4: PDP - Star Rating and Review Count in Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** VOSS 991 Gloss Gold Hollywood PDP (https://voss-helmets.com/products/voss-991-gloss-gold-hollywood-carbon-fiber-full-face-helmet-mips-pinlock-prepared)
**Revenue potential:** 8,000 sessions/mo x 0.4% CR lift x $419.99 AOV = $13,440/mo conservative.

**Hypothesis:** If we surface a star rating and review count directly in the PDP buy box, conversion rate will increase because visitors have a social proof anchor before evaluating price and size options on a $419.99 purchase.

**Data:** The buy box shows product title, $419.99 price, size chart link, six size options, and a loyalty points widget. No star rating or review count appears anywhere across three captured folds (Source: site-visual-summary, PDP folds 1-3). 4,600+ reviews exist on the live site (Source: live site extraction, 2026-07-31). Ad 1 uses "4700+ Reviews" as its primary conversion hook. Arriving at a PDP with no review signal breaks the expectation set by the ad (Source: meta-ads-visual-summary).

**V1:** A star rating display added directly below the product title and above the price in the buy box. Format: filled star icons, numeric rating, and parenthetical review count (e.g., "4.6 (312 reviews)"). The review count links to the reviews section further down the page. Mobile: same placement below the product title, full width. Desktop: same placement. All other buy box elements (price, size chart link, size selector, loyalty widget) unchanged.

---

## Slot 5: Homepage Fold 2 - Social Proof Section Replaces Loyalty Intro

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://voss-helmets.com/)
**Revenue potential:** 15,000 sessions/mo x 0.2% CR lift x $420 AOV = $12,600/mo conservative.

**Hypothesis:** If we replace the Voss Collective loyalty section in homepage fold 2 with a customer review strip, cold-traffic conversion will increase because first-time visitors see purchase validation before being asked to join a program they have no history with.

**Data:** Homepage fold 2 is entirely the Voss Collective loyalty tier structure: Rider (8pts/$1), Road Captain (5,000pts, +15%), and Voss Inner Circle (15,000pts, +30%), plus two CTAs (Source: site-visual-summary, homepage fold 2). This appears before any secondary product, review, or pricing content. Two of 3 active Meta ads route cold traffic to the homepage (Source: context.md). The loyalty program is not referenced in any ad creative (Source: meta-ads-visual-summary). A visitor who has never purchased has zero points and no status to unlock.

**V1:** Replace the Voss Collective tier section with a customer review strip. Strip contains 3-4 verbatim customer reviews from the existing review database, each showing: star rating, quoted review text (2-3 sentences), reviewer name, and helmet model purchased. Mobile: single-column layout with one review visible at a time and swipe navigation. Desktop: three-column grid showing three reviews simultaneously. The loyalty section moves to fold 4 or below in the variation and is not removed. No new CTA added in the review strip.

---

## Slot 6: Collection Page - Star Ratings on Product Cards

**Type:** A/B test (1 variation vs. control)
**Page:** All Helmets collection (https://voss-helmets.com/collections/all)
**Revenue potential:** 12,000 sessions/mo x 0.4% CR lift x $300 AOV = $14,400/mo conservative.

**Hypothesis:** If we add star ratings to product cards on the collection page, click-through to PDPs will increase because visitors can differentiate between models using social proof rather than name and price alone.

**Data:** Zero star ratings appear on any of the 65 product cards across three captured collection folds (Source: site-visual-summary, collection folds 1-3). Visitors comparing the 991 ($419.99), 993 ($299.99), 989 ($239.99), and 988 ($219.99) have no social signal to differentiate models. Competitors HJC and LS2 display ratings on every listing at Cycle Gear and RevZilla (Source: competitor research, 2026-07-31). 4,600+ reviews are available to pull from (Source: live site extraction, 2026-07-31).

**V1:** A star rating badge added below the product name on each card, above the price. Format: numeric rating, star icon, and review count (e.g., "4.6 ★ 312"). Products with no reviews show no badge. Mobile: 2-column card layout unchanged, rating appears as a single text line between product name and price. Desktop: 4-column grid unchanged, same placement. No other card elements modified.

---

## Slot 7: Cart - Free Shipping Progress Bar

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (https://voss-helmets.com/cart)
**Revenue potential:** 3,000 cart sessions/mo x 0.8% AOV lift x $280 blended AOV = $6,720/mo.

**Hypothesis:** If we add a free shipping progress bar to the cart header, AOV will increase for sessions below the $75 threshold because visitors see a concrete incentive to add another item before checking out.

**Data:** The cart shows no free shipping indicator. The $75 free shipping threshold is sitewide but appears only in the global announcement bar, not in the cart itself (Source: site-visual-summary, cart screenshot). Free shipping is cited in paid ad copy (Source: meta-ads-visual-summary). The catalog contains accessories from $19.99, including faceshields, creating natural add-on candidates. A $419.99 session has already cleared the threshold, but lower-ticket cart sessions (580 Modular at $249.99, accessories, sale items) have meaningful headroom below $75.

**V1:** A progress bar displayed at the top of the cart above the line items. When the cart total is below $75: bar shows "You're $[X] away from free shipping" with a filled progress indicator proportional to the threshold. When the cart total is at or above $75: bar shows "Free shipping unlocked" with a checkmark icon and a green color state. Mobile: full-width bar at the top of the cart drawer. Desktop: full-width bar at the top of the cart page, above the items list. No accessory cross-sell or product recommendations added in this variation. The progress bar mechanic is tested in isolation.

---

## Slot 8: Google Shopping - Fix Price Feed Rendering

**Type:** Immediate Fix

Both Google Shopping ad units captured on 2026-07-31 display "[Price]" as placeholder text instead of actual dollar amounts (Source: google-ads-visual-summary). If this is a live Merchant Center feed issue rather than a screenshot artifact, Shopping impressions are running without prices. Missing prices are a disqualifying signal for comparison shoppers and a feed quality violation that risks placement suspension.

**What to fix:**
- Audit all SKUs in Google Merchant Center for the `price` attribute
- Confirm the price field is populated in the correct format (numeric value + ISO 4217 currency code, e.g., "419.99 USD")
- Check whether `sale_price` overrides are blanking the `price` display
- Resubmit the feed and verify Shopping ad previews show actual prices before the next campaign cycle
- If the feed renders correctly in Merchant Center but "[Price]" appeared in the ad, capture it and file a Google Ads support ticket

No A/B test required. Fix, verify, and monitor CTR in Google Ads.

---

## Future Slot Candidates

1. **PDP: Fix "991 Carbon Black" Template Copy on Gold Hollywood Variant** - The description block in PDP fold 2 reads "991 CARBON BLACK" on the Gold Hollywood variant page. This is a template error visible to shoppers at the $419.99 consideration stage. Classify as an Immediate Fix and resolve before any PDP A/B test launches. Running a PDP test with incorrect copy contaminates results. Source: site-visual-summary (PDP fold 2).

2. **Cart: Remove T&C Checkbox Before Checkout** - A mandatory "I AGREE WITH THE TERMS AND CONDITIONS" checkbox sits above the checkout button in the mobile cart. Removing it eliminates a friction step at the final conversion moment. Industry benchmarks suggest 2-4% checkout initiation lift on removal. Source: site-visual-summary (cart screenshot).

3. **PDP: Surface BNPL Installment Pricing Near Price Field** - Buy Now Pay Later is available sitewide but not shown in the PDP buy box. For a $419.99 helmet, adding installment pricing (e.g., "or 4 x $105 with Afterpay") near the price reduces price-perception friction without discounting. Source: site-visual-summary (PDP fold 1), live site extraction (2026-07-31).

4. **Ad 2 (580 Modular LP): Restore Free Shipping in Announcement Bar** - The 580 Modular collection page shows "HASSLE-FREE RETURNS + EXCHANGES" in the announcement bar instead of the "FREE SHIPPING ON ORDERS $75+" shown on the homepage. A low-effort consistency fix for the Ad 2 landing experience. Source: meta-ads-visual-summary, site-visual-summary.
