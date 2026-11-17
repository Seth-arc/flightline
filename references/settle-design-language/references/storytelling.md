# Storytelling and editorial metaphor

Settle explains ideas visually, the way a good magazine spread does: one image, one idea, an unmistakable relationship. Three metaphors form the vocabulary. Use one per scene.

## The three metaphors

**Layers reveal complexity.** A simple surface sits on top; detail lives beneath it and is revealed by lifting, peeling or expanding. Use it for drill-down, progressive disclosure, notification stacks and "how it works" explanations. In motion: the top layer lifts (`shadow-lift`, 8 to 16px), the layers beneath fan out with a 30ms stagger, and they settle back when attention leaves.

**Alignment creates clarity.** Scattered elements move onto a shared line or grid, and the pattern becomes visible. Use it for sorting, filtering, comparison and before/after stories. In motion: items travel to their aligned positions on `gentle`, then a single `hairline` draws along the shared edge.

**Separate parts come together.** Distinct elements converge into one whole to show connection, integration or synthesis. Use it for onboarding, combining data sources, team or partner stories. In motion: parts approach on `heavy`, the gaps between them close to `space-1`, then the outer edge becomes one shape with one radius.

## Keeping a metaphor legible

- Two to five elements. If a metaphor needs more, it is a diagram, not a metaphor.
- Use real interface materials (surfaces, hairlines, radii) instead of illustration. The story is told with the same parts as the product.
- Name the idea in words as well: a `headline` or `pull-quote` beside the motion. The motion confirms the sentence; it never replaces it.
- The metaphor resolves to a still frame that is meaningful on its own. A screenshot of the end state should still tell the story.

## Rhythm: motion and stillness

A story page alternates two beats: **transition** (something changes, under 800ms) and **stillness** (nothing moves while the person reads, as long as they need). Never chain transitions without a still beat between them. Scroll-driven scenes advance one transition per scene and hold the end state across at least `space-9` of scroll before the next begins.

## Continuity between scenes

- **Persisting elements travel.** If an element exists in both the outgoing and incoming scene (a card becoming a detail view, a chart becoming a full-screen chart), it moves and resizes into place (a shared-element transition on `heavy`) while everything else fades.
- **Direction means hierarchy.** Going deeper moves content up or inward; going back reverses exactly. Sideways movement means siblings.
- **The camera does not move.** Scenes change by objects moving, never by the whole viewport panning, zooming or rotating.
- **Exits clear the stage first.** Outgoing content fades over `dur-quick` before incoming content settles, so two scenes never compete for attention.
