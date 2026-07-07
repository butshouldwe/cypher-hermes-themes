# Cypher for Hermes

**Five design-system themes for the [Hermes](https://hermes-agent.nousresearch.com) web dashboard.**
One operations room, five worlds — flip one attribute and the whole room changes voice.

> [!TIP]
> See them live and re-skin a dashboard with one click →
> **[butshouldwe.com/themes](https://butshouldwe.com/themes)**

[![Validate themes](https://github.com/butshouldwe/cypher-hermes-themes/actions/workflows/validate.yml/badge.svg)](https://github.com/butshouldwe/cypher-hermes-themes/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-2352c8.svg)](./LICENSE)
[![Themes: 5](https://img.shields.io/badge/themes-5-2352c8.svg)](#the-themes)

---

## The themes

| Theme | Mode | Character | Accent |
|---|---|---|---|
| **core** | ☀︎ light | Evidence Workshop — warm paper | blue |
| **teaching** | ☀︎ light | Clearroom — calm, generous | green |
| **cypher** | ☾ dark | Battle Ledger — the scored bout | teal |
| **architect** | ☾ dark | Signal Hierarchy — operations glass | periwinkle |
| **hermes** | ☾ dark | Messenger — warm gold on ink | gold |

Each theme carries a full palette, legible 17px base type, a sized sidebar,
heading hierarchy, and wrapping kanban — tuned so both light and dark read
cleanly, never light-on-light.

## Install

Hermes themes are drop-in files. Clone this repo and copy them in:

```bash
git clone https://github.com/butshouldwe/cypher-hermes-themes
cd cypher-hermes-themes
./install.sh            # copies *.yaml → ~/.hermes/dashboard-themes/
```

Or by hand:

```bash
cp *.yaml ~/.hermes/dashboard-themes/
```

Then **reload the dashboard** and pick a **“Cypher · …”** theme from the
switcher. On a remote dashboard, run this on the machine the dashboard runs on
(`HERMES_HOME` is honored if your `.hermes` lives elsewhere).

## How it works

Each `.yaml` follows the Hermes dashboard theme schema — a `palette`,
`typography`, `colorOverrides`, `componentStyles`, and a `customCSS` block that
maps the shell's Tailwind classes to the theme's ink so nothing renders
invisible. See the [Hermes theming docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/extending-the-dashboard).

## Customizing

These are generated from the **Cypher design system** token pipeline — the
source of truth is `themes/<id>/tokens.json` in the Cypher repo, emitted by
`scripts/emit-dashboard-themes.mjs`. To tweak a color, edit the token and
regenerate; hand-edits to the YAML will be overwritten. To spin your own theme,
copy the closest one and adjust — then open a PR (see
[CONTRIBUTING](./CONTRIBUTING.md)).

## License

[MIT](./LICENSE) — use them, fork them, ship them.

<sub>Cypher, by [butshouldwe?](https://butshouldwe.com) · evidence beats vibes</sub>
