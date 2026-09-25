# Baked Bags CRO Research Audit

## Data Sources Used

- Meta Ads & Landing Pages (user-provided screenshots + live WebFetch of bakedbags.life/packs/ and /conepack/)
- Google Ads Transparency Center (user-provided screenshot)
- PageSpeed / Core Web Vitals (Lighthouse JSON, fetched 2026-08-21)
- Current Site Screenshots — homepage, collection, PDP, cart (user-provided + live WebFetch of bakedbags.com)
- Reviews & UGC (20 verified customer reviews, CONED product line)
- Competitor Analysis (self-researched via WebSearch, 2026-08-21)

## Source Findings

### Meta Ads & Landing Pages

Three active Meta ads run to two landing pages on a separate domain (bakedbags.life), not the main store (bakedbags.com).

- **Ad 1** (running since Jul 19, 2026) and **Ad 2** (since Jul 22, 2026) both send traffic to bakedbags.life/packs/. Ad 1's entire copy is built around a subscription/rewards program: "Subscribe and unlock 10+ tiers of free gifts, surprise rewards and exclusive perks." The landing page it sends traffic to has no subscription or rewards mention anywhere in the three folds collected — the hero leads with "VARIETY PACKS UP TO 50% OFF" pricing instead. This is a full message-match failure: the exact hook that got the click disappears on landing.
- **Ad 3** (since Aug 1, 2026) sends traffic to bakedbags.life/conepack/. Ad copy — "Save 33% on Cones Variety Packs. 4 flavors for $39.99" — matches the landing page hero almost word for word ("SAVE 33% ON THE CONES STARTER PACK," "$60 → $39.99"). This is the strongest message match of the three ads.
- Both landing pages share the same template, press bar (Forbes, LA Weekly, LA Wire, New York Weekly, No Jumper), and customer quote block. Neither landing page has a sticky CTA bar in the folds captured.

### Google Ads

Three Google Search ads reviewed via Google Ads Transparency Center. All three use generic "shop now" framing with no pricing or discount callout — a direct gap against the Meta ads, which lead with specific numbers ($39.99, 33% off, 50% off). Separately, the Transparency Center screenshot shows three different "verified advertiser" names on the ad cards ("Asaduk haswe," "HANH PHUC COMMUNICATI...," "RICHFIELD ELECTRONICS LIMITED") — none matching Baked Bags. This is a paid-media trust/compliance flag worth raising with the client's ad account team, separate from on-site CRO.

### Reviews & UGC

20 verified reviews, all for the CONED product line.

#### What Customers Love

- Potency is the dominant theme: "put it in my ice cream and it hit like no other" (Dae S.), "I was zonked for the rest of the day" (Robert Y.), "off my ass... went to another planet" (Ariana R.).
- Variety pack format is repeatedly called out as a purchase driver: "I like the idea of having a variety and not getting bored" (Loveyy S.), "Love the option of a variety pack too" (Taylor H.).
- Multiple customers independently pair the cones with real ice cream — an unprompted, organic usage pattern across at least three reviews (Dae S., Azaera T., Robert Y.).
- Effects described as long-lasting and effective for pain relief in at least one case (Kiara M., fibromyalgia).

#### What Frustrates Customers

- Dosing confusion: "The serving size said 1, so I ate an entire cone and was zonked for the rest of the day" (Robert Y.) — this reads as a labeling clarity issue, not a satisfaction issue, but it's a real consumption-safety signal.
- Minor value complaint on portion size relative to price: "I feel like it should be a little more than just 50g" (Tiffany B.).
- One mention of "weird aftertaste like most eddies" (Finely W.), framed as a minor caveat rather than a dealbreaker.

#### Client-Actionable Insights

- Serving-size labeling is a candidate for a packaging/description fix, not just an on-site test — at least one customer over-consumed because a "1 serving" cue wasn't clear enough.
- The organic ice-cream-pairing behavior is a free, evidence-backed content and merchandising angle (recipe content, PDP imagery, ad creative) that isn't currently used anywhere in the collected ad or site assets.

### PageSpeed / Core Web Vitals

Collected 2026-08-21, mobile Lighthouse reports.

**Homepage** (bakedbags.com/?state=AZ&age_verified=true): Performance score 0.34. LCP 8.1s, CLS 0.153, TBT 790ms, FCP 4.5s, Time to Interactive 49.2s.

**PDP** (extra-strength-variety-pack-edibles-800mg): Performance score 0.39. LCP 18.5s, CLS 0.002, TBT 690ms, FCP 5.2s, Time to Interactive 53.3s.

Both pages fail Core Web Vitals thresholds badly — Google's "good" LCP threshold is 2.5s; the PDP is at roughly 7x that. A Time to Interactive near 50 seconds means a meaningful share of mobile visitors will act on a page that isn't yet responsive to taps. This is the single largest evidence-backed problem in the dataset and touches every other funnel stage.

### Competitor Analysis

Self-researched, 2026-08-21. No competitor data was provided by the client.

| Brand | Format | Subscription | Notable |
|---|---|---|---|
| Delta Munchies | Hemp-derived THC gummies/edibles, DTC | Subscribe & Save: 15% off every order, free shipping, pause/edit anytime | Direct DTC competitor with a live, visible subscription mechanic |
| Kanha | THC gummies | No DTC subscription found — primarily dispensary/delivery distribution | Not a direct DTC comp on subscription |
| Diamond CBD | Hemp-derived edibles, DTC | Subscription available across product lines; free shipping over $99 | Broader hemp catalog, subscription-first merchandising |

Baked Bags advertises a 10+ tier subscription/rewards program in Meta Ad 1 and Ad 2, but neither the landing pages nor the PDP show any subscription purchase option anywhere in the screenshots collected. Delta Munchies, a direct competitor, has a working subscribe-and-save flow live on its site. This gap is discussed further under Top Test Opportunities.

### Emails

Not collected — skipped by user during data collection (see manifest).

### Inspiration Sites

Not collected — skipped by user during data collection (see manifest).

### Non-Data Context

Not collected — skipped by user during data collection (see manifest).

### Current Site Screenshots

**Homepage:** Hero headline "THE LEADING CAUSE OF RED EYES" sits directly below a federal-ban countdown banner ("Starting December 11th '26, the US Federal government has banned all intoxicating hemp... stock up now") with a live running timer. The countdown competes with the primary offer message for the first thing a visitor sees. Below the CTA: a 4.8-star / 250,000+ customer line and two compliance checkmarks, followed by a press-logo row. No sticky CTA bar across any fold. Trust/compliance messaging repeats in two different visual formats (checkmark row in fold 1, a five-icon strip in fold 2).

**Collection page:** Category tab bar persists across all product grid folds. Multi-flavor pack cards use strikethrough pricing with a red "% Savings" badge; single-flavor cards show flat pricing with no savings badge, creating an inconsistent pricing-presentation pattern between the two card types on the same grid.

**PDP:** Buy box opens with a star-rating/customer-count line, then price ($60.00 struck through to $39.99), then three benefit bullets, then a flavor selector defaulted to "Variety Pack" (marked with a distinct SALE tag other flavors don't carry). Bundle & Save is quantity-based (1x/2x/3x of the same product) — not a mix-and-match bundle. No subscription option is visible anywhere in the buy box despite this being the exact product line (CONED) that Meta Ad 1 and Ad 2 advertise a subscription/rewards program for. Add to Cart is not sticky; the button sits inline in fold 2, meaning a visitor who has scrolled past it must scroll back up to purchase. The same trust-icon strip (Made in USA, Fast Shipping, Quality Ingredients, Lab Tested, Hemp Derived) appears three separate times across the PDP folds captured.

**Cart (drawer):** Strong AOV mechanics already in place: a free-shipping progress bar ("$45.01 away from free standard shipping"), an inline "Buy 2 save $5.00" prompt on the existing line item, a three-product "You may also like" cross-sell module, a toggleable Rush Order add-on, and a Sezzle 4-installment option shown above Checkout. This is the most conversion-mature section of the funnel observed.

## Cross-Source Themes

1. **Site speed is the highest-leverage, best-evidenced problem.** PDP LCP of 18.5s and Time to Interactive near 50-53 seconds on both homepage and PDP (Lighthouse data) sit under every other funnel stage — ad traffic paying for clicks that land on pages a meaningful share of mobile visitors can't yet interact with.
2. **Subscription/rewards messaging breaks between ad and site.** Meta Ad 1 and Ad 2's core hook — a 10+ tier subscription program — has no corresponding purchase mechanism anywhere in the landing page or PDP screenshots collected, while a direct competitor (Delta Munchies) has a live, visible subscribe-and-save flow. Confirmed by two independent sources: Meta ad/LP comparison and competitor research.
3. **Reviews surface a real dosing-clarity gap with safety implications**, distinct from a pure conversion issue: at least one verified customer over-consumed because serving-size labeling wasn't clear, which is both a support/liability concern and an on-site copy opportunity.

## Top Test Opportunities

**PDP Core Web Vitals Emergency Fix** — The Coned Variety Pack PDP loads with an 18.5s LCP and ~53s Time to Interactive on mobile (Lighthouse, 2026-08-21); a visitor arriving from a paid ad can tap "Add to Cart" and get no response for the better part of a minute. Evidence: PageSpeed. CR lift: not calculable without session/AOV data — treat as highest-priority fix given severity.

**Homepage Core Web Vitals Fix** — Homepage LCP is 8.1s with a 49.2s Time to Interactive (Lighthouse, 2026-08-21), roughly 3x Google's "good" LCP threshold. Evidence: PageSpeed. CR lift: not calculable without session/AOV data.

**Close the Subscription Message-Match Gap (Ad 1 & 2 → LP → PDP)** — Meta Ad 1 ("Subscribe and unlock 10+ tiers of free gifts") and Ad 2 both drive to bakedbags.life/packs/, which never mentions subscription anywhere in the three folds captured; the PDP buy box for the same CONED product line also shows no subscription option, only one-time purchase and quantity-based Bundle & Save. Competitor Delta Munchies has a live subscribe-and-save flow with 15% off and free shipping. Evidence: Meta ads visual summary, live LP WebFetch, PDP screenshots, competitor research. Est. lift: not calculable without session/AOV data.

**Serving-Size / Dosing Clarity in Buy Box** — PDP fold 1 shows three benefit bullets ("Two 25MG THC Cones Per Bag," "4 Different Flavors," "200 MG THC Total") but no explicit "1 cone = 1 serving" guidance at the point of purchase. A verified reviewer reported eating an entire cone believing it was one serving and being "zonked for the rest of the day." Evidence: reviews.md (Robert Y.), PDP screenshots. Est. lift: not calculable without session/AOV data; primary value is reduced support burden and overconsumption risk, secondary value is trust-building copy.

**Reposition the Federal-Ban Countdown Timer** — On the homepage, a running countdown banner ("US Federal government has banned all intoxicating hemp... stock up now") sits directly above the hero headline "THE LEADING CAUSE OF RED EYES," competing for first-view attention with the primary value proposition before a visitor has seen any product framing. Evidence: site-visual-summary.md, live homepage WebFetch. Est. lift: not calculable without session/AOV data.

**Add a Sticky Add-to-Cart Bar on PDP** — The primary "ADD TO CART" button sits inline in PDP fold 2, below the flavor selector and price; no sticky/persistent CTA was observed in any of the three PDP folds captured. Combined with the page's severe load-time issues, a visitor who scrolls past the buy box has no fast path back to purchase. Evidence: site-visual-summary.md (PDP fold notes, "CTA behavior"). Est. lift: not calculable without session/AOV data.

**Test the Ice-Cream-Pairing Angle in PDP/Ad Content** — At least three of 20 collected reviews independently describe pairing CONED products with real ice cream as an unprompted usage pattern ("put it in my ice cream and it hit like no other" — Dae S.; "put real ice cream on it" — Azaera T.). This pairing does not appear in any Meta ad, landing page, or PDP copy/imagery collected. Evidence: reviews.md. Est. lift: not calculable without session/AOV data; low-cost content test using existing customer language.

**Align Google Ads Copy with Meta's Pricing Specificity** — All three Google Search ads reviewed use generic "shop now" language with no discount or price shown, while Meta ads lead with specific numbers ($39.99, 33% off, 50% off) that reviews and landing page data show customers respond to. Evidence: google-ads-visual-summary.md vs. meta-ads-visual-summary.md. Est. lift: not calculable without session/AOV data; this is a paid-media copy test, not an on-site test.

**Consolidate Redundant Trust-Badge Repetition on PDP** — The same five-icon trust strip (Made in USA, Fast Shipping, Quality Ingredients, Lab Tested, Hemp Derived) appears three separate times across the three PDP folds captured, diluting its impact versus a single well-placed instance near the buy box. Evidence: site-visual-summary.md (PDP trust signals notes). Est. lift: not calculable without session/AOV data.

**Fix Google Ads Verified-Advertiser Mismatch** — The Google Ads Transparency Center screenshot shows three different verified advertiser names on Baked Bags' own ad cards ("Asaduk haswe," "HANH PHUC COMMUNICATI...," "RICHFIELD ELECTRONICS LIMITED"), none matching the brand. This is a paid-media account/compliance issue to flag to the client's Google Ads team — it can affect ad trust and eligibility, though it isn't a conversion-rate test in the traditional sense. Evidence: google-ads-visual-summary.md. Est. lift: not applicable — this is a compliance flag, not a CRO test.

**Standardize Collection Page Pricing Presentation** — On the collection grid, multi-flavor pack cards show strikethrough pricing with a red "% Savings" badge while single-flavor cards show flat pricing with no badge, creating an inconsistent value signal within the same grid. Evidence: site-visual-summary.md (Collection page, "Price display" notes). Est. lift: not calculable without session/AOV data.

## Unused but Valuable Findings

- Bundle & Save on the PDP is quantity-based only (1x/2x/3x of the same flavor selection) — no mix-and-match bundle option exists, which could be a future test given the review-confirmed customer preference for variety.
- The cart drawer's AOV mechanics (free-shipping bar, inline upsell prompt, cross-sell module, Rush Order toggle, Sezzle installments) are already strong and don't need a test — worth noting as a funnel stage that's ahead of the rest of the site.

## Missing Data

- No competitor data was provided by the client; the Competitor Analysis section above is entirely self-researched (WebSearch, 2026-08-21) and should be validated with the client before being used to justify test priority.
- Email campaigns, inspiration sites, and non-data context (call notes, strategic priorities) were not collected — those sections are omitted rather than guessed at.
- No traffic (sessions/mo) or AOV figures were provided or observed in any source, so every Est. lift line above states a CR-lift direction without a dollar figure. Revenue sizing requires the client to supply Shopify analytics.
