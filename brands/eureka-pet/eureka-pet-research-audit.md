# Eureka Pet CRO Research Audit

## Data Sources Used

- Meta Ads visual summary (3 ads, 9 landing page folds) — collected 2026-06-15
- Meta Ads landing page URLs (live-fetched 2026-06-15)
- Google Ads visual summary (3 screenshots) — collected 2026-06-15
- Customer Reviews — Trustpilot (collected 2026-06-15, truncated at 50k characters)
- PageSpeed / Core Web Vitals — Lighthouse 13.2.0, mobile simulation (2026-06-15)
- Site visual summary (homepage, collection, PDP, cart) — collected 2026-06-15
- Live site fetch — eurekapet.co (fetched 2026-06-15)
- Competitor research — self-researched 2026-06-15 (no user-provided competitor data)

---

## Source Findings

### Meta Ads & Landing Pages

Three campaigns running simultaneously with distinct acquisition angles.

**Ad 1 — Education funnel (kibble attack → why-air-dried page)**
Landing page: eurekapet.co/pages/why-air-dried
Ad copy attacks supermarket kibble: "Meat meal. Cereal fillers. Ingredients listed by weight to hide how little of the good stuff is actually in there." Landing page answers with headline "No Fillers, Fridge or Guesswork" and a three-column comparison table (Kibble vs Air-Dried vs Raw). Dual CTAs on page: "Try a Sample - $6" (filled, warm orange) and "Shop the Recipes" (outline). Social proof bar: ★★★★★ 4.8 | 6,000+ Happy Dogs.
Message match: Strong. Educational page is appropriate for cold/ToF traffic. CTA from ad ("Learn more") correctly leads to content, not a direct product.
Gap: Why-air-dried page claims "6,000+ Happy Dogs" but live site fetch shows "15,000+ satisfied customers." Count inconsistency is a minor credibility signal to audit.

**Ad 2 — Variety pack deal**
Landing page: eurekapet.co/products/variety-pack?selling_plan=703440847132
Ad copy: "For a limited time only save $77 and give your best mate 3 x different Eureka Recipes." Landing page shows subscription price $305.15 with "SAVE $53.85" badge (vs one-time $359.00). Welcome pack value adds $54.79 of extras (Gut Helper $32.90 + Goat Horn $11.90 + Eureka Scoop $9.99).
Message match: Partial. The "$77 savings" in the ad does not match "$53.85" shown on the landing page — a $23 gap on a $359 product. "Limited time only" urgency from the ad has no corresponding scarcity signal on the page.

**Ad 3 — $6 sample funnel**
Landing page: eurekapet.co/products/natural-dog-food-sample
Ad copy: "We're giving out samples of our three droolworthy recipes for just $6 - incl. delivery Australia wide!" Landing page: Taste Tester, $6.00, fussy-dog positioning, 335 reviews (★★★★★ 4.9).
Message match: Strong. Price, delivery promise, and fussy-dog angle all carry through. "Limited time only" from ad has no urgency on page — minor gap at $6 price point. This PDP has 335 reviews vs 75 on the variety pack, making it the highest-volume acquisition funnel.

---

### Google Ads

Google deploys a materially wider angle set than Meta:
- Sample funnel: "Try A Sample Today" / "Taste Tester Sample"
- Health outcomes: "All Natural, Nutrient Dense - Smaller Poos, Better Guts" / "Your dog's health transformation"
- Recipe-specific: "Grass Fed Lamb & Kangaroo | Air-Dried Dog Food"
- Educational: "Dog Food Calculator | Dog Feeding Guide Calculator" / "Ingredients to Avoid in Dog Food"
- Third-party validation: petfoodreviews.com.au 9.5/10 cited in ad copy; Shopping cards show 4.9★
- Offers: $6 Taste Tester, 15% subscription, 17% off Starter Pack sitelink

Shopping ads use yellow branded packaging with star ratings visible in cards. Display ads use lifestyle imagery — woman in yellow top matching brand palette.

Gap vs Meta: Health outcome language ("smaller poos, better guts") and petfoodreviews.com.au 9.5/10 validation — both tested in Google — are absent from Meta landing pages and the main site. These are proven-in-market proof points not yet deployed on the highest-traffic surfaces.

---

### Reviews & UGC

Source: Trustpilot, collected 2026-06-15. Feed truncated at 50,000 characters — additional reviews beyond this sample may exist.

#### What Customers Love

- **Palatability for fussy dogs** — the most-cited positive theme. "My super fussy staffy cross border collie who is not food motivated at all is OBSESSED." "Fussy little poodleX loved them." "My very fussy Schoodle absolutely loved them!" Multiple reviewers bought the $6 sample specifically to test palatability first.
- **Visible health outcomes** — coat, energy, gut health, weight control. "Her coat is looking shinier." "She is sleeping better, actually starting to play again and more energy." "His weight is reducing and his overall health is improving."
- **No crumbs** — one reviewer explicitly named this as a standout vs. other dry food: "there are no crumbs whatsoever at the bottom of the bag. Nothing wasted, nothing to throw out."
- **Australian made and owned** — a recurring purchase driver. "Trusted Australian company." "Love knowing that I'm supporting an Australian business."
- **Customer service** — prompt responses, solution-oriented. "Always a prompt response to any query." Multiple 5-star reviews attribute loyalty specifically to CX responsiveness.
- **Subscription flexibility** — ease of pausing, fast-tracking, or delaying. "So easy to fast-track or delay when needed." "Pause, change or cancel anytime."

#### What Frustrates Customers

- **Price** — the single most-cited friction point. "It's expensive and especially if you are feeding a larger dog." "Beyond my budget." "For a Rottweiler X Great Dane at $300+ for about 5kgs — TOTALLY unaffordable." "The same bag is now priced at $126" (customer didn't understand the $30 welcome discount was one-time).
- **Delivery failures** — two recurring issues: Aramex misdeliveries in rural areas ("Please just send my subscription to the post office") and one order not received two months after purchase.
- **Subscription enrollment confusion** — one customer claims "I did NOT order more" and reports unauthorized billing after sample purchase. Another couldn't log in to amend a scheduled order (email code not arriving in inbox).
- **No phone support / buried contact page** — "There is no phone number to contact anyone." "It was extremely difficult to find out HOW to actually contact them — no Contact Us easily available on the website."
- **Generic welcome treats for small dogs** — goat horn sent to a very small breed owner: "She could not even begin to enjoy such a rock hard large item." Croissant treat also flagged as unsuitable for small dogs.

#### Client-Actionable Insights

- **Aramex** is generating recurring 1-star reviews from rural customers. Reviewing carrier allocation by delivery zone or offering Australia Post as a selectable option for regional addresses would reduce avoidable churn.
- **Subscription opt-in confirmation** needs strengthening. At least two reviewers indicate they didn't understand they had started a subscription — one after a sample purchase, one after a variety pack order. A dedicated subscription confirmation screen or prominent email at enrollment would reduce disputed charge complaints.
- **Contact Us** is not in the main navigation. This surfaces as a service complaint from multiple reviewers. Adding a Help or Contact link to the main nav is a product fix.
- **Welcome treat sizing** — customers with small or toy breeds feel excluded by the default welcome gift. A pet size prompt at checkout or during subscription setup would allow size-appropriate treat selection.
- **Welcome discount communication** — the $30 first-order discount is not labeled as one-time at checkout. Adding "Your first order includes a $30 welcome discount" in the order confirmation and at checkout would prevent price-shock on renewal.

---

### PageSpeed / Core Web Vitals

Source: Lighthouse 13.2.0, mobile simulation, collected 2026-06-15.

| Page | Score | FCP | LCP | TBT | CLS | TTI | Speed Index |
|---|---|---|---|---|---|---|---|
| Homepage | 46/100 | 3.1s | 9.9s | 550ms | 0 | 35.7s | 17.9s |
| PDP (Taste Tester) | 33/100 | 3.7s | 7.7s | 1,450ms | 0.017 | 40.7s | 33.6s |

Both pages fail Core Web Vitals on mobile. The PDP score of 33/100 with TTI 40.7s is extreme — a visitor arriving from a Meta or Google mobile ad will wait over 40 seconds before the page is interactive. The PDP's Total Blocking Time of 1,450ms points to heavy JavaScript from third-party apps (subscription widget, review widget, analytics, sticky bar) blocking the main thread. With the $6 sample funnel driving the most traffic, PDP performance degradation directly suppresses acquisition volume. Desktop scores were not available from collected data.

---

### Competitor Analysis

Research date: 2026-06-15. No user-provided competitor data was available — all findings are self-researched.

| Brand | Format | Price (approx.) | Key strength | Key weakness |
|---|---|---|---|---|
| **Eureka Pet** | Air-dried | From $74.37/1.8kg (~$41/kg) | $6 sample entry, 3 protein recipes, Australian made, 4.8★ Trustpilot | PDP performance (33/100), thin cart AOV optimization |
| **Ziwi Peak** | Air-dried | ~$40–60/kg | Wide retail distribution (physical stores), NZ quality positioning, recipe range | Not Australian, DTC subscription play weaker |
| **Frontier Pets** | Freeze-dried | ~$56/kg (2.5kg) | "Raw equivalent" positioning, 10% subscription discount | Higher per-kg visual price, lower brand awareness vs Eureka |
| **Scratch Pet Food** | Fresh delivered | Lower per-kg | Subscription-native, Australian, transparent ingredients | Different format (not air-dried), lower protein density |

Ziwi Peak's physical retail presence (pet specialty stores, vets) gives it a touchpoint advantage Eureka cannot replicate DTC. Eureka's $6 Taste Tester sample is a strong DTC differentiator — no main competitor appears to offer an equivalent low-barrier entry product. petfoodreviews.com.au rates Eureka 9.5/10, which is already used in Google Ad copy but not on the website itself.

---

### Current Site Screenshots

**Homepage:**
The hero is a two-column layout — left column carries headline "All natural Aussie made air dried dog food" with subtext about 90% Aussie protein, followed by a single outline (unfilled) CTA button labeled "Discover More." Right column is a lifestyle photo of a grey/white dog on a couch with a yellow Eureka bag. No product imagery, no price, and no subscription offer appear in this column or above the fold. The announcement bar offers "Buy 4 Get 15% Off Natural Treats" — not the primary acquisition offer.

Folds 2 and 3 continue brand storytelling: farm origin story ("starting from the seed of an idea on our family farm in Eureka, NSW"), "A high protein, low carb ancestral diet" section, and a "Our Mission" manifesto block. No product grid or shop entry point exists within the first three folds. For intent-based traffic from Google, this creates a high-friction discovery path.

**Collection:**
Three-column product grid with 47 products. Left sidebar offers useful filters: Protein Source (Beef, Chicken, Fish, Goat, Kangaroo, Lamb, Venison) and Health Benefits (Digestive Care, Joint Health, Low Fat, Single Protein, Skin Coat Health). A sold-out product (Cognitive + Vitality Functional Treat) appears in the first row with no price displayed — visual confusion at first impression. No quick-add to cart on any card; all products require click-through to add. Subscribe & Save 15% announcement bar is persistent. Review counts are strong on lead products: Wild Venison 1,236 reviews, Wild Kangaroo 977 reviews, Taste Tester 335 reviews.

**PDP (Taste Tester — primary):**
Well-structured for a low-friction $6 purchase. Above-fold buy box includes: product title, ★★★★★ 4.9 (335 reviews, linked in orange), fussy-dog copy, $6.00 price, qty selector, and a black full-width "Add to cart" button. Four trust icons (Australian Made / Money Back Guarantee / 68°C / No Fillers) sit below the button, not between price and CTA. A persistent sticky add-to-cart bar at page bottom reinforces the CTA on scroll. Critical gap: no subscription widget on this PDP despite "Subscribe & Save 15%" running persistently in the announcement bar. A sample buyer cannot convert to subscription from this page.

**Cart (slide-out drawer):**
Single cross-sell ("I'm even better with — Cluckin Good Chews $18.95") in a carousel with no context for the recommendation. A discount code field sits below. No free-shipping progress bar (threshold is $59, visible elsewhere on site — a $6 sample order sits $53 below with no indicator). No subscription upsell. No bundle mechanic. No frequently-bought-together. Checkout CTA at bottom: "Checkout • $6.00." Cart is nearly empty of AOV optimization.

---

## Cross-Source Themes

**1. Price sensitivity is the primary conversion barrier** (evidence strength: high — reviews, review star data, competitor pricing research)
Dominant theme across Trustpilot reviews at multiple star levels. Large breed owners are most vocal: unworkable cost at $300+ for 5kg. Multi-dog and fixed-income households explicitly cite price as the reason they won't repeat-purchase despite loving the product. The welcome discount misunderstanding compounds perception of price increase at renewal. No on-site mechanism directly addresses price anxiety for high-cost segments.

**2. The $6 sample funnel is the strongest acquisition asset but is under-optimized post-click** (evidence strength: high — review volume delta, site visual summary, cart analysis)
335 reviews on the Taste Tester PDP vs 75 on the variety pack signals where new customer volume concentrates. Yet the page has no subscription widget, and the cart following a sample add has one cross-sell, no free-shipping bar, and no subscription upsell. The funnel driving the most new customers drops them at checkout with minimal LTV infrastructure.

**3. Homepage prioritizes brand story over purchase intent, misaligned with paid traffic** (evidence strength: medium — site visual summary, Google Ads angle analysis, live site fetch)
Three folds of brand origin and mission before any product, price, or shop entry point. Sole above-fold CTA is "Discover More" (outline, low visual weight). Google sends intent-heavy search traffic here. Meta's Ad 1 landing page (why-air-dried) has a dual-CTA hero with star ratings — the homepage does not.

---

## Top Test Opportunities

**1. Homepage hero — primary CTA swap** — The only above-fold CTA is "Discover More" (outline, no price, no product). For paid traffic with product or purchase intent, this offers no clear path to buy. Evidence: site visual summary (homepage fold 1), live site fetch, Google Ads (intent-based keywords landing on homepage), meta-ads-visual-summary (Ad 1 landing page has filled "Try a Sample - $6" CTA in same hero position). Est. lift: conservative 10–15% improvement in homepage CTR to product × [sessions/mo unknown] × $80 blended AOV.

**2. Cart — free-shipping bar + subscription upsell module** — Cart has one static cross-sell, no free-shipping indicator ($59 threshold — $53 above a $6 sample order), and no subscribe & save module. Evidence: site visual summary (cart), reviews (subscription flexibility praised by 5+ reviewers, validating subscribe-and-save appeal), live site data ($59 free shipping threshold). Est. lift: 10–20% AOV increase on cart orders (industry benchmark for free-shipping bar implementations).

**3. Taste Tester PDP — add subscribe & save option** — The primary sample acquisition page has no subscription widget despite a persistent "Subscribe & Save 15%" announcement bar at page top. The Variety Pack PDP has a subscribe/one-time toggle — the tech exists. Evidence: site visual summary (PDP fold 1 and layout notes), meta-ads-visual-summary (Ad 3 sends highest-volume sample traffic here), variety pack PDP confirms subscription widget is available. Est. lift: 3–5% of Taste Tester buyers converting to subscription represents outsized LTV vs. a one-time $6 transaction.

**4. Ad 2 — savings claim alignment** — Meta Ad 2 claims "save $77." Variety Pack landing page shows "SAVE $53.85." $23 discrepancy on a $359 product. Evidence: meta-ads-visual-summary (Ad 2, message match: partial), live fetch of variety-pack page (subscription $305.15 / one-time $359.00). Est. lift: 5–10% conversion improvement on variety pack PDP by removing trust friction at the point of highest transaction value.

**5. Taste Tester PDP — move trust icons above the buy button** — The four trust icons (Australian Made / Money Back Guarantee / 68°C / No Fillers) appear below "Add to cart," not between price and CTA. Reassurance signals are positioned after the decision point. Evidence: site visual summary (PDP fold 1), reviews citing Australian provenance and money-back guarantee as explicit purchase drivers. Est. lift: 3–8% PDP conversion improvement (per CRO placement benchmarks).

---

## Unused but Valuable Findings

- "Smaller Poos, Better Guts" health-outcome language used in Google Ads is absent from every landing page and the main site — a tested headline proven in-market that hasn't been applied to on-site copy.
- petfoodreviews.com.au 9.5/10 rating is cited in Google Ad copy but does not appear on the website or any Meta landing page.
- Carbon-neutral claim (NOCO2 partnership) appears on the live homepage but has not been used in any ad creative reviewed — an untested differentiator for an eco-conscious segment.
- Large breed pricing gap: multiple 1-3 star reviews cite structural unaffordability for large dogs (Rottweiler X Great Dane at $300+ for 5kg). No bundle, per-day pricing frame, or topper-use positioning exists on site to address this segment.

---

## Missing Data

No MISSING_DATA warnings in the manifest. Review feed was truncated at 50,000 characters — additional patterns may exist beyond the sample reviewed, though core themes across price, palatability, delivery, and service are well-represented in the collected data.
