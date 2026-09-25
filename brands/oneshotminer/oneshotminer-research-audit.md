# Oneshotminer CRO Research Audit

## Data Sources Used

- Current Site Screenshots (homepage, collection, PDP, cart) — `raw/site-visual-summary.md` + `raw/screenshots/`
- Live homepage fetch (text-level content, 2026-09-08)
- PageSpeed / Core Web Vitals — `raw/pagespeed.md` (mobile, collected 2026-09-08)
- Reviews & UGC — `raw/reviews.md` (Trustpilot-style, mixed rating, Nov 2025-May 2026)

No Meta Ads, Google Ads, competitor research, inspiration sites, email campaigns, non-data context, or social/community research were collected for this brand (skipped per manifest — brand does not run paid ads).

## Source Findings

### Reviews & UGC

#### What Customers Love

- Ease of setup and plug-and-play simplicity: "Setup and assembly wasnt difficult at all. Align the pieces, screw it all together, and plug it in." (Ronnie Slater)
- Aesthetic/novelty appeal as a desk or room display piece: "these are still a really cool show piece to have in my gaming room / office area" (Zack Wiebe), "my miner looks awesome on my work desk!!" (carter miller)
- Responsive support when it works: "their tech experts can help you get the setup you need" (Dave), "I reached out to the company via Instagram and they walked me through the troubleshooting process" (Mark Spitzig)
- Educational value for crypto beginners: "I had never mined for Bitcoin... these little miners do indeed mine for Bitcoin... You buy these for the learning experience" (Gary Milam)
- Low power draw as a differentiator, echoed in customer language, not just marketing copy

#### What Frustrates Customers

- Non-delivery and vanished packages: "Product never arrived." (multiple reviewers), "Total Scam. Never received my miner and they kept the money." (Philip Kleudgen)
- Refund process described as deliberately drawn out past the credit-card dispute window: "keep you talking exactly long enough so that you miss the refund date. Funnily enough, almost to the day exact!" (anonymous, May 2026)
- Cancellation requests ignored even within the company's own stated 1-hour cancellation window: "Company does not honor their own terms of service." (Nathan)
- Support named repeatedly as a single point of failure ("Mia" cited by name in 3+ separate 1-star reviews) with scripted, repetitive replies: "the service is run by an AI bot that sends back the same basic answer every time" (TJ)
- Broken/non-functional units on arrival with no fix: "it would not connect to the internet so it could function... those also did not work" (John Hassell)
- Partial or staged refund offers (30% then 50% then "full") that don't materialize: "They then offered me a full refund. Suprise this didn't happen either." (John Hassell)
- Setup instructions criticized as poor or mistranslated: "took a day and minimal instructions either online or the badly translated instructions" (Martin, 2-star)
- Missing bundled items (stand, ebook) requiring repeated follow-up: "No ebook ever sent and no stand received." (Robert Ellington)
- Pricing discrepancy at checkout vs. site: "I realized I was overcharged from the amount the website charged me for the order." (Derek P)

#### Client-Actionable Insights

- Reviews show a bimodal pattern: 5-star reviews cluster around delivery-went-fine + product-works, while nearly every 1-star review centers on refund/cancellation/support process, not the physical product. This is an ops/support fix, not a CRO fix — but it directly threatens the trust claims made on-site (see Cross-Source Themes).
- The company does reply to negative Trustpilot reviews with personalized fixes, which is good practice, but the reply pattern ("please reach out to us directly") suggests the same resolution isn't happening proactively over email — the escalation-to-public-review step seems necessary to get resolution.
- Recommend auditing the stated 1-hour cancellation policy against actual fulfillment/support workflow — several reviewers cite this policy by name as violated.
- Consider a dedicated support ticket system or escalation path so customers aren't stuck in repeat email loops with one named rep.

### PageSpeed / Core Web Vitals

Mobile, collected 2026-09-08.

**Homepage** (https://oneshotminer.com/)
- Performance score: 79/100
- LCP: 4.5s (above the 2.5s "good" threshold)
- CLS: 0 (good)
- TBT: 150ms
- TTI: 16.8s

**PDP** (https://oneshotminer.com/products/one-shot-pro-edition/)
- Performance score: 63/100
- LCP: 22.0s (severely above threshold — nearly 9x the "good" 2.5s benchmark)
- CLS: 0 (good)
- TBT: 240ms
- TTI: 22.1s

The PDP is the primary conversion page and has the worst performance score and by far the worst LCP of any page measured. A 22-second LCP means the largest visible element (likely the hero product image or the buy box) is not fully rendered until well after most mobile users have bounced. TTI at 22.1s compounds this: the buy box (Add to Cart, variant selector, bundle tiers) is likely not reliably interactive until the same point.

### Current Site Screenshots

**Homepage:** Dark orange/black theme. Top of page opens with an announcement bar reading "BANKRUPT SALE | ENDS WHEN STOCK RUNS OUT," immediately followed by a hero headline built around the 3.125 BTC solo-mining reward angle, with a single CTA "CHOOSE YOUR MINER." No trust signals (review count, star rating, guarantee) appear anywhere in folds 1-3 of the homepage — first-party rating information (1420+ reviews, per the live fetch and PDP) is withheld from the page most new visitors land on. Below the hero, the page moves straight into a 10-card product grid, each card carrying the identical promotional badge text ("Join the race of solo mining 3.125 BTC by yourself"), which reads as repetitive and reduces the badge's persuasive value through repetition. The live fetch also surfaces four trust badges (Free Shipping, Secure Payments, Moneyback Guarantee, Customer Support) and a "1000+ five-star reviews section" that were not visible in the collected fold screenshots — indicating these trust elements likely appear lower on the page (past fold 3) or the fold captures didn't reach that section. This is a gap: if trust signals are below the fold, they arrive too late to counter the "BANKRUPT SALE" urgency framing at first impression.

**Collection page:** Grid layout with filter/sort controls and a "9 products" count. Strikethrough compare-at pricing and "SAVE X%" badges appear on nearly every card, with the discount percentage varying card to card (40%, 70%, 65%, 67%, 72%) — inconsistent discount depth across near-identical hardware tiers may read as arbitrary or manufactured pricing rather than genuine markdowns. One structural inconsistency: the footer menu labels the flagship product "One Shot Miner PRO (2025 Edition)" while the PDP and homepage both title it "(2026 Edition)" — a version-label mismatch that undermines confidence in a store already facing scam accusations in reviews.

**PDP (One Shot Miner PRO — 2026 Edition):** The buy box opens with a customer quote and a "★★★★★ (1420+ reviews)" rating line directly above the price — a strong trust signal, but one that lives only on the PDP, not the homepage. Price is shown as $59.99 struck through against $100.00, with a "40% Off Spring Sale" tag, layered against a stock-scarcity note ("Update: Our stock is running extremely low"). Three quantity/bundle tiers are offered (1 / 2 / 3+1 free), with "Buy 3 & get 1 Free" visually pre-highlighted as "Best value" — the pre-selected option is not the cheapest per-unit price, and no comparison of per-unit cost across tiers is shown to justify the recommendation. A "+ FREE BONUS - Top Crypto Currency Secrets eBook" banner sits inside the buy box, adding another value claim before the visitor reaches Add to Cart. Below the fold, a "How the $373,000 solo miner got their one-in-a-million win" testimonial-style story is used as social proof for the core 3.125 BTC pitch — this is the single most concrete, specific proof point on the page (named dollar figure, named date), but it sits in fold 3, well below the buy box, where a large share of mobile visitors given the LCP/TTI numbers above may never scroll.

**Cart drawer:** Shows "24/7 Support - Lifetime Warranty" banner at top and a "Last units left" urgency banner at the bottom, sandwiching the checkout button — reinforcing the same urgency-plus-warranty combination used throughout the funnel. Three upsell cards (Mining Rig, Gamma Shot Miner, Buy 9 Get 3 Free) are embedded directly in the drawer, duplicating the PDP upsell strip. No visible security/payment icons or return-policy copy inside the drawer itself, unlike the PDP which shows payment icons directly under Add to Cart.

## Cross-Source Themes

Ranked by evidence strength x revenue potential x funnel importance:

1. **Trust-signal placement doesn't match trust-signal need.** The homepage — the page carrying the heaviest urgency/scarcity framing ("BANKRUPT SALE," repeated badge overlays) — shows no reviews, ratings, or guarantee badges in the first three folds, while the PDP has strong, specific trust signals (1420+ reviews, named testimonial, lifetime warranty) that arrive after the buy box context is already set. Reviews independently confirm trust is this brand's actual weak point: nearly every 1-star review centers on broken promises (refunds, cancellations, delivery), which makes early, prominent trust signals more valuable here than for a typical store, not less.
2. **PDP performance is actively blocking conversion.** A 22-second LCP and 22.1s TTI on the exact page carrying the buy box, bundle tiers, and Add to Cart button means a meaningful share of mobile traffic likely never sees an interactive purchase path. This is evidenced directly by PageSpeed data and compounds every other PDP-side finding (buy box hierarchy, social proof placement) — none of it matters if the page hasn't rendered.
3. **Pricing/urgency mechanics lack internal consistency.** Compare-at discount percentages vary unexplained across near-identical products (40-72%), the pre-selected "best value" bundle tier isn't backed by visible per-unit math, and a version-label mismatch (2025 vs. 2026 Edition) exists between footer and PDP. Individually minor, but reviews show this audience is primed to read inconsistency as evidence of manipulation ("scummy," "scam," "total legal scam" appear repeatedly) — so pricing/label inconsistencies carry more conversion risk here than they would for a brand without this review pattern.

## Top Test Opportunities

**Fix PDP Largest Contentful Paint** — The PDP loads with a 22.0s LCP and 22.1s TTI (vs. 4.5s/16.8s on homepage), meaning the buy box is likely non-interactive for a large share of mobile visitors well past the point they'd abandon. Evidence: PageSpeed data. Est. lift: conservative 15% CR lift x sessions/mo (unknown) x AOV (unknown) = revenue impact undetermined without traffic/AOV data, but LCP at this magnitude typically drives double-digit mobile bounce increases.

**Add review count and star rating to homepage above the fold** — The homepage carries the heaviest urgency messaging ("BANKRUPT SALE") but shows zero trust signals (no rating, review count, or guarantee badge) in folds 1-3, while the PDP has a "★★★★★ (1420+ reviews)" line directly above its buy box. Evidence: site-visual-summary.md, live homepage fetch. Est. lift: 5-10% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined, directionally high given trust is the brand's documented weak point.

**Surface the named social-proof story earlier on PDP** — The "$373,000 solo miner win" testimonial with a specific date and dollar figure is the single most concrete proof point on the page but sits in fold 3, below where PageSpeed data suggests many mobile users disengage. Evidence: site-visual-summary.md (PDP fold 3), PageSpeed TTI data. Est. lift: 3-6% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined.

**Show per-unit cost math on bundle tiers** — "Buy 3 & get 1 Free" is pre-selected as "Best value" but no per-unit price comparison is shown against the 1-unit or 2-unit tiers, leaving the recommendation unsubstantiated at the moment of decision. Evidence: site-visual-summary.md (PDP buy box detail). Est. lift: 2-4% AOV lift x sessions/mo (unknown) x AOV (unknown) = undetermined.

**Standardize discount percentage logic across collection cards** — Compare-at discounts range 40-72% across similar-tier hardware with no visible justification, which risks reading as manufactured pricing to an audience already primed by reviews to suspect manipulation. Evidence: site-visual-summary.md (Collection page). Est. lift: 2-4% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined.

**Fix version-label mismatch between footer and PDP** — Footer menu links "One Shot Miner PRO (2025 Edition)" while the live product is titled "(2026 Edition)" on both homepage and PDP; a small credibility gap in a business already fighting a scam narrative in public reviews. Evidence: site-visual-summary.md (Collection page footer), PDP title. Est. lift: minor direct CR impact, primarily a trust-consistency fix.

**Add security/return-policy copy inside the cart drawer** — The cart drawer shows urgency ("Last units left") and a warranty banner but no visible payment/security icons or return-policy link, unlike the PDP which shows payment icons directly under Add to Cart. Evidence: site-visual-summary.md (Cart drawer). Est. lift: 1-3% checkout completion lift x sessions/mo (unknown) x AOV (unknown) = undetermined.

**De-duplicate repeated badge copy on homepage product grid** — All 10 homepage product cards carry the identical overlay text ("Join the race of solo mining 3.125 BTC by yourself"), diluting its impact through repetition rather than differentiating products. Evidence: site-visual-summary.md (Homepage fold 1-2). Est. lift: 1-2% CR lift x sessions/mo (unknown) x AOV (unknown) = undetermined.

## Unused but Valuable Findings

- Support is repeatedly named as a single point of contact ("Mia") in negative reviews, which is an ops/staffing finding, not a CRO test, but worth flagging to the client separately given its frequency.
- The stated 1-hour cancellation policy is cited as violated in multiple reviews — a policy-enforcement gap outside CRO scope.

## Missing Data

- No sessions/mo, AOV, or conversion rate baseline was provided or found in collected sources — all lift estimates above are directional (percentage lift only) and cannot be converted to dollar figures until traffic/AOV data is supplied.
- No Meta Ads, Google Ads, competitor, inspiration, email, or social/community research was collected (brand does not run paid ads per manifest) — cross-channel message-match analysis is not possible for this audit.
