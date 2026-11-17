# Micro-interactions

Every control answers four questions without words: can I touch this, am I touching it, did it work, and what changed. Settle answers them with small, precise responses that are felt more than seen.

## The response ladder

| Moment | Response | Timing |
| --- | --- | --- |
| **Proximity** (pointer near, within ~80px) | A soft light follows the pointer across a card surface; nothing moves | spring `gentle` on the light's position |
| **Hover** | Background tint one step (`surface-raised` to a 3% ink overlay); cursor change | `dur-instant`, no delay |
| **Press** | Scale to 0.97 under the finger; secondary buttons darken their border | spring `snappy`, immediately on pointerdown |
| **Release** | Return to 1 with the `settle` overshoot; the action begins | spring `settle` |
| **Focus** (keyboard) | `focus-ring` appears instantly | none: focus never animates in |
| **Success** | The changed thing confirms itself (a check draws, a value settles); no global celebration | spring `snappy` |
| **Error** | Field border turns `critical`, message appears beneath with an 8px rise; no shaking | spring `gentle` |

## Precise rules

- **Respond on pointerdown, act on pointerup.** The press is felt instantly; the action can still be cancelled by sliding off.
- **Never delay the first response.** Hover and press have zero delay. Only tooltips wait (500ms the first time, instant for neighbours while one is open).
- **Proximity effects are lighting, not movement.** Cards may catch light near the pointer; they do not tilt, follow or magnetise toward it. The effect disappears on touch devices.
- **Drag has weight.** Picked-up items lift one shadow step (`shadow-lift`) and scale to 1.02. Past a boundary, resistance grows with distance (rubber-banding with `Settle.rubber`), so the edge is felt rather than hit. On release, velocity decides: a flick past 500px/s dismisses even if the distance is short.
- **Hit areas exceed visuals.** A 20px icon button has a 40px hit area.
- **States are reversible mid-motion.** Toggling twice quickly must reverse the knob from wherever it is. Springs make this free; never wait for an animation to finish before accepting input.
- **Disabled is still legible.** Disabled controls drop to `ink-subtle` text and lose their shadow; they never fade below 4.5:1, and they explain why on hover or focus.

## Keyboard parity

Everything reachable by pointer is reachable by keyboard: Tab order follows reading order, Space and Enter press buttons (with the same press motion), arrow keys move within segmented controls and lists, Escape closes the top layer and returns focus to the element that opened it.
