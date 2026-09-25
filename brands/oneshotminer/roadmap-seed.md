# Oneshotminer Roadmap Seed

**Store:** https://oneshotminer.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Current Site Screenshots, PageSpeed / Core Web Vitals, Reviews & UGC

## Key Insights

The PDP carries a 22.0s mobile LCP and 22.1s TTI (vs. 4.5s LCP / 16.8s TTI on the homepage), meaning the buy box, variant selector, and Add to Cart button on the store's primary conversion page are likely non-interactive for a large share of mobile visitors well past typical abandonment thresholds. Every downstream PDP finding in this audit is gated by this: hierarchy, social proof, and bundle-tier clarity don't matter if the page hasn't rendered.

Trust signals and urgency messaging are mismatched across the funnel. The homepage opens with a "BANKRUPT SALE | ENDS WHEN STOCK RUNS OUT" banner and shows zero reviews, ratings, or guarantee badges in its first three folds, while the PDP carries a strong "★★★★★ (1420+ reviews)" line directly above its buy box. This matters more than usual for this brand: Trustpilot reviews show a sharp bimodal pattern where nearly every 1-star review centers on broken refund and cancellation promises ("keep you talking exactly long enough so that you miss the refund date," "Company does not honor their own terms of service"), while 5-star reviews cluster around delivery-went-fine plus product-works. This audience is primed by public reviews to read inconsistency as evidence of manipulation, which raises the stakes on small credibility gaps elsewhere on-site: a footer link labels the flagship product "(2025 Edition)" while the PDP and homepage both call it "(2026 Edition)," and compare-at discount percentages vary 40-72% across near-identical hardware tiers with no visible justification.

The one genuinely strong, specific proof point on the site — a testimonial referencing a named $373,000 solo-mining win with a specific date — sits in PDP fold 3, below where the LCP/TTI data suggests many mobile visitors disengage.

## Top Test Opportunities

### 1. Fix PDP Largest Contentful Paint
**What's broken:** The PDP (https://oneshotminer.com/products/one-shot-pro-edition/) loads with a 22.0s mobile LCP and 22.1s TTI, compared to 4.5s LCP / 16.8s TTI on the homepage. The buy box sits in fold 1: large product image left with a thumbnail strip, right column holding a customer quote, "★★★★★ (1420+ reviews)" line, product title, price ($59.99 struck through $100.00), a low-stock note, a 4-item checklist, a variant selector (3 miner types), and a 3-tier quantity/bundle selector. At a 22-second LCP, this entire block is unlikely to be fully rendered and interactive before most mobile visitors would abandon.
**Evidence:** PageSpeed / Core Web Vitals (raw/pagespeed.md)
**Key data:** PDP LCP 22.0s, TTI 22.1s, Performance score 63/100, vs. homepage LCP 4.5s, TTI 16.8s, Performance score 79/100
**Est. lift:** conservative 15% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined pending traffic data

### 2. Add review count and rating to homepage above the fold
**What's broken:** The homepage opens with an announcement bar reading "BANKRUPT SALE | ENDS WHEN STOCK RUNS OUT" directly above a hero headline built on the 3.125 BTC solo-mining reward angle, with a single "CHOOSE YOUR MINER" CTA. No star rating, review count, or guarantee badge appears anywhere across the first three folds — the page moves straight from hero into a 10-card product grid. The PDP shows a "★★★★★ (1420+ reviews)" line directly above its buy box; this exact element is absent on the homepage.
**Evidence:** Site Screenshots (homepage folds 1-3), live homepage fetch
**Key data:** 1420+ reviews confirmed on PDP; zero trust signals visible in homepage folds 1-3
**Est. lift:** 5-10% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined

### 3. Move the named social-proof story above the fold on PDP
**What's broken:** PDP fold 3 contains a testimonial-style callout: "How the $373,000 solo miner got their one-in-a-million win," referencing a July 26, 2025 solo mining block win, with overlay CTA "Will you be the one who hits the next block?" This is the most concrete, specific proof point on the entire site (named dollar figure, named date) but appears well below the buy box, past where PageSpeed data suggests mobile engagement drops off.
**Evidence:** Site Screenshots (PDP fold 3), PageSpeed TTI data
**Key data:** PDP TTI 22.1s; testimonial currently in fold 3 of 3 captured
**Est. lift:** 3-6% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined

### 4. Show per-unit cost math on PDP bundle tiers
**What's broken:** The PDP buy box offers 3 quantity tiers: Buy 1 ($59.99), Buy 2 ($119.98, "Free shipping"), Buy 3 & get 1 Free ($179.97). The third tier is visually pre-selected (highlighted radio) and labeled "Best value," each tier also showing odds multiplier badges (2X/4X ODDS) and a "You save $X" line. No per-unit price is shown across tiers, so the "Best value" claim isn't substantiated at the point of decision.
**Evidence:** Site Screenshots (PDP buy box detail)
**Key data:** 3 tiers, no per-unit price comparison shown
**Est. lift:** 2-4% AOV lift x sessions/mo (unknown) x AOV (unknown) = undetermined

### 5. Standardize discount percentage logic on collection page
**What's broken:** The collection page grid shows "SAVE X%" badges on nearly every product card, with percentages varying unexplained card to card: 40%, 70%, 65%, 67%, 72%. No visible basis (bundle size, inventory age, launch pricing) differentiates why one near-identical hardware tier is marked down more than another.
**Evidence:** Site Screenshots (Collection page fold 1-2)
**Key data:** Discount range 40-72% across 9 products, no stated rationale
**Est. lift:** 2-4% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined

### 6. Fix version-label mismatch between footer and PDP
**What's broken:** The collection page footer's Menu section links to "One Shot Miner PRO (2025 Edition)," while the same product is titled "One Shot Miner PRO (2026 Edition)" on both the homepage and PDP. A small but visible inconsistency in a store where public reviews repeatedly allege the business is a "scam."
**Evidence:** Site Screenshots (Collection page footer, PDP title)
**Key data:** Footer: "(2025 Edition)" vs. PDP/homepage: "(2026 Edition)"
**Est. lift:** primarily a trust-consistency fix, minor direct CR impact

### 7. Add security and return-policy copy inside the cart drawer
**What's broken:** The cart drawer (right-side slide-out) shows a "24/7 Support - Lifetime Warranty" banner at the top and a "● Last units left" urgency banner at the bottom, sandwiching the "Check out" button, plus 3 upsell cards. No payment/security icons or return-policy link are visible inside the drawer, unlike the PDP, which shows payment icons directly beneath its Add to Cart button.
**Evidence:** Site Screenshots (Cart drawer)
**Key data:** PDP shows payment icons under Add to Cart; cart drawer does not
**Est. lift:** 1-3% checkout completion lift x sessions/mo (unknown) x AOV (unknown) = undetermined

### 8. De-duplicate repeated promotional badge copy on homepage grid
**What's broken:** All product cards in the homepage's 10-card grid (folds 1-2) carry the identical overlay text "Join the race of solo mining 3.125 BTC by yourself" on the product photo itself, regardless of which of the 6+ distinct miner models is shown. The repetition reduces the line's persuasive weight and doesn't differentiate products from each other.
**Evidence:** Site Screenshots (Homepage fold 1-2)
**Key data:** Identical badge text repeated across 10 product cards
**Est. lift:** 1-2% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined

## Unused Findings

- Support is named repeatedly by first name ("Mia") across multiple 1-star reviews describing repetitive, unresolved email loops — an ops/staffing gap, not a CRO test.
- The company's stated 1-hour cancellation policy is cited as violated in several reviews — a policy-enforcement issue outside CRO scope.
