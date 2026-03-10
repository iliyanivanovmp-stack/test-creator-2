---
description: Convert a CRO roadmap markdown file into a branded HTML one-pager for clients
---

You are converting a CRO testing roadmap from a detailed internal execution format into a branded, client-facing HTML one-pager. The HTML version is what the client sees. The markdown stays internal.

The goal: an executive can scan the HTML in 60 seconds, understand what we're testing, why, and what the revenue opportunity is.

## Step 1: Collect Inputs

Ask the user for:

1. **Client name and roadmap file.** List the markdown roadmap files in the client's folder under `clients/[client-name]/` and let them pick. If only one roadmap exists, confirm it.
2. **Homepage screenshot.** Ask the user to paste or provide a screenshot of the client's homepage. Use this to extract:
   - Primary brand color (hex)
   - Secondary/accent color if present
   - Overall visual style (light/dark, minimal/bold)
3. **Logo URL** (optional). A URL to the client's logo image. If not provided, skip the logo in the header.

## Step 2: Read and Analyze

- Read the selected roadmap markdown file.
- Analyze the homepage screenshot to determine brand colors and visual tone.
- Identify the roadmap structure: does it have an Insights/What We Found section? How many slots? A/B tests vs dev projects?

## Step 3: Extract and Condense Content

From the roadmap, extract:

- **Title:** The month and year from the H1.
- **Insights summary:** If an Insights or "What We Found" section exists, condense it to 2-3 sentences max. Lead with the single biggest finding. Include the revenue opportunity number. If no Insights section exists, synthesize a 1-2 sentence summary from the test hypotheses and revenue potentials.
- **Per-slot cards:** For each slot, extract:
  - Slot number(s) (e.g., "Slot 1" or "Slots 1 & 2")
  - Test or project name
  - Type: "A/B Test" or the dev project type (e.g., "Custom Shopify App")
  - Page being tested
  - Revenue potential: the final dollar figure only (e.g., "$180K/mo"), not the math
  - A 1-2 sentence plain-language description of what we're testing/building and why. Rewrite the hypothesis into direct language. No source citations.
- **Total revenue opportunity:** Sum the revenue potential figures across all slots.

**Drop entirely:**
- Variation descriptions (V1, V2, etc.)
- Briefs (design and dev specs)
- Data sections with source citations
- Mobile/desktop specifications
- Scheduling and sequencing notes
- Future Slot Candidates section
- Data Sources line

**Content rules:**
- No em dashes. Use periods, commas, or colons.
- Every word earns its place. No filler, no hedging, no fluff.
- Direct, active voice. Short sentences.
- Revenue potential: just the final number. "$180K/mo" not "1.2M sessions/mo at $100 AOV. A 0.15% CR lift = ~1,800 orders = ~$180K/mo."
- Dev projects without clear dollar figures: show "Impact to be measured" instead of leaving blank.

## Step 4: Generate HTML

Build a self-contained HTML file. All CSS in a `<style>` tag in the `<head>`. No external stylesheets, no JavaScript, no CDN links. The file must work offline.

### HTML Template Structure

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Month Year] Testing Roadmap - [Client Name]</title>
  <style>
    /* All CSS here, using --brand and --brand-light custom properties */
  </style>
</head>
<body>
  <!-- Header: logo (if provided) + title -->
  <!-- Executive Summary card -->
  <!-- Slot cards grid -->
  <!-- Footer -->
</body>
</html>
```

### CSS Specifications

Set CSS custom properties from the brand colors extracted from the homepage screenshot:
- `--brand`: primary brand color (hex from screenshot analysis)
- `--brand-light`: a 10% opacity version of the brand color for card backgrounds
- `--text`: #1a1a1a
- `--muted`: #666
- `--bg`: #f8f8f8
- `--card-bg`: #ffffff

Core styles:
- Font: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- Max width: 900px, centered with auto margins
- Padding: 48px 24px

**Header:**
- If logo provided: logo image left-aligned, max-height 40px, margin-bottom 16px
- Title: H1, font-size 28px, color var(--brand), font-weight 700
- Subtle 2px horizontal rule in the brand color below the title

**Executive Summary Card:**
- Background: var(--bg)
- Border-radius: 8px
- Padding: 24px
- Margin: 32px 0
- Text: 15px line-height 1.6
- The total revenue opportunity sits at the bottom of this card: font-size 20px, font-weight 700, color var(--brand)

**Slot Cards Grid:**
- CSS Grid: `grid-template-columns: repeat(2, 1fr)` with 20px gap
- Each card:
  - Background: var(--card-bg)
  - Border-radius: 8px
  - Box-shadow: 0 1px 3px rgba(0,0,0,0.08)
  - Border-left: 4px solid var(--brand)
  - Padding: 24px
- Inside each card:
  - **Top row:** Slot label (small, muted, uppercase, 11px tracking) and type badge (small rounded pill, 11px, uppercase, brand color background with white text for A/B tests, outlined for dev projects)
  - **Test name:** H3, font-size 18px, font-weight 600, margin-top 12px
  - **Page:** Below the name, muted text, 13px
  - **Revenue number:** Font-size 28px, font-weight 700, color var(--brand), margin 16px 0
  - **Description:** 14px, line-height 1.5, color var(--text)

**Footer:**
- Margin-top: 48px, padding-top: 24px
- Border-top: 1px solid #e0e0e0
- Text: 13px, color var(--muted), center-aligned
- Content: just the month and year

**Responsive:**
```css
@media (max-width: 640px) {
  .slots-grid { grid-template-columns: 1fr; }
  h1 { font-size: 24px; }
  .revenue { font-size: 24px; }
}
```

**Print:**
```css
@media print {
  body { padding: 24px; }
  .card { box-shadow: none; border: 1px solid #e0e0e0; break-inside: avoid; }
}
```

## Step 5: Save

Write the HTML file in the same client folder as the source roadmap:
- If source is `clients/froya/march-2026-roadmap.md`, save as `clients/froya/march-2026-roadmap.html`
- If source is a versioned file like `march-2026-roadmap-v2.md`, save as `march-2026-roadmap-v2.html`

After saving, tell the user the file path so they can open it in a browser or save as PDF.

## Pre-Publish Checklist

Before saving, verify silently:
- [ ] No em dashes anywhere in the output
- [ ] No variation descriptions, briefs, or source citations leaked through
- [ ] Every slot card has a revenue figure (or "Impact to be measured")
- [ ] Total revenue opportunity matches the sum of individual slots
- [ ] Brand color from the screenshot is applied consistently
- [ ] HTML is valid and self-contained (no external dependencies)
- [ ] Executive summary is 2-3 sentences max, not a wall of text
- [ ] Each slot description is 1-2 sentences max
