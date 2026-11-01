# Syncing the apps

A change is not done when it merges here; it is done when the apps carry it and `drift.py` reports
0 differences. Each app PR follows that app repo's own rules.

## NotTheOmiAIApp (GVoice, GMind, GMoney, GHealth, GDesk)

1. Copy `generated/uikit/UiTokens.java` to `ui-kit/src/main/java/br/gabriel/ui/UiTokens.java`.
2. If a component rule changed, change `Ui.java` (and `UiState`, `Dates`, `Motion`) to match.
3. Run that repo's checks: `python3 scripts/ui_lint.py`, `./gradlew :app:testDebugUnitTest
   :sentient:testDebugUnitTest` (screenshots in both themes).
4. Every merge there releases all four apps, so batch design syncs.

🟡 Its own old sources (`docs/redesign/design-system/tokens.json`, `scripts/gen_ui_tokens.py`) are
retired in NotTheOmiAIApp#245, which adds `scripts/sync_design_system.py`: it copies
`generated/uikit/UiTokens.java` in and checks the widget's hand-copied colours. Step 1 becomes
`python3 scripts/sync_design_system.py` (with this repo cloned next to it).

## PulseLoopAndroid

1. Change the matching literal in `ui/theme/PulseColors.kt` / `PulseType.kt` / `Motion.kt` /
   `DitherTransition.kt` / `FairyMode.kt` (names are in each token's `alias.pulseloop`).
2. 🟡 Adoption (PulseLoopAndroid#55): `PulseColors` and `FairyMode.Palette` read
   `GTokens.Colors.*` instead of literals. Once it merges, a colour sync is copying
   `generated/pulseloop/GTokens.kt` into `ui/theme/`.
3. Update the PulseLoop design canvas and design-system artifact (that repo's AGENTS.md, "The
   design files and the app move together").
4. Run `./gradlew :app:testDebugUnitTest` (includes `PulseTypeScaleTest`).

## Check

```sh
python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid
```
