# March 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Post-Purchase Surveys, Site Search, Reviews & UGC, Previous A/B Tests, Winning Tests Library, Competitor Research, Email Campaigns (8 emails analyzed), Meta Ads (top 5 ads analyzed)

---

## Test #1: $1 Promo Landing Page Lead Capture

**Page:** $1 Promo Sign-Up Page (https://www.gardenstreet.com.au/pages/1-aussie-craft-gin-sign-up)

**Hypothesis:** If we add social proof and reduce form friction on the $1 promo sign-up page, email capture rate will increase because the page currently shows a bare form with no trust signals despite being the landing page for a top-performing FOMO ad.

**Data:** 15,694 sessions in the last 30 days, second highest traffic page, zero optimization to date (Source: Shopify Analytics). Ad 4 (top 5 by performance) drives paid social traffic here with FOMO copy: "the only thing worse than missing a $1 gin? Finding out your mate got one and you didn't" (Source: Ads). The LP has no social proof despite 6,000+ reviews at 4.9 stars (Source: Reviews). The ad promises "sign up and we'll email you" (suggesting email-only), but the LP asks for 4 fields upfront: email, first name, mobile, DOB (Source: Ads, Screenshot). Community framing with concrete offers increases email capture by 43% in case studies (Source: Winning Tests Library).

**Variation 1:** Add a social proof bar directly above the form: "Join 6,000+ gin lovers | Rated 4.9 stars." One line, aggregate rating with star icons. Nothing else changes. Mobile: full-width bar stacked above the form. Desktop: same position, horizontally centered.

**Variation 2:** V1 (social proof bar) + reduce the form to email-only above the fold. First name, phone, and DOB move to a second step that expands after email submission. Mobile: email field + "Enter" CTA visible without scrolling; remaining fields appear on next screen. Desktop: same progressive flow, but remaining fields expand inline below the email field rather than a new screen.

**Brief:** Design: V1 needs a social proof bar component (star icons + member count). V2 adds a progressive disclosure form (email-only first step). Dev: inject on the existing custom page. V2 layers on V1. No conflicts with running tests.

---

## Test #2: Subscription PDP Exclusivity & Message Match

**Page:** Subscription PDP (https://www.gardenstreet.com.au/products/gin-club-subscription)

**Hypothesis:** If we add exclusivity framing to the subscription PDP, conversion rate will increase because 6 of 8 email campaigns land on this page and none of the email's exclusivity narrative (which drives the click) carries through to the page.

**Data:** 4,540 sessions in the last 30 days, plus email traffic from 6 of 8 campaigns analyzed (Source: Shopify Analytics, Email Campaigns). Klaviyo email/SMS attributes A$28,400 in total sales in the last 30 days, funneling through this page (Source: Shopify Analytics). Emails repeatedly use "You can't buy this gin anywhere else," "Exclusive to members," and "Unavailable anywhere else," but the PDP has zero exclusivity framing (Source: Email Campaigns). Emails cite distillery awards ("Champion Victorian Distillery 2024," "gold judges' nods") absent from the PDP (Source: Email Campaigns). GS06 proved specific, targeted proof beats generic claims (+9.64% RPV) (Source: Previous Tests). Customer-voice copy with specific claims generates +$50,945/mo in case studies (Source: Winning Tests Library).

**Variation 1:** Add an "Exclusive to Members" badge directly below the product title and above the price. Small, inline badge with lock icon and the text "Exclusive to Members. You can't buy this gin anywhere else." Mobile: badge sits between title and price, full-width. Desktop: inline next to the product title.

**Variation 2:** V1 (exclusivity badge) + add an "Award-Winning Distillery" badge next to the gin name in the "What's Inside" section. Text: "Champion Victorian Distillery 2024" with a small award icon. Mobile: badge wraps below the gin name. Desktop: inline next to the gin name.

**Brief:** Design: V1 needs an exclusivity badge component. V2 adds a small award badge. Dev: inject on the subscription PDP. Both variations preserve deployed elements (GS02, GS03, welcome gift, FAQ). Sequencing: GS14 (Deluxe Upgrade on PDP) targets above ATC. These elements sit in or below the buy box area. Confirm placement doesn't conflict.

---

## Test #3: Cart Drawer Trust & Reassurance

**Page:** Cart Drawer (sitewide, triggered on Add to Cart)

**Hypothesis:** If we add social proof and value reinforcement to the cart drawer, checkout initiation rate will increase because the drawer currently shows items and prices with zero trust or savings context at the final decision point before checkout.

**Data:** 2,359 sessions added to cart in the last 30 days, dropping to 1,790 at checkout (24.1% cart-to-checkout abandonment) (Source: Shopify Analytics). Survey respondents cited price and recurring purchase concerns as purchase barriers (Source: Surveys). GS03 proved that showing value breakdowns (individual RRP values) is the highest-impact lever at +A$41,233/mo (Source: Previous Tests). GS06 proved specific social proof at decision points works (+9.64% RPV) (Source: Previous Tests). Stacked trust signals in the cart drawer generate +$32,605/mo in case studies (Source: Winning Tests Library). The welcome gift currently displays "$62.50 $0.00" with no savings context (Source: Screenshot).

**Variation 1:** Add a single trust line above the checkout button: "Rated 4.9 stars from 6,000+ gin lovers" with star icons. One line, no other changes. This USP is universal across all products (subscription, gifts, one-off purchases) and backed by the review data (4.86 avg across 6,000+ reviews). Mobile and desktop: same position in the cart drawer, directly above the checkout button.

**Variation 2:** V1 (social proof line) + add a savings reinforcement below the line items: "You're saving $[X] on this order" dynamically calculated from total RRP minus cart price. For subscription boxes, this is $124+ ($223 RRP - $99). For gift boxes, calculate per product. This applies to all products, not just subscriptions. Mobile and desktop: same position, below the last line item and above the trust line + checkout button.

**Brief:** Design: V1 needs a single trust line with star icons. V2 needs a dynamic savings calculation line. Dev: V1 is a static text injection. V2 requires pulling RRP data per product and computing savings dynamically. Sequencing: GS13 (Deluxe Upgrade in Cart Drawer) is approved for dev and targets an upsell module. This test targets trust signals, a different element. Recommend running this test first (establish trust baseline), then layering GS13 on the winner.

---

## Test #4: New vs Returning Visitor Announcement Bar Personalization

**Page:** Sitewide, Announcement Bar (https://www.gardenstreet.com.au/)

**Hypothesis:** If we personalize the announcement bar based on whether the visitor is new or returning, conversion will increase because the current bar shows acquisition messaging to everyone, including the 92.18% of visitors who are returning customers and don't need "join today" prompts.

**Data:** 92.18% returning customer rate means the vast majority of visitors are existing subscribers (Source: Shopify Analytics). The current announcement bar promotes welcome gifts and joining, which is irrelevant to active members. Meanwhile, the 7.82% new visitors (the actual conversion targets) see the same generic bar as everyone else, with no acknowledgement that they're new (Source: Screenshot). GS11 (Geo Personalization) is testing city-based announcement bar copy and trending toward a win, proving that relevant, specific bar copy outperforms generic messaging (Source: Previous Tests). The brand's strongest cold-traffic hooks are: 6,000+ reviews at 4.9 stars, $82+ welcome gifts, and "Australia's #1 gin subscription" (Source: Ads, Reviews, Email Campaigns).

**Variation 1:** New visitors (no cookie/first session) see: "New here? 6,000+ gin lovers rate us 4.9 stars. $82+ in welcome gifts with your first box →". Returning visitors see the GS11 winner (unchanged). The personalization targets only the new visitor segment, using the strongest social proof + incentive hooks from ads and reviews. Detection: first-party cookie check. Mobile and desktop: same announcement bar format as GS11.

**Variation 2:** V1 (new visitor personalization) + returning non-purchasers (have visited before, no purchase cookie) see: "Welcome back! This month's gin is exclusive to members. Hassle-free refunds if you're not convinced →". This addresses the hesitation of warm leads who've browsed but not bought, using exclusivity (from emails) and risk reversal ("hassle-free refunds," validated in GS02's winning variation). Existing subscribers still see the GS11 winner. Mobile and desktop: same format.

**Brief:** Design: no new components needed, just different copy per segment (same announcement bar format as GS11). Dev: use cookie-based detection to identify new visitors (no cookie), returning non-purchasers (cookie but no purchase), and existing customers (purchase cookie or logged in). Swap announcement bar text accordingly. Sequencing: run after GS11 concludes and its winner is deployed as the new baseline. GS11 started Feb 19.

---

## Test #5: Dedicated Ad Landing Page ("You Can't Buy This Gin")

**Page:** New landing page (e.g., https://www.gardenstreet.com.au/pages/this-months-gin)

**Hypothesis:** If we build a dedicated landing page for Ad 2 ("YOU CAN'T BUY THIS GIN") that continues the ad's exclusivity narrative with a focused conversion path, ad-to-purchase conversion will increase because the current homepage destination is a long, multi-purpose page that buries the exclusivity, value, and product specifics the ad promises.

**Data:** Ad 2 (running since Feb 6, 2026) features "YOU CAN'T BUY THIS GIN" with the Backwoods Blood Orange Gin bottle and the copy "You don't need to plan. You don't need to guess" (Source: Ads). It currently lands on the homepage (33,725 sessions in the last 30 days, 86.6% mobile), where the Blood Orange Gin, exclusivity angle, and value breakdown are all absent above the fold (Source: Ads, Shopify Analytics, Screenshot). "Blood orange gin" is the #1 on-site search at 37 searches in the last 30 days, confirming demand for this specific product (Source: Site Search). Emails use the same exclusivity framing and cite distillery awards (Champion Victorian Distillery 2024) that appear nowhere on-site (Source: Email Campaigns). GS03 proved RRP value breakdowns convert (+A$41,233/mo) and GS02 proved storytelling descriptions convert (+21% RPV) (Source: Previous Tests).

**Variation:** Build a mobile-first landing page with a single conversion path. Structure: (1) Hero: Blood Orange Gin bottle with "You Can't Buy This Gin Anywhere Else" headline and "Exclusive to Garden Street Members" subhead. Mobile: bottle image stacked above headline. Desktop: image left, copy right. (2) "What's Inside This Month" with individual RRP values (proven GS03 format): 700ml Blood Orange Gin, Sodasmith tonic, blood orange garnish, snacks, magazine, totaling $223+. (3) "All of this for $99/month" price anchor + ATC button. Mobile: sticky ATC button at bottom of screen. Desktop: fixed ATC in the right column. (4) Welcome gift choice: Weekender Kit or At-Home Essentials Kit, $82.50 value (matching Email 5's presentation). (5) 3 new-member testimonials from Email 8 (Anne-Marie, Laura, Anonymous). (6) "Rated 4.9 from 6,000+ reviews. Free delivery. Cancel anytime." trust strip. Minimal navigation (logo + cart only, no full nav menu). The ads team updates Ad 2's destination URL once the page is live. This LP can be updated monthly with the new featured gin, making it a reusable asset.

**Brief:** Design: mobile-first single-page layout. Hero section, RRP breakdown, ATC, welcome gift visual, 3 testimonial cards, trust strip. Dev: build as a Shopify custom page with minimal navigation template. Sticky ATC on mobile. No conflicts with running tests. This page is new, not a modification.
