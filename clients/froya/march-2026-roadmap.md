# March 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Thank You Page Surveys (6,584 responses), Meta Ads Library, Site Screenshots (Homepage, LP, PDP, Collection, Cart Drawer), Reviews & UGC, Core Web Vitals, Competitor Research, Trustpilot, Email Campaigns

## What We Found

We analyzed 6,584 thank-you page survey responses from February 2026. These are people who bought. The ones who didn't are invisible, but the objections from buyers tell us what's killing conversion for everyone else.

**The top reason people almost didn't buy: price (54.1%).** But price is rarely the real problem. It's a value perception problem. Froya's clinical trial data (+79% hydration, +88% radiance) is buried behind an FAQ accordion on the PDP. The emails lead with it. The site doesn't.

**7.6% of buyers questioned if the brand was legitimate.** Their words: "Website looks like a scam," "too much promotions, does not look legit." The cart drawer, where doubt peaks, has zero trust signals. No reviews, no guarantee, no customer count.

**Three Meta ads use three different hooks. The landing page matches none of them.** Norse witchcraft, personal transformation, Viking heritage. All three land on "Delay Wrinkles by 10 years, Guaranteed." The strongest ad language (ingredient purity, clinical proof, origin story) is absent from the first fold.

**The opportunity:** The main landing page gets 1.2M sessions/mo at 1.62% CR. A 0.2% CR lift = ~2,400 additional orders at $100 AOV = **~$240K/mo in incremental revenue.** Even a 0.1% lift on this page alone is $120K/mo.

The four tests below are ordered by revenue potential. Each targets a different page or component, so they can run concurrently where noted.

---

## Test #1: Landing Page Hero Message Match

**Page:** Main landing page (/pages/fr-ya-organics-hyper-potent-arctic-balms-for-mature-skin). 1,216,799 sessions in the last 30 days (+31% MoM).
**Revenue potential:** 1.2M sessions/mo at $100 AOV. A 0.15% CR lift = ~1,800 orders = ~$180K/mo.

**Hypothesis:** If we replace the generic hero headline with clinical proof and ingredient story elements that match the ad angles driving traffic, we will increase the landing page conversion rate because the current hero ("Delay Wrinkles by 10 years, Guaranteed") doesn't echo the hooks from any of the top 3 Meta ads, and 7.6% of buyers almost didn't purchase due to trust/legitimacy concerns (Source: Surveys, Feb 2026).

**Data:** All 3 top Meta ads use different angles (Norse witchcraft/natural ingredients, personal transformation/"spent $2000+ on other products," Viking heritage/Sea Buckthorn origin story), but all land on the same hero that matches none of them (Source: Meta Ads Library). The brand's own emails prove clinical data converts: Email #2 leads with "+79.12% hydration, +82.35% skin health" and specific clinical results (Source: Email Campaigns, Mar 2026). The /clinical-trial page grew +739% in sessions last month, signaling demand for proof (Source: Shopify Analytics). 54.1% of buyers cite price as their top objection (Source: Surveys), yet the LP hero does no value framing before presenting the discount CTA.

**V1:** Replace the current hero headline and subhead. Keep the split layout (image left, copy right). Change "Delay Wrinkles by 10 years, Guaranteed" to a clinical-proof-led headline: e.g. "Clinically Tested. 79% More Hydrated Skin in 60 Days." Subhead changes from "Handmade skincare from Arctic plants" to "Made from Arctic plants and beeswax. No water, no fragrance, no preservatives. 7,405+ five-star reviews." This surfaces the ingredient purity claim from Ad #3 and the review count from Ad #1 directly in the hero. Keep the existing CTA button, review stars, 60-day guarantee line, and testimonial overlay unchanged. On mobile, the copy stacks above the image. On desktop, the split layout remains.
**Brief:** Design: Replace H1 text and subhead text only. No layout changes. Dev: Text swap in the hero section. Headline becomes e.g. "Clinically Tested. 79% More Hydrated Skin in 60 Days." Subhead becomes e.g. "Made from Arctic plants and beeswax. No water, no fragrance, no preservatives. 7,405+ five-star reviews." All other hero elements (image, CTA, stars, guarantee line, testimonial overlay) stay. Mobile: copy stacks above image as it does today.

**V2:** Same as V1, plus add a one-line trust bar directly below the hero CTA button: "393 clinicians recommend Froya on FrontrowMD | 4.7/5 on Trustpilot | 60-day money-back guarantee." This stacks three trust data points in one line at the moment of decision. Everything else stays the same as V1. On mobile, the trust bar wraps to two lines below the CTA. On desktop, it sits on one line.
**Brief:** Design: Same headline/subhead swap as V1. Add a trust bar element below the CTA. Three items separated by pipes: "393 clinicians recommend Froya on FrontrowMD | 4.7/5 on Trustpilot | 60-day money-back guarantee." Use smaller text (14px), muted color to not compete with the CTA. Dev: Add a new div below the CTA button. Style: inline text, pipe-separated, centered under the button. Mobile: allow wrapping to 2 lines.

---

## Test #2: Cart Drawer Trust Signals

**Page:** Cart drawer (site-wide, appears on all pages after ATC).
**Revenue potential:** 4.67% ATC to 1.62% purchase = ~89,000 visitors add to cart but only ~47,400 buy. Closing even 5% of that gap = ~2,080 additional orders = ~$208K/mo.

**Hypothesis:** If we add stacked trust signals above the checkout button in the cart drawer, we will reduce cart-to-checkout drop-off because the funnel leaks from 4.67% ATC to 1.62% purchase (Source: Shopify Analytics, last 30 days) and the cart drawer currently contains zero trust signals at the moment of purchase decision.

**Data:** 7.6% of buyers almost didn't purchase due to trust/legitimacy concerns, and 3.8% questioned whether the product would actually work (Source: Surveys, 6,584 responses, Feb 2026). Trustpilot reviews mention subscription auto-enrollment fears and product quality doubts (Source: Trustpilot, 5,052 reviews). The current cart drawer shows upsells and a subscription toggle but no guarantee, no reviews, no customer count (Source: Cart Drawer Screenshots). The cart drawer is the last touchpoint before checkout, and it offers zero reassurance.

**V1:** Add a trust signal bar between the "Continue Shopping" link and the estimated total/checkout button section. Three data points on one line: "7,405+ Reviews | 176K+ Women | 60-Day Guarantee." Text only, no icons. Muted styling so it doesn't compete with the checkout button. Everything else in the cart drawer stays the same (free shipping bar, upsells, subscription toggle, savings display). On mobile, the trust bar sits directly above the totals section. On desktop, it sits in the same position on the right-side cart panel.
**Brief:** Design: Single line of text between "Continue Shopping" and the totals section. "7,405+ Reviews | 176K+ Women | 60-Day Guarantee." 13px text, centered, gray (#666). No background, no border. Dev: Add a new element in the cart drawer template between the continue-shopping link and the totals/checkout section. Static text, no dynamic data needed (update review count quarterly). Mobile: same position, allow wrapping to 2 lines if needed. Desktop: single line.

**V2:** Same as V1, plus replace the "SUBSCRIBE & SAVE $40" toggle with a less pressured framing: "Optional: Subscribe for 30% off future orders. Cancel anytime." This addresses the subscription friction directly. 4.5% of buyers cite subscription concerns, and Trustpilot reviews mention auto-enrollment fears (Source: Surveys, Trustpilot). The toggle stays functionally identical, but the copy shifts from urgency ("SAVE $40") to reassurance ("Cancel anytime"). Trust bar from V1 is also included.
**Brief:** Design: Add trust bar from V1. Change subscription toggle label from "SUBSCRIBE & SAVE $40" to "Optional: Subscribe for 30% off future orders. Cancel anytime." Same toggle element, same functionality. Dev: Text change on the subscription toggle label. Add trust bar element per V1 spec. Mobile and desktop: same treatment for both changes. Note: V2 stacks on V1. If V1 wins but V2 doesn't outperform V1, we know the trust bar alone is the driver. If V2 wins over V1, the subscription copy change adds incremental lift.

---

## Test #3: PDP Clinical Proof Above the Fold

**Page:** Product page: The Complete System for Mature Women's Skin (/products/the-complete-system-for-mature-women-s-skin). 212,994 sessions in the last 30 days (+55% MoM). $4.47M/mo in sales.
**Revenue potential:** 213K sessions/mo on a $119-$159 product. A 0.5% ATC lift = ~1,065 additional carts. At current cart-to-purchase rate, that's ~$37K-$50K/mo.

**Hypothesis:** If we add clinical trial results above the fold on the PDP, we will increase add-to-cart rate because 3.8% of buyers questioned if the product works and 54.1% cited price as their top concern (Source: Surveys), and clinical proof both validates efficacy and justifies the price.

**Data:** The brand's Email #2 leads with specific clinical stats (+79.12% hydration, +82.35% skin health, +88.24% radiance, +73.53% reduction in aging signs) and these emails drive engagement (Source: Email Campaigns, Mar 2026). The /clinical-trial page exploded to 49,720 sessions (+739% MoM), showing visitors actively seek this proof (Source: Shopify Analytics). Yet the PDP does not surface these stats above the fold (Source: PDP Screenshots). The "Clinicians' Choice: 393 clinicians share this on FrontrowMD" badge exists on the PDP but is easy to miss. Survey verbatims include: "Does it really work?", "Nothing else I have ever used has worked," and "A lot of money and it may not work" (Source: Surveys).

**V1:** Add a "Clinical Results" section between the benefit icons row (Reduce Lines & Wrinkles, Boost Collagen, etc.) and the Clinicians' Choice badge. Display 3 key stats in a horizontal row: "79% More Hydrated | 88% More Radiant | 73% Less Visible Aging." Each stat in a small card with the percentage large and the descriptor below. Cite "60-day clinical study" underneath the row in small text. Remove the "WARNING! LOW STOCK [516 LEFT]" urgency element, which compounds trust issues. Everything else on the PDP stays: pricing, subscription options, ATC button, FAQs, reviews. On mobile, the 3 stat cards stack to a single scrollable row or 1-column stack. On desktop, 3 cards sit side by side.
**Brief:** Design: New section between benefit icons and Clinicians' Choice badge. Three stat cards in a row. Each card: large percentage (24px bold), descriptor text below (14px). "79% More Hydrated" / "88% More Radiant" / "73% Less Visible Aging." Below the row: "Based on a 60-day clinical study" in 12px muted text. Remove the low-stock warning banner entirely. Dev: Add new section in PDP template. Remove or hide the low-stock warning element. Mobile: cards in a horizontal scroll or stack to single column. Desktop: 3 cards in a row, centered. This test should run after Test #1 reaches significance (2-week minimum) since both tests use clinical data, and we want clean reads.

**V2:** Same as V1 (clinical stats + low-stock removal), plus replace the current product description list format with a customer-voice lead-in. Change "System Includes (60-day supply):" followed by the 4 bullet points to: "176,000+ women use this daily. The system includes everything for a complete 60-day routine:" followed by the same 4 products. This adds social proof context to the product description and anchors the product in social proof before listing contents.
**Brief:** Design: Same clinical stats section and low-stock removal as V1. Change the product description intro from "System Includes (60-day supply):" to "176,000+ women use this daily. The system includes everything for a complete 60-day routine:" Same 4 product bullets follow. Dev: Text change in the product description area, plus all V1 changes. Mobile and desktop: same text treatment, no layout changes to the description block.

---

## Test #4: Collection Page Trust Hero

**Page:** Collection page (/collections/all-products). 93,493 sessions in the last 30 days (+34% MoM).
**Revenue potential:** 93K sessions/mo. Smaller than the LP or PDP, but this page is growing fast (+34%) and has zero optimization today. A 0.3% CR lift = ~280 orders = ~$28K/mo.

**Hypothesis:** If we add a trust-building hero section above the product grid with social proof and a concern-based product finder, we will increase collection page conversion rate because the current page has no trust signals above the fold and 7.6% of buyers almost didn't purchase due to trust concerns (Source: Surveys).

**Data:** The collection page gets 93,493 sessions/mo (+34%) but opens with a sale banner and jumps straight into the product grid with no social proof, no reviews, no brand story (Source: Collection Page Screenshots). Email #1 proves that concern-based product matching ("For Aging & Mature Skin," "For Hair + Scalp," "For Psoriasis, Eczema") resonates with this audience (Source: Email Campaigns). The "Good For" filter exists in the sidebar but is collapsed and buried (Source: Collection Page Screenshots). 3.8% of buyers weren't sure the products would work, and survey verbatims show confusion about which product to choose: "I didn't understand which product I needed most" (Source: Surveys). Visitors land on this page and see a sale banner followed by products with no context for why they should trust the brand.

**V1:** Add a compact hero section between the sale banner and the product grid. Content: "521,833+ Successful Skin & Hair Transformations" (matching the homepage claim) with the star rating and review count. Below it, add 4 horizontal pill buttons for concern-based filtering: "Mature Skin" / "Hair & Scalp" / "Eczema & Psoriasis" / "Acne & Redness." These replace the sidebar filter functionality with a more prominent, visual approach. Keep the sidebar filters for users who want more specificity. On mobile, the pills wrap to 2x2 grid. On desktop, they sit in a single row.
**Brief:** Design: New hero section below the sale banner, above the product grid. "521,833+ Successful Skin & Hair Transformations" as H2, centered. Star rating (5 stars) + "7,405+ reviews" below, centered. Four concern-based pill buttons below: "Mature Skin," "Hair & Scalp," "Eczema & Psoriasis," "Acne & Redness." Pills styled as outlined buttons with the brand orange on hover/active state. Dev: Hero section is static HTML/CSS. Pill buttons filter the product grid by the corresponding collection tags (same as current sidebar categories). Mobile: pills in 2x2 grid. Desktop: pills in a single horizontal row. Keep existing sidebar filters intact.

**V2:** Same as V1, plus add a single before/after testimonial card below the pills. Show one rotating customer story (pull from the existing before/after carousel used on the homepage/LP/PDP). Format: before/after photo side by side, name + age, one-line quote, star rating. This adds visual proof that the products work before the visitor browses. On mobile, the card spans full width below the pills. On desktop, it sits centered below the pills at ~60% width.
**Brief:** Design: All V1 elements, plus a testimonial card below the pills. Before/after photo (split side-by-side), name + age, one-line quote, 5-star rating. Rotate through 3 customers (use Joan 64, Karen K., Nicole 39 from existing assets). Card has a subtle border, light background. Dev: All V1 implementation, plus a testimonial card component. Rotate testimonials on page load (random from 3). No carousel/slider needed. Mobile: full-width card. Desktop: centered, max-width 600px. Sequencing: This test can run simultaneously with Tests #1 and #2 since it targets a different page. Run after or alongside Test #3 since they don't share components.
