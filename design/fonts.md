---
domain: design, web
part: reference
summary: Free font sources and licence checks
adapt: Section 'Example from a real project' is one site's case; adapt or drop.
---

# Fonts: where to find them and how to check the licence

A plain-markdown copy of the `font-resources` skill, so it can be read without any tool.

## Sources

- **Fontshare** (fontshare.com, Indian Type Foundry): free fonts, commercial use allowed. The licence differs per font:
  - *Closed-source* fonts use ITF's Free Font License: use as they are; do not modify or redistribute.
  - *Open-source* fonts use the SIL Open Font License (OFL): modifying and redistributing are allowed.
  - So "use and modify" is only true for the open-source ones. Read the licence file in the download kit.
- **Tunera:** noted as a source of fonts that can be used and modified. The licence was not verified when this was written (2026-10-18); read it on the font's own page before relying on it.
- Other widely used source with open licences: Google Fonts (mostly OFL). Check each font.

## Before using a font

1. Open the licence file inside the download. Do not trust summaries.
2. Check:
   - commercial use,
   - modifying the outlines,
   - embedding in an app,
   - self-hosting for the web (webfont files),
   - redistributing the font file,
   - whether a modified version must be renamed (OFL "reserved font name").
3. Prefer OFL fonts when the font will be edited, bundled in an app, or kept in a public repository.
4. Keep the licence file next to the font in the project, and credit the source.

## Example from a real project: a static website

- Font: **Literata** (a serif designed for long reading, available under the SIL Open Font License, for example on Google Fonts).
- Self-hosted as two **WOFF2** files: a `latin` file and a `latin-ext` file. The extended file contains the letters needed for Turkish (ğ, ş, ı, İ, ç, ö, ü), and the browser downloads each file only when the page needs those characters.
- The licence file (`OFL.txt`) sits in the same folder as the font files, and the README names the font and licence.
- CSS: one `@font-face` block per file, with a fallback stack (`"Literata", Georgia, "Times New Roman", serif`) so text is readable before the font loads or if it fails.
- The font files are cached for a long time through response headers, because they never change.
- In the iPhone app of the same project no custom font is bundled: it uses the system font, so Dynamic Type (Larger Text) works without extra work.

## Practical tips

- Use at most two families: one for headings, one for text.
- Check that the font has the characters of every language you ship (for example Turkish ğ ş ı İ ç ö ü).
- On the web, serve only the weights you use and prefer WOFF2.
- In iOS apps, bundle the font files and list them under `UIAppFonts`, or use the system font where possible; remember Dynamic Type (text size settings).
