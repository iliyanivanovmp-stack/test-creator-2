# Natures Collection CRO Research Brief

**Data Sources:** Google Ads Transparency, Page Speed / Core Web Vitals, Competitor Research (Sheepskinhouse, Nordic Sheep), Site Screenshots (Homepage, Collection, PDP, Cart)

---

## Insights

Natures Collection has a stronger product story than its website tells. A 20-year product warranty, complimentary delivery, and free returns are real differentiators in a market where competitors compete on discount depth. But none of these are visible when a visitor is deciding whether to add to cart. They live in the footer. The site's editorial aesthetic is beautiful, but beauty without conversion structure is just a brochure.

Every competitor observed in Google Ads (Sheepskinhouse, Nordic Sheep, Saueskinner) leads with 40-75% off spring sale messaging. Natures Collection runs no active promotion. That gap in perceived value is significant when a shopper is comparing options. NC's premium positioning needs to be earned on-page with trust signals, social proof, and friction reduction. Right now, it is not.

The data converges on three problems. First, the PDP buy box is stripped of all reassurance: no warranty mention, no return policy, no Klarna BNPL option, not even a review count. Nordic Sheep shows 791 reviews and Klarna at the point of purchase. NC shows a SKU code and a gray button. Second, the cart is completely empty of conversion opportunity: no upsell, no BNPL, no trust signal, and two identically styled buttons with no clear primary action. For a brand selling €99-€899 items, the cart is leaving AOV on the table on every single transaction. Third, the homepage first fold has no CTA and no trust bar, meaning visitors who land on the homepage must scroll twice and find their own way to a product.

Underneath all of this: the homepage loads at 34/100 performance score with a 30MB payload and a 22.5-second lab LCP. The PDP is 45/100. Both fail Core Web Vitals. Every test we run will underperform until page speed is addressed. We recommend treating it as a parallel workstream, not a future consideration.

The opportunity: NC has the product quality and brand story to convert at a materially higher rate. The three tests below each target a confirmed friction point, supported by multiple data sources. Even conservative lifts at their price points add up quickly.

---

## Slot 1: PDP Buy Box - Trust Bar + BNPL

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages, all (e.g., naturescollection.eu/products/[any-rug-or-product])
**Revenue potential:** Without analytics access, we estimate conservatively: if top rug PDPs receive 8,000 sessions/month at a 1.5% current CR and a 15% relative lift from trust signals (in line with published benchmarks showing 11-23% ATC lift from trust signal placement near ATC), that is 18 additional orders at €130 average AOV = €2,340/month from CR alone. This estimate is a floor, not a ceiling, and does not include AOV impact from Klarna adoption.

**Hypothesis:** If we add a 3-point trust bar and Klarna BNPL messaging directly below the ATC button on all PDPs, add-to-cart rate will increase because visitors are currently making a €99-€899 purchase decision with zero reassurance at the point of action.

**Data:** NC's Google search ad leads with "100 days free return" and "free 2-3 days worldwide delivery" (Source: Google Ads) but neither appears anywhere on the PDP buy box. The 20-year warranty is only in the footer (Source: Site Screenshots - PDP). Klarna is accepted but communicated exclusively via a small footer payment icon (Source: Site Screenshots - Cart, Homepage). Nordic Sheep displays Klarna, MobilePay, and Apple Pay prominently near their buy button and shows a 100-day return policy in the buy box (Source: Competitor Research). Published data from Blend Commerce (2024) shows moving return policy from footer to near ATC produces a +23% add-to-cart lift. Trust signals at the point of purchase decision have produced +32.7% CR improvements in practitioner-reported tests (2024). The CRO ebook (Billion Dollar Websites, Ch. 9) states BNPL has "never once" produced a negative result and is especially effective on high-ticket items. NC's SKU ("NCL1020-1-96") is prominently displayed below the product title on every PDP, a B2B artifact that creates uncertainty for retail shoppers (Source: Site Screenshots - PDP).

**V1:** All changes apply to the buy box only. No changes to the product image gallery, description, or related products section.

Remove the SKU field from the PDP entirely (or move it to a collapsed "Product Details" accordion).

Below the price (and above the color selector), add a Klarna BNPL line in small text: "Pay in 3 with Klarna. No interest." with the Klarna logo inline. The exact installment amount should be dynamic based on the product price (e.g., "3 x €33" for a €99 product). On desktop, this line sits between the price and the color swatches. On mobile, it appears in the same position, stacked below the price.

Below the ADD TO CART button, add a horizontal 3-column trust icon bar with the following items: "20-Year Warranty" with a shield icon | "Free Delivery" with a truck icon | "Free Returns" with a circular arrow icon. On desktop, the three items display in a single row below the ATC. On mobile, the three items stack as a horizontal scrolling strip or display in a 3-column single row if screen width allows (minimum 320px width). The iconography and typography should match the existing NC brand system: minimal, sans-serif, no color other than dark gray.

The ADD TO CART button itself remains the same size and position. Do not change the button color in this variation to isolate the trust bar and BNPL as the causal variables.

---

## Slot 2: Cart Drawer - Upsell + BNPL + Trust

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (site-wide, triggered by any add-to-cart action)
**Revenue potential:** If NC processes 400 cart sessions/month and a contextually relevant upsell converts at 10% (lower end of published 8-15% benchmark for in-cart relevant offers) at an average upsell item price of €50 (care brush €19, cushion €89, slippers €99 - avg approx. €50): 400 x 10% x €50 = €2,000/month in incremental AOV. If BNPL visibility reduces cart abandonment by 5% among high-AOV visitors: 400 x 5% x €150 avg AOV = €3,000/month. Combined floor estimate: €5,000/month.

**Hypothesis:** If we add one contextual product recommendation and Klarna BNPL messaging to the cart drawer, AOV and cart-to-checkout rate will increase because visitors currently see an empty canvas with no reason to add more and no reassurance before checking out.

**Data:** The cart drawer is empty white space below the single line item, with no cross-sell, no trust signal, and no BNPL messaging (Source: Site Screenshots - Cart). Both the VIEW CART and CHECKOUT buttons are identical in color and visual weight, which removes clear call-to-action hierarchy (Source: Site Screenshots - Cart). NC's product catalog has natural pairings: a sheepskin rug pairs with a matching cushion, a care brush, or sheepskin slippers. The CRO ebook (Ch. 10) identifies the cart as the single best moment to upsell: "The best time to ask for a sale is after a customer has already decided to purchase from you." In-cart contextually relevant offers convert at 8-15%, compared to 2-4% for generic recommendations (practitioner benchmarks, 2024-2025). A 32% AOV increase has been documented from adding dynamic in-cart upsell banners (Swanky Agency case study). NC accepts Klarna but does not communicate it anywhere near the checkout button (Source: Site Screenshots - Cart, Homepage).

**V1:** All changes apply to the cart drawer only. The cart page (full page, separate from the drawer) is not changed in this test.

In the empty white space below the line item(s) and above the order note link, add a "Complete the Look" section. This section shows exactly one product recommendation, dynamically selected based on what is in the cart. Logic: if a sheepskin rug is in the cart, recommend the matching-size Long Wool Sheepskin Cushion (€89). If apparel is in the cart, recommend a complementary accessory. If the care brush or cleaning item is in the cart, recommend a sheepskin product. The recommendation card includes: a small product thumbnail (60x60px), product name in one line, price, and a single "Add" button. On desktop, the card displays as a single horizontal row (thumbnail left, name and price center, Add button right). On mobile, the same layout applies, sized to the narrower drawer width.

Above the CHECKOUT button, add one line of Klarna BNPL text: "Or pay in 3 with Klarna." in small gray text with the Klarna logo inline. This line appears between the "Taxes and shipping included" text and the CHECKOUT button. On both desktop and mobile, it is left-aligned with the other footer text in the cart drawer.

Differentiate the two CTA buttons: CHECKOUT becomes the primary button (darker, solid fill - use the same charcoal as the current ATC button). VIEW CART becomes a secondary button (outlined or lighter weight, same width). The checkout button continues to display the total (e.g., "CHECKOUT - €99,00"). On mobile, button stacking order remains: primary CHECKOUT button on top, secondary VIEW CART below.

Below the CHECKOUT button (outside the button, below it), add one line of trust text: "20-Year Warranty. Free Delivery. Free Returns." in a small, muted typeface. No icons in this version to keep the implementation simple and the test attributable.

---

## Slot 3: Homepage - Trust Bar + Hero CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (naturescollection.eu)
**Revenue potential:** The homepage is the top-of-funnel entry point for all direct, branded, and many paid traffic visitors. Without analytics access, a conservative model: if the homepage receives 15,000 sessions/month and a trust bar + hero CTA improves click-through to product pages by 8% relative (from, say, 55% to 59%), that is 600 additional visitors entering the product funnel per month. At a 1.5% CR and €130 AOV: 600 x 1.5% x €130 = €1,170/month. This is a conservative downstream estimate and does not capture improvements in time-on-site or direct add-to-cart from the homepage.

**Hypothesis:** If we add a trust icon bar below the navigation and a hero CTA button on the first fold, click-through to product pages will increase because visitors currently land on a first fold with no clear action and no stated reason to trust or buy.

**Data:** The homepage first fold is full-bleed editorial photography with no headline, no hero CTA, and no trust signals (Source: Site Screenshots - Homepage). The 20-year warranty, free delivery, and free returns appear only in the footer (Source: Site Screenshots - Homepage, Cart). Competitors Sheepskinhouse and Nordic Sheep both show a trust bar above the fold with returns, delivery, and product guarantees (Source: Competitor Research). NC's Google search ad copy leads with "100 days free return" and "free 2-3 days worldwide delivery" (Source: Google Ads) - these conversion levers are being used to attract clicks in paid search but are absent when visitors land on the homepage. The homepage performance score is 34/100 with a 22.5-second lab LCP (Source: Page Speed), which means a portion of mobile visitors bounce before any content loads. The B2B LOGIN nav item appears at the same visual weight as PRODUCTS and SUPPORT, which may signal to retail visitors that the site is primarily trade-facing (Source: Site Screenshots - Homepage).

**V1:** Two changes only. No changes to the hero image, product category tiles, navigation structure, or footer.

Add a sticky trust icon strip that appears between the navigation and the hero image. The strip contains four items in a single row: "20-Year Warranty" | "Complimentary Delivery" | "Free Returns" | "Handcrafted in Denmark." Each item is separated by a thin vertical divider. The strip uses a light background (off-white, consistent with the site's neutral palette), small sans-serif text, and minimal icons. On desktop, all four items display in one row. On mobile, the strip cycles through items as a scrolling ticker or marquee at a comfortable reading pace, showing 2 items at a time. The strip is sticky and remains visible as the user scrolls down.

On the first fold hero image, add a single CTA button: "Shop Sheepskin Rugs" (linking to naturescollection.eu/collections/sheepskin-rugs). The button is overlaid on the lower-center area of the hero image, positioned above any overlapping category tiles. Styling: white text on a semi-transparent dark background (matching the editorial aesthetic, not a brightly colored button that would clash with the imagery). On desktop, the button is horizontally centered on the full-width hero. On mobile, the button is centered and minimum 44px height for tap accessibility. The button text "Shop Sheepskin Rugs" uses the same capitalization style as other site CTAs.

---

## Future Slot Candidates

These test ideas are supported by the data but did not fit into the three prioritized slots:

1. **Collection page social proof:** Add review star ratings (count and score) to all product cards. If NC has no review system installed, this requires a reviews app as a prerequisite. Nordic Sheep shows 791 reviews; NC shows none. The absence of reviews is the most visible trust gap in the competitive set.

2. **Homepage hero: email capture with first-order offer.** Nordic Sheep converts homepage traffic with a 10% off popup. NC has no email capture mechanism observed. A welcome offer (10% off first order or a free care guide) could convert browsing visitors into leads for retargeting.

3. **Page speed as prerequisite workstream.** The homepage's 30MB payload and 22.5s LCP will suppress all test results. Removing unused JS (1,176 KB savings identified), compressing images (249 MB savings identified), and addressing render-blocking requests should be treated as a mandatory prerequisite, not a future test. This is a dev workstream, not a slot.

4. **PDP description copy:** Replace the generic maintenance-focused copy with copy that leads with the 20-year warranty, sourcing story, and Danish craftsmanship. This tests whether the product story (vs. product specs) drives higher ATC.

5. **Announcement bar expansion:** The current bar only rotates "COMPLIMENTARY DELIVERY." Adding "20-Year Warranty" and "100-Day Free Returns" as additional slides would add trust messaging at zero cost and could be a quick win before a formal test.
