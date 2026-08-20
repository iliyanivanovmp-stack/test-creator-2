# Essentia Roadmap Seed

**Store:** myessentia.com
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency Center, PageSpeed/Core Web Vitals, Current Site Screenshots, Competitor research (self-researched, Aug 5 2026)

## Key Insights

Mobile PageSpeed is the dominant issue: PDP LCP is 33.8s and TTI is 42.6s (score 0/100), homepage LCP is 11.8s with TTI at 37.1s. Both pages carry ~1.4-1.5MB of unused JavaScript. This sits upstream of the client's flagged problem — strong add-to-cart activity but a large drop-off before purchase completion — since a checkout flow inheriting similar JS weight is a likely cause.

Promotion messaging is inconsistent everywhere except the cart. The sitewide "20% OFF" banner is absent from all three Meta ads and all Google ad copy reviewed. Collection and PDP show only full price with no compare-at price despite the live sale — the discount only appears at the cart, where it auto-applies correctly. Google's ad set shows two different discount figures (30% and 22%) that match neither each other nor the 20% shown on-site.

Trust content is misplaced relative to purchase moments: PDP star ratings sit above the buy box, but trial (120-night) and warranty (20-year) terms sit in collapsed accordions below Add to Cart, and the cart page — closest to the flagged drop-off — has zero trust signals. Avocado (365-night trial, 25-year warranty) and Naturepedic (25-year warranty) both beat Essentia's terms.

## Top Test Opportunities

### 1. PDP mobile page-speed remediation
**What's broken:** Stratami PDP loads a large image gallery, three buy-box dropdowns, an Affirm widget, and a Consumer Reports video on initial mobile load. LCP 33.8s, TTI 42.6s, ~1.4MB unused JS, 6.4MB total page weight.
**Evidence:** raw/essentia-pdp-pagespeed.json
**Key data:** LCP 33.8s, score 0/100
**Est. lift:** 5-10% CR lift x unknown sessions x unknown AOV = TBD

### 2. Homepage mobile page-speed remediation
**What's broken:** Full-bleed video hero above a horizontally-scrolling product carousel. LCP 11.8s, TTI 37.1s, 1.5MB unused JS, 11.2MB total weight — heaviest page measured.
**Evidence:** raw/essentia-homepage-pagespeed.json
**Key data:** LCP 11.8s, score 0/100
**Est. lift:** 3-6% CR lift x unknown sessions x unknown AOV = TBD

### 3. Surface the sitewide discount on collection and PDP pricing
**What's broken:** Collection cards (Venti $1,699, Grateful Eight $1,999, Tatami $2,999, Stratami $3,599) and PDP show only full "Starting at $X" price, no strikethrough, despite the active 20% banner above. Discount only appears at cart.
**Evidence:** raw/site-visual-summary.md
**Key data:** Cart shows "Discount Applied -$719.80" on $3,599 item; collection/PDP show none
**Est. lift:** 2-4% CR lift x unknown sessions x unknown AOV = TBD

### 4. Add trust signals to the cart page
**What's broken:** Cart shows one line item, thumbnail, quantity stepper, discount line, static "Checkout" button. No guarantee, returns policy, warranty, or trial mention anywhere on the page.
**Evidence:** raw/site-visual-summary.md (Cart)
**Key data:** Zero trust elements on the page closest to the flagged drop-off
**Est. lift:** 2-4% CR lift on cart-to-checkout x unknown sessions x unknown AOV = TBD

### 5. Surface trial and warranty terms near Add to Cart on PDP
**What's broken:** "120 Night Sleep Trial" and "20 Year Warranty" sit as collapsed accordion items below the buy box, requiring a tap to expand. Star rating sits above the buy box; trial/warranty terms do not.
**Evidence:** raw/site-visual-summary.md (PDP), competitor research
**Key data:** Avocado offers 365-night trial/25-year warranty; Naturepedic 25-year warranty, both stronger than Essentia's terms
**Est. lift:** 2-3% CR lift on add-to-cart x unknown sessions x unknown AOV = TBD

### 6. Fix Ad 1 product mismatch (fix, not a test)
**What's broken:** Meta Ad 1 names the "Grateful Bed Eight" mattress; the linked landing page shows the "Grateful Bed Jr" kids' mattress.
**Evidence:** raw/meta-ads-visual-summary.md (Ad 1)
**Key data:** Wrong-product landing experience for adult-mattress clicks
**Est. lift:** not sizeable without spend/click data; priority fix

### 7. Add a highlighted upsell/cross-sell module
**What's broken:** PDP's EMF Foam Protection Upgrade dropdown defaults to "No EMF Foam Protection" with no visual emphasis. Cart has no bundle, cross-sell, or frequently-bought-together module.
**Evidence:** raw/site-visual-summary.md (PDP, Cart)
**Key data:** No AOV-lift mechanic at buy box or cart
**Est. lift:** 3-5% AOV lift x unknown sessions x unknown AOV = TBD

### 8. Route the Affirm ad (Ad 3) to a transactional page
**What's broken:** Ad 3 promotes 0% APR financing but links to an informational Affirm explainer page with no Add to Cart CTA across all three captured folds.
**Evidence:** raw/meta-ads-visual-summary.md (Ad 3)
**Key data:** No transactional path for financing-motivated clicks
**Est. lift:** not sizeable without spend/click data; funnel-leak fix

### 9. Reconcile discount percentage across ad channels and site
**What's broken:** Google Ads reference both "up to 30%" and "up to 22%" savings; neither matches the on-site 20% sale or Meta Ad 2's separate "30% via HSA/FSA" claim.
**Evidence:** raw/google-ads-visual-summary.md, raw/meta-ads-visual-summary.md
**Key data:** Three different discount figures across two channels and the site
**Est. lift:** 1-3% CR lift x unknown sessions x unknown AOV = TBD

### 10. Move certification/trust badges above the fold on homepage
**What's broken:** Certification badges and founder story don't appear until homepage fold 3, despite Google Ads' certification-led messaging ("GOLS & GOTS Certified," "#1 Rated").
**Evidence:** raw/site-visual-summary.md (Homepage), raw/google-ads-visual-summary.md
**Key data:** Certification-led ad traffic scrolls past 2 folds before seeing proof
**Est. lift:** 1-3% CR lift on Google-ad sessions x unknown sessions x unknown AOV = TBD

## Unused Findings

- Meta Ad 2 (HSA/FSA) shows strong message match with its landing page — worth replicating in future creative, not testing against.
- Cart discount application is accurate and well itemized — a positive control to preserve while testing earlier-funnel discount visibility.
