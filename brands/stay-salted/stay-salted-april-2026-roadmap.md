# Stay Salted CRO Research Brief

**Data Sources:** Meta Ads, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots

## Insights

The core problem is a leaky bucket. SALTED is spending on Meta ads, driving runner-specific traffic, and landing all of it on a mobile homepage that takes 64.2 seconds to render its largest content element. Most visitors are gone before they see the product. Those who stay encounter a generic "BUILT ON DEDICATION" opener that ignores the specific promise in the ad that brought them there.

The Strava proof in Ad 2 - a real athlete's 5K time dropping from 19:41 to 18:28 with SALTED - is the most compelling piece of social proof the brand has. It's specific, credible, and verifiable in a category full of vague hydration claims. It does not appear anywhere on the landing page. Visitors click expecting evidence and find brand positioning instead.

Two of four customer reviews independently mention mental clarity and focus as benefits, with no prompting. Neither the ads nor the landing page mention this. The pharmacist who runs 40km/week and works two jobs is describing a dual-use case that could expand SALTED's audience well beyond endurance athletes. The signal is sitting in the review data, invisible to prospects.

The cart adds a final friction layer: a promo code field visible by default trains customers to search for discounts before completing purchase. A free shipping progress bar simultaneously contradicts the €0.00 delivery shown directly above it. Trust erodes at the moment of highest purchase intent.

SALTED is 40% cheaper per sachet than LMNT with better potassium. The product is in a near-uncontested niche in Bulgaria. The opportunity is not the product. It's the funnel.

**Pre-test blocker:** The product page showed as out of stock as of April 29, 2026. No tests should launch until stock is confirmed available.

---

## Slot 1: Performance-Optimized, Message-Matched Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage as paid ad landing page (stay-salted.com)
**Revenue potential:** Without GA/Shopify access, session volume is estimated. At a conservative 1,500 paid sessions/month, a CR lift from ~1% (current, hampered by 64.2s mobile LCP) to 3% = 30 additional orders x €25.90 AOV = ~€777/month. Actual uplift may be significantly higher given the severity of the current mobile performance failure.

**Hypothesis:** If we serve paid ad traffic a lightweight, pain-point-specific landing page instead of the current homepage, conversion rate will increase because the two biggest blockers - a 64.2s mobile LCP and a message mismatch between ad promise and landing page - are eliminated simultaneously.

**Data:** Mobile LCP is 64.2s (PageSpeed Insights, April 29, 2026) against a 2.5s threshold. Primary cause: 12,198 KB of unoptimized images on a 36,373 KB total page. All 3 analyzed Meta ads (out of many active campaigns) target runners with specific pain points but land on a homepage that opens with "BUILT ON DEDICATION" and a product image. The Strava proof from Ad 2 (Vladimir Balabanov's 5K: 19:41 to 18:28 with SALTED) - the most credible social proof in the brand's arsenal - is absent from the landing page entirely (Sources: Page Speed, Meta Ads, Mobile Homepage Screenshots).

**V1:** Build a new, lightweight page to serve as the destination for all Meta ad traffic, replacing the current homepage as the ad landing URL. Target sub-3s LCP by serving WebP images at mobile-appropriate sizes, deferring non-critical JavaScript, and excluding the athletes grid and formula accordions from the initial render.

On mobile: Fold 1 contains a single headline that mirrors the runner's pain point from the ad. For the cramping angle: "Крампи по средата на бягането? Свърши с тях." (Cramps mid-run? Finish them.) For the pace angle: "6.3% по-бързо. Истински данни от Strava." (6.3% faster. Real Strava data.) Directly below the headline, the buy box (1-box at €25.90 and 2-box at €51.80 with free shipping tag, yellow-green "Вземи сега" CTA) is visible without any scrolling. No hero product image above the fold.

Fold 2 on mobile: the Strava comparison image (Vladimir Balabanov's 5K: 19:41 before vs. 18:28 with SALTED, labeled with his name and sport). Below it: two or three short customer quotes - Stoyan Stoyanov's run performance quote and Mladen Dikov's endurance quote.

Fold 3 on mobile: the formula callout (Na 1000mg, K 300mg, Mg 60mg) with one supporting line: "40% по-евтино на саше от LMNT. По-добър калий." (40% cheaper per sachet than LMNT. Better potassium.) No accordions - all key info is visible inline.

Fold 4 on mobile: a second "Вземи сега" CTA.

On desktop: two-column layout. Left column shows the headline, Strava proof image, and two customer quotes stacked vertically. Right column shows the buy box, sticky as the user scrolls. Formula callout appears below the fold as a full-width horizontal bar.

Use a URL parameter (e.g., ?angle=cramp or ?angle=pace) to swap the fold-1 headline dynamically based on which ad angle the visitor came from. This avoids building separate pages for each ad.

---

## Slot 2: Homepage Hero Restructure

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (stay-salted.com) - organic, direct, and non-paid traffic
**Revenue potential:** Estimated 500 organic/direct sessions/month. A CR lift from ~2% to 4% = 10 additional orders x €25.90 AOV = ~€259/month.

**Hypothesis:** If we replace the current mobile first fold (product image and brand tagline with buy box below fold) with a performance-proof headline and a buy box visible without scrolling, conversion rate will increase because visitors encounter a compelling proof point before they have to do anything.

**Data:** On mobile, the current first fold shows the SALTED logo, "BUILT ON DEDICATION" tagline, and a large product sachet image. The buy box requires scrolling past the full image. Two of four customers independently cited fast-acting results (effects within 1-2 uses) as a standout benefit. Neither this nor the Strava performance proof appears in any headline copy on the existing page (Sources: Mobile Homepage Screenshots, Reviews).

**V1:** On mobile: remove the full-screen product sachet image from fold 1. Replace with a two-line headline block. Large bold line: "6.3% по-бързо. Истински данни от Strava." (6.3% faster. Real Strava data.) Sub-line beneath it: "Усеща се от първото отпиване." (You feel it from the first sip.) Directly below the headline, the buy box (both pack options, yellow-green CTA) must be fully visible on a standard mobile screen without scrolling. Move the product sachet image to below the buy box as a supporting visual element.

On desktop: keep the existing two-column layout. Replace only the "BUILT ON DEDICATION" tagline in the left column with the performance-proof headline. Keep the product image in the left column. Keep the buy box in its current right-column position.

All other page elements - the athlete section, reviews, formula section, accordions, and benefit columns - remain unchanged on both mobile and desktop.

---

## Slot 3: Cart Optimization

**Type:** A/B test (1 variation vs. control)
**Page:** Cart page (stay-salted.com cart)
**Revenue potential:** Estimated 300 cart sessions/month. A 5-percentage-point lift in cart completion rate = 15 additional orders x €25.90 AOV = ~€389/month.

**Hypothesis:** If we collapse the default-visible promo code field, fix the contradictory free shipping messaging, and add a 2-box bundle upsell, cart completion rate will increase because we remove the signal that customers may be overpaying and eliminate the trust-eroding contradiction in the shipping display.

**Data:** The cart shows a promo code input field expanded and visible by default. Customers without a code feel they are overpaying and leave to search for discount codes, often not returning. The cart simultaneously displays €0.00 delivery and a progress bar stating "add €17.56 more to unlock FREE SHIPPING" - these directly contradict each other. The homepage and store page state free shipping applies to 2+ boxes, but the cart shows free shipping on a single box. No upsell toward the 2-box option exists at the highest-intent moment in the funnel (Sources: Cart Screenshot, Site Screenshots).

**V1:** Three changes applied together as a single variation:

Change 1: Replace the default-open promo code input with a collapsed text link: "Имаш промо код?" (Have a promo code?). The input field appears only when the link is clicked. This removes the discount-seeking signal for customers who do not have a code.

Change 2: Fix the shipping contradiction. Audit whether free shipping actually applies to single-box orders or only to 2+ boxes, then make the cart reflect that accurately. If shipping is free on all orders, remove the progress bar entirely. If the threshold is 2 boxes (€51.80), update the delivery line to show the actual shipping cost for a 1-box order and update the progress bar to show the correct gap.

Change 3: Add a bundle upsell card above the subtotal line. Text: "Добави още 1 кутия - безплатна доставка включена." (Add 1 more box - free shipping included.) Show the price upgrade inline: "€25.90 → €51.80." Include a single-tap button that upgrades the cart from 1 box to 2 boxes without leaving the cart page.

On mobile: changes stack vertically in the existing cart layout. The collapsed promo code link sits in the same position as the current input field. The bundle nudge card sits between the product line and the subtotal. On desktop: same structure with wider card layout.

---

## Future Slot Candidates

- **Subscription model (dev project, 1-2 slots):** LMNT drives LTV through subscribe-and-save at $1.30/sachet vs. $1.50 one-time. SALTED has no recurring purchase option. A native Shopify subscription integration (e.g., Recharge or Seal Subscriptions) with a ~10% discount could significantly increase customer LTV and reduce churn. This is a dev project, not a test.
- **Mental clarity ad angle:** Two of four reviews mention cognitive benefits independently. Testing a Meta ad targeting working athletes with a focus/clarity angle ("Stay sharp through the second shift") could open a second customer persona without changing the product.
- **Review volume build:** The review base is very thin. A post-purchase email requesting a review with a photo (plus a small incentive like a discount on next order) would strengthen social proof across the site and give future tests better qualitative data.
- **Flavor expansion:** One flavor vs. LMNT's 11 is a conversion barrier for taste-sensitive buyers. New SKUs would also enable variety-pack bundle testing.
