# Performance Golf CRO Research Brief

**Data Sources:** Meta Ads and landing pages, Google Ads Transparency, Reviews (357 Super 7-Wood only, Amazon), PageSpeed/Core Web Vitals (Lighthouse, mobile), Current site screenshots, 30-day Shopify business summary

## Insights

Mobile performance is failing sitewide. Homepage and PDP both score ~20/100 on Lighthouse mobile (pulled 2026-08-16), with CLS at 0.637-0.638, more than 6x over Google's "good" threshold of 0.1, and time-to-interactive above 43 seconds on both pages. On the 357 PDP this overlaps directly with the buy box, where variant selectors and a sticky Add-to-Cart bar likely shift position during load. Every paid-traffic mobile session hits this before a shopper can act. Source: PageSpeed/Core Web Vitals.

The 30-day Shopify pull (10,558 orders, $2.51M gross revenue, 2026-07-17 to 2026-08-16) shows a volume-up, value-down trend: orders climbed 30% week-over-week while AOV fell 30% from its peak, $282.09 to $196.60. Revenue stayed flat. Catalogue concentration is extreme: RS1 Putter alone is 49.4% of gross revenue, and RS1 + SF2 Driver together are 70.0%, yet neither has visible on-site review proof. Source: 30-day business summary, Reviews.

Cross-sell is nearly absent. Only 6.0% of club orders contain 2+ clubs, despite those orders averaging $556.69 versus $346.03 for single-club orders, a $210.66 gap. The cart drawer's "YOU MAY ALSO LIKE" module was captured empty. Source: 30-day business summary, Site screenshots.

Message match between paid ads and landing pages breaks in two places. Meta Ad 1 leads with "THE ONLY FAIRWAY WOOD FOR GOLFERS OVER 55," and that framing disappears from the 357 landing page's first three folds. Ad 3 promises "$100 OFF" with no matching callout on the shared SF2 landing page. Facebook-attributed orders carry a $346.06 AOV, 45% above the site average, so protecting this channel's landing experience matters more than its order share alone suggests. Source: Meta Ads and landing pages.

Fixing PDP mobile performance, homepage mobile performance, and the cart cross-sell gap alone represents a conservative $25,000/mo + $4,400/mo + $25,400/mo = roughly $54,800/mo in combined opportunity, before accounting for the message-match and trust-signal fixes below.

## Slot 1: Fix Mobile Layout Shift and Load Speed on Club PDPs

**Type:** Immediate Fix
**Page:** Product Detail Pages, all club templates (e.g. 357 Super 7-Wood: shop.performancegolf.com)

**What's broken:** Lighthouse mobile audit measured a Performance score of 21/100 on the 357 PDP, with CLS at 0.637 (6x over Google's 0.1 "good" threshold), LCP at 4.6s, total blocking time at 1,780ms, and time-to-interactive at 43.4s. The buy box sits at the top of the page: title, price with "17% OFF" badge, star rating, hand/shaft-flex variant toggles, and a full-width "ADD TO CART" button. A second sticky bottom bar with a collapsed "ADD TO CART" appears once the shopper scrolls to fold 3. The CLS score is consistent with these variant selectors and the sticky bar shifting position after initial paint, which both frustrates shoppers on mobile and directly costs Core Web Vitals ranking signal.

**Why this is urgent:** This isn't a design hypothesis to test, it's a broken load experience sitting on top of the highest-value step in the funnel. Facebook-attributed traffic, the largest paid source, converts at a $346.06 AOV, 45% above site average, and all of it lands on mobile pages scoring 21/100.

**Fix:** Diagnose and eliminate the render-blocking JS and late-loading elements causing the buy box (variant selectors, sticky Add-to-Cart bar) to shift after paint. Reserve layout space for these elements before they render so CLS drops toward the 0.1 threshold, and reduce total blocking time to cut time-to-interactive well below the current 43.4s. Applies to all club PDPs sharing this template.

**Revenue potential:** 1% CR lift x ~10,500 orders/mo x $238 AOV ≈ $25,000/mo (conservative; no session baseline available).

## Slot 2: Fix Mobile Layout Shift and Load Speed on Homepage

**Type:** Immediate Fix
**Page:** Homepage (shop.performancegolf.com)

**What's broken:** Lighthouse mobile audit measured a Performance score of 20/100 on the homepage, with CLS at 0.638, LCP at 5.6s, total blocking time at 1,100ms, and time-to-interactive at 46.2s, the worst of the two pages tested. The homepage hero, trust-signal row, and technology explainer sections all load into this same environment.

**Why this is urgent:** The homepage is the second-largest landing page by order volume (1,863 orders, $407,513.32 in the 30-day window). A shopper who clicks from an ad and later returns organically to the homepage hits nearly a 30-second-longer load-to-interactive experience than industry norms before any content is usable.

**Fix:** Same remediation as Slot 1, applied to homepage template: reserve layout space for elements that load late, cut render-blocking JS, and bring CLS toward the 0.1 threshold. Investigate whether the two pages share a common cause (e.g. the same app or script) so both fixes can ship together.

**Revenue potential:** 1% CR lift x 1,863 orders/mo x $238 AOV ≈ $4,400/mo (conservative; scoped to homepage landing-page order volume).

## Slot 3: Populate the Cart Drawer Cross-Sell Module

**Type:** A/B test (1 variation vs. control)
**Page:** Cart drawer (site-wide)

**Revenue potential:** 6,027 single-club orders/mo x 2% conversion to multi-club x $210.66 AOV gap ≈ $25,400/mo.

**Hypothesis:** If we populate the cart drawer's empty "YOU MAY ALSO LIKE" module with a second club, multi-club attach rate will rise because multi-club orders already average $210.66 more than single-club orders, the demand exists, it's just not being surfaced at the moment of purchase.

**Data:** The cart drawer is a right-side slide-out with a free-shipping progress banner and line items, but the "YOU MAY ALSO LIKE" section header renders with no products underneath it on every cart open (Source: Site screenshots). Multi-club orders average $556.69 versus $346.03 for single-club orders, and only 6.0% of club orders (382 of 6,409) contain 2+ clubs (Source: 30-day business summary).

**V1:** Populate the "YOU MAY ALSO LIKE" module with a complementary club recommendation (e.g. a driver or wood shown alongside a putter in cart), keeping the existing free-shipping banner and line-item layout unchanged. Mobile: module appears directly below the line items in the slide-out drawer, one product card wide. Desktop: same position, module can show up to 2 product cards side by side within the drawer width. Control: current empty module.

## Slot 4: Restore Senior-Specific Messaging on the 357 Fairway Wood Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** 357 Fairway/Hybrid landing page (performancegolf.com/357-fairway/media/hybrid-sc)

**Revenue potential:** 0.5% CR lift x 851 orders/mo x $249 AOV ≈ $1,050/mo direct (likely understates paid-media efficiency impact).

**Hypothesis:** If we reintroduce the senior-specific framing from Meta Ad 1 into the landing page's first fold, conversion rate will improve because shoppers who click an age-specific promise currently land on generic technology messaging with no reinforcement of "over 55" until deeper in the page, a message-match gap between ad and page.

**Data:** Meta Ad 1's creative headline is "THE ONLY FAIRWAY WOOD FOR GOLFERS OVER 55," with subtext "A Brand New Concept of Club Designed For Seniors." The landing page instead opens with "THE FIRST-EVER SUPER 7-WOOD WITH TRI-FUSION TECHNOLOGY," a technology-first headline with no age-specific framing across the top bar, hero video, or the Tri-Fusion benefit sections that follow (Source: Meta Ads and landing pages).

**V1:** Add the "GOLFERS OVER 55" framing to the hero fold, either as a headline addition or a subheadline directly under the existing Tri-Fusion headline, keeping the current hero video and Tri-Fusion technology claim intact. Mobile: senior framing appears as a short subheadline above the fold, before any scroll. Desktop: senior framing appears alongside the hero video in the same fold. Control: current Tri-Fusion-only headline.

## Slot 5: Add On-Site Review Display to RS1 Putter and SF2 Driver PDPs

**Type:** A/B test (1 variation vs. control)
**Page:** RS1 Putter and SF2 Driver Product Detail Pages

**Revenue potential:** 0.5% CR lift x 4,703 orders/mo (2,986 RS1 + 1,717 SF2) x ~$350 AOV ≈ $8,200/mo.

**Hypothesis:** If we add an on-site star-rating and review widget to the RS1 and SF2 buy boxes, conversion rate will improve because these two products drive 70.0% of gross revenue but show zero visible review proof, while the lower-revenue 357 PDP already displays "4.8 based on 3,700+ happy reviews" directly in its buy box.

**Data:** RS1 + SF2 combined are 70.0% of gross revenue ($1,759,648.30) with no on-site review widget captured for either (Source: 30-day business summary, Reviews). The SF2 landing page cites "76,744 Happy Golfers" as a stat callout but shows no star-rating widget or review list in the captured folds (Source: Meta Ads and landing pages).

**V1:** Add a star-rating badge and review count near the price in the buy box, matching the placement already used on the 357 PDP ("4.8 based on 3,700+ happy reviews"), for both RS1 and SF2 PDPs. Mobile: badge sits directly under the product title, above the price. Desktop: same position, inline with the title row. Control: current buy box with no rating display.

## Slot 6: Resolve the "$100 OFF" Message-Match Gap on the SF2 Landing Page

**Type:** A/B test (1 variation vs. control)
**Page:** SF2 Driver landing page, shared by Ad 2 and Ad 3 (shop.performancegolf.com/pages/sf2-driver-media-info-sc)

**Revenue potential:** Not independently quantifiable from available data. Ad 2 and Ad 3's shared landing page drove 920 orders / $306,784.94 in the 30-day window; this test's primary value is reducing ad-platform compliance risk and improving click-to-page trust, not a standalone CR lift.

**Hypothesis:** If we add an explicit "$100 OFF" callout to the SF2 landing page that matches Ad 3's creative claim, trust and message-match will improve because the page currently shows sale pricing ($299, marked down from $399) without stating the specific $100 discount the ad promises.

**Data:** Ad 3's creative headlines "SF2 DRIVER: CLAIM YOUR $100 OFF." The three captured folds of the shared landing page show $299 sale pricing marked down from $399 but no explicit "$100 off" badge or callout matching the ad's specific claim (Source: Meta Ads and landing pages).

**V1:** Add a "$100 OFF" badge or callout near the price in the hero fold that explicitly states the discount amount, keeping the existing $299/$399 pricing display unchanged underneath it. Mobile: badge sits directly above or beside the price in the hero fold. Desktop: same position, sized to match the existing price treatment. Control: current price display with no explicit "$100 off" callout.

## Slot 7: Add a Discount Badge to the RS1 Putter Collection Card

**Type:** A/B test (1 variation vs. control)
**Page:** Golf Clubs collection page

**Revenue potential:** 0.3% CR lift x 2,986 orders/mo x $414 avg RS1 price ≈ $3,700/mo.

**Hypothesis:** If we add a "Save up to X%" badge to the RS1 Putter's collection card, click-through and conversion will improve because every other major product card on the grid shows a savings badge, and RS1, the top-revenue product, is the visual exception with no offer shown.

**Data:** On the Golf Clubs collection page, product cards display in a 3-column grid with a "Save up to X%" badge on most cards (357 shows "Save up to 17%," SF2 "Save up to 25%," ONE.1 Wedge "Save up to 25%"). The RS1 Putter card is the exception, showing only "From $399.00" with no strikethrough price or savings badge (Source: Site screenshots).

**V1:** Add a "Save up to X%" badge to the RS1 Putter collection card, matching the style and placement already used on the 357, SF2, and ONE.1 cards, reflecting the live discount already applied at checkout. Mobile: badge sits in the top-left corner of the card, same position as other products. Desktop: same top-left corner placement within the 3-column grid. Control: current card with no badge.

## Slot 8: Match Homepage Hero to Ad-Driven Pricing and Urgency Expectations

**Type:** A/B test (1 variation vs. control)
**Page:** Homepage

**Revenue potential:** Not independently quantifiable, no session-level or returning-visitor data available to isolate this segment. Homepage is the 2nd-largest landing page (1,863 orders, $407,513.32) per 30-day data.

**Hypothesis:** If we add price and urgency messaging to the homepage hero, conversion rate among ad-influenced visitors will improve because every Meta ad landing page collected leads with strikethrough pricing and urgency copy (e.g. "Summer Sale Ends Soon! Save 50%"), while the homepage hero currently shows no price, discount, or urgency element.

**Data:** The homepage hero shows a full-bleed putter image with headline "YOUR STROKE ISN'T THE PROBLEM. YOUR PUTTER IS." and a single CTA "SEE HOW IT WORKS," with no price, discount, or urgency element visible in fold 1. All three Meta ad landing pages collected lead with strikethrough pricing and urgency copy in their hero folds (Source: Site screenshots, Meta Ads and landing pages).

**V1:** Add a price/urgency line to the hero fold beneath the existing headline, consistent with the sale messaging used on the ad landing pages, keeping the current hero image, headline, and "SEE HOW IT WORKS" CTA unchanged. Mobile: urgency line appears directly under the headline, above the CTA. Desktop: same position, inline within the hero text block. Control: current hero with no price or urgency messaging.

## Future Slot Candidates

1. **Multi-club bundle option on club PDPs** - Same underlying opportunity as Slot 3 (the $210.66 AOV gap between single- and multi-club orders), but at the PDP level instead of cart. Do not run alongside Slot 3, they compete for the same mechanic. Hold as the next test once Slot 3's result is in.
