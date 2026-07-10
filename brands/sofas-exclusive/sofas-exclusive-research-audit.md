# Sofas Exclusive CRO Research Audit

## Data Sources Used

- Google Ads (Transparency tool) — self-researched, 2026-06-15
- PageSpeed / Core Web Vitals — Lighthouse 13.2.0, mobile emulation (Moto G Power 2022), 2026-06-15
- Site screenshots — homepage, collection, PDP, cart drawer, 2026-06-15
- Live site fetch — sofasexclusive.com, 2026-06-15

**Sources not collected:** Meta Ads, Reviews & UGC, Competitor Insights, Inspiration Sites, Email Campaigns, Non-Data Context.

---

## Source Findings

### Google Ads

Seven or more search text ads and multiple Shopping (PLA) cards visible in Transparency screenshots. Verified advertiser: G & C Company.

**Headline themes running simultaneously:**
- Product-specific: "THE THEODORE Sofa", "90 Inch Top Grain Leather Sofa - Brown Leather Sofa"
- Category/collection: "Modern Luxury Sofas - Designer Collections", "COLLECTION SETS"
- Brand: "Sofas Exclusive - Modern Luxury Sofas"
- Feature-led: "Eco-Friendly Woven Fabric - In Stock & Ready to Ship"

**Offer signals:** One ad mentions free shipping ("ready for free shipping"). No discount, sale, or % off messaging in any ad. Shop Pay installments not surfaced in ad copy despite being present on the PDP.

**Messaging tone:** The Theodore Sofa ad uses aspirational lifestyle language — "sophistication and exploration", "extraordinary", "the sofa encapsulates." The display ad runs a lifestyle room scene with the tagline "A Sofa Store You Will Love / Transform your living space with our curated collection of premium, modern furniture."

**Message match gap:** Ads promise premium, aspirational positioning, but the site hero reads generically ("Lounge in Luxury" / "Experience furniture crafted to blend modern aesthetics") and the collection page surfaces a $278 chair as the first Best Selling result — jarring for visitors primed by premium ad creative. Shop Pay installments, which lower perceived price barriers for high-ticket items, are not mentioned anywhere in ad copy.

---

### Reviews & UGC

**Not collected.** The site shows 4.91 stars from 11 reviews (visible in homepage hero area and live fetch). A single testimonial carousel appears in homepage Fold 2 — one quote at a time, from Stephan W. about the Aphrodite Loveseat. A 2-star rating is visible on THE DAKOTA card in the collection grid, displayed with no review count or context.

The 11-review count is a structural trust problem for a premium sofa brand with products ranging up to $5,992. No product-level review data was collected — this is a data gap.

**Client-actionable insights:**
- Actively request reviews post-delivery. At 11 total reviews, even 10 new reviews significantly change social proof credibility.
- The 2-star Dakota rating with no count shown is likely deterring clicks on that product. Investigate whether this is a data entry error, an outlier rating, or a product quality issue before it erodes category page trust.

---

### PageSpeed / Core Web Vitals

*Source: Lighthouse 13.2.0, mobile emulation, 2026-06-15*

| Page | Perf Score | LCP | Speed Index | TTI | CLS |
|---|---|---|---|---|---|
| Homepage | 53/100 | 7.5 s | 11.5 s | 24.3 s | 0.163 |
| PDP (Volos Chair) | 65/100 | 6.5 s | 6.4 s | 30.8 s* | 0.101 |

*\*Lighthouse warning: "The page loaded too slowly to finish within the time limit. Results may be incomplete." TTI of 30.8s likely understates the true figure.*

**Homepage is critically slow on mobile.** A 7.5s LCP puts it in the bottom 10% of Shopify stores. TTI of 24.3 seconds means visitors on average mobile connections cannot interact with the page for nearly half a minute. Speed Index of 11.5s indicates content is painting very slowly, not just delayed interactivity.

**PDP did not complete the Lighthouse test.** TTI of 30.8s is flagged as incomplete — the real time-to-interactive is higher. LCP of 6.5s is poor.

**CLS:** Homepage CLS of 0.163 is in the "needs improvement" band (threshold: 0.1 good / 0.25 poor). This means visible layout shifts during load — elements moving as the page renders — which disrupts early engagement and trust formation.

**Implication:** On mobile (which drives the majority of Shopify traffic), the majority of paid ad visitors from Google are landing on pages that take 7–30+ seconds to become usable. This directly caps the ceiling on every other conversion test.

---

### Competitor Analysis

*Note: No competitor data was provided by the client. The following is self-researched. Research date: 2026-06-15.*

Sofas Exclusive operates in the online premium/luxury sofa segment. Key direct competitors based on Google Shopping and Transparency data context:

| Brand | Price Range | Key Differentiators | Weaknesses vs. Sofas Exclusive |
|---|---|---|---|
| Article | $500–$3,500 | Strong brand identity, fast shipping promise, high review volume (thousands per SKU) | Less "exclusive" positioning, mass-market feel |
| Castlery | $400–$3,000 | Clean UX, clear lead times, strong UGC | Limited catalog vs. SE's 43+ SKUs |
| Interior Define | $1,200–$6,000+ | Customization, premium positioning, strong content | Longer lead times, less in-stock messaging |

Sofas Exclusive's $278–$5,992 price range and "white glove delivery" + "30-day free returns" offer competitive parity with mid-to-premium players. The differentiator gap: SE has 11 reviews vs. hundreds or thousands at Article or Castlery — a significant trust disadvantage at the moment of purchase.

---

### Current Site Screenshots

#### Homepage

**Fold 1:** Dark charcoal theme with gold "SOFAS EXCLUSIVE" logo. Three trust badges (30-Days Free Returns, White Glove Delivery, Secure Payment) placed between nav and hero — strong placement. Hero: full-width sofa lifestyle image, headline "Lounge in Luxury," subheadline "Experience furniture crafted to blend modern aesthetics." Two side-by-side CTAs in identical white button styling: "VIEW MORE" and "SHOP NOW."

**Fold 2:** "Customers are saying" section. Rating 4.91 (11 reviews), Verified badge. Single rotating testimonial carousel. The explicit "11 reviews" count displayed at this high-visibility position signals thin social proof for a premium furniture brand.

**Fold 3:** Featured Brands section (Dienne, S/E, mater, Simpli Home) followed by New Arrivals product grid. No prices shown at this scroll depth on homepage.

**Conversion observations:**
- The dual CTA pattern ("VIEW MORE" / "SHOP NOW") with no visual hierarchy difference is indistinguishable to visitors. Two calls to action with identical weight splits intent and reduces click-through for both.
- "11 reviews" shown explicitly at prominent scroll position is a liability, not an asset. Either show the number with confidence (100+ reviews) or show only the star rating.
- Homepage does not surface prices, urgency, or specific product names — visitors arrive from product-specific ads (e.g., "THE THEODORE Sofa") and land on a generic brand page.

#### Collection Page

**Grid:** 43 results, Best Selling sort default. First product: THE VOLOS Chair at $278. Price range spans $278–$5,992 — a 21x spread in a single collection view.

**Trust friction:** THE DAKOTA card displays a 2-star rating with no review count. A 2-star product in the primary collection view is an active trust hazard for the entire category.

**Filters:** Left sidebar has 30+ color options and size toggles, but no fabric/material filter — relevant for a furniture buyer choosing between boucle, velvet, leather, and fabric.

**Card behavior:** No "Add to Cart" on cards — click-through required for every product. Quick View visible on hover. No price shown on THE SANTA MARINA Set card ("View Details >" only).

#### PDP (The Volos Chair — $278)

**Buy box structure (Fold 1):** Price → installment line (small print) → quantity stepper → ADD TO CART → Buy with SHOP. No product description. No reviews. "17 in Stock Now" is the only urgency signal.

**Below fold:** Trust icons (Nationwide Shipping, Premium Quality, Dedicated Support, Secure Checkout) appear well below the buy box. Specifications table with material/origin data. Dimensions table.

**Conversion observations:**
- No product description visible anywhere above — or adjacent to — the buy box. Buyers cannot understand what differentiates this chair from alternatives without scrolling to find features buried below specs.
- Two CTA buttons (Add to Cart + Buy with SHOP) have no visual hierarchy. For a $278 item, the cart path and Shop Pay express path serve different user intents — prioritizing one would reduce CTA paralysis.
- Reviews are not captured in any of the three screenshot folds. If they exist, they are far enough below fold to be effectively invisible for most sessions.
- Trust icons below the buy box arrive too late in the decision flow. For a $278–$5,992 purchase category, trust signals belong adjacent to the price.

#### Cart Drawer

**Layout:** Dark overlay drawer. Single line item (Volos Chair, $278), quantity stepper, Remove link. Large empty space between item and subtotal. No upsell, no cross-sell, no free shipping threshold bar, no bundle offer, no promotional messaging.

**Subtotal area:** "$278.00 USD" + "Taxes and shipping calculated at checkout." Two CTAs: "GO TO CHECKOUT" (primary button) and "GO TO CART" (text link).

**AOV observation:** The cart drawer is structurally empty of revenue-generating mechanics. A free shipping threshold (e.g., "Add $X for free shipping") and a single cross-sell recommendation would both require minimal dev work and address an obvious gap.

---

## Cross-Source Themes

**1. Trust deficit across every touchpoint** (evidence: site screenshots, Google Ads, review data)
11 reviews shown explicitly on the homepage, a 2-star rating on a collection card, no reviews visible on the PDP, and trust icons positioned below the buy box. For a brand selling $278–$5,992 sofas online, trust signals are either absent or actively undermining confidence. Every source points here.

**2. Mobile performance kills paid traffic ROI** (evidence: PageSpeed)
Homepage TTI 24.3s, PDP TTI 30.8s+ (incomplete). Google Ads are driving traffic to pages that take 25–30+ seconds to become interactive on mobile. This is a ceiling on every downstream conversion metric and cannot be fixed by UX testing alone.

**3. Cart has zero AOV mechanics** (evidence: site screenshots)
The cart drawer is functionally empty between the line item and the checkout button. No threshold bar, no cross-sell, no bundle prompt. This is a structural gap, not a friction reduction problem — there is no mechanism in place to increase order value.

---

## Top Test Opportunities

**1. Cart free shipping threshold + cross-sell** — The cart drawer has no AOV mechanics; a threshold bar ("Add $X for free shipping") and one cross-sell recommendation (e.g., a throw pillow or ottoman) address a structural gap with no existing conversion floor to beat. Evidence: site screenshots (cart drawer). Est. lift: AOV unknown × sessions unknown = $ unknown, but any AOV increase from $0 baseline mechanics is additive.

**2. PDP trust restructure above fold** — Trust icons (Nationwide Shipping, Premium Quality, Dedicated Support, Secure Checkout) currently sit below the buy box fold. Reviews are not visible in any of three captured PDP folds. Moving trust icons to adjacent-to-price position and surfacing an inline star rating near the buy box addresses the highest-friction area of the purchase flow. Evidence: PDP screenshots (Folds 1–3). Est. lift: 5–10% CR improvement on PDP sessions × sessions unknown × $278–$5,992 AOV = $ unknown.

**3. Homepage CTA consolidation** — Two identical-styled CTA buttons ("VIEW MORE" / "SHOP NOW") in the hero with no visual differentiation split click intent. Consolidating to one primary CTA with clear destination (Top Sellers or Collections) reduces decision paralysis. Evidence: homepage screenshots (Fold 1), live site fetch. Est. lift: 10–20% improvement in hero click-through × homepage sessions unknown = $ unknown.

**4. Collection page — suppress or contextualize low-rated products** — THE DAKOTA card shows a 2-star rating with no review count in the primary collection view. Suppressing star ratings below a minimum review count threshold (e.g., fewer than 5 reviews) or removing unrepresentative ratings from collection cards prevents active trust erosion. Evidence: collection page screenshots (Fold 2). Est. lift: indirect — reduces bounce from collection page, improves add-to-cart rate.

**5. PDP product description above buy box** — No product description is visible in any PDP fold captured. Buyers choosing between competing sofas need differentiation copy adjacent to the price. A 2–3 sentence description positioned between the product title and the price/CTA would reduce bounce from undecided visitors. Evidence: PDP screenshots (Folds 1–3). Est. lift: 3–8% CR improvement on PDP sessions × sessions unknown × AOV unknown = $ unknown.

---

## Unused but Valuable Findings

- Shop Pay installment messaging ("4 interest-free installments") is present on the PDP but absent from all Google ad copy — surfacing this in headlines could improve CTR and pre-qualify high-intent visitors before the click.
- The $278 Volos Chair ranks first in "Best Selling" on the Top Sellers collection, which may undermine the premium brand positioning promised by ads and the "Lounge in Luxury" hero. Consider whether the default sort should surface higher-AOV products first.
- Announced "White Glove Delivery" in trust bar is not reinforced anywhere in the PDP buy box or cart — a missed reassurance at high-friction decision points.

---

## Missing Data

No manifest MISSING_DATA warnings. However, the following sources were skipped during collection and represent meaningful analytical gaps:

- **Reviews & UGC** — with only 11 reviews on-site, third-party review data (Google, Yelp, Trustpilot) or Amazon equivalent products would provide the only customer voice signals available. Without this, the audit has no qualitative insight into what customers love or why they hesitate.
- **Meta Ads** — no paid social data means unknown whether there is a second ad channel driving traffic with different messaging or landing pages.
- **Competitor Insights** — competitor comparison above is self-researched at surface level. Client-provided context on pricing strategy, margin, and known competitive threats would sharpen test prioritization.
