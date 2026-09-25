# Bonkers Corner CRO Research Brief

**Data Sources:** Meta Ads & Landing Pages, Google Ads Transparency Center, PageSpeed/Core Web Vitals, Current Site Screenshots (homepage, PDP, cart), Competitor research (self-researched)

Bonkers Corner is running at least five different discount offers at once, and none of them match up. Each of the 3 Meta ads promises a specific code, NEW15 for 15% off, "10% OFF on Prepaid," "EXTRA 5% prepaid saving", but the landing page a shopper lands on never shows that code. Instead it rotates SHARKTANK10, an EMI-on-UPI option, and a UPI prepaid discount across three folds. Google Search and Display ads add two more framings not seen on Meta at all: "Starting At ₹999 Only" and "5% off on Prepaid Orders." The PDP's offer box rotates between three codes on its own. The cart drawer adds a fourth code, GOBONKERS15, plus a fifth framing on the checkout button. A shopper who clicks an ad for a specific discount never sees that discount again anywhere in the path to purchase.

Mobile load speed is the second critical issue, and it compounds the first. Homepage LCP is 39.0 seconds (Performance score 33/100) and PDP LCP is 49.2 seconds (score 37/100), roughly 15-20x over Google's 2.5s "good" threshold. Lighthouse flagged both runs as incomplete because the page loaded too slowly to finish testing. Source: PageSpeed/Core Web Vitals. This hits paid traffic hardest: the same visitors Meta and Google ads are paying to acquire are the ones most likely to abandon before the page renders.

Trust signals are inconsistent everywhere a shopper looks. The homepage's first three folds show zero trust content, no reviews, guarantee, or shipping promise, only a repeating Shark Tank/SHARKTANK10 announcement bar, even though a live fetch confirms trust copy ("100% MADE IN INDIA," "SHIPPING WITHIN 48 HOURS," testimonials) exists further down the page. Source: Current Site Screenshots, live homepage fetch. On PDP, a "90-Day Guarantee" badge appears on ad-linked product pages but not on the standard, organically-reached PDP. The cart drawer has zero trust content, every line is a discount code or savings figure.

Bonkers Corner sits in the mid-premium D2C streetwear bracket (~₹999-₹2,999), competing with The Souled Store and Snitch. Source: Competitor research. India's streetwear market is projected to grow from ~$10.86B (2024) to ~$20.86B by 2033, so paid acquisition costs in this category are likely to keep climbing, raising the cost of every visitor lost to a mismatched offer or a 39-second load.

No monthly sessions, AOV, or baseline conversion rate were collected for this brand, so dollar-value revenue estimates can't be calculated below. Every slot shows the formula with sessions and AOV left open. Supply those figures to convert the estimated lifts into projected monthly revenue.

## Slot 1: Lock the discount offer to one code across ads, landing pages, and PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Meta ad landing pages / PDP (Special Offers box)
**Revenue potential:** [Sessions/mo unknown] x 3-6% CVR lift on paid-social landing sessions x [AOV unknown] = revenue estimate not calculable without traffic/AOV data.

**Hypothesis:** If the landing page and PDP show one fixed discount code instead of a rotating offer box, conversion rate improves because shoppers currently never see the code the ad promised them.

**Data:** All 3 Meta ads promise a specific code or percentage in their caption (NEW15, "10% OFF on Prepaid," "EXTRA 5% prepaid saving"), but the landing page's Special Offers box rotates between SHARKTANK10, EMI-on-UPI, and a UPI prepaid discount instead, none of which match. Source: meta-ads-visual-summary.md. Google Search and Display ads add two more framings not seen on Meta at all ("Starting At ₹999 Only," "5% off on Prepaid Orders"). Source: google-ads-visual-summary.md.

**V1:** Replace the rotating Special Offers box on ad-linked landing pages and the PDP with a single static offer, SHARKTANK10, the code already used in the site-wide announcement bar and the cart drawer's primary banner. Same bordered callout placement directly below price and size selector on both mobile and desktop. No rotation between folds. Update Meta ad copy to reference SHARKTANK10 by name so the ad, landing page, and PDP all state the same code.

## Slot 2: Fix homepage and PDP mobile load speed

**Type:** Immediate Fix

Homepage LCP is 39.0 seconds (Performance score 33/100) and PDP LCP is 49.2 seconds (score 37/100) on mobile. Both Lighthouse runs returned a warning that the page loaded too slowly to complete testing, meaning real-world load is likely worse than what's captured. CLS is not the issue on either page (0 and 0.001), this is a load and interactivity bottleneck, not a layout-shift one. Source: raw/pagespeed.md. This is not a test candidate, it's a broken state that undercuts every dollar spent on the Meta and Google ads driving traffic to these exact pages. Fix load performance before running any of the tests below, since a page that doesn't render within a Lighthouse timeout will suppress every other test's results.

## Slot 3: Standardize the 90-Day Guarantee badge on every PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (all PDPs)
**Revenue potential:** [Sessions/mo unknown] x 1-3% CVR lift x [AOV unknown] = revenue estimate not calculable without traffic/AOV data.

**Hypothesis:** If the "90-Day Guarantee" badge appears on every PDP instead of only ad-linked ones, conversion rate improves because a consistent trust signal at the point of purchase reduces purchase risk.

**Data:** The collected standard PDP (Rev It Up Oversized T-shirt, ₹999) shows title, price, a 2-review star rating, size selector, and Add to Cart, with no guarantee badge. The two ad-linked PDPs (beige cargo pants, bottle-green pants) show a black "90-DAY GUARANTEE, Stitch & fabric defects? We cover it" badge directly under the price. Source: site-visual-summary.md, meta-ads-visual-summary.md (Ads 2, 3).

**V1:** Add the existing "90-DAY GUARANTEE, Stitch & fabric defects? We cover it" badge to every PDP, in the same placement already used on ad-linked pages: directly under the price, above the size selector. Same badge style and copy on mobile and desktop, no new creative needed.

## Slot 4: Move existing trust copy above the fold on homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (fold 1)
**Revenue potential:** [Sessions/mo unknown] x 1-2% CVR lift x [AOV unknown] = revenue estimate not calculable without traffic/AOV data.

**Hypothesis:** If proven trust copy already on the page moves into the first fold, conversion rate improves because most mobile visitors currently scroll past it without seeing it.

**Data:** The homepage's first three folds are entirely lifestyle photography (an 8-model hero, a two-panel lifestyle shot, an "Explore New In" slide), each with only a "SHOP NOW" button. The only recurring credibility element across all three folds is the announcement bar cycling "AS SEEN ON SHARK TANK" and the SHARKTANK10 code. A live fetch of the full homepage confirms trust copy, "100% MADE IN INDIA," "SHIPPING WITHIN 48 HOURS," and customer testimonials, exists further down the page. Source: site-visual-summary.md (Homepage folds 1-3), live homepage fetch.

**V1:** Add a compact trust strip directly beneath the fold-1 hero image, using the site's existing copy verbatim: "100% MADE IN INDIA" and "SHIPPING WITHIN 48 HOURS." On mobile, stack as a single-row scrollable strip under the hero, above the "SHOP NOW" CTA. On desktop, place as a horizontal row spanning the hero's width. No new trust claims, only relocating what already exists lower on the page.

## Slot 5: Consolidate cart drawer discount messaging and add a trust line

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (drawer)
**Revenue potential:** [Sessions/mo unknown] x 1-2% CVR lift x [AOV unknown] = revenue estimate not calculable without traffic/AOV data.

**Hypothesis:** If the cart drawer shows one discount mechanic instead of three, and adds a trust line in the space freed up, checkout conversion improves because current decision friction comes from competing offers with no trust signal to counterbalance them.

**Data:** The cart drawer stacks a black "Get 10% off with code SHARKTANK10" banner under the header, a 3-tier spend-unlock progress bar below it (₹500 to 10%, ₹5,999 to 15%, ₹9,999 to 20% via GOBONKERS15), and a "5% OFF on Prepaid Orders" sub-label under the Checkout button, three distinct offers with zero guarantee, returns, or trust content anywhere in the drawer. Source: site-visual-summary.md (Cart).

**V1:** Remove the SHARKTANK10 banner and the "5% OFF on Prepaid Orders" sub-label, keeping only the 3-tier GOBONKERS15 spend-unlock bar since it drives incremental cart value. In the space freed under the header, add a single trust line: "90-Day Guarantee, Stitch & fabric defects covered." Same drawer layout and Checkout button placement on mobile and desktop.

## Slot 6: Add color swatches to standard PDPs

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (standard catalog PDPs)
**Revenue potential:** [Sessions/mo unknown] x 0.5-1.5% CVR lift on affected SKUs x [AOV unknown] = revenue estimate not calculable without traffic/AOV data.

**Hypothesis:** If standard PDPs show color swatches alongside the size selector, conversion rate improves because shoppers currently can't see or select color variants on this page type at all.

**Data:** The collected PDP (Rev It Up T-shirt) offers only a size selector (XS-XXL) with no color/variant swatches. The three ad-linked PDPs (jersey, cargo pants, sporty pants) each show 3-5 color swatches alongside size. Source: site-visual-summary.md (PDP), meta-ads-visual-summary.md (Ads 1-3).

**V1:** Add color swatches next to the size selector on standard PDPs, matching the placement and style already used on ad-linked PDPs. On mobile, swatches sit in a horizontal row above the size selector; on desktop, side by side with size. Selecting a swatch updates the product image, same interaction pattern as the ad-linked pages.

## Slot 7: Add a sticky Add to Cart button on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (all PDPs)
**Revenue potential:** [Sessions/mo unknown] x 0.5-1.5% CVR lift x [AOV unknown] = revenue estimate not calculable without traffic/AOV data.

**Hypothesis:** If Add to Cart becomes sticky as the visitor scrolls past the buy box, conversion rate improves because shoppers currently have to scroll back up to purchase after reviewing product detail.

**Data:** Across all four PDPs observed (the standard PDP and all three ad-linked PDPs), Add to Cart sits inline within the buy box and does not become sticky as the visitor scrolls through fabric composition and style-highlight content in folds 2-3. Source: site-visual-summary.md (PDP, "CTA behavior"), meta-ads-visual-summary.md (all 3 ads, "LP CTA" notes).

**V1:** Add a fixed bottom bar with product thumbnail, price, and an Add to Cart button that appears once the visitor scrolls past the primary buy box. On mobile, full-width fixed bar at the bottom of the viewport. On desktop, a fixed bar spanning the content width. Bar disappears when the visitor scrolls back to the primary buy box.

## Slot 8: Test a starting-price anchor on homepage category tiles

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (category promo tiles)
**Revenue potential:** [Sessions/mo unknown] x lift not established, this is a lower-confidence test pending real collection-page data x [AOV unknown] = revenue estimate not calculable without traffic/AOV data.

**Hypothesis:** If homepage category tiles show a "Starting at ₹999" price anchor, click-through to product pages improves because shoppers currently see only lifestyle imagery and a "SHOP NOW" button with no price context before clicking in.

**Data:** The homepage's category tiles (BOTTOMS, T-SHIRTS, DRIFT 2.0) show large lifestyle imagery with a "Shop Now" button and no price shown. Source: site-visual-summary.md. Separately, Google Search and Shopping ads already use starting-price anchors not tested anywhere on Meta or on-site ("Starting At ₹999 Only," "View 3 prices from ₹299.00"). Source: google-ads-visual-summary.md. This slot combines a documented UI gap with a documented ad-side data point rather than a single audit finding, treat it as the lowest-confidence slot in this roadmap and revisit once a real collection/PLP page is collected.

**V1:** Add a "Starting at ₹999" price badge to each homepage category tile, in the lower corner of the tile image. Same badge placement and size across all tiles on mobile and desktop. No change to the tile imagery or "Shop Now" button.

## Future Slot Candidates

1. **Recollect an actual collection/PLP page** - The three "collection" screenshots on file show homepage-style category promo tiles, not a product-listing grid with cards, prices, or filters. No collection-page friction can be evaluated until this is recollected.
2. **Full evaluation of the cart drawer's cross-sell carousel** - The "You may also like" carousel in the cart drawer is only partially visible in the captured screenshot. A follow-up screenshot would allow AOV-mechanic testing once fully visible.
