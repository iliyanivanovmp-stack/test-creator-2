# March 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Post-Purchase Surveys, Site Search, Reviews & UGC, Previous A/B Tests, Winning Tests Library, Competitor Research, Email Campaigns (8 emails analyzed), Meta Ads (top 5 ads analyzed)

---

## Test #1: $1 Promo Landing Page Lead Capture

**Page:** $1 Promo Sign-Up Page ([https://www.gardenstreet.com.au/pages/1-aussie-craft-gin-sign-up](https://www.gardenstreet.com.au/pages/1-aussie-craft-gin-sign-up))

**Hypothesis:** If we add social proof and reduce form friction on the $1 promo sign-up page, email capture rate will increase because the page currently shows a bare form with no trust signals despite being the landing page for a top-performing FOMO ad.

**Data:** 15,694 sessions in the last 30 days, second highest traffic page, zero optimization to date (Source: Shopify Analytics). Ad 4 (top 5 by performance) drives paid social traffic here with FOMO copy: "the only thing worse than missing a $1 gin? Finding out your mate got one and you didn't" (Source: Ads). The LP has no social proof despite 6,000+ reviews at 4.9 stars (Source: Reviews). The ad promises "sign up and we'll email you" (suggesting email-only), but the LP asks for 4 fields upfront: email, first name, mobile, DOB (Source: Ads, Screenshot). Community framing with concrete offers increases email capture by 43% in case studies (Source: Winning Tests Library).

**V1:** Add a social proof bar directly above the form: "Join 6,000+ gin lovers | Rated 4.9 stars." One line, aggregate rating with star icons. Nothing else changes. Mobile: full-width bar stacked above the form. Desktop: same position, horizontally centered.
**Brief:** Design: social proof bar component with star icons + member count. Dev: inject bar element above the Klaviyo form on the existing custom page. The Klaviyo form is not modified. No conflicts with running tests.

**V2:** Replace the static hero with a split layout: left side keeps the $1 bottle visual, right side adds a "Your mate's already signed up" counter showing the number of people registered (real or social proof framing) + 2 short member testimonials (one about unboxing, one about gin quality). The Klaviyo form remains unchanged.
**Brief:** Design: split layout with bottle visual on left, sign-up counter + 2 testimonial cards on right. Mobile: stacked (bottle above, counter + testimonials below, form at bottom). Desktop: two-column split. Dev: inject on the existing custom page, restructuring the hero section. The Klaviyo form is not modified. No conflicts with running tests.

---

## Test #2: Subscription PDP Exclusivity & Message Match

**Page:** Subscription PDP ([https://www.gardenstreet.com.au/products/gin-club-subscription](https://www.gardenstreet.com.au/products/gin-club-subscription))

**Hypothesis:** If we add exclusivity framing to the subscription PDP, conversion rate will increase because 6 of 8 email campaigns land on this page and none of the email's exclusivity narrative (which drives the click) carries through to the page.

**Data:** 4,540 sessions in the last 30 days, plus email traffic from 6 of 8 campaigns analyzed (Source: Shopify Analytics, Email Campaigns). Klaviyo email/SMS attributes A$28,400 in total sales in the last 30 days, funneling through this page (Source: Shopify Analytics). Emails repeatedly use "Exclusive to members," "Unavailable anywhere else," and member-only language, but the PDP has zero exclusivity framing (Source: Email Campaigns). Emails cite distillery awards ("Champion Victorian Distillery 2024," "gold judges' nods") absent from the PDP (Source: Email Campaigns). GS06 proved specific, targeted proof beats generic claims (+9.64% RPV) (Source: Previous Tests). Customer-voice copy with specific claims generates +$50,945/mo in case studies (Source: Winning Tests Library). Note: the individual gin changes monthly and is not always exclusive to Garden Street, so exclusivity framing targets the subscription box experience (curation, welcome gifts, member perks), not the bottle itself.

**V1:** Add an "Only Available Through Gin Club" badge directly below the product title and above the price. Small, inline badge with lock icon and the text "Only available through Gin Club. Curated gins, welcome gifts, and member perks you won't find anywhere else." This frames the subscription experience as exclusive (which is evergreen) rather than claiming the individual gin is unavailable elsewhere. Mobile: badge sits between title and price, full-width. Desktop: inline next to the product title.
**Brief:** Design: exclusivity badge component (lock icon + text). Dev: inject badge between product title and price on the subscription PDP. Preserve deployed elements (GS02, GS03, welcome gift, FAQ). Sequencing: GS14 (Deluxe Upgrade on PDP) targets above ATC. This badge sits in the buy box area. Confirm placement doesn't conflict.

**V2:** V1 (subscription exclusivity badge) + replace the generic product description (currently 5 paragraphs about "Australia's most exciting craft distilleries," "personal tasting room," etc.) with a month-specific story that mirrors the email narrative. For this month: lead with the Backwoods Blood Orange Gin, the distillery's origin, and what makes this month's box special. Same tone and hooks the emails use to drive the click, so the PDP delivers on the promise. This copy updates monthly with the new gin, making it an evergreen format. Mobile and desktop: same position, replaces the existing description block above the value props.
**Brief:** Design: no new components, just a copy swap in the description block (the area between the "Gin Club Subscription" title and the value prop icons). Dev: replace the static description with month-specific copy. V1's exclusivity badge also injected (same as V1). Preserve deployed elements (GS02, GS03, welcome gift, FAQ). Same sequencing consideration as V1 re: GS14.

---

## Test #3: Cart Drawer Trust & Reassurance

**Page:** Cart Drawer (sitewide, triggered on Add to Cart)

**Hypothesis:** If we add value reinforcement and risk reversal to the subscription line item in the cart drawer, checkout initiation rate will increase because the drawer currently shows the subscription price with zero context about the value, welcome gift, or flexibility at the final decision point before checkout.

**Data:** 2,359 sessions added to cart in the last 30 days, dropping to 1,790 at checkout (24.1% cart-to-checkout abandonment) (Source: Shopify Analytics). Survey respondents cited price and recurring purchase concerns as purchase barriers (Source: Surveys). GS03 proved that showing value breakdowns (individual RRP values) is the highest-impact lever at +A$41,233/mo (Source: Previous Tests). GS06 proved specific social proof at decision points works (+9.64% RPV) (Source: Previous Tests). Stacked trust signals in the cart drawer generate +$32,605/mo in case studies (Source: Winning Tests Library). The welcome gift currently displays "$62.50 $0.00" with no savings context (Source: Screenshot).

**V1:** Add a single USP line below the subscription line item in the cart drawer: "$223+ value for $99. Free shipping." This is the strongest lever (GS03 proved RRP breakdowns at +A$41,233/mo) and anchors the price against the value they're getting. Only shows on the subscription product, not single gin purchases. Mobile and desktop: same position, directly below the subscription line item.
**Brief:** Design: single text line below the subscription line item. Dev: conditionally inject below the subscription product in the cart drawer (check product type or tag). Static text. Sequencing: GS13 (Deluxe Upgrade in Cart Drawer) targets an upsell module, a different element. Recommend running this test first, then layering GS13 on the winner.

**V2:** Replace V1's value line with a risk-reversal line below the subscription line item: "No lock-in. Skip, pause, or cancel anytime." This directly addresses the top survey barrier (recurring purchase concerns) with a different angle than V1. Tests whether removing commitment fear outperforms value anchoring. Only shows on the subscription product. Mobile and desktop: same position, directly below the subscription line item.
**Brief:** Design: single text line below the subscription line item (same placement as V1, different copy). Dev: conditionally inject below the subscription product in the cart drawer. Static text. Same sequencing as V1 re: GS13.

---

## Test #4: New Visitor Homepage Hero

**Page:** Homepage ([https://www.gardenstreet.com.au/](https://www.gardenstreet.com.au/))

**Hypothesis:** If we replace the generic brand hero with a conversion-focused hero for new visitors, subscription signup rate will increase because the current hero shows the same lifestyle image and "Garden Street Gin Club" branding to everyone, with no hooks tailored to first-time visitors who don't yet know or trust the brand.

**Data:** 33,725 homepage sessions in the last 30 days, 86.6% mobile (Source: Shopify Analytics). 92.18% returning customer rate means only 7.82% are new visitors, yet the hero makes no effort to convert them (Source: Shopify Analytics). The current desktop hero is a lifestyle image with no CTA. Mobile adds "Welcome to Australia's Favourite Gin Club," a review quote, and a "Purchase Today" button, but no value proposition or incentive (Source: Screenshot). The brand's strongest cold-traffic hooks are: 6,000+ reviews at 4.9 stars, $82+ welcome gifts, and "$223+ value for $99" (Source: Ads, Reviews, Email Campaigns). GS11 (announcement bar personalization) is trending toward a win, proving that relevant, targeted copy outperforms generic messaging (Source: Previous Tests).

**V1:** Replace the hero for new visitors with a social-proof-led version. Headline: "Rated 4.9 from 6,000+ Gin Lovers." Subhead: a short review quote. CTA: "Purchase Today." Desktop: text overlay on the left, hero image on the right. Mobile: image above, headline + quote + CTA stacked below. Returning visitors see the current hero unchanged.
**Brief:** Design: new hero layout with headline, review quote, and CTA. Desktop: two-column (text left, image right). Mobile: stacked. Dev: detect new visitors via first-party cookie (no cookie = new). Swap hero for new visitors only. No conflicts with running tests (GS11 targets the announcement bar, not the hero).

**V2:** Replace the hero for new visitors with a value-led version. Headline: "Australia's #1 Gin Subscription." Subhead: "$223+ value for $99/month. + $82 welcome gift with your first box." CTA: "Join Today." Desktop: text overlay on the left, hero image on the right. Mobile: image above, headline + value props + CTA stacked below. Returning visitors see the current hero unchanged.
**Brief:** Design: new hero layout with headline, value proposition lines, and CTA. Desktop: two-column (text left, image right). Mobile: stacked. Dev: same cookie detection as V1. Swap hero for new visitors only. No conflicts with running tests.

---

## Test #5: Dedicated Monthly Gin Landing Page

**Page:** New landing page ([https://www.gardenstreet.com.au/pages/this-months-gin](https://www.gardenstreet.com.au/pages/this-months-gin))

**Hypothesis:** If we build a dedicated landing page for the monthly featured gin with a focused conversion path, ad-to-purchase conversion will increase because the current ad destination (homepage) is a long, multi-purpose page that buries the specific gin, value breakdown, and story the ad promises.

**Data:** Ad 2 (running since Feb 6, 2026) features "YOU CAN'T BUY THIS GIN" with the Backwoods Blood Orange Gin bottle, but lands on the homepage (33,725 sessions in the last 30 days, 86.6% mobile), where the featured gin and value breakdown are absent above the fold (Source: Ads, Shopify Analytics, Screenshot). "Blood orange gin" is the #1 on-site search at 37 searches in the last 30 days, confirming demand for the specific product (Source: Site Search). Emails tell the distillery's story and cite awards that appear nowhere on-site (Source: Email Campaigns). GS03 proved RRP value breakdowns convert (+A$41,233/mo) and GS02 proved storytelling descriptions convert (+21% RPV) (Source: Previous Tests). The gin changes every month, so the LP is built as a reusable template: the structure stays the same, the gin-specific content (hero image, headline, distillery story, RRP items) swaps monthly.

**V1:** Build a mobile-first landing page template with a single conversion path. Structure: (1) Hero: featured gin bottle + headline tailored to this month's story (this month: "You Can't Buy This Gin Anywhere Else" for the Blood Orange Gin, but future months adapt the angle to whatever fits the gin, e.g., awards, origin, botanicals). Mobile: bottle image stacked above headline. Desktop: image left, copy right. (2) "What's Inside This Month" with individual RRP values (proven GS03 format): this month is 700ml Blood Orange Gin, Sodasmith tonic, blood orange garnish, snacks, magazine, totaling $223+. (3) "All of this for $99/month" price anchor + ATC button. Mobile: sticky ATC button at bottom of screen. Desktop: fixed ATC in the right column. (4) Welcome gift choice: Weekender Kit or At-Home Essentials Kit, $82.50 value. (5) 3 new-member testimonials. (6) "Rated 4.9 from 6,000+ reviews. Free delivery. Cancel anytime." trust strip. Minimal navigation (logo + cart only, no full nav menu). The ads team updates the ad destination URL once the page is live.
**Brief:** Design: mobile-first single-page template with 6 sections (hero, RRP breakdown, price anchor + ATC, welcome gift visual, 3 testimonial cards, trust strip). The template is reusable: swap gin image, headline, distillery story, and RRP items monthly. Dev: build as a Shopify custom page with a minimal navigation template (logo + cart only). Sticky ATC on mobile, fixed ATC in right column on desktop. No conflicts with running tests. This page is new, not a modification.