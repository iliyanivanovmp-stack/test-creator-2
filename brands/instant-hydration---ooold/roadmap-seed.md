# Instant Hydration Roadmap Seed

**Store:** https://instanthydration.com
**AOV:** unknown ($27.50 subscription / $49.50 one-time per box, per PDP)
**Monthly sessions:** unknown
**Data sources:** Meta Ads and Landing Pages, Google Ads Transparency, PageSpeed / Core Web Vitals, Current Site Screenshots, Reviews & UGC, Social & Community Research, Competitor research (self-researched), Non-Data Context

## Key Insights

Subscription enrollment/cancellation is the most evidence-backed friction point. Two 1-star Amazon/Trustpilot reviews describe being converted to a subscription without authorization ("Cannot Cancel," "SCAM... $99 charge"), corroborated by the Trustpilot summary in Social & Community Research. The PDP screenshot shows why: a locked incentive list (sampler, shipping, water bottle) unlocks only after a flavor and delivery frequency are chosen, with no default pre-selection.

On-page priority doesn't match the trust-signal architecture or Google Ads spend. Energy+, confirmed by TikTok/LinkedIn evidence as a genuine pivot ("the moment Instant Hydration becomes more than a hydration brand"), owns the homepage hero and audited PDP, yet that PDP shows zero star rating or review count across three folds, despite the homepage's "2M+ Orders | 100M+ Servings" badge one click away. Google Ads still favors the core line; Energy+ is only one minor display unit.

Ad-to-landing-page match breaks on two of three Meta campaigns. The Target ad ("RUN don't walk to Target") lands on a standard DTC page — WebFetch shows only a generic "Find in Store" link, no Target text. ICEE and Luigi's collab ads match hero imagery, but the buy box title and "Select from 14 Flavors" CTA never name the collab flavor.

## Top Test Opportunities

### 1. Default-select a flavor on the Energy+ PDP
**What's broken:** Buy box shows two flavor tiles (Sour Green Apple, Tropical Crush), each with a quantity stepper starting at 0, none pre-selected. Primary CTA stays disabled, reading "SELECT A FLAVOR," until a quantity is set. A locked incentive list below (sampler, shipping, water bottle) stays inert until then.
**Evidence:** Site Screenshots (PDP fold 1)
**Est. lift:** 3-5% CR lift x sessions/mo x AOV = pending session data

### 2. Add review/star-rating trust signal to the Energy+ PDP
**What's broken:** No star rating or review count appears in any of the three PDP folds captured, despite the homepage leading with "2M+ Orders | 100M+ Servings" one click away.
**Evidence:** Site Screenshots (PDP vs. Homepage)
**Est. lift:** 2-4% CR lift x sessions/mo x AOV = pending session data

### 3. Fix Target-ad landing page message match
**What's broken:** Ad 2 sells in-store Target availability ("officially on shelves at Target"); its landing page shows only a generic "Find in Store" link, no Target-specific text anywhere.
**Evidence:** Meta Ads visual summary, live WebFetch
**Est. lift:** reduces post-click bounce on this ad; needs ad-level data

### 4. Carry collab branding into the buy box and CTA
**What's broken:** ICEE/Luigi's landing pages open with matching hero banners, but the buy box below reads generic "Instant Hydration Electrolyte Powder," CTA reads "Select from 14 Flavors" — no collab name in either.
**Evidence:** Meta Ads visual summary, live WebFetch
**Est. lift:** 2-3% CR lift on collab-ad traffic x sessions/mo x AOV = pending data

### 5. Reduce homepage/PDP Time to Interactive and Total Blocking Time
**What's broken:** Mobile Lighthouse: Homepage 48/100 (TTI 31.8s, TBT 1,410ms), PDP 47/100 (TTI 34.1s, TBT 1,840ms) — both "poor." CLS is 0 on both. Pages render but resist tap interaction for over half a minute, ahead of a flow requiring manual selection.
**Evidence:** PageSpeed mobile lab data, 2026-09-09
**Est. lift:** 3-6% CR lift x sessions/mo x AOV = pending session data

### 6. Clarify subscription enrollment at the point of selection
**What's broken:** The PDP's flavor-selection step is where subscribe-vs-one-time is decided, but two 1-star reviews describe ending up subscribed without realizing it during this flow, corroborated independently by the Trustpilot summary.
**Evidence:** Reviews & UGC, Social & Community Research
**Est. lift:** reduces support tickets/negative reviews; measure via review sentiment, not CR

### 7. Add an AOV mechanism to the cart page
**What's broken:** Cart shows one line item, a large empty white space, then checkout summary — no upsell, cross-sell, bundle offer, or free-shipping progress bar anywhere.
**Evidence:** Site Screenshots (Cart)
**Est. lift:** 3-5% AOV lift x sessions/mo x current AOV = pending data

### 8. Give the core electrolyte line equal homepage visual weight
**What's broken:** The core 14-flavor line — tied to most reviews and Google Ads volume — is one fold-2 tile equal in size to Energy+, despite Energy+ being the newer, not-yet-best-selling product per Non-Data Context.
**Evidence:** Site Screenshots (Homepage), Non-Data Context, Google Ads visual summary
**Est. lift:** 2-4% CR lift on non-Energy+ traffic x sessions/mo x AOV = pending data

### 9. Align Google Ads spend with current on-site priority (Energy+)
**What's broken:** Homepage and audited PDP are built around Energy+, confirmed as a genuine pivot by TikTok/LinkedIn evidence, but Google Ads shows Energy+ as one minor display unit against the core line's dominant presence.
**Evidence:** Google Ads visual summary, Site Screenshots, Social & Community Research
**Est. lift:** not a CR test — paid-media reallocation; needs spend/CVR data

### 10. Address the "50 Day Happiness Guarantee" return-shipping gap
**What's broken:** Ads and site badges market "Try Risk Free for 50 Days," but a 3-star reviewer reports paying return shipping inside that window.
**Evidence:** Reviews & UGC
**Est. lift:** not a CR test — policy fix; measure via complaint volume

## Unused Findings

- A Trustpilot reviewer alleges "invited" reviews skew more positive than organic ones — worth flagging, not a test.
- The TSA/travel-hack TikTok post (@laurenwolfe, 18.6K views) is the top organic post this window and isn't reflected in paid creative or site messaging — a content angle, not a test.
