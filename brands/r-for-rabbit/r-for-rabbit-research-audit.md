# R for Rabbit CRO Research Audit

## Data Sources Used

- Manifest: `brands/r-for-rabbit/manifest.md`
- User-provided Reviews & UGC: `raw/reviews.md`, `raw/reviews-attachment-1.txt`, `raw/reviews-attachment-2.txt`, `raw/reviews-attachment-3.txt`
- Existing screenshots and visual summaries: `raw/meta-ads-visual-summary.md`, `raw/google-ads-visual-summary.md`, `raw/site-visual-summary.md`
- PageSpeed JSON: `data-collection/homepage-speed.json`, collected 2026-06-09 13:05:01 UTC; `data-collection/pdp-page-speed.json`, collected 2026-06-09 13:00:15 UTC
- Live store text fetch: https://rforrabbit.com/, fetched during audit on 2026-06-09
- Self-researched competitor sources, researched 2026-06-09: R for Rabbit live site, LuvLap official site, Mee Mee official site, FirstCry/Babyhug pages, Owler competitor listing

## Source Findings

### Meta Ads & Landing Pages

Meta ads and landing screenshots show strong product-level message match but weak offer-code clarity. Ad 1 promotes the Rock N Roll 2-in-1 stroller cum rocker with up to 45% off and code `NEW12`; the PDP shows the same stroller, price `₹6,998`, color swatches, `Add To Cart`, free customization, pincode checker, trust icons, and stroller media, but visible offer cards emphasize other offers such as `DAYONE`, app savings, and free customization. Ad 2 promotes Feather Diaper Sample at `₹3` via app code `TRYSAMPLE`; its PDP fold does match with a `Try Diaper Sample at ₹3` app-exclusive banner, but visible offer cards show `DPR15` and `DAYONE`. Ad 3 promotes Feather Diapers with `DPR15`; its PDP shows the same product and `DPR15`, but also introduces subscription, cashback, app savings, and bundle modules before description content.

Landing pages are rich in product proof, video, UGC, bundles, and offers, but the first fold asks shoppers to process many simultaneous incentives. The offer promise from the ad is not always the dominant offer on the PDP, which can make promo-code shoppers pause at the moment they should be adding to cart. `raw/meta-ads.md` was not present, so individual landing page URLs could not be fetched from ad records; the ad landing analysis uses collected visual summaries only.

### Google Ads

Google Ads screenshots show a broader acquisition footprint than Meta: strollers, tricycles, high chairs, feeding bottles, baby carriers, carry cots, car seats, diaper bags, scooters, bicycles, and diapers. Headline themes include `R for Rabbit Official Store`, safety, premium design, sale events, `Up To 50% off`, and category-specific claims. Promo language includes `DPR15`, `FFRIST`, app/event sale references, cash on delivery/free shipping snippets, and savings up to `₹1000`.

The diaper code `DPR15` appears in both Meta and Google Ads, but Google Ads also uses many other sale/code themes. This creates acquisition consistency around discounting, but not around a single next step. The site header and cart currently emphasize `DAYONE`, while ad creatives may prime visitors for `NEW12`, `TRYSAMPLE`, `DPR15`, or `FFRIST`.

### Reviews & UGC

Review data covers 76 dated reviews from 2025-10-15 through 2026-02-10 in `raw/reviews.md` and attachments. Ratings were 57 five-star, 4 four-star, 1 two-star, and 14 one-star reviews.

#### What Customers Love

- Comfort and softness, especially Feather Diapers. Representative quotes: "The softest diapers ever witnessed", "diapers are very gentle and rash free", and "comfortable and last long."
- Broad one-stop assortment. Customers mention using diapers, high chairs, strollers, baby carriers, car seats, toys, bath tubs, sippers, grooming kits, and feeding products.
- Safety, quality, and trust. Positive reviews repeatedly use language such as "trusted baby brand", "safe", "sturdy", "premium", "scientific research", and "quality standards".
- Community, app, subscription, and expert support can be differentiators. Positive reviews mention a smooth app, subscription plan, parenting community, expert consultation, and specific helpful support agents.

#### What Frustrates Customers

- Delivery and fulfillment failures are the clearest negative theme. Customers report delayed products, no delivery updates, wrong item delivered, no proactive communication, and prepaid orders not arriving.
- Return/refund handling creates trust damage. Complaints mention delayed refunds, non-returnable-product confusion, return pickup delays, and cancellation requests not being handled.
- Customer support quality is inconsistent. Several one-star reviews describe agents disconnecting, email non-response, IVR dead ends, and support not coordinating with couriers.
- Packaging, product condition, and data-security concerns are severe when they appear. Reviews mention tampered/open products, bad quality/marked potty training product, wrong item delivery, and one alleged order-data leak tied to financial fraud.

#### Client-Actionable Insights

- Improve delivery-status communication for prepaid and essential repeat products such as diapers; show proactive delivery expectations and escalation paths before checkout and in post-purchase messaging.
- Add clearer return/refund policy treatment on PDP and cart for hygiene-sensitive products, including what qualifies for replacement if the item arrives damaged, tampered, or incorrect.
- Train support scripts around non-returnable items so agents do not prematurely deny resolutions on damaged/wrong deliveries.
- Investigate logistics exceptions and data-security complaints; these are trust issues that can depress conversion for new parents even when product satisfaction is high.

### PageSpeed / Core Web Vitals

Homepage PageSpeed was collected 2026-06-09 13:05:01 UTC. Scores: Performance 27, Accessibility 81, Best Practices 73, SEO 85. Key mobile lab metrics: LCP 26.5s, FCP 3.8s, Speed Index 12.6s, Total Blocking Time 6,030ms, Time to Interactive 56.2s, CLS 0.068, unused JavaScript savings 1,718 KiB.

Feather Diapers PDP PageSpeed was collected 2026-06-09 13:00:15 UTC. Scores: Performance 29, Accessibility 67, Best Practices 77, SEO 77. Key mobile lab metrics: LCP 20.0s, FCP 3.4s, Speed Index 18.7s, Total Blocking Time 7,580ms, Time to Interactive 75.1s, CLS 0.007, unused JavaScript savings 1,632 KiB.

The highest conversion risk is not layout shift; it is waiting and main-thread blockage. Product discovery and PDP purchase options are likely visible late or sluggish, especially with floating widgets, carousel/product modules, UGC/video, app banners, and offer logic competing for JavaScript budget.

### Competitor Analysis

Competitor research date: 2026-06-09. User-provided competitor file `raw/competitors.md` was not present. Self-researched sources identify FirstCry/Babyhug, Mee Mee, LuvLap, Mothercare, and Chicco as relevant competitors; Owler specifically lists FirstCry, Mothercare, Mee Mee, and Chicco as top R for Rabbit competitors.

| Brand | Price / Offer Evidence | Key Features | Weakness / Opportunity vs. R for Rabbit | Source Type |
|---|---:|---|---|---|
| R for Rabbit | Rock N Roll stroller PDP `₹6,998`; Feather Diaper PDP `₹394`; cart threshold asks `Add ₹1106 more to save ₹100`. Live site claims 500+ products, 5M+ happy parents, 4.5+ rating across platforms. | Strong D2C brand, broad baby gear/diapering/feeding range, app savings, subscription, bundles, UGC/video, safety/quality positioning. | On-site promo stack is noisy; collected reviews show delivery/refund trust concerns; product cards show red liquid error text. | Collected screenshots and live store fetch |
| LuvLap | Official site shows Alpha stroller `₹6,999` vs `₹9,999`, Sunshine stroller `₹3,999`, several stroller deals 19-33% off. | Safety harness, reversible handle, recline, canopy, broad baby care and gear assortment. | More utilitarian price-led competitor; R for Rabbit can win with community/app/proof if trust and clarity improve. | Self-researched official site |
| FirstCry / Babyhug | Babyhug diaper pants page shows prices from about `₹530-₹1,286`, per-diaper pricing from `₹6.03-₹22.32`, very high rating counts; Babyhug 3-in-1 high chair review page shows `₹2,997.50` vs `₹5,995`. | Marketplace scale, Babyhug private label, club pricing, very high visible review counts, broad assortment. | Strong price/review-count pressure; R for Rabbit needs clearer owned-brand trust and delivery confidence. | Self-researched FirstCry pages |
| Mee Mee | Ultra Sleek Portable Baby High Chair listed at `Rs. 8,499`, low stock, add-to-cart visible. | Premium high chair positioning, folding, self-standing storage, safety belt, adjustable tray, cushioned seat, national retail distribution. | More focused product pages; R for Rabbit can compete with app/community/subscription ecosystem but should reduce first-fold clutter. | Self-researched official site |

### Emails

No email screenshots (`email-1.png`, `email-2.png`) and no `raw/emails.md` were present. Email message match, subject-line, and CTA findings are a missing data gap.

### Inspiration Sites

No `raw/inspiration.md` and no inspiration screenshots were present. Inspiration-site UX patterns are a missing data gap.

### Non-Data Context

No `raw/context.md` was present. Strategic priorities beyond the manifest are unknown. The manifest notes 3 total test slots, 0 dev/project slots, 1 variation vs. control, and no specific focus areas.

### Current Site Screenshots

Live store text confirms R for Rabbit positions itself as a broad baby-products store spanning baby gear, diapering, feeding and nursing, baby skin care, toys, nursery, kids furniture, and gifts. It claims 5M+ happy parents, 500+ products, and 4.5+ ratings across online and digital platforms.

Homepage: The first fold has a green coupon strip for `DAYONE`, full navigation, search, app download, account/order/cart icons, a hero carousel for gifts, and horizontal savings tiles. Fold 2 introduces the official store paragraph and `Most Loved Products`; fold 3 continues product carousels and `Shop by Age`. The conversion issue is hierarchy: brand trust, seasonal gifting, offers, product carousels, app download, cashback, WhatsApp, and carousel controls all compete early. Product cards show red liquid error text before the `Add to Cart` button, creating a broken-store cue exactly where users evaluate products.

Collection page: The `All` collection uses a left filter sidebar and a four-column product grid. Filters are extensive, including product type, weight capacity, age, availability, ratings, discount, features, folding mechanism, hood/canopy, brakes, safety standard, harness, material, and price. The visible grid repeats Feather Diapers variants rather than mixed categories. Each card includes image, truncated title, rating, price, red liquid error text, and `Add to Cart`. The page gives strong filtering depth but weak category clarity and repeated error text in the main buying path.

PDP: The Feather Diapers PDP first fold has the promo strip, nav, subscription banner, gallery, title, `4.7 | 939`, SKU, `₹394`, app savings, cashback, style selector, size guide, diaper size and pack size dropdowns, subscription vs one-time selectors, and `Add To Cart`. Fold 2 adds pincode check, offer cards, trust icons, and frequently bought together. Fold 3 adds UGC/video tiles, description/FAQ/reviews tabs, testing badges, and embedded video. The issue is that high-value proof and testing content sit below purchase complexity, while the buy box asks shoppers to choose size, pack, purchase type, app savings, cashback, coupons, and subscription before seeing the deeper trust story.

Cart: Cart is a right-side drawer with coupon reminder `Use Coupon: DAYONE`, progress text `Add ₹1106 more to save ₹100`, milestone savings from `₹100` to `₹800`, app savings strip with `Download`, Feather Diapers line item, size/pack dropdowns, quantity stepper, coupon field, pincode checker, estimated total dropdown, `You are saving ₹0 on this order`, and `Check Out`. The drawer has clear AOV mechanics, but the zero-savings message and multiple saving systems can make the cart feel less rewarding than intended.

## Cross-Source Themes

1. Trust is the highest-leverage theme. Reviews show strong product love but 14 one-star reviews concentrated around delivery, refunds, support, tampered/wrong products, and data-security fears; site, ads, and PDPs lean heavily on safety/quality claims, so trust gaps happen at the exact promise the brand sells.
2. Offer and promo clarity is fragmented across the funnel. Meta, Google, homepage, PDP, and cart surface `NEW12`, `TRYSAMPLE`, `DPR15`, `DAYONE`, `FFRIST`, app savings, cashback, threshold savings, and subscription savings. Evidence appears in Meta ads, Google ads, PDPs, homepage, and cart.
3. Product-card and PDP purchase paths have avoidable friction. Site screenshots show red liquid error text on product cards, repeated diaper variants in collection, heavy first-fold PDP decision load, and PageSpeed performance scores of 27-29 with LCP at 20.0-26.5s and TBT above 6s.

## Top Test Opportunities

**Fix Broken Product Card Error Text on Homepage and Collection** - Product cards currently show red liquid error text between price and `Add to Cart`, making the store look technically broken at the point of purchase. Evidence: site screenshots, homepage summary, collection summary, PageSpeed JS bloat. Est. lift: 2.0% CR lift x unknown sessions/mo x unknown AOV = unknown.

**Unify First-Order Offer Messaging From Ad to PDP to Cart** - Shoppers arriving from ads see codes such as `NEW12`, `TRYSAMPLE`, or `DPR15`, but the PDP/cart often emphasizes `DAYONE`, app savings, cashback, and threshold savings instead. Evidence: Meta visual summary, Google visual summary, PDP screenshots, cart screenshot. Est. lift: 1.5% CR lift x unknown sessions/mo x unknown AOV = unknown.

**Simplify Feather Diapers Buy Box Around Size, Pack, and Purchase Type** - The PDP buy box stacks app savings, cashback, selectors, subscription vs one-time, offer cards, pincode, and bundles before many proof elements, slowing the path to add-to-cart for a repeat-purchase product. Evidence: PDP screenshots, Meta Ad 2/3 landing summaries, PageSpeed PDP LCP 20.0s and TBT 7,580ms, review praise for diaper softness/comfort. Est. lift: 2.5% CR lift x unknown sessions/mo x unknown AOV = unknown.

**Add Delivery/Return Confidence Near Checkout for Hygiene and Gear Products** - Reviews show delayed delivery, wrong item, tampered product, refund, and support failures, while the cart asks for checkout without reassuring shoppers about escalation, replacement, or refund policy. Evidence: 76-review dataset, cart screenshot, PDP pincode/check/offer area. Est. lift: 1.5% CR lift x unknown sessions/mo x unknown AOV = unknown.

**Make Cart Savings Feel Earned Instead of Fragmented** - Cart shows `Add ₹1106 more to save ₹100`, multiple savings milestones, app download savings, coupon input, and `You are saving ₹0`, which can undercut the reward loop. Evidence: cart screenshot, Google/Meta offer fragmentation, review support complaints. Est. lift: 1.0% CR lift x unknown sessions/mo x unknown AOV = unknown.

## Unused but Valuable Findings

- Homepage `Most Loved Products` and `Just Launched` carousels may hide breadth because the visible card rows compete with hero, offer tiles, app prompt, cashback, and WhatsApp widgets.
- Competitor price pressure from Babyhug diaper pants and LuvLap strollers makes per-unit price clarity and discount credibility important for R for Rabbit.
- Positive reviews mention the parenting community and expert support, but that proof is not prominent in the collected PDP first fold.

## Missing Data

- `raw/meta-ads.md` was missing, so ad landing page URLs could not be fetched from ad records during audit.
- `raw/google-ads.md` was missing; Google Ads analysis used the visual summary only.
- `raw/competitors.md` was missing; competitor analysis used self-research only.
- Email screenshots and `raw/emails.md` were missing, so lifecycle/email message match could not be analyzed.
- `raw/inspiration.md` and inspiration screenshots were missing, so inspiration-site patterns could not be analyzed.
- `raw/context.md` was missing, so non-data strategic context is limited to the manifest.
