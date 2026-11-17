# Iconography

Icons are drawn, not decorated: single-weight strokes on a 24px grid, the same family as the type.

- **Grid:** 24 × 24 viewBox, 2px safe padding, key shapes on whole pixels.
- **Stroke:** 1.5px, round caps, round joins, no fills except for small solid dots (status, live).
- **Colour:** `currentColor` when inline, so icons take `ink`, `ink-muted` or `signal` from their text. As `<img>`, the files in `assets/icons` are drawn in `ink` light (#1b1b19); inline the SVG to recolour.
- **Size:** 20px in 40px controls, 16px in 32px controls and inline with `body-small`.
- **Pairing:** an icon beside a label sits `space-2` away, optically centred on the label's x-height.
- **Motion:** icons swap with a crossfade plus 0.9 to 1 scale on `snappy`. A check may draw its stroke (stroke-dashoffset) on `snappy` to confirm success. Icons never spin except the single progress indicator.
- **Never** use emoji as icons, and never mix filled and outline families in one view.

The starter set in `assets/icons` (check, close, chevron, plus, arrow, dot) covers the components here. Extend it following the grid above; if a third-party set is needed, choose one drawn at 1.5px with round caps and note it here.
