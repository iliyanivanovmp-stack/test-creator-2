# FIT Protection Roadmap Seed

**Store:** fitprotection.com
**AOV:** ~$380 blended (Mag $364 / All-LOXX $409)
**Monthly sessions:** Unknown — analytics access needed
**Data sources:** Meta ads visual summary, Google ads visual summary, PageSpeed Lighthouse exports, Judge.me reviews (29 verified), site visual summary (homepage + collection + PDP + cart), live site fetch

---

## Key Insights

All three active Meta ads route to the same homepage, but the homepage does not match any of the three ad frames. Ad 1 and Ad 2 are RV-destination-labeled ("RV Glass Protection," "Exact Fit For Your RV"). Ad 3 leads with "NEVER LET A $2 ROCK RUIN YOUR TRIP" and shows a Jeep. The homepage hero leads with "NEVER LOSE ANOTHER COVER" — a cover retention frame — with a UTV product image and a configurator that defaults to the UTV category. An RV buyer must manually switch the first dropdown to find their fit. The 537+ verified reviews trust signal (Judge.me, 4.17/5 average) does not appear until fold 2; fold 1 trust relies entirely on LOXX industrial credentials, an unfamiliar B2B brand to most consumers. Every paid visitor is exposed to this mismatch.

PDP performance is critically broken. Lighthouse exports show 51/100 performance with an 8.7s LCP and 23.9s TTI on the product page — the page that hosts the ATC button. The homepage is also slow (68/100, 4.4s LCP, 22s TTI), but the PDP is worse by every metric. Google Shopping clicks, organic product URL traffic, and retargeting impressions all land on this experience. At 8.7s LCP, most mobile users abandon before the page is usable. Per Google data, each 1-second LCP improvement yields 2–4% CR lift.

Customer support perception is suppressing conversion and pulling down the public review average. Three separate 1-star reviews — each written exclusively about support — describe the same situation: no phone number, no named contact, emails going unanswered. Bob (Forest River Nobo, 1-star): "There is no physical address or phone number. There isn't even a name of a contact person." Rhonda Ishmael (Forest River Impression, 1-star): "I have not received a response from the email." The live site shows only info@fitprotection.com with Mon–Fri 8a–5p MST hours. With 537 public reviews and a 4.17 average, these 1-star reviews are visible at scale in Google Shopping and review feeds.

---

## Top Test Opportunities

### 1. Homepage Hero Headline — Rock Chip vs. Cover Loss Frame
**What's broken:** The homepage hero headline reads "NEVER LOSE ANOTHER COVER." in large white text on a dark background, left-aligned with a UTV product image to the right. The subtext reads "Exact Fit To Your Glass. No Drilling, No Straps. Off in 15 seconds." This frame addresses cover retention loss. Ad 3 — an active running creative — leads with "NEVER LET A $2 ROCK RUIN YOUR TRIP" and a Jeep visual. A visitor from that ad lands on a headline that addresses a different problem than the one they just responded to.
**Evidence:** Meta ads visual summary (Ad 3 copy and visual), site visual summary (hero fold 1)
**Key data:** Ad 3 is active across Facebook, Instagram, Messenger, WhatsApp, Threads from July 24, 2026. Homepage hero is the first element below the configurator bar on all three Meta ad landings.
**Est. lift:** 5–10% CR on paid traffic from headline-to-ad alignment

### 2. RV Category Default — Configurator Match for RV Ad Traffic
**What's broken:** The "Find My Cover in 3 Taps" configurator bar sits immediately below the nav and shows three dropdowns: vehicle type (defaulting to "UTV"), Brand, and Model, followed by a teal "FIND MY COVER" CTA button. An RV buyer arriving from Ads 1 or 2 (both RV-destination-labeled) sees UTV pre-selected in the first field and must manually switch to RV before they can begin their fitment search. This is a required extra step that increases friction for a defined paid traffic segment.
**Evidence:** Meta ads visual summary (Ads 1 and 2 destination labels), site visual summary (configurator, fold 1)
**Key data:** 2 of 3 active Meta ads carry RV destination labels. The configurator is the primary above-fold conversion mechanism on the homepage.
**Est. lift:** 8–15% configurator start rate from RV-tagged paid traffic

### 3. Trust Signal Elevation — Move Reviews to Fold 1
**What's broken:** Fold 1 of the homepage contains four stat tiles: "~100yr LOXX fastening heritage," "Mil-Aero-Marine trust," "300+ lb hold per LOXX fastener," and "Exclusive NA partner for glass covers." These tiles appear in the lower section of fold 1, directly beneath the hero. The 537+ verified reviews block with Judge.me badge appears at fold 2 — a full scroll below the primary conversion area. For a first-time visitor who does not recognize LOXX, industrial heritage credentials are less persuasive than customer validation.
**Evidence:** Site visual summary (fold 1 trust tiles, fold 2 review block), reviews (537 reviews, 4.17 / 5 average)
**Key data:** 537 verified Judge.me reviews. Review badge not visible until fold 2 on both desktop and mobile captures.
**Est. lift:** 3–8% CR on cold paid traffic

### 4. PDP Page Speed — LCP Remediation
**What's broken:** The PDP product page (e.g., Can-Am Defender listing) loads with an 8.7s Largest Contentful Paint and 23.9s Time to Interactive per Lighthouse export. Performance score: 51/100. Total Blocking Time is 580ms. The buy box — including the sticky "ADD PROTECTION · $364 →" ATC bar and the four-step configuration flow — is fully non-interactive for nearly 24 seconds after navigation. Every Google Shopping click, organic product URL visit, and product-level Meta retargeting impression lands on this experience.
**Evidence:** PageSpeed Lighthouse exports (PDP metrics, July 2026)
**Key data:** PDP LCP 8.7s (threshold for "good": 2.5s). Homepage LCP 4.4s. Both critical; PDP is 3.5x worse than "good" threshold.
**Est. lift:** 5–12% CR improvement from meaningful LCP reduction

### 5. Support Contact Visibility — Phone or Chat in Header and PDP
**What's broken:** The live site shows support contact limited to info@fitprotection.com with Mon–Fri 8a–5p MST hours. The PDP trust row reads "Free ship - lower 48 | 1-Year warranty | Rebuild free if it fails" — no contact reference. No phone number, named contact, or chat widget is visible in the header, nav, or PDP buy box. Multiple 1-star reviews cite this exact gap as their only reason for leaving a negative review.
**Evidence:** Reviews (Bob 1-star, Rhonda Ishmael 1-star), live site fetch (contact info)
**Key data:** 3 of the lowest-rated reviews in the dataset are exclusively about support accessibility. Overall review average: 4.17/5 across 537 reviews.
**Est. lift:** 2–5% CR improvement; higher impact on mid-funnel abandonment

### 6. Tariff Disclosure — Pre-Purchase Notice for International Buyers
**What's broken:** No tariff or import duty disclosure is visible on any product page, cart, or checkout flow. Taryn Lowe (1-star, Coachmen Freedom Express) paid $183.86 in import tariffs to collect a $465 order at UPS pickup — noting she could have replaced three windshields with her insurance deductible for the same price. The disclosure gap creates post-purchase shock and a public 1-star review.
**Evidence:** Reviews (Taryn Lowe, 1-star, with photo)
**Key data:** $183.86 tariff on $465 product (40% effective tariff rate). No disclosure text found on product page or checkout in live site fetch.
**Est. lift:** Eliminates duty-related checkout abandonment; reduces international 1-star review rate

### 7. AOV — Accessories Cross-Sell in Cart Drawer
**What's broken:** The cart drawer shows one upsell: the All-LOXX retention upgrade (switch from $364 Mag to $409 All-LOXX). The free shipping progress bar appears as fully green with "FREE SHIPPING TO THE LOWER 48 — UNLOCKED" at the $364 base price — always unlocked from the first item. Three accessories confirmed live on site: vinyl cleaner ($25), removable magnets ($39), extended warranty ($39). None appear in the cart drawer or on the PDP. No cross-sell mechanism exists below the All-LOXX upsell.
**Evidence:** Site visual summary (cart section), live site fetch (accessories and pricing)
**Key data:** Free shipping threshold pre-unlocked at $364. Accessories exist at $25–$39. All-LOXX upsell already in cart.
**Est. lift:** $25–$78 AOV increase per converted order with add-on adoption

### 8. Homepage Desktop Sticky CTA — Persistent Find My Cover
**What's broken:** The "Find My Cover" configurator sits between the nav and the hero on the homepage — visible only above the fold. As users scroll through the LOXX education section (fold 1 lower), the product grid (folds 2–3), and the feature explainer, no persistent CTA is available. The nav is static; no floating button or sticky bar appears. Users who want to start the configurator after reading through the page must scroll back to the top.
**Evidence:** Site visual summary (CTA behavior notes across all three homepage folds)
**Key data:** Desktop screenshots confirm no sticky element across full homepage scroll. Configurator is the only primary CTA mechanism on the homepage.
**Est. lift:** 2–5% CR improvement on desktop traffic

---

## Unused Findings

- **$20 off email popup** — Confirmed live but not visible in any fold screenshot. If it fires before configurator intent is established, it may interrupt the primary CTA flow. Audit trigger timing and the impact on configurator start rate.
- **Blackout / overnight privacy use case** — Multiple reviewers describe using the cover for overnight vehicle privacy ("dark inside the camper," sleeping at Cracker Barrel parking lots). Not present in any current ad or product copy. Potential messaging angle for a segment not currently addressed.
- **Owner email credibility moment** — One 5-star buyer credits a personal owner email for converting them from hesitant to purchased. A founder-voice cart-abandonment sequence could replicate this conversion mechanism at scale.
- **SCRATCH TO WIN widget** — Present across all collection folds in bottom-left corner. Not mentioned elsewhere in data. Worth monitoring click rate vs. conversion rate on engaged sessions.
