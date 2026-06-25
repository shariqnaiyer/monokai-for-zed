# Monokai for Zed

The complete Monokai family as a single [Zed](https://zed.dev) theme extension —
all ten variants in one place, including both light filters.

| Theme | Background | Appearance |
| --- | --- | --- |
| Monokai | `#272822` | dark |
| Monokai Classic | `#272822` | dark |
| Monokai Dimmed | `#1e1e1e` | dark |
| Monokai Pro | `#2d2a2e` | dark |
| Monokai Pro (Filter Machine) | `#273136` | dark |
| Monokai Pro (Filter Octagon) | `#282a3a` | dark |
| Monokai Pro (Filter Ristretto) | `#2c2525` | dark |
| Monokai Pro (Filter Spectrum) | `#222222` | dark |
| Monokai Pro Light | `#faf4f2` | light |
| Monokai Pro Light (Filter Sun) | `#f8efe7` | light |

Each theme defines the full Zed surface — editor, syntax, terminal ANSI palette,
git/diagnostic states, scrollbars, indent guides and collaboration cursors — with
the classic Monokai token mapping (pink keywords, yellow strings, green functions,
italic cyan types, italic orange parameters).

## Install

### From the Zed extension registry

Open the command palette (`cmd/ctrl-shift-p`) → **zed: extensions** → search for
**Monokai** → install. Then pick a theme via the theme selector
(`cmd/ctrl-k cmd/ctrl-t`).

### As a local dev extension

1. Clone this repo.
2. Command palette → **zed: install dev extension** → select this folder.
3. Pick a theme via the theme selector (`cmd/ctrl-k cmd/ctrl-t`).

## Editing the colors

All ten themes are generated from a single palette table so the hundreds of
surface keys stay consistent. To tweak anything, edit the `PALETTES` dict in
[`gen_theme.py`](gen_theme.py) and regenerate:

```bash
python gen_theme.py
```

This rewrites [`themes/monokai.json`](themes/monokai.json).

## Color accuracy

The dark Pro filters and both light filters use the exact palettes published in
Monokai's official VS Code theme. "Monokai" and "Monokai Dimmed" mirror the
classic Sublime Text and VS Code built-ins respectively.

## License

[MIT](LICENSE). This is an independent, community theme — not affiliated with or
endorsed by Monokai. "Monokai" and "Monokai Pro" are names of their respective
owner; only color values (which are not copyrightable) and original
configuration are included here.
