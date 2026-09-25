# Swanson Vitamins Roadmap Seed

**Store:** https://www.swansonvitamins.com
**AOV:** Unknown (observed PDP/collection prices range $10.79-$55.49, PDP focus item at $23.19)
**Monthly sessions:** Unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, Reviews and UGC, PageSpeed / Core Web Vitals, Current Site Screenshots, Social and Community Research, Competitor Analysis (self-researched)

## Key Insights

The PDP's most aggressive competitive lever — a "40% off today" Subscribe to Save discount, more generous on paper than Puritan's Pride's 20% or Vitacost's 10% — shows no visible price difference. Both "Subscribe to Save" and "One-time purchase" display $23.19 on the Triple Magnesium Complex PDP, confirmed live on 2026-09-12. A shopper comparing the two boxes has no price signal to justify the pre-selected subscribe option.

Two of three active Meta ad campaigns route paid traffic into a dead end. Ad 2 (k2o) and Ad 3 (Mellow Magnesium) both promise "100% Money Back Guarantee" in the ad creative, but their landing pages are gated by an 18+ age-verification interstitial that blocks the product grid before it renders — confirmed live on 2026-09-12, matching the screenshot evidence of a near-blank fold 1 on both pages. Ad 1 (probiotics), which has no such gate, shows strong message match with its "science-backed," GMP-certified landing page. Site speed compounds the problem for traffic that does get through: PDP LCP is 12.2s and homepage LCP is 7.2s (Lighthouse, mobile, 2026-09-12), both roughly 3-5x Google's 2.5s "good" threshold, with TBT over 1.6s on each.

Reviews surface one recurring, fixable complaint: shoppers want the oxide/citrate/glycinate split spelled out. "Swanson should however list the percentages of each" (Jeffrey M., Jul 25, 2026); "I suspect this is mostly mag oxide which isn't absorbed" (1-star, Sep 5, 2026); "Not the best mix of Magnesium sources. Oxide has a ridiculously low bioavailability" (Charles R., Jun 12, 2026). At least one 3-star review traces directly to this gap: a shopper expected a cognitive-focused formula and got a blended one, writing "I should have done my own research instead of trusting the label" (Cecilia B., Sep 5, 2026).

## Top Test Opportunities

### 1. Fix Subscribe-vs-One-time price display on PDP
**What's broken:** On the Triple Magnesium Complex PDP, the buy box shows two stacked purchase options: a green-highlighted "Subscribe to Save" box (labeled "Best Value," pre-selected, showing "595+ have subscribed" and "40% off today") sitting above a plain "One-time purchase" option. Both display the identical price, $23.19. No strikethrough, compare-at price, or visible dollar/percent savings distinguishes the two, so the "40% off" claim has no corresponding visual proof at the decision point.
**Evidence:** site-visual-summary.md (PDP fold 1), live PDP verification (2026-09-12).
**Key data:** Both options at $23.19; competitor comparison shows Puritan's Pride (20% Subscribe & Save) and Vitacost (10% Autoship) both display visible discounts on their equivalent options.
**Est. lift:** Sessions/mo and baseline CR not collected; size against PDP traffic once available.

### 2. Remove or defer the age-verification gate on k2o and Mellow Magnesium landing pages
**What's broken:** Following the Ad 2 and Ad 3 Meta links lands on `/collections/brand-k2o` and `/collections/mellow-magnesium`, both of which show an interstitial requiring shoppers to confirm they are 18+ before any product grid, pricing, or the ad's promised money-back guarantee renders. Screenshot evidence shows fold 1 on both pages as nearly blank apart from one headline.
**Evidence:** meta-ads-visual-summary.md (Ad 2, Ad 3 fold 1), live verification (2026-09-12).
**Key data:** Ad 1 (no gate) shows full message match; Ad 2/Ad 3 (gated) show the guarantee claim missing or footer-only in captured folds.
**Est. lift:** Sessions/mo for these two campaigns not collected.

### 3. Compress PDP load time
**What's broken:** The Triple Magnesium Complex PDP takes 12.2s to reach Largest Contentful Paint on mobile, with 1,630ms of Total Blocking Time — the page loads the buy box and Add to Cart button this slowly for both paid and organic shoppers.
**Evidence:** raw pagespeed JSON, `swanson vitamins -pdp-pagespeed.json` (2026-09-12).
**Key data:** LCP 12.2s vs. Google's 2.5s "good" threshold; Performance score 0.37/1.0; CLS is 0 (not a layout problem).
**Est. lift:** Sessions/mo not collected.

### 4. Compress homepage load time
**What's broken:** The homepage takes 7.2s to LCP on mobile with 1,750ms TBT, delaying the hero "Shop Stacks" CTA and trust-badge row from becoming usable.
**Evidence:** raw pagespeed JSON, `swanson-pagespeed-homepage.json` (2026-09-12).
**Key data:** LCP 7.2s vs. 2.5s threshold; Performance score 0.33/1.0.
**Est. lift:** Sessions/mo not collected.

### 5. Add ingredient-ratio breakdown to Triple Magnesium Complex PDP
**What's broken:** The Supplement Facts accordion on the PDP shows a single combined figure (Magnesium 400mg, 95% DV) with no split between the oxide, citrate, and glycinate sources named in the product title. Product copy in fold 3 explains the three-source formulation in prose but never states the per-compound ratio.
**Evidence:** raw/reviews.md (3+ reviews requesting this), site-visual-summary.md (Supplement Facts panel, fold 3).
**Key data:** Direct quote: "Swanson should however list the percentages of each" (Jeffrey M., Jul 25, 2026).
**Est. lift:** Sessions/mo and return/complaint baseline not collected; expected to reduce mismatch-driven negative reviews more than lift raw CR.

### 6. Move PDP trust/certification badges adjacent to the buy box
**What's broken:** The row of 7 certification icons (Gluten Free, Non-GMO, Vegan, Halal, Dairy Free, third-party-tested, Money-Back Guarantee) sits directly below the product image gallery, separated from the price and purchase-option boxes by the full image column width.
**Evidence:** site-visual-summary.md (PDP fold 1 layout).
**Key data:** Star rating (4.5, 1,589 reviews) already sits correctly above the buy box; certification badges do not.
**Est. lift:** Sessions/mo not collected.

### 7. Surface homepage trust badges above the fold
**What's broken:** The homepage hero (fold 1) shows only the staff-picks headline and "Shop Stacks" CTA with no trust signal. The 500K+ Reviews, 750+ 3rd-Party Tested, and 100% Money-Back Guarantee badges appear only in fold 2.
**Evidence:** site-visual-summary.md (homepage fold 1 vs. fold 2).
**Key data:** Live-verified homepage also cites "4.3 stars from 37,346 reviews via Trustpilot" (2026-09-12), currently placed below the fold.
**Est. lift:** Sessions/mo not collected.

### 8. Carry PDP cross-sell into the cart drawer
**What's broken:** The cart drawer's only AOV mechanic is a green progress bar reading "You're only $25.81 away from free shipping," with no product suggestions shown. The PDP's "Frequently Purchased Together" row (Mellow Magnesium Variety Pack, Vitamin D3 5,000IU, C-1000 Vitamin C, Zinc Picolinate) does not carry into the cart.
**Evidence:** site-visual-summary.md (PDP fold 2, cart drawer).
**Key data:** Free-shipping gap of $25.81 on a $23.19 line item; four adjacent SKUs already surfaced on the PDP go unused in the cart.
**Est. lift:** Sessions/mo not collected; AOV reference ~$23-55 based on observed prices.

## Unused Findings

- Google Ads (24 units reviewed) use discount-code and testimonial-video messaging inconsistent with Meta's guarantee-led angle — a message-consistency issue better measured on assisted-conversion than direct CR.
- The "Shop Stacks" staff-picks page has no filter/sort controls across all three captured folds, limiting it as a category-browsing entry point.
- Ad 3's four landing-page products each carry only 1 review despite a 5-star rating — a thin proof signal for paid-social traffic.
