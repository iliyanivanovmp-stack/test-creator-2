# LABAREAU Roadmap Seed

**Store:** https://labareau.nl
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads, Google Ads, Reviews & UGC, PageSpeed/CWV, Non-Data Context, Site Screenshots, Social Research (last30days-ecom), Competitor Analysis (self-researched)

## Key Insights

September's dip is not a conversion problem — site CR held at a stable 2.5%, matching pre-giveaway performance, and AOV rose slightly. The hit is on the buy side: CTR dropped 36%, CPC rose 43% post-giveaway, producing a 27% revenue-per-click decline (€14.49 to €10.56, 25-31 Aug vs. 1-4 Sept). The brand's #2 priority — landing pages matching the ad clicked — is the strongest lever: of three Meta ads audited, only Ad 2 (collagen/Matrixyl claims landing on The Rich Cream PDP, whose benefit list echoes those terms) delivers message match. Ad 1's 14% bundle offer isn't visible above the fold on its landing PDP. Ad 3 promises a "perfect anti-aging product" narrative but lands on a quiz interstitial with no product, price, or restated claim.

Discount dependency compounds this: discount share of gross revenue climbed from 12% to 20.5% while volume halved, and reviews confirm customers expect it — "I hope there are some discounts like other companies" (Hasna Qatto), "a bit pricey unfortunately" (Val Markou, 4★). Ad 1 leads with a 14% discount, reinforcing the pattern the brand wants to break.

The PDP is also a technical ceiling: 38/100 mobile Lighthouse, 19.7s LCP, against 52/100 and 5.2s on the homepage. Two of three Meta ads route directly to PDP templates.

## Top Test Opportunities

### 1. Restate Ad 3's specific claims on its landing destination
**What's broken:** Ad 3 promises a "perfect anti-aging product" discovery narrative with specific claims (huidbarrière, fijne lijntjes). It lands on a single-fold, dark-maroon quiz interstitial: shoppers pick their biggest skincare frustration from 5 options, then see a panel stating "20+ jaar klinische ervaring" with a "Shop LABAREAU" text link — no product, price, or review anywhere.
**Evidence:** Meta Ads visual summary (Ad 3), raw/context.md Priority #2.
**Est. lift:** data unavailable — no sessions/mo or Ad 3 traffic split.

### 2. Move Ad 1's bundle offer above the fold
**What's broken:** Ad 1 promises "AHA Peel & The Toner, 14% korting." Its landing PDP opens on a single-unit buy box at €49,00; the matching bundle tile only appears in fold 2, styled generically, not echoing the ad's offer language.
**Evidence:** Meta Ads visual summary (Ad 1).
**Est. lift:** data unavailable — no baseline CR by ad.

### 3. Fix PDP load speed before testing PDP elements
**What's broken:** The Rich Cream PDP scores 38/100 mobile Lighthouse, 19.7s LCP (vs. 2.5s "good"), 790ms TBT — against 52/100/5.2s on the homepage. Any buy-box test here is capped by pre-paint abandonment.
**Evidence:** raw/pagespeed.md (Lighthouse, fetched 2026-09-11).
**Est. lift:** n/a — dev prerequisite.

### 4. Test a fixed evergreen offer against the recurring discount mechanic
**What's broken:** The site runs a rotating gift-at-€100 banner plus ad-led percentage discounts; discount share of gross revenue rose from 12% to 20.5% while volume halved.
**Evidence:** raw/context.md Priority #1, raw/reviews.md (Hasna Qatto, Karima).
**Est. lift:** brand's own estimate — "one extra euro per click shows up immediately"; no independent CRO figure available.

### 5. Add printed review counts to collection-page cards
**What's broken:** The "Alle Producten" grid (24 products) shows 5-star visual rows with no printed review count, while homepage tiles and the PDP both show printed counts (1141, 2382).
**Evidence:** raw/site-visual-summary.md (Collection vs. Homepage/PDP).
**Est. lift:** data unavailable.

### 6. Add guarantee/returns/shipping copy to the cart drawer
**What's broken:** The cart drawer ("WINKELWAGEN (2)") shows line items, a free-sample module, checkout, and payment icons — no guarantee, returns, or shipping copy anywhere.
**Evidence:** raw/site-visual-summary.md (Cart section).
**Est. lift:** data unavailable.

### 7. Reinforce the doctor-authority claim with a comparable proof point
**What's broken:** Google Ads run "Aangeraden Door Artsen" (recommended by doctors) with a 4★/168-review badge, absent from Meta creative; the homepage shows only a generic "Recommended by doctors" checkmark with no supporting detail.
**Evidence:** raw/google-ads-visual-summary.md; competitor analysis shows Bader and Dr. Barbara Sturm run the same doctor-created positioning at 2-3x Labareau's price (Bader's "Rich Cream" ~€265/50ml vs. Labareau's €119).
**Est. lift:** data unavailable.

### 8. Test a refill/smaller-format SKU against the price objection
**What's broken:** The only recurring complaint pairs price with short shelf life: "a bit pricey" alongside "the products only last for six months once opened" (Karima) — a cost-per-use issue, not pure price resistance. No refill/smaller-format option is visible on PDP or collection page.
**Evidence:** raw/reviews.md (Karima, Val Markou).
**Est. lift:** data unavailable.

### 9. Standardize PDP accordion language to Dutch
**What's broken:** Ad 2's landing page (The Rich Cream PDP, fold 3) shows four benefit tiles in English ("Native collagen," "Deep Hydration," "Clinically Proven") inside an otherwise all-Dutch page — a language-consistency break on the site's strongest message-match template.
**Evidence:** raw/meta-ads-visual-summary.md (Ad 2, Fold 3).
**Est. lift:** data unavailable.

### 10. Surface the newsletter/promo-alert signup earlier in the funnel
**What's broken:** Labareau's own review reply tells a customer to "keep an eye on our newsletter as we always announce promotions there first," but no newsletter signup appears in any captured homepage, collection, or cart shot.
**Evidence:** raw/reviews.md (Karima reply), raw/site-visual-summary.md (no signup captured).
**Est. lift:** data unavailable.

## Unused Findings

- Live homepage fetch (2026-09-11) shows a running giveaway banner not in the static screenshots — TikTok's top post in 30 days is the same giveaway (61,208 views), confirming giveaways outperform evergreen content.
