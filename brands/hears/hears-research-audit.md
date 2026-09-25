# Hears CRO Research Audit

## Data Sources Used

- Google Ads Transparency (screenshots + visual summary)
- PageSpeed / Core Web Vitals (Lighthouse JSON, homepage + PDP)
- Current Site Screenshots (homepage, collection, PDP, cart) + live WebFetch verification (2026-09-13)
- Social & Community Research (last30days-ecom: Trustpilot, Amazon, TikTok, Pinterest, Web, YouTube)
- Reviews & UGC (on-site Judge.me/Loox-style reviews, collected verbatim)
- Competitor research (self-researched via WebSearch, 2026-09-13)
- Meta Ads: not applicable — brand does not run Meta ads

## Source Findings

### Meta Ads & Landing Pages

Not applicable. Hears does not run Meta ads; no landing page or creative data exists for this channel.

### Google Ads

Ad copy segments hard by use case — sleep, motorbike/moto rides, festivals, concerts, music — with headlines like "Earplugs for Sleep - Blocks snoring," "Best Earplugs for Festivals," and "Awarded Winning Earplugs 2026." Body copy repeats near-verbatim across ads: "Protect Your Ears With Hears' 20dB Earplugs... Patented High-Fidelity Filters for Clear Sound and Comfort." The live-verified homepage headline ("The most iconic earplug is back for the 2026 season") and hero CTA ("SHOP PACHA EDITION") do not reference any specific use case from the ad headlines — a user clicking a "Best Earplugs for Sleep" ad lands on a Pacha festival-edition hero, not a sleep-specific message. No Meta channel exists to cross-check, so this is a single-channel message-match gap between ad intent and homepage landing state.

A second finding: three third-party resellers ("On Web Consulting Ltd," "ShopForward B.V.," "Now-Sale.co...") appear in Google Shopping listings alongside Hears' own verified account, showing Hears product images and listings under their own advertiser names. This is a brand-control/channel-conflict issue worth flagging to the client, not a CRO test.

Offers shown in ads ("Festival Season - 45% Off," "Buy 2 & Get 10% Off") differ from the live sitewide offer ("BUY 2, GET 1 FREE"), a discount-framing mismatch between ad promise and site delivery.

### Reviews & UGC

#### What Customers Love

- Comfort for side/stomach sleepers, repeated across many reviews ("Perfect for Side Sleepers," "Great for sidesleepers," multiple mentions of sleeping without ear ache)
- Effectiveness against snoring specifically — a recurring, specific use case ("Sleeping with a snoring wife," "Finally a snoring block-out device," "Blocks out snoring but lets me hear the alarm")
- Concert use without post-event ear ringing/tinnitus relief, with repeated BTS concert mentions ("Hears at BTS," "Tame the concert")
- Multiple tip sizes (XS/S/M) called out as fitting small or unusual ear canals
- Cleaning kit and carry pouch called out positively as accessory add-ons

#### What Frustrates Customers

- The collected on-site review set is overwhelmingly 5-star (two reviews are 4-star; none are 3-star or below), which is a data-representativeness gap: this looks like a curated storefront review widget, not the full distribution. First-party reviews alone cannot describe real frustration themes.
- No negative or mixed on-site reviews were present in the collected file to draw friction points from — this section is intentionally left thin rather than invented. See Social & Community Research below for the corroborating trust-score gap that points to unresolved complaints existing off-site.

#### Client-Actionable Insights

- Several reviewers request higher attenuation options mid-review ("Thinking my next set of buds could be even slightly more sound reducing... assuming I have 20dB now") — signal for cross-sell/upsell messaging toward the 25dB SNR option post-purchase, not a site test.
- Repeated unprompted praise for the cleaning kit as a "free gift" — suggests the accessory has strong perceived value that isn't yet leveraged as a stated PDP or cart incentive line (product/ops note, not a test idea).

### PageSpeed / Core Web Vitals

Collected 2026-09-13. Both tested URLs carried a `?variant=...&_pos=5&_psq=pacha&_ss=e&_v=1.0` query string (a search-result click-through), not a clean direct URL — flagged in the manifest for verification. Live WebFetch of the clean homepage and PDP URLs during this audit confirmed the same page structure and content, so the scores below are treated as representative of the live site rather than an anomalous capture.

**Homepage** — Performance 0.59, Accessibility 0.70, Best Practices 1.00, SEO 0.85. LCP 1.7s (good), CLS 0.001 (good), **TBT 8,590 ms** (very poor — threshold for "poor" is >600ms), Speed Index 36.4s, **Time to Interactive 65.6s**, Max Potential FID 670ms.

**PDP** — Performance 0.55, Accessibility 0.78, Best Practices 0.77, SEO 0.92. LCP 2.4s (needs improvement), CLS 0.001 (good), **TBT 17,600 ms** (very poor), Speed Index 25.0s, **Time to Interactive 85.9s**, Max Potential FID 1,320ms.

Both pages paint fast (good LCP/CLS) but become interactive extremely slowly — total blocking time in the 8.5–17.6 second range means the page looks ready long before a user can actually tap a button, scroll a carousel, or open the color swatch selector without input lag. This pattern (fast paint, catastrophic interactivity) usually traces to heavy third-party/JS widgets — the floating AI "Ask a question" chat widget, UGC video carousels, and app-embedded review widgets seen across the homepage, PDP, and collection screenshots are the likely contributors, though the JSON does not name specific scripts.

### Competitor Analysis

Self-researched via WebSearch, 2026-09-13 (no user-provided competitor file exists for this brand).

| Brand | Positioning | Price (approx.) | Notable strength | Notable weakness |
|---|---|---|---|---|
| Loop (Quiet 2 / Experience 2) | Design-forward, reusable, sleep + concert lines | ~$25 (sleep), higher for Experience line | Strong design/style reputation, washable/reusable | Less flat-response/high-fidelity claim than Eargasm |
| Eargasm High Fidelity | Concert/musician-focused, flat-response filter | ~$44 | Strong sound-clarity reputation among musicians | Narrower use-case focus (concerts), runs large per fit feedback |
| Mack's (Snore Blockers / Ultra Soft Foam / Pillow Soft) | Budget, maximum noise blocking, sleep-first | ~$18 | Highest NRR (33dB) at lowest price | Foam/disposable format, not reusable or high-fidelity |

Hears' own reviews explicitly mention shoppers comparing against Flares, Zound, and Alpine before choosing Hears — a data point not surfaced in this WebSearch pass but corroborated first-party. Hears' price point (~$43–46 per set) sits above Loop's sleep line and Mack's, and near Eargasm, while claiming both sleep and concert/high-fidelity use cases in one SKU — a broader use-case claim than any single competitor above makes.

### Emails

Not collected — no `raw/emails.md` file exists and no screenshots were provided for this source. Not flagged as a gap since it was not selected during collection.

### Inspiration Sites

Not collected — not selected during collection.

### Non-Data Context

Not collected — no `raw/context.md` file exists and none was selected during collection.

### Social & Community Research

Collected via last30days-ecom, 2026-09-13 (range 2026-08-14 to 2026-09-13). Directional findings, third-party sourced.

- **Trust-score gap (corroborated across two independent platforms):** Trustpilot shows a 3.5 TrustScore on 1,284 reviews ("somewhat happy" as the dominant recent sentiment), and Amazon shows 3.8/5 on 232 ratings for the "Hears One Ear Plugs" listing. Both sit well below the 4.9/5 "Rated by 200,000+ customers" claim shown live on the Hears homepage and PDP. This is corroborated by two independent third-party sources and stands in direct tension with first-party site messaging — strong enough evidence to treat as more than directional.
- **Fashion/luxury crossover (corroborated across Pinterest and independent web editorial):** A Saint Laurent x Hears collaboration ("Sound Check, Fashion Check: Saint Laurent x Hears Earplugs Drop," fuckingyoung.es) positions Hears in a fashion-adjacent lane distinct from purely functional competitors (Loop, Eargasm, Mack's). This narrative was not observed anywhere in the collected site screenshots or homepage — it is not currently part of the on-site positioning captured in this audit's evidence.
- **TikTok:** Active brand presence (@hears.com, 26.8K likes/889 followers) plus organic creator content. One creator video frames first-time earplug purchase around hearing-loss anxiety — an angle not directly reflected in the ad headline set (which is festival/concert/sleep-led, not anxiety/prevention-led).
- **Amazon competitive crowding:** Hears does not dominate its Amazon category; competitors (Yawsoy, Mack's, DEWALT, Eargasm, HEAROS, EarPeace) appear in the same search results, several with higher review counts than Hears' own listing.
- Directional only, uncorroborated by first-party evidence: the YouTube branded review video ("My Tinnitus Changed How I Protect My Hearing") and the TikTok hearing-loss-anxiety angle are single-source signals not otherwise confirmed elsewhere in this audit.

### Current Site Screenshots

Live-verified against hears.com and the PDP URL on 2026-09-13 via WebFetch, in addition to the collected screenshots. Capture date for the original screenshots was not provided.

**Homepage:** Announcement bar reads "LIMITED TIME OFFER: BUY 2, GET 1 FREE" — confirmed live. Hero is a full-bleed lifestyle photo with "HEARS × PACHA" co-branded overlay, headline "The most iconic earplug is back for the 2026 season," CTA "SHOP PACHA EDITION" — confirmed live and unchanged. "Rated 4.9/5 by 200,000+ customers" appears in the hero, repeated multiple times down the page — confirmed live. A collapsed vertical tab on the left edge reads "GET A FREE SET OF HEARS," and a floating "Ask a question" AI-chat pill sits near the bottom of the hero — both present in every screenshot fold and likely contributors to the page's heavy TBT (see PageSpeed above). The entire homepage hero and bestseller section is built around one limited-edition seasonal drop (Pacha), with no visible path back to core "Sleep" or "Motosports" framing until Fold 2/3 — a mismatch for any visitor arriving from a sleep- or moto-themed Google ad.

**Collection page:** Filter pills (Hears, Hears Sleep, Music & events, Focus, Moto) sit above a 4-column grid with "BESTSELLER," "LIMITED EDITION," and multiple "SOLD OUT" sub-variant badges. Several product images in Folds 2–3 (Hears Sleep grid, Accessories, Merch) render as unloaded gray placeholder blocks in the captured screenshots — this could be lazy-load timing at capture time rather than a persistent bug; not confirmed live in this pass since WebFetch only returns text, not rendered images. Bundle cards show percentage-off badges (18%, 19%, 21%, 30%) with no visible original strikethrough price alongside them in the captured fold.

**PDP:** Live WebFetch of the clean `/products/hears-earplugs` URL shows "Brass Blue" as the default featured variant. This directly answers the manifest's open question: the "Pacha Edition 2.0" colorway shown in the original screenshot captures was a search-result click-through state (carrying `?variant=...&_psq=pacha...` in the URL), **not** the page's actual default. The captured PDP screenshots should be read as "a user arriving via Pacha-related search," not as the default first-time landing state. Separately, the screenshots show one swatch in the "Color: Pacha Edition 2.0" row with a diagonal strike-through (unavailable) sitting directly beside a green-dot "In stock ready to ship" status — a partial-variant-OOS state, not a fully-sold-out product. The buy box structure (single "$46/set" vs. highlighted "MOST POPULAR" Buy 2 Get 1 Free at "$31 Per set," 33% off) is consistent with the homepage's sitewide bundle promo. A sticky mini-cart bar appears on scroll in the desktop capture; mobile stickiness was not captured.

**Cart:** Right-side drawer, not a full page. Free-shipping progress bar ("You're $38 away from free shipping," $50 threshold) sits above a cross-sell carousel recommending the full-price core product ($43) as an add-on to a cart that (in the captured state) contains only a $12 accessory item — the accessory-only cart is $38 below the free-shipping bar with no lower-cost path shown to close that gap other than the full-price core product.

## Cross-Source Themes

Ranked by evidence strength × revenue potential × funnel importance:

1. **Trust/rating discrepancy between site claim (4.9/5, 200,000+ customers) and two independent third-party sources (Amazon 3.8/5, Trustpilot 3.5 TrustScore).** Corroborated by Social & Community Research and confirmed live on-site. High revenue potential (trust signals sit directly in the hero and PDP buy box, both high-traffic conversion points) and high evidence strength (two independent platforms agree).
2. **Catastrophic Total Blocking Time (8.6s homepage / 17.6s PDP) despite fast paint scores.** Confirmed via Lighthouse JSON on both key pages, with the floating chat widget and multiple carousel/video embeds visible in screenshots as likely contributors. High funnel importance — this sits on every homepage and PDP session, not a single page.
3. **Ad-to-landing message mismatch: use-case-segmented Google Ads (sleep, moto, festival) land on a single Pacha-festival-themed homepage hero regardless of ad intent, and ad-stated offers ("45% Off," "Buy 2 & Get 10% Off") don't match the live sitewide offer ("Buy 2, Get 1 Free").** Evidence from Google Ads visual summary cross-checked against live homepage. Directly affects paid traffic, which is the highest-intent, highest-cost segment.

## Top Test Opportunities

**Fix the ad-to-homepage message mismatch for non-Pacha traffic** — Google Ads segment by use case (sleep, moto, festival, concert) but 100% of homepage traffic lands on one Pacha-festival hero with no dynamic swap; a "Best Earplugs for Sleep" ad click lands on a beach/cocktail festival image with no sleep messaging above the fold. Evidence: Google Ads visual summary, live homepage WebFetch. Est. lift: 0.5-1% CR lift x unknown sessions/mo x $43 AOV = revenue unknown (sessions/mo not collected).

**Reduce Total Blocking Time on PDP (17.6s) and homepage (8.6s)** — Both pages paint fast but take 65-86 seconds to become fully interactive per Lighthouse; the floating "Ask a question" AI-chat widget, UGC video carousels, and embedded review widgets are visible on every fold and are the likely script-weight contributors. Evidence: PageSpeed JSON (homepage + PDP), site screenshots. Est. lift: 0.5-1.5% CR lift x unknown sessions/mo x $43-46 AOV = revenue unknown (sessions/mo not collected); TBT at this level is known industry-wide to suppress add-to-cart rate on mobile.

**Reconcile the review-count/rating discrepancy between site and third-party platforms** — Site claims 4.9/5 by 200,000+ customers; Amazon shows 3.8/5 (232 ratings), Trustpilot shows 3.5 TrustScore (1,284 reviews). A shopper who checks Amazon or Trustpilot before buying sees a materially different story than the PDP hero claims. Evidence: last30days-ecom (Trustpilot + Amazon, corroborated across two platforms), live PDP/homepage WebFetch. Est. lift: 0.5-1% CR lift x unknown sessions/mo x $43-46 AOV = revenue unknown.

**Correct or contextualize the swatch-availability contradiction on PDP** — The "Color: Pacha Edition 2.0" swatch row shows one option with a diagonal strike-through (unavailable) sitting directly beside a green "In stock ready to ship" status message with no distinction between "this exact color is out" vs "the product overall is in stock." Evidence: site-visual-summary.md PDP Fold 1 description. Est. lift: 0.3-0.5% CR lift x unknown sessions/mo x $43-46 AOV = revenue unknown.

**Surface a clearer low-cost path to the $50 free-shipping threshold from the cart drawer** — Cart shows "$38 away from free shipping" with only a full-price $43 core product offered as the cross-sell, no lower-cost add-on (e.g., the $9-12 accessory-tier items) shown as a closer-gap option. Evidence: cart screenshot description (site-visual-summary.md). Est. lift: 0.3-0.8% AOV lift x unknown sessions/mo x $50 avg cart = revenue unknown.

**Default the PDP to the core product, not a promotional edition, for non-search traffic** — Live WebFetch confirms "Brass Blue" is the actual PDP default, but the collection page and paid-search click-throughs push users toward "Pacha Edition 2.0," a limited/partially-OOS colorway; confirming which is the intended default for ad landing pages closes an internal inconsistency between merchandising and paid traffic intent. Evidence: manifest open question resolved via live WebFetch (2026-09-13), collection/PDP screenshots. Est. lift: 0.3-0.6% CR lift x unknown sessions/mo x $43-46 AOV = revenue unknown.

**Test moving the 100-day guarantee and warranty trust badges higher on the PDP** — Currently the "100-day money back guarantee" sits below the Add to Cart button and the "2 Year Warranty" / "100-Day Free Returns" badges only appear in the cart drawer, not on the PDP buy box itself, at a point when trust signals matter most given the rating discrepancy above. Evidence: PDP and cart screenshot descriptions (site-visual-summary.md). Est. lift: 0.3-0.5% CR lift x unknown sessions/mo x $43-46 AOV = revenue unknown.

**Investigate and fix unloaded/placeholder product images on the collection page** — Hears Sleep grid, Accessories, and Merch sections show gray placeholder blocks in place of product photography in the captured folds; unclear if this is a lazy-load timing artifact or a persistent bug, but it sits directly in the browse-to-PDP path. Evidence: site-visual-summary.md Collection Fold 2-3. Est. lift: 0.2-0.5% CR lift x unknown sessions/mo x $43-46 AOV = revenue unknown; flagged as needing live re-verification before building a test brief.

**Clarify the "GET A FREE SET OF HEARS" collapsed side-tab CTA** — A vertical tab on the homepage's left edge promises a free set but is collapsed/unexplained across all three homepage screenshot folds, with no visible expanded state captured; unclear mechanic (referral? giveaway? contest?) may be under-leveraged as an acquisition or list-growth CTA. Evidence: site-visual-summary.md Homepage Layout notes. Est. lift: 0.2-0.4% CR/list-growth lift x unknown sessions/mo x $43-46 AOV = revenue unknown.

**Segment ad-to-Google-Shopping traffic away from third-party reseller listings** — Google Ads Transparency shows three third-party resellers (On Web Consulting Ltd, ShopForward B.V., Now-Sale.co) running verified Shopping listings using Hears product images alongside Hears' own account; unclear if these are authorized resellers or arbitrage, and inconsistent offer framing ("45% Off," "Buy 2 & Get 10% Off") versus the live site promo ("Buy 2, Get 1 Free") risks a broken-promise landing experience for a meaningful slice of paid traffic. Evidence: Google Ads visual summary. Est. lift: not a CR test — this is a channel-integrity/brand-control finding to route to the client directly, included here because it affects the same ad-to-site funnel as opportunity #1.

## Unused but Valuable Findings

- The Saint Laurent x Hears fashion collaboration (corroborated across Pinterest and independent editorial coverage) is not reflected anywhere in the current homepage or PDP messaging — a positioning opportunity distinct from any CRO test, worth a separate creative/merchandising conversation with the client.
- Reviewers repeatedly self-report wanting to size up in attenuation (20dB → 25dB) after purchase — a signal for a post-purchase or PDP cross-sell flow rather than a homepage/PDP layout test.

## Missing Data

- Reviews & UGC: the collected on-site review file is near-uniformly 5-star and does not represent real customer friction — the "What Frustrates Customers" section above is intentionally thin because inventing complaints would violate this audit's data-integrity rule. The Trustpilot/Amazon rating gap is the best available substitute evidence for real dissatisfaction themes, but it does not name specific complaint topics.
- Monthly sessions and AOV were not provided in the manifest or any collected source — every dollar estimate in Top Test Opportunities above is left as "revenue unknown" rather than invented.
- Mobile-specific PDP sticky-cart behavior was not captured (only desktop-width screenshots exist) — flagged, not assumed either way.
- Collection-page placeholder/unloaded images could not be re-verified live in this pass (WebFetch returns text only, not rendered images) — flagged for manual re-check before roadmap execution.
