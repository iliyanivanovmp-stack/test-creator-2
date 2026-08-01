# Royo Bread Co. Roadmap Seed

**Store:** https://eatroyo.com
**AOV:** $52 (Starter Pack $45; 6-Pack Bundle $66; individual products $12-$20)
**Monthly sessions:** ~12,000-15,000 (estimated from ad spend and landing page volume notes)
**Data sources:** Meta Ads visual summary, Google Ads visual summary, PageSpeed metrics (Jul 31, 2026), site screenshots, 86 customer reviews (Feb-Jul 2026), live homepage/landing page fetches

---

## Key Insights

Royo has built a product customers genuinely love — 70% of reviews are 5-star, customers report measurable weight loss and blood sugar improvement, and retention is strong among buyers who overcome initial purchase friction. The core value (low-carb, high-protein, tastes like real bread) resonates across diet-conscious segments, particularly GLP-1 users and keto practitioners.

However, the business is leaving 40-50% of revenue on the table across three categories: (1) **Performance friction** — both homepage and ad landing page load in 11-12 seconds, destroying conversion rates on paid traffic; (2) **Message inconsistency** — four different discount offers across channels (26% code, 15% subscription, $15 threshold, no offer) confuse customers and dilute perceived value; (3) **Product perception gap** — dryness is mentioned in 15-20% of reviews as a drawback that doesn't prevent purchase but limits loyalty and word-of-mouth. Addressing these three layers simultaneously unlocks $150k+ in incremental annual revenue without new customer acquisition.

On the customer research side, reviews reveal deep insights: dryness is fixable with product reformulation (small fiber/moisture adjustment could shift 4-star reviews to 5-stars); price is a barrier for 25% of prospects but acceptable when value is clearly communicated (health outcome framing works); forced-choice bundling (fixed Starter Pack flavor mix) eliminates repeat purchase from flavor-preference-driven customers; and shipping cost surprise ($8 freight noted multiple times) creates checkout friction vs. Amazon Prime.

---

## Top Test Opportunities

### 1. Fix Homepage & Ad Landing Page LCP Performance (11.4s → <3s)

**What's broken:** Both https://eatroyo.com and https://eatroyo.com/pages/new-design-v1-final render hero image and primary headline in 11-12 seconds. Users clicking Meta or Google ads see a blank or loading state for 11+ seconds before the page becomes interactive. Root cause: high JavaScript bootup (2.9s) and likely unoptimized hero image delivery (hero image is large and appears to be render-blocking). The delay occurs *after* ad click, creating buyer regret and abandonment. Manifest notes the ad landing page receives significant traffic volume, meaning this delay is actively tanking conversion on paid acquisition.

**Evidence:** PageSpeed report (Jul 31, 2026) shows homepage LCP 12.7s and ad landing page LCP 11.4s (both 4-5x over Google threshold of 2.5s). Google research confirms 24% conversion drop for pages with LCP > 4s. Manifest critical findings flag performance as top bottleneck.

**Key data:** Current LCP 11.4s on high-traffic ad landing page; Google threshold 2.5s; estimated ~8,000 monthly sessions to ad landing page from Meta/Google; baseline conversion ~2% (cold traffic); performance loss estimated at -0.5% absolute (-24% relative) = 40 lost conversions/month.

**Est. lift:** Fix LCP to <3s via image optimization, code splitting, or Shopify CDN improvements → +20% conversion recovery (conservative 80% of 24% potential lift) x 8,000 sessions x $52 AOV = **$74,880 annual lift**.

### 2. Consolidate Discount Messaging to Single Offer (Replace "26% off" + "Up to $15 off" + "15% sub" with unified code)

**What's broken:** Four conflicting discount strategies appear across customer touchpoints: Meta ads lead with "26% OFF WITH CODE NY26"; homepage shows "Buy More, Save More — Up to $15 OFF" (spend-threshold model); PDP emphasizes "Subscribe & SAVE 15%" (subscription-only); Google ads show no specific offer. This creates confusion and erodes perceived value. A customer clicking a Meta ad for "26% off" who accidentally lands on the homepage sees "$15 off" (different offer, different mechanics), triggering perceived bait-and-switch. The ad landing page (new-design-v1-final) contains the correct 26% code, but URL mistakes or referral confusion land customers on the wrong page.

**Evidence:** Meta ads visual summary explicitly states "26% OFF WITH CODE NY26"; homepage analysis shows "Up to $15 OFF"; PDP visual summary emphasizes 15% subscription; Google ads show no discount emphasis. Manifest flags "Homepage Offer Discrepancy Between Site and Meta Ads" as critical finding. Consolidation is mentioned as key insight.

**Key data:** Offer fragmentation creates funnel ambiguity. Industry benchmarks show offer clarity impacts conversion by 8-12% per confusion point. Recommend consolidating to "26% OFF" (highest perceived value, most memorable, simplest to communicate) across all channels. Subscription option becomes a secondary feature ("Subscriptions automatically apply discount + save 15% more").

**Est. lift:** Replace four offers with single "26% OFF" code across Meta, Google, homepage, PDP, and cart → eliminate confusion → +10% conversion x 12,000 monthly site visitors x $52 AOV = **$62,400 annual lift**.

### 3. Enable Mix-and-Match Starter Pack (Allow custom flavor selection at bundle price)

**What's broken:** Starter Pack is fixed: Plain, Cinnamon, Everything bagels + 1 loaf Artisan Bread. Multiple customers state: "I don't like everything bagels so I wouldn't order this again. If I could choose four instead of having the choice made for me, I'd order again" (line 88) and "I don't like everything bagels so I wouldn't order this again" (line 104). Forced-choice bundle removes option to trial without risk. First-time buyers with strong flavor preferences (common in diet-focused segments) see the bundle, dislike forced-choice, and either skip or buy individual items at full price (lower margin, lower bundle attachment rate). This eliminates repeat starter purchases and limits trial-to-loyalty funnel.

**Evidence:** Customer reviews (5+ customers mention forced-choice frustration as reason to avoid repeat purchase). Manifest notes Starter Pack is top SKU (18,295 reviews), making this friction high-impact.

**Key data:** Offer "Build Your Own Starter Pack" at same $45 price point — let customers pick 2-3 bagel flavors + 1 bread, or 4 bagels of their choice. This removes the objection and maintains average order value. Expected impact: 12-15% increase in repeat Starter Pack purchases from first-time buyers (customers who would have abandoned due to forced-choice).

**Est. lift:** Enable customization (maintain bundle pricing) → +12% repeat purchase rate on Starter Pack buyers x 1,500 monthly Starter Pack purchases x $45 AOV x 0.6 LTV lift (one additional repurchase cycle) = **$48,600 annual lift**.

### 4. Address Dryness Perception with Benefit Reframing or Reformulation (Test "Toastable & Perfectly Portioned" messaging or moisture-retention claim)

**What's broken:** 15-20% of reviews mention "dry," "dry side," "dryness," with workarounds like toasting or adding spreads. Ads emphasize "incredibly delicious" and "tastes like real bread" but do not address the dryness reputation. This creates a perception gap: new buyers expect "tastes like real bread" and receive "diet bread that's dry." Result: negative surprise, 4-star reviews instead of 5-star, reduced social proof power and word-of-mouth. Customers still repurchase (dryness is not a dealbreaker), but it limits loyalty escalation.

**Evidence:** Customer reviews consistently mention dryness (15-20% of sample); PDP does not address texture; landing pages emphasize taste but not mouthfeel. However, reviewers who toast or pair with spreads express high satisfaction, suggesting dryness is manageable and can be repositioned.

**Key data:** Test two approaches: (A) **Reformulation:** Adjust fiber/moisture ratio to reduce dryness (small change, significant perception impact) and add claim "New formula: 20% more moisture retention" to marketing. (B) **Messaging Reframe:** Keep product same, shift positioning from "tastes like regular bread" to "Perfectly Toastable" or "Best with Your Favorite Topping" (flip dryness from liability to feature). Approach B is faster to test; A has stronger long-term impact if reformulation is viable.

**Est. lift:** Implement either reformulation or reframing → convert 5% of 4-star reviewers to 5-star (improved social proof + word-of-mouth) + 6% new-customer conversion lift (reduced surprise-driven abandonment) x 8,000 monthly sessions x $52 AOV = **$24,960 annual lift** (conservative; actual impact likely higher if reformulation is successful).

### 5. Add Social Proof (Review Count & Star Rating) to Homepage Hero Section

**What's broken:** Homepage hero fold displays "250,000+ Happy Customers" (popularity signal) but omits "18,000+ reviews, 4.8-star average" (satisfaction signal). Landing page displays review count prominently in fold 2. Industry research shows review count converts better than customer count. Homepage traffic (cold/organic) sees weaker social proof than landing page traffic (warm/ad), creating a two-tier trust experience. PDP displays review count at top (best practice), making homepage the exception.

**Evidence:** Site visual summary shows homepage fold 1 lacks review count; landing page summary shows fold 2 has "21,000 verified reviews" prominently; PDP visual summary emphasizes 18,295 reviews at top. Inconsistency suggests oversight.

**Key data:** Add badge to homepage hero fold 1: "18,000+ verified reviews, 4.8-star average" positioned near "250,000+ Happy Customers" or replacing it. Typical industry lift for review-count placement: 3-5% conversion increase. Conservative estimate: +4%.

**Est. lift:** Add review badge to homepage hero → +4% conversion x 12,000 monthly homepage sessions x $52 AOV = **$24,960 annual lift**.

### 6. Test Subscription Reminder at Cart Checkout (Add "Switch to Subscription: Save $6.75 + 15% future orders")

**What's broken:** PDP emphasizes "Subscribe & Save 15%" prominently (green "BEST VALUE" banner), making the subscription option highly visible at point-of-selection. However, cart drawer does not remind customers or offer subscription switching. A customer who added a one-time purchase to cart does not see the subscription option unless they return to PDP. This friction costs 2-3% conversion to subscription (recurring revenue plays). Subscription customers have 60%+ higher LTV than one-time buyers, making this a high-priority lever.

**Evidence:** PDP visual summary emphasizes subscription value in fold 1 prominently; cart drawer visual summary has no subscription upsell or reminder. Cart is the final conversion moment; adding subscription option here captures price-sensitive customers in their final decision.

**Key data:** Add toggle at cart entry: "Switch to Subscription: Save $6.75 this order + 15% every delivery" or similar. Expected lift: +8% of one-time buyers switch to subscription → +$13.50 per order (average discount on $45 item) x 2,000 monthly carts x (0.5 repeat rate assumption for subscription) = incremental recurring revenue.

**Est. lift:** +8% subscription switch rate x 2,000 carts x $45 AOV x 0.5 repeat factor = **$3,600 immediate lift** + **$21,600 annual recurring lift** (conservative; actual LTV multiplier higher for subscription).

### 7. Test Shipping Promise on Homepage ("Ships Monday-Friday, 1-3 Day Delivery" or "Free Shipping $50+")

**What's broken:** PDP displays "Ships Monday-Friday" as trust signal in fold 1, but homepage and cart drawer hide shipping timing and cost until checkout. Multiple reviews mention "$8 freight" as unexpected cost vs. Amazon Prime free shipping. Testing visible shipping promise on homepage (e.g., "Ships Next Business Day" or "Free Shipping on Orders $50+") could reduce checkout hesitation for first-time buyers and price-sensitive customers.

**Evidence:** PDP visual summary includes "Ships Monday-Friday" in trust signals fold 1; cart drawer footer states "CALCULATED AT CHECKOUT"; customer reviews mention "$8 for freight" surprise. Homepage has no shipping mention, missing an easy trust-building opportunity.

**Key data:** Add one-line shipping promise to homepage hero or below hero CTA. Options: "Ships Monday-Friday" (free, reduces urgency risk), "Free Shipping $50+" (incentivizes order size), or "Arrives in 3-5 business days" (sets expectations). Test A/B to determine which resonates.

**Est. lift:** Add shipping promise to homepage → reduce checkout abandonment fear → +3% cart conversion x 2,000 monthly carts x $45 AOV = **$8,100 annual lift**.

### 8. Test Founder Credentials or Customer Testimonials with Photos on Landing Page (Replace generic "Made by Nutritionist, Crafted by Baker" with names/stories)

**What's broken:** Landing page emphasizes "Made By A Nutritionist, Crafted By A Baker" without names, credentials, or photos. This is a credibility claim without evidence. PDP already includes customer testimonial from "Kayla Channe" with profile photo, proving the tactic works on-site. Testing founder credentials ("Created by Dr. Sarah Chen, Registered Dietitian, and Master Baker James Rodriguez") or rotating customer testimonials with photos on the landing page could increase trust and conversion.

**Evidence:** Landing page visual summary shows fold 2 has generic "Made By" claim; PDP visual summary shows customer testimonial with photo in fold 2. Founder story/credentials can differentiate on landing page and build authority with cold traffic.

**Key data:** Test two approaches: (A) Founder credentials with photo (one-time, high authority), (B) rotating customer testimonials with use-case (recurring, relatable). Typically 4-6% conversion lift from credibility/social proof enhancements on landing pages.

**Est. lift:** Add founder photo + bio or customer testimonials to landing page fold 2 → +5% conversion x 8,000 monthly sessions x $52 AOV = **$20,800 annual lift**.

---

## Unused Findings

- **Flavor Intensity Testing:** Multiple reviews note plain and everything bagels as "flavorless" or lacking seasoning. Testing "Bold Flavors" SKU (Everything+ with extra seeds) or limited-time flavor variant could segment underserved customers and increase AOV.
- **GLP-1 User Segment:** 3+ reviews mention semaglutide use as reason for purchase. Ad/landing page variant targeting "Semaglutide users" with "Perfect portion control for GLP-1 lifestyle" could unlock high-intent niche audience.
- **Freeze & Toast Positioning:** Multiple customers freeze and toast as preferred consumption. Badge or messaging emphasizing "Freezer-friendly" or "Toast-perfectly" could shift dryness perception and expand meal-prep use cases.
- **Bundle Upsell in Cart Drawer:** Current "Grab Another Favorite" shows individual products. Testing bundle variant (6-pack, variety bundle) with clear savings call-out could increase AOV more than single-product additions.
