# Instant Hydration Roadmap Seed

**Store:** instanthydration.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed / Core Web Vitals, Current Site Screenshots

## Key Insights

Message match breaks down in three places across the funnel. The homepage hero CTA ("GET UP TO 50% OFF") links to /products/premium-electrolyte-drink-mix, a different product than the ICEE product nearly all Meta ads (and a share of Google ads) land on, and different from the ICEE card directly below the hero in fold 2. On the ICEE landing page itself, the ad's exact offer phrase "Try Risk Free for 50 Days + FREE GIFT" isn't in the above-the-fold buy box — only "50 Day Happiness Guarantee" appears there; the exact phrase exists further down the page. And Google Ads run 35-55% off messaging across varied creative angles that don't match Meta's consistent risk-free/free-gift framing, so retargeted shoppers see inconsistent offers depending on channel.

The page carrying the most paid traffic also has the worst technical performance. The ICEE landing page scores 36/100 on mobile PageSpeed with LCP 7.0s and CLS 0.546 — more than double the 0.25 "poor" CLS threshold — versus the homepage's 60/100, LCP 4.8s, CLS 0. That CLS score points to visible layout shift in the buy box, pricing table, or comparison table during load, right where a paid-traffic visitor is deciding to buy.

Across 45 reviews, saltiness is the most repeated complaint by volume, cutting across star ratings: "tasted like straight salt water" (1★), "Tastes like the ocean" (2★), "very, very salty" (3★), and even 4-5★ reviewers report needing to double or triple the recommended water ratio. No captured page — landing page, homepage, PDP substitute, or collection — includes dilution guidance or addresses the taste directly. A secondary theme is stevia aftertaste/sensitivity, distinct from the brand's "monk fruit" sweetener messaging, which several reviewers seem unaware the product also contains.

## Top Test Opportunities

Top Test Opportunities must be mutually exclusive. If an opportunity is a broader version of another, keep the broader version and mention the narrower case inside it.

### 1. Fix homepage hero CTA product mismatch
**What's broken:** The homepage hero (fold 1) is a full-bleed video/image of two women outdoors with a green pill CTA button reading "GET UP TO 50% OFF." This button links to /products/premium-electrolyte-drink-mix. Directly below in fold 2, on a dark background, two side-by-side cards sit under the headline "Hydration Starts Here": left card "ICEE x Instant Hydration" and right card "Shop Electrolytes." The hero CTA's destination doesn't match either card's product focus, and doesn't match the ICEE product that nearly all paid ad traffic lands on.
**Evidence:** site-visual-summary.md (homepage fold 1 URL overlay, fold 2 card descriptions)
**Key data:** Hero CTA routes to a third, distinct product URL not otherwise referenced on the page.
**Est. lift:** 1-2% CR lift x unknown sessions/mo x unknown AOV = [needs sizing data]

### 2. Surface the ad's exact risk-free offer above the fold on the ICEE landing page
**What's broken:** The ICEE landing page buy box (fold 1) sits below a hero with the headline "THE ICONIC FLAVOR YOU LOVE. NOW WITH THE ELECTROLYTES YOU NEED." and a stat ticker bar. The buy box itself shows a 3-tier pricing table, a purchase-type selector defaulted to "Subscribe & Save," and a red CTA "SELECT FROM 14 FLAVORS." Nowhere in this fold does the ad's specific promise, "Try Risk Free for 50 Days + FREE GIFT," appear verbatim — the closest text is "50 Day Happiness Guarantee," which appears one fold down, under the CTA, not inside the buy box itself.
**Evidence:** meta-ads-visual-summary.md, meta-ads.md, live WebFetch of the landing page
**Key data:** All 3 active Meta ads use the identical offer line; landing page buy box doesn't restate it in matching language.
**Est. lift:** 0.5-1.5% CR lift on paid landing traffic

### 3. Fix Core Web Vitals on the ICEE landing page
**What's broken:** Mobile Lighthouse on the ICEE product page (the page nearly all paid traffic lands on) scores 36/100 performance, with LCP 7.0s and CLS 0.546 — over double the "poor" threshold of 0.25. This points to visible shifting in the buy box/pricing table/comparison table area as the page loads, likely from unstaged image or table rendering described in the visual summary.
**Evidence:** raw/instanthydration-importnantpage-pafespeed.json
**Key data:** Homepage by comparison scores 60/100, LCP 4.8s, CLS 0 — the landing page is meaningfully worse than the site's own baseline.
**Est. lift:** 2-3% CR lift on paid landing traffic

### 4. Add pricing to collection page product cards
**What's broken:** The collection page ("Top Rated Electrolytes") shows a 3-column grid of 6 products across 2 captured folds — Premium Electrolyte Drink Mix, LUIGI'S Lemon Italian Ice, ICEE Blue Raspberry & Cherry, Electrolyte Variety Pack (30ct and 12ct), and MVP Bundle. Each card shows only a badge, product image, and title. No price, compare-at price, or per-unit cost appears on any card in either fold.
**Evidence:** site-visual-summary.md (collection page, both folds)
**Key data:** 0 of 6 visible product cards show any price.
**Est. lift:** 1-2% collection-to-PDP click-through lift

### 5. Address "too salty" perception on the landing page
**What's broken:** The landing page's benefit section (fold 2) shows a row of 6 icon+label callouts including "French Grey Sea Salt (Hand-Harvested Sel Gris)" — positioning salt as a premium ingredient, but not addressing taste intensity or serving guidance. No fold captured across the homepage, landing page, or cart references dilution instructions.
**Evidence:** reviews.md (top complaint by volume across 45 reviews, spanning 1-5 star ratings)
**Key data:** Reviewers report needing 24-32oz+ of water vs. presumed lower label guidance to make the product palatable.
**Est. lift:** 0.5-1% CR lift; primary value is reducing post-purchase 1-star reviews

### 6. Add a sticky mobile add-to-cart bar on the ICEE landing page
**What's broken:** The landing page's primary CTA, a red "SELECT FROM 14 FLAVORS" button, is manually repeated at least 3 times across the captured folds (buy box, below the accordion, end of the comparison section) rather than persisting as a fixed bar. The header shows only a static "CART" icon, no add-to-cart bar.
**Evidence:** meta-ads-visual-summary.md (LP CTA notes), pagespeed data (mobile TTI 35.3s)
**Key data:** CTA is repeated 3+ times manually across a page with a 35.3s time-to-interactive, increasing scroll distance to the next CTA repeat.
**Est. lift:** 1-2% CR lift on mobile paid traffic

### 7. Clarify the auto-added free sampler in the cart drawer
**What's broken:** The cart drawer (right-side slide-out, header "Your Cart") shows two line items: a "3 Pack Sampler" thumbnail marked "FREE" with no visible add action, and the main product with a strikethrough price and "Every 30 Days" subscription label. Large empty white space sits between the line items and the subtotal.
**Evidence:** site-visual-summary.md (cart drawer)
**Key data:** No labeled connection between the auto-added sampler and the ad's "FREE GIFT" promise.
**Est. lift:** 0.5-1% CR lift from reduced cart-stage confusion

### 8. Promote the competitor comparison table higher on the landing page
**What's broken:** A two-column comparison table (Instant Hydration vs. Liquid I.V. vs. LMNT) on a light blue background sits in fold 3 — the last section before the page's final CTA — after the buy box, accordion, review callout, and three lifestyle photo cards. It shows favorable rows on calories, sugar, and sodium type.
**Evidence:** meta-ads-visual-summary.md (fold 3), self-researched competitor pricing context (2026-08-04)
**Key data:** Table already shows favorable positioning (10 cal vs. 45, 0g sugar vs. 11g) but is reached only after 2+ folds of scrolling.
**Est. lift:** 0.5-1% CR lift by surfacing differentiation earlier for price-comparing shoppers

## Unused Findings

- Homepage athlete endorsements (Max Holloway, Shawn Johnson, Jameis Winston) don't appear in any captured Meta ad creative or the ICEE landing page — a trust asset not yet reused in the paid funnel.
- Stevia aftertaste/sensitivity is a distinct secondary review complaint from saltiness, tied to a labeling gap ("monk fruit" messaging vs. actual stevia content) rather than a UI/CRO fix.
- Price objections ("$37 for 20 packs") recur across otherwise satisfied 3-5★ reviews; the landing page already shows per-stick pricing but doesn't connect it to a value comparison.
