# Labareau CRO Research Brief

**Data Sources:** Meta Ads, Google Ads, Reviews & UGC, PageSpeed/CWV, Non-Data Context, Site Screenshots, Social Research (last30days-ecom), Competitor Analysis (self-researched)

September's dip is not a conversion problem. Site CR held at a stable 2.5%, matching pre-giveaway performance, and AOV rose slightly. The hit is on the buy side: CTR dropped 36% and CPC rose 43% post-giveaway, producing a 27% revenue-per-click decline, €14.49 to €10.56 (25-31 Aug vs. 1-4 Sept). Source: Non-Data Context.

The brand's own #2 priority, landing pages matching the ad clicked, is the strongest lever available. Of three Meta ads audited, only Ad 2 (collagen and Matrixyl claims landing on The Rich Cream PDP, whose benefit list echoes those terms) delivers message match. Ad 1's 14% bundle offer isn't visible above the fold on its landing PDP. Ad 3 promises a "perfect anti-aging product" narrative but lands on a quiz interstitial with no product, price, or restated claim. Source: Meta Ads visual summary.

Discount dependency compounds the problem. Discount share of gross revenue climbed from 12% to 20.5% while volume halved, and reviews confirm customers expect it: "I hope there are some discounts like other companies so that we can always buy" (Hasna Qatto). Source: Reviews & UGC. Ad 1 leads with a 14% discount, reinforcing the exact pattern the brand wants to break.

The PDP is also a technical ceiling. The Rich Cream scores 38/100 mobile Lighthouse with a 19.7s LCP, against 52/100 and 5.2s on the homepage. Source: PageSpeed/CWV. Two of three Meta ads route directly to PDP templates, meaning paid traffic is landing on the slowest page on the site before any message-match or offer test can be judged fairly.

Revenue opportunity: not quantifiable this cycle. Sessions/mo and AOV were not collected (Source: Non-Data Context), so dollar-value lift cannot be calculated. The one available benchmark is the brand's own: "one extra euro per click shows up immediately" at current volume. Source: Non-Data Context.

---

## Slot 1: Fix PDP Load Speed

**Type:** Immediate Fix
**Page:** Product Detail Page, The Rich Cream (Ad 2's landing destination)

The Rich Cream PDP scores 38/100 mobile Lighthouse with a 19.7s LCP, roughly 4x Google's "poor" threshold (2.5s), against 52/100 and 5.2s on the homepage. Source: PageSpeed/CWV (Lighthouse, fetched 2026-09-11). Two of three Meta ads land directly on PDP templates, so this is not a hypothesis to test, it is a technical failure capping every other test on the page. Fix before running Slots 2 or 3, since a buy-box or message-match variation can't be judged fairly against a control that abandons before paint.

---

## Slot 2: Restate Ad 3's Claims on Its Landing Destination

**Type:** A/B test (1 variation vs. control)
**Page:** Ad 3 Landing Page, Skin Quiz Interstitial
**Revenue potential:** data unavailable, sessions/mo and Ad 3-specific traffic split were not collected.

**Hypothesis:** If we restate Ad 3's specific claims (huidbarrière, fijne lijntjes) and show the product it's selling on the landing interstitial, more Ad 3 clickers will continue into the funnel because the current page shows zero connection to what the ad promised.

**Data:** Ad 3 promotes a "perfect anti-aging product" discovery narrative with specific claims, then lands on a single-fold, dark-maroon quiz interstitial: five quiz-answer buttons, a "20+ jaar klinische ervaring" panel, and a "Shop LABAREAU" text link, no product, price, or restated claim anywhere. Source: Meta Ads visual summary (Ad 3). This is the brand's own named priority for the cycle. Source: Non-Data Context, Priority #2.

**V1:** Add a hero strip above the quiz that restates the ad's specific claim (huidbarrière, fijne lijntjes) with a small product thumbnail, price, and a real button in place of the current text link. The quiz itself stays unchanged below it. Mobile: hero strip stacks above the quiz options, full width. Desktop: hero strip sits above the fold, quiz options remain below. (KB: resources/kb/presell-page-structure.md)

---

## Slot 3: Move Ad 1's Bundle Offer Above the Fold

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page, The Toner (Ad 1's landing destination)
**Revenue potential:** data unavailable, no baseline conversion rate split by ad.

**Hypothesis:** If the "AHA Peel & The Toner, 14% korting" bundle becomes the default buy-box selection above the fold, more Ad 1 clickers will convert because the current PDP opens on a single-unit €49,00 buy box, and the matching bundle only appears in fold 2 with different styling than the ad's offer language.

**Data:** Ad 1 promotes a specific bundle with a 14% discount; its landing PDP doesn't surface that offer until shoppers scroll past the single-unit buy box, and the bundle tile that does appear doesn't echo the ad's headline framing. Source: Meta Ads visual summary (Ad 1).

**V1:** Replace the default above-the-fold buy box with the bundle pre-selected, showing bundle contents and a "14% korting" badge that matches the ad's exact headline wording. The single-unit option remains available as a secondary choice below it. Mobile: bundle card sits directly under the product title and images, before any scroll. Desktop: bundle occupies the primary buy-box position beside the image gallery. (KB: resources/kb/pdp-structure.md)

---

## Slot 4: Fixed Evergreen Offer vs. Recurring Discount Mechanic

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** data unavailable, no sessions/mo baseline; brand's own estimate is "one extra euro per click shows up immediately" at current volume.

**Hypothesis:** If the homepage banner runs a fixed, non-expiring gift-at-€100 offer instead of rotating percentage-discount messaging, revenue-per-click will hold or improve because discount share of gross revenue has climbed from 12% to 20.5% of revenue while volume halved, and customers already associate the brand with discounts they wait for.

**Data:** Discount share of gross revenue rose from 12% to 20.5% while volume halved. Source: Non-Data Context, Priority #1. Reviews independently confirm discount expectation: "I hope there are some discounts like other companies so that we can always buy" (Hasna Qatto); "a bit pricey unfortunately" (Val Markou, 4★). Source: Reviews & UGC.

**V1:** Replace the rotating percentage-discount banner with a static gift-at-€100 threshold banner, no percentage-off copy anywhere on the homepage. Mobile: single banner strip below the top nav. Desktop: same banner spanning the full width above the hero. (KB: resources/kb/cold-friendly-offer-positioning.md)

---

## Slot 5: Add Review Counts to Collection Cards

**Type:** A/B test (1 variation vs. control)
**Page:** Collection, "Alle Producten" grid
**Revenue potential:** data unavailable.

**Hypothesis:** If every collection card shows a printed review count next to its star rating, shoppers comparing products will trust the ratings more, because the homepage and PDP already show printed counts (1141, 2382) and the collection grid is the only funnel step showing stars with no count.

**Data:** The "Alle Producten" grid (24 products) shows visual-only star rows with no printed count, while homepage tiles and the PDP both show printed counts. Source: Site Screenshots.

**V1:** Add a printed count in parentheses next to the star row on every card, in the same format already used on the homepage and PDP. Mobile: 2-column grid, count sits directly under the stars. Desktop: count sits in the same position within the existing card layout.

---

## Slot 6: Add Trust Copy to the Cart Drawer

**Type:** A/B test (1 variation vs. control)
**Page:** Cart (drawer)
**Revenue potential:** data unavailable.

**Hypothesis:** If the cart drawer adds a short guarantee, returns, and shipping-time line, checkout intent will increase because the drawer's only current trust signal is a row of payment icons under the checkout button.

**Data:** The cart drawer shows two line items, a free-sample module, checkout, and payment icons, no guarantee, returns, or shipping-time copy anywhere in the capture. Source: Site Screenshots (Cart section).

**V1:** Add a one-line trust bar between the free-sample module and the checkout button, stating the return window and shipping estimate from existing site policy. Mobile: single line above the checkout button. Desktop: same placement, full cart-drawer width. (KB: resources/kb/cro-system.md)

---

## Slot 7: Reinforce the Doctor-Authority Claim

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** data unavailable.

**Hypothesis:** If the homepage's generic "Recommended by doctors" line becomes a specific, comparable proof point matching Google's "Aangeraden Door Artsen" claim, trust will increase because the homepage version currently carries no supporting detail while a stronger, unused version of the same claim is already live in Google Ads.

**Data:** Google Ads runs "Aangeraden Door Artsen" with a 4-star/168-review badge; the homepage shows only a generic "Recommended by doctors" checkmark with no supporting detail. Source: Google Ads visual summary. Competitor research shows Augustinus Bader and Dr. Barbara Sturm run the same doctor-created positioning at 2-3x Labareau's price (Bader's "Rich Cream" ~€265/50ml vs. Labareau's €119). Source: Competitor Analysis.

**V1:** Replace the "Recommended by doctors" checkmark line with a badge module showing the 4-star/168-review detail already used in Google Ads, placed next to the existing Trustpilot rating. Mobile: stacked badge row under the hero headline. Desktop: same row, beside the Trustpilot badge. (KB: resources/kb/cold-friendly-offer-positioning.md)

---

## Slot 8: Surface Newsletter Signup Earlier in the Funnel

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** data unavailable.

**Hypothesis:** If a promo-alert newsletter signup module appears on the homepage, signups will increase because Labareau's own review reply already directs customers to the newsletter for promotions, yet no signup module appears anywhere in the captured homepage, collection, or cart funnel.

**Data:** Labareau's reply to a customer review reads "keep an eye on our newsletter as we always announce promotions there first," but no newsletter signup is visible in any captured homepage, collection, or cart screenshot. Source: Reviews & UGC; Site Screenshots.

**V1:** Add a signup strip (email field plus submit) between the hero and the product grid, framed around promo-alert access rather than a generic "join our newsletter." Mobile: full-width strip. Desktop: same strip, centered.

---

## Future Slot Candidates

1. **Test a refill or smaller-format SKU against the price objection** - the only recurring product complaint pairs price with short shelf life once opened ("the products only last for six months once opened," Karima), suggesting a cost-per-use gap rather than pure price resistance.
2. **Standardize PDP accordion language to Dutch** - Ad 2's landing page (The Rich Cream PDP, fold 3) shows four benefit tiles in English inside an otherwise all-Dutch page, a language-consistency break on the site's strongest message-match template.
