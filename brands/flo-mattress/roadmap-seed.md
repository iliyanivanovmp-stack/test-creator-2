# Flo Mattress Roadmap Seed

**Store:** https://www.flomattress.com/
**AOV:** unknown
**Monthly sessions:** unknown
**Data sources:** manifest; Meta and Google ads; 89 Amazon reviews dated June 22, 2024–July 5, 2026; July 14, 2026 mobile Lighthouse; site screenshots; live homepage; official Wakefit, SleepyCat, and The Sleep Company pages

## Key Insights

All three Meta ads and all brand traffic land on one homepage. Its discount/refund hero omits the ads' celebrity, 95% five-star, doctor, and vacuum-packed proof. “10,00,000+ customers” appears much later, while the PDP displays 21,984 reviews.

The 89-review sample is 88.8% four or five stars, led by comfort, value, and support. Orthopedic outcomes conflict: “significant relief from the back pain issue” versus “made my back pain worse.” Complaints include cover failure, bulging, aloe scent, 22-day delivery, and a pickup unresolved for 15 days.

July 14 mobile Lighthouse scored home 48 and PDP 49. LCP was 6.5/7.4 s and payload 4,591/5,798 KiB; PDP TTI was 28.9 s. AOV, sessions, baseline CR, desktop and field CWV are missing, so revenue impact is unquantified.

## Top Test Opportunities

### 1. Ad-Specific Homepage Landing States
**What's broken:** Every ad opens the same bedroom hero with discount, refund headline, ₹9-per-night line, and orange CTA. Celebrity, review, orthopedic, doctor, latex, cooling, and boxed-delivery proof is absent beside it.
**Evidence:** Meta ads, Google ads, manifest, homepage.
**Key data:** Three Meta ads share one URL; 18 Google cards add orthopedic and doctor angles.
**Est. lift:** +4% relative CR × unknown sessions/mo × unknown AOV = unquantified.

### 2. Above-the-Fold Mattress Finder
**What's broken:** The generic hero CTA precedes five options, forcing visitors to translate soft, hard, latex, spring, and acupressure positioning themselves.
**Evidence:** Homepage, collection, reviews, competitors.
**Key data:** Five options; reviews conflict on firmness and back-pain outcomes.
**Est. lift:** +3% relative CR × unknown sessions/mo × unknown AOV = unquantified.

### 3. Five-Mattress Comparison Cards
**What's broken:** Two-column collection cards show imagery, one-line copy, starting price, discount, and CTA, but no firmness, material, sleeper fit, cooling, rating, or comparison.
**Evidence:** Collection screenshots, reviews, competitor pages.
**Key data:** The collection is only two folds and five products.
**Est. lift:** +3% relative CR × unknown sessions/mo × unknown AOV = unquantified.

### 4. Mobile Critical-Path Performance
**What's broken:** Oversized payloads and scripts delay content; homepage GIFs and duplicated marketing scripts are major flagged waste.
**Evidence:** July 14, 2026 Lighthouse reports.
**Key data:** Home/PDP scores 48/49; LCP 6.5/7.4 s; payloads 4,591/5,798 KiB.
**Est. lift:** +3% relative CR × unknown sessions/mo × unknown AOV = unquantified.

### 5. Persistent PDP Purchase Bar
**What's broken:** The right buy box stacks price, timer, delivery, EMI, help, color, size, units, dimensions, thickness, and quantity; Add to Cart first appears in Fold 2.
**Evidence:** PDP screenshots.
**Key data:** Captured configuration ₹6,392.85; mobile sticky state was not collected.
**Est. lift:** +2% relative CR × unknown sessions/mo × unknown AOV = unquantified.

### 6. PDP Firmness and Suitability Calibration
**What's broken:** Ergo is preselected beside an Ortho switch and 21,984 reviews, but no visual maps sleep position, body needs, firmness, and expected outcome.
**Evidence:** PDP, reviews, Google ads.
**Key data:** Review outcomes range from “excellent back support” to “made my back pain worse.”
**Est. lift:** +2% relative CR × unknown sessions/mo × unknown AOV = unquantified.

### 7. Progressive Size Configuration
**What's broken:** Color, standard/custom mode, units, dimensions, thickness, quantity, and measurement help form one long pre-purchase sequence.
**Evidence:** PDP screenshots, review size issues.
**Key data:** One buyer reported a size issue; custom sizing is supported.
**Est. lift:** +2% relative CR × unknown sessions/mo × unknown AOV = unquantified.

### 8. One-Click Cart Protector Add-On
**What's broken:** The protector recommendation requires size choice without visibly confirming compatibility with the mattress above.
**Evidence:** Cart screenshot.
**Key data:** The drawer already knows the mattress dimensions, thickness, color, and size.
**Est. lift:** +4% relative checkout AOV × unknown checkouts/mo × unknown AOV = unquantified.

### 9. Collapsed Promo-Code Entry
**What's broken:** An open promo field precedes recommendations and checkout, inviting code hunting despite displayed savings.
**Evidence:** Cart screenshot.
**Key data:** No free-shipping threshold is shown; checkout reassurance covers delivery, trial, and EMI.
**Est. lift:** +1% relative checkout CR × unknown checkouts/mo × unknown AOV = unquantified.

### 10. Add-All Frequently Bought Together Bundle
**What's broken:** Two pillows and a protector use separate selectors, quantities, prices, and Add to Cart buttons instead of one bundle action.
**Evidence:** PDP Fold 3 screenshot.
**Key data:** Three accessories require three independent decisions.
**Est. lift:** +5% relative PDP AOV × unknown PDP orders/mo × unknown AOV = unquantified.

## Unused Findings

- The live July 14 announcement said a Prime Day sale was extended until July 10, while the screenshot showed a Monsoon Sale ending July 14.
- Marketplace reviews report 22-day delivery and a 15-day unresolved pickup against the live site's 14-day delivery promise.
