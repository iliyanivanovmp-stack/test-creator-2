# Solace Bands Roadmap Seed

**Store:** solacebands.com
**AOV:** unknown (est. $45 used for lift calcs, needs client confirmation)
**Monthly sessions:** unknown (est. 30,000 used for lift calcs, needs client confirmation)
**Data sources:** Google Ads Transparency Center, PageSpeed/Core Web Vitals (mobile, Lighthouse), Current Site Screenshots (homepage, collection, PDP, cart), Reviews & UGC (~100 Amazon reviews), live homepage fetch, self-researched competitor landscape

## Key Insights

Mobile performance is the highest-severity issue in the funnel: the homepage scores 38/100 on Lighthouse mobile with a 7.1s LCP and 38.3s Time to Interactive, and the PDP scores 50/100 with a 5.4s LCP and 45.6s Time to Interactive. Total Blocking Time on the homepage (1,340ms) is over 4x Google's "poor" threshold, most likely driven by the autoplay UGC video carousel and stacked product carousels loading on initial render. Since Google Ads is the brand's only paid channel and routes directly to these two pages, a meaningful share of paid clicks are arriving on a page that isn't yet interactive.

The brand's central selling mechanic — "5 for $99" / "Buy 2, Get 1 Free" — headlines the homepage announcement bar, dominates Google Ads offer copy, and is the only interactive AOV lever in the cart drawer (via a progress bar tied to quantity). But it's completely absent from the PDP buy box, the single highest-intent page in the funnel: the buy box shows one price ($39.99) and a single-unit Add to Cart button, with the bundle referenced only in on-page copy further down. A shopper arriving from a "5 for $99" ad clicks into a PDP that doesn't restate or activate that offer until they've already added one unit and opened the cart drawer.

Reviews (~100 Amazon reviews) surface a clear, repeated friction theme unrelated to product quality: sizing instructions are described as printed in "microscopic text" and the included pin tool as "outdated," with dozens of independent reviewers describing difficulty landing on a comfortable fit. This is the single most repeated complaint in the sample and likely suppresses repeat purchase and review sentiment, though it's primarily a packaging/instructions fix rather than a pure CRO lever. A secondary theme is color-accuracy complaints (delivered band color reads greener/grayer than product photography shows) and clasp-reliability reports, both flagged as unused findings below since they're product/ops issues, not test surfaces.

Message match between Google Ads and the homepage is partial: roughly a third of ad headlines lead with PFAS-free/hypoallergenic/non-toxic safety claims, but the homepage hero headline is "Give Your Apple Watch A Makeover" — the safety claim doesn't appear until the fold-3 trust ticker or the "What Sets Solace Bands Apart?" comparison table further down the page. Competitor research (WebSearch, 2026-08-04) found a 2026 Sarasota Magazine roundup naming Solace "the easiest recommendation" among Apple Watch band brands — a third-party editorial signal the site doesn't currently leverage, relying instead only on self-reported review counts (2M+ sold, 15K+ reviews).

## Top Test Opportunities

### 1. Surface the bundle offer inside the PDP buy box
**What's broken:** On the Imperium Adapt PDP, the buy box sits in the right column: product title, star rating with review count ("3576 reviews"), price ($39.99), a color selector with ~50+ swatches across 4 rows, a size selector, and a single black "ADD TO CART" button, followed by a Shop Pay installment line and a 3-icon trust row (Ships Next Day, Lifetime Quality, Money-Back Guarantee). There is no subscription, bundle, or multi-quantity option inside this buy box — it supports a single-unit purchase only. The "5 for $99" and "Buy 2, Get 1 Free" bundle deal, which headlines the homepage announcement bar and most Google Ads copy, is referenced only in an on-page copy block further down the PDP, outside the buy box and below the fold. A shopper who clicked a "5 Bands For $99" ad lands on a page where that exact offer isn't visible or actionable at the moment they decide whether to add to cart.
**Evidence:** Google Ads visual summary (offer is the lead CTA/sitelink in ad copy), site visual summary (PDP buy box detail — "Single purchase option only... bundle deal is referenced only in on-page copy further down"), homepage screenshot (bundle in top announcement bar).
**Key data:** Bundle offer appears in Google Ads sitelinks ("5-Free Watch Bands," "Buy 2 Get 1 Free Sitewide," "5 Bands for $99 This Week") and the homepage top bar, but zero buy-box presence on PDP.
**Est. lift:** 1% CR lift x 30,000 sessions/mo x $45 AOV = $13,500/mo.

### 2. Fix mobile homepage load performance
**What's broken:** The homepage (solacebands.com/) loads a hero with a large lifestyle image, a product carousel with color-swatch selectors, a scrolling trust-badge ticker, and a 4-video autoplay UGC/testimonial carousel — all within the first three folds. On mobile Lighthouse, this page scores 38/100 with a 7.1s Largest Contentful Paint and a 38.3-second Time to Interactive; Total Blocking Time is 1,340ms, more than 4x Google's "poor" (300ms) threshold, indicating heavy main-thread JS work — consistent with the autoplay video carousel and stacked product carousels rendering on load.
**Evidence:** raw/solace-homepage-pagespeed.json (mobile Lighthouse lab data, collected 2026-08-04).
**Key data:** Performance score 38/100, LCP 7.1s, TTI 38.3s, TBT 1,340ms, CLS 0.
**Est. lift:** 0.5% CR lift x 30,000 sessions/mo x $45 AOV = $6,750/mo.

### 3. Fix mobile PDP load performance
**What's broken:** The PDP (Imperium Adapt) loads a large product image with a thumbnail gallery of 4 lifestyle photos, a sticky/persistent buy box with an extensive ~50+ swatch color grid, and further down a full-width banner with icon callouts plus an "Over-Engineered To Exceed Your Expectations" section with large lifestyle imagery. On mobile Lighthouse, this page scores 50/100 with a 5.4s LCP and a 45.6-second Time to Interactive — the page immediately downstream of every "Shop Now" and product-ad click.
**Evidence:** raw/solace-pdp-pagespeed.json (mobile Lighthouse lab data, collected 2026-08-04).
**Key data:** Performance score 50/100, LCP 5.4s, TTI 45.6s, TBT 750ms, CLS 0.
**Est. lift:** 0.5% CR lift x 20,000 PDP sessions/mo x $45 AOV = $4,500/mo.

### 4. Lead the homepage hero with the PFAS-free/safety claim
**What's broken:** The homepage hero (fold 1, below the top announcement bar) shows an eyebrow line "2M+ BANDS SOLD | 15K+ 5-STAR REVIEWS," a headline "Give Your Apple Watch A Makeover" (with "Makeover" italicized in blue serif), supporting subhead copy, and a single blue "Shop Now" button, next to a large lifestyle photo of a wrist stacked with 4 bands. The PFAS-free/non-toxic/hypoallergenic safety claim — the dominant theme in roughly a third of Google Ads headlines — doesn't appear until the scrolling trust-badge ticker in fold 3, or the "What Sets Solace Bands Apart?" comparison table further down the page.
**Evidence:** Google Ads visual summary (headline themes: "No PFAS, BPA, or Phthalates," "Non-Toxic," "Skin Friendly / Hypoallergenic" appearing twice), site visual summary (homepage fold 1-3 breakdown).
**Key data:** Roughly 1 in 3 ad headlines lead with a safety/non-toxic claim; hero headline on-site is lifestyle-only ("Makeover").
**Est. lift:** 0.5% CR lift x 30,000 sessions/mo x $45 AOV = $6,750/mo.

### 5. Add price to collection page product cards
**What's broken:** The collection page ("All Solace Bands," 29 items) displays a dense 5-column desktop grid with two-image product cards (flat band + on-watch shot), product name, and color swatches with a "+N" overflow indicator. Across all three captured folds of the grid, no price, compare-at price, or sale badge appears on any product card — only status badges like "Sold out," "NOT RESTOCKING," or a donation badge on one item. Shoppers must click into an individual PDP to see the single price point ($39.99 on the sampled PDP).
**Evidence:** site visual summary (collection page — "Price display: No visible price shown on product cards in any fold").
**Key data:** 0 of 29 collection-grid items show price in any captured fold.
**Est. lift:** 0.3% CR lift x 15,000 collection sessions/mo x $45 AOV = $2,025/mo.

### 6. Add sizing clarity to the PDP
**What's broken:** The PDP's collapsible accordions ("Features," "Description," "Shipping and Warranty") sit below the buy box, but none is dedicated to sizing/link-adjustment guidance. Reviews describe the physical instructions bundled with the product as printed in "tiny microscopic text" requiring "a magnifying glass," and the included pin tool as "outdated" and difficult to use — friction that happens after purchase but is repeatedly severe enough to drive returns and 1-3 star reviews.
**Evidence:** raw/reviews.md (recurring across dozens of reviews — e.g., Schultz: "installation instructions are printed in such tiny microscopic text," Geri L. Dickinson: "instructions are written in super small print," Diane: "the size range is the length of a link... wasn't a 'just right'").
**Key data:** Sizing/instructions friction is the single most repeated complaint theme across the ~100-review sample.
**Est. lift:** 0.3% CR lift x 20,000 PDP sessions/mo x $45 AOV = $2,700/mo.

### 7. Add a trust/guarantee element to the cart drawer
**What's broken:** The cart drawer is a right-side slide-out with a "SOLACE" header, a progress bar ("Add Bands To Unlock Rewards" with "Buy 2, Get 1 Free" and "5 for $99" milestones), the line item with quantity stepper, a "These Popular Bands Match Your Selected Size" cross-sell module (3 cards with one-click "Add" buttons), and a full-width black "CHECK OUT" button at the bottom. No guarantee copy, return-policy reference, or trust badge appears anywhere in the drawer, despite "Money-Back Guarantee" and "Lifetime Quality" being core trust claims used on the PDP and homepage.
**Evidence:** site visual summary (Cart section — "Trust signals: Not visible in the cart drawer — no guarantee, returns copy, or trust badge shown in this capture").
**Key data:** Cart drawer trust-signal count: 0, vs. 3-icon trust row present on PDP.
**Est. lift:** 0.2% CR lift x 25,000 add-to-cart sessions/mo x $45 AOV = $2,250/mo.

### 8. Leverage third-party editorial mention in on-site trust copy
**What's broken:** The homepage trust ticker and hero eyebrow cite only self-reported metrics ("Over 2 Million Sold," "15,000+ 5-Star Reviews," "2M+ BANDS SOLD"). No third-party editorial or press mention appears anywhere in the captured homepage folds.
**Evidence:** Competitor research (Sarasota Magazine, "The 7 Best Apple Watch Band Brands in 2026," names Solace "the easiest recommendation," accessed 2026-08-04), site visual summary (homepage trust signals — no editorial citations present).
**Key data:** 0 third-party press mentions currently surfaced on-site vs. at least one favorable 2026 roundup available.
**Est. lift:** 0.2% CR lift x 30,000 sessions/mo x $45 AOV = $2,700/mo.

## Unused Findings

- Clasp-reliability complaints (magnetic clasp releasing, pin popping loose) recur across multiple independent reviewers over an extended period and may warrant product-team escalation.
- Color-accuracy complaints (delivered band color reading greener/grayer than product photography) recur often enough to suggest a photography/color-calibration audit.
- WizeBand, a direct PFAS-free competitor, offers a 100-day return window — more generous than Solace's stated guarantee — worth a policy review outside the CRO test scope.
