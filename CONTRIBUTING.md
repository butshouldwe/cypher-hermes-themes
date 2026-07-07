# Contributing

Thanks for wanting to make the dashboard nicer to live in. 💙

## Reporting a problem or requesting a theme

Open an [issue](https://github.com/butshouldwe/cypher-hermes-themes/issues/new/choose)
— there are templates for a **bug** (a theme reads wrong) and a **theme
request** (a palette you'd love to see).

## Changing a theme

1. **Fork & branch** — `git checkout -b fix/core-contrast`.
2. **Edit the YAML.** Keep the schema intact: `palette`, `typography`,
   `colorOverrides`, `componentStyles`, and the `customCSS` block. The golden
   rule is **legibility** — light themes must resolve the shell's `text-white`
   to dark ink, dark themes to light ink; never ship light-on-light.
3. **Validate locally** — `python3 scripts/validate.py`. CI runs the same check
   on every PR; it must pass.
4. **Open a PR** against `main` with a screenshot of the theme in the dashboard
   (before/after helps). The PR template asks for it.

## Adding a new theme

Copy the closest existing theme, rename `name:` to `cypher-<id>` and `label:`,
retune the palette, and make sure `colorOverrides.cardForeground` contrasts
`colorOverrides.card`. Add a row to the README table. Then PR.

## Style

Keep it warm and legible. These themes exist so the dashboard feels like *yours*
— not to win a contrast-ratio limbo. Ship comfort.
