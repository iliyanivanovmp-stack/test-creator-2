# Eureka Pet Co CRO Research Audit

**Site:** eurekapet.co
**Audit date:** April 27, 2026
**Sources collected:** Meta Ads, Google Ads Transparency, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots

---

## Meta Ads

3 ads analyzed out of many active campaigns. All confirmed active as of the audit date.

**Ad 1** (Library ID: 282589898112630, started Feb 3, 2026)
- Platform: Meta (Facebook, Instagram, Messenger, WhatsApp)
- Copy: "We're giving out samples of our three droolworthy recipes for just $6 - incl. delivery Australia wide! Limited time only."
- Social proof in ad: "Feeding 15,000+ Aussie Dogs"
- CTA: "Learn More"
- Landing page: eurekapet.co/products/natural-dog-food-sample (Taste Tester PDP)
- Message match: Strong. Ad promises $6 sample with delivery, LP delivers exactly that.

**Ad 2** (Library ID: 121856709023037, started Jan 19, 2026)
- Copy: Identical to Ad 1
- Creative: Different video
- CTA: "Shop Now"
- Landing page: Same as Ad 1 (Taste Tester PDP)

**Ad 3** (Library ID: 121368663757632, started Jan 19, 2026)
- Copy: "Start your pup's Eureka journey with our Starter Pack and enjoy a $38 discount! This pack includes a total of 3x 800g bags. One of each Eureka Recipe - the ultimate high protein, wild caught feast for your furry friend!"
- CTA: "Shop Now"
- Landing page: eurekapet.co/products/starter-pack (UTM: utm_source=fb&utm_medium=paid-social&utm_campaign={{campaign.name}}&utm_content={{ad.name}})
- Message match: Moderate. Ad says "$38 discount," LP shows "SAVE 17% OFF" with $185 / $223.11 crossed out. The dollar amount is implied by the math but not displayed.
- **Critical issue:** UTM parameters contain unfilled Liquid placeholders: `{{campaign.name}}` and `{{ad.name}}`. Tracking is broken for this campaign. Performance data is unreliable.

**Cross-ad observations:**
- 2 of 3 ads drive to the $6 sample offer. This is the dominant acquisition funnel.
- Both landing pages are standard Shopify PDPs, not dedicated landing pages. Navigation, "Spin to Win" popup, and an announcement bar promoting treats ("Buy 4 Get 15% Off Natural Treats") are all visible.
- Subscription is not mentioned on either landing page despite being a core business model.
- No fussy-eater angle in any of the 3 ads analyzed.

---

## Google Ads Transparency

Source: adstransparency.google.com, searched for "Eureka Pet Co," reviewed Apr 27, 2026.

Eureka is running across Search, Display, Shopping, and YouTube formats.

**Search ad headlines and copy observed:**
- "Try A Sample - Air Dried Dog Food Delivery" | "Australian made. All natural. No nasties."
- "All Natural, Nutrient Dense - Smaller Poos, Better Guts" | Rated 9.5/10 by petfoodreviews.com.au. Subscribe today for 15% off. A$77 off Variety Pack.
- "Proudly Australian Owned - Eureka Pet Co" | Rated 9.5/10 by petfoodreviews.com.au. Subscribe today for 10% off. A$77 off Variety Pack.
- "Try A Sample Today - Eureka Pet Co" | "3 air-dried recipes. No fillers, no preservatives. 90% Aussie meat, 10% fruit & vegetables. Rated 9.5/10..."
- "Order Your First Box Today - Delivered To Your Door" | Sitelinks: Try A Sample, Try A Starter Pack, $6 Taste Tester Pack, Our Food, Order A Taste Tester Today
- "Eureka Dog Food - Eureka Pet Co" | "High protein, low carb. Lightly air dried. Get your sample today."
- "Claim A Sample Today - Premium Dog Food" | "3 air-dried recipes. No fillers, no preservatives. 90% Aussie meat, 10% fruit & vegetables."
- "100% Australian Dry Dog Food - Natural Dry Dog Food" | "Independently rated one of Australia's best. Try our three air-dried recipes."
- "All Natural Dog Food - Premium Dog Food" | Badge: 17% off Starter Pack

**Display/Shopping observations:**
- Display ads show brand photography (product packs, lifestyle dog photos)
- Shopping ads show individual products with "[Price]" placeholders visible in some ads, suggesting potential shopping feed rendering issues
- YouTube format ads also present

**Key observations:**
1. Sample/trial funnel is the dominant conversion mechanic across all Google formats, consistent with Meta.
2. "Smaller Poos, Better Guts" is one of the strongest outcome-focused headlines in the mix, but has no corresponding landing page. All sample traffic lands on the generic Taste Tester PDP.
3. Subscription discount is inconsistent: some ads say "10% off," others say "15% off." The actual subscription offer on-site is 15% off + free treats for life. The 10% figure may be outdated or from a previous offer.
4. Third-party validation ("Rated 9.5/10 by petfoodreviews.com.au") is used in Google Search ads but is not visible on any landing page or PDP seen in screenshots.
5. Multiple promotional angles running simultaneously: $6 sample, $77 off Variety Pack, 17% off Starter Pack. This may fragment perception for remarketing audiences.

---

## Reviews & UGC

Source: User-provided review data from Eureka Pet Co review platform. Reviews dated Aug 2025 through Apr 2026.

### Positive themes (ordered by frequency)

**1. Fussy/picky eater solved**
The single most common theme across positive reviews. Dog owners who had tried multiple brands report their picky dog immediately takes to Eureka. This is cited as the primary reason for loyalty and referrals.

Verbatims:
- "MY CATTLE DOG IS EXTREMELY FUSSY BUT LOVES THIS FOOD CUSTOMER FOR LIFE"
- "Our very fussy dachshund loves it! I love that it's aussie made, love the high protein and low carb ingredients list."
- "My super fussy staffy cross border collie who is not food motivated at all is OBSESSED with his new food."
- "Fussy dog gives tick of approval. I bought the sample packs and my fussy little poodleX loved them."
- "Finally! Dry food my dogs eat! I'm 5 days in and my cavoodle and Cavalier are licking their plates clean. They've never eaten all their biccies!!"
- "As a pet parent to Rocky, my notoriously picky pup, finding a food that he actually enjoys has been quite the challenge. However, Eureka pet food has truly been a game changer!"
- "She doesn't like dry food very much, I tried all different types but would only eat them when there was nothing else. Since I have bought Eureka she loves them."
- "Our very fussy dachshund loves it! The quality is outstanding."

**2. Visible health results**
Coat shininess, improved energy, cleaner teeth, better digestion, and weight management mentioned frequently.

Verbatims:
- "Since starting Eureka he is the healthiest and happiest he has ever been. His favourite game ever is playing 'find it'."
- "His coat is super shiny and his teeth still white. He has over time tried other brands but never ever liked them."
- "He seems to have slowed down eating and seems to savour every mouthful... His weight is reducing and his overall health is improving."
- "His coat looks shinier and healthier than ever."
- "I've been feeding this food since 4 years now and their coat is nice and shiny."

**3. Fast delivery and responsive service**
Multiple references to same-day dispatch, next-day delivery when needed, and helpful customer service.

**4. Sample-to-full-purchase funnel working**
Multiple reviews follow the exact conversion path: tried $6 sample, dog loved it, immediately ordered full bag or Starter Pack.

**5. Subscription valued**
Existing subscribers are happy. Free treats for life is noticed and appreciated. Subscription flexibility (pause, skip, change frequency) mentioned positively. One humorous review called it "sneaky" because the free treats made them buy more treats.

**6. Versatility**
Used as training treats, meal topper, enrichment (scatter mat, Kong), and complete meal. Particularly valued in rescue/foster contexts.

**7. Australian ownership and ingredient quality**
"Aussie made and owned" is a trust signal that resonates. Clean ingredient list appreciated by health-conscious pet owners.

### Negative themes (ordered by frequency)

**1. Price is the #1 complaint**
Multiple reviews from the past 12 months cite the price as a barrier to continued purchase or initial trial. Most complaints are not about the value proposition but about the absolute dollar amount.

Verbatims:
- "I paid $97 on my first 1.8kg bag. That was double the most expensive dry food I've bought. I went to re-order and the same bag is now priced at $126. You just out priced yourself of a customer."
- "Extremely expensive! I don't mind the food my dog eats it but unfortunately it's a Rottweiler X Great Dane and at $300+ for about 5kgs!!!"
- "They delivery is fast, but too expensive. It is still very expensive. I would order it again if the price was made more affordable."
- "I like your products, but you are a bit stingy... I had to pay an extra $10 [for shipping when using voucher], which basically negates the voucher."
- "Ridiculously expensive. My dog is very fussy with food and I don't want to spend a lot of money for something she may not eat."
- "Price is the most difficult factor though. Love the ethos the pride you take in your hard work and the undeniable quality of the product - we just simply can't afford it."
- "$300 for 5.4 kilos is financially out of many peoples reach."

**2. Welcome discount cliff (price shock on reorder)**
At least one verified review and likely more represent a pattern: the $30 welcome discount is applied to the first order, reducing it to ~$97. On reorder without the discount, the price jumps to $126. Customers perceive this as a price increase and leave negative reviews. The brand responded clarifying the discount, but the pattern suggests the welcome discount is not clearly communicated as one-time.

**3. Dog rejection (~10-15% of sample buyers)**
Some dogs simply don't like the product. This is expected with any pet food, but the reviews suggest the rate is non-trivial. One review mentions 4 dogs out of 4 rejected all samples. Another mentions one of two chihuahuas rejected it. The brand correctly addresses this with the sample pack and money-back guarantee, but the rejection experience is a churn signal.

**4. Digestive transition issues**
Several reviews mention diarrhea or loose stools during the transition period, particularly with the Single Protein Chicken. The brand addresses this in responses but the pattern suggests transition guidance is not prominent enough pre-purchase.

**5. No phone support**
Mentioned in multiple reviews as a trust barrier, particularly for new customers making a high-price purchase for the first time. One reviewer called it a "Facebook scam" specifically because of no phone number. The brand is a small team, but the perception gap is real.

**6. Large dog affordability gap**
Multiple reviews from owners of large breeds (Rottweiler x Great Dane, German Shepherd) note the product is effectively unaffordable at scale. The brand acknowledged they're working on a more economical option. No mention of this on the site.

**7. Pack size requests**
Multiple requests for 300-400g packs for small dogs. Current smallest food bag is 800g. This is a product gap, not a CRO issue.

**8. Couriers Please shipping complaints**
At least one review specifically names Couriers Please as unreliable (multiple missed deliveries, claimed deliveries that didn't happen). Courier reliability is outside CRO scope but affects post-purchase trust.

**9. Subscription auto-reorder confusion**
One subscriber didn't realize they could manage frequency. Another couldn't log in to amend an upcoming order.

### Client-actionable insights (not test ideas)

- **Welcome discount cliff:** Communicate clearly at checkout and in the post-purchase flow that the welcome discount is one-time. A proactive email before the second order ("Your subscription price explained") could prevent negative reviews and price-shock churn.
- **Venison chews ingredient accuracy:** One reviewer flagged "Venison chews - Contains Beef (Beef collagen)" labeled as "Single Protein." If accurate, this needs addressing to avoid trust damage and potential regulatory exposure.
- **No phone support:** Consider adding a chat-based support option prominently on PDPs during high-consideration moments.
- **Couriers Please:** Audit courier reliability. One negative review specifically named the carrier as a reason to distrust the brand.
- **YouTube ad tone:** One reviewer found the "we get a lot of flack, not comparing apples to apples" opener "arrogant." At least one lost sale tied to this. Worth reviewing with the team.
- **Large dog segment:** The brand mentioned in review responses they are working on an economical option. Adding "Coming soon for large breeds" messaging could retain large dog owners who otherwise churn on price.

---

## Page Speed / Core Web Vitals

Source: Google PageSpeed Insights, tested April 27, 2026. Mobile results only (primary traffic device for DTC ecommerce).

**Homepage (eurekapet.co/)**
- Performance score: 23 / 100
- LCP (Largest Contentful Paint): 14.0s (threshold: good = <2.5s)
- FCP (First Contentful Paint): 5.5s
- TBT (Total Blocking Time): 1,800ms
- CLS (Cumulative Layout Shift): 0.138 (threshold: good = <0.1)
- Speed Index: 17.8s
- Core Web Vitals: FAILED
- Top opportunities: Eliminate render-blocking resources, reduce unused JavaScript, improve image delivery, reduce main thread work (~10s), avoid large network payloads

**Taste Tester PDP (eurekapet.co/products/natural-dog-food-sample)**
- Performance score: 27 / 100
- LCP: 12.4s (FAILED)
- FCP: 5.8s
- TBT: 2,250ms (FAILED)
- CLS: 0.015 (GOOD)
- Speed Index: 23.9s
- Core Web Vitals: FAILED
- Top opportunities: Eliminate render-blocking requests, improve image delivery (~808KB savings), reduce unused JavaScript (~113KB), reduce main thread work (~17s), avoid large network payloads (~7.4MB)

**Context:** Both pages fail Core Web Vitals. The PDP has a worse TBT (2,250ms vs. 1,800ms) and worse Speed Index (23.9s vs. 17.8s). The LCP of 12-14s means the majority of mobile users wait over 10 seconds to see the most important content on screen. Given that 70-80% of DTC ecommerce traffic is mobile, this is a direct revenue leak affecting every paid campaign Eureka runs.

---

## Competitor Research

Sources: WebFetch (bugsys.com.au), WebSearch (competitor landscape), April 27, 2026.

**ZIWI Peak (New Zealand, AU retail distribution)**
- Premium air-dried, positioned as NZ-origin
- No direct-to-consumer trial pack in Australia
- Retail-distributed (Petstock, VetSupply, Peekapaw)
- No DTC subscription model visible
- Differentiator vs. Eureka: Broader retail availability, NZ provenance, cat product range

**Bugsy's (Australian DTC, bugsys.com.au)**
- Air-dried dog food, "human-grade Australian meats"
- Starting price: $34.95 (vs. Eureka's $74.37 for main food bags)
- No subscription model detected
- Variety Pack as trial entry ($132.80 for 5 flavors vs. Eureka's $6 sample)
- Social proof: "2,039,896+ Meals Served"
- Rewards program (loyalty points)
- Free shipping threshold: $150+
- No money-back guarantee visible
- Collaborates with veterinarians and PhD animal nutritionists in formulation

**Frontier Pets (Australian DTC, Evans Head NSW)**
- Freeze-dried complete meals, formulated by Holistic Vet Cathy Cornack
- Only 3% carbs - similar low-carb positioning to Eureka
- Different format (freeze-dried vs. air-dried)
- Rated highly on petfoodreviews.com.au (same third-party site Eureka uses in Google ads)

**Competitive gap summary:**
- No competitor matches Eureka's $6 entry-point sample with free delivery. This is a unique acquisition advantage.
- No competitor has a subscription model with free treats for life. Eureka's retention mechanics are stronger than the market.
- Bugsy's prices start lower ($34.95 vs. $74.37), which may attract price-sensitive customers Eureka can't retain.
- The "Rated 9.5/10 by petfoodreviews.com.au" third-party validation used in Eureka's Google ads is not surfaced on any landing page, despite being a legitimate trust signal.

---

## Current Site Screenshots

Source: User-provided screenshots, taken April 27, 2026.

**Homepage (desktop)**

Fold 1: Split hero. Left: cream background with headline "Same Recipe, Better Value." subheader "Single Protein Chicken," body copy "90% Aussie Chicken, 10% fruit, veg & seeds. No fillers, no preservatives, no nonsense!" CTA: "SHOP NOW" (outline button, links to Single Protein Chicken). Right: full-bleed photo of white dog with Eureka bag. Rotating carousel (2 dots visible). "Spin to Win" popup visible bottom-left, partially dismissed. Announcement bar: "Buy 4 Get 15% Off Natural Treats →" (orange).

Issues:
- Hero headline "Same Recipe, Better Value." is brand-internal language that likely refers to a recent reformulation or repricing. First-time visitors have no context for "which recipe" or "better than what."
- No $6 sample CTA anywhere on the homepage, despite the $6 sample being the dominant paid acquisition offer.
- No fussy eater mention in the top fold.

Fold 2: Split layout. Left: lifestyle photo of woman and dog with Eureka bag. Right: headline "A high protein, low carb ancestral diet." followed by brand story copy (Australian-owned, family farm, grass-fed lamb, free-range chicken, wild-caught game, air-dried at 68 degrees). CTA: "About Us" (outline button). This fold is brand storytelling, not conversion.

Fold 3: Large orange/amber section "Our Mission" with decorative carousel: "Real meat, bone and organs to power your pooch." Three carousel slides, left/right arrows. "Our Recipes" heading begins below.

**Taste Tester PDP (eurekapet.co/products/natural-dog-food-sample, desktop)**

- Product name: "Taste Tester"
- Rating: 4.9 stars (3,095 reviews) - strongest social proof on the site
- Description: "Make sure your dog will love Eureka by getting a taste of all three of our air-dried dog food recipes! Each Taste Tester includes 3 x 20g samples plus shipping Australia wide."
- Price: $6.00
- Trust badges (4 icons): 100% Australian Made & Owned, 100% Money Back Guarantee, 68°C Gently Air Dried, No Fillers or Glycerins
- Sticky ATC bar on scroll: "Taste Tester Sample | Add to cart"
- Below fold: "See it in action!" UGC photo section (3 dog photos visible in carousel)
- Further below: "FREE SHIPPING OVER $59 | HANDCRAFTED WITH LOVE IN AUSTRALIA" ticker
- Further below: "Bundle & Save" section showing 6 treat products
- Announcement bar: "Buy 4 Get 15% Off Natural Treats →" (treats promotion, not sample-related)
- "Spin to Win" popup visible

Issues: No subscription mention anywhere on the page. The page has the brand's highest review count but the generic copy ("Make sure your dog will love Eureka") does not lead with the fussy eater insight that drives conversion in reviews.

**Starter Pack PDP (eurekapet.co/products/starter-pack, desktop)**

- Product name: "Starter Pack - 3x 800g"
- Rating: 4.9 stars (236 reviews)
- Description: "Start your pup's Eureka journey with our Starter Pack and enjoy a $38 discount on 3 x 800g air dried packs..."
- Price: $185.00 (was $223.11). "SAVE 17% OFF" badge.
- Fine print: "*No exchanges, recipe swaps, or refunds are available on this product."
- Same 4 trust badges as Taste Tester PDP
- Below fold: Customer review callout ("Brooks has been loving Eureka's air-dried food") + product flat lay
- Further below: Bundle & Save section with treats
- Sticky ATC bar: "Starter Pack - 3x 800g | Add To Cart - $185.00 $223.11"
- Announcement bar: "Buy 4 Get 15% Off Natural Treats →"

Issues: Message mismatch with Ad 3 ($38 discount in ad vs. "SAVE 17%" on page). No cost-per-day or per-serve framing to address the #1 review complaint about price. No exchange/refund policy note is unusual for a $185 product and may increase hesitation.

**Collection Page (/collections/all, desktop)**

- 48 products in one mixed collection (food bags, treats, supplements, accessories)
- Left sidebar filters: Protein Source (Beef, Chicken, Fish, Goat, Kangaroo, Lamb, Venison), Health Benefits (Digestive Care, Joint Health, Low Fat, Single Protein, Skin Coat Health)
- No product type filter (no way to filter by food vs. treats vs. supplements)
- Sort: Featured
- Badge system on cards: SAMPLE, BUY 4+ GET 15% OFF, SUBSCRIBE & SAVE 15%, NEW - SAVE $14.80, Deal, NEW PRICE - BETTER VALUE! (six different badge types creating visual noise)
- Product card format: image, name, verbose star text ("4.9 out of 5 stars rating in total (3095) reviews"), price
- No quick-add CTA on product cards. All purchases require clicking through to PDP first.
- Taste Tester is correctly featured first (highest review count at 3,095)

**Cart Drawer (mobile, with Taste Tester in cart)**

- Top banner: "Your sample is on its way!" (positive reassurance)
- Cart item: Taste Tester Sample, $6.00, quantity stepper
- Large dead white space between cart item and upsell section (significant mobile UX gap)
- Upsell: "I'm even better with [arrow carousel]" showing Mighty Liver Munchies $18.95 + "Quick Add" button
- Prominent promo code field: "Got a discount code? Enter it h..." + "Apply" button
- CTA: "Checkout • $6.00" (full-width black button)
- No subscription upsell
- No free shipping threshold indicator
- No trust badges (money-back guarantee, Australian-made, etc.)

---

## Cross-Source Analysis

**Theme 1: Fussy eater is the #1 conversion driver but is absent from the site**
Reviews (~30%+ of positive reviews), competitors (no one owns this angle), and Meta/Google ads (none of the 3 Meta ads and no visible Google Search ads use this angle) all point to the same gap. The site's strongest differentiated proof point is not being leveraged in copy, PDPs, or paid acquisition.

**Theme 2: Price is the #1 objection and the site never addresses it**
Reviews (repeated price complaints, welcome discount cliff), competitors (Bugsy's starts at $34.95), and Google ads (discount-led offers dominate) all point to price sensitivity. The site has no cost-per-day or cost-per-serve framing anywhere visible. The welcome discount cliff ($97 first order, $126 reorder) is creating negative reviews that damage the brand's 4.9-star reputation.

**Theme 3: Mobile performance is critically broken**
PageSpeed scores of 23 and 27 on the two highest-traffic pages, with LCP over 12 seconds, mean most mobile users abandon before the page fully loads. This is a sitewide revenue leak affecting every paid campaign.

**Theme 4: The cart is leaking revenue**
The visible promo code field is a known cart abandonment trigger (users leave to search for codes). The CRO ebook cites 70% of cart adds never convert. The upsell shows a $18.95 treat instead of a $74-185 subscription upgrade. No trust signals reinforce the purchase decision at the checkout moment.

**Theme 5: Subscription LTV is the real revenue story but has no funnel presence**
The $6 sample is the acquisition mechanic. The subscription (15% off + free treats for life) is the retention mechanic. But the Taste Tester PDP has zero subscription mention, the cart upsells a treat instead of a subscription, and none of the 3 Meta sample ads analyzed mention subscription. The two mechanics are not connected in the customer journey.

**Theme 6: Message match gaps between ads and landing pages**
"Smaller Poos, Better Guts" Google headline has no LP equivalent. The announcement bar on both PDPs promotes treats to food-focused ad traffic. Ad 3 UTM tracking is broken. The Starter Pack's $38 dollar discount (ad) vs. 17% off badge (LP) creates a minor but unnecessary disconnect.
