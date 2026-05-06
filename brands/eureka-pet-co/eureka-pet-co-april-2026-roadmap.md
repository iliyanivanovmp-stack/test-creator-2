# Eureka Pet Co CRO Research Brief

**Data Sources:** Meta Ads, Google Ads Transparency, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots

---

## Insights

Eureka has a problem hiding in plain sight. Across 3,095 reviews on the Taste Tester PDP alone, the single most common buying story is a dog owner who tried everything, found their picky dog would eat nothing, discovered Eureka, and never looked back. That story is nowhere on the site. The homepage hero says "Same Recipe, Better Value." The Taste Tester PDP leads with "Make sure your dog will love Eureka." The ads talk about $6 and Australian ingredients. The fussy eater narrative, the one that converts, is buried in the review section.

The second problem is price. It is the most frequently cited complaint in reviews, with customers describing the product as "ridiculously expensive," walking away at the reorder price after a welcome discount expired, or calculating that they simply cannot feed a large dog on Eureka economics. The site's response to this is to say nothing. There is no cost-per-day framing, no per-serve calculation, no "this costs less than you think" section anywhere across the pages we reviewed. The brand is leaving the price objection unanswered every time a new visitor lands.

These two gaps converge on the highest-traffic moment in the funnel: the $6 Taste Tester PDP. Two of three active Meta ad sets and multiple Google campaigns drive to this page. It has 3,095 reviews and a 4.9-star rating, the strongest social proof on the site. But the copy is generic, there is no subscription mention, and the cart it feeds into has a visible promo code field that sends a meaningful percentage of buyers searching for discount codes they will not find, often not returning.

Meanwhile, mobile performance is critically broken. The homepage scores 23/100 and the Taste Tester PDP scores 27/100 on Google PageSpeed, with LCP times above 12 seconds. Most mobile visitors abandon before the page loads. Every paid impression Eureka buys on Meta and Google is paying for traffic that sees a white screen for over 10 seconds before anything renders.

The opportunity is clear. Eureka's product genuinely solves one of the most frustrating problems in pet ownership, a dog that won't eat. That proof is in the reviews. The job of CRO here is to surface that proof at every key decision point, connect the $6 sample to the subscription that follows, and stop losing revenue at the cart. A conservative 1-2% lift on the Taste Tester PDP plus reducing cart abandonment by a meaningful margin would compound across every paid campaign Eureka runs.

---

## Slot 1: Dedicated Sample Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** Current control: eurekapet.co/products/natural-dog-food-sample | Variation: new dedicated LP (same URL via redirect or separate URL for Meta/Google ad targeting)
**Revenue potential:** Exact session counts require GA access. At a conservative 500 paid sessions/day (15,000/mo) to the sample page, a 1.5% CR lift = 225 additional sample purchases/month at $6 = $1,350 direct. The larger opportunity: each incremental sample buyer has a path to a $185 Starter Pack subscription. If 10% of those 225 convert downstream = 22 Starter Pack sales/month = $4,070 additional. Estimated combined monthly lift: ~$5,400.

**Hypothesis:** If we replace the standard Taste Tester PDP with a dedicated landing page built around the fussy eater narrative and stripped of navigation, the conversion rate will increase because the current PDP was built for organic product browsing, not for paid traffic arriving with a specific intent. The PDP contains the announcement bar promoting treats, a "Spin to Win" popup, full site navigation, and generic product copy, all of which dilute the message from the ad.

**Data:** 2 of 3 active Meta ad sets and multiple Google campaigns all drive to this page, making it the highest-traffic acquisition page on the site (Source: Meta Ads, Google Ads Transparency). The page has 3,095 reviews at 4.9 stars, the strongest social proof asset on the site, but the copy does not reference the fussy eater outcome that drives over 30% of positive reviews (Source: Reviews & UGC, Site Screenshots). The CRO ebook (Billion Dollar Websites, Dylan Ander) identifies paid landing pages as the highest-leverage test for any brand whose primary acquisition channel is paid advertising. Outcome-focused headlines have been shown to convert 18-47% better than feature-focused equivalents across 2,654+ ecommerce store tests (Source: BrillMark 2025 Report, via CRO community research).

**V1:** Dedicated landing page. Navigation stripped to logo only (no menu, no cart icon, no login). Announcement bar removed. "Spin to Win" popup suppressed. Hero section headline: "Even the fussiest dogs can't say no." Sub-copy directly below: "Try all 3 Eureka recipes for just $6 - free delivery Australia-wide." ATC button: "Try for $6" (black, full-width on mobile, wide on desktop). Below the ATC: the same 4 trust badges from the PDP (100% Australian Made & Owned, 100% Money Back Guarantee, 68°C Gently Air Dried, No Fillers or Glycerins). Below that: a curated social proof section with 4-6 fussy-eater review verbatims, each showing dog name, breed, and star rating. Pull directly from existing reviews: Rachel Kelly (Cavoodle with gut issues), Bel Humphreys (fussy poodle who lined up each piece), tRACY (cattle dog "Australia's fussiest dog"), Rachel McRoberts (staffy not food motivated). Close with a single line of reassurance: "Not sure yet? We also offer a 100% money-back guarantee on all full-size food orders." No other links, no navigation, no footer upsells.

On mobile: headline full-width, sub-copy below, full-width black ATC button, trust badges in a 2x2 grid, testimonials in a vertically scrolling card stack (one per card with dog name and breed). Sticky bottom bar: "Try for $6 - Free Delivery" remains visible on scroll.

On desktop: Split layout. Left half: headline, sub-copy, ATC button, trust badges. Right half: hero product photography (same Taste Tester pack image currently used). Below the hero: 2-column testimonial grid. Full width guarantee line at bottom.

---

## Slot 2: Taste Tester PDP - Subscription Bridge

**Type:** A/B test (1 variation vs. control)
**Page:** eurekapet.co/products/natural-dog-food-sample
**Revenue potential:** If 2% of Taste Tester PDP visitors click through to a subscription recipe page as a result of this prompt, and 10% of those complete a $74.37 subscription order, that is 2 subscription starts per 1,000 PDP sessions. At even 5,000 organic/direct PDP sessions/month, that is 10 new subscribers/month at $74.37 = $744 in first-month revenue with recurring subscription value compounding monthly.

**Hypothesis:** If we add a subscription upgrade prompt below the trust badges on the Taste Tester PDP, more sample buyers will discover and consider the subscription because currently the page has zero mention of subscription and presents no next step after the $6 purchase.

**Data:** The Taste Tester PDP has no subscription mention visible anywhere in the top 3 folds or below (Source: Site Screenshots). Subscription customers are among Eureka's most loyal: one reviewer has been a subscriber for 4 years, multiple reference the free treats as a delight, and the subscription was described as "sneaky" in the best possible way because the free treats drove further purchases (Source: Reviews & UGC). The brand's own Google ads cite subscription as a key offer but it does not appear on the most-visited page in the acquisition funnel (Source: Google Ads Transparency).

**V1:** Below the 4 trust badges and above the "Product Details" accordion, add a single benefit strip. Design: light cream background, single row, no border. Text: "Most Eureka dogs end up on a subscription. Get 15% off any full-size bag + free treats for life, every order." followed by a text link "Browse all recipes →" linking to the air-dried food collection. The strip is not a popup, modal, or interruption. It is a static inline section that sits naturally in the page flow after the purchase decision point.

On mobile: same position below trust badges. Strip is full-width, text centered, "Browse all recipes →" is a tappable inline link.

On desktop: same position, same width as the buy box column. The strip does not extend to the full page width, it stays within the right-column buy box layout.

---

## Slot 3: Cart Drawer - Promo Code Field

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (sitewide, all sessions)
**Revenue potential:** Every visitor who adds to cart sees this field. At even a 3% improvement in cart-to-checkout rate on 1,000 cart sessions/month = 30 additional checkouts. If 80% of those complete at $6 AOV (Taste Tester-heavy cart mix) = 24 incremental purchases = $144/month in sample revenue. The downstream subscription value from those additional sample purchases is the real multiplier. For higher-AOV carts (Starter Pack at $185), each recovered session is worth considerably more.

**Hypothesis:** If we collapse the visible "Got a discount code? Enter it h..." input field behind a dismissible text link, cart-to-checkout conversion will increase because the prominent input field signals to customers without a code that they are paying full price, triggering a tab-leave to search for discount codes that often results in non-return.

**Data:** The cart drawer currently shows a full input field and "Apply" button as a prominent above-the-fold element on mobile (Source: Site Screenshots). The CRO ebook (Billion Dollar Websites, Dylan Ander) specifically identifies distractions in the cart and checkout flow as conversion killers, recommending removal of any element not directly related to completing the sale. CRO community research confirms the visible promo code field is a known cart abandonment trigger in DTC ecommerce, with the recommended fix being a collapsed "Have a code?" link that expands on click. Eureka runs a "Spin to Win" wheel that already distributes some codes, increasing the likelihood that customers without a spin-derived code feel they are missing a discount.

**V1:** Replace the visible text input and "Apply" button with a small grey text link: "Have a discount code? Apply at checkout." No input field visible by default. Customers who have a code can apply it at the Shopify checkout step (which has its own discount field). This removes the visual trigger for code-hunting behavior while still providing a path for customers with codes.

On mobile: the text link sits in the same position as the current input field, styled in grey, smaller than the "Checkout" button. Single tap to take them to checkout where they can apply the code.

On desktop: same treatment. Single line of grey text above the "Checkout" button.

---

## Slot 4: Cart Drawer - Subscription Upsell for Sample Buyers

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (when Taste Tester is the cart item)
**Revenue potential:** The Taste Tester is the highest-volume cart item. If the subscription upsell prompt drives even 3% of sample buyers to click through and subscribe to a recipe, and the average subscription starts at $74.37/month: 3% of 500 sample carts/month = 15 new subscribers = $1,115 in first-month subscription revenue, recurring monthly.

**Hypothesis:** If we replace the "I'm even better with Mighty Liver Munchies" treat upsell with a subscription upgrade prompt when the Taste Tester is in cart, more sample buyers will enter the subscription funnel because the treat upsell adds $18.95 one-time while the subscription starts at $74.37/month recurring. The current upsell optimizes for a small one-time AOV bump rather than LTV.

**Data:** The cart drawer shows "I'm even better with Mighty Liver Munchies $18.95 + Quick Add" as the only upsell when the Taste Tester is in cart (Source: Site Screenshots). There is a large dead white space above this upsell section (visible in mobile cart screenshot). No subscription mention exists anywhere in the cart experience (Source: Site Screenshots). Review data shows subscribers are Eureka's most satisfied customers and specifically mention the sample pack as the entry point: "I received the taste tester sample pack and my dogs were immediately obsessed. Will never go back." (Source: Reviews & UGC). The brand's subscription offer (15% off + free treats for life) is a meaningful value proposition that is not presented at the moment of highest intent.

**V1:** When the Taste Tester is the only item in cart, replace the treat upsell section with a subscription prompt. The dead white space above the prompt is filled with 2 short review verbatims from fussy-dog customers (each 1-2 lines, with dog name and breed). Below the reviews: a subscription prompt block with headline "Most sample buyers end up subscribing." Sub-copy: "Get 15% off any full-size recipe + free treats for life, delivered on your schedule." CTA: "Browse recipes →" (text link, not a heavy button - the goal is to educate and invite, not pressure). The "Checkout • $6.00" button remains as the primary CTA and is not moved or de-emphasized.

On mobile: review verbatims in the dead space, subscription prompt below, "Browse recipes →" link, followed by the existing "Checkout • $6.00" button at the bottom.

On desktop: same layout in the cart drawer sidebar. Reviews and subscription prompt fill the white space. Checkout button remains at the bottom.

---

## Slot 5: Homepage Hero - Fussy Eater Angle

**Type:** A/B test (1 variation vs. control)
**Page:** eurekapet.co/ (homepage)
**Revenue potential:** The homepage receives traffic from all channels (organic, direct, social, email, brand search). At a conservative 20,000 sessions/month and a 0.5% lift in downstream sample page visits, that is 100 additional sample page sessions/month feeding the sample acquisition funnel. For homepage visitors who buy directly: a 1% CR lift at a blended AOV of $90 (mix of Taste Tester, Starter Pack, individual bags) = $18,000/month in incremental revenue. These are directional estimates; GA data is needed to validate.

**Hypothesis:** If we replace the "Same Recipe, Better Value." hero headline with a fussy-eater-led headline and a $6 sample CTA, homepage conversion will increase because the current headline uses internal brand language that first-time visitors cannot understand, and the page's strongest conversion lever (the $6 sample) is not surfaced anywhere in the top 3 folds.

**Data:** The current homepage hero says "Same Recipe, Better Value." with a "SHOP NOW" CTA linking to the Single Protein Chicken product (Source: Site Screenshots). There is no mention of the $6 sample on the homepage despite it being the dominant paid acquisition offer across Meta and Google (Source: Meta Ads, Google Ads Transparency). The fussy eater theme appears in over 30% of positive reviews and is the most common reason customers cite for trying Eureka, but it does not appear in the homepage top 3 folds (Source: Reviews & UGC, Site Screenshots). Outcome-focused headlines have been shown to convert 18-47% better than feature-focused ones across large-scale ecommerce testing (Source: BrillMark 2025 report via CRO community research). "Same Recipe, Better Value." is a features and pricing statement with no emotional hook for a first-time visitor.

**V1:** Replace the hero headline with: "The food even the fussiest dogs can't say no to." Sub-copy: "Try all 3 recipes for $6 - free delivery Australia-wide." CTA button changes from "SHOP NOW" to "Try for $6" (same black outline style, links to Taste Tester PDP). The hero image (white dog with Eureka bag) and the split layout remain unchanged. The orange underline styling under the headline remains if it fits the new line length.

On mobile: headline stacks full-width across the screen. Sub-copy below in smaller text. "Try for $6" CTA button full-width black. The hero image may appear below the text block depending on the current responsive breakpoint. If the hero currently stacks on mobile with text above and image below, this variation follows the same pattern.

On desktop: same two-column split layout as the control. Left: new headline, sub-copy, CTA. Right: same dog photo.

---

## Slot 6: Starter Pack PDP - Cost-Per-Day Framing

**Type:** A/B test (1 variation vs. control)
**Page:** eurekapet.co/products/starter-pack
**Revenue potential:** The Starter Pack is a $185 purchase (vs. $6 for the Taste Tester). Ad 3 drives specifically to this page. Price is the #1 review complaint across the site. Even a 1% CR lift on this page represents high revenue per incremental conversion. GA session data needed to quantify precisely. Directionally: if the page receives 1,000 sessions/month, a 2% CR improvement = 20 additional purchases = $3,700/month.

**Hypothesis:** If we add a cost-per-day framing line directly below the price on the Starter Pack PDP, conversion will increase because price is the most frequently cited objection in reviews and the site currently provides no context to make the $185 price feel defensible.

**Data:** The #1 review complaint across all reviewed feedback is price, with specific references to "$97," "$126," "$185," and "$300+" as barriers (Source: Reviews & UGC). The Starter Pack PDP shows $185.00 / $223.11 with a "SAVE 17% OFF" badge, but no context on what that translates to per day or per serve (Source: Site Screenshots). In review responses, the brand itself argues that cost-per-serve is lower than it appears because the food is nutrient-dense and dogs eat less volume, but this argument is never made on the product page (Source: Reviews & UGC). The ad for this page leads with "$38 discount" (a concrete dollar saving) while the PDP shows "17% off" (a percentage), creating a small message mismatch that compounds the price confusion (Source: Meta Ads, Site Screenshots).

**V1:** Directly below the "$185.00 $223.11" pricing line, add one line of grey body text: "From [X per day] for a 10kg dog - less than a takeaway coffee." The exact per-day amount should be calculated from Eureka's feeding guidelines (available in the on-page accordion, or from the feeding calculator at eurekapet.co/pages/feeding-calculator) and verified with the client before implementation. The framing should use a relatable anchor ("less than a takeaway coffee" or equivalent) to make the daily cost feel accessible rather than technical. Below this line, no other changes to the existing page layout.

On mobile: same position - inline below the price block, above the quantity stepper. Grey text, smaller font size than the price. Does not compete visually with the price.

On desktop: same inline position in the buy box column. Right-aligned with the price, or centered if buy box is centered.

---

## Slot 7: Announcement Bar - Sample Offer vs. Treats Promotion

**Type:** A/B test (1 variation vs. control)
**Page:** Sitewide (all pages, all sessions)
**Revenue potential:** The announcement bar is the first content most visitors see. It influences intent from the moment of arrival. If the variation increases click-throughs to the Taste Tester PDP by even a modest amount, and the sample-to-subscription funnel does its job, the downstream LTV gain compounds across every session. Directionally: sitewide impression volume makes even a 0.2% CR lift material at scale.

**Hypothesis:** If we replace the "Buy 4 Get 15% Off Natural Treats" announcement bar with a bar promoting the $6 sample offer, more new visitors will enter the sample acquisition funnel because the current bar promotes a treats bundle that is not relevant to first-time visitors arriving from food-focused paid ads.

**Data:** The announcement bar on the Taste Tester PDP, Starter Pack PDP, and homepage all show "Buy 4 Get 15% Off Natural Treats →" (Source: Site Screenshots). The dominant paid acquisition offer across Meta and Google is the $6 sample (2 of 3 Meta ads, multiple Google Search campaigns) (Source: Meta Ads, Google Ads Transparency). The bar promoting treats sends an inconsistent message to paid traffic arriving to try the food. The "$6 sample + free delivery" offer is the brand's clearest, lowest-friction call to action and is not surfaced in the announcement bar on any page.

**V1:** Change announcement bar text to: "Try all 3 recipes for $6 - free delivery Australia-wide →" Link to eurekapet.co/products/natural-dog-food-sample. The orange background and arrow styling remain unchanged.

On mobile: announcement bar remains as a single line of text with the new copy. Same tap behavior.

On desktop: same single-line bar. "→" arrow remains on the right.

Note: This change affects all traffic, including existing customers who already know about the sample. For returning subscribers, the bar is neutral (they may forward the link, or ignore it). For new visitors, it aligns the bar with the primary acquisition offer. An alternative for a future test: personalizing the bar by new vs. returning visitor segment.

---

## Slot 8: Collection Page - Quick-Add to Cart

**Type:** A/B test (1 variation vs. control)
**Page:** eurekapet.co/collections/all (or collections/air-dried-food as a more targeted start)
**Revenue potential:** The collection page is where product discovery and comparison happen. Removing a click from the purchase path (collection card to PDP to ATC) directly reduces friction. If 5% of collection page visitors who would otherwise leave without clicking convert to ATC via quick-add, and the collection receives 5,000 sessions/month, that is 250 additional ATCs at a blended AOV of $75 = $18,750/month. Directional only - GA data needed to validate session and current ATC rate.

**Hypothesis:** If we add "Quick Add" buttons directly on product cards in the collection, the ATC rate will increase because the current flow requires a click to the PDP before adding to cart, adding friction for returning visitors and high-intent browsers who already know which product they want.

**Data:** The collection page currently shows product cards with name, star rating, and price only. There is no ATC or Quick Add button visible on any card (Source: Site Screenshots). All 48 products require clicking through to a PDP before adding to cart. The CRO ebook (Billion Dollar Websites, Dylan Ander) specifically recommends optimizing collections pages for Revenue Per Session by reducing browsing-to-purchase friction. Reviews and repeat purchase behavior (multiple reviews from 2-4 year customers) suggest a meaningful portion of traffic is returning buyers who know the product and do not need the PDP to make a decision (Source: Reviews & UGC).

**V1:** Add a "+ Quick Add" button to each product card. For single-SKU products (e.g., Mighty Liver Munchies at a fixed weight), the button adds directly to cart on click. For multi-variant products (e.g., Wild Venison & Grass Fed Lamb "From $74.37" with multiple size options), the button opens a compact inline variant selector (Small / Regular / Large or the actual size labels from the product) that appears on click without navigating away from the collection page. Once a variant is selected, a single click adds to cart.

On mobile: the Quick Add button is always visible below the product price on each card. Full-width within the card. On tap, single-variant products add to cart immediately with a brief cart confirmation animation. Multi-variant products show a bottom sheet variant selector.

On desktop: Quick Add button appears on hover over the card image and remains visible as a pill button centered on the image. Variant selector appears as a small dropdown below the button on hover.

---

## Future Slot Candidates

These ideas have data support but did not rank in the top 8 by revenue potential or readiness.

1. **Dedicated "Smaller Poos, Better Guts" landing page** - Google ads use this headline but it has no LP equivalent. A dedicated landing page for Google Search traffic built around gut health outcomes could improve message match and conversion for the search acquisition channel.

2. **Remove or reposition "Spin to Win" popup** - The gamified wheel appears on the Taste Tester PDP, Starter Pack PDP, and Homepage. It interrupts the purchase intent of arriving ad traffic. Testing suppression for paid traffic (while keeping it for organic/direct) could reduce distraction-driven abandonment.

3. **PDP subscription toggle in buy box** - Add a "One-time / Subscribe & Save" toggle in the buy box for the individual food bag PDPs (Wild Venison, Wild Kangaroo, Wild Boar, Single Protein Chicken). This presents subscription as a default consideration rather than something customers have to discover separately.

4. **petfoodreviews.com.au third-party badge on PDPs** - Google ads prominently cite "Rated 9.5/10 by petfoodreviews.com.au" as a trust signal. This rating does not appear on any landing page. Adding it as a badge near the star rating or in the trust badge row could increase credibility for customers arriving from non-brand search or comparison shopping.

5. **Starter Pack no-refund policy framing** - The fine print "*No exchanges, recipe swaps, or refunds are available on this product." may be increasing hesitation on a $185 purchase. Testing a reframing ("Sample packs are available for $6 to ensure your dog loves it before committing") could reduce the perceived risk of the no-refund policy.
