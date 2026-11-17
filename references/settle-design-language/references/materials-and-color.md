# Materials and colour

Settle imagines its interface as a few honest materials: warm paper for the ground, a slightly brighter card stock for objects, a pressed well for tracks, graphite for the one thing that matters most, and a single thread of deep cobalt (`signal`) for attention. The palette is almost entirely neutral so that the few colours that appear carry meaning.

## Surfaces are depth, not decoration

| Token | Depth | Use |
| --- | --- | --- |
| `surface-sunken` | −1 | Tracks, rails, wells, code blocks, input backgrounds inside cards |
| `surface` | 0 | The page |
| `surface-raised` | +1 | Cards, controls, the toggle knob |
| `surface-overlay` | +2 | Sheets, menus, popovers, toasts |

- Change depth by one step at a time. A raised card holds sunken wells, not a second raised card.
- Pair each depth with its shadow: `shadow-rest` at +1, `shadow-lift` when picked up or hovered, `shadow-float` at +2, `shadow-sheet` for sheets and dialogs.
- In the dark theme surfaces get lighter as they rise (`surface-overlay` is the lightest), because light still comes from above. Shadows there are mostly a hairline highlight plus deep ambient black.

## Edges

- `hairline` separates content (list dividers, section rules). It is decorative and may be faint.
- `line` outlines a card or sheet when shadow alone does not hold the edge, for example cards on `surface-sunken`.
- `line-control` identifies something you can operate: field borders, unchecked boxes, secondary buttons. It holds 3:1 against every surface. Never substitute `hairline` for it.

## The three colour roles

1. **Graphite** (`fill-primary` / `on-fill-primary`): the primary action and the on state of a toggle. It is the ink itself, so the most important control looks like the most important text.
2. **Signal** (`signal`, `signal-soft`, `on-signal`, `focus-ring`): focus, live, recording, syncing, the current step of a flow, the playhead of a timeline. Use it in one place per view.
3. **Status** (`positive`, `caution`, `critical` and their `-soft` pairs): outcomes. Always pair with a word or a glyph; colour alone never carries status.

## Rules

- Never tint large areas with `signal` or status colours. The largest coloured area on a screen is the primary button.
- Selected and active states use `stone` (a material tint), not colour. Text on `stone` is `ink` or `ink-muted`.
- Images and illustrations sit on `surface-sunken` with `radius-lg`, so they read as set into the page.
- The scrim (`scrim`) fades in with its layer, using the layer's spring, never ahead of it.

## Contrast, verified

All text tokens reach 4.5:1 on all four surfaces in both themes. `signal` reaches 5.1:1 on every light surface and 6.8:1 on every dark surface, so it may set text. `line-control` reaches 3.3:1 at its lowest (light theme, on `surface-sunken`). `on-fill-primary` on `fill-primary` is 15:1.
