# March 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Meta Ads (Top 3), Product Reviews, Page Speed / Core Web Vitals, Competitor Research, Current Site Screenshots

## Insights

Norse Organics does $2.99M/mo in gross sales on 876K sessions at a 2.55% conversion rate. The numbers are healthy and growing. But under the surface, the site is leaving significant revenue on the table through self-inflicted friction.

The biggest problem is trust erosion through discount chaos. The site displays at least six different discount percentages simultaneously: 40% in the header, 45% on landing pages, 22% on the PDP, 21% on collection bundles. Add a countdown timer, "TODAY ONLY," "LIMITED STOCK," and "OUR BIGGEST DISCOUNT EVER" on the same page, and visitors have every reason to wonder what the real price is. One customer on the landing page wrote: "I was VERY skeptical. I had a serious case of buyers remorse after purchasing." She still bought, but many don't. When 51% of visitors who reach checkout abandon before paying, price confusion at the moment of truth is a likely contributor.

That checkout abandonment is the single largest revenue leak. 46,062 visitors reached checkout last month. Only 22,348 completed. At $82.96 AOV, that's roughly $1.97M in monthly abandoned revenue. The funnel from ATC to checkout is strong (86% proceed), so visitors want the product. Something between "begin checkout" and "place order" is breaking the deal. Possible culprits: EUR pricing shown to a 94% US audience, discount expectations from landing pages not matching checkout totals, or shipping/delivery surprises.

The ad-to-landing-page experience also has clear gaps. Ad #1 targets teens with a 25% off promise but sends traffic to a general acne page showing 45% off. Ad #3 tells a compelling ingredient education story, but the landing page leads with a discount headline, not ingredients. These mismatches waste the intent the ad created. Norse's top 3 Meta ads have been running 5+ months (proven performers), but the landing pages aren't tailored to the audience each ad attracts.

Conservative estimate: /pages/stop-acne receives 258,929 sessions/mo at a 2.55% CR and $82.96 AOV. A 0.5% CR lift (to 3.05%) would generate an additional $107K in monthly revenue. Across all three landing pages (545K combined sessions), a similar lift would mean $225K+/mo. The upside is real. The data points to where it is.

---

## Slot 1: Landing Page Trust & Message Match Test

**Type:** A/B test (2 variations vs. control)
**Page:** /pages/stop-acne (https://norseorganics.co/pages/stop-acne). This is the highest-traffic landing page at 258,929 sessions/mo. Learnings apply to /pages/stop-acne-teens and /pages/acne.
**Revenue potential:** 258,929 sessions/mo x 0.5% CR lift x $82.96 AOV = $107,370/mo additional revenue.

**Hypothesis:** If we replace the discount-first hero with a trust-first hero that matches the ad's messaging, more visitors will proceed to purchase because they'll feel informed rather than pressured.

**Data:** The top Meta ads target parents of teens with acne, but /pages/stop-acne leads with "TODAY ONLY: ACNE DAY SALE 45%" and stacks urgency tactics (Source: Meta Ads, Site Screenshots). 51% of visitors who reach checkout abandon (Source: Shopify Analytics). Reviews show skepticism is a real barrier: "I was VERY skeptical. I had a serious case of buyers remorse" and "I thought I had probably fallen for a scam" (Source: Landing Page Social Proof, Reviews). Meanwhile, Norse has strong trust assets underused on this page: 409 clinicians on FrontrowMD, 6,328+ reviews, 60-day money-back guarantee, and a unique Arctic botanical ingredient story (Source: PDP Screenshots, Competitor Research).

**V1: Trust-First Hero (Replace Urgency with Credibility)**
Replace the "TODAY ONLY: ACNE DAY SALE 45%" headline and urgency banner with a credibility-led hero. Lead with the Clinicians' Choice badge (409 clinicians on FrontrowMD), the 6,328+ review count, and the 60-day money-back guarantee. Keep the same product imagery. Move the discount to a secondary position below the fold, presented as a straightforward "Subscribe & Save" offer without artificial urgency. Remove the countdown timer, "LIMITED STOCK," and "OUR BIGGEST DISCOUNT EVER" text. Keep one clear CTA.
**Brief:** On mobile, the hero should show the Clinicians' Choice badge and star rating above the headline, with the money-back guarantee as a line directly below the CTA button. On desktop, the left half stays as the product image (current), the right half gets the restructured copy. The scrolling "OUR RETURN POLICY IS SIMPLE" banner stays (it's a trust signal, not urgency). Remove the "WANT UP TO 45% OFF?" sticky popup in the bottom-left corner for this variation only. The discount section below the fold should show a clean price comparison: "One-time: $XX / Subscribe: $XX (save 40%)" with no countdown or scarcity language.

**V2: Ingredient Education Hero (Match Ad #3's Angle)**
Replace the discount hero with the ingredient education story that Ad #3 uses to attract clicks. Headline: "Botanical Buffet Of Arctic Plants For Blemishes" (already on the homepage, not on this LP). Below, show 4 key ingredients with one-line benefits (tamanu oil: anti-bacterial + scar healing, calendula: soothes inflammation, sea buckthorn: omega-7 for skin regeneration, beeswax: antimicrobial humectant). These are the same ingredients listed in the Ad #3 copy. Below the ingredients, add the Clinicians' Choice badge and a single CTA. No discount in the hero. Discount appears only below the fold.
**Brief:** On mobile, the hero shows the headline, then a horizontal scrollable row of 4 ingredient cards (icon + name + one-line benefit), then the Clinicians' Choice line, then the CTA. On desktop, ingredients display as a 4-column grid between headline and CTA. Product imagery stays the same. The rest of the page below the fold remains unchanged (reviews, before/afters, media logos). Remove the countdown timer, "TODAY ONLY," and "LIMITED STOCK" for this variation. Keep the "WANT UP TO 45% OFF?" popup removed as well.

---

## Slot 2: PDP Pricing Clarity & Trust Optimization

**Type:** A/B test (2 variations vs. control)
**Page:** /products/kill-acne-redness-ritual (https://norseorganics.co/products/kill-acne-redness-ritual). 83,769 direct sessions/mo, plus overflow from landing pages that link to this PDP.
**Revenue potential:** 83,769 sessions/mo x 0.5% CR lift x $82.96 AOV = $34,747/mo additional revenue. This is conservative because landing page traffic also funnels here.

**Hypothesis:** If we simplify the pricing presentation and remove artificial urgency from the PDP, more visitors will add to cart because the offer will feel straightforward instead of suspicious.

**Data:** The PDP currently shows a countdown timer ("PRICE INCREASE IN: 00:09:55"), conflicting discount percentages (22% one-time vs 45% subscribe vs 40% in header), and EUR pricing for a 94% US audience (Source: Site Screenshots, Shopify Analytics). Reviews cite price-to-value concerns: "90 bucks for this tiny travel sized" and "for the cost I had MUCH higher hopes" (Source: Product Reviews). Competitors price their teen acne systems at $39-75 (Source: Competitor Research). Norse's Clinicians' Choice section (409 clinicians on FrontrowMD) is a strong differentiator but sits below the pricing section, buried under urgency elements (Source: PDP Screenshot).

**V1: Clean Pricing (Remove Urgency, Fix Currency)**
Remove the countdown timer entirely. Display prices in USD only (not EUR) for US visitors. Simplify to two clear options: "One-time: $88" and "Subscribe & Save: $68/shipment (save 23%)." No coupon code required, no "SAVE 45% ON YOUR 1ST PURCHASE" badge, no "LOWEST PRICE ever" claims. Move the Clinicians' Choice badge above the pricing section so it appears before the price. Keep the 60-day money-back guarantee line directly above the ATC button.
**Brief:** On mobile, the buy box order becomes: (1) product title + review count, (2) Clinicians' Choice badge with "409 clinicians recommend this" line, (3) pricing toggle (one-time / subscribe), (4) quantity selector, (5) "No Acne in 60 days or money back" guarantee line, (6) ATC button. No countdown timer. No "PRICE INCREASE IN" element. On desktop, same order in the right column. The subscribe option should auto-calculate savings in dollars, not percentages. Image carousel and review slider on the left remain unchanged.

**V2: Value Justification (Address Price Objection Head-On)**
Keep V1's clean pricing changes (no timer, USD, simplified options). Add a "What's Inside" breakdown directly below the product title showing the 3 products in the ritual (Acne Killer Night Balm, 6-in-1 Day Balm, Premium Face Scrub) with individual values and a "Ritual Price" total. This reframes $88 as a bundle deal rather than a single product price. Below the breakdown, add "Lasts 60-90 days" with a daily cost calculation ($88 / 60 days = $1.47/day).
**Brief:** On mobile, the "What's Inside" section is a compact vertical list: three rows, each showing product tin icon + product name + "worth $XX." Below the list, a summary line: "3 products worth $XX. Ritual price: $88." Then the per-day cost: "$1.47/day for clear skin." On desktop, this displays as a horizontal 3-column layout with the summary line centered below. Everything else from V1 applies (no timer, USD, Clinicians' Choice above price, guarantee above ATC). Sequencing note: this variation builds on V1's changes and adds the value breakdown.

---

## Slot 3: Checkout Abandonment Reduction (Cart Drawer)

**Type:** A/B test (2 variations vs. control)
**Page:** Cart drawer (site-wide, triggered on all pages when items are added). Appears for all 53,648 add-to-cart sessions/mo.
**Revenue potential:** 46,062 checkout sessions/mo x 5% reduction in abandonment x $82.96 AOV = $191,036/mo additional revenue. The 51% abandonment rate means even a modest improvement moves significant revenue.

**Hypothesis:** If we add objection-handling content and pricing clarity to the cart drawer, more visitors will complete checkout because their concerns about price, shipping, and product legitimacy will be addressed before they reach the checkout page.

**Data:** 51% of visitors who reach checkout abandon (Source: Shopify Analytics). The current cart drawer shows upsells, a subscribe toggle, and a "SECURE CHECKOUT" button but no objection-handling content (Source: Cart Drawer Screenshot). The 60-day money-back guarantee, Clinicians' Choice endorsement, and free shipping status are absent from the cart. Reviews show price and trust are the top objections: "I was VERY skeptical," "for the cost I had MUCH higher hopes" (Source: Product Reviews). The currency also shows EUR in the cart for US visitors (Source: Cart Drawer Screenshot).

**V1: Trust Stack in Cart Drawer**
Add three trust signals between the cart total and the checkout button: (1) "60-Day Money-Back Guarantee" with a shield icon, (2) "409 Clinicians Recommend" with the FrontrowMD badge, (3) "Free Shipping" confirmation (currently only shown as a progress bar at top). Remove the "YOU MIGHT ALSO LIKE" upsell section entirely to reduce decision fatigue and keep the visitor focused on checkout. Fix currency to USD for US visitors.
**Brief:** On mobile, the cart drawer currently shows: free shipping bar → product → subscribe toggle → total → checkout button → payment icons. For V1, insert the 3 trust signals as a compact horizontal row of icons + text between the total and the checkout button. Each signal is one line: icon + short text. No upsell section on the left. The cart drawer should be narrower and faster to scan. On desktop, same layout. The trust signals stack vertically in a bordered box above the checkout button. Currency displays in USD for visitors with US IP.

**V2: Savings Summary + Trust Stack**
Keep V1's trust signals. Add a "Your Savings" breakdown above the trust stack showing: original price, discount amount, and final price in a clear 3-line format. If the visitor has the subscribe toggle on, show the recurring price and cumulative annual savings ("Save $XX/year with Subscribe & Save"). This addresses the discount confusion by making the math explicit in the cart itself.
**Brief:** On mobile, between the cart total and trust signals, add a savings summary box with a light background: "Retail: $XXX" (strikethrough), "Your price: $XX," "You save: $XX." If subscribe is toggled on, add a fourth line: "Annual savings: $XX." Then the trust signals from V1. Then checkout button. On desktop, same layout. The savings box and trust signals share the right column of the cart drawer. The upsell section ("YOU MIGHT ALSO LIKE") stays removed. Sequencing note: this variation builds on V1 and adds the savings breakdown.

---

## Future Slot Candidates

Strong test ideas that didn't fit into this month's 3 slots:

1. **Dedicated teen landing page redesign.** /pages/stop-acne-teens (87K sessions/mo) is nearly identical to /pages/stop-acne with "for teens" appended. A true teen-specific page with age-appropriate messaging, parent-focused trust signals, and teen before/afters would better match the teen-targeted ads.

2. **Muscle & Joint Builder PDP fix.** The media section shows acne quotes on a joint pain product page. Currency is mixed USD/EUR. Both recent reviews are negative. This page needs a content audit and likely a messaging overhaul.

3. **Quiz funnel optimization.** /pages/quiz-v1 gets 16,933 sessions/mo. Quizzes typically convert higher than standard landing pages. If this quiz is underperforming, optimizing it could capture high-intent traffic.

4. **Checkout page social proof.** If checkout-level data shows where visitors drop (payment info, shipping, order review), adding review snippets or the money-back guarantee to the checkout page could reduce abandonment further.

5. **Homepage hero test.** 99K sessions/mo on the homepage. The current hero leads with a single review quote (Linda). Testing a hero that leads with the 500K cured claim or the Clinicians' Choice badge could improve conversion for non-ad traffic.

6. **Currency localization.** Not an A/B test. The site should display USD for US visitors and EUR for European visitors. This is a dev fix, not a test.

7. **Subscription value communication.** Loop Subscriptions drives $741.7K/mo (25% of revenue). The subscribe toggle exists but the value prop is buried behind a coupon code (VIKING10). Making subscription the default selection with clear savings could grow this channel.
