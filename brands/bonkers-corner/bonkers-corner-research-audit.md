# Bonkers Corner CRO Research Audit

## Data Sources Used

- Meta Ads & Landing Pages (screenshots, 3 ads, no URLs — screenshots only)
- Google Ads Transparency Center (2 screenshots)
- PageSpeed / Core Web Vitals (Lighthouse mobile JSON, homepage + PDP)
- Current Site Screenshots (homepage, PDP, cart drawer — live homepage also fetched)
- Competitor research (self-researched via WebSearch, no user-provided competitor file)

Reviews were collected (raw/reviews.md) but excluded from this audit per user instruction — span Nov 2024–Jul 2026, old and low-volume, not sufficient signal. Not cited below.

## Source Findings

### Meta Ads & Landing Pages

All three Meta ads use the same landing page pattern: a full-height product image, a buy box with price/size/Add to Cart, and a rotating "Special Offers" box that cycles between SHARKTANK10, an EMI-on-UPI option, and a prepaid UPI discount.

None of the three ads' stated offers match what appears on their own landing page:
- Ad 1 promises "15% off first order with NEW15." The landing page never shows NEW15 — it rotates SHARKTANK10 (₹130 off), EMI, or ₹65 UPI discount instead.
- Ad 2 promises "10% OFF on Prepaid." The landing page shows SHARKTANK10 (₹140 off), EMI, or ₹70 UPI discount — no offer matches "10% prepaid" as framed in the ad.
- Ad 3 promises "EXTRA 5% prepaid saving." The landing page rotates SHARKTANK10 (₹130 off) and EMI — the specific 5% figure never appears.

This is a consistent pattern across all three ads, not an isolated case: the specific code or percentage a shopper clicks on is never the offer waiting for them.

Trust signals are inconsistent across the three PDPs. Ad 2 and Ad 3's landing pages show a "90-Day Guarantee — Stitch & fabric defects? We cover it" badge directly under the price. Ad 1's landing page has no such badge. Review counts are also thin and inconsistent: 9 reviews (Ad 1), 1 review (Ad 2), 12 reviews (Ad 3). None of the three ads' landing pages use a sticky Add to Cart — the CTA is static within the buy box across all folds.

### Google Ads

Google Search and Display ads lean much harder on the "As Seen on Shark Tank India" angle than Meta creative does — it appears as an explicit headline ("As Seen on Shark Tank India – Bonkers Corner Is Trending") in multiple ad units, where on Meta it only surfaces as a site-wide announcement bar, not ad copy. Google ads also introduce discount figures not seen in the Meta set: "Starting At ₹999 Only," "5% off on Prepaid Orders," and price-anchored Shopping ads ("View 3 prices from ₹299.00"). Combined with the Meta-side mismatches above, the brand is running at least five distinct discount framings across two channels (NEW15, SHARKTANK10, 10% prepaid, extra 5% prepaid, ₹999 starting price) with no single consistent offer a shopper can rely on between ad and landing page.

### Reviews & UGC

Excluded from this audit per user instruction (old, low-volume dataset spanning Nov 2024–Jul 2026). See Missing Data.

### PageSpeed / Core Web Vitals

Source: Lighthouse mobile reports, collected 2026-08-26.

**Homepage** (bonkerscorner.com/): Performance score 33/100. FCP 10.0s, LCP 39.0s, TBT 1,020ms, Speed Index 24.3s, TTI 48.8s. Lighthouse's own run warning: "page loaded too slowly to finish within the time limit; results may be incomplete" — meaning actual real-world load is likely worse than what's captured here.

**PDP** (Rev It Up Oversized T-shirt): Performance score 37/100. FCP 16.2s, LCP 49.2s, TBT 750ms, CLS 0.001, Speed Index 20.2s, TTI 53.2s. Same incomplete-run warning.

Both pages are catastrophically slow by any Core Web Vitals threshold (Google's "good" LCP bar is 2.5s — these pages are 15-20x over it). CLS is not a problem on either page (0 and 0.001). The bottleneck is load and interactivity, not layout shift. At an LCP near 40-50 seconds, the practical reality is that a large share of paid-traffic visitors — the same visitors the Meta and Google ads above are paying to acquire — are abandoning before the page finishes rendering.

### Competitor Analysis

Self-researched via WebSearch (research date: 2026-08-26). No user-provided competitor file existed for this collection.

| Brand | Price range | Positioning | Notable weakness/gap vs. Bonkers Corner |
|---|---|---|---|
| The Souled Store | ~₹500–₹2,000 | Licensed IP (Marvel, DC, anime) streetwear, dominant in the fandom-merch lane | Bonkers Corner also runs Spider-Man/Marvel collabs but without Souled Store's catalog depth in licensed prints |
| Bewakoof | Lower-mid price tier | High-volume, broad catalogue, accessible everyday casualwear | Bonkers Corner positions as edgier/more distinctive graphic design at a similar-to-slightly-higher price point |
| Snitch | Mid-premium | Fast-follow trend fashion, heavy paid-social spend | Direct mid-premium competitor; comparable use of prepaid/discount-code offer stacking in ads |

Bonkers Corner sits in the mid-premium D2C streetwear bracket (~₹999–₹2,999 observed on-site and in ads), competing most directly with The Souled Store and Snitch rather than Bewakoof's lower price tier. Industry-wide, India's streetwear market is projected to grow from ~$10.86B (2024) to ~$20.86B by 2033 (CAGR ~7.58%), meaning paid acquisition costs in this category are likely to keep climbing — raising the cost of every visitor lost to slow load times or offer mismatch documented above.

### Emails

Not collected (source skipped per manifest).

### Inspiration Sites

Not collected (source skipped per manifest).

### Non-Data Context

Not collected (source skipped per manifest).

### Current Site Screenshots

**Homepage:** Image-heavy, editorial/lifestyle-led layout — full-bleed model photography with minimal text across all three folds captured. No product cards, prices, or category tiles appear anywhere in the first three folds; a shopper arriving on the homepage sees lifestyle imagery and "SHOP NOW" buttons before seeing a single price or product. Zero trust signals are visible on the homepage itself (no star rating, review count, guarantee badge, or shipping promise) — the only recurring credibility element is the site-wide announcement bar (Shark Tank mention + SHARKTANK10 code). No sticky header or CTA on mobile. The live homepage fetch confirms additional trust copy exists further down the page ("100% MADE IN INDIA," "SHIPPING WITHIN 48 HOURS," customer testimonials) — but none of it appears in the above-the-fold screenshots collected, meaning it's likely below what most mobile visitors scroll to see.

**Collection page:** Gap — no actual product-listing/PLP grid was captured. The three "collection" screenshots (collections-f1/f2/f3.png) show homepage-style category promo tiles (large lifestyle imagery, "BOTTOMS," "T-SHIRTS," "DRIFT 2.0" overlays with Shop Now buttons), not a page with product cards, prices, or filters. Collection-page findings cannot be evaluated from this data set.

**PDP:** Single-image-led buy box (Rev It Up Oversized T-shirt, ₹999, was ₹1,199, SAVE 17%). Star rating shows only 2 reviews, directly under the price. No guarantee badge appears on this PDP, unlike the beige cargo and bottle-green pants PDPs seen via the Meta ad landing pages (which show a "90-Day Guarantee" badge) — guarantee messaging is inconsistent product-to-product rather than a standard buy-box element. Only one variant type (size) is offered; no color swatches, unlike the ad-linked PDPs which show 3-5 color swatches. No sticky Add to Cart as the page scrolls. No upsell or frequently-bought-together module visible in the three folds captured. The Special Offers box rotates between EMI, prepaid UPI discount, and SHARKTANK10 across the three folds — the same rotating-offer pattern seen on the ad landing pages, meaning a shopper scrolling the PDP sees a different "current" offer depending on which fold they're looking at, with no single offer displayed consistently.

**Cart (drawer):** Right-side slide-out drawer with a black "Get 10% off with code SHARKTANK10" banner, then a tiered spend-unlock progress bar (₹500 → 10%, ₹5,999 → 15%, ₹9,999 → 20% via code GOBONKERS15) — a third and fourth discount code distinct from anything shown in the ads or PDP offer rotation. A "You may also like" cross-sell carousel with quick-add buttons sits below the line item. Checkout CTA is a static full-width black button with a "5% OFF on Prepaid Orders" sub-label — a fifth discount framing. No guarantee, returns, or trust badge appears anywhere in the cart drawer; every piece of copy in the cart is a discount code or savings figure, not a trust signal.

## Cross-Source Themes

1. **Offer inconsistency across every touchpoint (Meta ads → landing pages → PDP → cart).** Evidence: all 3 Meta ads (each promises a specific code/percentage the landing page doesn't show), Google Ads (adds ₹999-starting and 5%-prepaid framings not seen on Meta), PDP (offer box rotates between 3 different codes across 3 folds), cart drawer (introduces a 4th code, GOBONKERS15, plus a 5th "5% prepaid" sub-label on checkout). This is the strongest, most evidence-dense theme — five+ discount framings are live simultaneously with no single consistent offer.
2. **Catastrophic load performance on paid-traffic entry points.** Evidence: PageSpeed homepage (LCP 39.0s, score 33/100) and PDP (LCP 49.2s, score 37/100), both with Lighthouse's own "too slow to complete" warning. Directly undermines the ad spend documented in Meta Ads and Google Ads sources — visitors arriving from paid clicks are the ones most likely to abandon before the page renders.
3. **No trust signals above the fold anywhere in the funnel.** Evidence: homepage (zero trust signals in 3 folds, only discount bar), PDP (guarantee badge missing on the collected PDP but present on ad-linked PDPs — inconsistent), cart drawer (zero trust/guarantee content, only discount messaging). The only credibility lever used site-wide is "As Seen on Shark Tank," repeated as text rather than reinforced with reviews, guarantees, or badges at the point of purchase.

## Top Test Opportunities

**Unify the discount offer across ads and landing pages** — Each Meta ad promises a specific code (NEW15, 10% prepaid, extra 5% prepaid) that never appears on its own landing page, which instead rotates SHARKTANK10/EMI/UPI offers. Evidence: meta-ads-visual-summary.md (all 3 ads). Est. lift: 3-6% CVR lift on paid-social landing sessions x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV data].

**Fix homepage and PDP load speed** — Homepage LCP is 39.0s and PDP LCP is 49.2s on mobile, both roughly 15-20x Google's 2.5s "good" threshold, with Lighthouse flagging the run as incomplete due to load time. Evidence: raw/pagespeed.md. Est. lift: every 1s of LCP improvement below current levels is associated with meaningful CVR recovery per industry benchmarks (Google/Deloitte); at LCP this severe, even partial improvement (e.g., 39s → 15s) likely recovers a large share of currently-abandoning sessions x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV data].

**Add a consistent guarantee badge to every PDP** — The collected PDP (Rev It Up T-shirt) shows no guarantee badge, while ad-linked PDPs (beige cargo, bottle-green pants) show a "90-Day Guarantee" badge directly under price. Evidence: site-visual-summary.md (PDP), meta-ads-visual-summary.md (Ads 2, 3). Est. lift: 1-3% CVR lift from consistent trust signal at point of purchase x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV data].

**Surface trust signals on the homepage above the fold** — Homepage folds 1-3 show zero trust signals (no reviews, guarantee, shipping promise); the live site fetch shows "100% MADE IN INDIA," "48-hour shipping," and testimonials exist further down the page, meaning most mobile scrollers likely never see them. Evidence: site-visual-summary.md (Homepage), live homepage WebFetch. Est. lift: 1-2% CVR lift x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV data].

**Consolidate the cart drawer's discount messaging** — The cart drawer shows SHARKTANK10 (banner), a 3-tier GOBONKERS15 spend-unlock bar, and a "5% OFF Prepaid" sub-label under checkout — three distinct offers competing for attention with no trust signal to counterbalance them. Evidence: site-visual-summary.md (Cart). Est. lift: 1-2% CVR lift from reduced decision friction at checkout x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV data].

**Add color swatches to standard PDPs** — The collected PDP (Rev It Up T-shirt) offers only a size selector with no color variant, while ad-linked PDPs show 3-5 color swatches. Evidence: site-visual-summary.md (PDP), meta-ads-visual-summary.md (Ads 1-3). Est. lift: 0.5-1.5% CVR lift on affected SKUs x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV data].

**Add a sticky Add to Cart button on PDP** — All PDPs observed (both the standard PDP and ad-linked PDPs) use a static, non-sticky Add to Cart button within the buy box across all folds, requiring a scroll back up to purchase after viewing product detail. Evidence: site-visual-summary.md (PDP), meta-ads-visual-summary.md (all 3 ads, "LP CTA" notes). Est. lift: 0.5-1.5% CVR lift x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV data].

**Recollect an actual collection/PLP page** — No true product-listing grid was captured; the "collection" screenshots show homepage-style category tiles instead. This blocks any collection-page test hypothesis from being evaluated. Evidence: manifest.md (Missing Data Warnings). Not scoreable until real data is collected — listed here as a data-gap-driven opportunity, not a ready test.

## Unused but Valuable Findings

- Google Ads use distinct starting-price anchors (₹999, ₹299) not tested on Meta or the collected PDP — worth testing as a homepage/collection pricing anchor if a real collection page is recollected.
- The cart drawer's cross-sell carousel ("You may also like") is only partially visible in the captured screenshot — worth a follow-up screenshot to evaluate AOV mechanics fully.

## Missing Data

- Reviews were collected (raw/reviews.md, 14 reviews, Nov 2024–Jul 2026) but excluded from this audit per user instruction — dataset is old and low-volume, insufficient signal for test hypotheses.
- No actual collection/PLP grid screenshot exists — collections-f1/f2/f3.png show homepage-style category promo tiles, not a product-listing page. Collection-page test opportunities cannot be evidence-backed until this is recollected.
- No Meta Ads landing page URLs were provided (screenshots only) — landing pages could not be independently fetched or verified beyond what the screenshots show.
- No AOV, monthly sessions, or conversion rate figures were provided or collected for this brand — every "Est. lift" dollar figure above is left as a formula with sessions/AOV unresolved. These must be supplied before the roadmap can attach real dollar estimates.
