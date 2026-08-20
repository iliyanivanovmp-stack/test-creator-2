# Performance Golf, 30-Day Business Summary

**Prepared:** 2026-08-16
**Source:** Shopify Admin API (`performancegolf.myshopify.com`, Shopify Plus), pulled 2026-08-16
**Window:** 2026-07-17 to 2026-08-16
**Currency:** USD (100% of orders). **Store timezone:** America/New_York.

This document is a self-contained export. Every number below comes from the Shopify pull described above. Read the "Data caveats" section before drawing conclusions, several obvious-looking metrics mean something narrower than they appear.

---

## 1. Data caveats, read first

These constrain what can honestly be concluded. They matter more than usual because this doc is intended for downstream analysis.

| # | Caveat | Effect |
|---|---|---|
| 1 | **Both edge days are partial.** The window opens 2026-07-17 at 10:12 and closes 2026-08-16 at 10:10. | Use the 29-day full-day window (2026-07-18 to 2026-08-15) for any rate or average. Headline totals below cover all 31 calendar dates. |
| 2 | **No new-versus-repeat split.** Shopify returned the customer object but withheld `orders_count` and `total_spent` on every order. Those are protected customer data fields requiring separate Shopify approval, which this app does not have. | Repeat rate, cohort behaviour, and LTV are unavailable. Do not infer them. |
| 3 | **"Abandoned checkouts" only counts checkouts that reached email capture.** All 2,224 records have an email address. | The 17.4% figure in section 7 is not a true cart abandonment rate. Real browse-to-cart-to-checkout abandonment is far higher and is not measurable from this data. |
| 4 | **No traffic or session data.** The client does not use Google Analytics, and no Microsoft Clarity export exists yet. | There is no site-wide conversion rate, bounce rate, or funnel step data. Nothing here divides by sessions. |
| 5 | **60-day API ceiling.** The token holds `read_orders`, not `read_all_orders`. | No year-over-year or seasonal comparison is possible. All trends are within-window only. |
| 6 | **`total_price` includes tax and shipping.** | The $238.19 AOV is gross. Merchandise-only AOV is $220.93. Both are given below. |
| 7 | **Attribution is Shopify's `landing_site` and `referring_site` only.** | This is first-touch landing data, not modelled multi-touch attribution. Roughly 63% of orders carry no UTM source at all. |
| 8 | Customer-level bulk export was deliberately not pulled (personally identifiable information). | Section 8 geography comes from order addresses, aggregated to country and state only. |

---

## 2. Headline numbers

**Full window, 2026-07-17 to 2026-08-16, 10,558 live orders** (10,630 pulled, 72 cancelled and excluded).

| Metric | Value |
|---|---|
| Gross revenue (total price) | $2,514,819.85 |
| Merchandise subtotal | $2,332,582.00 |
| Discounts given | $182,429.97 |
| Tax collected | $155,517.85 |
| Shipping collected | $26,720.00 |
| Live orders | 10,558 |
| AOV, gross | $238.19 |
| AOV, merchandise only | $220.93 |
| Median order | $256.53 |
| 25th / 75th / 90th percentile order | $47.00 / $422.94 / $459.03 |

**Normalised 29-day window, 2026-07-18 to 2026-08-15** (both partial days removed, use this for rates):

| Metric | Value |
|---|---|
| Orders | 10,211 |
| Revenue | $2,434,183.13 |
| AOV | $238.39 |
| Average orders per day | 352.1 |
| Average revenue per day | $83,937.35 |

**Order financial status:** 96.1% paid (10,148), 3.0% refunded (320), 0.9% partially refunded (90).

---

## 3. The most important pattern: volume up, order value down

Week-over-week, ending 2026-08-15:

| Week | Orders | Revenue | AOV |
|---|---|---|---|
| Jul 19 to Jul 25 | 2,248 | $555,229.01 | $246.99 |
| Jul 26 to Aug 1 | 2,258 | $636,956.12 | $282.09 |
| Aug 2 to Aug 8 | 2,480 | $584,133.31 | $235.54 |
| Aug 9 to Aug 15 | 2,929 | $575,838.56 | $196.60 |

Order count climbed 30% across the four weeks while AOV fell 30% from the peak. Revenue stayed roughly flat between $555k and $637k. The most recent week set the volume record and the AOV floor at the same time.

This is the single clearest trend in the dataset and it should anchor any analysis. The mix is shifting toward cheaper orders rather than the business growing. Whatever drove the extra 681 orders in the final week is not carrying equivalent value.

---

## 4. Product performance

### Revenue leaders

| Product | Revenue | Units | Orders | Order attach | Typical price |
|---|---|---|---|---|---|
| RS1 Putter | $1,242,986.10 | 3,006 | 2,986 | 28.3% | $399 / $429 |
| SF2 Driver | $516,662.20 | 1,728 | 1,717 | 16.3% | $299 |
| 357 Super 7-Wood | $211,571.81 | 851 | 845 | 8.0% | $249 |
| ONE.1 Wedge | $114,826.85 | 771 | 700 | 6.6% | $149 |
| iON+ Golf Ball | $79,799.35 | 1,381 | 891 | 8.4% | $34.99 |
| 359 Super 9-Wood | $75,005.20 | 397 | 395 | 3.7% | $189 |
| Simple Strike Sequence | $53,059.00 | 547 | 543 | 5.1% | $97 |
| Senior Swing Distance Program | $34,921.00 | 743 | 739 | 7.0% | $47 |
| One Shot Slice Fix | $32,101.00 | 683 | 679 | 6.4% | $47 |
| SpeedTrac | $29,293.35 | 164 | 163 | 1.5% | $179 |
| PG1 Scratch | $18,982.00 | 1,060 | 1,051 | 10.0% | $29 |
| PG1 Plus | $15,964.00 | 859 | 836 | 7.9% | $29 |
| SwingSmooth Pro | $15,288.00 | 116 | 115 | 1.1% | $62.10 |

The RS1 Putter alone accounts for 49.4% of gross revenue. RS1 and SF2 together account for 70.0%. This is a heavily concentrated catalogue.

### The free PG1 trial dominates order composition

"PG1 7-Day Trial (No Subscription)" attaches to **49.9% of all orders (5,273)** at $0.00. It is the highest-attach item in the catalogue and carries no revenue.

- 636 orders (6.0%) contain nothing but free items.
- 5,700 orders (54.0%) mix the free trial with paid product.
- Excluding free-only orders, AOV rises to $253.46 and median to $269.54.

Of the 2,986 RS1 Putter orders, 2,077 (69.6%) also carry the free PG1 trial. The trial is functioning as the primary front-end hook attached to hardware sales, not as a standalone acquisition product.

### Live price test on the top product

The RS1 Putter sold at two prices throughout the entire window in a near-even split: **1,524 units at $399 and 1,479 units at $429**. The split holds day by day across all 31 dates, averaging close to 50/50 and never drifting outside roughly 39% to 60%.

That consistency is what a running 50/50 price test looks like. This export cannot confirm which tool is running it or which arm is winning, because Shopify does not expose the experiment assignment. **Anyone analysing RS1 revenue or AOV needs to know this test is live**, otherwise the two price points read as noise.

Note the iON+ Golf Ball also shows two price points, $34.99 (889 units) and $98.97 (492 units). That is a single ball versus a three-pack, not a test. $98.97 is exactly three times $32.99.

### Refund exposure

410 orders were refunded or partially refunded, covering $148,206.86 of gross order value.

| Product | Orders containing | Refunded | Rate |
|---|---|---|---|
| RS1 Putter | 2,986 | 224 | 7.5% |
| 359 Super 9-Wood | 395 | 25 | 6.3% |
| 357 Super 7-Wood | 845 | 42 | 5.0% |
| PG1 7-Day Trial | 5,273 | 245 | 4.6% |
| SF2 Driver | 1,717 | 58 | 3.4% |
| SpeedTrac | 163 | 5 | 3.1% |
| PG1 Scratch | 1,051 | 26 | 2.5% |
| ONE.1 Wedge | 700 | 17 | 2.4% |
| iON+ Golf Ball | 891 | 2 | 0.2% |

The RS1 Putter carries both the highest revenue share and the highest refund rate among high-volume products. Digital courses barely refund at all.

---

## 5. Basket structure

| Metric | Value |
|---|---|
| Average units per order | 1.75 |
| Average line items per order | 1.74 |
| Single-line orders | 4,582 (43.4%) |
| Two-line orders | 4,678 (44.3%) |
| Three-line orders | 805 (7.6%) |
| Four-line orders | 470 (4.5%) |
| Five or more lines | 23 (0.2%) |

Because the free trial occupies a line on half of all orders, the true paid-item basket is thinner than 1.74 suggests. Most orders are effectively one paid product plus a free trial.

### Two cross-sell gaps

**Multiple clubs per order is rare but very valuable.** Of 6,409 orders containing at least one club, only 382 (6.0%) contain two or more. Those orders average $556.69 against $346.03 for single-club orders, a $210.66 gap.

**Hardware and digital courses almost never sell together.** Of 6,409 hardware orders, just 5 (0.1%) also contain a digital training course. The two catalogues, clubs and courses, are running as near-completely separate funnels despite serving the same customer.

### Order value distribution

| Subtotal band | Orders | Share |
|---|---|---|
| $0 to $25 | 1,147 | 10.9% |
| $25 to $50 | 1,922 | 18.2% |
| $50 to $75 | 69 | 0.7% |
| $75 to $100 | 653 | 6.2% |
| $100 to $150 | 708 | 6.7% |
| $150 to $200 | 662 | 6.3% |
| $200 to $300 | 2,217 | 21.0% |
| $300 to $400 | 1,656 | 15.7% |
| $400 to $500 | 1,324 | 12.5% |
| $500 to $750 | 160 | 1.5% |
| $750 to $1,000 | 29 | 0.3% |
| Over $1,000 | 11 | 0.1% |

The distribution is strongly bimodal. One cluster sits under $50 (29.1% of orders, the subscription and digital-course business) and another sits between $200 and $500 (49.2%, the hardware business). The $50 to $200 middle is thin at 19.9%.

Only 4.2% of orders (445) paid for shipping, generating $26,720.00.

---

## 6. Channels and traffic sources

### Order source

| Source | Orders | Share | Revenue | AOV |
|---|---|---|---|---|
| web | 9,061 | 85.8% | $2,365,908.08 | $261.11 |
| subscription_contract_checkout_one | 1,198 | 11.3% | $54,805.31 | $45.75 |
| Channel 3890849 | 294 | 2.8% | $93,718.87 | $318.77 |
| channel:9273665 | 5 | 0.0% | $387.59 | $77.52 |

Recurring subscription billing accounts for 11.3% of order count but only 2.2% of revenue. Those orders are mostly PG1 Scratch (613), PG1 Plus (289), and Scratch Club (206).

Channel 3890849 is an unnamed app channel with the highest AOV of any source at $318.77. Its landing paths are all cart and checkout-clone links, and 241 orders in the window carry the tags "Shop App Test 03/17/2026" and "Shop Cash offers acquired". That is consistent with the Shopify Shop app, though the numeric channel ID alone does not prove it. Worth confirming before anyone builds on it.

### UTM source

| Source | Orders | Share | Revenue | AOV |
|---|---|---|---|---|
| No UTM | 6,652 | 63.0% | $1,337,511.90 | $201.07 |
| facebook | 2,318 | 22.0% | $802,158.07 | $346.06 |
| Klaviyo | 488 | 4.6% | $55,578.35 | $113.89 |
| microsoft | 399 | 3.8% | $133,191.65 | $333.81 |
| search | 232 | 2.2% | $67,052.78 | $289.02 |
| awin | 119 | 1.1% | $32,414.79 | $272.39 |
| attentive | 68 | 0.6% | $4,391.76 | $64.58 |
| scg-internal | 66 | 0.6% | $26,821.58 | $406.39 |
| affiliate | 64 | 0.6% | $6,859.53 | $107.18 |
| omnisend | 49 | 0.5% | $17,816.89 | $363.61 |
| tsg-internal | 23 | 0.2% | $9,673.82 | $420.60 |
| chatgpt.com | 11 | 0.1% | $3,878.37 | $352.58 |

Facebook drives 22.0% of orders at an AOV 45% above the site average. Paid traffic converts to materially higher-value orders than untagged traffic.

Medium split: no medium 63.8%, cpc 27.7%, email 4.3%, affiliate 1.1%, sms 0.6%.

### Referring site

| Referrer | Orders | Share |
|---|---|---|
| pg1.performancegolf.com | 2,922 | 27.7% |
| Direct or none | 2,678 | 25.4% |
| www.google.com | 1,316 | 12.5% |
| www.performancegolf.com | 1,095 | 10.4% |
| facebook.com | 699 | 6.6% |
| instagram.com | 383 | 3.6% |
| m.facebook.com | 321 | 3.0% |
| shop.app | 214 | 2.0% |
| www.bing.com | 171 | 1.6% |
| l.facebook.com | 113 | 1.1% |

The `pg1.performancegolf.com` subdomain is the largest single referrer at 27.7%, ahead of Google and the main site. A separate PG1 funnel property is feeding more orders into the store than organic search does.

### Landing pages

| Landing path | Orders | Revenue |
|---|---|---|
| /products/rs1-putter | 2,433 | $1,040,577.03 |
| / | 1,863 | $407,513.32 |
| No landing site | 1,208 | $56,265.65 |
| /cart/clear | 1,137 | $64,485.86 |
| /pages/sf2-driver-media-info-sc | 920 | $306,784.94 |
| /pages/sf2-driver-media-product-sc | 420 | $136,333.69 |
| /collections/wedges/products/one-1-wedge | 393 | $74,268.88 |
| /pages/pg1-acc | 269 | $5,985.56 |
| /products/pg1 | 156 | $3,419.04 |
| /products/357-fairway-wood | 140 | $40,118.90 |

Two observations worth flagging. The `/cart/clear` path is the fourth-highest landing page at 1,137 orders, which is unusual for a landing destination and suggests a redirect or funnel mechanic rather than genuine entry. The two `sf2-driver-media` advertorial pages together drove 1,340 orders and $443,118.63, making that page pair the second-strongest revenue entry point after the RS1 product page.

---

## 7. Abandoned checkouts

**Reminder from the caveats: this covers only checkouts that reached email capture. Every one of the 2,224 records has an email address. This is not total cart abandonment.**

| Metric | Value |
|---|---|
| Abandoned checkouts | 2,224 |
| Total value | $608,929.46 |
| Average value | $273.80 |
| Median value | $299.65 |
| Average line items | 1.94 |
| Single-line checkouts | 646 (29.0%) |
| Contactable by email | 2,224 (100%) |
| Accepting marketing | 930 (41.8%) |
| Had a discount applied | 419 (18.8%), worth $42,107.97 |

Against 10,558 orders in the same window, email-captured checkouts abandoned at 17.4%. Read that as "of people who got far enough to give an email, 17.4% did not finish", not as a site abandonment rate.

### What is being abandoned

| Product | Units abandoned | Value |
|---|---|---|
| PG1 7-Day Trial | 1,405 | $0.00 |
| RS1 Putter | 657 | $271,743.00 |
| SF2 Driver | 467 | $139,633.00 |
| iON+ Golf Ball | 387 | $23,597.98 |
| 357 Super 7-Wood | 294 | $73,206.00 |
| Senior Swing Distance Program | 167 | $7,849.00 |
| Simple Strike Sequence | 161 | $15,617.00 |
| One Shot Slice Fix | 161 | $7,567.00 |
| ONE.1 Wedge | 124 | $18,476.00 |
| 359 Super 9-Wood | 77 | $14,553.00 |

1,561 abandoned checkouts (70.2%) contain at least one club, together worth $559,300.34. High-ticket hardware is where the abandonment value sits.

### Abandonment by value band

| Value band | Count | Share |
|---|---|---|
| $0 to $25 | 265 | 11.9% |
| $25 to $50 | 92 | 4.1% |
| $50 to $75 | 22 | 1.0% |
| $75 to $100 | 50 | 2.2% |
| $100 to $150 | 137 | 6.2% |
| $150 to $200 | 176 | 7.9% |
| $200 to $300 | 370 | 16.6% |
| $300 to $400 | 477 | 21.4% |
| $400 to $500 | 568 | 25.5% |
| $500 to $750 | 47 | 2.1% |
| $750 to $1,000 | 16 | 0.7% |
| Over $1,000 | 4 | 0.2% |

Abandoned checkouts skew higher in value than completed orders. The $300 to $500 band holds 46.9% of abandonments but only 28.2% of completed orders. Put plainly, the more expensive the basket, the more likely it stalls at checkout.

Abandonment sources: no UTM 56.8%, facebook 25.3%, Klaviyo 6.9%, microsoft 3.5%, search 2.2%.

---

## 8. Discounts

| Metric | Value |
|---|---|
| Orders with a discount | 1,910 (18.1%) |
| Total discount value | $182,429.97 |
| Discount as share of subtotal | 7.8% |
| Average discount on discounted orders | $95.51 |
| Median discount depth | 26.1% |

| Code | Orders | Revenue | AOV |
|---|---|---|---|
| BIG3VAULT | 511 | $1,122.79 | $2.20 |
| GIFT30 | 334 | $90,897.54 | $272.15 |
| INSIDER20 | 132 | $37,179.21 | $281.66 |
| PGSUPPORT10 | 89 | $30,028.23 | $337.40 |
| PGSUPPORT20 | 85 | $20,375.83 | $239.72 |
| LOVEYOURGAME15 | 30 | $9,445.19 | $314.84 |
| WELCOME30 | 22 | $5,440.38 | $247.29 |
| GOLF15 | 21 | $7,017.28 | $334.16 |
| PGSUPPORT30 | 15 | $3,338.14 | $222.54 |
| TAKE50 | 4 | $563.27 | $140.82 |

BIG3VAULT is the most-used code by a wide margin and generates almost no revenue, $2.20 per order. It bundles three digital courses (Senior Swing Distance Program, Simple Strike Sequence, One Shot Slice Fix) plus PG1 Scratch at effectively zero cost. It is a lead-generation giveaway, not a discount, and it should be excluded from any discount-effectiveness analysis or it will distort the averages badly.

The PGSUPPORT family of codes appears to be customer-service issued and carries the highest AOVs in the table.

Two codes look like test artefacts left live: KEVINTEST (2 orders, $0.00) and "feawfwf" (1 order, $0.00).

---

## 9. Timing

### Day of week

| Day | Orders | Revenue | AOV |
|---|---|---|---|
| Monday | 1,305 | $321,646.14 | $246.47 |
| Tuesday | 1,334 | $300,041.60 | $224.92 |
| Wednesday | 1,301 | $310,096.15 | $238.35 |
| Thursday | 1,431 | $346,265.74 | $241.97 |
| Friday | 1,687 | $402,214.29 | $238.42 |
| Saturday | 1,867 | $454,615.32 | $243.50 |
| Sunday | 1,633 | $379,940.61 | $232.66 |

Saturday is the strongest day on both volume and revenue. The weekend, Friday through Sunday, carries 49.1% of orders. AOV stays remarkably stable across all seven days, varying only from $224.92 to $246.47.

### Hour of day (store timezone)

Ordering runs on a broad daytime plateau. Volume climbs sharply from 07:00 (331 orders), holds nearly flat between 09:00 and 18:00 at roughly 635 to 710 orders per hour, then declines through the evening. The trough sits between 02:00 and 05:00 at 54 to 62 orders per hour. Peak hour is 10:00 with 710 orders.

### Geography

| Country | Orders | Share | Revenue | AOV |
|---|---|---|---|---|
| United States | 9,963 | 94.4% | $2,423,550.37 | $243.26 |
| Canada | 236 | 2.2% | $39,976.45 | $169.39 |
| Australia | 111 | 1.1% | $21,896.78 | $197.27 |
| United Kingdom | 90 | 0.9% | $11,851.59 | $131.68 |
| Sweden | 26 | 0.2% | $1,169.60 | $44.98 |
| Germany | 22 | 0.2% | $6,778.27 | $308.10 |
| Ireland | 22 | 0.2% | $1,179.74 | $53.62 |
| New Zealand | 10 | 0.1% | $4,800.22 | $480.02 |

Top US states by order count: Florida 938, California 851, Texas 628, New York 488, Pennsylvania 435, Ohio 397, Michigan 397, North Carolina 383, Illinois 378, New Jersey 280.

International AOV runs well below US AOV in every major market except Germany and New Zealand, both of which have sample sizes too small to be reliable.

---

## 10. Daily detail

| Date | Orders | Revenue | AOV |
|---|---|---|---|
| 2026-07-17 (partial) | 200 | $57,904.13 | $289.52 |
| 2026-07-18 | 296 | $82,026.13 | $277.12 |
| 2026-07-19 | 489 | $80,304.74 | $164.22 |
| 2026-07-20 | 314 | $77,190.22 | $245.83 |
| 2026-07-21 | 256 | $71,629.39 | $279.80 |
| 2026-07-22 | 270 | $71,086.11 | $263.28 |
| 2026-07-23 | 286 | $78,550.42 | $274.65 |
| 2026-07-24 | 324 | $85,054.96 | $262.52 |
| 2026-07-25 | 309 | $91,413.17 | $295.84 |
| 2026-07-26 | 342 | $96,634.20 | $282.56 |
| 2026-07-27 | 334 | $81,687.96 | $244.57 |
| 2026-07-28 | 318 | $86,577.30 | $272.26 |
| 2026-07-29 | 304 | $81,748.47 | $268.91 |
| 2026-07-30 | 299 | $88,552.43 | $296.16 |
| 2026-07-31 | 298 | $87,832.48 | $294.74 |
| 2026-08-01 | 363 | $113,923.28 | $313.84 |
| 2026-08-02 | 346 | $107,679.17 | $311.21 |
| 2026-08-03 | 336 | $81,242.67 | $241.79 |
| 2026-08-04 | 297 | $65,485.68 | $220.49 |
| 2026-08-05 | 339 | $82,123.76 | $242.25 |
| 2026-08-06 | 351 | $85,908.59 | $244.75 |
| 2026-08-07 | 367 | $81,744.94 | $222.74 |
| 2026-08-08 | 444 | $79,948.50 | $180.06 |
| 2026-08-09 | 309 | $72,589.91 | $234.92 |
| 2026-08-10 | 321 | $81,525.29 | $253.97 |
| 2026-08-11 | 463 | $76,349.23 | $164.90 |
| 2026-08-12 | 388 | $75,137.81 | $193.65 |
| 2026-08-13 | 495 | $93,254.30 | $188.39 |
| 2026-08-14 | 498 | $89,677.78 | $180.08 |
| 2026-08-15 | 455 | $87,304.24 | $191.88 |
| 2026-08-16 (partial) | 147 | $22,732.59 | $154.64 |

Best revenue day: 2026-08-01 at $113,923.28. Highest volume day: 2026-08-14 at 498 orders. The four highest-volume days all fall in the final week and all carry sub-$194 AOV.

### Abandoned checkouts by day

| Date | Count | Value |
|---|---|---|
| 2026-07-17 | 45 | $14,003.36 |
| 2026-07-18 | 75 | $22,211.03 |
| 2026-07-19 | 104 | $18,782.85 |
| 2026-07-20 | 64 | $19,402.54 |
| 2026-07-21 | 52 | $14,984.72 |
| 2026-07-22 | 60 | $18,254.75 |
| 2026-07-23 | 60 | $17,717.74 |
| 2026-07-24 | 60 | $20,725.15 |
| 2026-07-25 | 69 | $20,659.37 |
| 2026-07-26 | 80 | $27,113.66 |
| 2026-07-27 | 72 | $22,803.63 |
| 2026-07-28 | 73 | $22,036.97 |
| 2026-07-29 | 60 | $19,452.24 |
| 2026-07-30 | 54 | $17,639.50 |
| 2026-07-31 | 58 | $18,874.79 |
| 2026-08-01 | 67 | $20,785.83 |
| 2026-08-02 | 62 | $20,786.98 |
| 2026-08-03 | 77 | $21,368.85 |
| 2026-08-04 | 74 | $16,153.93 |
| 2026-08-05 | 68 | $13,844.05 |
| 2026-08-06 | 78 | $21,182.85 |
| 2026-08-07 | 103 | $23,646.34 |
| 2026-08-08 | 80 | $16,692.41 |
| 2026-08-09 | 64 | $20,023.27 |
| 2026-08-10 | 43 | $12,832.90 |
| 2026-08-11 | 106 | $24,188.70 |
| 2026-08-12 | 107 | $29,125.86 |
| 2026-08-13 | 101 | $24,533.70 |
| 2026-08-14 | 84 | $18,142.46 |
| 2026-08-15 | 85 | $23,748.09 |
| 2026-08-16 | 39 | $7,210.94 |

---

## 11. Catalogue reference

Modal selling price and 30-day volume for every product with recorded sales.

| Product | Price | Units | Orders |
|---|---|---|---|
| PG1 7-Day Trial (No Subscription) | $0.00 | 5,276 | 5,273 |
| RS1 Putter | $399.00 / $429.00 | 3,006 | 2,986 |
| SF2 Driver | $299.00 | 1,728 | 1,717 |
| iON+ Golf Ball | $34.99 | 1,381 | 891 |
| PG1 Scratch | $29.00 | 1,060 | 1,051 |
| PG1 Plus | $29.00 | 859 | 836 |
| 357 Super 7-Wood | $249.00 | 851 | 845 |
| ONE.1 Wedge | $149.00 | 771 | 700 |
| Senior Swing Distance Program | $47.00 | 743 | 739 |
| One Shot Slice Fix | $47.00 | 683 | 679 |
| Simple Strike Sequence | $97.00 | 547 | 543 |
| 359 Super 9-Wood | $189.00 | 397 | 395 |
| Scratch Club (14 days free, then $29/mo) | $29.00 | 206 | 206 |
| SpeedTrac | $179.00 | 164 | 163 |
| Pain-Free Distance System | $47.00 | 123 | 123 |
| SwingSmooth Pro | $62.10 | 116 | 115 |
| Pendulum Swing Sequence | $97.00 | 66 | 66 |
| DrawForce Automatic Draw Trainer | $129.00 | 46 | 46 |
| ONE.S Wedge | $129.00 | 44 | 44 |
| Kinetic Movement Method | $97.00 | 44 | 44 |
| The Click Stick | $149.00 | 41 | 41 |
| 7 Days All Access Pass To Private Lesson Library | $0.00 | 40 | 40 |
| ONE Wedge | $149.00 | 34 | 31 |
| EZ3 | $189.00 | 31 | 30 |
| PG1 Personalized Game-Improvement App | $0.00 | 30 | 30 |
| Pendulum Swing Trainer | $79.99 | 24 | 24 |
| AnyLie Hybrid | $199.00 | 16 | 14 |
| Thriver | $299.00 | 13 | 13 |
| Square Set | $99.00 | 12 | 12 |
| EZ5 | $179.00 | 11 | 11 |
| The Launch Deck | $99.00 | 11 | 11 |
| Forever Slice Fix | $47.00 | 10 | 10 |
| EZ7 | $179.00 | 10 | 10 |
| The Hinge | $159.00 | 9 | 8 |
| SQ Putter | $199.00 | 8 | 8 |
| Thriver - Steel | $199.00 | 6 | 6 |
| The StraightAway | $79.00 | 4 | 4 |
| One Swing System + PG1 ($29/mo) | $29.00 | 4 | 2 |
| VIP Coaching | $99.00 | 3 | 3 |
| SF1 + EZ7 Bundle | $379.00 | 3 | 3 |

---

## 12. Open questions this data raises

These are questions the export surfaces but cannot answer. They are the natural starting points for follow-up analysis.

1. **What drove the final week's volume spike at low value?** Order count jumped 18% week-over-week while AOV dropped 17%. Across the full four weeks, orders rose 30% and AOV fell 30% from its peak. Identifying the source would explain whether this is a healthy acquisition push or margin-eroding mix shift.
2. **Which RS1 price arm is winning?** The $399 versus $429 split is live and covers the top revenue product. Shopify cannot answer this. The experimentation tool can.
3. **Why do hardware and digital courses never sell together?** A 0.1% cross-attach rate between two catalogues serving the same golfer is either a deliberate funnel separation or a large missed opportunity.
4. **What is `/cart/clear` doing as the fourth-largest landing page?** 1,137 orders entered there. That is a funnel mechanic worth understanding before optimising it.
5. **Is channel 3890849 the Shop app?** It has the highest AOV of any channel at $318.77 and deserves a name.
6. **Why does abandonment skew so heavily to the $300 to $500 basket?** This band is 46.9% of abandonments against 28.2% of completed orders. Something at checkout is harder for expensive baskets.
7. **What explains the 7.5% RS1 refund rate?** It is the highest among high-volume products and sits on the single largest revenue line.

---

## 13. How this was produced

```bash
python3 scripts/shopify_pull.py orders 30      # 10,630 orders
python3 scripts/shopify_pull.py checkouts 30   # 2,224 abandoned checkouts
```

Raw JSON containing personally identifiable information stays local and gitignored at `data/shopify/2026-08-16-orders-30d.json` and `data/shopify/2026-08-16-checkouts-30d.json`. Every figure in this document is aggregated and contains no customer-identifying information.

A bulk customer export was attempted and deliberately not completed, since the 30-day analysis does not require customer-level records and the pull would have exported personally identifiable data unnecessarily.
