# Product

The context Impeccable (and any designer) needs before touching this system.

## Platform

Android phones first, tablets and landscape supported. `adaptive` is not a goal yet: no iOS app
ships from this system (PulseLoop has an iOS sibling outside it).

## Stack

- NotTheOmiAIApp: Android Views in Java, one shared kit module `ui-kit` (`br.gabriel.ui`):
  `UiTokens` (generated from here), `Ui` components, `UiState`, `Dates`, `Theme`, `Motion`.
- PulseLoopAndroid: Jetpack Compose with Material 3 themed through `PulseColors`, `PulseType`,
  `Motion`, `Dither`, `DitherTransition`.
- Cochilo: Jetpack Compose; `CTokens` generated in Cochilo's own `design/` from this core, its
  layer and the Tatá Slings brand ([docs/products.md](docs/products.md)), read through
  `CochiloTheme`, and a small component kit in `br.gabriel.cochilo.ui.kit`.

## Users

One owner and the people the owner shares the apps with, many of them Brazilian; the UI speaks English
and Brazilian Portuguese. PulseLoop also has public testers with smart rings.

## Product Purpose

- **GVoice** records from an Omi wearable or the phone mic and transcribes on the phone.
- **GMind** keeps conversations, mail, calendar and recordings searchable and answers with sources.
- **GMoney**, **GHealth**: money and health pages over GMind's data. **GDesk**: the desk robot app.
- **PulseLoop**: a smart-ring health app (sleep, heart, activity, coach).
- **Cochilo**: a baby sleep tracker for the owner's family: logs sleep, feeds, pumping, diapers and
  daylight, predicts the next nap from the baby's own history, and keeps every byte on the phone.

## Positioning

Personal, private, calm tools. Nothing leaves the phone that doesn't have to, and the UI says so.

## Operating Context

Glanced at on the move, one-handed, often in the dark (PulseLoop at night; Cochilo at 3am with a
baby in one arm). Impeccable mode:
**Operate** for app screens, **Read** for this repo's docs.

## Brand Commitments

The 4dp mint frame, Ubuntu Mono everywhere, one mint accent with `on-mint` text, the mint
highlighter behind one word of a title, and PulseLoop's Bayer dither. And Fairy mode: when the
profile name is Tatá's (the owner's wife), the brand turns pink; it's a gift, not a setting. These are the brief, not
findings: an audit doesn't propose replacing them.

## Product Principles

1. Content first, chrome second. 2. One action per screen. 3. States, not logs. 4. Privacy is
visible. 5. Readable Portuguese in mono. 6. Reachable by everyone.

## Accessibility & Inclusion

WCAG 2.1 AA: 4.5:1 text and 3:1 graphics in every shipped theme, 48dp targets, sp type that
survives 200% font scale, TalkBack labels on every control, "Remove animations" honoured.
