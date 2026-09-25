# Swanson Vitamins CRO Research Brief

**Data Sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews and UGC, PageSpeed / Core Web Vitals, Current Site Screenshots, Social and Community Research, Competitor Analysis (self-researched)

Swanson's most aggressive competitive lever is invisible at the point of purchase. The Triple Magnesium Complex PDP pre-selects "Subscribe to Save" with a "40% off today" claim, more generous on paper than Puritan's Pride's 20% Subscribe & Save or Vitacost's 10% Autoship. But both purchase options show the identical $23.19, confirmed live on 2026-09-12. A shopper comparing the two boxes has no price signal to justify picking the pre-selected, higher-margin option over one-time purchase.

Paid traffic is losing customers before they see a product. Two of three active Meta campaigns (Ad 2: k2o, Ad 3: Mellow Magnesium) promise "100% Money Back Guarantee" in the ad creative, then route clicks into an 18+ age-verification gate that blocks the entire product grid and hides that same guarantee claim. Only Ad 1 (probiotics), which carries no gate, shows full message match with its landing page. Traffic that does get through then hits a slow site: PDP LCP is 12.2s and homepage LCP is 7.2s (Lighthouse, mobile, 2026-09-12), 3-5x Google's 2.5s "good" threshold, with Total Blocking Time over 1.6 seconds on both pages.

Reviews point to one specific, fixable gap. Three of 22 reviews on the Triple Magnesium Complex PDP ask for the oxide/citrate/glycinate split behind the single combined "400mg, 95% DV" figure: "Swanson should however list the percentages of each" (Jeffrey M., Jul 25, 2026); "I suspect this is mostly mag oxide which isn't absorbed" (1-star, Sep 5, 2026); "Not the best mix of Magnesium sources. Oxide has a ridiculously low bioavailability" (Charles R., Jun 12, 2026). At least one 3-star review traces directly to this gap, a shopper who wanted a cognitive-focused formula and got a blended one: "I should have done my own research instead of trusting the label" (Cecilia B., Sep 5, 2026).

Sessions/month and baseline conversion rate were not provided for any page in this collection, so no dollar-value revenue estimate can be calculated yet. Every slot below is prioritized by data support and directional opportunity size instead: the pricing and paid-traffic fixes come first because they sit directly in front of active purchase decisions and live ad spend, not because a specific dollar figure was modeled.

## Slot 1: Remove the Age-Verification Gate on Non-Restricted Collections

**Type:** Immediate Fix
**Page:** k2o Hydration and Mellow Magnesium landing pages (`/collections/brand-k2o`, `/collections/mellow-magnesium`)

**What's broken:** Both pages sit behind an 18+ age-verification interstitial that blocks the product grid, pricing, and the "100% Money Back Guarantee" claim from rendering at all. Neither product line (an electrolyte hydration mix and a magnesium supplement) is an age-restricted category. This matches the screenshot evidence of a near-blank fold 1 on both pages, live-verified 2026-09-12.

**Data:** Confirmed live on both URLs (2026-09-12). Ad 1 (probiotics), which carries no such gate, shows strong message match with its landing page and a full product grid on load. Ad 2 and Ad 3 both lead with the guarantee claim in the ad creative, and that claim does not appear before the gate on either page.

**Fix:** Remove the age-verification gate from the k2o and Mellow Magnesium collections so paid traffic reaches the product grid and guarantee messaging immediately, matching the Ad 1 experience. No variation to test: this is blocking content the ad already paid to show.

## Slot 2: Fix Subscribe-vs-One-Time Price Display on PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page, Triple Magnesium Complex (`/products/triple-magnesium-complex`)
**Revenue potential:** data unavailable, sessions/mo and baseline CR for this PDP were not collected. AOV reference point: $23.19 observed unit price.

**Hypothesis:** If the Subscribe to Save box shows a struck-through regular price alongside the discounted price, more shoppers will keep the pre-selected subscribe option because the "40% off today" claim will finally have a visible number behind it.

**Data:** Both "Subscribe to Save" (labeled "Best Value," pre-selected, "595+ have subscribed," "40% off today") and "One-time purchase" display the identical $23.19, confirmed live on 2026-09-12. No strikethrough or compare-at price distinguishes the two. Puritan's Pride (20% Subscribe & Save) and Vitacost (10% Autoship) both show a visible discount on their equivalent options.

**V1:** Add a struck-through "regular price" above the current $23.19 on the Subscribe to Save box, with the dollar amount saved shown next to it (e.g. "$38.65 ~~$23.19~~, save $15.46"). One-time purchase keeps its plain $23.19 with no strikethrough. Mobile: boxes stay stacked as they are now, with the new price line sitting directly under "40% off today." Desktop: same layout, price line sits in the same position within the wider box. (KB: resources/kb/pdp-structure.md — subscription option should be made "genuinely sexier" than one-time via visible value, not just pre-selection.)

## Slot 3: Compress PDP Load Time

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page, Triple Magnesium Complex (`/products/triple-magnesium-complex`)
**Revenue potential:** data unavailable, sessions/mo for PDP traffic were not collected. AOV reference point: $23.19.

**Hypothesis:** If the PDP's hero product image is served at optimized, responsive sizes and non-critical third-party scripts are deferred until after first paint, Largest Contentful Paint will drop toward Google's 2.5s threshold because the current 12.2s LCP and 1,630ms TBT indicate both an oversized hero asset and blocking script execution, not a layout problem (CLS is 0).

**Data:** Lighthouse (mobile, 2026-09-12): PDP performance score 0.37/1.0, LCP 12.2s (roughly 5x the 2.5s "good" threshold), TBT 1,630ms, CLS 0.

**V1:** Serve the product gallery's hero image in compressed, responsive formats with the LCP image preloaded, and defer non-critical scripts (reviews widget, chat) until after the buy box renders. No visible content, copy, or layout changes on mobile or desktop.

## Slot 4: Compress Homepage Load Time

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (`/`)
**Revenue potential:** data unavailable, sessions/mo for the homepage were not collected.

**Hypothesis:** If the homepage's hero image is served at optimized, responsive sizes and non-critical scripts are deferred, Largest Contentful Paint will drop toward Google's 2.5s threshold because the current 7.2s LCP and 1,750ms TBT are delaying the "Shop Stacks" CTA and trust badges from becoming usable, with CLS at 0 ruling out a layout cause.

**Data:** Lighthouse (mobile, 2026-09-12): homepage performance score 0.33/1.0, LCP 7.2s, TBT 1,750ms, CLS 0.

**V1:** Serve the hero banner image in compressed, responsive formats with the LCP image preloaded, and defer non-critical below-fold scripts until after the hero and CTA render. No visible content, copy, or layout changes on mobile or desktop.

## Slot 5: Add Ingredient-Ratio Breakdown to Triple Magnesium Complex PDP

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page, Triple Magnesium Complex (`/products/triple-magnesium-complex`)
**Revenue potential:** data unavailable, sessions/mo and baseline return/complaint rate were not collected. Expected to reduce mismatch-driven negative reviews more than lift raw CR.

**Hypothesis:** If the Supplement Facts panel shows the milligram or percentage split between magnesium oxide, citrate, and glycinate, fewer shoppers will buy expecting a single-purpose formula and leave a mismatch complaint, because the current panel shows only a combined "Magnesium 400mg, 95% DV" with no split.

**Data:** At least 3 of 22 reviews ask for or complain about the missing split: "Swanson should however list the percentages of each" (Jeffrey M., Jul 25, 2026); "I suspect this is mostly mag oxide which isn't absorbed" (1-star, Sep 5, 2026); "Not the best mix of Magnesium sources. Oxide has a ridiculously low bioavailability" (Charles R., Jun 12, 2026). One 3-star review traces a purchase mismatch directly to this gap (Cecilia B., Sep 5, 2026).

**V1:** Add a per-compound breakdown line (milligrams or percentage of the 400mg total for oxide, citrate, and glycinate) beneath the existing combined total in the Supplement Facts accordion, on both mobile and desktop. No other panel content changes.

## Slot 6: Move Trust and Certification Badges Next to the Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page, Triple Magnesium Complex (`/products/triple-magnesium-complex`)
**Revenue potential:** data unavailable, sessions/mo for PDP traffic were not collected.

**Hypothesis:** If the 7 certification badges (Gluten Free, Non-GMO, Vegan, Halal, Dairy Free, third-party-tested, Money-Back Guarantee) move from below the image gallery to directly under the buy box, more shoppers will see them before deciding, because they currently sit a full image-column width away from the price and purchase options.

**Data:** Site screenshots (PDP fold 1) show the star rating (4.5, 1,589 reviews) already placed correctly above the buy box, while the certification badge row sits below the image gallery, separated from price and purchase options by the full image column.

**V1:** Move the certification badge row to sit directly beneath the purchase options and Add to Cart button, in place of its current position below the image gallery. Mobile: badges display as a horizontal scrollable row. Desktop: badges display as a single row spanning the buy box width. (KB: resources/kb/pdp-structure.md — top-of-page order puts store benefits and trust badges beside the buy box, not separated by the image column.)

## Slot 7: Surface Homepage Trust Badges Above the Fold

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (`/`)
**Revenue potential:** data unavailable, sessions/mo for the homepage were not collected.

**Hypothesis:** If the 500K+ Reviews, 750+ 3rd-Party Tested, and 100% Money-Back Guarantee badges move into fold 1, fewer shoppers who don't scroll past the hero will leave with zero trust signal, because those badges currently appear only in fold 2.

**Data:** Site screenshots show the homepage hero (fold 1) carries only the staff-picks headline and "Shop Stacks" CTA, with the three trust badges appearing in fold 2. Live verification (2026-09-12) confirms the homepage also cites "4.3 stars from 37,346 reviews via Trustpilot," currently placed below the fold.

**V1:** Duplicate the three fold-2 trust badges into fold 1, placed beneath the "Shop Stacks" CTA. Mobile: badges stack in a single compact row under the CTA. Desktop: badges sit beside or beneath the headline, next to the CTA. Fold 2 badges remain unchanged.

## Slot 8: Carry PDP Cross-Sell Into the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer
**Revenue potential:** data unavailable, sessions/mo and cart-stage baseline CR were not collected. AOV reference point: $23-55 based on observed PDP and collection pricing.

**Hypothesis:** If the cart drawer shows product suggestions alongside its free-shipping progress bar, more shoppers will add a second item to close the shipping-threshold gap, because the drawer's only current AOV mechanic is a bar reading "You're only $25.81 away from free shipping" with no product suggestion attached to it.

**Data:** Cart drawer screenshot shows the free-shipping progress bar as the sole AOV mechanic. The PDP's "Frequently Purchased Together" row (Mellow Magnesium Variety Pack, Vitamin D3 5,000IU, C-1000 Vitamin C, Zinc Picolinate) does not carry into the cart drawer.

**V1:** Add the PDP's "Frequently Purchased Together" products beneath the existing free-shipping progress bar in the cart drawer. Mobile: products display as a horizontal scroll row. Desktop: products display as inline cards. The free-shipping bar keeps its current position and copy.

## Future Slot Candidates

1. **Unify guarantee/value messaging across Google and Meta ad creative** - Meta ads lead with a specific "100% Money-Back Guarantee" on 2 of 3 creatives, while the Google Ads set (24 units reviewed) leans on rotating discount codes and broad category messaging with no consistent guarantee callout, a message-consistency gap best measured on assisted-conversion rather than direct CR.
2. **Add filter/sort controls to the "Shop Stacks" staff-picks page** - The page the homepage's main CTA leads to has no filter or sort controls across all three captured folds, giving a shopper with a specific need (e.g. "protein," "sleep") no way to narrow results from this entry point.
3. **Reduce Ad 3 (Mellow Magnesium) SKU social-proof gap** - Ad 3's four landing-page products each show only 1 review despite a 5-star rating, a thin proof signal for a $22.99-$24.99 impulse-adjacent purchase reached via paid social.
