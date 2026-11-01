# Foundations

Values live in `tokens/tokens.json`; this page says what they are for and why. Status: ✅ in both
apps, 🟡 in one app, ⬜ planned.

## Colour ✅

- **Value first.** page → surface → line → muted → ink is a grayscale ramp that works without hue.
  Depth comes from `surface` on `page`, never from shadow.
- **One accent.** Mint is the brand and "act here": the one filled action, the title highlighter,
  the active tab, progress chips, the frame. Roughly 60 neutral / 30 surface / 10 accent: when mint
  covers more than a button and a pill, it stops pointing at anything.
- **Text on mint is `on-mint` or `ink`** (9.7:1 / 12.6:1). White on mint is 1.4:1.
- **Coral is for recording and alerts.** Solid coral only for Stop and the recording dot; alerts and
  destructive actions use `coral-text`, on `coral-soft` when they need a ground.
- **Semantic ≠ brand** (PulseLoop 🟡): `success` green for good / in range / connected, `warning`
  amber, `info` cyan. Mint never means success.
- **Data palette** (PulseLoop 🟡): one hue per metric, a zone scale (low → good → normal →
  borderline → elevated → high → critical) and four sleep stages. Data colours appear only on data.
- **Dark is designed, not inverted.** Dark values are chosen per token (coral lightens to stay
  legible, the panel goes to pure black).

## Type ✅

- Ubuntu Mono, three faces, bundled in `assets/fonts/` with the Ubuntu Font Licence.
- 12sp floor. Each layer has a fixed set of roles; screens use roles, never inline sizes.
- Line height as a ratio in Compose (em) so an inline size change can't leave a gap under the line.
- Tracked caps only for the caption / eyebrow role (+0.5 / +1).

## Space ✅

4-based scale: 4, 8, 12, 16, 24, 32, 40, 48, 64. Gutter 24 (32 from 600dp). Page top 32 under the
header. 40 above a section caption, 12 below, no divider. Proximity groups first; lines only between
rows of one group.

## Shape ✅

4 for controls, 8 for cards (the one card radius), 16 for pills and sheet tops, round for the play
button and thumbs. No shadows (the snackbar's 2dp is the one exception), no gradients.

## The frame ✅

A 4dp mint border round every screen; the signature. uikit 🟡 also uses it as the loading line: one
lap in 1500ms while the screen waits on something the user asked for (white in dark, ink in light),
then a 250ms fade back to mint. Background work never runs the frame.

## Dither 🟡 (PulseLoop)

Where a colour would be tinted down, it is drawn at full strength through a 4×4 Bayer matrix
(`layers.pulseloop.dither`): lighter means fewer dots. One dither cell is 1dp (≥ 2px). Text and icons
on dither get a 1.5dp page-coloured outline so a 12sp label reads at any density. Fairy mode swaps
the dots for smooth washes. ⬜ Decide whether uikit adopts it (divergences D-3).

## Motion ✅ / 🟡

- 150ms for presses, colour changes and small fades; 250ms for screens, sheets and content rising
  in. One curve, quick out and gentle in (`cubic-bezier(0.2, 0, 0, 1)`), no bounce.
- Press: scale to 97% under the finger.
- uikit: a screen's first content fades and rises 8dp, rows staggered 25ms (max 8).
- PulseLoop: rings and bars fill from empty in 900ms (`sweepIn`); screens change through a 750ms
  diagonal dither wipe (divergences D-2).
- With the system's animations off, nothing moves; things appear.

## Iconography ✅

One line set, 22dp, stroke 1.75, tinted `ink` or `muted` (`assets/icons/android/gg_ic_*.xml`).
Monograms `GV_` / `GM_`: an ink square, Ubuntu Mono bold, white letters (`assets/logos/`). Never emoji.
