# Gabriel Design System

The single source of truth for the design of every Gabriel app: tokens, rules, components, fonts,
icons and marks. Apps copy from here; they don't define their own.

| App | Repo | Layer |
|---|---|---|
| GVoice, GMind, GMoney, GHealth, GDesk | [NotTheOmiAIApp](https://github.com/gabrielbr/NotTheOmiAIApp) `ui-kit` | `uikit` (Views, light + dark) |
| PulseLoop | [PulseLoopAndroid](https://github.com/gabrielbr/PulseLoopAndroid) | `pulseloop` (Compose, dark) |

## What's here

| Path | What |
|---|---|
| [`tokens/tokens.json`](tokens/tokens.json) | Every value: core (shared) + one layer per app |
| [`DESIGN.md`](DESIGN.md) | The system on one page (DESIGN.md format; frontmatter generated) |
| [`PRODUCT.md`](PRODUCT.md) | Who the apps are for, and the brand commitments |
| [`docs/`](docs/) | Foundations, components, content, accessibility, tokens, syncing, divergences, audit process |
| [`generated/`](generated/) | `UiTokens.java` (uikit), `GTokens.kt` (PulseLoop), CSS variables |
| [`assets/`](assets/) | Ubuntu Mono + licence, `GV_`/`GM_` marks, line icons |
| [`audits/`](audits/) | One audit per change (graphic-design-fundamentals + impeccable) |
| [`scripts/`](scripts/) | `gen_tokens.py`, `check_tokens.py`, `drift.py` |
| [`.claude/skills/`](.claude/skills/) | The two audit skills, vendored |
| [`AGENTS.md`](AGENTS.md) | The rules for changing anything here |

## Use

```sh
python3 scripts/gen_tokens.py      # after editing tokens/tokens.json
python3 scripts/check_tokens.py    # contrast, scale, coverage, versions, generated files
python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid
python3 -m unittest discover -s tests
```

Python 3.8+, no dependencies.
