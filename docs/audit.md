# Auditing a change

Every change to this repo is audited with **ux-user-flows**, **graphic-design-fundamentals**,
**impeccable** and **less-is-more** before merge (AGENTS.md). Every app built on this system runs
the same four on every screen and flow (AGENTS.md, "Every app built on this boilerplate uses the
four skills"). The audit is a file in `audits/`, made from `audits/TEMPLATE.md`, linked in the PR.

## Steps

1. **Scope.** List what changed: tokens (with old → new values), rules, components, assets.
2. **ux-user-flows §13.** If the change touches a flow (what a component does in each state, what
   happens when, navigation, copy that tells someone what to do), write the flow and answer the 15
   flow review questions in `.claude/skills/ux-user-flows/SKILL.md`. Issues by severity (critical /
   important / polish), each with the principle and the fix. If no flow changes, say so in a line.
3. **graphic-design-fundamentals §13.** Answer each of the 13 checklist questions for the change.
   Report issues by severity (critical / important / polish), each with the principle it breaks
   and a concrete fix.
4. **impeccable `audit` (native).** Follow `.claude/skills/impeccable/reference/audit.native.md`,
   scored against `reference/android.md`: Accessibility, Performance, Appearance & theming,
   Platform conformance, Adaptivity, 0–4 each, findings P0–P3. For a visual change also run
   `critique`. The brand commitments in PRODUCT.md are the brief, not findings.
5. **less-is-more.** For every element the change adds or touches, answer the five questions in
   `.claude/skills/less-is-more/SKILL.md`. List what was removed, moved or merged and why, then
   score it. A change that adds a tap to a common action fails.
6. **Evidence.** Paste `check_tokens.py` and `drift.py` output. For colour changes, the contrast
   ratios. For visual changes, screenshots from the apps in each theme they ship.
7. **Verdict.** Merge only with no new critical / P0 / P1. Pre-existing findings get an id
   (`A-n`), a "known" contrast entry where it is a colour pair, and a line in the audit's open list.

## When a skill won't load

Read the skill's `SKILL.md` and references from `.claude/skills/` and apply them by hand. Say in
the audit which skill ran by hand and why.
