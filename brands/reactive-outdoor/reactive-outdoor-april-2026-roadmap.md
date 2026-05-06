# Reactive Outdoor CRO Research Brief

**Data Sources:** Meta Ads, Google Ads, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots, CRO Ebook, CRO Community Research

---

## Insights

The biker/motocamping segment is Reactive Outdoor's top-performing product. Every active Meta ad (out of many running campaigns) funnels high-intent buyers to a landing page. Their best ad drops the biker hook the moment a visitor arrives. "BEST BIKER TENT EVER!" becomes "Easiest Camping Tent Setup Revealed." That mismatch is costing conversions on the page that matters most.

The reviews tell a consistent story: buyers love the setup speed, but they're regularly surprised by how small the tent is. Over 15 reviews across Trustpilot and Amazon, from buyers in the US, AU, and GB, describe the "2-3 person" tent as a 1-person tent in practice. "WAY too small" (Brett, AU). "1.5 person tent at best" (Neilio, GB). "I'm 5'4" and I barely fit" in the 1-2 person size (Alyssa, US). This is the most documented friction point in the data. The product detail page does not show a single dimension or size guide in the buy box. Worse, there is no price visible until the cart.

The cart drawer has a significant empty space where an upsell should live. A buyer at $199.95 with purchase intent is the highest-value moment on the site. That space is generating $0 in additional revenue today. Industry data from Zipify (October 2025) shows cart upsells averaging 20-30% AOV lift with a 10% take rate.

Mobile page speed is severe: LCP of 15.9s on the homepage and 9.8s on the best-performing landing page. Every second above 3s LCP costs conversions. These numbers represent a structural drag on every dollar of ad spend going to the site.

The three tests below target the highest-leverage moments in the funnel: the top-performing landing page hero, the PDP buy box (where size anxiety is killing decisions), and the cart (where there is free money sitting uncaptured).

---

## Slot 1: Biker Landing Page Hero: Message Match

**Type:** A/B test (1 variation vs. control)
**Page:** de.reactiveoutdoor.com/pages/ro-editorial-biker-us-2
**Revenue potential:** Reactive Outdoor's top-performing product with multiple active Meta ads driving to this page. A conservative 10% relative lift in conversion rate on this page directly compounds against all paid spend pointing to it. Without internal session data, a precise number isn't possible, but this is the highest-leverage single test in the funnel.

**Hypothesis:** If we replace the generic "Easiest Camping Tent Setup Revealed" hero headline with a motocamping-specific headline that mirrors the ad creative, conversion rate will increase because visitors arriving from a "BEST BIKER TENT EVER!" ad will immediately see their context reflected on the page, reducing the cognitive mismatch that causes drop-off.

**Data:** The biker ad (started April 13, 2025) uses "BEST BIKER TENT EVER!" as its headline, yet the landing page hero opens with "Easiest Camping Tent Setup Revealed." A generic headline with no motocamping identity. (Source: Meta Ads, Landing Page Screenshots) The motocamping angle appears only in fold 2: "Transform Your Motocamping Experience." By fold 2, a large share of mobile visitors have already bounced. Motocampers self-identify as the ideal buyer in reviews: Luis (ES) specifically notes the tent is "perfect for motorcycle trips where you only spend a single night in the same place." Matthew (US) cites it as his go-to for motorcycle camping. Celia (US) bought it specifically because of mobility limitations on her bike. (Source: Reviews) This segment is real, validated, and self-selecting. The landing page just fails to confirm their choice at first glance. (Source: Non-data Context) Industry evidence shows hero section personalization matching visitor source consistently increases conversion. One case study found an 80% increase in add-to-cart rate when hero images matched visitor interest segment. (Source: CRO Community Research)

**V1:** Replace the hero headline with: **"The Fastest Tent on Two Wheels."** Subheadline: "Park your bike. Pull it out. Camp in seconds. The 3 Secs Tent is built for riders who don't waste time." Keep everything else identical to control: the countdown timer, the 56,830+ review count, the three checkmarks (Quick & Easy Setup, Durable & Weatherproof, Thoughtful Features), and the "Check Availability →" CTA. On mobile, the headline stacks to two lines, remains left-aligned, and sits above the countdown timer exactly as the current layout does. On desktop, the headline occupies the same centered position as the control, with the same font weight and size hierarchy. No other element changes. The goal is to isolate the headline's impact on conversion with no confounding changes.

---

## Slot 2: PDP Buy Box: Price Visibility and Size Selector

**Type:** A/B test (1 variation vs. control)
**Page:** reactiveoutdoor.com (3 Secs Tent product page)
**Revenue potential:** The PDP is the last stop before the cart. Size misrepresentation is the single most documented complaint in the review data: 15+ reviews across two platforms from three countries. Every buyer who purchases the wrong size represents a return, a negative review, or a lost repeat purchase. A 5% relative conversion lift on the PDP combined with a reduction in return rate compounds directly into margin. If 5,000 sessions/month hit the PDP at a 3% conversion rate and $199.95 AOV, a 5% lift adds approximately 7-8 purchases/month, or roughly $1,400-1,600 in monthly revenue, before accounting for return rate improvement.

**Hypothesis:** If we add a size selector with explicit floor dimensions and use-case framing, plus make the price visible in the buy box, conversion rate will increase and return rate will decrease because buyers will self-select the correct size and won't be surprised by the price at cart. These are two of the top drivers of abandonment and returns in the current funnel.

**Data:** The PDP buy box shows no price at any point above the cart. Price only appears after clicking "GET YOURS NOW!" and reaching the cart ($199.95). The CRO ebook (Dylan Ander, "Billion Dollar Websites") directly addresses this: "Do not 'bury' your price, no matter how high the price is. Users do not like the feeling of hunting down a price. That excitement turns into anxiety or frustration." (Source: CRO Ebook, PDP Screenshots) On size: "Significantly smaller than advertised" (Lily Lee, US, Aug 2025). "WAY too small, I'm only 188cm" (Brett, AU, May 2025). "3 person is definitely not 3 person, only 2 could fit" (Mark F, AU, Apr 2026). "I'm 5'4" and I barely fit without touching the sides" in the 1-2 person tent (Alyssa, US). Amazon reviews: "gonna be smaller than what you are thinking" (Michael, Amazon, Sep 2025). (Source: Reviews) The PDP buy box currently has no size selector, no dimensions, and no use-case guidance visible above the fold. All size information is buried in the collapsed Features accordion. (Source: PDP Screenshots) The sticky bottom bar CTA says "SEE TENT SIZES" while the buy box CTA says "GET YOURS NOW!": inconsistent signals that suggest the size decision is expected to happen somewhere, but isn't supported in the primary conversion area. (Source: PDP Screenshots)

**V1:** In the buy box, directly above the "GET YOURS NOW!" CTA button, add two changes:

**Change 1: Price.** Display the price prominently: "~~$519.80~~ **$199.95** (62% off)" in a minimum 18px font. Include the "Save 62%" badge immediately adjacent in the same style as the cart drawer badge. This applies identically on mobile and desktop.

**Change 2: Size Selector with Dimensions.** Add a size selector above the price with two options:
- "Small (1-2 Person) | Floor: 7.5ft x 3.4ft | Best for: solo rider, ultralight pack"
- "Large (2-3 Person) | Floor: 8.2ft x 4.6ft | Best for: solo camper with gear, couples close quarters"

Below the selector, add one line of guidance in a small font: "Sleeping with an air mattress or over 6ft tall? Go Large." This text is static and not toggle-dependent.

On mobile, the size selector displays as two tappable pill buttons stacked or side-by-side depending on screen width, with the dimension text visible beneath the selected option. On desktop, the selector sits in the right-hand buy box column with the same layout. All other buy box elements (benefit bullets, trust icons, delivery estimate, payment icons, accordions) remain identical to control.

Note: Exact floor dimensions should be confirmed from product specs before implementation. Placeholder dimensions above are approximate from review descriptions and should be verified with the client.

---

## Slot 3: Cart Drawer: Upsell Section

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide)
**Revenue potential:** The cart drawer has a large empty space between the product line item and the urgency/checkout section. A buyer at $199.95 in the cart has committed to purchase intent. Industry data (Zipify, October 2025) shows cart upsells averaging 20-30% AOV lift with a 10% upsell take rate, comparable to post-purchase upsell performance. If 1,000 buyers/month reach the cart and 10% take a $50 upsell, that is $5,000 in incremental monthly revenue at near-zero marginal cost.

**Hypothesis:** If we add a contextual product recommendation in the empty space of the cart drawer, AOV will increase because buyers who have already committed to a purchase are in the highest-intent state on the site, and a relevant, lower-priced addition requires minimal decision-making.

**Data:** The cart drawer shows a large empty white space between the product item and the "Hurry up! Only a few left in stock!" row. No upsell, cross-sell, or product recommendation exists. (Source: Cart Screenshot) The CRO ebook: "On-page upsells are a powerful way to increase revenue on your website. They appear on Homepages, Product Pages, and most often, your Cart. Typically, you want your upsell products to be less expensive than the product the customer came to buy." (Source: CRO Ebook) Changing copy in a cart drawer product recommendation widget increased AOV by 21.18% and revenue per visitor by 40.37% in a documented split test. (Source: CRO Community Research, blendcommerce.com)

**V1:** In the empty space of the cart drawer, between the product line item and the "Hurry up!" row, add a product recommendation card. The card contains: a small product thumbnail image, a short product name, a one-line benefit, the price, and a green "Add" button. Recommended upsell candidate: the HighGround Truck Tent (if lower-priced than the main cart item) or a standalone camping accessory from the catalog. The specific product should be selected based on two criteria: (1) it must be less expensive than the current cart item, and (2) it must be complementary: something a 3 Secs Tent buyer would naturally use together.

On mobile, the card sits full-width between the product row and the urgency row. On desktop, the card uses the same full-width layout within the drawer column. The "Add" button triggers an in-drawer add without closing the drawer or navigating away. The existing trust icons (1-Year Money Back, Free Domestic Shipping), subtotal, and "PROTECTED CHECKOUT" CTA remain below, unchanged. If the buyer adds the upsell, the cart updates inline and the subtotal reflects the new total.

If no single product is an obvious fit at a lower price point, test a "Complete Your Setup" upsell offering a tent care kit, waterproofing spray, or a spare peg set. The specific product decision should be made with the client before implementation.

---

## Future Slot Candidates

These didn't make the top 3 but are queued for the next cycle:

1. **Homepage Hero: Discount Conflict and Country Selector.** The announcement bar says "62% OFF" while the hero badge says "SITEWIDE 50% off." Two different numbers in the same view. The green "Shopping Country/Store [SELECT]" bar adds friction before a visitor has seen the product. Test: remove or collapse the country selector; unify discount messaging to a single number.

2. **Biker Landing Page: Takedown Social Proof.** The #2 review complaint is that takedown is harder than advertised. The landing page copy says "Truly 1-Person Setup & Pack Away (Yes, You Can Do It Alone)." Test adding a "How to Take Down in 60 Seconds" video or GIF in fold 2 to proactively address the objection before the buyer reaches the cart.

3. **Mobile Page Speed: Technical Sprint.** Homepage LCP is 15.9s on mobile (April 25, 2026). Landing page LCP is 9.8s. Both are in the red. A focused performance sprint (image compression, unused JS removal, lazy loading) targeting a sub-4s LCP would lift conversion across all paid traffic. Not a standard A/B test. More suitable as a development sprint with before/after measurement.
