# CRO Workflow — Handoff Doc

This system generates CRO audits and testing roadmaps for Shopify brands. It runs entirely through Claude Code slash commands. Output is markdown files saved to `brands/[brand-name]/`.

---

## Command Pipeline

Each command runs in its own fresh session. No command inherits context from the previous one — everything passes through files on disk.

```
/cro-collect
    ↓ manifest.md + raw/*.md + screenshots folder
/cro-audit
    ↓ [brand]-research-audit.md (updated manifest)
/cro-research-roadmap
    ↓ [brand]-[month]-[year]-roadmap.md
/roadmap-to-html
    ↓ [brand]-[month]-[year]-roadmap.html
```

| Command | What it does | Output |
|---------|-------------|--------|
| `/cro-collect` | Intake only. Asks which sources are available, collects text/URLs in chat, confirms screenshots are in folder. Zero analysis. | `manifest.md` + `raw/` files |
| `/cro-audit` | Fresh session. Reads all disk files, loads screenshots on-demand, WebFetches store URL + Meta ad LPs, researches competitors. Writes the full research audit. | `[brand]-research-audit.md` |
| `/cro-research-roadmap` | Fresh session. Reads audit only. Greps CRO ebook + does community research for ideation fuel. Writes prioritized A/B test roadmap. | `[brand]-[month]-[year]-roadmap.md` |
| `/roadmap-to-html` | Fresh session. Reads roadmap + audit. Extracts brand colors from homepage screenshot. Generates Shopify-safe HTML with Tests tab + Data Insights tab. | `[brand]-[month]-[year]-roadmap.html` |
| `/cro-roadmap` | Separate pipeline for existing clients with internal analytics (GA4, heatmaps, Intelligems). Not part of the prospect workflow above. | `[brand]-[month]-[year]-roadmap.md` |

---

## Brands Folder Structure

```
brands/[brand-name]/
├── manifest.md                    # Handoff artifact — what was collected, status, next step
├── raw/
│   ├── meta-ads.md                # Landing page URLs (fetched during /cro-audit)
│   ├── reviews.md
│   ├── pagespeed.md
│   ├── competitors.md
│   ├── emails.md
│   ├── context.md
│   ├── google-ads.md
│   ├── inspiration.md
│   └── screenshots/
│       ├── meta-ad-1.png          # Ad creative
│       ├── meta-ad-1-lp-f1.png    # Landing page fold 1
│       ├── meta-ad-1-lp-f2.png
│       ├── meta-ad-1-lp-f3.png
│       ├── homepage-f1.png
│       ├── homepage-f2.png
│       ├── homepage-f3.png
│       ├── collection-f1.png
│       ├── collection-f2.png
│       ├── collection-f3.png
│       ├── pdp-f1.png             # Optional
│       ├── cart.png
│       └── google-ads.png
├── [brand]-research-audit.md
├── [brand]-[month]-[year]-roadmap.md
└── [brand]-[month]-[year]-roadmap.html
```

---

## Core Design Principle

**Each command starts with a clean context window.**

The biggest enemy of good CRO ideas is a saturated context. When an agent generates test hypotheses after spending tokens on data intake, its thinking is shaped by the weight of the collection — not by pattern recognition. Every command boundary in this pipeline is a deliberate context reset.

- `/cro-collect` never analyzes anything. It just saves data to disk.
- `/cro-audit` starts fresh, reads everything from disk, does all analysis in one focused session.
- `/cro-research-roadmap` starts fresh with only the audit. It adds ebook patterns and community research for ideation at the exact moment they're useful — not before.
- `/roadmap-to-html` starts fresh with only the roadmap and audit.

Screenshots never enter the chat window during collection. They live on disk and are loaded on-demand during the audit session only.

---

## What Changed in the Last Session

**1. CRO ebook + community research moved from audit to roadmap command.**
These are ideation accelerators (pattern libraries), not data sources. They were being used in the heaviest context window. They now run at the start of `/cro-research-roadmap` when the agent is in ideation mode with a clean context.

**2. `## Top Test Opportunities` section added to the audit.**
The audit now ends with a ranked list of up to 5 specific, testable opportunities scored by evidence strength × revenue potential × fixability. The roadmap command reads this list first and picks slots from the top down — instead of re-deriving priority from scratch.

**3. `/cro-research` split into `/cro-collect` + `/cro-audit`.**
Previously, data collection and audit writing happened in the same session. The audit was being written with all the collection context still warm. Now collection is purely mechanical (zero analysis, zero screenshot loading, zero WebFetch), and the audit runs in a fresh session reading everything from disk.
