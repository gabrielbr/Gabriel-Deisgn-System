# Syncing the apps

A change is not done when it merges here; it is done when the apps carry it and `drift.py` reports
0 differences. Each app PR follows that app repo's own rules.

## NotTheOmiAIApp (GVoice, GMind, GMoney, GHealth, GDesk)

1. Copy `generated/uikit/UiTokens.java` to `ui-kit/src/main/java/br/gabriel/ui/UiTokens.java`.
2. If a component rule changed, change `Ui.java` (and `UiState`, `Dates`, `Motion`) to match.
3. Run that repo's checks: `python3 scripts/ui_lint.py`, `./gradlew :app:testDebugUnitTest
   :sentient:testDebugUnitTest` (screenshots in both themes).
4. Every merge there releases all four apps, so batch design syncs.

Today that repo still has its own copy of the old sources (`docs/redesign/design-system/tokens.json`,
`scripts/gen_ui_tokens.py`). ⬜ Retire them in favour of this repo: replace the generator with a
note pointing here, so there is one source. Until then, edit here first and keep both equal.

## PulseLoopAndroid

1. Change the matching literal in `ui/theme/PulseColors.kt` / `PulseType.kt` / `Motion.kt` /
   `DitherTransition.kt` / `FairyMode.kt` (names are in each token's `alias.pulseloop`).
2. ⬜ Adoption step, once: copy `generated/pulseloop/GTokens.kt` into `ui/theme/` and make
   `PulseColors` read `GTokens.Colors.*` instead of literals (keeping its FairyMode getters).
   After that, a sync is a file copy.
3. Update the PulseLoop design canvas and design-system artifact (that repo's AGENTS.md, "The
   design files and the app move together").
4. Run `./gradlew :app:testDebugUnitTest` (includes `PulseTypeScaleTest`).

## Check

```sh
python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid
```
