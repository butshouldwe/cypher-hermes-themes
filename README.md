# Cypher — Hermes Dashboard Themes

Five Cypher themes for the [Hermes](https://hermes-agent.nousresearch.com)
web dashboard, generated from the Cypher design-system tokens.

| Theme | Mode | Character |
|---|---|---|
| `core` | light | Evidence Workshop — warm paper |
| `teaching` | light | Clearroom — calm, generous |
| `cypher` | dark | Battle Ledger — the scored bout |
| `architect` | dark | Signal Hierarchy — operations glass |
| `hermes` | dark | Messenger — warm gold on ink |

## Install

Drop the YAML files into your Hermes dashboard themes directory and reload:

```bash
./install.sh            # copies *.yaml → ~/.hermes/dashboard-themes/
# or manually:
cp *.yaml ~/.hermes/dashboard-themes/
```

Then reload the dashboard and pick a "Cypher · …" theme from the switcher.
On a remote dashboard, run this on the machine the dashboard runs on.

## Regenerate

These are generated from `themes/<id>/tokens.json` in the Cypher repo by
`scripts/emit-dashboard-themes.mjs` — edit tokens, not the YAML.
