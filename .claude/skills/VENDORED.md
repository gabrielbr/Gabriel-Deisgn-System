# Vendored skills

The four design skills live here so every Claude Code session opened in this repo loads them,
whatever account or machine it runs on. AGENTS.md requires all four on every change here, and on
every screen and flow of every app built on this system. The apps copy this folder (see
`docs/products.md`, "The four design skills").

| Skill | Source | Version | Licence |
|---|---|---|---|
| `ux-user-flows/` | The owner's own claude.ai skill, copied 2026-11-04 | — | The owner's |
| `impeccable/` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable), `plugin/skills/impeccable` at commit `d41d9860b0094dcb68030657da63461212835aaa` | skill 4.9.2, launcher 0.1.25 | Apache-2.0 (`impeccable/LICENSE`, `impeccable/NOTICE.md`) |
| `graphic-design-fundamentals/` | The owner's own claude.ai skill, copied 2026-11-01 | — | The owner's |
| `less-is-more/` | Written here (0.29.0), from Cochilo's 0.43.0 audit; sources linked in `SKILL.md` | 1.0 | The owner's |

Notes

- Impeccable's `scripts/impeccable` launcher downloads its engine binary from the project's GitHub
  releases on first run and checks it against `scripts/engine-checksums.txt`. Where a session
  refuses to run it, read `SKILL.md` and `reference/*.md` directly (the skill says the same).
  This system is native Android, so audits use `reference/audit.native.md` and
  `reference/android.md`; `detect` (a web scanner) does not apply to Compose or Views code.
- **Impeccable is kept at its latest release** (the owner's rule, 2026-11-16). A session that sees
  Impeccable report a newer version (its `UPDATE_AVAILABLE` line) updates it here in a patch PR,
  then re-copies it to every app, the same day. Don't run `npx impeccable update` inside an app:
  the apps' copies come from here.
- To update Impeccable: copy `plugin/skills/impeccable` from the newest upstream commit over this
  folder (delete the old files first, so removed references go too), keep `LICENSE` and
  `NOTICE.md`, update the table above, check `scripts/impeccable context` runs, and record it in
  CHANGELOG.md (patch).
- `graphic-design-fundamentals` is edited on claude.ai. When it changes there, copy the new
  `SKILL.md` here in a patch PR so the repo's copy doesn't lag.
- `ux-user-flows` is edited on claude.ai too, the same way: when it changes there, copy the new
  `SKILL.md` here in a patch PR, and the apps re-copy it.
- `less-is-more` is kept here. The owner can also upload it to claude.ai (Settings ›
  Capabilities › Skills) so projects outside these repos can use it. When it changes, edit it here
  first, then upload the new copy.
