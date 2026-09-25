# Labareau — Social & Community Research (last30days-ecom)

> Third-party/community research. Directional only — treat findings as hypotheses until confirmed by first-party reviews or site evidence elsewhere in the audit.

**Mode:** Engine
**Date:** 2026-09-11

## Sources Run

- TikTok: active @labareau account with recent branded content — passed precheck
- Instagram: two active accounts found (@labareau, @labareauofficial) — passed precheck, but the engine's Instagram reel search hit a 404 on the ScrapeCreators endpoint and returned 0 items despite the account being active
- Pinterest: at least one brand-relevant pin found — passed precheck (weak signal)
- Trustpilot: a Trustpilot profile exists at trustpilot.com/review/labareau.com — passed precheck, but the engine's own Trustpilot lookup returned a 404 (see note below)
- Web: always run

## Sources Skipped

- Reddit: zero results actually about the brand — only coincidental word matches on unrelated place names
- X/Twitter: no x.com posts found for "Labareau"; only the brand's own site and unrelated results
- YouTube: zero relevant hits — all results were unrelated "Labubu" toy content, a phonetic collision
- Amazon: no Labareau listings found on amazon.com

## Findings by Source

### TikTok
The brand's own @labareau account is active and posting recent giveaway/promotional content. The most engaged post in the date window (2026-08-13) is a giveaway announcement: "LINDSAY'S FAVORITES ARE YOURS TO WIN... Our biggest giveaway yet is here. 9 winners... Over €5,400 in total prize val[ue]," which drove 61,208 views, 459 likes, and 25 comments — by far the highest-engagement item across every source checked. Comments on the post are positive and low-friction ("Heel mooi!", "GEWELDIG!! Dit wil je toch"). Source: [tiktok.com/@labareau/video/7673157203129290016](https://www.tiktok.com/@labareau/video/7673157203129290016)

### Web
Independent coverage skews toward founder/brand-story press rather than product reviews. LinkedIn posts from the brand and from founder Lindsay van der Looij reference a feature in LINDA (a Dutch magazine), published 2026-08-27, and describe Labareau as built on a "SAXZ-12" clinical formula with "over 20 years of clinical experience," founded in 2021, headquartered in Amsterdam, with 1-10 employees. Source: [nl.linkedin.com — LABAREAU/LINDA feature](https://nl.linkedin.com/posts/labareau_lindsay-van-der-looij-deelt-beautytips-activity-7498685629627617280-eeVB), [linkedin.com — Lindsay van der Looij](https://www.linkedin.com/posts/lindsayvanderlooij_proud-to-share-my-story-with-linda-after-activity-7498643640802566145-hMlt)

Dutch beauty blog FEM/Drimble covered a specific product launch ("The BB Filter," a day cream) on 2026-08-24 under the headline "Dit product van LABAREAU móét je hebben voor een natuurlijke sun-kissed glow." Source: [drimble.nl](https://drimble.nl/vrouw/blogs/105977620/dit-product-van-labareau-moet-je-hebben-voor-een-natuurlijke-sun-kissed-glow.html)

SkinCarisma's product database lists Labareau with 10 catalogued products spanning serums, essence, ampoules, sunscreen, and exfoliating scrubs/peeling gel, including The AHA Peel, The Day Formula, and The Glow Getter 3 In 1 Hydrating Spray SPF 20. Source: [skincarisma.com/brands/8019](https://www.skincarisma.com/brands/8019)

A LinkedIn profile for a Labareau manager confirms the brand's Amsterdam base and an operating team since at least January 2024. Source: [linkedin.com/in/lisa-jonas](https://www.linkedin.com/in/lisa-jonas-08042b257)

### Pinterest
Weak, low-confidence signal. Of 18 pins found, most were pruned as off-target. The two surviving items were both actually re-shared Instagram posts (not native Pinterest content) about customer testimonials/reviews — one confirmed on-brand ("Nothing feels as good as reading your reviews... Real results, your honest thoughts"), the other flagged by the engine as an off-target match for a different brand ("LavishSkin," not Labareau — likely a keyword collision, not real Labareau content). Treat Pinterest findings here as low-confidence.

### Trustpilot — precheck vs. engine mismatch (flag)
The manual WebSearch precheck in Step 2 found a live Trustpilot profile at trustpilot.com/review/labareau.com with search-snippet-reported ratings varying between 4.0 stars (245 reviews) and 4.7 stars (382 reviews) depending on the snippet source — these numbers come from search-result summaries, not a verified page read, and should not be treated as confirmed. When the engine ran its own Trustpilot lookup, it returned an HTTP 404 and could not confirm the canonical domain or pull actual review content. This is a data gap, not evidence of an absent or negative Trustpilot presence — the profile exists per the precheck, but review-level content was not captured. Flag for manual verification during the audit if Trustpilot sentiment matters to the analysis.

### Instagram — coverage gap
Both @labareau and @labareauofficial accounts are confirmed active via search, but the engine's reel-fetching endpoint (ScrapeCreators) returned HTTP 404 for this query and could not pull actual reel content or captions. As with Trustpilot, this is a tooling gap, not evidence of low Instagram activity.

## Cross-Source Signal

Giveaways/promotions are the highest-engagement content type the brand runs (TikTok's top post by a wide margin is a giveaway, and the brand-provided metrics in `raw/context.md` independently confirm August's giveaway drove a record revenue month). This corroborates, from an outside angle, the brand's own framing that promotional/giveaway mechanics currently carry more weight in engagement and revenue than evergreen content.
