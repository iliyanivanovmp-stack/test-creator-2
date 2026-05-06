# Ibex CRO Research Brief

**Data Sources:** Meta Ads, Google Ads, Reviews & UGC, Page Speed / Core Web Vitals, Site Screenshots

---

## Insights

The biggest problem on ibex.com is happening right before checkout. Every customer who adds a product to their cart on mobile sees an auto-added line item at the top of their cart: a $3-4 EcoCart carbon offset charge. It appears as a product. It is non-refundable. If a customer deletes it and edits the cart, it reloads. At least one verified customer returned their entire order over this and stated they will never shop at Ibex again. This is not a small UX issue - it is an active trust-destroyer at the bottom of the funnel, right at the moment of maximum purchase intent.

The second major issue is message match. Ibex is running two paid channels with completely different promises. Google search ads offer "$20 off your first order - Code TRYIBEX20." The announcement bar on the site shows free shipping info. New customers from Google arrive expecting a $20 discount and see no confirmation of it anywhere above the fold. Meanwhile, Meta ads drive urgency around "Last Chance Gear - Final colorways, retiring styles, won't be back" and land visitors on a sale page with a generic road trip image and the word "SALE." The emotional momentum built by the ad evaporates on landing.

Both paid traffic destinations - the sale collection page and the Men's Natural Boxer Brief PDP - score 43-44 on mobile performance with LCPs of 13.6s and 19.2s respectively. Every 1-second delay in mobile load time reduces conversions by approximately 7% (Google, 2024). At 19 seconds to main content, paid Meta traffic arriving on the boxer brief PDP is operating at a fraction of its potential.

Reviews and third-party research confirm the product quality is strong once it reaches a customer who trusts the brand enough to buy. The boxer brief gets 4.5 stars on 109 reviews. The challenge is getting customers to the purchase decision - not product satisfaction after the fact.

Revenue opportunity: Fixing cart trust friction and sharpening message match on the two highest-traffic paid landing pages targets the full paid traffic funnel from click to purchase. These are not small pages - they are the destinations Ibex is actively paying to send customers to right now.

---

## Slot 1: Cart - Carbon Offset Opt-In

**Type:** A/B test (1 variation vs. control)
**Page:** Cart - ibex.com/cart
**Revenue potential:** Any customer who adds to cart and encounters the EcoCart line item is a potential exit. Without internal cart abandonment data, a conservative estimate of recovering 5% of cart sessions that currently see the EcoCart charge - assuming even modest monthly cart volume of 5,000 sessions at Ibex's AOV of approximately $100 - represents $25,000/month in recovered revenue. The actual opportunity scales directly with cart volume.

**Hypothesis:** If we change the EcoCart carbon offset from an auto-added cart item to an opt-in checkbox, cart-to-checkout conversion rate will increase because customers will no longer encounter an unexpected, non-refundable third-party charge as the first item in their cart.

**Data:** A verified customer returned their entire order in February 2026 after the EcoCart charge auto-reloaded after deletion and they missed it - calling it non-refundable and stating they will never shop at Ibex again. (Source: Reviews) The cart screenshot confirms EcoCart appears as the first line item on mobile, displayed above the customer's actual product with a green third-party logo, price, and quantity controls - visually indistinguishable from a product. (Source: Site Screenshots) The Ibex brand response acknowledged the issue. This is a documented, recurring friction point at the single highest-intent moment in the purchase funnel.

**V1:** Remove EcoCart as an auto-added line item. Instead, place a single opt-in checkbox at the bottom of the cart summary, above the Checkout button. The checkbox reads: "Add carbon offset to my order (+$X) - offset 116 lbs of carbon for this shipment." It is unchecked by default. Customers who want to contribute can check it before proceeding to checkout. On mobile, this sits between the order total and the Checkout button. On desktop, it appears in the right-side cart summary column, below the subtotal and above the Checkout button. The EcoCart brand logo can remain visible next to the checkbox text for credibility. No other changes to the cart layout.

---

## Slot 2: Sale Page Hero - Last Chance Urgency Match

**Type:** A/B test (1 variation vs. control)
**Page:** Sale collection - ibex.com/collections/sale
**Revenue potential:** 2 of 3 active Meta ads land on this page (starting March 26, 2026). A conservative 0.5% lift in sale page conversion rate, applied to an estimated 20,000 monthly sessions driven by paid Meta traffic at $80 average sale order value, equals $8,000/month in incremental revenue. The actual figure scales with Meta spend.

**Hypothesis:** If we replace the generic sale page hero with copy and imagery that mirrors the urgency messaging in the Meta ads, sale-to-checkout conversion rate will increase because customers who arrived primed for "Last Chance, Final Colorways" will find that promise confirmed on landing instead of a generic SALE page.

**Data:** Both active Last Chance Meta ads use identical urgency copy: "Ibex merino wool doesn't go on sale often - and these particular styles won't be back. If you've been considering it, now is genuinely the right time. Final colorways, retiring styles, and prices that reflect neither." (Source: Meta Ads) The sale page hero is a road trip landscape with "SALE" text overlaid - no urgency language, no product specificity, no reference to final colorways or retiring styles. (Source: Site Screenshots) The current announcement bar reinforces this disconnect: it says "Don't Miss Out: Last Chance Gear" but the hero below it does not follow through. Message match between ad promise and landing page delivery is a documented conversion lever - the content, messaging, and visuals on a landing page must align with the ad that brought visitors there.

**V1:** Replace the current road trip hero image and "SALE" headline with a new hero section that mirrors the ad's urgency directly. Headline: "Last Chance Gear." Subheadline: "These styles won't be back. Final colorways, retiring products - at prices that reflect neither." CTA buttons: "Shop Women's Sale" and "Shop Men's Sale" (same two-button layout as the current homepage hero). The hero image should feature a model wearing a specific product from the sale (e.g., the Paradox leggings or the Mammoth hoodie already featured in the Meta ads) rather than a landscape without product focus, so arriving ad traffic immediately recognizes the product they clicked on. On desktop, the layout mirrors the current split-image hero format. On mobile, the image stacks above the headline and CTA buttons. The rest of the sale page layout remains unchanged.

---

## Slot 3: Announcement Bar - First-Time Visitor Welcome Offer

**Type:** A/B test (1 variation vs. control)
**Page:** Sitewide announcement bar - all pages (targeting new visitors from Google)
**Revenue potential:** Google search ads are running "$20 off your first order - Code TRYIBEX20" across multiple campaigns. If Google drives 10,000 new visitor sessions per month and even 2% more of them convert due to visible offer confirmation (a conservative lift), at $100 AOV that is $20,000/month in incremental new customer revenue.

**Hypothesis:** If we display the TRYIBEX20 new customer offer in the announcement bar for first-time visitors, new customer conversion rate will increase because visitors arriving from Google ads that promised $20 off will immediately see that offer confirmed on-site rather than needing to wait for a popup or miss it entirely.

**Data:** The TRYIBEX20 "$20 off your first order" promotion appears as an extension on multiple Google search ads. (Source: Google Ads) The current announcement bar shows "Don't Miss Out: Last Chance Gear. Free shipping on orders over $149, US only." - no mention of the $20 discount. (Source: Site Screenshots) A popup carrying this offer appears to exist (visible in PageSpeed screenshot), but its timing and targeting are unknown. Customers who clicked a Google ad specifically because of the $20 off promise arrive on site with no immediate confirmation of that offer - creating a trust gap right at the start of the session. The free shipping threshold also varies between channels: Google ads state $99+, the announcement bar states $149 - another point of confusion for new visitors.

**V1:** For sessions identified as first-time visitors (no prior Ibex cookie), rotate the announcement bar to display the welcome offer as the primary message: "New here? Get $20 off your first order - Code TRYIBEX20." The existing free shipping message remains as a secondary rotation. On mobile, the bar alternates between the two messages on a 4-second cycle. On desktop, both messages can be displayed simultaneously if the bar width allows, or rotate in the same cycle. Returning visitors see only the free shipping message as today. The popup behavior remains unchanged - this test is specifically about surfacing the offer in the announcement bar where it is visible immediately on page load, without requiring a popup trigger.

---

## Future Slot Candidates

- **PDP Buy Box - Boxer Brief social proof above fold:** The Men's Natural Boxer Brief PDP (Meta Ad #2 destination) has key product information hidden in collapsed accordions ("Field Notes," "The Clip") and no reviews visible in the buy box on arrival. Adding the star rating and a selected review pull-quote directly below the price, and expanding one key feature accordion by default (specifically addressing the waistband quality concern visible in reviews), could improve PDP conversion rate. Blocked until page speed is addressed - LCP of 19.2s on mobile means most paid traffic never waits long enough to see the buy box.
- **Page speed remediation:** The LCP issues on both paid traffic destinations (13.6s homepage, 19.2s PDP) are the single largest conversion drag on the site. Image compression, render-blocking script deferral, and unused JavaScript removal are the three highest-impact fixes. This is a dev project, not an A/B test, but it unlocks the full potential of every other test on this list.
- **Sale page Paradox-specific landing:** Meta Ad #3 CTA reads "Shop Paradox Last Chance Colors" but lands on the general sale page. A Paradox-specific sale page or anchored section would improve message match for this specific ad set.
- **Bundle offer on boxer brief PDP:** "I would buy three more pair if less expensive" (Oct 2025 review) - a buy-2-get-10%-off or 3-pack bundle offer on the boxer brief PDP could improve AOV for a product with documented price sensitivity and repeat purchase intent.
