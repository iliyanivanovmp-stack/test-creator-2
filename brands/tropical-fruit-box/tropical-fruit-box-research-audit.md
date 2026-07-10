# Tropical Fruit Box CRO Research Audit

## Data Sources Used

**User-provided:**
- Meta Ads visual summary (3 ads + landing pages)
- Google Ads visual summary (Shopping ads)
- Site screenshots visual summary (homepage, collection, PDP, cart)
- PageSpeed Lighthouse data — homepage and Best Sellers (collected 2026-06-23)
- Customer reviews — Taste the Tropics Fruit Box, REVIEWS.io (33 reviews, 7 months to 3 years old)

**Self-researched:**
- Live site fetch: tropicalfruitbox.com homepage and Best Sellers collection (fetched 2026-06-24)
- Competitor research: Miami Fruit, The Fruit Company, Fruit Gift of the Month (researched 2026-06-24)

---

## Source Findings

### Meta Ads & Landing Pages

**Ad 1 — Brand Awareness (active since Nov 7, 2025)**
Headline: "Level Up Your Flavor With Tropical Fruit Box." No offer. CTA: Shop now. Lands on Best Sellers collection. Announcement bar shows "PROMO: 20% OFF $89+" (live site uses code PRIME20). No dedicated banner or hero reinforces the promo on arrival. Visitors land directly into a 14+ product grid with no contextual welcome message or offer confirmation. Weak message match — the ad sets a discovery/flavor tone but the landing page gives no structured entry point.

**Ad 2 — Discount Offer (active since Jan 19, 2026)**
The entire hook is "Save $15 with code META15." Lands on the "Create Your Own Tropical Fruit Box" PDP at $119. META15 is not mentioned anywhere on the PDP — not in the announcement bar, not in the buy box, not anywhere. Visitors who clicked specifically to redeem a $15 discount arrive with no confirmation the code exists or works. This is a hard trust break at the most expensive PDP on the site.

**Ad 3 — Discount + Gifting (active since Jan 19, 2026)**
Hook: "Use SWEET15 to get $15 OFF." Body copy emphasizes gifting convenience ("short on time", "select when to send it"). Lands on the same Best Sellers collection as Ad 1. SWEET15 is not visible anywhere on the page. The gifting angle — the clearest emotional hook in the ad — finds zero reinforcement in the collection layout, copy, or product sorting. Visitors have to mentally bridge the ad promise to an unrelated product grid.

**Summary:** 2 of 3 active ads promise specific discount codes that are invisible on their landing pages. Both ads with codes (META15, SWEET15) are running simultaneously to the same destination or an adjacent page. This pattern suggests the codes were added as ad-level offers without any landing page coordination.

---

### Google Ads

Shopping-format ads only. Headlines are product- and flavor-specific: "Buy Fresh Cherimoya Fruit," "Fresh Soursop — Sweet & Creamy," "Taste the Exotics Fruit Box," "PinkGlow Pineapple." Free Shipping referenced in at least one listing. No discount codes in visible Shopping headlines.

**Gaps vs. Meta:** Meta runs brand-level awareness and code-based offers. Google Shopping runs SKU-level, descriptive, flavor-forward headlines. No shared messaging framework across channels. The gifting angle from Meta Ad 3 and the "exotic fruits you didn't know existed" brand line do not appear in Shopping ads. These channels appear to be managed independently with no cross-channel message architecture.

---

### Reviews & UGC

**Product reviewed:** Taste the Tropics Fruit Box (33 reviews, REVIEWS.io)

#### What Customers Love

- **Novelty and discovery.** Repeated delight at encountering fruits they had never seen or tasted. "They had new fruit experiences." "Some they have never seen before." "Have never eaten Maisy or golden berry." The discovery element is the core emotional driver.
- **Pink pineapple as a standout.** Mentioned across multiple reviews as the single most memorable item. "The pink pineapples almost sent me into shock they were so good. I literally closed my eyes and felt my whole body go weak." "Pink pineapples are worth every penny."
- **Gifting success.** Multiple reviews describe giving the box as a gift with strong recipient reactions. "Order Sunday, delivered in Ohio on Thursday." "My gift recipient was really impressed." "Everyone loved it!" "She was so so excited to receive it!" The gifting use case is consistently successful and self-reported.
- **Fruit quality and freshness.** "Sun ripened scrumptiousness." "All the fruits was ripe, juicy and very flavorful." "Everything was delicious!" General quality satisfaction across reviewers.
- **Identification cards.** One detailed review specifically called out the fruit ID cards: "The identification cards were especially helpful so we knew how to cut into the fruits and when they were ripe enough to eat." This is a conversion-relevant differentiator with zero visibility in ads or on-site.
- **Packaging and presentation.** Box quality noted as gift-appropriate. "This lovely Tropical Fruit Box." "Most beautiful fruit."

#### What Frustrates Customers

- **Ripeness inconsistency.** One review: "Most of the fruit was over ripe and had to be eaten the day we received it to avoid throwing it away." Another: "my bananas came in mushed so I made a smoothie with them." A third noted a negative experience with the avocado specifically.
- **Low review volume on some products.** The Create Your Own PDP (Ad 2's landing page) shows only 1 review with no written content. This undermines the trust of code-motivated traffic arriving on a $119 item.

#### Client-Actionable Insights

- **Proactive ripeness communication.** One reviewer noted that "the fruit is shipped with fruit in differing stages of ripeness so we won't have to eat all at once" and framed it positively. This is intentional product design that other reviewers interpret negatively. A post-purchase email explaining staggered ripeness as a feature (not a defect) would reduce disappointment and returns.
- **Build review volume on high-traffic PDPs.** The Create Your Own PDP has 1 review. It's the landing page for a $15-off discount ad. A review request sequence targeting recent purchasers of that SKU should be prioritized.
- **Fruit ID cards are a hidden differentiator.** No mention of identification cards in any ad, on the homepage, or in the site-visual-summary buy box. This is a tangible physical feature that reduces the anxiety of ordering unfamiliar fruit — it belongs in the product description and potentially in ad creative.

---

### PageSpeed / Core Web Vitals

**Data collected:** 2026-06-23, mobile emulation (Lighthouse 13.2.0)

| Metric | Homepage | Best Sellers |
|---|---|---|
| Performance Score | 51 | 52 |
| Accessibility Score | 69 | 68 |
| Best Practices Score | 77 | 77 |
| SEO Score | 85 | 85 |
| First Contentful Paint | 2.8s | 3.2s |
| Speed Index | 15.5s | 11.6s |
| Largest Contentful Paint | **12.0s** | **8.6s** |
| Time to Interactive | **51.6s** | **43.6s** |
| Total Blocking Time | 420ms | 330ms |
| Cumulative Layout Shift | 0.01 | 0.00 |

**Assessment:** Both pages fail on mobile. An LCP of 12.0s on the homepage means the main visible content takes 12 seconds to load on a mid-range mobile device — Google's threshold for "Poor" is 4s. A Time to Interactive of 51.6s means the page is unresponsive to taps for nearly a minute after navigation. The Best Sellers page (primary paid traffic destination) is marginally better at 8.6s LCP and 43.6s TTI — still deeply in "Fail" territory by any standard. CLS is clean on both pages (no layout instability). Server response time is healthy (10-20ms), indicating the bottleneck is JavaScript execution and render-blocking resources on-client, not server-side latency. Total Blocking Time of 330-420ms confirms heavy JS on the main thread.

These scores represent a pre-conversion leak that exists before any on-page CRO can take effect. A visitor who clicks a Meta ad and waits 43+ seconds for the page to respond is likely to bounce before seeing any offer, product, or trust signal.

---

### Competitor Analysis

**Self-researched, 2026-06-24**

| | Tropical Fruit Box | Miami Fruit | The Fruit Company |
|---|---|---|---|
| Price range | $49–$149 | $147–$277 | ~$40–$80/month |
| Focus | Exotic/tropical, gifting | Tropical, farm-to-door | General fruit clubs |
| Reviews | ~192 on flagship SKU | 6,000+ (stated) | Broad ratings |
| Origin story | Women-owned, Miami FL | South Florida farm | Pacific Northwest |
| Subscription | 10% Subscribe & Save | VIP Club | Multiple club tiers |
| Active promo | PRIME20 (20% off $89+) | SUMMER2026 (30% off select) | — |
| Key differentiator | Variety + gifting, lower entry price | Volume of reviews, media coverage | Legacy brand trust |

**Key findings:** Miami Fruit is the most direct competitor and commands significantly higher prices ($147+ vs. $109 entry). Their review volume (6,000+) dwarfs Tropical Fruit Box's (~192 on the flagship). The price gap suggests Tropical Fruit Box occupies a "premium but accessible" position — a meaningful advantage if communicated. The fruit ID cards and women-owned brand story are differentiators Miami Fruit does not appear to lead with.

---

### Current Site Screenshots

**Homepage:** Hero is clean and confident — "Farm-Fresh, Tropical & Exotic Fruits – Delivered to You!" with dual CTAs (Variety Boxes / Build Your Box). Press logos (Chowhound, The Spruce Eats, BYRDIE, Fodor's) and BBB badge appear immediately after the hero — good trust placement. Product sections follow: Popular, Mango, Exotic. No review section or UGC on the homepage. No sticky social proof while scrolling. The announcement bar shows the promo code (PRIME20: 20% OFF $89+) but this is the only place the offer lives — there is no persistent reinforcement as users scroll into product sections. Cookie consent banner pinned to the bottom of fold 1 competes with the CTA row.

**Best Sellers collection:** "Best Sellers" as the page title — no subheadline or contextual frame. 3-column grid, Featured sort default. 14+ products with no filter panel — no way to narrow by price, occasion, fruit type, or recipient. The announcement bar promo is not echoed with any in-page banner or editorial section. Product cards show title, price (with struck-through sale pricing), and stars. Badges (BEST, NEW, % OFF) are inconsistent — no systematic badging logic visible. One product card appears in black-and-white (likely out of stock), which reads as a dead end in the grid. The "20% OFF $89+" offer applies to most products in this price range but there is no banner, callout, or visual indicator within the grid to help visitors identify qualifying products.

**PDP — Taste the Tropics Fruit Box:** Buy box is dense but well-structured. Fold 1 includes: scarcity ("1 LEFT IN STOCK"), struck-through price ($109 was $149), size variants, greeting card options (6 choices including Birthday, Anniversary, Easter), subscribe/save toggle ($109 vs. $98.10), quantity stepper, Add to Cart, trust badge strip, and Buy with Shop Pay. This is a lot of content above the fold — the greeting card selector is prominent, which reinforces the gifting use case well. Social proof popup and live chat widget visible in fold 2. 4.78 stars from 192 reviews with photo gallery from customers. The PDP is relatively well-optimized for conversion; the main gap is that the active promo code (PRIME20) is not called out in the buy box itself.

**Cart (drawer):** Slide-out drawer with good AOV structure. Two add-on sections visible: Pink Pineapple add-on ($15, valid on orders over $89) and "You May Also Like" with Sunshine card ($5) and Pink Pineapple Gift Box ($49). Shipping protection ($3, defaulting ON) adds a small revenue line. Subscription upsell button ("Upgrade to Subscription & Save 10%") is the first element below the item. Cart expiry countdown ("Your cart expires in 14:48") creates urgency. TropiRewards loyalty program mentioned at the bottom. Cart AOV mechanics are more developed than the collection page would suggest. The main missed opportunity: no place in the cart references the PRIME20 discount code — a visitor who is $10 short of the $89 qualifying threshold gets no prompt.

---

## Cross-Source Themes

**Ranked by evidence strength × revenue potential × funnel importance:**

**1. Discount code message match failure (Evidence: Meta Ads 2 & 3 + landing page analysis)**
Two active ads simultaneously promise $15 discounts via unique codes (META15, SWEET15). Neither code appears on the landing page. This affects every visitor who clicked an offer-motivated Meta ad — a segment that, by ad design, represents higher purchase intent. The fix is cosmetic (a single banner or announcement bar swap per audience), yet the revenue leak is proportional to paid spend on those ads.

**2. Site performance at fail-level on mobile (Evidence: PageSpeed — both pages)**
Homepage TTI 51.6s, LCP 12.0s. Best Sellers TTI 43.6s, LCP 8.6s. Both primary pages fail Google's Core Web Vitals thresholds by a factor of 5-10x on mobile. This is a pre-conversion leak — a meaningful percentage of paid traffic bounces before any CRO can engage them. TBT of 330-420ms indicates a JavaScript-heavy payload.

**3. Collection page lacks guided selling on a complex catalog (Evidence: Site screenshots + live fetch)**
Best Sellers is the primary paid traffic landing page (2 of 3 Meta ads point here). It has 14+ products and no filter panel — no occasion filter, no price filter, no fruit type filter. Visitors with gift-buying intent (the dominant use case from reviews) have no way to narrow by "for her," "under $100," or "first-timer." The catalog is large enough to cause decision paralysis.

---

## Top Test Opportunities

**1. Discount Code Landing Banner — Best Sellers (SWEET15/META15 traffic)**
Ad 3 promises "Use SWEET15 to get $15 OFF" but the Best Sellers page shows no mention of SWEET15. Every visitor arriving via that ad faces an immediate trust gap. Test: inject a persistent welcome bar or above-the-fold banner for Meta ad traffic that reads "Your $15 off is ready — use SWEET15 at checkout" with a shop button below it.
Evidence: Meta Ad 3 visual summary, live site fetch. Est. lift: +8–12% CR on this traffic segment × [unknown sessions] × ~$109 AOV = material given ad-level spend.

**2. Discount Code Confirmation Banner — Create Your Own PDP (META15 traffic)**
Ad 2's entire hook is the META15 code. Landing page shows zero code confirmation. Test: add a code-confirmation banner in the announcement bar or buy box header that reads "META15 applied at checkout — $15 off your order" for this audience segment.
Evidence: Meta Ad 2 visual summary, live PDP site-visual-summary. Est. lift: +10–15% CR on META15-motivated traffic × ~$119 AOV.

**3. Collection Page Occasions Filter or Editorial Sections**
Best Sellers has no filtering. Gifting is the primary conversion driver (reviews, ad copy, PDP greeting card options). Test: add an occasions-based editorial row above the product grid ("Shopping for a gift? → Browse Gifting Boxes") or a filter panel with "Occasion," "Price Range," and "Fruit Type" options. This reduces decision paralysis for gift-buyers and creates an on-ramp for discovery-mode visitors.
Evidence: Site-visual-summary (collection page), reviews (gifting use case dominant), Meta Ad 3 (gifting angle). Est. lift: +5–10% CR on Best Sellers traffic × sessions × ~$109 AOV.

**4. Fruit ID Cards as a Trust Signal in Buy Box**
The identification cards included in each box are mentioned by at least one detailed reviewer as the feature that made the exotic fruit experience accessible. This differentiator is absent from all ads, the homepage, and the PDP buy box. Test: add a single line in the buy box below the product title — "Includes fruit ID cards: how to cut, when it's ripe" — or add it as a trust badge icon in the badge strip.
Evidence: Review (Brian F, 3 years ago), site-visual-summary (no ID card mention on PDP). Est. lift: +2–4% CR on PDP × ~$109 AOV (low estimate given small footprint of change).

**5. Performance Fix — Best Sellers LCP and TTI**
LCP 8.6s and TTI 43.6s on the primary paid landing page is a pre-funnel leak. TBT of 330ms suggests deferring or removing non-critical JS. Test: audit and defer third-party scripts (chat widget, social proof popup, app download banners) that load in the head. Target: LCP under 4s, TTI under 10s.
Evidence: PageSpeed — Best Sellers (2026-06-23). Est. lift: industry baseline for LCP improvements from 8s→4s on mobile is 15–25% bounce rate reduction. Revenue impact scales with total paid traffic volume.

---

## Unused but Valuable Findings

- **TropiRewards loyalty program** is mentioned only at the bottom of the cart drawer — no homepage or collection page placement. Could be a secondary test on the Best Sellers page (loyalty sign-up = email capture + repeat purchase signal).
- **Subscribe & Save** toggle exists on the PDP but is not surfaced on collection cards or the cart drawer prominently. Subscription acquisition at the collection level (e.g., "Subscribe & save 10%" callout on product card) could lift LTV without changing AOV.
- **Miami Fruit pricing gap**: Miami Fruit's entry price is $147 vs. Tropical Fruit Box's $109. This 26% price advantage is never stated explicitly on-site in a comparison or value frame. A "premium quality, accessible price" message has competitive evidence but no current expression in ads or landing pages.
- **Accessibility score of 68-69** on both pages may indicate color contrast or labeling issues that compound the mobile performance problem. Not a standalone test but worth auditing during a performance sprint.
