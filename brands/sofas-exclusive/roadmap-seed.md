# Sofas Exclusive Roadmap Seed

**Store:** https://sofasexclusive.com/
**AOV:** Unknown (product range: $278–$5,992; best-selling sort surfaces a $278 chair first)
**Monthly sessions:** Unknown
**Data sources:** Google Ads (Transparency), PageSpeed/Core Web Vitals (Lighthouse 13.2.0, mobile, 2026-06-15), site screenshots (homepage, collection, PDP, cart drawer), live site fetch

## Key Insights

Trust is the primary conversion barrier across every touchpoint. The site has 11 total reviews — displayed explicitly on the homepage at a high-visibility position — for a brand selling sofas up to $5,992. The homepage testimonial section leads with "4.91 ★ (11)" rather than burying the count, which actively signals thin social proof. On the collection page, THE DAKOTA card shows a 2-star rating with no review count displayed, creating an isolated trust hazard in the primary browsing flow. The PDP buy box has no visible reviews in any of three captured folds, and trust icons (Nationwide Shipping, Premium Quality, Dedicated Support, Secure Checkout) sit well below the add-to-cart button — arriving after the visitor has already decided to scroll past the purchase decision.

Mobile performance sets the ceiling for all conversion work. The homepage scores 53/100 on Lighthouse mobile with LCP 7.5s, Speed Index 11.5s, and TTI 24.3s. The PDP hit the Lighthouse time limit — TTI of 30.8s is flagged as incomplete, meaning the true figure is higher. Google Ads are driving paid traffic to pages that take 25–30+ seconds to become interactive on mobile. CLS on the homepage is 0.163 — in the "needs improvement" band — meaning elements visibly shift during load, disrupting early trust formation. These numbers cap the uplift available from any UX or copy test.

The cart drawer is structurally empty of revenue mechanics. Between the single line item and the checkout button sits a large blank space with no free shipping threshold bar, no cross-sell, no bundle prompt, and no urgency messaging. The store's ad copy mentions free shipping but the cart makes no reference to it as a threshold incentive. Two checkout CTAs ("GO TO CHECKOUT" button and "GO TO CART" text link) split exit intent. Every order that passes through checkout without an upsell is a missed AOV opportunity against a zero baseline.

## Top Test Opportunities

### 1. Cart Free Shipping Threshold Bar + Cross-Sell
**What's broken:** The cart drawer is a dark overlay sliding in from the right. It shows one line item (product thumbnail, name, quantity stepper, Remove link, price) then a large visually empty section — approximately 40–50% of the drawer height — before the subtotal block. The subtotal block shows "$278.00 USD," "Taxes and shipping calculated at checkout," and two CTAs stacked vertically: "GO TO CHECKOUT" (full-width light button) and "GO TO CART" (text link below). The empty section contains no messaging, no visual elements, and no product recommendations. Free shipping is announced in the site-wide announcement bar but is not referenced in the cart at all.
**Evidence:** Cart drawer screenshot, announcement bar (live site fetch), Google Ads mentioning free shipping
**Key data:** Empty space spans the majority of the cart drawer between item and subtotal; announcement bar confirms free shipping offer exists but is not reinforced at checkout entry
**Est. lift:** AOV unknown × sessions unknown = uncalculated, but additive from $0 baseline — any cross-sell conversion is pure gain

### 2. PDP Trust Restructure Above Fold
**What's broken:** On the Volos Chair PDP, the right-side buy box stacks in this order from top: breadcrumb ("Sofas Exclusive"), product name ("THE VOLOS Chair"), price ("USD 278.00"), shipping line ("Shipping calculated at checkout"), Shop Pay installment line (small text), quantity stepper, "ADD TO CART" button (dark charcoal, full-width), "Buy with SHOP" button (purple, full-width), stock indicator ("17 in Stock Now"). Four trust icons — NATIONWIDE SHIPPING, PREMIUM QUALITY, DEDICATED SUPPORT, SECURE CHECKOUT — appear below this entire block, in a separate section well below the fold. No star rating or review count appears anywhere in the buy box or adjacent to the price. The installment line ("4 INTEREST-FREE INSTALLMENTS, OR FROM $25.09/MO WITH Shop Pay") is present but in small secondary text with no visual prominence.
**Evidence:** PDP screenshots (Folds 1–3), homepage review count (11 total), collection card observations
**Key data:** 11 total reviews on-site; no reviews visible in three PDP folds captured; trust icons positioned below both CTA buttons; installment option present but de-emphasized
**Est. lift:** 5–10% CR improvement on PDP sessions × sessions unknown × $278–$5,992 price range = uncalculated

### 3. Homepage Hero CTA Consolidation
**What's broken:** The homepage hero has a full-width lifestyle sofa image (curved cream/white sofa in an earthy interior) with a centered white headline "Lounge in Luxury" and subheadline "Experience furniture crafted to blend modern aesthetics." Directly below the subheadline sit two side-by-side white rectangular buttons of identical size, color, weight, and styling: "VIEW MORE" on the left and "SHOP NOW" on the right. There is no visual hierarchy, no color differentiation, no size difference, and no copy distinction that would help a visitor know which to choose or what each leads to.
**Evidence:** Homepage screenshot (Fold 1), live site fetch confirming dual CTA presence
**Key data:** Both CTAs are styled identically — same white background, same border, same text weight; no destination is implied by either label
**Est. lift:** 10–20% improvement in hero CTA click-through × homepage sessions unknown = uncalculated

### 4. Collection Page — Suppress Unrepresentative Low Ratings
**What's broken:** In the collection product grid (Best Selling sort, 43 results), THE DAKOTA Curved Sectional Sofa card shows a visible 2-star rating displayed directly on the card with no review count shown. This card appears in the second row of the grid alongside normally priced, higher-rated products. The rating renders as a star graphic without context — no "(1 review)" qualifier, no indication this is a single outlier — making it read as a low-quality product signal in a collection otherwise positioned as premium.
**Evidence:** Collection page screenshot (Fold 2)
**Key data:** 2-star rating visible with no count; displayed alongside products with no ratings shown; top of page is labeled "TOP SELLERS"
**Est. lift:** Indirect — reduces category-level bounce; prevents trust erosion for adjacent products in the grid

### 5. PDP Product Description Above Buy Box
**What's broken:** On the Volos Chair PDP, the buy box goes directly from the product name to the price with no description, no benefit statement, and no copy that communicates what the chair is or why to buy it. A "Specifications" table (Origin: United States, Main Color: Everest Green, Material: Wood+Fabric, Filler: High Density Foam, Wood Type: Eucalyptus, Upholstery: Velvet) and a "Dimensions & Weights" table appear below the fold. A "Product Features" heading appears at the bottom of Fold 3 with body text cut off. No description text appears above or adjacent to the add-to-cart button in any captured fold.
**Evidence:** PDP screenshots (Folds 1–3)
**Key data:** Zero description text in buy box; specs table is below fold; features section is at the bottom of third fold; Google Ads use lifestyle/aspiration copy ("sophistication and exploration") that is not reflected anywhere on the PDP
**Est. lift:** 3–8% CR improvement on PDP sessions × sessions unknown × AOV unknown = uncalculated

## Unused Findings

- Shop Pay installment messaging exists on the PDP but is absent from all Google ad headlines — surfacing "4 interest-free payments" in ad copy could improve CTR and pre-qualify high-intent traffic before the click.
- The $278 Volos Chair surfaces first in the "Best Selling" sort on the Top Sellers collection, creating a $278 anchor on a page meant to present premium positioning; adjusting default sort to AOV-weighted or margin-weighted could increase session value.
- "White Glove Delivery" is announced in the trust bar but not mentioned in the PDP buy box or cart — a missed reassurance at the two highest-friction decision points in the funnel.
