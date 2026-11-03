# Accessibility

Target: WCAG 2.1 AA in every theme an app ships. These are checked per screen before review.

- **Contrast.** Text ≥ 4.5:1, graphics and boundaries ≥ 3:1. Every pair is listed in
  `tokens.json` `contrast` and checked by `check_tokens.py`. Don't lighten `muted` or `muted-2`.
- **Not colour alone.** A state has a word or an icon as well as a colour.
- **Targets.** 48dp minimum, 8dp apart. Small visuals (the 32dp app switch) sit in a 48dp area.
- **Text scaling.** sp only; buttons, headers and bars use min height, not fixed height, so 200%
  doesn't clip. Rows of chips flow (wrap between chips, never inside one; a chip's word never
  breaks). Two kinds of label may stop growing at **150%** (the label scale cap): a word under an
  icon that carries the same meaning (the tab bar), and a chart's axis ticks (hours, day names),
  whose band widens with them. Everything else, and every spoken label, grows in full. Each app
  keeps a 200% screenshot of its main screens.
- **TalkBack.** Rows announce label + value + state; icon buttons have a description; switch rows
  are one control; charts, rings and gauges have a spoken summary; header status, timers and
  progress chips are live regions.
- **Motion.** "Remove animations" makes everything appear in place, including the frame lap and the
  dither wipe.
- **Back.** System and predictive Back always work; never trapped in a flow.
