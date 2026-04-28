# May 2026 Testing Roadmap

**Data Sources:** Shopify Analytics, Customer Surveys (Fairing), Meta Ads, Google Ads Transparency, Site Search, Reviews & UGC (Yotpo), Page Speed, Email Campaigns, Content Calendar, Intelligems Analytics, Inspiration Sites, Current Site Screenshots, Internal Test History

---

## Insights

The single biggest signal is one the client already named: Hello Summer Sale is the May revenue moment. 1,236 shoppers searched "sale" in the last 30 days. Survey verbatims are explicit: *"Sale was my reason for purchasing,"* *"thank god for sales,"* *"I made a purchase yesterday, and this sale wasn't available then."* But a custom landing page for a 5-day window is the wrong shape. It can't accumulate significance in time, and the brand already routes paid and email traffic to themed collections that work fine as containers. The leverage is component-level activations that turn existing collection pages into sale pages during the window: tier-aware announcement bar with countdown, sale-tagged collection tile badges, a sale hero strip on HSS-relevant collections, and a finale-day intensification on May 25. The framework reuses across all four 2026 sale events without per-sale rebuild cost.

The second priority is AOV, but the surface has shifted. Cart drawer upsells have already been tested at Printfresh and lost. The new opportunity is Intelligems post-purchase upsells, a feature that wasn't testable before and routes around the pre-purchase risk that killed cart-drawer attempts. With 12.7K monthly orders flowing through checkout, every post-purchase impression is pure incremental AOV with zero conversion-rate risk. Eligible accessory SKUs at $20-70 (eye mask, headband, pouch, hair bows) line up with the right offer geometry: lower-priced complement to the main purchase, single-click acceptance, session-only discount.

The third theme is product page enrichment, refined from earlier framing. Brand-level reviews already render as a clickable star rating on PDP, so leading with that is a wasted variation. The harder gaps are fabric education ("eco satin" 1,512 monthly searches; reviews call out "shouldn't be described as satin"), cross-silhouette discovery (78K monthly searches dominated by print names; reviews repeatedly request the same print in different silhouettes), and colorway exploration (multi-colorway prints exist but only one swatch shows on PDP). The narrative exists. Putting it on the page that decides the sale is the conversion lever.

Revenue opportunity, conservative math:
- HSS sale activations (Slot 1): 250K sale-week visitors × 1.5% baseline CR × 7% relative lift × $190 AOV = **~$50K incremental** for HSS alone. Framework reused 4x annually = ~$200K.
- Post-purchase upsells (Slot 2): 12.7K monthly orders × 8% take rate × $40 avg add = **~$40K/month incremental AOV** with zero pre-purchase conversion risk. Annualized: ~$480K.
- PDP stack (Slot 3): 480K PDP entries × 5% relative ATC lift × 27.6% ATC-to-purchase × $215 AOV = **~$68K/month incremental**, compounding across every PDP. Annualized: ~$815K.

Three slots, three ranges of upside, one clear May priority.

---

## Slot 1: Hello Summer Sale Activation Components

**Type:** A/B test (3 variations vs. control)
**Page:** Site-wide announcement bar + HSS-relevant collection pages (Pajamas, Sets, Out West, Jungle Cat, Beach Grouping). No new LP. Components inject into existing pages and activate during the sale window.
**Revenue potential:** ~250K sale-week sessions × 1.5% baseline CR × 7% relative lift × $190 sale AOV = **~$50K incremental for HSS alone**. Framework reuses across July Apparel Sale (7/1), Xmas in July (7/24), Goodbye Summer Sale (8/30). Annualized: ~$200K.

**Hypothesis:** If we surface the sale through tier-aware messaging, countdown urgency, price anchoring on collection tiles, and a sale-themed hero strip on landing collections, sale-week conversion lifts because shoppers see the deal at every step of the funnel without needing to be routed to a destination we built for 5 days.

**Data:** Site search "sale" with 1,236 queries in 30 days, top 7 query (Source: Shopify Analytics). 339 surveys produced multiple sale-driven verbatims confirming sales drive purchase intent (Source: Surveys). Calendar confirms HSS public sale May 21-25 with tiered loyalty access and a Memorial Day 20% extra coupon as the closer (Source: Content Calendar). 51% of all visitors land on collection pages, bounce 75.1% and worsening (Source: Intelligems). Average discount last 30 days is 3.66%, down 42.8% from prior period; HSS will be the biggest discount event of the period and traffic will spike (Source: Intelligems). Brand has demonstrated capability for excellent themed components on existing pages (Mother's Day Shop tiles, Monogram Shop, Palm Beach Moment) (Source: Email Campaigns, Site Screenshots). Pattern evidence: GoodUI Pattern #59 documents countdown deadlines lifting conversion in 60-70% of A/B tests, strongest on already-discounted offers; Dylan Ander Ch 6 on price anchoring and scarcity; Unbounce message-match research showing 2x+ conversion gaps when ad-to-page copy aligns.

**Critical scheduling note:** The public sale runs only May 21-25 (5 days). Components launch by May 12 in a dormant state, then the sale flag flips on May 19 (FT early access) → May 21 (public). A standard A/B test will not reach significance in 5 days at current CR. Significance accrues across HSS + July Apparel Sale + Xmas in July + Goodbye Summer Sale. Treat HSS as the launch event of an ongoing test, not a one-off.

**V1: Tier-aware announcement bar with countdown + sale-tagged collection tile badges.**
The site-wide announcement bar swaps copy by audience segment during the sale window. Logged-in Founding Tier users see "Your early access ends in [countdown]"; logged-in Dream Team users see "Your early access ends in [countdown]"; cold or anonymous traffic sees "Sale starts in [countdown], members shopping now" pre-May 21, then "Hello Summer Sale, ends Mon 11:59pm" once the public sale begins. Countdown is real-time. Concurrent change: sale-tagged badges on collection tiles across HSS-eligible collections. Each product tile shows a strikethrough was-price, the sale price, and a "% off" pill anchored top-left of the product image. Mobile and desktop: bar copy fits a single line, truncates with ellipsis past 70 characters; badge size scales with tile size.

**V2: V1 + sale hero strip injected at top of HSS-relevant collections.**
Adds a slim full-width hero strip at the top of Pajamas, Sets, Out West, Jungle Cat, and Beach Grouping collections (the LP-lite compromise). Strip contains a collection-specific headline (e.g., "Hello Summer Sale: Out West & Jungle Cat 20% off"), the same countdown to May 25 11:59pm, and 3-4 grouping/persona tiles inline (Mother's Day Shop pattern reused: "Out West / Jungle Cat," "Beach Grouping" with date-gated "Unlocks May 21 / 23" copy for non-VIPs, "Under $100," "Founders' Picks"). Below the strip, the existing collection grid renders unchanged. Mobile: strip stacks vertically, tiles in 2x2. Desktop: strip is single-row with tiles in 4-up. Strip suppresses on collections outside the HSS scope.

**V3: V2 + finale-day intensification on May 25.**
Adds three changes that activate only in the final 24 hours. Announcement bar shifts color from neutral to high-contrast urgency, copy changes to "Final day + extra 20% with code MEMORIAL," and a one-time exit-intent overlay fires on PDP and collection pages (not on cart or checkout) surfacing the stacked code with a single CTA. Exit-intent fires once per session, suppresses on logged-in users who've already used MEMORIAL, and is hard-killed at midnight 5/25.

---

## Slot 2: Post-Purchase Upsells via Intelligems

**Type:** A/B test (3 variations vs. control)
**Page:** Post-purchase confirmation flow (between order placement and the order confirmation page), enabled via Intelligems' post-purchase upsell feature.
**Revenue potential:** 12.7K monthly orders × 8% take rate × $40 average add value = **~$40K/month incremental AOV** with zero pre-purchase conversion risk. Annualized: ~$480K.

**Hypothesis:** Pre-purchase cart upsells have already been tested at Printfresh and lost; the buyer is unwilling to be interrupted at the cart. Post-purchase upsells route around that resistance entirely. The buyer has committed; the only question is whether to add. With Intelligems' new post-purchase support, we can test offer construction (single vs. multi-step, accessory vs. set completion) on a surface that didn't exist before.

**Data:** Cart drawer upsells already tested at Printfresh, did not win (Source: Internal test history). Intelligems recently shipped post-purchase upsell support (Source: Client confirmation). Average units per order is 1.56, most customers buy a single item (Source: Intelligems). Eligible accessory SKUs at the right price points: Eye Mask $34, Twisted Headband ~$28, Quilted Pouch $38, Hair Bows $20-40, Boyfriend Boxer $68, Cocktail Napkins $68 (Source: Site, Reviews). Reviews confirm strong individual ratings on these accessories: Eye Mask 4.9/19 reviews, Quilted Pouch 4.9/100 reviews (Source: Yotpo). Site search shows print-name dominance (cat 3,936, bagheera 1,433, mahjong 1,208), suggesting same-print accessories are a strong matching signal (Source: Shopify Analytics). Per CRO best practice (Dylan Ander, Ch 10), upsells must be discounted, relevant, one-click, complementary, and much cheaper than main purchase. These SKUs all qualify. Athos (PDP-side upsell tool) is being set up but not ready until June, so May testing is post-purchase only (Source: Client).

**V1: Single complementary accessory at 20% off, print-matched.**
Single post-purchase offer between checkout and confirmation: one accessory matched to the print(s) just bought (eye mask, headband, or pouch in the same print or a complementary one). Copy: "Add the matching [Eye Mask / Headband / Pouch] for 20% off, one click." Single Add and single Decline. Selection logic: prioritize same-print accessory; fall back to highest-rated accessory under $40 if no print match exists. Mobile and desktop: single product card with image, name, was/is price, and one Add CTA.

**V2: Two-step post-purchase, accessory then second offer on decline.**
Same as V1 for step one. If the buyer declines, a second offer surfaces: a different accessory category at the same 20% off (e.g., declined an eye mask, get offered a hair bow or pouch). Single decline at step two ends the flow. Logic: never show the same accessory category twice; cap at two steps to avoid fatigue.

**V3: Complete-the-set post-purchase, larger ticket.**
Single post-purchase offer for a complementary apparel piece in the same print: matching robe if a set was bought, matching shorts if a long PJ was bought, matching long PJ if a short set was bought. 10-15% discount (lower than V1/V2 because the ticket is higher, $98-148 range). Copy: "Complete the set with the matching [Robe / Shorts / Long PJ] for [X]% off." Single Add and single Decline. Falls back to V1's accessory offer if no matching apparel SKU is in stock in the buyer's size.

**Sequencing note:** During HSS week (May 21-25), V3's discount logic must suppress to avoid stacking with sale prices that would zero out margin. Session-only post-purchase discount suppresses by default when the cart contained a sale SKU. Test scheduling: launch V1 and V2 by May 12 to bake before HSS. V3 launches immediately after HSS ends (May 26).

---

## Slot 3: PDP Conversion Stack: Fabric Story, Print Discovery, Colorway Swatches

**Type:** A/B test (3 variations vs. control)
**Page:** Product Detail Pages (top-revenue products: Courtly Check Bagheera Eco Satin Soho Set, Spa Day Wildest Dreams, Champagne & Caviar Rittenhouse, Bagheera Eco Satin Robe, Mah Jongg Long PJ). PDP template applies sitewide once approved.
**Revenue potential:** 480K direct PDP entries/month × 5% relative ATC lift × 27.6% ATC-to-purchase × $215 AOV = **~$68K/month incremental**. Compounds across every PDP and every collection→PDP path. Annualized: ~$815K.

**Hypothesis:** If we surface assets that already exist (fabric story, cross-silhouette print discovery, colorway swatches where applicable) on the PDP itself, ATC rate lifts because we close customer information gaps before the size selector: fabric expectation alignment, discovery of preferred silhouettes, and easy comparison of colorways without leaving the page.

**Data:** Site search shows "eco satin" with 1,512 queries (top 3). Customers want fabric education on the page they're already on (Source: Shopify Analytics). Reviews flag fabric-description mismatch: *"It's not the shiny satin feel or appearance you may think of. It is a viscose... shouldn't be described as satin"* (Source: Reviews). Brand-level reviews already render as a clickable star rating on PDP, so reviews-above-fold is not a productive variation (Source: Site Screenshot, internal note). Print-name searches dominate (cat 3,936, bagheera 1,433, mahjong 1,208, bagel 1,869, caviar 1,140) and reviews repeatedly request more silhouettes per print: *"hope this print is produced in a future Eco Satin or long PJ version,"* *"I wish you would do a separate top and bottom"* (Source: Site Search, Reviews). Inspiration: Desmond & Dempsey "Shop the Print" PDP module shows all silhouettes within a print. Lake Pajamas full-width fabric hero on PDP (Source: Inspiration). Product line confirms multi-colorway prints exist: Bagheera comes in Tobacco, Wedding Cake, Floral, Ink (Source: Reviews, product titles). Current PDP shows only one colorway thumbnail per product (Source: Site Screenshot). Add-to-Cart Rate is currently 3.16% and trending down -6.74% (Source: Intelligems).

**V1: Eco Satin / Cotton fabric story module above the size selector.**
Adds a fabric education module sized to ~30% of viewport height, positioned immediately under the price/installments line and above the size selector (so it informs the size decision). Module title is fabric-specific (e.g., "About Eco Satin"), one image (closeup texture or production shot pulled from /pages/sustainability), 3 short bullets ("Sourced from sustainable forests," "Low water, biodegradable," "Soft, breathable, kind to skin"), and a small "Learn more" link to the sustainability page. The module is only shown for the relevant fabric (different copy/image for Eco Satin, Organic Cotton, Pima Modal Knit). Mobile: stacked layout, image full-width above bullets. Desktop: image left 40%, bullets right 60%. The brand-level star rating already renders elsewhere on PDP and is not duplicated here.

**V2: V1 + "Shop the Print" cross-silhouette module between buy-box and description accordion.**
Adds a horizontal-scroll module titled "Shop This Print" or "More in [Print Name]" positioned between the buy-box trust icons and the description accordion (so it sits in the natural scroll path after the user has decided on size but before they're scanning details). Pulls all SKUs that share the print and shows silhouette thumbnails (PJ set, robe, eye mask, shorts, pouch). 5-8 cards on average. Each card shows silhouette image, silhouette name (e.g., "Long PJ Set"), price, and clicks to that PDP. Sold-out silhouettes show a slash-through and a "Notify Me" affordance. The module appears only when the print has 2+ silhouettes; for single-silhouette prints it suppresses. Sort: same-print silhouettes first, complementary prints appended only if same-print silhouette count is below 3. Mobile: horizontal scroller, ~35% viewport width per card. Desktop: 5-up static grid that wraps if more silhouettes exist.

**V3: V2 + colorway swatch row inside the buy-box (where applicable).**
Replaces the single color thumbnail next to "Color: [Name]" with a row of clickable swatch chips representing all colorways of the same print + silhouette combination. E.g., Bagheera Eco Satin Robe displays Tobacco / Wedding Cake / Floral / Ink as 4 chips. Clicking a chip navigates to the matching PDP (each colorway is its own SKU/PDP). The chip set only appears when 2+ colorways exist; for single-colorway products (e.g., Courtly Check Bagheera collab) a single chip remains. Sold-out colorways show with a slash-through and a "Notify Me" affordance. Mobile and desktop: chips are 32px square swatches in a horizontal row immediately below the "Color: [Name]" label, wrapping to a second row if more than 6 colorways exist.

**Sequencing dependency:** V1, V2, V3 stack sequentially (V2 includes V1, V3 includes V1+V2) so we can attribute incremental impact per layer. Run continuously, no sequencing conflict with Slots 1 or 2. Begin May 5-7 to bake significance before HSS.

---

## Future Slot Candidates (queue for June+)

These ideas have data support but didn't fit the May 3-slot count. Logged for future months.

- **Hen House LP test**: paid traffic + email traffic both drive to a bare LP. If the HSS activation framework wins, port the pattern to Hen House and other always-on collection campaigns.
- **Filter / nav UX rebuild**: multiple survey verbatims about broken filters; "tennis" 1,414 searches finds an existing product that's hard to discover via nav. Scope likely a multi-slot dev project.
- **Gift workflow rebuild**: survey friction on gift message field, gift wrap "sold out," $8 to email gift card. Brand promises "Gifting Made Easy" in email footer. Mismatch.
- **Page Speed / LCP**: 2.82s P75 trending worse. Worth a dev slot if speed degradation continues.
- **Print discovery on the homepage / collection LP**: "Shop the Print" pattern at the LP level rather than just PDP.
- **Loyalty tier visibility**: Dream Team Points exist with tiers, but most users sit at "Tier: none" with 100 points and no visibility on what unlocks. May convert lurkers to FT/DT (the same loyalty tiers HSS uses for early access).
- **Homepage shoppable tiles**: 3 filter tabs on "Shop Top Picks" and 2x2 category tiles dominate above-fold real estate. No heatmap data yet on click distribution or per-tile RPS, so the test variable is unclear. Request heatmap access before scoping.
- **Mobile gallery zoom**: flagged by user as feeling off on mobile. Needs a UX walkthrough to articulate the specific friction (zoom level, gesture, controls, layout shift) before turning into a structured test.
- **Athos PDP upsells**: dependent on Athos setup, expected June. Pre-purchase PDP upsell mechanics (e.g., "frequently bought together" with one-click add) become testable once the tool is live.

---

## Client-Actionable Flags (Not Tests)

These need internal investigation, not A/B testing.

1. **"New sizing" reviews**: multiple verbatims complaining about a sizing reset. Not visible in heatmaps or CRO funnel; only surfaced in 4-star and below review themes. Worth a product-side investigation.
2. **Eco Satin description mismatch**: customer expectation (shiny silk-like satin) vs. reality (viscose, muted, wrinkles). Either product description rewrite or fabric repositioning needed. The fabric story module in Slot 3 V1 helps reframe but doesn't replace this.
3. **Final sale + sizing exchange policy**: frustration when items don't fit and exchange is blocked. Consider a "fit guarantee" on certain SKUs even within final-sale designations.
4. **Shipping protection toggle off by default**: fine, but the language is undifferentiated. Worth understanding take rate.
5. **Gifting promise vs. delivery gap**: "Gifting Made Easy" in email footer vs. multiple survey complaints about gift wrap "sold out" and missing gift message field. Operations + product gap.
