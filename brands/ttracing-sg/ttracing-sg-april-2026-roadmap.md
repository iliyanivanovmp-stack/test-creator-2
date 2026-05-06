# TTRacing Singapore CRO Research Brief

**Data Sources:** Meta Ads, Google Ads Transparency, Reviews & UGC, Page Speed / Core Web Vitals, Competitor Research, Site Screenshots

---

## Insights

TTRacing Singapore's biggest conversion problem is not traffic - it's trust. The brand has earned 20,100 reviews at 4.8 stars on Shopee and consistent praise for standing desk quality. None of that proof appears on the page the brand calls its most important: the Match & Make bundle deals page. Visitors arrive from paid search, see no evidence that anyone has bought or loved these bundles, and leave.

The numbers make this urgent. The Match & Make bundle page - where bundles start at $175 and reach $695+ - scores 19/100 on mobile performance. Lab data shows a 24.1-second LCP for first-time visitors. Every optimization on this page is already operating at a fraction of its potential. Fixing performance is the highest-leverage technical action available, outside any A/B test.

On the page itself, three problems converge. Every bundle card uses the same CTA: "Configure Now." The word configure implies a multi-step process, not a deal being claimed. Seven bundles are presented with three different badge types and two different savings formats - some show "Save up to $229," others show "Start from $175" with no savings signal at all. The countdown timer exists only in the announcement bar. There is no in-page urgency, no hierarchy between deals, and no social proof of any kind.

These are the same patterns documented in TTRacing's Australian site audit. This is a systemic issue across the brand's global properties, not a one-market anomaly.

The revenue case is straightforward. If the Match & Make page converts at 2% today, a 0.4% CR lift at $400 average bundle AOV across an estimated 5,000 monthly sessions delivers $8,000 in additional monthly revenue. Each slot below targets a distinct element of the same funnel. Replace session estimates with actual data from Shopify analytics to validate the opportunity size.

---

## Slot 1: Bundle Page Social Proof Bar + In-Page Countdown

**Type:** A/B test (1 variation vs. control)
**Page:** Match & Make bundle deals page (ttracing.sg/pages/match-make-bundle-deals)
**Revenue potential:** ~5,000 sessions/mo x 0.4% CR lift x $400 AOV = ~$8,000/mo. Insert actual monthly sessions from Shopify analytics to validate.

**Hypothesis:** If we add a social proof bar and visible countdown timer to the bundle page header, conversion will increase because visitors currently have no trust signal and no on-page urgency before reaching the bundle cards.

**Data:** The bundle page has zero reviews, ratings, or customer counts anywhere on the page (Source: Site Screenshots). The brand has 20,100 ratings at 4.8 stars on its Shopee store (Source: Meta Ad landing page, observed Apr 2026). The countdown timer exists only in the announcement bar, not in the page body (Source: Site Screenshots). Google Ads are actively driving traffic to this page with urgency-led copy ("Flash Sale Alert") that the page itself does not reflect (Source: Google Ads Transparency). The CRO ebook is explicit: "Reviews and Testimonials are absolutely required for virtually every type of product or service today. If you click an ad and go to a page with zero reviews, would you be comfortable buying?" (Source: CRO Ebook, Chapter on Social Proof).

**V1:** Add a two-element trust bar directly below the "Match & Make Sale" title and above the bundle cards. Element 1 is a star rating badge: five gold stars, "4.8 / 5 from 20,000+ customers" in a compact inline format. This figure comes from TTRacing's verified Shopee SG store ratings as of April 2026. Element 2 is an in-page countdown timer: "Sale ends in: [DD] [HH] [MM] [SS]" with a compact dark or red background pill, matching the announcement bar styling for visual consistency. The two elements sit on the same horizontal row, centered, between the page subheading and the first row of bundle cards. On mobile, the star badge stacks above the countdown timer, both centered, with 12px spacing between them. The announcement bar countdown can remain as-is. The bundle cards below are unchanged.

---

## Slot 2: Bundle Card CTA Copy

**Type:** A/B test (1 variation vs. control)
**Page:** Match & Make bundle deals page (ttracing.sg/pages/match-make-bundle-deals)
**Revenue potential:** ~5,000 sessions/mo x 0.3% CR lift x $400 AOV = ~$6,000/mo. Insert actual monthly sessions from Shopify analytics to validate.

**Hypothesis:** If we replace "Configure Now" with deal-affirming CTA copy on every bundle card, conversion will increase because "Configure" implies effort and complexity while visitors have already decided they want a bundle deal.

**Data:** "Configure Now" appears as the CTA on all 7 bundle cards across the page (Source: Site Screenshots). The same CTA was documented as a friction point in TTRacing's Australian site audit on a structurally identical Easter bundle page (Source: TTRacing AU audit, April 2026). The CRO ebook describes this mechanism: "The Gator takes the path of least resistance. If your website forces users to rely on their conscious minds to figure out what's happening, they'll get overwhelmed, frustrated, and leave" (Source: CRO Ebook). The word "configure" summons the Judge by implying a multi-step, effortful process. Paid visitors landing from "Flash Sale Alert" and "Best Deals" ads arrive in a deal-claiming mindset, not a configuration mindset.

**V1:** Replace "Configure Now" with "Claim This Bundle" on every bundle card button. Button styling (dark red, full-width within card, white text) remains unchanged. The circle-plus icon after the text can be removed or kept - keep if it increases perceived interactivity based on the brand's preference. On mobile, the button is full-width within the card, same as control. The change applies to all 7 bundle cards simultaneously so the test measures the copy, not a single card. No other changes to the cards.

---

## Slot 3: Bundle Card Savings Framing

**Type:** A/B test (1 variation vs. control)
**Page:** Match & Make bundle deals page (ttracing.sg/pages/match-make-bundle-deals)
**Revenue potential:** ~5,000 sessions/mo x 0.3% CR lift x $400 AOV = ~$6,000/mo. Insert actual monthly sessions from Shopify analytics to validate.

**Hypothesis:** If we standardize all bundle cards to show explicit dollar savings with a crossed-out original price, conversion will increase because visitors can immediately rank deals by value without doing mental arithmetic.

**Data:** The page currently uses two incompatible savings formats across 7 bundles (Source: Site Screenshots). Four bundles show "Save up to $X" in green. Three bundles show "Start from $X" with no savings signal - these include the KittyPuff voucher ($175.12), Productivity Combo ($359), and Bonus Drop ($339). The "Start from" format frames the bundle as a cost, not a deal. The highest-savings bundles (Save $229, Save $256) are not visually differentiated from the lowest-savings bundles (Save $53.88, Save $70.68). The CRO ebook: "Make prices obvious. Leverage the power of free" (Source: CRO Ebook, Buy Box chapter). Secretlab, TTRacing's primary competitor, uses consistent savings anchoring with strikethrough pricing across all product listings (Source: Competitor Research). Reviews confirm customers cite value as a primary purchase driver (Source: Reviews & UGC).

**V1:** Standardize all 7 bundle cards to a two-line savings format. Line 1 (green text, bold): "You save: $[X]" - always showing the dollar value saved, not the final price. For bundles currently showing "Start from $X," calculate and display the actual dollar savings. For the KittyPuff 12% off voucher, show the savings amount at the lowest eligible price. Line 2 (smaller, grey text): "From $[X]" with a strikethrough showing the original combined value. The current green "Save up to $X" text is replaced by this standardized block. The CTA button and card image remain unchanged. On mobile, the two-line savings block sits in the same position as the current savings text, stacked vertically within the card body. Cards currently missing a clear savings number should be confirmed with the brand before implementation to ensure accuracy.

---

## Future Slot Candidates

These ideas have data support but did not fit into the three prioritized slots. Queue for discussion in future months.

**Cart drawer checkout path:** "VIEW CART" is the only CTA in the cart drawer. Adding a direct "Checkout" button eliminates one step between purchase intent and payment. Same issue documented in TTRacing AU audit (April 2026). Low development effort, potentially high impact given every buyer passes through the cart.

**Homepage hero CTA hierarchy:** "LEARN MORE" (filled red button) is visually dominant over "SHOP NOW" (ghost button) on the homepage hero. The buttons are inverted relative to conversion priority. A simple button style swap could lift homepage-to-product-page clicks at zero design cost.

**Sizing confidence tool on gaming chair PDPs:** Four separate reviewers across SG and AU flagged fit issues (backrest too short above 170cm, seat depth causing knee pressure). Secretlab differentiates explicitly on sizing (S/Regular/XL with anthropometric specs). A simple inline sizing guide or height/weight-based recommendation on gaming chair product pages could reduce purchase hesitation and returns.

**Bundle page performance:** Match & Make LP scores 19/100 on mobile with a 24.1-second lab LCP. This is a technical sprint item, not an A/B test, but it is the single highest-leverage improvement available. Every split test on this page runs at diminished potential until performance is addressed.
