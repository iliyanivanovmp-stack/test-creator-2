# Primal Queen CRO Research Brief

**Data Sources:** Meta Ads, Google Ads Transparency, Reviews & UGC (Amazon), Page Speed / Core Web Vitals, Site Screenshots, CRO Ebook (Billion Dollar Websites), CRO Community Research

---

## Insights

Every dollar Primal Queen spends on Meta and Google lands on a page that takes 11 seconds to show the hero image on mobile. The paid ad landing page (/pages/tiktok) weighs 38.5MB and scores 41/100 on performance. Google's own research pegs a 0.1-second LCP improvement at 8.4% more ecommerce conversions. Primal Queen is 8.5 seconds over the 2.5-second threshold. This isn't a small optimization. It's the most expensive problem on the site.

The second problem is message match. The top Meta ad shows a "Hormone Reset Kit" at $186 → $29 with "Last Chance" urgency. It lands on a generic page about ancestral nutrition and beef organ subscriptions. The specific kit, the $29 price, and the urgency are gone. Google search ads promise "Up to 62% Off": the page delivers "Get 1 Month Free." These are the same value in different frames, but the visitor's brain expects continuity. When the promise in the ad doesn't match the page, The Gator wakes up The Judge, and the sale is over.

Reviews are the strongest signal in this audit. Over 1,200 customers found one review helpful enough to click: a 52-year-old describing 9 months of consistent energy, lighter periods, and functional days without the fatigue that used to control her. A woman with PMDD describes her period going from 12 days to 7, flow from "changing a disc every hour" to manageable. A 54-year-old who stopped for 4 weeks reports every menopause symptom returning with "a vengeance." These are not vague supplement reviews. They are powerful, specific, and credible. None of them are in the hero.

What is in the hero: "Since using Primal Queen, I feel more balanced, focused, and energized. Highly recommended!" (Sarah R.) The star rating in the carousel appears to be 3 out of 5. The most powerful social proof in the business is buried in the review section while the hero shows a text graphic that says "BECOME A PRIMAL QUEEN TODAY," with no product visible.

One operational issue is not a CRO test but needs to be flagged: at least 10 independent reviews cite broken and empty capsules arriving in the bag. "Half the bag is unusable... I spent $60 on roughly 20 useable pills." Loyal customers who explicitly love the product are not reordering because of this. That is a packaging defect driving silent churn that no A/B test will fix.

Revenue opportunity estimate: session data was not shared, but conservative assumptions based on 12+ active Meta creatives and multiple Google search/display/shopping campaigns suggest 40,000+ sessions per month to the paid landing page. At a 2% cold-traffic conversion rate and $44 AOV (monthly subscription), that's $35,200/mo in landing page revenue. A 15% lift from fixing LCP alone (well below what Google's benchmarks imply for an 8.5-second improvement) adds $5,280/mo, or $63,360 per year. Stack the headline, social proof, and checkout tests and the compounding effect is significant.

---

## Slot 1: Landing Page Speed: LCP from 11s to Under 2.5s

**Type:** A/B test (1 variation vs. control)
**Page:** /pages/tiktok (primalqueen.com/pages/tiktok), the destination for all paid Meta and Google ad traffic
**Revenue potential:** 40,000 estimated sessions/mo x 15% conservative CR lift x 2% baseline CR x $44 AOV = ~$5,280/mo additional revenue. LCP benchmarks imply far higher. This uses 15% as the floor, not the ceiling.

**Hypothesis:** If we reduce the landing page LCP from 11.0s to under 2.5s, conversion rate will increase because mobile visitors are currently bouncing before the hero loads.

**Data:** Lighthouse mobile test (May 7, 2026) shows /pages/tiktok at 11.0s LCP, 38.5MB total payload, 44.8s Time to Interactive, and 41/100 performance score. Google research: 0.1s LCP improvement = 8.4% ecommerce conversion lift. Documented case study: 31% LCP improvement led to 8% more sales. The landing page payload is nearly double the homepage (38.5MB vs. 21.5MB), driven by uncompressed images and 1,247 KiB of unused JavaScript. (Source: Page Speed / Core Web Vitals)

**V1:** A rebuilt version of /pages/tiktok with identical content and layout, optimized for speed:
- All images converted to WebP format with explicit width/height attributes
- Hero image/video preloaded via `<link rel="preload">` so it is the first asset the browser fetches
- Non-critical JavaScript deferred or lazy-loaded (target: reduce unused JS from 1,247 KiB to under 200 KiB)
- Render-blocking CSS inlined for above-the-fold styles; remaining CSS loaded asynchronously
- Total page payload target: under 5MB
- Target LCP: under 2.5s
- On mobile: the hero renders fully within the first 2-3 seconds; the founder story, testimonials, and subscription offer section load progressively as the user scrolls. No visible layout shift (CLS target: 0, same as current). On desktop: same progressive loading; hero video loads at full resolution after LCP image is painted.
- All existing content: copy, CTAs, offer, and testimonials remains unchanged. This is a speed-only test.

---

## Slot 2: Message Match: Hormone Reset Kit Dedicated Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** Control: /pages/tiktok (current destination for all Meta ads). Variation: new dedicated landing page, e.g., /pages/hormone-reset-kit. Traffic split: Meta Ad 2 (Library ID: 933712316262038, "Hormone Reset Kit $186 → $29, Last Chance") only.
**Revenue potential:** Assuming Ad 2 drives 20% of total paid sessions = 8,000 sessions/mo. Message match correction benchmarks at 30-35% CR lift. At 30% lift: 8,000 x 2.6% vs. 2% CR = 48 additional purchases x $29 (kit price as entry offer) = $1,392/mo, not counting downstream subscription LTV, which is the real prize.

**Hypothesis:** If we send the Hormone Reset Kit ad to a dedicated landing page that leads with the $29 kit offer, conversion rate will increase because the ad promises a specific product at a specific price and the current page delivers neither.

**Data:** Meta Ad 2 (active since Mar 2, 2026) shows "HORMONE RESET KIT" with a crossed-out $186 price and a $29 price, alongside "Last Chance" urgency text. The /pages/tiktok landing page opens with "STOP SETTLING For Low Energy, Hormonal Chaos..." and routes visitors to a general Beef Organs subscription. The $29 kit, the specific "Hormone Reset Kit" name, and the "Last Chance" urgency all disappear at the click. Industry data: dynamic text replacement and dedicated ad landing pages lift conversion 30-35% by restoring ad-to-page relevance. (Source: Meta Ads, CRO Community Research)

**V1:** A new landing page built specifically for the Hormone Reset Kit ad. On mobile and desktop:
- Hero headline: "Hormone Reset Kit: $29 Today Only" (matching the ad's exact offer and urgency language)
- Hero subheadline: "Everything you need to reset your hormones, reduce PMS, and reclaim your energy. One kit."
- Hero image: the Hormone Reset Kit product shot (same creative used in the Meta ad)
- Price prominently displayed: ~~$186~~ $29, with "Last Chance" or countdown urgency element
- Kit contents listed with icons: what's included, why each piece matters for hormone health
- CTA: "Claim My Kit for $29" (green button, above the fold on mobile)
- Below the fold: founder story condensed to 2-3 paragraphs, 3 customer testimonials specific to hormonal improvements (Briana's PMDD review, PippaCan's hot flash/menopause review, the 53rd birthday energy review), trust badges (365-day guarantee, Made in USA, free shipping)
- On mobile: single-column layout, CTA button sticky at bottom. On desktop: two-column hero with kit image on right, headline/price/CTA on left. Product image scales to full bleed on desktop.

---

## Slot 3: Landing Page Hero Headline: Dream Outcome vs. Pain Point

**Type:** A/B test (1 variation vs. control)
**Page:** /pages/tiktok (primalqueen.com/pages/tiktok)
**Revenue potential:** 40,000 sessions/mo x 10% CR lift (conservative; headline optimization research averages 34%) x 2% baseline CR x $44 AOV = ~$3,520/mo.

**Hypothesis:** If we replace the pain-avoidance headline with a Dream Outcome headline that names specific results customers report, conversion will increase because visitors have something concrete to move toward instead of only something to move away from.

**Data:** Current headline leads with "STOP SETTLING For Low Energy, Hormonal Chaos, and Feeling Like a Stranger in Your Own Body." This is a list of negatives. Reviews document specific outcomes with high clarity and emotional weight: steady all-day energy (1,207 helpful votes), periods reduced from 12 days to 7 (294 helpful votes), hot flashes stopped (multiple reviews), libido restored (multiple reviews), menopausal symptoms returned when the product was stopped. None of these specific outcomes appear in the headline or subheadline. CRO ebook: "Headlines are supposed to tell your customers the end result of using your product... The Dream Outcome." Headline optimization tests average 34% CR lift. (Source: Reviews, Site Screenshots, CRO Ebook Chapter 6, CRO Community Research)

**V1:** Replace the current two-line headline and subheadline with:
- Headline: "Wake Up With Energy. Sleep Through Lighter Periods. Feel Like Yourself Again."
- Subheadline: "Beef organ superfoods formulated specifically for women's hormones, energy, and cycle health, trusted by over 1 million women."
- Flash sale badge above the headline stays: "FLASH SALE: GET 1 MONTH FREE"
- CTA, trust bar, and testimonial carousel below the headline stay unchanged
- On mobile: headline stacks in two lines max, font size 28-32px, same pink/purple color scheme as current. On desktop: headline is 36-40px, positioned left of the hero image. Subheadline is one line on desktop, two lines on mobile. Nothing else on this page changes.

---

## Slot 4: Landing Page Hero: Product Image Above Fold

**Type:** A/B test (1 variation vs. control)
**Page:** /pages/tiktok (primalqueen.com/pages/tiktok)
**Revenue potential:** 40,000 sessions/mo x 8% CR lift x 2% baseline CR x $44 AOV = ~$2,816/mo. The product appearing above fold sets purchase intent earlier and reduces scroll-to-conversion depth.

**Hypothesis:** If we replace the text-graphic oval ("BECOME A PRIMAL QUEEN TODAY") in the hero with a clear product image, conversion will increase because visitors will know what they're considering buying before they decide to scroll.

**Data:** Current hero image is an oval containing the text "BECOME A PRIMAL QUEEN TODAY." No product is visible in fold 1. The Beef Organs product bag first appears in fold 3, approximately 2 full scrolls below the fold. CRO ebook: "One hundred percent of users will see your Hero Image... images and videos are the most overlooked aspect of a website's UX... images and videos make up more than 50% of the assets on a website." The Gator needs to see the product to feel the purchase is concrete. (Source: Site Screenshots, CRO Ebook Chapter 6)

**V1:** The oval text graphic in the hero is replaced with a product shot of the Primal Queen Beef Organs pouch, held at a slight angle against a pink paint-splash background consistent with brand aesthetics. The "GET 1 MONTH FREE" pink circular badge that overlays the bottom-right of the current oval is retained, overlaying the bottom-right corner of the product image. On mobile: product image is centered, full-width within the hero, stacked below the headline and CTA. On desktop: product image occupies the right column of the split hero layout, same proportions as the current oval. All headline copy, CTA, trust bar, and testimonial carousel stay unchanged.

---

## Slot 5: Landing Page Subscription Offer: % Off vs. Free Month Framing

**Type:** A/B test (1 variation vs. control)
**Page:** /pages/tiktok, subscription offer section (below the fold)
**Revenue potential:** 40,000 sessions/mo x assumed 5% reach subscription section x 15% lift in subscription take rate x $44 recurring AOV = ~$1,320/mo in first-month revenue, plus LTV from subscribers retained.

**Hypothesis:** If we reframe the subscription offer from "Get 1 Month Free" to "Save 30% Every Month. Forever," subscription conversion will increase because percentage-off framing is more tangible and matches the "Up to 62% Off" language already used in Google search ads.

**Data:** Google search ads (observed May 7, 2026) lead with "Up to 60% Off" and "Up to 62% Off" headlines. Visitors arriving from Google are primed to expect a percentage discount. The landing page delivers "Get 1 Month Free," a different frame for a similar value. When the ad promises % off and the page delivers a free month, visitors must mentally convert to compare, which adds friction. Simplest math wins. (Source: Google Ads Transparency, Site Screenshots)

**V1:** In the subscription offer section on /pages/tiktok:
- Section headline changes from "Get 1 Month Free" (or equivalent) to: "Save 30% Every Month. Forever."
- Monthly savings shown in dollar terms below the headline: "You save $16.20 with every order" (based on 30% of $54 monthly refill price; adjust to actual discount amount).
- 3-month plan shown as featured/recommended with "Most Popular" tag, price displayed as "From $37.95/mo" (or actual price), full savings shown as "$23.10 saved per shipment."
- "Get 1 Month Free" language removed from this section entirely. The flash sale badge above the hero is unaffected.
- On mobile: offer cards stack vertically, savings amount is large and prominent. On desktop: offer cards sit side by side, same layout as current, with updated copy only.

---

## Slot 6: Homepage Hero: Social Proof Upgrade

**Type:** A/B test (1 variation vs. control)
**Page:** primalqueen.com/ (homepage)
**Revenue potential:** 80,000 estimated sessions/mo x 5% CR lift x 1.5% baseline CR (organic/branded traffic converts lower than cold paid traffic) x $44 AOV = ~$2,640/mo.

**Hypothesis:** If we replace the generic hero testimonial carousel with specific outcome-driven quotes from the highest-voted reviews, trust will increase and homepage conversion will lift.

**Data:** Current hero carousel features Sarah R.: "Since using Primal Queen, I feel more balanced, focused, and energized. Highly recommended!" The visible star rating in the carousel appears to be 3 out of 5 stars. Meanwhile, reviews with 294, 434, and 1,207 helpful votes exist, all describing specific outcomes with clinical specificity and emotional weight. "Quiet, constant stamina" after 9 months. Period from 12 days to 7. "Every symptom of menopause came back with a vengeance" when she stopped. Specific outcome testimonials outperform generic ones because they make the transformation concrete. (Source: Reviews, Site Screenshots)

**V1:** Replace the hero testimonial carousel with 3 rotating slides using verbatim quotes from the highest-helpfulness verified reviews:

Slide 1 (from the 53rd birthday review, 1,207 helpful votes):
> "My periods are now regular, shorter, and come with significantly reduced PMS. The exhaustion doesn't control me anymore. I used to think I was just lazy. This isn't the case for me now."
> Verified Buyer, 9 months on Primal Queen

Slide 2 (from Briana's PMDD review, 294 helpful votes):
> "My period went from 12 days to 7. I usually have a very heavy flow. This month it was actually manageable. I haven't felt this good in years."
> Verified Buyer, PMDD

Slide 3 (from PippaCan, stopped for 4 weeks):
> "I went off this after several months and every symptom of menopause came back with a vengeance. I knew at that point that this product absolutely worked."
> Verified Buyer, 54

Each slide shows 5 stars, reviewer first name, and "Verified Buyer" label. On mobile: single slide with swipe navigation, reviewer name below quote. On desktop: same carousel, slightly wider card, same placement as current. No other hero elements change.

---

## Slot 7: Homepage Urgency: Real Countdown vs. Perpetual Flash Sale

**Type:** A/B test (1 variation vs. control)
**Page:** primalqueen.com/ (homepage)
**Revenue potential:** Urgency tests are conversion-rate tests on existing traffic. If a genuine deadline lifts homepage CR by 10% on top of the social proof lift: 80,000 sessions/mo x 10% x 1.5% x $44 AOV = $5,280/mo. The real value is in reducing "I'll come back later" behavior.

**Hypothesis:** If the flash sale has a real, visible expiry date and the offer genuinely changes when the countdown reaches zero, urgency will become credible and time-to-purchase will decrease.

**Data:** As of May 7, 2026, "Flash Sale: GET 1 MONTH FREE" appears in 4 simultaneous locations on the homepage: the announcement bar (Marrow product competes), a badge above the headline, the scrolling ticker, and the sticky bottom CTA bar. The flash sale has been running since at least March 2, 2026 (the date the earliest Meta ad using this offer started). A "flash sale" running for 2+ months is not a flash sale. Visitors recognize patterns: when the timer never hits zero, the urgency becomes background noise. Real countdown urgency is a validated conversion lever when the deadline is genuine. (Source: Meta Ads, Site Screenshots)

**V1:** The flash sale runs with a real expiry tied to a specific campaign end date (e.g., Mother's Day: May 11, 2026 at 11:59 PM). The countdown timer in the announcement bar and hero displays days, hours, minutes, seconds, counting down to this specific date. When the timer hits zero:
- The "Get 1 Month Free" offer is replaced with standard pricing or a lower offer (e.g., "Save 20%")
- The announcement bar updates to reflect the new offer
- The scrolling ticker text updates accordingly
- The sticky bar CTA also updates

On mobile: countdown timer is integrated into the sticky bottom bar (replacing the dashed line currently shown). On desktop: countdown timer sits directly below the flash sale badge above the hero headline. Timer font is consistent with brand type (bold, dark purple). The 4 urgency elements are consolidated to 2: the announcement bar and the hero badge. The scrolling ticker is removed entirely: it competes with the announcement bar and adds page weight.

---

## Slot 8: Checkout: Hide the Discount Field

**Type:** A/B test (1 variation vs. control)
**Page:** Shopify checkout (all checkout sessions)
**Revenue potential:** Estimated 1,200 initiated checkouts/mo (implied by 800 purchases/mo at ~67% checkout completion). PayPal/comScore: 27% abandon to search for promo codes = ~324 checkout abandonments per month from this cause. Recovering 30% of those: 97 x $44 = $4,268/mo.

**Hypothesis:** If we hide the "Add discount" field behind a collapsed text link, checkout abandonment will decrease because visitors will not be prompted to leave the page to search for a promo code.

**Data:** Current Shopify checkout shows "Add discount" as a visible section. PayPal/comScore research: 27% of checkout visitors abandon specifically to search for a discount code when the field is visible. Hiding the field behind a link ("Have a promo code?") removes the visual prompt without eliminating the functionality for visitors who actually have a code. Case data: hiding the promo code field lifts checkout conversion by up to 34%. Reviews confirm customers actively compare Primal Queen's Amazon vs. site pricing, showing price-sensitivity behavior that would translate to promo code searching. (Source: Site Screenshots, Reviews (Jen, 234 helpful votes), CRO Community Research)

**V1:** The "Add discount" section in checkout is collapsed by default and replaced with a small text link below the order summary: "Have a promo code? Click here." The input field appears only when a visitor clicks this link. On mobile: the text link sits below the order summary total, in a small gray font, easily scannable but not prominent. On desktop: same treatment, a text link rather than a box or labeled section. All other checkout fields, express checkout options, trust badges, and legal disclaimer remain unchanged. The link still functions: visitors with a real code can enter it; the friction is only for those who see the field and are prompted to go looking.

---

## Future Slot Candidates

- **Checkout subscription disclaimer language:** The legal block above "Pay now" is long, formal, and anxiety-inducing. A rewrite to plain language ("We'll send your next order in 30 days. Cancel anytime in your account.") could reduce last-second abandonment without changing the legal accuracy.
- **PQ7 "Natural Ozempic Alternative" claim:** This Google display ad angle is aggressive and carries regulatory risk. Worth discussing with client before scaling.
- **Rating inconsistency across Google ads:** Three different star ratings appearing in ads (3.8★ 289 reviews, 3.8★ 11,514, 4.6★ 4,117). Auditing the source and standardizing to one credible, accurate rating could improve Google ad CTR.
- **Broken capsules packaging fix:** Not a CRO test. This is a fulfillment/quality issue. At least 10 independent reviews cite empty and broken capsules. This is a silent churn driver affecting loyal repeat buyers.
- **Post-menopausal audience segmentation:** Reviews show the product underperforms for fully post-menopausal women. Ads could be segmented to exclude or add friction for this audience, reducing refund rates and improving overall review scores.
