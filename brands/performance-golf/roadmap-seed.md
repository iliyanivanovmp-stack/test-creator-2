# Performance Golf Roadmap Seed

**Store:** https://shop.performancegolf.com/
**AOV:** $238.19 gross / $220.93 merchandise-only (30-day Shopify data)
**Monthly sessions:** unknown (no GA/Clarity data collected)
**Data sources:** Meta Ads and landing pages, Google Ads Transparency, Reviews (357 Super 7-Wood only, Amazon), PageSpeed/Core Web Vitals (Lighthouse, mobile), Current site screenshots, 30-day Shopify business summary

## Key Insights

Mobile performance is failing sitewide: both homepage and PDP score ~20/100 on Lighthouse mobile, with CLS at 0.637-0.638 (over 6x Google's "good" threshold of 0.1) and time-to-interactive above 43 seconds on both pages. This overlaps directly with the buy box on the 357 PDP, where variant selectors and a sticky Add-to-Cart bar likely shift position during load — a technical issue sitting on top of the funnel step that matters most.

The 30-day Shopify pull (10,558 orders, $2.51M gross revenue, window 2026-07-17 to 2026-08-16) surfaces a volume-up/value-down trend: orders climbed 30% week-over-week across the window while AOV fell 30% from its peak ($282.09 to $196.60), with revenue flat around $555k-$637k/week. Catalogue concentration is extreme — RS1 Putter alone is 49.4% of gross revenue, and RS1 + SF2 Driver together are 70.0% — yet neither product has visible on-site review data (the only review source collected was Amazon reviews for the lower-revenue 357 Super 7-Wood). Cross-sell is nearly absent: only 6.0% of club orders contain 2+ clubs despite those orders averaging $556.69 vs. $346.03 for single-club orders (a $210.66 gap), and hardware/digital-course cross-attach sits at 0.1%. The cart drawer's "YOU MAY ALSO LIKE" module was captured empty in the site screenshot, directly consistent with this gap.

Message match between paid ads and landing pages shows two concrete gaps: Meta Ad 1 leads with a senior-specific angle ("THE ONLY FAIRWAY WOOD FOR GOLFERS OVER 55") that disappears from the landing page's first three folds, and Ad 3 promises "$100 OFF" on the creative with no matching callout on the shared SF2 landing page. Facebook-attributed orders carry a $346.06 AOV, 45% above the site average, so protecting and improving this channel's landing experience carries outsized weight.

## Top Test Opportunities

### 1. Fix PDP layout shift and mobile load speed on club product pages
**What's broken:** On the 357 Super 7-Wood PDP (and by extension other club PDPs sharing the same template), the buy box sits at the top: product title, price with "17% OFF" badge, star rating ("4.8 based on 3,700+ happy reviews"), hand/shaft-flex variant toggles, and a full-width orange "ADD TO CART" button. By fold 3, a second sticky bottom bar appears showing the product name, price, and a collapsed "ADD TO CART" with expand chevron. Lighthouse mobile audit measured CLS of 0.637 on this exact page (Google's "good" threshold is 0.1) — consistent with the variant selectors and/or the appearance of the sticky bar shifting layout after initial paint. Time-to-interactive is 43.4 seconds; total blocking time is 1,780ms.
**Evidence:** raw/pagespeed.md (Lighthouse JSON), raw/site-visual-summary.md (PDP fold detail)
**Key data:** Performance score 21/100 mobile; LCP 4.6s; CLS 0.637; TBT 1,780ms; TTI 43.4s
**Est. lift:** 1% CR lift x ~10,500 orders/mo x $238 AOV ≈ $25,000/mo (conservative; no session baseline available)

### 2. Populate the cart drawer cross-sell module
**What's broken:** The cart drawer is a right-side slide-out, header "CART (2)," with a free-shipping progress banner at top and two line items shown (product + the free PG1 trial bundled in). Below the line items sits a "YOU MAY ALSO LIKE" section header with no products rendered underneath it in the captured screenshot — an empty merchandising slot on every cart open.
**Evidence:** raw/site-visual-summary.md (cart drawer), raw/context.md (30-day data)
**Key data:** Multi-club orders average $556.69 vs. $346.03 single-club ($210.66 gap); only 6.0% of club orders (382 of 6,409) contain 2+ clubs
**Est. lift:** Converting 2% of single-club orders (~6,027/mo) to multi-club at the existing gap ≈ $25,400/mo

### 3. Restore senior-specific messaging on the 357 Fairway Wood landing page
**What's broken:** Meta Ad 1's creative headline is "THE ONLY FAIRWAY WOOD FOR GOLFERS OVER 55" with subtext "A Brand New Concept of Club Designed For Seniors." The landing page (performancegolf.com/357-fairway/media/hybrid-sc) that this ad links to opens instead with "THE FIRST-EVER SUPER 7-WOOD WITH TRI-FUSION TECHNOLOGY!" — a technology-first headline with no age-specific framing across the first three folds (top bar, hero video, and the "Tri Fusion" benefit sections that follow).
**Evidence:** raw/meta-ads-visual-summary.md, WebFetch of live landing page
**Key data:** Ad 1 drives to a page with 4.8 rating / 3,300+ reviews cited; 357 product does 845 orders/mo per catalogue data
**Est. lift:** 0.5% CR lift x 851 orders/mo x $249 AOV ≈ $1,050/mo direct (likely understates paid-media efficiency impact)

### 4. Add on-site review display to RS1 Putter and SF2 Driver PDPs
**What's broken:** Neither of the two highest-revenue products has visible on-site review collection. The SF2 Driver landing page cites "76,744 Happy Golfers" as a stat callout but no star-rating widget or review list appears in the captured folds; the RS1 Putter PDP was not separately captured but the collection page shows no rating badge on its card, unlike the 357 (which does show "4.8 based on 3,700+ happy reviews" directly in its buy box).
**Evidence:** raw/reviews.md (scope gap — only 357 reviews collected), raw/meta-ads-visual-summary.md
**Key data:** RS1 + SF2 = 70.0% of gross revenue ($1,759,648.30 combined); zero on-site review proof captured for either
**Est. lift:** 0.5% CR lift x (2,986+1,717) orders/mo x ~$350 avg AOV ≈ $8,200/mo

### 5. Resolve the "$100 OFF" message-match gap on the shared SF2 landing page
**What's broken:** Ad 3's creative shows the SF2 driver against a red radial background with the text "SF2 DRIVER — CLAIM YOUR $100 OFF." Ad 3 shares its landing page with Ad 2 (shop.performancegolf.com/pages/sf2-driver-media-info-sc), and the three captured folds of that shared page show sale pricing ($299, marked down from $399) but no explicit "$100 off" badge or callout matching the ad's specific claim.
**Evidence:** raw/meta-ads-visual-summary.md
**Key data:** Ad 2+3 shared landing page drove 920 orders / $306,784.94 revenue in the 30-day window (landing-page data)
**Est. lift:** Not independently quantifiable from available data; primary value is reducing ad-platform/compliance risk and improving click-to-page trust, not a standalone CR lift

### 6. Add a discount badge to the RS1 Putter collection card
**What's broken:** On the "GOLF CLUBS" collection page, product cards display in a 3-column grid with a "Save up to X%" badge in the top-left corner of most cards (357 Super 7-Wood shows "Save up to 17%," SF2 Driver "Save up to 25%," ONE.1 Wedge "Save up to 25%"). The RS1 Putter card is the exception: it shows only "From $399.00" with no strikethrough price or savings badge, making the top-revenue product visually appear as the one item on the grid without an active offer.
**Evidence:** raw/site-visual-summary.md (collection page)
**Key data:** RS1 Putter = 49.4% of gross revenue ($1,242,986.10); 2,986 orders/mo
**Est. lift:** 0.3% CR lift x 2,986 orders/mo x $414 avg RS1 price ≈ $3,700/mo

### 7. Match homepage hero to ad-driven pricing/urgency expectations
**What's broken:** The homepage hero shows a full-bleed putter image with headline "YOUR STROKE ISN'T THE PROBLEM. YOUR PUTTER IS." and a single CTA "SEE HOW IT WORKS," with no price, discount, or urgency element visible in fold 1. This contrasts with every Meta ad landing page collected, which leads with strikethrough pricing and urgency copy (e.g., "Summer Sale Ends Soon! Save 50%"). A visitor who clicked a sale-driven ad, didn't convert, and returns to the homepage organically encounters a colder, unmatched experience with no continuation of the offer.
**Evidence:** raw/site-visual-summary.md (homepage), WebFetch of live homepage, raw/meta-ads-visual-summary.md
**Key data:** Homepage is the 2nd-largest landing page (1,863 orders, $407,513.32) per 30-day data
**Est. lift:** Not independently quantifiable — no session-level or returning-visitor data available to isolate this segment

### 8. Introduce a multi-club bundle option directly on club PDPs
**What's broken:** The 357 Super 7-Wood PDP buy box offers only Hand and Shaft Flex variant selectors with a single one-time-purchase "ADD TO CART" button — no bundle, multi-club, or subscription option is shown anywhere in the three captured folds. This is the PDP-level version of the cart cross-sell gap (Opportunity 2): the same $210.66 AOV lift from multi-club orders is unaddressed at the point of first product selection, not just at cart.
**Evidence:** raw/site-visual-summary.md (PDP buy box detail), raw/context.md
**Key data:** Same underlying data as Opportunity 2 ($210.66 AOV gap, 6.0% multi-club attach rate)
**Est. lift:** Kept as backup/PDP-level variant of Opportunity 2 — do not run both simultaneously, as they compete for the same mechanic

## Unused Findings

- A live, unlabeled 50/50 price test appears to already be running on the RS1 Putter ($399 vs. $429, near-even split across all 31 days) — confirm this isn't still active before proposing any new RS1 pricing test.
- The `/cart/clear` URL is the 4th-largest landing page (1,137 orders) — an unusual redirect/funnel mechanic worth investigating separately from this roadmap.
- No competitor pricing or positioning data was collected for this engagement (skipped per manifest) — a competitive audit could sharpen future PDP and pricing tests.
