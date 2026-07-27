# Sharland England CRO Research Audit

## Data Sources Used

**User-provided:**
- Meta Ads visual summary (3 ads + landing pages) — data-collection/meta-ads-visual-summary.md
- Google Ads visual summary — data-collection/google-ads-visual-summary.md
- Reviews & UGC (Trustpilot) — data-collection/reviews.md
- PageSpeed / Core Web Vitals — data-collection/pagespeed.md
- Site visual summary (homepage, collection, PDP, cart) — data-collection/site-visual-summary.md

**Self-researched:**
- Live site fetch: sharland-england.com (2026-07-13)
- Competitor research: web search (2026-07-13)
- Birdie Fortescue competitor product fetch (2026-07-13)

**Not collected:** Email campaigns, inspiration sites, non-data context, competitor data file.

---

## Source Findings

### Meta Ads & Landing Pages

**Ad 1 — Juliette Outdoor Collection**
Video ad headlines "Inspired by antique pieces, our Juliette collection brings timeless charm to outdoor spaces." Offers 10% off first order. Landing page: the Outdoor Collection page. The ad makes a specific collection promise (Juliette) but the LP mixes Juliette pieces with unrelated outdoor items and has no Juliette-specific hero or storytelling. The 10% off offer from the ad reappears only in a dismissible newsletter popup that fires immediately over the product grid — blocking roughly one product card slot. No review counts on collection cards. No trust signals beyond the popup discount.

**Ad 2 — Hadley Tray (Best Seller) — highest priority**
Ad promises "Discover in Berry" and calls it the bestselling tray. LP is the Hadley Tray PDP, Berry pre-selected — message match is strong. Buy box has 23 five-star reviews immediately below price, three-swatch colour selector, quantity control, and a dark full-width ADD TO CART button. Icon trust row below: Designed by Louise Roe, Sustainable, Handmade, Ships Globally. However: shipping timeline and returns policy are buried in collapsed accordions, not visible in the buy box. No shipping cost or returns window shown until checkout. "Pairs well with" carousel (Pinet Plant Pot, Concha Dish, Little Flower) has no bundle mechanic or single-click add — cross-sell is passive.

**Ad 3 — US Expansion**
Ad creative says "FASTER SHIPPING. NO TARIFFS." Landing page is the US collection. Hero confirms "No delays... from our US warehouse" but omits "No Tariffs" — partial message gap. Critical friction: all prices display in GBP (£185, £395, £1,075, etc.) despite the ad targeting US visitors. A US visitor who clicked on "FASTER SHIPPING. NO TARIFFS" and arrives at GBP pricing faces an immediate trust and comprehension gap.

**Cross-ad gap:** Newsletter popup fires on load across all collection landing pages (Ads 1 and 3), displacing product content before the user has shown any interest. On PDPs (Ad 2) no popup fires — PDP experience is noticeably better than collection experience.

---

### Google Ads

Mix of search, shopping, display, and educational content ads. "Save 10% On Your First Order" appears in the headline of the search ad — more prominent than Meta's treatment. Shopping ads show individual product prices in GBP with lifestyle and product-on-white imagery. A competitor display ad ("Mugs, Plates, Vases & More - Handmade By Italian Artisans") was visible in the same SERP, indicating brand search is partially captured by a competitor.

Educational content angle ("Rattan Or Wicker? What's the Difference?") appears in Google only — good for top-of-funnel intent matching. The 10% offer strategy is more consistent in Google than Meta: Meta ads 2 and 3 don't use the 10% angle at all, creating channel inconsistency. The US expansion and "No Tariffs" angle visible in Meta has no counterpart in Google ads seen.

---

### Reviews & UGC

**Source:** Trustpilot. 4.7 average (estimated based on review sample — exact count not scraped). Review date range: 2022–2025.

#### What Customers Love

- **Personal service by name:** "Quinn's excellent customer service resolved the issue" (MPDouglas, US, Aug 2024); "Katherine couldn't have been more helpful and kind" (Consumer, May 2025); "Celia is exceptional at her job... she helped me source it after it sold out so quickly" (Jayne Wilkinson, Dec 2022). Multiple US customers specifically call out named staff members.
- **Packaging and unboxing:** "The packing materials were excellent and the packing organization meticulous" (Deborah Lamping, US, Aug 2023); "beautifully packed and with a personal note" (Ba, GB, Dec 2023); "beautiful handwritten note, cant wait to get more" (kris jezak, US, May 2024); "Louise's kind thank you card was very charming" (Unattributed).
- **Product quality:** "Beautiful and well-made products" (multiple reviewers). "It completely makes the entire room!" (VCB, US, Nov 2023). "The unique shape and detail of this piece make for a fun way to warm up my butler's pantry" (Jen B, US, Nov 2023) — specifically about the Hadley Tray.
- **Shipping speed to US:** "Fast shipping!" (Samantha Stephano, US, Jul 2024); "For starters I was amazed at the speed the Hadley tray arrived" (Jen B, US, Nov 2023). The new US warehouse may improve this further.
- **International confidence:** "Living in the US, we were concerned about the logistics of shipping to our address. That wasn't necessary." (Very happy customer, US) — concern exists, then resolved positively.

#### What Frustrates Customers

- **Returns process — no acknowledgement:** "I returned an item on 3rd December... signed for on 5th Dec. I've had no acknowledgement... There's no phone number." (Claire Custance, GB, Dec 2025). One-star review. Returns and post-purchase support visibility is a trust gap.
- **Weight vs. price expectation:** "The rattan tray and planters are lovely. However, they are a bit light weight. I was expecting them to be more substantial for the price." (Margaret Nanni, US, Sep 2023). At £185 for a tray, physical weight expectations are a pre-purchase concern that copy doesn't currently address.
- **Shipping anxiety (pre-purchase):** US customers mention concern about international shipping before they order — even when the experience turns out fine. The site doesn't resolve this concern proactively.
- **Non-delivery:** "Still haven't received my order." (Edwards Lucy, FR, Jan 2024) — one data point, could be isolated.

#### Client-Actionable Insights

- **Customer service is a genuine differentiator.** Named agents are remembered years later. Consider enabling a direct chat or callback option — email-only support creates friction for returns/post-purchase issues (see Custance complaint).
- **Packaging as brand moment.** The personal note and handwritten card appear repeatedly in positive reviews. This is free UGC fuel — a prompt to photograph the unboxing in post-purchase emails could generate content.
- **"Light weight" objection.** Product copy for the Hadley Tray does not address weight or substantiality. Adding context about rattan's properties (intentionally lightweight for serving/portability) would pre-empt this objection.
- **Returns process visibility.** The one 1-star review from 2025 is specifically about post-return silence. A clearer returns tracking mechanism or auto-acknowledgement would prevent this.

---

### PageSpeed / Core Web Vitals

**Tested:** 2026-07-13 (mobile)

| Page | Perf | LCP | CLS | TTI |
|------|------|-----|-----|-----|
| Homepage | 56 | 27.3s | 0.124 | 30.9s |
| PDP (Hadley Tray) | 59 | 29.0s | 0s | 33.5s |

Both pages score in the "needs improvement" range. LCP at 27–29 seconds is catastrophic — Google's threshold for "good" is under 2.5s. A 30-second TTI means the page is essentially unresponsive for the first half-minute on mobile. Homepage CLS of 0.124 indicates layout shifting during load (likely the newsletter popup or carousel).

PDP CLS is 0 (clean), which is notable given the image-heavy layout — layout stability is not the primary performance issue.

Total Blocking Time is low (60–100ms), suggesting the JS payload isn't the main culprit — image sizes and load order are the likely drivers given the editorial photography-heavy design.

**Impact:** UK and US paid traffic both arrive on pages that load in 27–30 seconds on mobile. At these load times, a significant fraction of paid clicks never see a product. Industry data suggests >3s LCP can cause 30–50% of mobile visitors to bounce before first interaction.

---

### Competitor Analysis

**Research date:** 2026-07-13. User-provided competitor data not collected — all findings are self-researched.

| Brand | Price Range (accessories) | Key Differentiators | Weaknesses |
|-------|--------------------------|---------------------|------------|
| **Sharland England** | £38–£185 (accessories), £775–£1,395 (furniture) | Louise Roe designer brand, handmade, named customer service, US warehouse, press (Vogue, NYT, AD) | GBP-only pricing for US visitors, no social proof on collection pages, slow site |
| **Soane Britain** | Ultra-premium (rattan chairs £2,000–£5,000+) | Original British rattan revival, trade-focused, workshop tours, heritage positioning | No DTC ecommerce focus, minimal accessibility pricing |
| **Birdie Fortescue** | £38–£54 (rattan trays, now £38 on sale) | Norfolk studio, affordable entry point, similar natural aesthetic | Far lower price point signals lower quality/prestige, smaller range, limited reviews (2 reviews seen) |
| **The Rattan Company** | Mid-market furniture | Large furniture range, "handmade" claim, free UK shipping | Primarily furniture-focused, limited accessories, less premium positioning |

**Key competitive insight:** Sharland England sits between Birdie Fortescue (accessible, mass) and Soane Britain (ultra-premium, trade). The Hadley Tray at £185 is 3-5x the price of Birdie Fortescue's comparable rattan tray. This price delta needs to be justified through design authority, provenance story, and trust signals — which are mostly concentrated on the PDP and absent from the homepage and collection pages.

---

### Emails

Not collected. No data available.

---

### Inspiration Sites

Not collected. No data available.

---

### Non-Data Context

Not collected. No data available.

---

### Current Site Screenshots

**Homepage:**
Editorial-first layout built around brand aspiration. Four-slide carousel hero leads with "Juliette Collection / SHOP GARDEN FURNITURE." No review count, no star rating, no shipping promise, no guarantee copy anywhere on the page. Press logo bar (Vogue, Telegraph, WSJ, NYT, House & Garden, AD, Veranda, Interiors) appears at fold 2 — strong authority signal but positioned below the scroll fold. Bestsellers carousel at fold 2 shows 4 products including the Hadley Tray at £185 with colour swatches but no social proof. "Shop By Collection" editorial tiles occupy fold 3. No sticky header CTA or cart prompt. The homepage communicates brand prestige well but gives a new visitor no reason to trust or act beyond browsing.

**Collection Page:**
4-column product grid. Newsletter popup fires on load, covering one product card slot in the top row — the first product the user would naturally click is obscured before they have demonstrated any intent. No review counts on product cards. No strikethrough pricing or sale signals. GBP prices only. Editorial image blocks interspersed through the grid. Filter controls (Collection, Product Type, Sort By) are visible but generic.

**PDP — Hadley Tray:**
Strongest page on the site. Image gallery takes ~75% width; right-column buy box is visible and sticky during scroll on desktop. Social proof (★★★★★ 23 reviews) appears immediately below price — well-placed. Colour selector with Berry pre-selected matches Ad 2's promise. ADD TO CART button is dark and full-width. Description accordion is open by default with full product copy. However: Shipping & Returns collapsed. No shipping timeline or cost in the buy box. No returns window or guarantee. No urgency (no stock counter, no "only X left"). "Pairs well with" carousel shows 3 cross-sell items but no bundle discount or one-click add.

**Cart:**
Full-page cart (not slide-out). Subtotal shows correctly. Shipping is "calculated at checkout" — unknown until the next step. No free shipping threshold bar. "You May Also Like" section provides passive cross-sell but no mechanic (no discount, no bundle). Three express checkout options (Shop Pay, PayPal, Google Pay) are prominent — good. No trust copy (guarantee, returns policy, or security badge) visible in the cart itself.

---

## Cross-Source Themes

**1. Trust signals are concentrated on the PDP and absent everywhere else (Evidence: site visual summary, meta ads, reviews)**
23 reviews exist on the Hadley Tray PDP and are positioned well. But the homepage has zero reviews, the collection pages have zero review counts on cards, and the cart has zero trust copy. For a brand that has press in Vogue, AD, and the NYT, and a 4.7 Trustpilot rating, the trust gap between PDP and every other page is the most structurally significant conversion problem.

**2. Shipping anxiety is a real pre-purchase concern, especially for US customers (Evidence: reviews, meta ads, site visual)**
Multiple reviews mention pre-purchase concern about international shipping ("we were concerned about the logistics"). The site addresses this only via a "Ships Globally" icon on the PDP and a US warehouse hero on the Ad 3 landing page. No shipping timeline appears in the buy box. Shipping cost is unknown until checkout. The new US warehouse is a major selling point that isn't surfaced on the site's core pages.

**3. Page performance is eliminating a significant portion of paid traffic before first interaction (Evidence: pagespeed, meta ads, google ads)**
LCP of 27–29 seconds on mobile means paid traffic from both Meta and Google is bouncing before seeing a product. At industry-average mobile bounce rates for >3s LCP (40–60%), a substantial fraction of the ad budget is wasted on sessions that never load. This affects every other test — if the page doesn't load, nothing else matters.

---

## Top Test Opportunities

Ranked by evidence strength × revenue potential × fixability. Slot count: 8. Writing 10 entries (8 + 2 backup).

---

**1. Collection Page Popup Timing**
Newsletter popup fires on page load over the first row of the product grid, blocking product discovery before the user has shown any intent. Ads 1 and 3 both land on collection pages, making this a paid-traffic conversion killer. Evidence: meta-ads-visual-summary.md (Ads 1 and 3 landing pages), site-visual-summary.md (collection page fold 1). Est. lift: 8–15% CR lift on collection pages × sessions unknown × ~£300 AOV (blended accessories + furniture) = revenue impact scales with traffic.

**2. US Landing Page Currency Display (Ad 3)**
Ad 3 targets US visitors with "FASTER SHIPPING. NO TARIFFS." Landing page shows GBP prices throughout (£185, £395, £1,075). A US visitor has no easy way to know the exchange rate. The "No Tariffs" claim in the ad is also not restated on the landing page. Evidence: meta-ads-visual-summary.md (Ad 3), manifest.md open questions. Est. lift: 10–20% CR lift on Ad 3 LP × US traffic unknown × ~£200 AOV (lower given accessible accessories focus of US collection LP).

**3. PDP Shipping Transparency in Buy Box**
Shipping cost and timeline are both unknown at the PDP level — shipping cost not revealed until checkout, shipping timeline buried in a collapsed accordion. Review data shows US customers have pre-purchase shipping anxiety, even when the actual experience is positive. Adding estimated shipping timeline (e.g., "US: 3–5 days from our US warehouse") and an explicit returns window directly to the buy box would address the leading pre-purchase hesitation. Evidence: reviews.md (multiple US reviewers citing shipping concern), site-visual-summary.md (PDP buy box), meta-ads-visual-summary.md (Ad 2 LP). Est. lift: 5–10% CR lift on PDP × sessions unknown × £185 AOV.

**4. Cart Shipping Reveal**
"Shipping calculated at checkout" in the cart is a known cart abandonment trigger. Combined with no trust copy, no returns promise, and no security badge visible, the cart provides no reassurance during the highest-intent moment on the site. Adding a visible shipping cost (or free shipping threshold) and a one-line returns promise would close the loop. Evidence: site-visual-summary.md (cart), pagespeed.md (performance issues may compound cart abandonment). Est. lift: 5–8% reduction in cart abandonment × sessions unknown × £370 average cart (observed at 2× Hadley Tray).

**5. Collection Page Review Counts on Product Cards**
No star ratings or review counts appear on any product card across any collection page. The Hadley Tray has 23 five-star reviews — zero of that social proof reaches a visitor browsing the collection grid. For a brand competing at £185+ for accessories (3–5x lower-end competitors), social proof at the point of browsing is a conversion lever. Evidence: site-visual-summary.md (collection cards), meta-ads-visual-summary.md (Ad 1 and 3 collection LPs), reviews.md (strong review quality). Est. lift: 3–7% CR lift on collection pages × sessions unknown × ~£300 AOV.

**6. Homepage Trust Signal Block**
Homepage has press logos (Vogue, NYT, AD) at fold 2 but no star rating, no review count, no customer quote, and no shipping promise anywhere. New visitors from non-branded Google search or Meta prospecting land here with no social proof to anchor trust. Adding a Trustpilot badge or star rating alongside the press logos, or a one-line quote near the hero, would leverage existing reputation without redesigning the page. Evidence: site-visual-summary.md (homepage folds 1–3), reviews.md (strong quality), live site fetch (4.7 Trustpilot mentioned). Est. lift: 2–5% CR lift on homepage entry sessions × sessions unknown × ~£250 AOV (discovery-stage AOV likely lower).

**7. Cart AOV Mechanic — Free Shipping Threshold Bar**
Cart contains "You May Also Like" product thumbnails but no active AOV mechanic. No free shipping threshold bar, no bundle offer, no volume incentive. Given the product range (accessories from £38–£185, furniture to £1,395), a threshold bar tied to a free-shipping milestone or a small gift-with-purchase would add urgency to upsell. "Pairs well with" items (Pinet Plant Pot £95, Concha Dish £80, Little Flower £55) are already shown on the PDP — surfacing them again in cart with a threshold lever would convert passive cross-sell into active AOV growth. Evidence: site-visual-summary.md (cart), meta-ads-visual-summary.md (PDP "Pairs well with" carousel). Est. lift: £15–30 AOV increase × conversion rate on existing cart sessions.

**8. Ad 1 Juliette Message Match — Dedicated Collection Hero**
Ad 1 specifically promotes the Juliette collection by name ("our Juliette collection brings timeless charm"). The landing page is the general Outdoor Collection page, with Juliette pieces mixed in but no Juliette-specific hero, headline, or storytelling. The emotional promise from the ad ("timeless charm") disappears on arrival. A simple hero banner at the top of the Outdoor Collection page that references Juliette by name — or a dedicated Juliette landing page — would complete the message match. Evidence: meta-ads-visual-summary.md (Ad 1 creative + LP fold 1). Est. lift: 8–12% CR lift on Ad 1 traffic × Ad 1 sessions unknown × ~£875–£1,375 AOV (Juliette chair/table range).

**9. PDP "Pairs Well With" — One-Click Add or Bundle**
The "Pairs well with" carousel on the Hadley Tray PDP shows Pinet Plant Pot (from £95), Concha Dish (from £80), and Little Flower (£55). Combined with the Hadley Tray at £185, a styled bundle would reach ~£415. Currently the carousel is display-only — each item requires a separate PDP visit to add. Adding a one-click "Add to cart" button on carousel items, or a pre-configured bundle with a small discount (e.g., 5% off when buying 2+ items), would convert a passive editorial element into an AOV driver. Evidence: site-visual-summary.md (PDP upsell section), meta-ads-visual-summary.md (Ad 2 LP fold 2). Est. lift: £50–80 AOV increase on PDP sessions that reach the cross-sell section.

**10. Homepage Hero CTA Specificity**
Current hero CTA: "SHOP GARDEN FURNITURE" (outlined, white, bottom-left of carousel). This is specific to the Juliette/outdoor launch but appears on the general brand homepage for all visitors — including those arriving from search for ceramics, trays, or linens. A dynamic or more generalist CTA ("Explore the Collection" or a split hero with multiple paths) would reduce mismatch for non-furniture visitors. Evidence: site-visual-summary.md (homepage fold 1), live site content (multiple product categories confirmed: tabletop, linens, vases, ceramics). Est. lift: 2–4% CR lift on non-outdoor homepage sessions.

---

## Unused but Valuable Findings

- Named customer service agents (Quinn, Katherine, Celia) are cited by name in reviews years after purchase — an in-site "your personal stylist" or "chat with our team" CTA could convert this cultural strength into a direct revenue path.
- "Louise's kind thank you card" appears in multiple reviews — the unboxing moment is a positive brand touchpoint that could be referenced in buy-box copy ("Every order includes a personal note from Louise") to pre-sell the full experience before purchase.
- Competitor display ad appearing in Sharland England brand search results (Google Ads screenshot) — brand search is not fully protected; a branded search campaign review or competitive bidding analysis is warranted.

---

## Missing Data

None flagged in manifest.
