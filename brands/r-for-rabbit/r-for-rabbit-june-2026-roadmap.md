# R for Rabbit CRO Research Brief

**Data Sources:** manifest, Reviews & UGC, Meta ads visual summary, Google ads visual summary, site visual summary, PageSpeed JSON, live store fetch, competitor research

## Insights

R for Rabbit has a trust gap. Reviews from 2025-10-15 to 2026-02-10 show strong product love, with 57 five-star reviews out of 76 total reviews. Customers praise comfort, softness, safety, and range. Direct quotes include "The softest diapers ever witnessed", "diapers are very gentle and rash free", and "comfortable and last long" - Source: Reviews & UGC.

The problem is not product desire. The problem is confidence during the buying path. One-star reviews from 2025-10-15 to 2026-02-10 cite delayed delivery, no updates, wrong items, tampered products, refund delays, support disconnects, email non-response, and one alleged order-data leak - Source: Reviews & UGC.

The site also creates unnecessary doubt at the exact point customers should move forward. Product cards on homepage carousels and the All collection grid show a red liquid/template error above the outlined Add to Cart button. That error appears across Most Loved Products, Just Launched, and repeated Feather Diapers collection cards - Source: site visual summary.

Offer clarity is fragmented. Meta Ad 1 promotes NEW12, Meta Ad 2 promotes TRYSAMPLE, Meta Ad 3 promotes DPR15, Google also shows FFRIST, while the header and cart emphasize DAYONE, app savings, cashback, threshold savings, and subscription savings. The active deal changes between ad, PDP, and cart - Source: Meta ads visual summary, Google ads visual summary, PDP screenshots, cart screenshot.

Speed compounds the issue on high-intent pages. PageSpeed data from 2026-06-09 shows homepage Performance 27, LCP 26.5s, and TBT 6,030ms. Feather Diapers PDP Performance is 29, with LCP 20.0s, TBT 7,580ms, and TTI 75.1s - Source: PageSpeed JSON. Revenue potential cannot be modeled because monthly sessions and AOV are unknown.

## Slot 1: Remove Product Card Error Text

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage carousels and All collection grid (https://rforrabbit.com/)
**Revenue potential:** unknown sessions/mo x 0.2% absolute CR lift x unknown AOV = unknown monthly revenue.

**Hypothesis:** If we remove the red liquid/template error from product cards, more shoppers will continue to Add to Cart because the price and CTA zone will no longer look broken.

**Data:** Product cards on homepage carousels and the All collection grid show image, title, rating, price, then red liquid/template error text above the outlined Add to Cart button - Source: site visual summary. The error appears across Most Loved Products, Just Launched, and repeated Feather Diapers collection cards - Source: homepage screenshots, collection screenshots.

**V1:** Remove the red liquid/template error from every affected product card. Keep the existing image, title, rating, price, and outlined Add to Cart button unchanged. On mobile, keep the corrected card stack in the same vertical order. On desktop, keep the existing grid and carousel layout with the error space collapsed.

## Slot 2: Unify First-Order Offer Messaging

**Type:** A/B test (1 variation vs. control)
**Page:** Paid ad landing path, PDP, and cart (https://rforrabbit.com/)
**Revenue potential:** unknown sessions/mo x 0.2% absolute CR lift x unknown AOV = unknown monthly revenue.

**Hypothesis:** If the same first-order offer is carried from ad landing experience to PDP to cart, more shoppers will reach checkout because they will not need to reconcile competing coupon codes.

**Data:** Meta Ad 1 promotes NEW12, Meta Ad 2 promotes TRYSAMPLE, Meta Ad 3 promotes DPR15, and Google also shows FFRIST, while cart says Use Coupon: DAYONE - Source: Meta ads visual summary, Google ads visual summary, cart screenshot. PDP cards show DPR15 and DAYONE, so the active deal changes between PDP and cart - Source: PDP screenshots.

**V1:** Use the cart's DAYONE offer as the persistent first-order offer across the tested path. On mobile and desktop PDP views, show DAYONE as the active first-order offer in the existing offer area and remove competing first-order code emphasis from the same page state. In cart, keep Use Coupon: DAYONE as the visible continuation of the same offer.

## Slot 3: Simplify Feather Diapers Buy Box

**Type:** A/B test (1 variation vs. control)
**Page:** Feather Diapers PDP (https://rforrabbit.com/)
**Revenue potential:** unknown sessions/mo x 0.2% absolute CR lift x unknown AOV = unknown monthly revenue.

**Hypothesis:** If the Feather Diapers buy box brings proof closer to the price and Add to Cart decision, more shoppers will add to cart because comfort and safety claims will be visible before the offer stack creates friction.

**Data:** The Feather Diapers PDP first fold shows title, 4.7 | 939, SKU, INR394, app savings, cashback, style selector, size guide, size dropdown, pack dropdown, subscription vs one-time options, and Add To Cart - Source: PDP screenshots. Testing badges, UGC, FAQ, reviews, and video sit below offers and bundles, while reviews from 2025-10-15 to 2026-02-10 praise softness and comfort - Source: reviews, PDP screenshots.

**V1:** Move the existing comfort and safety proof from below the offer and bundle area into the buy box near the 4.7 | 939 rating and price. Keep the existing selectors, subscription vs one-time options, and Add To Cart controls unchanged. On mobile, place the proof directly above the style selector. On desktop, place it beside the rating and price within the existing first-fold buy box.

## Future Slot Candidates

1. **Add delivery and return confidence near checkout** - Cart has coupon, threshold, app download, line item, pincode, total, and checkout controls, but no visible reassurance for delayed, wrong, tampered, or damaged orders.
2. **Make cart savings feel earned** - Cart shows Add INR1106 more to save INR100, app savings, coupon input, and You are saving INR0, which weakens the savings moment.
