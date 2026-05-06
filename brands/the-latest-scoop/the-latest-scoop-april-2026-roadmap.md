# The Latest Scoop CRO Research Brief

**Data Sources:** Meta Ads, Google Ads, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots, CRO Ebook Reference

---

## Insights

The single biggest finding from the data is structural: The Latest Scoop is investing in paid media to drive traffic to a site that is losing visitors before the page even loads. Mobile LCP of 72.6s on the homepage and 48.8s on the PDP means that on the most important device for fashion shoppers, most visitors see nothing but a blank screen for nearly a minute. This is not a conversion rate problem. It is a traffic waste problem that sits upstream of everything else.

The second finding is that the site offers no social proof at any stage of the funnel. No review stars on collection grids. No review count on PDPs. No testimonials on the homepage. For a 20-year-old brand with 13 locations, this is a significant missed asset. Customers considering a $165 pair of jeans have no signal that anyone else bought them, liked them, or found the fit true to size. The Facebook reviews that are publicly visible are negative - complaints about return policy, quality, and customer service. The absence of owned positive reviews leaves that negative perception unchallenged at the exact moment a visitor is deciding whether to buy.

The cart compounds the AOV problem. Every session that adds to cart arrives in a drawer with empty white space below the line item and no product recommendations. A Logan Jean cart ($165) is $35 short of the $200 free shipping threshold. That gap sits in a blank white void with no suggestion of what to add.

Three data sources - reviews, site screenshots, and Google Ads - point to the same root issue: the brand is not building trust fast enough with first-time online visitors. Google Ads run fall messaging in late April (message match gap). The buy box hides the return policy behind a tab. Product photography mixes ghost mannequins with model shots in the same grid, creating quality doubt before a visitor even clicks a product. For a brand that has earned significant loyalty in-store, the online experience is not doing that reputation justice.

If session data confirms these estimates (verify in Shopify analytics), a conservative 15% lift in PDP conversion rate on ~15,000 monthly PDP sessions at $130 CAD average order value would generate approximately $29,000 CAD in additional monthly revenue from Slot 1 alone.

---

## Slot 1: PDP Trust Signal Overhaul

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Pages, starting with top-selling products (e.g., thelatestscoop.ca/products/logan-high-rise-dad-jean-dark-blue)
**Revenue potential:** ~15,000 PDP sessions/mo (estimate; verify in Shopify) x 1.5% conservative CR lift x $130 CAD AOV = ~$29,000 CAD/mo. Estimate requires actual session data to validate.

**Hypothesis:** If we surface customer reviews and the return policy directly in the buy box, and lead with the model photo instead of the ghost mannequin, PDP conversion will increase because visitors gain the purchase confidence currently missing at the point of decision.

**Data:** Zero customer reviews appear anywhere on the PDP for a $165 item, removing the most trusted form of social proof at the moment of decision (Source: Site Screenshots). Facebook reviews show customers questioning quality and feeling misled by the return policy, both of which could be addressed by displaying reviews and proactively surfacing the actual 14-day refund policy (Source: Reviews & UGC). The ghost mannequin is the first image on the PDP, while the more compelling on-figure model photo is second - visitors on mobile who don't swipe never see it (Source: Site Screenshots). Trust signal improvements have been shown to lift new visitor conversion by 12-24% in controlled studies (Source: Conversion Rate Experts Trust Study, 2024). The CRO ebook identifies buy box social proof as one of the five highest-leverage PDP optimizations (Source: CRO Ebook, Chapter 6).

**V1:**

*Image gallery:* Swap image order so the on-figure model photo (woman wearing the jeans with a black top, full body) is displayed first. The ghost mannequin photo moves to second position. This applies to all product images across the test. On mobile, the first swipe image is the model shot. On desktop, the model shot is the primary large image in the left panel.

*Review display:* Add a reviews app (e.g., Judge.me or Okendo) and display a star rating and review count directly below the product name in the buy box: e.g., "4.6 (38 reviews)" as a clickable link that scrolls to the reviews section. If no reviews exist at test launch, implement a review collection flow (post-purchase email sequence requesting reviews) for 2-4 weeks before starting the test, so the variation has data to display. On mobile and desktop, the star rating appears below the product title, above the price.

*Return policy snippet:* Add a one-line return policy note directly below the ADD TO BAG button: "Free returns within 14 days. No questions asked." This is not a new policy - it is the existing published policy made visible where it counts. On mobile, this line appears immediately below the full-width checkout button. On desktop, it appears in the right-side buy column below the button.

*Size guide link:* Add a "Size Guide" text link next to the SIZE label in the buy box. Clicking opens a modal overlay with a size chart. This applies to all clothing PDPs. On mobile, the link appears inline next to "SIZE:" as a small underlined text link. On desktop, same placement in the buy column.

No other changes to the page. Control is the current PDP as-is.

---

## Slot 2: Cart Cross-Sell for AOV and Free Shipping Nudge

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (site-wide, all products)
**Revenue potential:** ~5,000 cart sessions/mo (estimate; verify in Shopify) x 10% conservative AOV lift x $130 CAD AOV = ~$6,500 CAD/mo in additional revenue. Cart cross-sell studies show 10-30% AOV lift; 10% used here as floor estimate.

**Hypothesis:** If we add a curated cross-sell section inside the cart drawer that surfaces complementary products relevant to what is already in the cart, AOV will increase because visitors in the cart are in an active buying state and currently see nothing to add.

**Data:** The cart drawer has a large empty white space below the line item with no product recommendations of any kind (Source: Site Screenshots). A $165 cart is $35 short of the $200 free shipping threshold, with no prompt to add a complementary item to close that gap (Source: Site Screenshots). The CRO ebook states: "Cross-selling tactics become four times more efficient if you show the customer the related product in their shopping cart, just before they proceed to checkout" and dedicates Chapter 10 to cart upsells as "free money" (Source: CRO Ebook, Chapters 9-10). A case study from Swanky Agency recorded a 32% AOV lift from cart cross-sell on a Shopify fashion store (Source: Swanky Agency Case Study). The free shipping threshold at $200 CAD creates a natural nudge mechanic that is currently unused (Source: Site Screenshots).

**V1:**

*Cross-sell section:* Add a "You Might Also Like" section in the empty space below the cart line item(s), above the discount code field. Show 3 product tiles, each with the product image, name, price, and a one-click "Add" button. Products shown are algorithmically recommended based on cart contents (Shopify's native "You might also like" recommendation engine or a cross-sell app such as Frequently Bought Together). On mobile, the 3 tiles display as a horizontal scroll row (each tile ~120px wide). On desktop, 3 tiles display side-by-side in a row below the line items.

*Free shipping nudge:* Enhance the existing "You're $35.00 away from free shipping" bar at the top of the cart to directly reference the cross-sell section: update the text to read "You're $35 away from free shipping - add one more item:" with an arrow pointing down to the cross-sell row. This makes the connection between the nudge and the action explicit. The progress bar remains. On mobile, this text replaces the current "You're $35.00 away from free shipping!" phrasing and is followed immediately by the horizontal product scroll. On desktop, same update above the cross-sell row.

No changes to the checkout button, discount code field, or total display. Control is the current cart as-is.

---

## Slot 3: Homepage Hero CTA

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (thelatestscoop.ca)
**Revenue potential:** ~25,000 homepage sessions/mo (estimate; verify in Shopify) x 5% conservative lift in click-through to shop x $130 CAD AOV x site average CR of ~2% = ~$3,250 CAD/mo. This is the most conservative slot because the lift is indirect (click-through, not direct purchase).

**Hypothesis:** If we add a prominent CTA button and a short value proposition to the homepage hero, more visitors will move from the hero into the shop, because currently the hero offers no action to take and no reason to click.

**Data:** The homepage hero displays "new drops" in large text over a three-panel lifestyle image, but contains no button, no link, and no directional CTA (Source: Site Screenshots). Visitors from Google Ads and Meta arrive on the homepage with category intent (dresses, jeans, outerwear) but are given no direct path to act on that intent above the fold (Source: Google Ads Transparency, Site Screenshots). The CRO ebook identifies the homepage hero as one of the highest-impact test locations due to the volume of traffic it receives (Source: CRO Ebook, Chapter 15). Competitor Aritzia uses a prominent hero CTA button on their homepage directing visitors to specific seasonal collections, a pattern consistent across major fashion retailers (Source: Competitor Research).

**V1:**

*CTA button:* Add a single CTA button centered on the hero image, positioned in the lower third of the hero panel (below the "new drops" text). Button text: "Shop New Arrivals." Button style: white background with black text, to contrast against the dark imagery. On mobile, the hero image scales to a single-panel view. The button is centered below the "new drops" text, spanning approximately 60% of screen width. On desktop, the button appears centered across the three-panel hero, below the "new drops" text overlay.

*Value proposition line:* Add a single line of supporting text above the button: "New styles added weekly. Free shipping over $200." Set in small white sans-serif text. On mobile, this line appears directly above the button. On desktop, same placement above the button in the center panel.

No changes to the hero imagery, navigation, or announcement bar. Control is the current homepage hero as-is.

---

## Future Slot Candidates

**Page speed remediation (critical prerequisite):** Mobile LCP of 72.6s on the homepage and 48.8s on the PDP means traffic is being lost before any CRO test can work. Addressing the top PageSpeed audit flags - inefficient cache policies, render-blocking requests, duplicate JavaScript, and unoptimized image delivery - should be treated as a prerequisite to the test program, not a future test. Every dollar spent on paid media is partially wasted until load times are fixed.

**Google Ads message match:** Google Search and Display ads are running fall messaging ("Fade Into Fall," "outerwear for changing seasons") in late April 2026. Creating season-matched landing pages or updating ad copy to reflect current spring drops would reduce the gap between ad promise and on-site delivery.

**Collection page photography standardization:** The Best Sellers collection grid mixes ghost mannequins, on-figure model shots, and lifestyle images in the same row. Standardizing to on-figure model photography across all product cards would improve browse confidence and reduce quality perception issues raised in reviews.

**Announcement bar conversion messaging:** The rotating bar currently cycles through "$1,000 email giveaway," "13 locations," and "new drops weekly." None of these address purchase objections. Replacing two of the three slots with trust/shipping messages ("Free returns within 14 days" and "Free shipping on orders over $200") would better serve first-time visitors.

**Return policy proactive communication:** The Facebook review complaints about a "store credit only" policy suggest a communication breakdown between what the actual policy says (14-day refunds to original payment) and what customers understand. A dedicated effort to surface the policy at every friction point - PDP buy box, cart, order confirmation - would reduce post-purchase complaints and potentially improve conversion for new visitors who hesitate due to return risk.
