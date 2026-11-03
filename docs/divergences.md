# Divergences register

Where the apps still differ. Each item says what differs, why it may be fine, and the proposal.
Nothing here changes an app until the owner decides; a decision is a PR here (with its audit) and
then a sync. Status: ⬜ open, 🟡 decided, being synced, ✅ closed.

| Id | What | uikit | PulseLoop | Proposal | Status |
|---|---|---|---|---|---|
| D-1 | Type scale and role names | 12, 13, 14, 16, 22, 30, 56; `label` = 16 bold, `title` = 22 | 12, 14, 16, 20, 24, 28, 32, 40; `label` = 12, `title` = 16 bold | One core scale and one set of role names. Same name meaning two sizes is the worst part: rename first (e.g. uikit `label` → `row-label`), then converge sizes. | ⬜ |
| D-2 | Screen transition | 250ms fade + 8dp rise | 750ms diagonal dither wipe | Keep both as brand-appropriate per app, or pick one. The wipe is 3× the 150–300ms UI guidance; it's a signature, so it needs a deliberate "yes". | ⬜ |
| D-3 | Tints | flat colour tints (`coral-soft`, `mint` pill) | Bayer dither instead of tints | Decide if the dither is a system-wide brand element; if yes, specify it for Views. | ⬜ |
| D-4 | Themes | light + dark, user choice | dark only | Fine for now; any token PulseLoop adds stays dark-only until it ships light. | ⬜ |
| D-5 | Screen titles | display title, one word on the mint highlighter | tabs have no title (the tab bar names it) | Document both as allowed patterns, or align. | ⬜ |
| D-6 | Row minimum | 56dp | 48dp | Agree on one (48 is the target floor; 56 the comfortable row). | ⬜ |
| D-7 | Semantic colours | none beyond coral (no success/warning/info) | success, warning, info, a full data palette | Move success / warning / info into core with light values when uikit needs them (GHealth will). | ⬜ |
| D-8 | Duplicate sources | NotTheOmiAIApp still has `docs/redesign/design-system/tokens.json` + `scripts/gen_ui_tokens.py`; its README/IMPLEMENTATION say display 34/40, the tokens say 30/36 | PulseColors holds literals; a separate design-system artifact | Point both apps at this repo (docs/consuming.md) and delete the copies: NotTheOmiAIApp#245, PulseLoopAndroid#55. | 🟡 |
| D-9 | Data palette reuse | — | `metric-stress` = `metric-calories` = `zone-elevated` (#FF9A5C); `metric-blood-sugar` = `warning`; `metric-heart-rate` = `coral` | Give each metric its own hue, or document that shared hues never appear on one chart. | ⬜ |
| D-10 | Fairy mode | not built | built (`FairyMode`) | Build it in the kit (docs/fairy-mode.md "Views kit"); decide whether the apps share the flag. | ⬜ |
| D-11 | Self-update | built (GMind updates all five apps; GMoney and GHealth have no network) | built (`update/`), no checksum | Each app updates itself to docs/self-update.md; GMind keeps first installs only. PulseLoop gains the checksum. Owner's call, 2026-11-02. | 🟡 |
| D-12 | Night viewing (Cochilo) | light + dark | dark only | Cochilo is used at night next to a sleeping baby, where bright and blue-green light is what to avoid. Today it follows the system theme and its panel goes dark while the baby sleeps. Open: should the 4dp mint frame dim at night, or a dim red night theme exist? Either touches a brand commitment, so it's the owner's call. Fairy mode isn't carried: its trigger is the profile name, and Cochilo's profile is the baby. | ⬜ Since Cochilo's 0.14.0 night light and the 0.28.0 move, its night theme lives in Cochilo's own layer (docs/products.md). |
