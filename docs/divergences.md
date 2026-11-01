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
