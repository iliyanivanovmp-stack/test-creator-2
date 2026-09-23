# SVIBE October 2026 HTML production notes

Internal companion to `svibe-october-2026-roadmap.html`. Prepared 23 September 2026. No storefront changes were made.

## Inputs and design

Used the sole October roadmap, `svibe-research-audit.md`, the user-provided saved homepage, supplied transparent logo, and all 24 collected screenshot references. No launch dates requested or displayed. Month taken from the roadmap filename because its H1 has no month.

Hero candidates visually inspected: live Open Graph `SVibe_Logo.png` (logo, not a useful hero); wide `slider-desktop.png` (selected); portrait `slider01_f4af6b15-c233-4109-a925-368316884ddf.png` (mobile art direction); `IMG_9531.jpg` (less representative product framing); homepage screenshot (fallback). The wide campaign asset preserves the whole Curve silhouette without baked-in text. Desktop image frame is 2:1 at 50%/50%; mobile uses the matching portrait campaign at 50%/8%. Assets are embedded so the deliverable has no local dependencies. Fonts are Google Fonts Bodoni Moda and DM Sans. Brand cues: serif display headings, plum controls, cream/lilac surfaces, transparent original logo, authentic product photography.

## Live verification and corrections

The following pages were reopened in Chromium and/or fetched directly during production:

- https://svibe.com/
- https://svibe.com/products/female-vibrator-curve-svibe
- https://svibe.com/products/svibe-snail-jovi-couples-ring
- https://svibe.com/products/snail-jovi-arc
- https://svibe.com/pages/return-and-refund-policy

Currency shown was USD. A Bulgaria/EUR location suggestion was dismissed without changing the market. Product JSON verified Curve at $149, Jovi at $69, Arc at $89. Curve Pink/Peach/Black/Purple were available; Jovi default available; Arc Blue Haze and Nior Haze available. Default Curve was Pink and Arc Blue Haze. Curve shows 4.8 / 321 reviews and the four documented badges. Gallery imagery can show purple while Pink is selected; mockups preserve the documented imagery and do not imply the pictured gallery color is the selected SKU.

1. **Slot 1: captured landing page, not a verified current state.** Exact URL was absent from the supplied evidence. Searched the live sitemap and inspected `/pages/landing-jovi-09`, `/pages/why-couples-are-switching`, and `/pages/thousands-of-couples-are-replacing-their-bullet-vibes`. None reproduced the captured Reconnect page. Therefore the card says Audit capture / URL unverified, has no guessed canonical link, and explicitly requires the exact URL or confirmation of ads-only/unpublished status. Neither of those statuses is known. Both the block proposal and its feature wording remain audit-sourced only until the control is checked. Jovi product and price were verified separately. The two-motor/remote proposal follows roadmap line 23; product-feature wording still needs confirmation before implementation.
2. **Slots 2 and 3: measurements are historical, targets are not results.** Retained 13.5s/10.2s from audit lines 61-62 with 23 Sep 2026 and not-rerun labels. Used the under-2.5s target from roadmap lines 34 and 45, rather than the conflicting under-4s headings. No claim about the exact LCP element, site-wide slowest page, conversion lift, or confirmed improvement is made.
3. **Slot 4: do not publish a blanket 30-day return promise.** The live policy states a two-year warranty, a 14-day eligible-return window for unused/unopened sealed items in UK/EU, and no returns outside UK/EU. The source's proposed 30 Day Returns badge is inconsistent with that policy. Replaced it with a two-year warranty and View returns policy link concept. The existing Curve 03 Warranty accordion remains below Add to Cart and expands to product-manual languages. Slot 4 now explicitly shows this wrong body and makes correcting it, or linking to the actual warranty terms, a prerequisite to surfacing the two-year warranty beside purchase actions.
4. **Cart verified with an actual buyable SKU.** Added one Pink Curve, reloaded, opened the cart drawer. Observed Curve $149 vs $239, free gift The 20 Gateways to Orgasm $0 vs $40, two line items, free shipping unlocked against $129 threshold, savings $130, subtotal/checkout $149, unchecked Order Protect $3.95 and free Extra Discreet Packaging. The gift countdown read 9:57 at capture. No warranty/returns line was visible. No checkout or order was submitted. The concept preserves these meaningful cart details and adds the reassurance module.
5. **Slot 5: conditional copy, not an invented favorable claim.** The live Whisper quiet badge remains. Expanded specifications say Reassuringly quiet, less than 40db; that is storefront copy, not a new measurement. The proposal is explicitly conditional on checking current production units.
6. **Slot 6: avoid an unsupported site-wide absence claim.** Inspected How to use, Specifications, and Warranty accordions. The copy refers to the captured details section and reviewer feedback, not an assertion that no guidance exists anywhere. Proposed care wording is from roadmap line 80 and must be checked against the product manual before implementation.
7. **Slot 7: mobile-only sticky cart confirmed.** Fresh Chromium shopper-scroll checks at 1440x900 and 390x900, at scroll positions 0, 1200, 2400 and 4000: desktop `.pdc__sticky.is-on` remains `display:none` with zero-size bounds. Mobile changes from translated offscreen at the top to `display:flex`, transform zero, x=0/y=835/width=390/height=65 after scrolling, with SNAIL CURVE, $149.00, $239.00 and ADD TO CART. This confirms mobile-visible/desktop-hidden behavior in the checked session, not a broken scroll trigger. It does not establish whether desktop hiding is intended. The earlier unqualified page-wide claim was too broad. Reframed as a device-specific existing-feature review with desktop intent to confirm and no duplicate bar proposed.
8. **Slot 8: unsupported feature attribution removed.** Roadmap line 99 asserts that Jovi's two-motor feature belongs to Arc, but the supplied Arc screenshot summary itself says 1 Powerful Motor. Do not repeat this as a proven product-mapping error. Retained the source-backed naming overlap and distinct prices as a review opportunity. Jovi / Arc are clearly marked working names, not live or final names.

## Claim and visual source map

| Slot | Roadmap lines | Audit lines | Visual reference | Composition and preserved cues |
|---|---|---|---|---|
| 1 | 19-23 | 25 | ad3-landing-f1/f2/f3; public Jovi photo | Captured/variation; cream hero, serif Reconnect headline, couple photo, plum CTA; new product block |
| 2 | 30-34 | 57-64, 105 | pdp-f1; live Curve | Measurement/target and full PDP; gallery, swatches, serif title, review count, plum purchase button |
| 3 | 41-45 | 61, 101 | homepage-f1; campaign originals | Wide first fold and time target; campaign image, shipping strip, logo, Shop Now |
| 4 | 53-57 | 105, 107 | pdp-f1; cart-drawer; live cart | Purchase journey; pink line item, gift, shipping, extras, savings, checkout, added warranty module |
| 5 | 64-68 | 47, 51, 105 | pdp-f1; reviews | Enlarged claim/feedback/guidance sequence; gallery, title, rating, badge context |
| 6 | 76-80 | 44-46, 52 | pdp-f3; live details asset | Existing five features and enlarged sixth; cream/lilac, numbered cards, serif labels, authentic lifestyle image |
| 7 | 88-92, superseded by live evidence above | original screenshots only | pdp-f2/f3; live fixed control | Existing scrolled experience; UGC, Real homes real views, details, product thumbnail, plum CTA |
| 8 | 99-103, qualified as above | 25 | homepage-f1, collections-f1, live Jovi/Arc | Current/working naming; hand-held product assets, serif names, category and distinct prices |

Data Insights bullet provenance: source list audit lines 5-11; paid-social 21/23/25; Google 31/33; reviews 38/39/41/44-47; performance 57-64; screenshots 101/103/105/107; community 94/95/97; competitors 72-76; cross-source themes 111-115. The Curve 321-review figure also appears in the supplied site evidence. Data Insights describes the dated audit, not a newly rerun research report. No external case-study uplift figure is carried forward.

## Rendered QA

Rendered all eight cards and both tabs at 1440x950 and 390x844. Checked each desktop and mobile composition visually, including hero. All images loaded, tab switching worked without JavaScript, no page horizontal overflow, no SVG text outside its viewport. Complete Tests and Data Insights pages rendered. Output is an ASCII-only Shopify fragment with scoped styles, embedded imagery, separate mobile SVGs, print styling, and no launch dates or scripts.

Two weakest first-pass concepts improved: slot 3 had letterboxing and white copy over white space, corrected with proper desktop aspect ratio and dedicated mobile image crop plus the original shipping strip; slot 7's CTA was too small, enlarged while preserving its live anatomy. Also fixed checkout text wrapping and enriched slot 4 with the verified gift, savings, and checkboxes. Re-rendered after changes.

Desktop scores (1-5): source resemblance / brand cues / asset fidelity / change clarity / readability / composition distinctness.

| Slot | Scores |
|---|---|
| 1 | 4 / 5 / 5 / 5 / 4 / 4 |
| 2 | 4 / 5 / 5 / 5 / 5 / 4 |
| 3 | 5 / 5 / 5 / 5 / 5 / 5 |
| 4 | 4 / 5 / 5 / 5 / 4 / 5 |
| 5 | 4 / 5 / 5 / 5 / 5 / 5 |
| 6 | 4 / 5 / 5 / 5 / 5 / 5 |
| 7 | 4 / 5 / 5 / 5 / 4 / 5 |
| 8 | 4 / 5 / 5 / 5 / 5 / 4 |

Limitations retained visibly: captured landing URL unverified; performance not rerun; noise and care copy require product validation; naming direction is provisional. No live Shopify publishing was requested or performed.

## Follow-up drift corrections

Slots 01, 04 and 07 revised in response to user review. No live store content was edited. Slot 04 illustrates correcting/linking the accordion rather than claiming the store fix has been made. Slot 07 explicitly distinguishes mobile from desktop and does not infer product intent from shipped scripts. Complete desktop/mobile render checks repeated after the revisions.
