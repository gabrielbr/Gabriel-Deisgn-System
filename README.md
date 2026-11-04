# Gabriel Design System

The single source of truth for the design of every Gabriel app: tokens, rules, components, fonts,
icons and marks. Apps copy from here; they don't define their own.

| App | Repo | Layer |
|---|---|---|
| GVoice, GMind, GMoney, GHealth, GDesk | [NotTheOmiAIApp](https://github.com/gabrielbr/NotTheOmiAIApp) `ui-kit` | `uikit` (Views, light + dark) |
| PulseLoop | [PulseLoopAndroid](https://github.com/gabrielbr/PulseLoopAndroid) | `pulseloop` (Compose, dark) |
| Cochilo | [Cochilo](https://github.com/gabrielbr/Cochilo) | Builds on the core in its own repo (`design/`): its layer and the Tatá Slings brand live there ([docs/products.md](docs/products.md)) |

## What's here

| Path | What |
|---|---|
| [`tokens/tokens.json`](tokens/tokens.json) | Every value: core (shared) + one layer per app |
| [`docs/self-update.md`](docs/self-update.md) | How every app finds, shows and installs its own updates |
| [`docs/products.md`](docs/products.md) | Products, brands and the core: a partner brand and a product's own layer live in the product's repo |
| [`docs/brands.md`](docs/brands.md) | Brands: the rules for dressing an app as a partner's product |
| [`docs/fairy-mode.md`](docs/fairy-mode.md) | Fairy mode: the pink variant for Tatá, and how to build it |
| [`DESIGN.md`](DESIGN.md) | The system on one page (DESIGN.md format; frontmatter generated) |
| [`PRODUCT.md`](PRODUCT.md) | Who the apps are for, and the brand commitments |
| [`docs/`](docs/) | Foundations, components, content, accessibility, tokens, syncing, divergences, audit process |
| [`generated/`](generated/) | `UiTokens.java` (uikit), `GTokens.kt` (PulseLoop), CSS variables |
| [`assets/`](assets/) | Ubuntu Mono + licence, the `GV_`/`GM_` marks, line icons |
| [`audits/`](audits/) | One audit per change (ux-user-flows + graphic-design-fundamentals + impeccable + less-is-more) |
| [`scripts/`](scripts/) | `gen_tokens.py`, `check_tokens.py`, `drift.py` |
| [`.claude/skills/`](.claude/skills/) | The four design skills, vendored; every app built on this system copies them ([products.md](docs/products.md#the-four-design-skills)) |
| [`AGENTS.md`](AGENTS.md) | The rules for changing anything here |

## Use

```sh
python3 scripts/gen_tokens.py      # after editing tokens/tokens.json
python3 scripts/check_tokens.py    # contrast, scale, coverage, versions, generated files
python3 scripts/drift.py --notheomi ../NotTheOmiAIApp --pulseloop ../PulseLoopAndroid
python3 -m unittest discover -s tests
```

Python 3.8+, no dependencies.
