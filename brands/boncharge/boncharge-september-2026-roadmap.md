# Bon Charge CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed/Core Web Vitals, Current Site Screenshots (homepage, collection, cart), Social & Community Research, live WebFetch re-verification (2026-09-12), competitor WebSearch

## Insights

Live re-verification on 2026-09-12 found all three active Meta ad landing pages sold out: Tortoise Shell Computer Glasses, Crystal Computer Glasses, and the Red Light Face Mask. Every dollar of live Meta ad spend is currently driving clicks into a dead end. The Red Light Face Mask page compounds this: it shows "Sold out" while its own buy-box copy still reads "In Stock | Limited Quantities Available" — both messages live on the same page at once (Source: meta-ads-visual-summary.md, live WebFetch re-check).

Ads 1 and 2 promise "the full BON CHARGE wellness collection" but land on a single eye-strain SKU, with no mention of the specific product shown or the 25% sitewide discount live on the page at the time of collection (Source: meta-ads-visual-summary.md). This is a message-match gap on top of the stock issue: even once inventory is fixed, the ad-to-page story does not connect.

Site performance is severely broken on the two pages most likely to receive paid traffic. Real Lighthouse data pulled 2026-09-12 shows the homepage scoring 0.16 (LCP 14.7s, TBT 3,410ms, TTI 44.1s) and the PDP scoring 0.32 (LCP 13.2s, TTI 48.0s) — both 3-4x past Google's "poor" threshold (Source: raw/pagespeed.md, real Lighthouse JSON).

A currency display bug recurs on three separate surfaces: the homepage banner shows "$125" free shipping while the PDP and ad landing pages show "€115," and the cart prices one upsell line item in USD ($356.21) against an otherwise EUR cart (Source: site-visual-summary.md, live WebFetch re-check). This is a systemic geo/currency bug, not a single screenshot artifact, and it hits checkout trust directly.

Sessions/mo and AOV were not provided for Bon Charge, so dollar-impact estimates below are qualitative, not calculated. The math that matters most here is simpler: 3 of 3 tracked Meta ad creatives currently cannot convert at all.

## Slot 1: Fix Contradictory Stock Status on Ad-Driven Landing Pages

**Type:** Immediate Fix
**Page:** Ad landing pages / PDP (Tortoise Shell Computer Glasses, Crystal Computer Glasses, Red Light Face Mask)

**What's broken:** All three actively running Meta ad creatives point to sold-out PDPs, live-verified 2026-09-12 (Source: meta-ads-visual-summary.md, live WebFetch re-check). The Red Light Face Mask page shows "Sold out" while the buy-box copy directly above it still reads "In Stock | Limited Quantities Available" — both messages rendering at once.

**Why this is the priority:** 3 of 3 active Meta creatives are driving spend into either a fully blocked purchase path or a page that contradicts itself about whether the product can be bought. This affects 100% of tracked Meta ad traffic while the ads remain active.

**Fix:** Pause ad spend on any SKU that is out of stock until inventory is restored, or restock the SKUs directly. On the Red Light Face Mask PDP specifically, remove the "In Stock | Limited Quantities Available" line the moment stock hits zero, or replace the buy box with a back-in-stock notification form so the two contradicting messages never render together. Apply the same logic on mobile and desktop.

## Slot 2: Fix the Currency Display Bug

**Type:** Immediate Fix
**Page:** Homepage, PDP / ad landing pages, Cart

**What's broken:** The homepage free-shipping banner reads "Free Shipping on Orders Over $125," while the identical banner on PDP and ad landing pages reads "Free Shipping on Orders Over €115" (Source: site-visual-summary.md, live WebFetch re-check, 2026-09-12). In the cart drawer, the main line item prices in EUR while the upsell module below it shows "$356.21" in USD. The mismatch recurs on three separate surfaces, which points to a geo/currency-detection bug rather than an isolated capture issue.

**Why this is the priority:** Inconsistent currency across the homepage, product pages, and cart undermines checkout trust on every session, regardless of traffic source or volume.

**Fix:** Audit the geo/currency-detection logic across the homepage banner, PDP/landing page banner, and cart line items so all three read the same currency for the same shopper session. Verify the fix on both mobile and desktop, and re-check the Face, Neck and Chest Bundle discount figure while in this area, since the seed also flagged an unreconciled "30% off" vs. "7% savings" discrepancy on that same bundle (Source: raw/site-visual-summary.md; verify directly before citing either figure).

## Slot 3: Bridge the Ad-to-Landing Message Match Gap on Glasses Ads

**Type:** A/B test (1 variation vs. control)
**Page:** Landing page / PDP (Tortoise Shell Computer Glasses, Crystal Computer Glasses)
**Revenue potential:** Sessions/mo and AOV were not provided, so a dollar figure cannot be calculated. Both Ads 1 and 2 currently send 100% of their clicks to a page with none of the ad's stated framing, which caps how much of that traffic can convert regardless of volume.

**Hypothesis:** If we add above-the-fold copy that names the exact product shown and restates the 25% sitewide discount already live on the page, bounce rate will drop because visitors currently land on a single-SKU page with none of the "full wellness collection" messaging or discount mention promised in the ad.

**Data:** Ads 1 (Tortoise Shell Computer Glasses) and 2 (Crystal Computer Glasses) both use the headline "Enhance your wellbeing. Shop the full BON CHARGE wellness collection and start thriving today," but land on a single-SKU, eye-strain-only PDP. Neither the specific product nor the 25% sitewide discount live on the page is mentioned in the ad (Source: meta-ads-visual-summary.md, Ads 1 & 2).

**V1:** Add a headline block directly under the existing hero image that names the specific glasses shown in the ad (e.g. "Tortoise Shell Computer Glasses") and restates the live discount ("25% off sitewide"). Keep the rest of the page and buy box unchanged. On mobile, this block sits full-width above the existing product title; on desktop, it sits in the same position, scaled to the existing content width.

## Slot 4: Replace Autoplay Video with Static Imagery to Cut Load Weight

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage and PDP (both carry the same autoplay-video weight problem)
**Revenue potential:** Sessions/mo and AOV were not provided, so a dollar figure cannot be calculated. Both pages fail Google's "poor" performance threshold by 3-4x, which caps conversion on all traffic hitting either page regardless of volume.

**Hypothesis:** If we replace the homepage's autoplaying hero and testimonial videos, and defer the PDP's 4-clip video testimonial grid until after initial page render, LCP and TBT will drop and conversion will increase because real Lighthouse data shows both pages failing Google's "poor" threshold by a wide margin.

**Data:** Homepage scores 0.16 (LCP 14.7s, CLS 0.234, TBT 3,410ms, TTI 44.1s); PDP scores 0.32 (LCP 13.2s, TBT 900ms, TTI 48.0s) (Source: raw/pagespeed.md, real Lighthouse JSON, 2026-09-12). Both exceed Google's 4-second "poor" LCP threshold by roughly 3-4x. The homepage hero is a full-width autoplaying video with a second autoplaying testimonial video in fold 3; the PDP carries a 4-clip video testimonial grid (Source: site-visual-summary.md).

**V1:** On the homepage, replace the autoplaying hero video with a static hero image carrying the same headline and CTA, and replace the fold-3 autoplaying testimonial video with a static testimonial image or text quote. On the PDP, keep the video testimonial grid but lazy-load it so it only loads once the shopper scrolls near it, instead of on initial page load. Apply on both mobile and desktop; the goal is unchanged layout and copy, only deferred or removed video weight.

## Slot 5: Add a Sticky CTA Bar to the Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** Sessions/mo and AOV were not provided, so a dollar figure cannot be calculated. This affects every homepage session, since the homepage is the entry point and currently has no persistent path to purchase.

**Hypothesis:** If we add a sticky CTA bar to the homepage, click-through to product and collection pages will increase because the homepage's only CTA today is a single non-sticky "Shop Best Sellers" button, while both the PDP and Ad 3's landing page already carry a persistent sticky Add to Cart bar on every fold.

**Data:** The homepage has no sticky header or CTA across its three collected folds; its only call to action is one non-sticky red "Shop Best Sellers" button in the hero. The PDP and Ad 3's landing page both carry a persistent sticky bar (product, price, Add to Cart) visible on every fold (Source: site-visual-summary.md, homepage vs. PDP/LP CTA comparison).

**V1:** Add a sticky bar that appears after the shopper scrolls past the hero, containing a "Shop Best Sellers" CTA that links to the same destination as the existing hero button. On mobile, the bar sits fixed to the bottom of the viewport; on desktop, it sits fixed to the top, below the existing site header. No other homepage content changes.

## Slot 6: Add a Guarantee Badge to the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart
**Revenue potential:** Sessions/mo and AOV were not provided, so a dollar figure cannot be calculated. This affects every session that opens the cart drawer, the last on-site step before checkout.

**Hypothesis:** If we add the same "30-Day Easy Returns · 1-Year Warranty" badge shown on the PDP to the cart drawer, checkout progression will increase because the cart currently shows only a free-shipping banner with no guarantee, returns, or warranty reassurance at the point closest to purchase (KB: resources/kb/cro-system.md).

**Data:** The cart drawer shows a free-shipping banner, the line item, an upsell module, and a "Checkout Securely" button, with no guarantee, returns, or warranty badge anywhere in the drawer. The PDP, by contrast, shows "30-Day Easy Returns · 1-Year Warranty" directly beneath its own Add to Cart button (Source: site-visual-summary.md, Cart section).

**V1:** Add a single-line trust badge ("30-Day Easy Returns · 1-Year Warranty") directly above the "Checkout Securely" button in the cart drawer, matching the copy already used on the PDP. No other cart content or layout changes. On mobile, the badge sits full-width above the checkout button; on desktop, it sits in the same position within the existing drawer width.

## Future Slot Candidates

1. **Investigate Google Ads Transparency 500-error units** - Multiple ad units across a 30+-unit set (glasses, face mask, toothbrush, hair-growth) render "500. That's an error" instead of creative in the Transparency Center. Given the confirmed OOS pattern found on Meta's landing pages, this needs a live click-through of the specific units' actual destinations before it can be scoped as a fix or test.
2. **Reconcile the Trustpilot domain split** - boncharge.com shows a 2.4 TrustScore from 6 reviews, while the legacy blublox.com domain carries 4 stars from 1,400+ reviews. A prospect searching independently is more likely to land on the low-scoring result first. This is a reputation/domain-consolidation question, not a directly testable on-site mechanic.
3. **Confirm the Ad 2 fold-3 product mismatch** - The collected screenshot for Ad 2's landing page fold 3 shows the Tortoise Shell Computer Glasses page instead of the Crystal Computer Glasses shown in folds 1-2 of the same ad. This may be a capture-time issue rather than live site behavior; needs a live click-through of Ad 2's current landing URL before treating it as a bug.
