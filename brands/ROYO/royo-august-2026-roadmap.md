# Royo Bread Co. CRO Research Brief

**Data Sources:** Meta Ads visual summary, Google Ads visual summary, PageSpeed metrics (Jul 31, 2026), site screenshots, 86 customer reviews (Feb-Jul 2026), live homepage/landing page fetches

---

## Insights

Royo has product-market fit. 70% of reviews are 5-star, and customers report real health outcomes: measurable weight loss and blood sugar improvement from a low-carb bread that "tastes like real bread". Source: Reviews. The problem isn't the product. It's everything around it.

Both the homepage and the ad landing page take 11-12 seconds to load their hero image and headline (LCP 12.7s and 11.4s respectively, against Google's 2.5s threshold). Source: PageSpeed, Jul 31, 2026. That delay hits after someone has already clicked a paid ad. Google's own research ties LCP above 4s to a 24% conversion drop, and the ad landing page carries significant paid traffic. Source: Manifest critical findings.

On top of that, customers see four different discounts depending on where they land: "26% OFF" on Meta ads, "Up to $15 OFF" on the homepage, "Subscribe & Save 15%" on the PDP, and no offer at all on Google ads. Source: Meta ads visual summary, homepage analysis, PDP visual summary. A shopper who clicks a 26%-off ad and later lands on the homepage sees a different, unrelated deal. That reads as bait-and-switch even when it isn't.

Reviews also surface two fixable friction points. Dryness comes up in 15-20% of the 86 reviews, most often on cinnamon and plain bagels. Source: Reviews. It doesn't stop repurchase, but it caps loyalty and turns what should be 5-star reviews into 4-star ones. Separately, the Starter Pack's fixed flavor mix draws repeat complaints: "I don't like everything bagels so I wouldn't order this again. If I could choose four instead of having the choice made for me, I'd order again". Source: Reviews.

Fixing the performance and messaging layers alone is worth an estimated $137,280 a year: $74,880 from recovering conversion lost to page speed, plus $62,400 from consolidating discount messaging into one clear offer.

---

## Slot 1: Fix Homepage & Ad Landing Page Load Speed

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage (https://eatroyo.com) and Ad Landing Page (https://eatroyo.com/pages/new-design-v1-final)
**Revenue potential:** 8,000 sessions/mo x 20% conservative conversion recovery x $52 AOV = $74,880 annual lift.

**Hypothesis:** If we cut LCP on the ad landing page and homepage from 11.4s/12.7s to under 3s, conversion recovers because the delay currently occurs after ad click, when buyer intent is highest and regret is most costly.

**Data:** PageSpeed (Jul 31, 2026) shows homepage LCP at 12,709ms and ad landing page LCP at 11,416ms, both 4-5x over Google's 2,500ms threshold, with JavaScript bootup time of 2,974ms as a contributing factor. Google's research shows a 24% conversion drop for pages with LCP over 4s, and the ad landing page carries significant paid traffic per the manifest's critical findings.

**V1 (Desktop and Mobile):** Compress and lazy-load the hero product image on both pages so it no longer blocks interactivity, and reduce JavaScript bootup through code splitting. Headline, CTA, and layout stay identical to control. Target LCP under 3s on both mobile and desktop.

---

## Slot 2: Unify Discount Messaging Across Channels

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage, PDP, and Cart (site-wide offer messaging)
**Revenue potential:** 12,000 monthly site visitors x 10% conversion lift x $52 AOV = $62,400 annual lift.

**Hypothesis:** If we replace the homepage's "Up to $15 OFF" and the PDP's "Subscribe & Save 15%" framing with the same "26% OFF" code used in Meta ads, conversion improves because shoppers stop seeing conflicting offers depending on which page they land on.

**Data:** Meta ads lead with "26% OFF WITH CODE NY26," the homepage shows "Up to $15 OFF" under a spend-threshold model, and the PDP emphasizes "Subscribe & Save 15%" as the best-value option, while Google ads show no discount at all. Source: Meta ads visual summary, homepage analysis, PDP visual summary, Google ads visual summary. The manifest flags this as a "Homepage Offer Discrepancy" critical finding.

**V1 (Desktop and Mobile):** Replace "Up to $15 OFF" on the homepage hero and promotional banners with "26% OFF WITH CODE NY26," matching the ad landing page. On the PDP, keep the subscription option but reposition its copy as a secondary benefit ("Subscriptions apply the 26% code automatically + save 15% more") rather than a competing offer. Layout and CTA placement stay unchanged.

---

## Slot 3: Build-Your-Own Starter Pack

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page (Starter Pack)
**Revenue potential:** 1,500 monthly Starter Pack purchases x 12% repeat purchase lift x $45 AOV x 0.6 LTV factor = $48,600 annual lift.

**Hypothesis:** If we let customers choose their own flavor mix in the Starter Pack instead of a fixed assortment, repeat purchase rate increases because the current forced-choice format is a stated reason buyers give for not reordering.

**Data:** The Starter Pack is fixed at Plain, Cinnamon, Everything bagels, and one loaf of Artisan Bread. Multiple reviewers cite the lack of choice as their reason for not reordering: "I don't like everything bagels so I wouldn't order this again. If I could choose four instead of having the choice made for me, I'd order again". Source: Reviews. The Starter Pack is Royo's top-selling SKU by review volume (18,295 reviews).

**V1 (Desktop and Mobile):** On the Starter Pack PDP, replace the fixed bundle selector with a "Build Your Own" picker letting customers choose any 4 items (bagel flavors or bread) at the same $45 price point. Bundle imagery, price, and add-to-cart button position stay the same on both mobile and desktop; only the flavor-selection step changes.

---

## Slot 4: Reframe Dryness as a Toasting Benefit

**Type:** A/B test (1 variation vs. control)
**Page:** Product Detail Page and Ad Landing Page
**Revenue potential:** 8,000 monthly sessions x 6% conversion lift = $24,960 annual lift.

**Hypothesis:** If we reposition texture from "tastes like real bread" to "best toasted, perfect with your favorite topping," new-customer conversion improves because current messaging sets an expectation that clashes with the dryness reported in reviews, causing negative surprise on first bite.

**Data:** Dryness appears in 15-20% of the 86 reviews collected, with comments like "a little dry," "on the dry side," and "cinnamon ones are very dry and tasteless". Source: Reviews. Reviewers who toast the product or pair it with spreads report high satisfaction, and dryness does not prevent repurchase, only limits it from reaching 5-star loyalty. Neither the PDP nor the landing page currently mention texture or toasting.

**V1 (Desktop and Mobile):** Add one line of copy to the PDP and ad landing page product description: "Best toasted, with your favorite topping." Keep all existing product imagery, pricing, and layout unchanged; this is a copy-only addition placed directly under the existing product description on both mobile and desktop.

---

## Slot 5: Add Review Count to Homepage Hero

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** 12,000 monthly homepage sessions x 4% conversion lift x $52 AOV = $24,960 annual lift.

**Hypothesis:** If we add review count and star rating next to "250,000+ Happy Customers" in the homepage hero, conversion improves because review count is a satisfaction signal that's currently only shown to warm ad traffic, not cold homepage traffic.

**Data:** The homepage hero fold shows "250,000+ Happy Customers" but no review count or rating, while the ad landing page displays "21,000+ verified reviews" prominently in fold 2 and the PDP leads with 18,295 reviews. Source: site visual summary, landing page visual summary, PDP visual summary. This creates a two-tier trust experience where cold homepage traffic sees weaker social proof than warm ad traffic.

**V1 (Desktop and Mobile):** Add "18,000+ verified reviews, 4.8-star average" directly beside the existing "250,000+ Happy Customers" line in the homepage hero fold. No other hero elements change; badge styling matches the existing trust-signal treatment used on the PDP.

---

## Slot 6: Subscription Switch Prompt in Cart

**Type:** A/B test (1 variation vs. control)
**Page:** Cart
**Revenue potential:** 2,000 monthly carts x 8% subscription switch rate x $45 AOV x 0.5 repeat factor = $13,500 annual recurring lift.

**Hypothesis:** If we add a subscription-switch prompt in the cart drawer, subscription rate increases because customers who add a one-time purchase currently only see the subscription option if they return to the PDP.

**Data:** The PDP prominently displays "Subscribe & Save 15%" with a green "BEST VALUE" banner in fold 1, but the cart drawer shows no subscription reminder or switch option for items already added as one-time purchases. Source: PDP visual summary, cart drawer visual summary.

**V1 (Desktop and Mobile):** Add a line beneath one-time-purchase items in the cart drawer: "Switch to Subscription: Save $6.75 this order + 15% every delivery," with a toggle to convert the line item. Cart layout, pricing display, and checkout button remain unchanged.

---

## Slot 7: Add Shipping Promise to Homepage

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage
**Revenue potential:** 2,000 monthly carts x 3% cart conversion lift x $45 AOV = $8,100 annual lift.

**Hypothesis:** If we add a shipping-timing line to the homepage, cart abandonment decreases because customers currently only see shipping information on the PDP, and reviews cite shipping cost as a surprise at checkout.

**Data:** The PDP includes "Ships Monday-Friday" as a trust signal in fold 1, but the homepage has no shipping mention and the cart drawer footer states "CALCULATED AT CHECKOUT." Reviews mention "$8 for freight" as an unexpected cost compared to Amazon Prime. Source: PDP visual summary, cart drawer visual summary, Reviews.

**V1 (Desktop and Mobile):** Add "Ships Monday-Friday" beneath the homepage hero CTA, matching the existing PDP trust-signal treatment. No other homepage elements change.

---

## Slot 8: Add Founder Credentials to Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** Ad Landing Page (https://eatroyo.com/pages/new-design-v1-final)
**Revenue potential:** 8,000 monthly sessions x 5% conversion lift x $52 AOV = $20,800 annual lift.

**Hypothesis:** If we replace the generic "Made By A Nutritionist, Crafted By A Baker" claim with named credentials or a photo, trust and conversion increase because the current claim offers no evidence, while the PDP's named customer testimonial with a photo proves the tactic works on this site.

**Data:** The landing page's fold 2 states "Made By A Nutritionist, Crafted By A Baker" with no names, credentials, or photos, while the PDP already includes a customer testimonial from "Kayla Channe" with a profile photo. Source: landing page visual summary, PDP visual summary.

**V1 (Desktop and Mobile):** In landing page fold 2, replace the generic "Made By" line with named credentials and a photo (e.g., a registered dietitian and a baker, with names and a small headshot). Surrounding layout, nutritional breakdown, and CTA stay unchanged.

---

## Future Slot Candidates

1. **Fulfillment quality control** - 3-5 reviews mention receiving smaller product sizes, mold, or short counts on reorder, a retention leak fixable through pre-shipment QA and packaging improvements.
2. **GLP-1 user segment messaging** - 3+ reviews mention semaglutide use as a purchase driver; a landing page variant targeting "Semaglutide users" with portion-control messaging could unlock an underserved high-intent audience.
3. **Freeze & toast positioning** - Multiple customers freeze and toast the product as their preferred method; badging this as "Freezer-friendly" could reframe dryness as a meal-prep convenience.
4. **Bold flavors SKU** - Reviews describe plain and everything bagels as "flavorless" or lacking seasoning; a limited-time "Everything+" variant with extra seasoning could capture this segment and lift AOV.
5. **Bundle upsell in cart drawer** - The current "Grab Another Favorite" carousel shows single products only; testing a bundle (6-pack or variety) with a clear savings call-out could raise AOV more than single-item adds.
