# Bonkers Corner Roadmap Seed

**Store:** https://www.bonkerscorner.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency Center, PageSpeed/Core Web Vitals, Current Site Screenshots (homepage, PDP, cart), Competitor research (self-researched)

## Key Insights

Bonkers Corner is running at least five distinct discount framings simultaneously across its funnel with no single consistent offer. Each of the 3 Meta ads promises a specific code or percentage — "15% off with NEW15," "10% OFF on Prepaid," "EXTRA 5% prepaid saving" — and none of those codes appear on that ad's own landing page, which instead rotates SHARKTANK10, an EMI-on-UPI option, and a UPI prepaid discount across its three folds. Google Search and Display ads add further framings not seen on Meta at all ("Starting At ₹999 Only," "5% off on Prepaid Orders"). The PDP's Special Offers box itself rotates between three different codes across three scroll folds. The cart drawer introduces a fourth code (GOBONKERS15, tied to a 3-tier spend-unlock bar) and a fifth framing ("5% OFF on Prepaid Orders" as a checkout sub-label). A shopper clicking an ad for one specific discount never sees that discount again anywhere in the purchase path.

Homepage and PDP load speed are catastrophic on mobile: homepage LCP is 39.0 seconds (Performance score 33/100), PDP LCP is 49.2 seconds (score 37/100) — both roughly 15-20x over Google's 2.5s "good" LCP threshold, and Lighthouse flagged both runs as incomplete because the page loaded too slowly to finish testing. This directly undercuts the paid acquisition spend visible in both the Meta and Google ad sets: visitors who click a paid ad are the same visitors most likely to abandon before the page renders.

Trust signals are inconsistent and largely absent above the fold. The homepage shows zero trust signals across all three folds captured (no reviews, guarantee, or shipping promise) — only the repeating Shark Tank/SHARKTANK10 announcement bar. A live fetch of the homepage confirms trust copy ("100% MADE IN INDIA," "SHIPPING WITHIN 48 HOURS," testimonials) exists further down the page, but it's absent from what mobile visitors see first. On PDP, a "90-Day Guarantee" badge appears on ad-linked product pages (beige cargo, bottle-green pants) but not on the standard collected PDP (Rev It Up T-shirt) — the badge is applied inconsistently rather than as a standard buy-box element.

## Top Test Opportunities

### 1. Unify the discount offer across ads and landing pages
**What's broken:** Each of the 3 Meta ad creatives states a specific offer in its caption (NEW15 for 15% off; "10% OFF on Prepaid"; "EXTRA 5% prepaid saving"). On click-through, the landing page's Special Offers box — a bordered callout box sitting directly below the price and size selector in the buy box — instead rotates between SHARKTANK10 (a flat rupee discount), an "EMI on UPI" installment option, and a UPI prepaid discount, changing which one displays depending on which of the three scroll folds the visitor is on. The exact code/percentage promised in the ad is never shown. Google Ads add further offer variants (₹999 starting price, plain "5% off on Prepaid Orders") not present on Meta at all.
**Evidence:** meta-ads-visual-summary.md (all 3 ads, Message Match notes), google-ads-visual-summary.md (Gaps vs. Meta)
**Key data:** 5+ distinct discount framings identified live across ads, PDP, and cart with zero overlap to the specific ad clicked
**Est. lift:** 3-6% CVR lift on paid-social landing sessions x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV]

### 2. Fix homepage and PDP mobile load speed
**What's broken:** Both the homepage and the observed PDP take 39-49 seconds to reach Largest Contentful Paint on mobile (Lighthouse, real device throttling profile). Both Lighthouse runs returned a run warning that the page loaded too slowly to finish within the time limit, meaning true real-world load may be worse. CLS is not the issue on either page (0 and 0.001) — this is purely a load/interactivity bottleneck, not a layout-shift one.
**Evidence:** raw/pagespeed.md (bonkers-homepage-pagespeed.json, bonkers-pdp-pagespeed.json)
**Key data:** Homepage LCP 39.0s (score 33/100), PDP LCP 49.2s (score 37/100), TBT 1,020ms/750ms
**Est. lift:** Meaningful CVR recovery per industry LCP-to-CVR benchmarks at this severity x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV]

### 3. Add a consistent guarantee badge to every PDP
**What's broken:** On the collected standard PDP (Rev It Up Oversized T-shirt, ₹999), the buy box shows title, price, a 2-review star rating, size selector, and Add to Cart — with no guarantee or defect-coverage badge anywhere near the price. On the two ad-linked PDPs (beige cargo pants, bottle-green pants), a black "90-DAY GUARANTEE — Stitch & fabric defects? We cover it" badge sits directly under the price, above the size selector. The badge exists in the theme but isn't applied uniformly.
**Evidence:** site-visual-summary.md (PDP), meta-ads-visual-summary.md (Ads 2, 3 landing page fold 1)
**Key data:** Badge present on 2 of 3 observed PDPs; absent on the one PDP reached via organic/site navigation
**Est. lift:** 1-3% CVR lift from consistent point-of-purchase trust signal x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV]

### 4. Surface trust signals above the fold on homepage
**What's broken:** The homepage's first three scroll folds are entirely lifestyle photography — a full-bleed 8-model hero image, a two-panel lifestyle shot, and a single-model "Explore New In" slide — each with only a "SHOP NOW" button and no star rating, review count, guarantee, or shipping-time copy visible. The only recurring credibility element across all three folds is the black announcement bar cycling "AS SEEN ON SHARK TANK" and the SHARKTANK10 code. A live fetch of the full page confirms trust copy ("100% MADE IN INDIA," "SHIPPING WITHIN 48 HOURS," testimonials) exists lower on the page, past what the three-fold screenshot set captured.
**Evidence:** site-visual-summary.md (Homepage folds 1-3), live homepage WebFetch
**Key data:** 0 trust signals in first 3 folds vs. confirmed trust content further down page
**Est. lift:** 1-2% CVR lift x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV]

### 5. Consolidate cart drawer discount messaging
**What's broken:** The cart drawer (right-side slide-out) stacks three separate discount elements: a black "Get 10% off with code SHARKTANK10" banner directly under the header, a 3-tier spend-unlock progress bar below that (₹500→10%, ₹5,999→15%, ₹9,999→20% via code GOBONKERS15), and a "5% OFF on Prepaid Orders" sub-label beneath the black full-width Checkout button. No guarantee, returns policy, or trust badge appears anywhere in the drawer — every line of copy is a discount code or savings figure.
**Evidence:** site-visual-summary.md (Cart)
**Key data:** 3 distinct discount codes/framings stacked in a single cart drawer with zero trust content
**Est. lift:** 1-2% CVR lift from reduced decision friction at checkout x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV]

### 6. Add color swatches to standard PDPs
**What's broken:** The collected PDP (Rev It Up T-shirt) offers only a size selector (XS-XXL) with no color/variant swatches. The three ad-linked PDPs (jersey, cargo pants, sporty pants) each show 3-5 color swatches alongside size. Variant selection is inconsistent across the catalog rather than a standard buy-box element.
**Evidence:** site-visual-summary.md (PDP, "Buy box detail" note), meta-ads-visual-summary.md (Ads 1-3)
**Key data:** 0 of 1 standard-navigation PDPs show color swatches vs. 3 of 3 ad-linked PDPs
**Est. lift:** 0.5-1.5% CVR lift on affected SKUs x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV]

### 7. Add a sticky Add to Cart button on PDP
**What's broken:** Across all four PDPs observed (the standard PDP and all three ad-linked PDPs), the "ADD TO CART" button sits inline within the buy box and does not become sticky/fixed as the visitor scrolls through product detail, fabric composition, and style-highlight content in folds 2-3. A visitor who scrolls to review fabric/fit details must scroll back up to purchase.
**Evidence:** site-visual-summary.md (PDP, "CTA behavior"), meta-ads-visual-summary.md (all 3 ads, "LP CTA" notes)
**Key data:** Static CTA confirmed on 4 of 4 observed PDPs
**Est. lift:** 0.5-1.5% CVR lift x [sessions/mo unknown] x [AOV unknown] = [$ — needs traffic/AOV]

### 8. Recollect an actual collection/PLP page
**What's broken:** The three "collection" screenshots on file (collections-f1/f2/f3.png) show homepage-style category promo tiles — large lifestyle imagery with "BOTTOMS," "T-SHIRTS," "DRIFT 2.0" overlays and Shop Now buttons — not a product-listing grid with individual cards, prices, or filters. No collection-page friction can be evaluated from this data.
**Evidence:** manifest.md (Missing Data Warnings), site-visual-summary.md (Collection Page note)
**Key data:** 0 of 3 collection screenshots show an actual PLP grid
**Est. lift:** Not scoreable until real collection-page data is collected

## Unused Findings

- Google Ads use starting-price anchors (₹999, ₹299) not tested on Meta or the collected PDP — worth testing as a homepage/collection pricing anchor once a real collection page is recollected.
- The cart drawer's "You may also like" cross-sell carousel is only partially visible in the captured screenshot — a follow-up screenshot would allow full evaluation of AOV mechanics.
