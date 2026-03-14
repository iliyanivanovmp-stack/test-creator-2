---
description: Convert a roadmap HTML file into a Shopify-pasteable version
---

You are converting a roadmap HTML file (the standalone version) into a Shopify-pasteable version that can be pasted directly into a Shopify page's custom HTML content area.

## Step 1: Identify the source file

Ask the user which HTML roadmap file to convert. List available `.html` files under `clients/` and let them pick. If one was just generated or is obvious from context, confirm it.

## Step 2: Read and convert

Read the source HTML file, then produce the Shopify version with these changes:

### Structure changes

1. **Strip document wrappers.** Remove `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>` tags and their closing counterparts. The output starts with the `<link>` tags for Google Fonts, then `<style>`, then `<div id="cvrt-roadmap">`.
2. **Remove non-pasteable head elements.** Drop `<meta>`, `<title>`, `<link rel="icon">` tags. Keep only Google Fonts `<link>` tags.

### CSS changes

3. **Full-bleed breakout.** The `#cvrt-roadmap` root must break out of Shopify's content container:
   ```css
   #cvrt-roadmap {
     width: 100vw;
     position: relative;
     left: 50%;
     right: 50%;
     margin-left: -50vw;
     margin-right: -50vw;
   }
   ```
4. **No max-width containers.** Remove `max-width` and `margin: 0 auto` from content wrappers, hero inner containers, stats bars, and footers. Everything should be full-width within the full-bleed container. The Shopify page's own container handles the outer width.
5. **Prefix ALL class names with `cvrt-`.** Every CSS class in both the `<style>` block and the HTML markup must be prefixed with `cvrt-` to prevent Shopify theme styles from overriding the roadmap design. Examples:
   - `.hero` becomes `.cvrt-hero`
   - `.card` becomes `.cvrt-card`
   - `.content` becomes `.cvrt-content`
   - `.footer` becomes `.cvrt-footer`
   - `.summary` becomes `.cvrt-summary`
   - `.tab-bar` becomes `.cvrt-tab-bar`
   - `.tab-panel` becomes `.cvrt-tab-panel`
   - `.section-label` becomes `.cvrt-section-label`

   This applies to every class. Generic names like `.hero`, `.card`, `.footer`, `.content` will be overwritten by Shopify themes. The `cvrt-` prefix plus the `#cvrt-roadmap` ID selector creates enough specificity to win over theme styles without `!important`.

6. **Keep `#cvrt-roadmap` ID scoping.** All CSS selectors must still be prefixed with `#cvrt-roadmap` (e.g., `#cvrt-roadmap .cvrt-hero`). The ID + class combination provides the specificity needed.

### Reference implementation

Use `clients/vyper/march-2026-roadmap-shopify.html` as the reference for correct Shopify structure. Key patterns to match:
- Font links at the top (no other head elements)
- `<style>` block with theme reset, full-bleed breakout, all `cvrt-` prefixed selectors
- `<div id="cvrt-roadmap">` as the root
- No document wrappers

## Step 3: Save

Save the Shopify version alongside the source file with `-shopify` suffix:
- Source: `clients/rps-water-pumps/april-2026-roadmap.html`
- Output: `clients/rps-water-pumps/april-2026-roadmap-shopify.html`

## Pre-publish checklist

Before saving, verify silently:
- [ ] No `<!DOCTYPE>`, `<html>`, `<head>`, `<body>` tags
- [ ] Google Fonts `<link>` tags are present at the top
- [ ] `#cvrt-roadmap` has full-bleed breakout CSS
- [ ] No `max-width` or `margin: 0 auto` on content containers
- [ ] ALL class names are prefixed with `cvrt-` in both CSS and HTML
- [ ] All CSS selectors use `#cvrt-roadmap .cvrt-*` pattern
- [ ] No `<meta>`, `<title>`, or favicon tags remain
- [ ] File renders the same visual design as the source, just Shopify-safe
