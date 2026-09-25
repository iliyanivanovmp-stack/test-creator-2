# SVibe Roadmap Seed

**Store:** svibe.com
**AOV:** unknown (PDP unit price $149 for flagship Snail Curve, $69-$89 for other bestsellers)
**Monthly sessions:** unknown
**Data sources:** Meta Ads & Landing Pages, Google Ads Transparency, Reviews & UGC, PageSpeed/Core Web Vitals, Current Site Screenshots, Social & Community Research, Competitor Analysis (self-researched)

## Key Insights

Paid acquisition has a message-match problem that gets worse the further a shopper travels from Ad 1. Ad 1 (Snail Curve) matches its landing page cleanly, but Ad 2 (Snail Jovi Arc) drops the ad's "hands-free internal pleasure" framing for a "Longer Erections"/couples-ring angle, and Ad 3 (Snail Jovi) links to an entirely different emotional landing page template ("Reconnect. Without the awkward conversation.") that carries none of the ad's product claims and shows a different price ($69) than the related Jovi Arc PDP context ($89). Google Ads repeats a "2 years warranty, 30 days return policy" line and "$10 off sign up" / "Save up to $30" offers on nearly every unit — neither is honored on any of the three Meta-linked landing pages reviewed.

Mobile performance is a hard blocker sitting under all of this: the homepage (10.2s LCP) and the Snail Curve PDP (13.5s LCP) both score 61/100 on mobile PageSpeed, 4-5x over Google's 2.5s "good" threshold. The PDP is the direct landing page for Ad 1 and the pricing-context page referenced by Ad 2 — meaning paid traffic is landing on the two slowest pages on the site.

Reviews (pasted by user) surface a specific claims-accuracy conflict: the live PDP's "Whisper quiet" trust badge is directly contradicted by a verified reviewer ("Not whisper quiet, but not distracting" — Shanna Church, 8/23/2026). Cleaning difficulty and lubricant necessity are recurring unprompted complaints that never appear pre-purchase. Off-site sentiment (Trustpilot: 3.8/113 reviews as of 2026-09-22) runs cooler than the on-site 4.8/2,847 — directional, not corroborated by first-party evidence, but worth watching.

## Top Test Opportunities

### 1. Fix Ad 3 (Snail Jovi) landing page message match
**What's broken:** Ad 3's video creative promises "two motors, a remote," names the product "Snail Jovi," and frames it as one of two couples rings the creator "tried." The linked landing page uses a completely different template: a hero headline "Reconnect. Without the awkward conversation," a "Sound familiar?" section with four numbered relationship pain-point blocks (Frequency Drop, Routine, Wanting to Reconnect, Missing the Early Days), each paired with a lifestyle photo. The only product reference anywhere in the three captured folds is a persistent sticky bottom bar showing a product thumbnail, "Snail Jovi $69 $89," and a "Let's try this" button — no motor count, no remote, no feature list, no star-rating icons (only a text line "Rated 4.7/5 by 358 couples · Ships discreetly · 2-year warranty" under the hero CTA).
**Evidence:** Meta Ads visual summary (Ad 3)
**Key data:** Price shown ($69) differs from the Jovi Arc PDP price context seen via Ad 2 ($89 base)
**Est. lift:** 0.5-1.5pp CVR recovery on Ad 3 traffic x unknown sessions/mo x $69 AOV = withheld pending session data

### 2. Compress PDP mobile LCP below 4 seconds
**What's broken:** The Snail Curve PDP (svibe.com/products/female-vibrator-curve-svibe) — the landing destination for Ad 1 and the pricing-context page for Ad 2 — takes 13.5 seconds to reach Largest Contentful Paint on mobile, against Google's 2.5s "good" threshold. The page structure is a left-column hero product image with a 6-thumbnail strip below, and a right-column buy box (title, price, rating, 4 trust badges, color swatches, Add to Cart button) — likely the hero image or thumbnail strip is the LCP element given the page's heavy visual weight.
**Evidence:** PageSpeed JSON (svibe-pdp-pagespeed.json, fetched 2026-09-23), Site Screenshots (confirms this PDP as the ad-1 landing page)
**Key data:** Performance score 61/100, LCP 13.5s, FCP 4.7s, TTI 14.8s, CLS 0
**Est. lift:** 0.3-1.0pp CVR on mobile paid traffic x unknown sessions/mo x $149 AOV = withheld pending session data

### 3. Compress homepage mobile LCP below 4 seconds
**What's broken:** The homepage hero is a full-width purple background image of a hand holding the Snail Curve against a shoulder/back, with a left-aligned text block (5-star icon row, "Different Feels Better" headline, "SHOP NOW" button) layered on top. This large hero image is the likely LCP element, loading in 10.2 seconds on mobile — over 4x the 2.5s threshold.
**Evidence:** PageSpeed JSON (svibe-homepage-pagespeed.json, fetched 2026-09-23), Site Screenshots (homepage fold 1)
**Key data:** Performance score 61/100, LCP 10.2s, FCP 4.2s, TTI 15.5s, CLS 0
**Est. lift:** 0.3-0.8pp CVR x unknown sessions/mo x $149 avg order = withheld pending session data

### 4. Surface warranty/returns claim in the PDP buy box and cart drawer
**What's broken:** "2 Year Warranty" and "30 days return policy" are headline trust claims repeated in nearly every Google text ad and shown as an icon badge directly in the Snail Jovi Arc PDP buy box (next to "Secure Checkout" and "Discreet Shipping"). On the Snail Curve PDP, the same warranty information exists only inside a collapsed "Warranty" accordion below the fold — not visible in the buy box itself, where the visible trust row is instead "Never loses contact / 600+ combinations / Whisper quiet / 100% Body Safe." The cart drawer (slide-out, triggered from any Add to Cart action) shows a green free-shipping banner, a gift line item with countdown timer, two AOV checkboxes (Order Protect $3.95, Extra Discreet Packaging free), and a "SECURE CHECKOUT" button — no warranty or returns copy appears anywhere in the drawer.
**Evidence:** Google Ads visual summary, Site Screenshots (PDP buy box + cart drawer)
**Key data:** Warranty claim appears in Google Ads copy and Jovi Arc PDP badge row but not in Curve PDP buy box or cart
**Est. lift:** 0.2-0.5pp CVR x unknown sessions/mo x $149 AOV = withheld pending session data

### 5. Reconcile the "Whisper quiet" PDP badge against reviewer feedback
**What's broken:** The Snail Curve PDP shows a 4-icon trust badge row directly below the star rating link, reading "Never loses contact / 600+ combinations / Whisper quiet / 100% Body Safe." A verified on-site review states: "Not whisper quiet, but not distracting." (Shanna Church, 8/23/2026) — a direct contradiction of the specific claim in that badge.
**Evidence:** Reviews (pasted by user), Site Screenshots (PDP fold 1, trust badge row)
**Key data:** Verified reviewer quote directly contradicts the "Whisper quiet" badge copy
**Est. lift:** Not a CVR-lift test — a claims-accuracy fix that protects trust-badge credibility and reduces post-purchase complaint/return risk

### 6. Surface cleaning and lubricant requirements before purchase
**What's broken:** The PDP's captured folds (hero + buy box, UGC carousel, "The details" 5-feature callout section) contain no mention of cleaning method or lubricant requirement anywhere in the product description or the three collapsed accordions (How To Use / Specifications / Warranty — contents not visible since collapsed). Reviews raise both unprompted: "the design makes it a bit difficult to clean thoroughly" (Alora Aldrige, 8/25/2026) and "Must use lubricant with this material." (Kearstin, 9/16/2026).
**Evidence:** Reviews, Site Screenshots (PDP folds 1-3, no mention found)
**Key data:** Two independent verified reviewers raise these points unprompted
**Est. lift:** Reduces return/refund rate rather than lifting CVR directly; pairs with the warranty-surfacing test as a trust/expectation-setting theme

### 7. Add a sticky mobile Add-to-Cart bar on the PDP
**What's broken:** The Snail Curve PDP's "ADD TO CART — $149.00" button sits directly under the color swatches, above the fold on desktop, with no sticky/persistent equivalent as the shopper scrolls into fold 2 (UGC video carousel, "Real homes, real views" grid) or fold 3 ("The details" 5-feature section, "Curve or Gizi?" comparison intro). The only persistent element observed across the site is an unrelated bottom-left "Mystery Discount + FREE Guide" popup tab, not a purchase CTA.
**Evidence:** Site Screenshots (PDP folds 1-3, CTA behavior notes)
**Key data:** No sticky Add to Cart bar observed in any of the three captured PDP folds
**Est. lift:** 0.2-0.6pp CVR on PDP sessions x unknown sessions/mo x $149 AOV = withheld pending session data

### 8. Disambiguate "Snail Jovi" vs. "Snail Jovi Arc" naming site-wide
**What's broken:** Two distinct products, "Snail Jovi" ($69, list $129, 46% off) and "Snail Jovi Arc" ($89, list $99, 10% off), share a near-identical name differing only by one word. This already produced a visible downstream error: Ad 3 names its product "Snail Jovi" and describes features ("two motors, a remote") that, per Ad 2's landing page, belong to "Snail Jovi Arc" instead — the two products' identities have bled into each other across paid creative.
**Evidence:** Meta Ads visual summary (Ads 2 and 3), Homepage live verification (2026-09-23 pricing)
**Key data:** Live-confirmed pricing: Snail Jovi $69/$129 (46% off), Snail Jovi Arc $89/$99 (10% off)
**Est. lift:** Reduces misdirected-purchase and support/return risk; a broader, site-wide naming fix that the Ad 3 message-match test (opportunity #1) is the strongest single example of

## Unused Findings

- Trustpilot's 3.8 TrustScore (113 reviews, as of 2026-09-22) runs cooler than the 4.8/2,847 on-site rating — a monitoring signal, not an independently actionable test.
- A third-party case study (Boost agency) claims a prior dark/sensorial redesign lifted SVibe's revenue per visitor 33.9% — unverified by first-party evidence collected in this audit, flagged rather than acted on.
- Award badges (2024 Awards Winner, HBIZ Europa, Sexual Freedom Awards finalist) exist only inside a separate quiz-block panel on the collection page, invisible to a shopper scanning the product grid — a candidate for surfacing directly on product cards.
- Independent YouTube reviewer coverage exists specifically for the Snail Curve — a possible source for third-party review clips to supplement the PDP's currently brand-only UGC carousel.
