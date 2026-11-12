# Showcase Page Spec (for all agents)

Every style gets ONE self-contained HTML file: `showcase/<style>/index.html`.
Input: `design-md/<style>/DESIGN.md` (read it fully — colors, typography, components, layout, motion, voice).

## Hard rules

1. Single HTML file, all CSS in one `<style>` block, no JS frameworks, no build step.
2. No external asset dependencies that break offline: Google Fonts `<link>` is allowed but you MUST provide a sensible system-font fallback stack. Images: use pure CSS/SVG only (gradients, shapes, inline SVG icons). Never hotlink photos.
3. Use the exact tokens from DESIGN.md (hex colors, radii, spacing, font weights/sizes/letter-spacing) as CSS variables under `:root`.
4. Page copy in English, matching the brand's real product domain (e.g. stripe → payments SaaS, nike → sportswear, cal → scheduling). Do NOT use lorem ipsum.
5. Must look good at 1280px desktop width; basic responsiveness not required but don't break at 900px.

## Required page structure (in this exact order)

```html
<body>
  <header class="sg-banner">
    <!-- Fixed strip at top: left = "<STYLE-FOLDER>" (mono, small) + brand display name (from DESIGN.md);
         right = one-line English description from DESIGN.md. Style this banner in the style's own language. -->
  </header>

  <main>
    <section id="components">  <!-- "Components" — component gallery, one page section -->
      <!-- Required sub-blocks, each with a small label:
           1. Color tokens — swatch grid with hex labels
           2. Typography specimen — display / heading / body / caption lines using the type scale
           3. Buttons — primary, secondary, ghost/text, + one hover-looking state (all sizes if DESIGN.md defines them)
           4. Inputs — text input (default + focus-looking), select, checkbox/switch, one disabled
           5. Cards — one standard content card, one feature/stat card
           6. Badges / tags / pills — 3–4 variants
           7. Navigation — a full navbar/nav example in-style
           8. Table or list row (if the style suits it; skip if truly out of character) -->
    </section>

    <section id="product">  <!-- "Finished Product" — a complete landing page mock -->
      <!-- A believable, polished landing page for this brand/product:
           hero (headline + sub + CTA + visual), logos/social-proof strip, 3 feature cards,
           a stats or pricing section, one testimonial or quote, big CTA band, footer with link columns.
           This is the showpiece — it must feel like the real brand's site, applying motion/voice notes from DESIGN.md where cheap to do (CSS transitions only). -->
    </section>
  </main>
</body>
```

## Quality bar

- This is a design-replication task, not scaffolding: get the *feel* right — the DESIGN.md files are dense with intent (e.g. "thin 300 weight, -1.4px tracking", "pill buttons", "atmospheric gradient mesh upper third"). Apply those notes.
- Avoid generic AI look: no default bootstrap blues, no Tailwind gray, unless the style IS that.
- Keep each file roughly 500–900 lines. Dense but focused.
