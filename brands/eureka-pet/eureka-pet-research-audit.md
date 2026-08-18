# Eureka CRO Research Audit

## Data Sources Used

- User-provided collection manifest: `brands/eureka-pet/manifest.md`
- Meta Ads and landing page screenshots: `raw/meta-ads.md`, `raw/meta-ads-visual-summary.md`
- Live landing page text fetched during audit: `https://eurekapet.co/products/starter-pack?selling_plan=703440912668`, `https://eurekapet.co/products/natural-dog-food-sample`
- Google Ads Transparency screenshots: `raw/google-ads-visual-summary.md`
- Reviews and UGC: Trustpilot reviews collected 2026-06-15 in `raw/reviews.md`
- PageSpeed / Core Web Vitals: Lighthouse JSON collected 2026-08-18 in `raw/pagespeed.md`, `raw/eurekapet-pagespeed-homepage.json`, `raw/pdp-pagespeed-eureka.json`
- Non-data context: `raw/context.md`
- Current site screenshots and live homepage text: `raw/site-visual-summary.md`, `https://eurekapet.co/`
- Self-researched competitor sources, researched 2026-08-18: ZIWI official site, Frontier Pets official site, Lyka official site/help centre, Pet Food Reviews Australia, 99PetShops, The Australian/Herald Sun snippets from web search

## Source Findings

### Meta Ads & Landing Pages

Ad 1 uses a trainer-led angle: "What food do you use in your training?" The destination is the Starter Pack PDP, not a training-specific landing page. The first fold has a conventional product-gallery-left and buy-box-right PDP with title "Starter Pack - 3x 800g," 4.9 rating with 303 reviews, recipe selector, frequency selector, autoship panel, quantity selector, and black "Add to cart" CTA. Live page text reinforces the starter journey, a 15% discount, 3 x 800g bags, over 90% meat/organs/bone, no fillers, Australian ingredients, transition guidance, and free shipping over $59. The message-match gap is that the ad creates a training/treat-use frame, while the page asks shoppers to choose recipe and subscription mechanics before it visibly explains training use cases.

Ad 2 is tighter. The ad states that 86% of customers say their dog's health improved after switching and shows a $19.99 sample offer. The Taste Tester PDP first fold carries the same $19.99 sample, 4.9 rating with 3707 reviews, one 20g sample of each of seven recipes, free delivery, $20 subscription credit, quantity selector, and black "Add to cart" CTA. Live page text confirms free delivery Australia-wide and the $20 credit. The landing page matches price and sampling, but the health-improvement proof behind the 86% claim is not visible in the collected first three folds.

Ad 3 uses the strongest problem-solution hook: "Say Bye to Gut, Itching, Joint Problems." It lands on the same Taste Tester PDP. The collected folds show broad sampling, air-dried comparison, "Why Air-dried?", ingredients, 12,000+ verified buyers, and sticky "Add To Cart - $19.99." The page does include deeper benefit copy for easy digestion, lean muscle/energy, joint health/mobility, and healthy skin/coat, but this is below the early purchase area and not framed as a direct continuation of the ad's gut/itching/joint promise.

### Google Ads

Google Ads Transparency screenshots show a broader acquisition mix than Meta: feeding calculator, proudly Australian owned, all-natural dog food, high-protein dog treats, "raw without the thaw," Aussie made treats, beef dog treats, and Eureka air-dried dog food. Offers include 17% off Starter Pack, 24% discount badges, Buy 4 Get 15% Off, and "Try a sample today." This creates good category coverage, but the paid-search/product message set is fragmented compared with Meta. Google communicates category, origin, and product range; Meta communicates health improvement, risk-free trial, and the $19.99 sample. The landing pages currently carry more of the Google category language than the Meta problem-specific language.

### Reviews & UGC

#### What Customers Love

- Dogs actually eat it, including fussy dogs. Representative reviews include "Ruby is a very fussy 9-year-old Cavoodle, and she has absolutely loved all three," "my fussy little poodleX loved them," and "My super fussy staffy cross border collie... is OBSESSED."
- Customers see health, coat, digestion, energy, weight, and vitality benefits. Reviewers mention shinier coats, weight control, better sleep, more energy, reduced stomach trouble, and healthier/happier dogs.
- Ingredient quality supports the premium price for many buyers. Customers repeatedly cite pure ingredients, no fillers, raw proteins and organs, Australian-made sourcing, and nutritional confidence.
- Subscription flexibility and service are a real strength for satisfied customers. Positive reviews call the subscription easy to fast-track or delay, simple to manage, and backed by prompt support.
- Treat/topper/training use is a high-value adoption path. Reviews say Eureka works as a treat, topper, scatter-mat food, Kong filler, training reward, and rescue-dog enrichment food.
- No-crumbs, shelf stability, portability, and low smell appear as concrete convenience benefits that are more specific than generic "easy" messaging.

#### What Frustrates Customers

- Price is the clearest barrier. Review language includes "beyond my budget," "still very expensive," "ridiculously expensive," and "$300+ for about 5kgs... unaffordable." Some customers like the product but can only justify it as a treat or topper.
- Subscription intent and control can create distrust. One 1-star reviewer said they "never signed up for more" after sampling and felt money was taken without consent.
- Delivery and courier problems damage trust. Reviews mention wrong address delivery, Aramex delivery issues, a request to deliver to a post office, and sample packs not received.
- Contact and support discoverability is inconsistent. One reviewer said there was "no phone number," another called the Contact Us page difficult to find, and a loyal customer reported an unresolved login code problem.
- One-size-fits-all gifts can disappoint small-dog owners. Reviews specifically mention goat horns and a croissant gift being unsuitable for small dogs.
- Taste tester conversion is not guaranteed. A few dogs ate samples then rejected the full-size bag, or refused samples entirely.

#### Client-Actionable Insights

- Make subscription terms and post-sample enrollment unmistakable in-cart and at checkout, especially around the $20 credit and autoship paths.
- Give shoppers size-appropriate treat/gift options, or ask dog size before assigning welcome gifts.
- Add highly visible help/contact paths in the header, cart drawer, account/login flow, and subscription management surfaces.
- Audit courier messaging and delivery instructions for rural/post-office use cases; negative reviews name delivery as a reason to leave despite liking the food.
- Build more price framing around topper, treat, and partial-feed use because review data shows budget-sensitive customers still buy when they can make a bag last 4-6 weeks.
- Use concrete convenience claims from reviews: no crumbs, no lingering smell, keeps in a treat pouch, no refrigeration, and easy delivery management.

### PageSpeed / Core Web Vitals

Collected 2026-08-18. Homepage Lighthouse performance score was 25/100, accessibility 76/100, best practices 77/100, SEO 92/100, agentic browsing 52/100. Homepage lab metrics were LCP 11.8s, CLS 0.641, TBT 560ms, FCP 2.7s, and Speed Index 9.5s. Lighthouse attributed major layout shift to the main content and hero bottom group, with image/media elements lacking explicit sizes, including the header logo and a mobile image. Main-thread work was 9.0s and unused JavaScript savings were estimated at 1,229 KiB.

The Taste Tester PDP Lighthouse performance score was 54/100, accessibility 84/100, best practices 77/100, SEO 92/100, agentic browsing 75/100. PDP lab metrics were LCP 4.6s, CLS 0.01, TBT 550ms, FCP 3.2s, and Speed Index 20.3s. Main-thread work was 21.7s and unused JavaScript savings were estimated at 1,223 KiB. The PDP has better CLS than the homepage but still has slow perceived completion and heavy JavaScript.

### Competitor Analysis

Competitor research date: 2026-08-18. No user-provided `raw/competitors.md` was present; competitor data below is self-researched.

| Brand | Price reference | Key features | Eureka-relevant weakness/opportunity |
| --- | --- | --- | --- |
| Eureka Pet Co | Taste Tester $19.99; Starter Pack autoship $169.15 or one-time $199.00 from collected/live PDPs | Australian owned/made, air-dried, 75-90%+ meat depending recipe, 7-recipe Taste Tester, $20 first-subscription credit, free treats for life on qualifying autoship | Strong proof exists, but paid landing pages do not consistently put ad-specific health/training proof above the CTA. Budget objections need clearer partial-feed framing. |
| ZIWI Peak | Official site shows air-dried dog recipes from $29.58-$48.08 NZD; 99PetShops showed Ziwi Peak Air-Dried Lamb 1kg from $68.49 AUD | New Zealand air-dried category leader, up to 96% protein, no fillers/artificial ingredients, complete meal/topper/treat positioning, Z-TWINTECH air-drying | Global premium brand but less Australia-owned than Eureka; Eureka can win on local sourcing, sample-first trial, and better subscription perks. |
| Frontier Pets | Official site shows 300g dog food from $25.95-$29.95, 3 x 300g Starter Bundle $59.95, and ~$4.50/day for a 10kg dog example | Freeze-dried raw, vet-developed, 10,000+ reviews, free-range Australian ingredients, just add water, shelf stable, autoship 10%, bundles 15% | Strong cost-comparison and daily-cost framing. Eureka should match the clarity of daily cost/topper use without copying freeze-dried hydration mechanics. |
| Lyka | Official help centre says pricing is personalized by dog profile; homepage shows 4.9 rating, 8,000+ reviews, 100,000+ Aussie dogs, 30% off first 2 deliveries | Fresh gently cooked meals, vet nutritionist formulated, personalized portions, clinical gut/poo proof, delivery subscription, no sample packs but starter box | Lyka owns personalization and clinical proof. Eureka can counter with shelf-stable convenience, sample packs, no freezer/fridge, and clearer skin/gut/joint benefit substantiation. |

### Emails

Email campaigns were skipped in the manifest. No email screenshots or `raw/emails.md` were present, so no email findings were analyzed.

### Inspiration Sites

Inspiration sites were skipped in the manifest. No inspiration screenshots or `raw/inspiration.md` were present, so no inspiration findings were analyzed.

### Non-Data Context

User-provided context says not to create any tests on the collection page. Collection-like screenshots are future audit context only. Test focus must stay on the Ad 1 landing page, Ad 2/3 landing page/PDP, and homepage. Ad 2 and Ad 3 share the same Taste Tester landing page, which is also the PDP.

### Current Site Screenshots

Homepage: The first fold has a sticky header and promo bar, centered logo, navigation, and a split hero with "Real Food Real Easy," subcopy "One less thing to think about.", orange "Shop Now" CTA, Trustpilot "Excellent," "Join 76,000+ happy dogs!", and a dog image on the right. Live homepage text later shows reviews, "Say Eureka in 3 easy steps," Quick Calculator, recipe selection, and Autoship + Save. The early hierarchy is clean but generic: it does not surface the most conversion-relevant review themes, the $19.99 sample path, or health-specific claims in the hero.

Collection page: Files named `pdp-f1.png`, `pdp-f2.png`, and `pdp-f3.png` visually show the "All" collection with 50 products, filters, product cards, ratings, prices, badges, and sort control. This is reference context only because the user explicitly requested no collection-page tests.

PDP: The Starter Pack PDP shows the product gallery, title, 4.9/303 reviews, selected Eureka 90 option, frequency selector, autoship preselected at $169.15 with savings and free perks, quantity selector, black add-to-cart CTA, trust badges, accordions, video tiles, comparison content, 12,000+ verified buyers band, "Why Air-dried?", and a sticky subscription CTA lower on the page. The paid trainer ad does not visibly continue into a trainer/treat/topper explanation above the CTA.

PDP: The Taste Tester PDP shows the product gallery, 4.9/3707 reviews, $19.99 price, sample badge, copy about seven recipes and one 20g sample of each, free delivery, $20 first-subscription credit, quantity selector, black add-to-cart CTA, free-shipping/sample/Australian-owned badges, video tiles, comparison table, review band, "Why Air-dried?", ingredients/process icons, and sticky "Add To Cart - $19.99." It matches Ad 2's sample offer but underserves Ad 3's gut/itching/joint promise in the first purchase area.

Cart: The cart is a drawer with "Cart - 1," a close icon, "Your Sample is On the Way!," Taste Tester item at $19.99, quantity controls, remove icon, discount code field, black "Checkout - $19.99" button, and an "I'm even better with" cross-sell carousel showing Fillet O Fish at $19.95 with "+ Quick Add." It has an AOV mechanic, but no visible guarantee, delivery reassurance, subscription clarity, or $20 credit reminder.

## Cross-Source Themes

1. Paid-message continuation is uneven. Meta Ad 1 promises training utility, Ad 3 promises relief from gut/itching/joint problems, reviews validate training/topper use and health outcomes, but the corresponding PDP first folds prioritize generic product configuration and sampling mechanics. Evidence strength: Meta ads, landing page screenshots, live PDP text, reviews. Revenue potential: high because paid traffic is already segmented by intent. Funnel importance: high because the gap appears before add-to-cart.

2. Premium-price anxiety needs more specific value framing. Reviews repeatedly say the product is expensive or unaffordable, while positive reviews justify price through no waste, small feeding amounts, topper/training use, health improvements, and customer service. Competitors such as Frontier Pets explicitly show daily cost comparisons. Evidence strength: reviews, competitor research, PDP pricing, Google Ads discounts. Revenue potential: high because it affects sample-to-subscription and full-size conversion. Funnel importance: high across homepage, PDP, and cart.

3. Trust is strong but not placed where risk spikes. Eureka has 4.9 ratings, 12,000+ verified buyers, 76,000+ happy dogs, guarantees, Australian-made badges, and positive service reviews. Yet negative reviews cluster around subscription misunderstanding, delivery, contact discoverability, login, and unsuitable gifts. Evidence strength: reviews, site screenshots, cart screenshot, PDP screenshots. Revenue potential: medium-high because risk reassurance can protect checkout and subscription conversion. Funnel importance: high at add-to-cart/cart and autoship selection.

## Top Test Opportunities

**Ad 3 Symptom-Match Taste Tester Hero** - The Taste Tester first fold does not visibly continue the "gut, itching, joint problems" ad promise, costing high-intent health-problem clicks clarity before add-to-cart. Evidence: Meta Ad 3 summary, Taste Tester PDP screenshots, live PDP text, reviews citing gut health, coat, energy, joints. Est. lift: 3-6% CR lift x unknown sessions/mo x unknown blended AOV = model required.

**Ad 1 Training/Topper Starter Pack Hero** - The trainer-led ad lands on a Starter Pack buy box with recipe and autoship controls but no above-CTA training/topper use case, costing message match for trainer-qualified traffic. Evidence: Meta Ad 1 summary, Starter Pack PDP screenshots, live PDP text, reviews mentioning training reward/treat pouch/topper use. Est. lift: 3-5% CR lift x unknown sessions/mo x unknown blended AOV = model required.

**Homepage Sample-First Path Above The Fold** - The homepage hero CTA only says "Shop Now" and does not surface the low-friction $19.99 Taste Tester path despite paid and review evidence that sampling converts hesitant/fussy-dog buyers. Evidence: homepage screenshots, live homepage text, Meta Ads 2/3, Taste Tester PDP, reviews. Est. lift: 2-4% CR lift x unknown sessions/mo x unknown blended AOV = model required.

**Premium Value Cost-Framing Block Near PDP CTA** - The Starter Pack and Taste Tester pages show price and discounts, but they do not immediately reframe premium cost with daily/topper/training economics, no-waste proof, or feeding-duration examples. Evidence: reviews price objections, competitor Frontier daily-cost framing, Starter Pack/Taste Tester PDP screenshots. Est. lift: 2-5% CR lift x unknown sessions/mo x unknown blended AOV = model required.

**Autoship Clarity And Consent Panel** - The Starter Pack buy box preselects autoship with perks and a lower one-time price option, while reviews show subscription misunderstanding and refund anxiety, risking checkout abandonment or post-purchase distrust. Evidence: Starter Pack PDP screenshots, reviews mentioning unexpected subscription/money taken, live page subscription language. Est. lift: 2-4% CR lift x unknown sessions/mo x unknown blended AOV = model required.

**Cart Drawer Risk-Reversal And Credit Reminder** - The cart drawer has checkout and a cross-sell but lacks visible money-back guarantee, free delivery/threshold clarity, subscription reassurance, and the Taste Tester $20 credit reminder at the moment of checkout. Evidence: cart screenshot, Taste Tester PDP text, reviews about delivery, contact, subscription control. Est. lift: 1.5-3% checkout lift x unknown sessions/mo x unknown blended AOV = model required.

**Health Proof Strip Above Taste Tester CTA** - The Taste Tester page has reviews and broad air-dried benefits lower down, but the first fold does not show concrete proof for the 86% health-improvement ad claim near the add-to-cart button. Evidence: Meta Ad 2 summary, Taste Tester PDP screenshots, reviews, live page health-benefit sections. Est. lift: 2-4% CR lift x unknown sessions/mo x unknown blended AOV = model required.

**Homepage Hero Proof Upgrade** - The homepage first fold uses "One less thing to think about" and Trustpilot proof, but misses the strongest review-backed reasons to believe: fussy dogs eat it, coats improve, no fillers, and subscription control. Evidence: homepage screenshots, reviews, Google ad themes, live homepage testimonials. Est. lift: 2-3.5% CR lift x unknown sessions/mo x unknown blended AOV = model required.

**Small-Dog Gift Fit Reassurance** - Subscription perks promise free treats for life and welcome gifts, but reviews cite goat horn/croissant mismatch for small dogs, so the perk can create concern instead of increasing perceived value. Evidence: reviews, Starter Pack autoship screenshots, live autoship perk text. Est. lift: 1-2.5% subscription selection lift x unknown sessions/mo x unknown subscription AOV = model required.

**PDP Performance Stabilization Test For Homepage-To-PDP Flow** - The homepage has LCP 11.8s and CLS 0.641, while the Taste Tester PDP has Speed Index 20.3s and heavy JavaScript, creating likely lost engagement before shoppers reach product education or sticky CTA. Evidence: PageSpeed collected 2026-08-18, Lighthouse JSON diagnostics, homepage and PDP screenshots. Est. lift: 1-3% CR lift x unknown sessions/mo x unknown blended AOV = model required.

## Unused but Valuable Findings

- Google Ads include treat-specific and feeding-calculator messages that could support future search-specific landing page variants, but current requested focus excludes collection-page tests.
- The collection grid shows many product badges and price formats, which may be useful for future merchandising work but should not enter the current roadmap.
- Contact discoverability and login-code issues likely require operational fixes alongside CRO messaging because reviews describe support access as hard to find.

## Missing Data

- Collection screenshots with canonical names `collection-f1.png`, `collection-f2.png`, and `collection-f3.png` were missing; files named `pdp-f1.png`, `pdp-f2.png`, and `pdp-f3.png` visually show collection-grid content instead.
- Email campaign data was skipped, so lifecycle message match and offer sequencing could not be assessed.
- Inspiration-site data was skipped, so external UX pattern extraction was not available.
- Monthly sessions and blended AOV were not present in the collected data, so revenue estimates remain formula-based rather than dollarized.
