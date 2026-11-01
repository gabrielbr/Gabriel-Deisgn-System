# Changelog

Semantic versioning (AGENTS.md "Versioning"). Each entry says what changed for each app and what
the app has to do.

## 0.3.0 — 2026-11-01

Fairy mode joins the system: the pink variant PulseLoop shows when the profile name is Tatá's.

- `variants.fairy` in tokens.json: the match rule, five colours that each replace one brand token
  (`fairy-accent` → mint, `fairy-on-accent` → on-mint, `fairy-accent-soft` → mint-soft,
  `fairy-rem` → stage-rem, and new `fairy-action` → snackbar-action), and the celebration's values.
- `check_tokens.py`: a layer that carries any variant colour must carry the replacement of every
  replaced token it has, and every contrast pair is checked again with the variant on.
  CSS gets `[data-variant="fairy"]`.
- docs/fairy-mode.md: who it's for, what changes and what never does, the transformation, the
  lifecycle, and how to build it in Compose (done), the Views kit (to do) and the web.
- AGENTS.md: Fairy mode is part of the system; a new brand token gets its fairy replacement.
- **NotTheOmiAIApp:** copy `generated/uikit/UiTokens.java` (adds `FAIRY_ACCENT`,
  `FAIRY_ON_ACCENT`, `FAIRY_ACTION`; nothing uses them until the kit builds Fairy mode, D-10).
- **PulseLoop:** nothing; `GTokens.kt` is unchanged.

## 0.2.1 — 2026-11-01

Docs only: the app syncs are open (NotTheOmiAIApp#245 retires that repo's own token copy and fixes
the kit; PulseLoopAndroid#55 makes PulseColors read GTokens). docs/consuming.md and D-8 say so.
No app has anything new to do.

## 0.2.0 — 2026-11-01

Fixes the kit's three contrast failures from the 0.1.0 audit, and a fourth found while fixing them.

- **New uikit tokens:** `on-coral` (`#17161A` both themes) for the Stop label and icon, replacing
  white (A-1, 3.6:1 → 5.0:1); `snackbar-action` (`#43F3B7` light, `#0A7A55` dark) for the
  snackbar's action, replacing mint (A-2, 1.3:1 → 4.8:1 in dark).
- **`"pair": true`** on uikit colours that share a light value with an earlier token (`panel`,
  `on-panel`, `on-coral`, `snackbar-action`). The kit looks dark values up by light value, so
  `panel` drew `#F2F2F2` instead of `#000000` in dark and the player's times were 2.1:1 (A-10).
  `check_tokens.py` enforces the mark; the generated comment says how to read the token.
- `coral`'s usage text no longer states the wrong rule; `drift.py` prints a unified diff and
  understands PulseLoop reading `GTokens.Colors.*`; AGENTS.md: agents merge their own PRs here.
- **NotTheOmiAIApp:** copy `generated/uikit/UiTokens.java`; in `Ui.java` read `PANEL`, `ON_PANEL`,
  `ON_CORAL`, `SNACKBAR_ACTION` as pairs, use `ON_CORAL` on Stop, `SNACKBAR_ACTION` on the
  snackbar, and draw the tab badge 12sp coral-text on coral-soft (A-3).
- **PulseLoop:** nothing changes in value; adopt `generated/pulseloop/GTokens.kt` (comment text
  for `coral` changed).

## 0.1.0 — 2026-11-01

First version: captures what both apps ship today. No value changed.

- `tokens/tokens.json` with `core` and the `uikit` and `pulseloop` layers; generators for Java,
  Kotlin, CSS and DESIGN.md; `check_tokens.py`; `drift.py` (both apps: 0 differences).
- Rules (AGENTS.md), DESIGN.md, PRODUCT.md, docs, the divergences register (D-1…D-9).
- Assets: Ubuntu Mono with its licence, `GV_`/`GM_` marks, the `gg_ic_*` icon set.
- Audit skills vendored; first audit `audits/2026-11-01-v0.1.0.md` (open: A-1…A-9).
- **NotTheOmiAIApp:** nothing to do; `generated/uikit/UiTokens.java` equals the app's file.
- **PulseLoop:** nothing to do; `PulseColors` equals the `pulseloop` layer.
