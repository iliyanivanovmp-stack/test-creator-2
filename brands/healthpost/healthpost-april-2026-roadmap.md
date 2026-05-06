# HealthPost CRO Research Brief

**Data Sources:** Meta Ads, Google Ads Transparency, Reviews & UGC, Page Speed, Competitor Research, Site Screenshots

## Insights

HealthPost is spending on paid traffic across Meta and Google while sending that traffic to pages that functionally break the ad promise. Ad 1, actively promoting "Save $15 When You Spend $75, Use Code: SPEND75" since April 22, 2026, lands every click on a homepage hero showing an unrelated Nature's Sunshine sale. There is no mention of SPEND75, the $15 saving, or the $75 threshold anywhere visible above the fold. Visitors who clicked because of a savings offer have to figure out, without any help, how to redeem a deal the homepage doesn't acknowledge.

This sits on top of a mobile page speed problem that affects every paid touchpoint. The homepage loads in 5.3s on mobile (threshold: 2.5s). The PDPs that ads 2 and 3 send paid traffic to load in 7.0s. Both Core Web Vitals assessments failed as of April 29, 2026. Per Google and Deloitte's 2019 research, each additional second of mobile load time reduces conversions by up to 20%. At 7.0s, the math is brutal.

The trust inconsistency runs through the entire funnel. Meta ads promise "65,000+ reviews and counting." The PDPs where those ads land show 18-29 product-level reviews with no sitewide context. The cart shows "5 Star rating from 7800+ reviews." Google ads show "Over 54,000 Product Reviews." Some Google search ads still show "Free Delivery Over $59" when the threshold is $79. A customer who encounters all of these numbers in a single session will notice. Trust built in the ad is eroded step by step across the page.

One genuine strength: the rewards program. Multiple long-term customers explicitly cite it as the reason they return to HealthPost instead of buying cheaper elsewhere. It appears in the site trust bar but is not used to convert first-time visitors. That opportunity is in the Future Slots section.

Conservative revenue model across the three tests below: Slot 1 scales directly with SPEND75 ad volume (at 5,000 ad sessions/month, the potential is ~$4,250/month). Slot 2 and Slot 3 each model at approximately $5,850/month on a 30,000-session baseline. These are estimates built without access to Shopify or Meta analytics. Plug in real numbers and the opportunity sizes proportionally.

---

## Slot 1: SPEND75 Dedicated Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** Control: Homepage (https://www.healthpost.co.nz/), current destination for the SPEND75 Meta ad. V1: Dedicated landing page at a new URL (e.g., https://www.healthpost.co.nz/pages/spend75). Split SPEND75 Meta ad traffic 50/50 between both destinations.
**Revenue potential:** At 1,000 SPEND75 ad sessions/month, lifting CR from an estimated 0.5% (broken message match baseline) to 1.5% adds 10 conversions x ~$85 avg basket = ~$850/month. At 5,000 sessions/month, the uplift is ~$4,250/month. Use your actual Meta Ads Manager click volume to model precisely.

**Hypothesis:** If we route SPEND75 ad traffic to a dedicated page that validates and activates the offer, conversion rate will increase because visitors with promo intent need immediate confirmation that the deal is real before committing to build a qualifying basket.

**Data:** The SPEND75 Meta ad (active since April 22, 2026) lands all clicks on a homepage promoting a "1 week only: 10-30% off Nature's Sunshine" sale with no mention of SPEND75 anywhere in the visible area (Source: Meta Ads, Site Screenshots). The visitor who clicked expecting a $15 discount sees a completely unrelated promotion. Instapage's dedicated landing page A/B test showed nearly 3x higher conversion rate for paid traffic vs. a homepage. A message-matched headline test documented a 42% lift in two weeks (Source: CRO Community Research).

**V1:** Build a standalone landing page stripped of the full site navigation. Replace the main nav with a slim HealthPost logo-only header to remove off-page exits.

On desktop: two-column layout above the fold. Left column: bold headline "Save $15 When You Spend $75" in HealthPost's existing dark teal typeface. Subheadline: "Use code SPEND75 at checkout. One use per customer." Below: a 3-step visual of the offer mechanics (Add $75+ to cart, Enter SPEND75 at checkout, Pay $15 less). Primary CTA: "Start Shopping" in HealthPost teal. Right column: a 2x3 product grid of top-selling items that help customers build toward the $75 threshold, each showing brand name, product name, price, and an "Add to Cart" button. Below the fold: a trust bar mirroring the existing site bar ("Free NZ Shipping Over $79 | 100% Kiwi Family Owned | 65,000+ Customer Reviews | Shop Now & Pay Later"). Below that: a second product grid of 6 more qualifying products. A sticky header appears on scroll showing "SPEND75: $15 off $75+ orders | [Start Shopping]" in HealthPost teal.

On mobile: single-column layout. Top fold: "Save $15 When You Spend $75" headline, "Use code SPEND75 at checkout" subheadline, the 3-step offer visual stacked vertically, "Start Shopping" CTA. Below fold 1: trust bar. Below fold 2: a 2-per-row product card grid of qualifying products (brand, name, price, ATC). A sticky bottom bar persists through scroll: "SPEND75: $15 off $75+ | Start Shopping" in HealthPost teal. The hamburger menu remains accessible but not the primary nav strip.

---

## Slot 2: PDP Trust Injection

**Type:** A/B test (1 variation vs. control)
**Page:** All PDPs receiving paid ad traffic. Confirmed examples: SLO Cedar + Sage Natural Deodorant PDP (https://www.healthpost.co.nz/products/slo-cedar-sage-natural-deodorant?sku=2DPCR) and Weleda Arnica Sport Massage Oil PDP (https://www.healthpost.co.nz/products/weleda-arnica-massage-oil?variant=46872859279578). Implement globally across all PDPs.
**Revenue potential:** Estimated 9,000 PDP sessions/month (modeled at 30% of a 30,000-session baseline, without Shopify analytics) x 1% CR lift x $65 avg order value = ~$5,850/month. Adjust with your actual PDP session data.

**Hypothesis:** If we add a sitewide customer count callout inside the buy box directly below the product-level review count, conversion rate will increase because visitors arriving from ads that promise "65,000+ reviews" currently see 18-29 product reviews with no bridge between the two numbers, creating a trust gap at the point of purchase.

**Data:** Meta ads 2 and 3 (both active since April 22, 2026) include "65,000+ reviews and counting" as a primary trust bullet. The SLO PDP shows 29 reviews; the Weleda Arnica PDP shows 18 reviews. Neither PDP provides any context that these are product-level counts within a much larger sitewide total (Source: Meta Ads, PDP Screenshots). The reviews themselves are strong: SLO 4.5/5, Weleda 5.0/5, with high repurchase intent across both (Source: Reviews & UGC). The problem is not the reviews' quality but the count disconnect. The Billion Dollar Websites CRO ebook cites a coffee brand using "40,000+ reviews" as a trust signal above the fold: "This is an incredible signal to increase trust right above the fold." (Source: CRO Ebook).

**V1:** Add a single trust line directly below the product star rating and review count in the buy box. No other changes to the buy box, page layout, or any other element.

Current state on SLO PDP: "4.5/5 (29)" displayed as the review row.
Variant: "4.5/5 (29 reviews) | Trusted by 65,000+ HealthPost customers" on the same row or directly below it. The "29 reviews" text links to the product review section lower on the page. The "65,000+" links to HealthPost's sitewide review platform or the About Us reviews page. Style: HealthPost's existing body text style (grey, smaller than the product title), pipe-separated.

On desktop: the trust line sits in the right-hand buy box column, directly below the star rating row, before the price. It reads: "[Star rating] (29 reviews) | Trusted by 65,000+ HealthPost customers." Both counts are displayed on one line. The "65,000+" is a text link.

On mobile: same position below the star rating, above the price. If the line is too wide for smaller screens, it wraps to two lines: "[Star rating] (29 reviews)" on line 1, "Trusted by 65,000+ HealthPost customers" on line 2. No truncation on either line. The "65,000+" remains a tappable link.

---

## Slot 3: Cart Discount Code Field Collapse

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide, all devices). Control reflects the cart drawer state observed in the mobile screenshot taken April 29, 2026.
**Revenue potential:** Estimated 3,000 cart sessions/month (modeled at 10% of a 30,000-session baseline, without Shopify analytics) x 3% completion rate lift x $65 avg order = ~$5,850/month. One published A/B test reported a 9% drop in cart abandonment from discount code field optimization (Source: CRO Community Research). Adjust with your actual cart session count and completion rate from Shopify.

**Hypothesis:** If we remove the "Discount code" field from the cart drawer and surface it only at Shopify's native checkout step, cart completion rate will increase because the visible field prompts non-promo visitors to leave the cart to search for a code they saw advertised but do not have.

**Data:** The cart drawer displays a visible "Discount code +" expandable field to all cart visitors (Source: Cart Screenshot, April 29, 2026). HealthPost is simultaneously running an active Meta ad with promo code SPEND75 since April 22, 2026 (Source: Meta Ads). Any visitor who did not come via that specific ad will see the discount field, recognize that a code likely exists (because the field is prominent), and leave the cart to find it. This is a self-inflicted abandonment trigger. CRO community research confirms that moving or hiding discount code fields reduces this exit behavior and cart abandonment (Source: CRO Community Research). The Billion Dollar Websites ebook advises removing non-purchase distractions from the cart: "Remove Distractions. Many Checkout flows include upsells, which are great for increasing AOV but can distract customers if done wrong... remove any other links or content that are not directly related to the sale." (Source: CRO Ebook). Shopify's native checkout already contains a discount code field at the payment step, meaning no customer loses the ability to apply a valid code.

**V1:** Remove the "Discount code +" row from the cart drawer entirely. No other changes to the cart: trust bar, free shipping progress bar, item row, upsell section, estimated total, and CTA buttons all remain unchanged.

On mobile: the current cart layout (top to bottom) is: trust bar, free shipping progress, item row, "You may also like" upsell, "Discount code +", estimated total, CONTINUE SHOPPING + CHECKOUT. The variant removes the "Discount code +" row. The layout becomes: trust bar, free shipping progress, item row, upsell, estimated total, CONTINUE SHOPPING + CHECKOUT. The vertical space contracts naturally. Shopify checkout (step 2, payment information) retains the native discount code field where customers with valid codes can still apply them.

On desktop: apply the same removal to the desktop cart drawer or cart page. The "Discount code" input does not appear until the customer reaches Shopify checkout.

---

## Future Slot Candidates

**PDP page speed (dev project, 2 slots):** The highest-impact technical investment available. PDP LCP is 7.0s on mobile vs. a 2.5s threshold. Identified savings: 2,224 KB unused JavaScript, 1,163 KB image optimization, 512 KB unused CSS, 919 KB cache lifetime improvements. This is not an A/B test - it is a prerequisite for paid traffic to convert. Fixing this before the PDP trust injection test would amplify Slot 2's results significantly.

**Free shipping threshold test:** healthy.co.nz offers free shipping at $70 NZD vs. HealthPost's $79. A test lowering the threshold for first-time visitors (or sitewide) would capture cart values in the $70-$78 range where HealthPost loses on price comparison.

**Cart upsell gap fix:** The current Arnica Cream upsell ($24.30) brings a $30.30 cart to $54.60, still $24.40 short of the free shipping threshold. Replacing the upsell with a dynamic recommendation that accounts for the cart's distance from $79 (showing products priced to close the gap) would increase both ATC rate on the upsell and free shipping attainment.

**Rewards program hero for first-time visitors:** Multiple long-term customers cite the rewards program as the primary reason they return to HealthPost over cheaper alternatives. The program is not featured in homepage heroes, paid ads, or landing pages targeted at new visitors. A test surfacing "Earn [X] Healthy Rewards Points on this order" as a hero-level benefit for unrecognized visitors could lift first-purchase conversion.

**Health-goal navigation test (mobile):** healthy.co.nz navigates by health goal (Sleep, Immunity, Brain, Digestion). HealthPost navigates by product category (Health & Supplements, Food & Drink). A goal-based mobile navigation variant could improve depth of browse and session-to-cart rate for visitors who know their problem but not the product.

**Fix Google ad delivery threshold copy:** Two active Google search ads state "Free Delivery Over $59." The current threshold is $79. Any customer clicking those ads and reaching checkout expecting free delivery at $59 will encounter a $20 gap. This is an ad copy fix, not a test, but it is a live trust-eroding inconsistency.
