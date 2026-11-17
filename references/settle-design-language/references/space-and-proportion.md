# Space and proportion

Negative space is the primary material. It is what makes a minimal interface feel generous instead of empty.

## The grid

- Base unit 4px; the working steps are `space-2` (8), `space-4` (16), `space-5` (24), `space-6` (32), `space-7` (48).
- Desktop layout: 12 columns, 24px gutters, `space-8` (64px) page margins, content capped at 1200px. Reading columns are 8 columns or 34em, whichever is narrower.
- Tablet: 8 columns, `space-6` margins. Phone: 4 columns, `space-5` margins.
- Align everything to a shared left edge within a scene. Alignment is the cheapest form of clarity: if two things line up, the eye assumes they belong together.

## Proportion

- Controls share one height system: 32px (compact), 40px (default), 48px (touch and primary flows). Hit areas are never smaller than 40 × 40px, even when the visible control is smaller.
- Padding inside a control is about 40% of its height horizontally (16px on a 40px button).
- Corner radius grows with the object: nested radii follow `outer = inner + padding`. A 12px button inside a card with 8px padding sits in a 20px card (`radius-lg`).
- Icons are 20px in 40px controls and 16px in 32px controls, optically centred.

## Rhythm of space

| Relationship | Gap |
| --- | --- |
| Label to its field, icon to its label | `space-1` to `space-2` |
| Items in a group | `space-3` to `space-4` |
| Groups in a panel | `space-5` to `space-6` |
| Sections in a page | `space-7` to `space-8` |
| Chapters in a story | `space-9` to `space-10` |

Doubling the gap is how Settle says "this is a new thought". Use space instead of a divider wherever possible; add a `hairline` only when space alone is ambiguous.
