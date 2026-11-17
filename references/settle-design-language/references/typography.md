# Typography

Two voices and one instrument. The editorial voice (`display`, a refined serif with optical sizes) tells the story. The interface voice (`sans`, a precise grotesque) does the work. The mono family (`mono`) holds figures and code, where alignment is the point.

## Families

- `display`: Newsreader, weights 300 to 400, optical sizing on. Light weights at large sizes; never bold.
- `sans`: Geist, weights 400 to 600. Body at 400, labels at 500, headings at 550.
- `mono`: Geist Mono, 400. Tabular figures by default.

All three load from Google Fonts (see the `@import` at the top of `assets/settle-tokens.css`). Fallbacks are listed in each stack so layout holds before fonts arrive.

## Scale

The interface steps are 12, 13, 14, 15, 17, 22; the editorial steps are 24, 34, 52, 72. The jump between the two sets is deliberate: interface text should never be confused with a statement.

## Rules

- One `display-xl` or `display` per scene. If a screen needs two statements, it is two scenes.
- Line length for `body` is 60 to 72 characters. Set `max-width: 34em` on reading columns.
- Headlines are sentence case and end without a full stop, unless they are a full sentence in an editorial scene, where the full stop is part of the voice.
- Tighten tracking as size grows (the tokens already do this); loosen only `caption`.
- Hierarchy comes from size and weight, then from `ink-muted`. Never from colour.
- Numbers that change (counters, prices, timers) use `numeric` or `font-variant-numeric: tabular-nums` so digits do not jitter while they animate.
- Text never animates letter by letter. A headline may enter as one block (fade plus 8px rise on `settle`); body text simply appears.
