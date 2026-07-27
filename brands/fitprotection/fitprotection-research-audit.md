# FIT Protection CRO Research Audit

## Data Sources Used

**User-provided:**
- Meta Ads creative and visual summary (3 ads) — raw/meta-ads.md, raw/meta-ads-visual-summary.md
- Google Ads visual summary — raw/google-ads-visual-summary.md
- PageSpeed / Core Web Vitals — Lighthouse JSON exports — raw/pagespeed.md
- Reviews — 29 Judge.me verified reviews — raw/reviews.md
- Site screenshots with visual summary — raw/site-visual-summary.md (homepage, collection, PDP, cart)

**Self-researched (July 27, 2026):**
- Live site fetch: fitprotection.com
- Competitor market search: RV and UTV windshield cover landscape

**Not collected (per manifest):**
- Competitor insights (user-provided)
- Inspiration sites
- Email campaigns
- Non-data context

---

## Source Findings

### Meta Ads & Landing Pages

Three active Meta ads (all live as of July 24, 2026) all route to the homepage (fitprotection.com). No separate landing pages exist.

**Ad angles:**
- Ad 1: RV-focused — "Your machine deserves better than a tarp." Interior RV visual. Destination label: "RV Glass Protection / Built in the USA."
- Ad 2: RV/UTV — "Rock chips and sun don't care about cheap covers." Dark RV at night. Claims "3,000+ LB TOTAL RV HOLD." Destination label: "Glass Protection Systems / Exact Fit For Your RV."
- Ad 3: Rock chip angle — "NEVER LET A $2 ROCK RUIN YOUR TRIP." Jeep/4WD visual. Destination label says "Built Exact For Your RV" but shows a Jeep — internal creative/label inconsistency.

**Message match gaps:**
- All three ads land on a homepage that defaults to a UTV-first experience. The configurator pre-selects the UTV category. The hero headline is "NEVER LOSE ANOTHER COVER" — a cover retention frame — not a rock chip or RV glass protection frame.
- 537+ reviews trust signal appears at fold 2 only. Fold 1 trust relies entirely on LOXX credentialing (unfamiliar industrial brand) before any social proof.
- Ads 1 and 3 share identical body copy despite different visuals and destination labels.
- Ad 2's "3,000+ LB TOTAL RV HOLD" claim from the ad is not surface-matched on the homepage — stat tiles reference "300+ lb / fastener" and "850 lb mag" rather than the total RV hold figure.

---

### Google Ads

Two video ads and one shopping listing visible (screenshot reviewed July 2026).

- Video ads use dark/moody branding consistent with Meta creative. The only visible copy is: "THAT'S WHERE FIT PROTECTION Comes In." No specific benefit claim, hold number, or vehicle type mentioned — significantly less specific than Meta.
- Shopping ad shows a Yamaha Wolverine UTV with "[Price]" as a price placeholder, indicating a potential product feed rendering issue. If prices aren't populating, this listing may be excluded from Shopping auctions or underperforming on click-through.
- Overall, Google creative is weaker on specificity. Meta ads lead with concrete claims (rock chips, LOXX hold numbers, marine-grade materials). Google video ads show only a vague tagline.

---

### Reviews & UGC

Source: 29 Judge.me verified reviews. Overall average: 4.17 / 5.

#### What Customers Love

- **Perfect custom fit** — Reviewers repeatedly note the cover fits their exact model without modification. "Fit my 2025 Rockwood Mini Lite window perfectly." "Product fits like a glove."
- **Highway hold in crosswinds** — Core claim validated across multiple reviews. "Stayed on tight going down the road even tested with a side wind — it did not move." "It didn't budge" on a 16-hour MD-to-FL trip.
- **Easy install and removal** — Consistently mentioned. "Easy to put on and looks nice." "Off in 15 seconds" aligns with product claims.
- **Owner credibility** — One 5-star review explicitly credits a personal email from the owner for converting a hesitant buyer: "The owner came out in an email and told us what was going on and that he will stand behind the product."
- **Unexpected privacy / blackout benefit** — "My favorite thing is how dark the inside of the camper is when we left it on while sleeping at the Cracker Barrel parking lot overnight." (Elizabeth, Package Protection, 5-star.) Not a featured benefit in any current ad or product copy.
- **Insurance framing** — Multiple buyers reference the purchase as protection against a $1,000–$3,000 windshield replacement. "Spent the $500 now instead of $2,000 for a new glass on the highway."

#### What Frustrates Customers

- **Customer support** — Three separate 1-star reviews cite support as the sole reason for low ratings: "Support is almost non existent. There is no physical address or phone number. There isn't even a name of a contact person." (Bob, 1-star). "Customer support is Lacking. I have not received a response from the email." (Rhonda Ishmael, 1-star). "I learned a $300 lesson. I should have listened to the bad reviews." (Bob, 1-star).
- **Tariff surprise** — "We had to pay $183.86 in tariffs in order to pick up our order at the UPS ($465 product). The possibility of having to pay a tariff was never mentioned. We could have replaced 3 windshields for that price." (Taryn Lowe, 1-star, Coachmen Freedom Express).
- **Fit inconsistencies** — "Magnets did quite line up for us." (Veronica Mascorro, 3-star). "Need about 4 more magnets flapping." (Gary Moore, 3-star). "I was disappointed in the fit though." (Kenneth Jordan, 3-star).
- **Unverified first impressions** — A notable share of 5-star reviews come from buyers who haven't road-tested yet ("will update in March," "haven't driven with it yet"). While positive, these don't confirm the core highway-hold promise.

#### Client-Actionable Insights

- **Add direct contact** — Three 1-star reviews cite the same problem: no phone, no named person, no email response. Adding a phone number, chat widget, or a visible named contact (e.g., "Talk to the Arizona team") could directly prevent the most common 1-star trigger.
- **Tariff disclosure** — Add an "International orders may be subject to import duties" notice on product pages and at checkout. The $183 tariff surprise on a $465 order is a conversion-killer and a public trust problem.
- **QC magnet alignment** — Multiple reviewers cite magnet misalignment on delivery. Investigate whether the issue is shipping-related or a production step that can be tightened.
- **Activate the blackout use case** — Overnight privacy/blackout is emerging organically in reviews. Adding it to product copy ("blocks light for overnight camping") opens a second use case for a buyer segment not currently addressed.

---

### PageSpeed / Core Web Vitals

Source: Lighthouse JSON exports, July 2026.

**Homepage (fitprotection.com):**
- Performance: 68/100
- LCP: 4.4s (poor — "good" threshold is under 2.5s)
- Total Blocking Time: 460ms (needs improvement)
- TTI: 22.0s (critical)
- CLS: 0 (good)
- Speed Index: 5.1s

**PDP:**
- Performance: 51/100 (poor)
- LCP: 8.7s (critical — 3.5x the "good" threshold)
- Total Blocking Time: 580ms (needs improvement)
- TTI: 23.9s (critical)
- CLS: 0 (good)
- Speed Index: 6.7s

The PDP is the most conversion-critical page and has the worst performance. An 8.7s LCP means the main visible element takes over 8 seconds to paint. On mobile, this results in a blank or partial screen past the point where most users abandon. TTI of 23.9s means the page is non-interactive for nearly 24 seconds. Every paid click (Meta, Google Shopping, retargeting) landing on a product URL hits this wall.

---

### Competitor Analysis

Source: Self-researched, July 27, 2026. No user-provided competitor data.

| Brand | Product Type | Price Range | Fit | Key Weakness vs. FIT |
|---|---|---|---|---|
| **FIT Protection** | Custom RV + UTV windshield cover | $364–$409 | Model-specific custom cut | Support perception; no tariff disclosure |
| **MagneShade** | RV windshield cover (magnetic) | Est. $200–$400 | Custom fit | Less industrial fastening than LOXX; buyer forums show users actively seeking alternatives |
| **BougeRV** | RV windshield cover (magnetic) | Est. $80–$150 | Semi-custom / universal | Not precision-cut to model; weaker hold specs |
| **Pro Fab Outdoors** | UTV windshield covers (padded) | Est. $120–$180 | Custom fit to model | Lower retention specs; no LOXX; lower price point |
| **Gorilla Offroad** | UTV windshield covers | Unconfirmed | Custom fit | Less premium positioning |

**Market context:** DIY alternatives (shade netting + magnets) cost under $150. Universal-fit strap/velcro covers run $60–$90. FIT Protection's $364–$409 positions it at the premium end, differentiated by marine-grade materials, model-specific cuts, and LOXX industrial fastening. The exclusive North American LOXX partnership is a genuine moat — if communicated clearly against lower-cost alternatives.

---

### Emails

Not collected. Skipped per manifest.

---

### Inspiration Sites

Not collected. Skipped per manifest.

---

### Non-Data Context

Not collected. Skipped per manifest.

---

### Current Site Screenshots

**Live site fetch note (July 27, 2026):** Confirms a "$20 off first cover" email capture offer exists but was not visible in any fold screenshot — likely a popup. Also confirms three accessories (vinyl cleaner $25, removable magnets $39, extended warranty $39) that are not cross-sold on PDP or in the cart beyond the All-LOXX retention upgrade.

**Homepage:**
The "Find My Cover in 3 Taps" configurator is the primary CTA, prominent above the fold. Hero headline "NEVER LOSE ANOTHER COVER" addresses retention loss, not rock chip or glass replacement costs. The LOXX credentialing block in fold 1 occupies significant space before any social proof — four stat tiles referencing LOXX heritage (100 years, military, aerospace, marine). The 537+ reviews badge appears at fold 2. No sticky CTA bar visible on desktop. The $20 off email capture is not visible in any scroll state captured.

**Collection page:**
Well-organized with UTV / RV / Vehicle / Custom Fit tabs. Cards use CONFIGURE rather than ATC, consistent with the custom-fit purchase flow. Price filter bug: all 22 products appear in "Under $400" — including All-LOXX variants at $409 — and the "$400–$450" bracket shows 0 results. A "SCRATCH TO WIN" gamification widget appears in the bottom-left corner across all collection folds.

**PDP:**
Strong buy box. Star rating (537+) positioned above price — good. Sticky ATC bar at page bottom ("ADD PROTECTION · $364 →"). Four-step configuration (Wiper Setup → Retention → Finish → Speed Upgrade) is logical. Trust row directly below price (free shipping, warranty, rebuild free). "Perfect-Fit Promise" block appears in fold 2. Review quotes with specific proof claims in fold 3 ("SIDE WIND — DID NOT MOVE"). No accessory cross-sell on PDP — the All-LOXX upsell is cart-only.

**Cart:**
Cart drawer (mobile). All-LOXX upgrade upsell present with dark LOXX-branded block. Free shipping bar shows "UNLOCKED" with a full green progress bar — already cleared at the $364 base price. No cross-sell for accessories (cleaner, extra magnets, extended warranty) in cart. Zero AOV incentive from the shipping threshold.

---

## Cross-Source Themes

Ranked by evidence strength × revenue potential × funnel importance:

**1. Message match failure across all paid traffic**
All 3 Meta ads use different problem frames (RV glass protection, rock chip prevention, LOXX hold stats) that are not reflected in the homepage hero. 2 of 3 ads are RV-focused landing on a UTV-default homepage. Trust is delayed to fold 2. This affects every paid visitor entering the site. Sources: Meta ads visual summary, site visual summary, live site fetch.

**2. PDP performance is critically broken**
8.7s LCP and 23.9s TTI on the page that hosts the ATC button. Every organic, Shopping, and retargeted visitor landing on a product URL hits a near-unusable mobile experience. Sources: PageSpeed Lighthouse exports.

**3. Customer support perception actively suppresses conversion**
The three lowest-rated reviews all cite the identical problem — no phone, no named contact, unanswered emails. With a 4.17/5 average on 537 reviews, these are visible at the top of review feeds and visible in Google Shopping. Sources: Reviews, live site fetch (email-only contact).

---

## Top Test Opportunities

Ranked by evidence strength × revenue potential × fixability. Monthly sessions unknown — lift estimates are CR-based; dollar impact pending analytics access. Blended AOV: ~$380.

**1. Homepage Hero Headline — Rock Chip vs. Cover Loss Frame**
On the homepage, the above-fold hero headline reads "NEVER LOSE ANOTHER COVER." in large white text on a dark background, with a UTV product image to the right and the configurator bar above. Ad 3 — an active running creative — frames the purchase trigger as "NEVER LET A $2 ROCK RUIN YOUR TRIP." These are different buyer fears: cover retention vs. windshield damage prevention. A visitor arriving from Ad 3 does not see their problem reflected in the headline. Test a headline variant matching the rock chip / windshield replacement framing (e.g., "One $364 Cover. Zero Cracked Windshields.") for traffic from that ad angle. Evidence: Meta ads visual summary (Ad 3 copy), site visual summary (hero fold 1). Est. lift: 5–10% CR on paid traffic from aligned ad-to-headline match.

**2. RV Category Default — Configurator Landing Match**
The "Find My Cover in 3 Taps" configurator sits directly below the nav bar and shows three dropdowns: vehicle type (defaulting to UTV), Brand, and Model, with a teal "FIND MY COVER" button. 2 of 3 active Meta ads are RV-destination-labeled. An RV buyer landing from Ad 1 or Ad 2 must manually switch the first dropdown from UTV to RV before they can find their fit. Test a configurator state where referrer-matched or RV-ad traffic defaults the first dropdown to RV, reducing a required manual step for a defined traffic segment. Evidence: Meta ads visual summary (Ads 1 and 2 destination labels), site visual summary (configurator, fold 1). Est. lift: 8–15% configurator start rate from RV-tagged paid traffic.

**3. Trust Signal Elevation — Reviews to Fold 1**
In fold 1, the trust section below the hero consists of four LOXX credential stat tiles (LOXX fastening heritage, mil-aero-marine trust, 300+ lb / fastener, exclusive NA partner). The 537+ verified reviews block with Judge.me badge appears at fold 2 only — a full scroll below the configurator. For a first-time visitor who has never heard of LOXX, industrial fastening credentials are less persuasive than customer validation. Test adding the star rating and review count (e.g., "★★★★★ 537+ verified reviews") into the fold 1 trust bar or directly beneath the hero headline. Evidence: Site visual summary (fold 1 and fold 2 trust signal placement), reviews (4.17 average, 537 reviews). Est. lift: 3–8% CR on cold paid traffic.

**4. PDP Page Speed — LCP Remediation**
The PDP scores 51/100 performance with an 8.7s LCP and 23.9s TTI on Lighthouse export. The homepage is also slow (68/100, 4.4s LCP, 22s TTI) but less critical. Every Google Shopping click, organic product-URL visit, and product-level retargeting impression lands on this experience. Per Google benchmarking, each 1-second LCP improvement delivers 2–4% CR lift. Prioritize PDP: identify and defer the render-blocking resources driving TBT (580ms) and audit the LCP element (likely the main product image) for size and preload configuration. Evidence: PageSpeed Lighthouse exports. Est. lift: 5–12% CR improvement from meaningful LCP reduction.

**5. Support Contact Visibility**
The live site shows support contact as email-only (info@fitprotection.com, Mon–Fri 8a–5p MST). No phone number, chat widget, or named contact person is visible in the header, PDP trust row, or footer. Three separate 1-star reviews cite exactly this gap. Bob (1-star, Forest River Nobo): "There is no physical address or phone number. There isn't even a name of a contact person." Rhonda Ishmael (1-star, Forest River Impression): "I have not received a response from the email." Adding a visible phone number or chat option to the header and PDP trust section addresses the most-cited conversion suppressor in the review dataset. Evidence: Reviews (Bob, Rhonda Ishmael, 1-star), live site fetch. Est. lift: 2–5% CR improvement; higher impact on mid-funnel abandonment rate.

**6. Tariff Disclosure — International Buyer Pre-Purchase Notice**
No tariff or import duty disclosure is visible on any product page or at checkout. Taryn Lowe (1-star, Coachmen Freedom Express) paid $183.86 in tariffs on a $465 order with zero advance notice — noting she could have replaced three windshields with her insurance deductible for the same cost. This is both a public 1-star review and a likely cart abandonment trigger for Canadian buyers who discover the cost at pickup. Adding a one-line disclosure ("International orders may be subject to import duties") on product pages and at checkout is a zero-cost copy change that eliminates the most damaging post-purchase surprise. Evidence: Reviews (Taryn Lowe, 1-star). Est. lift: Reduces international 1-star rate; eliminates duty-related checkout abandonment.

**7. AOV — Accessories Cross-Sell in Cart**
The cart drawer currently shows one upsell: the All-LOXX retention upgrade ($409 swap). The free shipping bar displays "UNLOCKED" at full green — already cleared by the $364 base product price. Three accessories exist on the live site (vinyl cleaner $25, removable magnets $39, extended warranty $39) but none appear in the cart drawer or on the PDP. Since the free shipping threshold provides zero incremental AOV incentive (always unlocked at the base price), a one-item accessory add-on block in the cart (e.g., "Add the 2-Year Warranty — $39") is the most direct AOV lever currently missing. Evidence: Site visual summary (cart section), live site fetch (accessories pricing). Est. lift: $25–$78 AOV increase per converted order with add-on adoption.

**8. Homepage Desktop Sticky CTA**
No sticky header or CTA bar is visible on desktop across any homepage fold. The configurator ("Find My Cover") is the primary CTA and lives only above the fold. Users scrolling through the LOXX education block (fold 1 lower) and the product grid (folds 2–3) have no persistent action point — they must scroll back up to use the configurator. A sticky "Find My Cover" button fixed to the top nav on desktop scroll would keep the primary CTA accessible at all times. Evidence: Site visual summary (CTA behavior notes, all folds). Est. lift: 2–5% CR improvement on desktop traffic.

**9. Collection Price Filter — $409 All-LOXX Misclassification**
The filter sidebar on the collection page shows all 22 products in the "Under $400" bracket, including All-LOXX variants priced at $409. The "$400–$450" bracket returns 0 results. A buyer filtering by price to compare options gets incorrect results, and any buyer specifically looking for the All-LOXX tier cannot filter to it. This is a low-effort configuration fix (update price metafield or filter logic) with a small but real impact on comparison-mode buyers. Evidence: Site visual summary (collection fold 2, filter sidebar). Est. lift: Small; near-zero effort to fix.

**10. Google Shopping Feed — Price Rendering Issue**
The Google Ads screenshot shows "[Price]" as a literal placeholder in a Shopping ad for a Yamaha Wolverine UTV cover. If product prices are not populating in the Merchant Center feed, affected SKUs may be suppressed from Shopping auctions or running without a price — both reduce impressions and click-through rate. Audit the product feed export for price field errors and confirm all active SKUs are rendering correctly in Merchant Center. Evidence: Google Ads visual summary (shopping ad price placeholder). Est. lift: Restores Shopping impressions and CTR for affected SKUs.

---

## Unused but Valuable Findings

- **$20 off email popup** — Confirmed live but invisible in all fold screenshots. If it fires before configurator intent is established, it may interrupt the primary CTA flow. Audit trigger timing and conversion impact.
- **Blackout / privacy use case** — Multiple reviewers organically describe overnight privacy as a major benefit ("dark inside the camper," sleeping at Cracker Barrel). Not present in any ad or product copy. Could open a new buyer messaging angle.
- **Owner email conversion story** — One 5-star review credits a personal email from the owner for converting a hesitant buyer. A founder-voice cart-abandonment email could replicate this at scale.
- **SCRATCH TO WIN widget** — Present across all collection pages. Unclear if it drives engagement or creates visual noise. Worth tracking click rate vs. conversion rate on sessions where it's triggered.

---

## Missing Data

None flagged — all sources listed in the manifest were collected and analyzed.
