# Motion

Motion in Settle is physics, not choreography by stopwatch. Every moving thing is a spring with stiffness, damping and mass. Springs keep their velocity when interrupted, so a toggle flicked back halfway turns around smoothly instead of restarting. That one property is most of what makes an interface feel natural.

## The four springs

| Preset | Stiffness | Damping | Mass | Damping ratio | Overshoot | Settles in | Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `snappy` | 520 | 34 | 1 | 0.75 | 3% | ~340ms | Parts under the finger: toggles, press release, segmented indicator, checkmarks |
| `settle` | 300 | 22 | 1 | 0.64 | 7% | ~570ms | The signature landing: toasts, popovers, cards arriving, a value snapping into place |
| `gentle` | 220 | 24 | 1 | 0.81 | 1% | ~540ms | Size and layout: disclosure height, list reflow, panels resizing |
| `heavy` | 160 | 26 | 1.6 | 0.81 | 1% | ~800ms | Large surfaces: sheets, scene changes, shared-element transitions |

In JavaScript: `Settle.spring({ from: 0, preset: 'settle', onUpdate: fn }).to(1)`. In CSS: `transition: transform var(--dur-settle) var(--ease-spring-settle)`. The `linear()` curves in the easing tokens are sampled from the same springs, so CSS and JS motion match.

## Rules of weight

- **Size sets the spring.** The bigger the thing, the heavier the preset. A full-screen sheet never uses `snappy`; a checkbox never uses `heavy`.
- **Overshoot means arrival.** Use `settle` when something lands in a resting place. Never overshoot on exit, on opacity or on colour.
- **Damping ratio stays at or above 0.6.** Below that, motion reads as bounce. One visible oscillation at most.
- **Exits are faster than entrances.** Leaving uses `ease-exit` over `dur-quick`, or a stiffer spring. Attention moves on; the thing that left should not hold it.
- **Gestures hand over velocity.** When a drag ends, pass the release velocity into the spring (`spring.to(target, velocity)`). The motion continues the person's movement rather than starting a new one.

## Choreography

- **Lead with the cause.** The element the person touched moves first; consequences follow 30 to 60ms later. A list reorders after the dragged item lands, not with it.
- **Stagger sparingly.** At most 5 items, 30ms apart. Past that, move the group as one block.
- **Move along the relationship.** A popover grows from its trigger (`transform-origin` at the trigger). A sheet rises from the edge it belongs to. A detail view grows out of the card it came from.
- **Small distances.** Entrances travel 8 to 16px, not across the screen. Opacity carries the rest.
- **Pause on purpose.** After a scene lands, hold stillness for at least 400ms before anything else moves on its own. Ambient motion (pulses, idle loops) is limited to one `signal` indicator showing live state.

## Reduced motion

With `prefers-reduced-motion: reduce`, spatial motion (translate, scale, size) resolves instantly. Opacity and colour still fade over `dur-quick`, so state changes remain perceptible. `Settle.reduced()` reports the setting; `Settle.spring` honours it automatically.

## Do and don't

| Do | Don't |
| --- | --- |
| Scale a pressed button to 0.97 | Scale it to 0.9 or rotate it |
| Slide the segmented indicator to its new option | Fade the old one out and the new one in |
| Grow a popover from its trigger | Fade it in from the centre of the screen |
| Let a toggle knob overshoot by about a pixel | Let it bounce three times |
| Animate `transform` and `opacity` | Animate `width`, `top` or `box-shadow` every frame on large elements |
