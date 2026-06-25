import json
import os

# ---------------------------------------------------------------------------
# Palettes for every Monokai filter. All values verified against the official
# "monokai.theme-monokai-pro-vscode" 2.0.13 theme files, except "Monokai" and
# "Monokai Dimmed" which mirror the classic Sublime / VS Code built-ins.
#
#   bg      editor background (the lightest dark / the page on light themes)
#   chrome  sidebar / tabs / panels (darker than bg on dark themes)
#   hl      solid selection / active-element highlight
#   border  pane + element borders
#   ln      gutter line numbers
#   comment muted text & comments
#   fg2     punctuation / slightly-muted text (also the neutral selection grey)
#   fg      foreground
#   red orange yellow green cyan purple : the six accents
# ---------------------------------------------------------------------------
PALETTES = {
    "Monokai": {  # classic Sublime Monokai
        "appearance": "dark",
        "bg": "#272822", "chrome": "#1e1f1c", "hl": "#3e3d32", "border": "#414339",
        "ln": "#90908a", "comment": "#75715e", "fg2": "#c7c7bb", "fg": "#f8f8f2",
        "red": "#f92672", "orange": "#fd971f", "yellow": "#e6db74",
        "green": "#a6e22e", "cyan": "#66d9ef", "purple": "#ae81ff",
    },
    "Monokai Classic": {
        "appearance": "dark",
        "bg": "#272822", "chrome": "#1d1e19", "hl": "#3e3d32", "border": "#34352f",
        "ln": "#57584f", "comment": "#6e7066", "fg2": "#c0c1b5", "fg": "#fdfff1",
        "red": "#f92672", "orange": "#fd971f", "yellow": "#e6db74",
        "green": "#a6e22e", "cyan": "#66d9ef", "purple": "#ae81ff",
    },
    "Monokai Dimmed": {  # VS Code "Monokai Dimmed" built-in
        "appearance": "dark",
        "bg": "#1e1e1e", "chrome": "#181818", "hl": "#37373d", "border": "#2a2a2a",
        "ln": "#6a6a6a", "comment": "#9a9a9a", "fg2": "#aeaeae", "fg": "#c5c8c6",
        "red": "#d08442", "orange": "#d08442", "yellow": "#cfaf5e",
        "green": "#b9ca4a", "cyan": "#6089b4", "purple": "#9872a2",
    },
    "Monokai Pro": {
        "appearance": "dark",
        "bg": "#2d2a2e", "chrome": "#221f22", "hl": "#403e41", "border": "#3a373b",
        "ln": "#5b595c", "comment": "#727072", "fg2": "#c1c0c0", "fg": "#fcfcfa",
        "red": "#ff6188", "orange": "#fc9867", "yellow": "#ffd866",
        "green": "#a9dc76", "cyan": "#78dce8", "purple": "#ab9df2",
    },
    "Monokai Pro (Filter Machine)": {
        "appearance": "dark",
        "bg": "#273136", "chrome": "#1d2528", "hl": "#3a4449", "border": "#323b3f",
        "ln": "#545f62", "comment": "#6b7678", "fg2": "#b8c4c3", "fg": "#f2fffc",
        "red": "#ff6d7e", "orange": "#ffb270", "yellow": "#ffed72",
        "green": "#a2e57b", "cyan": "#7cd5f1", "purple": "#baa0f8",
    },
    "Monokai Pro (Filter Octagon)": {
        "appearance": "dark",
        "bg": "#282a3a", "chrome": "#1e1f2b", "hl": "#3a3d4b", "border": "#363845",
        "ln": "#535763", "comment": "#696d77", "fg2": "#b2b9bd", "fg": "#eaf2f1",
        "red": "#ff657a", "orange": "#ff9b5e", "yellow": "#ffd76d",
        "green": "#bad761", "cyan": "#9cd1bb", "purple": "#c39ac9",
    },
    "Monokai Pro (Filter Ristretto)": {
        "appearance": "dark",
        "bg": "#2c2525", "chrome": "#211c1c", "hl": "#403838", "border": "#392f2f",
        "ln": "#5b5353", "comment": "#72696a", "fg2": "#c3b7b8", "fg": "#fff1f3",
        "red": "#fd6883", "orange": "#f38d70", "yellow": "#f9cc6c",
        "green": "#adda78", "cyan": "#85dacc", "purple": "#a8a9eb",
    },
    "Monokai Pro (Filter Spectrum)": {
        "appearance": "dark",
        "bg": "#222222", "chrome": "#191919", "hl": "#363537", "border": "#2f2e30",
        "ln": "#525053", "comment": "#69676c", "fg2": "#bab6c0", "fg": "#f7f1ff",
        "red": "#fc618d", "orange": "#fd9353", "yellow": "#fce566",
        "green": "#7bd88f", "cyan": "#5ad4e6", "purple": "#948ae3",
    },
    "Monokai Pro Light": {
        "appearance": "light",
        "bg": "#faf4f2", "chrome": "#ede7e5", "hl": "#d3cdcc", "border": "#e0dad9",
        "ln": "#bfb9ba", "comment": "#a59fa0", "fg2": "#706b6e", "fg": "#29242a",
        "red": "#e14775", "orange": "#e16032", "yellow": "#cc7a0a",
        "green": "#269d69", "cyan": "#1c8ca8", "purple": "#7058be",
    },
    "Monokai Pro Light (Filter Sun)": {
        "appearance": "light",
        "bg": "#f8efe7", "chrome": "#eee5de", "hl": "#ded5d0", "border": "#ded5d0",
        "ln": "#beb5b3", "comment": "#a59c9c", "fg2": "#72696d", "fg": "#2c232e",
        "red": "#ce4770", "orange": "#d4572b", "yellow": "#b16803",
        "green": "#218871", "cyan": "#2473b6", "purple": "#6851a2",
    },
}

def aa(hex_color, alpha):
    """Append an 8-bit alpha (0-255) to a #rrggbb color."""
    return hex_color + format(int(alpha), "02x")

def syntax(p):
    def s(color, **extra):
        d = {"color": color}; d.update(extra); return d
    return {
        "attribute": s(p["green"]),
        "boolean": s(p["purple"]),
        "comment": s(p["comment"], font_style="italic"),
        "comment.doc": s(p["comment"], font_style="italic"),
        "constant": s(p["purple"]),
        "constructor": s(p["cyan"]),
        "embedded": s(p["fg"]),
        "emphasis": s(p["red"], font_style="italic"),
        "emphasis.strong": s(p["orange"], font_weight=700),
        "enum": s(p["cyan"]),
        "function": s(p["green"]),
        "function.method": s(p["green"]),
        "function.builtin": s(p["green"]),
        "hint": s(p["comment"]),
        "keyword": s(p["red"]),
        "label": s(p["cyan"]),
        "link_text": s(p["yellow"], font_style="italic"),
        "link_uri": s(p["purple"]),
        "number": s(p["purple"]),
        "operator": s(p["red"]),
        "predictive": s(p["comment"], font_style="italic"),
        "preproc": s(p["fg"]),
        "primary": s(p["fg"]),
        "property": s(p["fg"]),
        "punctuation": s(p["fg2"]),
        "punctuation.bracket": s(p["fg2"]),
        "punctuation.delimiter": s(p["fg2"]),
        "punctuation.list_marker": s(p["red"]),
        "punctuation.special": s(p["red"]),
        "string": s(p["yellow"]),
        "string.escape": s(p["purple"]),
        "string.regex": s(p["orange"]),
        "string.special": s(p["purple"]),
        "string.special.symbol": s(p["yellow"]),
        "tag": s(p["red"]),
        "text.literal": s(p["yellow"]),
        "title": s(p["green"], font_weight=700),
        "type": s(p["cyan"], font_style="italic"),
        "type.builtin": s(p["cyan"], font_style="italic"),
        "variable": s(p["fg"]),
        "variable.special": s(p["orange"], font_style="italic"),
        "variant": s(p["cyan"]),
    }

def players(p):
    me = {"cursor": p["fg"], "background": p["cyan"], "selection": aa(p["fg2"], 0x40)}
    out = [me]
    for c in [p["green"], p["purple"], p["orange"], p["red"], p["yellow"], p["cyan"]]:
        out.append({"cursor": c, "background": c, "selection": aa(c, 0x3d)})
    return out

def style(p):
    bg, chrome, hl, border = p["bg"], p["chrome"], p["hl"], p["border"]
    ln, comment, fg2, fg = p["ln"], p["comment"], p["fg2"], p["fg"]
    red, orange, yellow = p["red"], p["orange"], p["yellow"]
    green, cyan, purple = p["green"], p["cyan"], p["purple"]
    accent = cyan
    st = {
        "border": border,
        "border.variant": aa(border, 0x80),
        "border.focused": accent,
        "border.selected": accent,
        "border.transparent": "#00000000",
        "border.disabled": aa(border, 0x80),
        "elevated_surface.background": chrome,
        "surface.background": chrome,
        "background": bg,
        "element.background": chrome,
        "element.hover": aa(hl, 0x80),
        "element.active": hl,
        "element.selected": hl,
        "element.disabled": aa(chrome, 0x80),
        "drop_target.background": aa(accent, 0x40),
        "ghost_element.background": "#00000000",
        "ghost_element.hover": aa(hl, 0x80),
        "ghost_element.active": hl,
        "ghost_element.selected": hl,
        "ghost_element.disabled": aa(chrome, 0x80),
        "text": fg,
        "text.muted": comment,
        "text.placeholder": comment,
        "text.disabled": comment,
        "text.accent": accent,
        "icon": fg,
        "icon.muted": comment,
        "icon.disabled": comment,
        "icon.placeholder": comment,
        "icon.accent": accent,
        "status_bar.background": chrome,
        "title_bar.background": chrome,
        "title_bar.inactive_background": chrome,
        "toolbar.background": bg,
        "tab_bar.background": chrome,
        "tab.inactive_background": chrome,
        "tab.active_background": bg,
        "search.match_background": aa(yellow, 0x44),
        "panel.background": chrome,
        "panel.focused_border": accent,
        "panel.indent_guide": aa(fg2, 0x40),
        "panel.indent_guide_active": fg2,
        "panel.indent_guide_hover": fg2,
        "pane.focused_border": accent,
        "pane_group.border": border,
        "scrollbar.thumb.background": aa(fg2, 0x33),
        "scrollbar.thumb.hover_background": aa(fg2, 0x55),
        "scrollbar.thumb.border": "#00000000",
        "scrollbar.track.background": "#00000000",
        "scrollbar.track.border": "#00000000",
        "editor.foreground": fg,
        "editor.background": bg,
        "editor.gutter.background": bg,
        "editor.subheader.background": chrome,
        "editor.active_line.background": aa(hl, 0x66),
        "editor.highlighted_line.background": aa(hl, 0x66),
        "editor.line_number": ln,
        "editor.active_line_number": fg,
        "editor.invisible": ln,
        "editor.wrap_guide": aa(fg2, 0x22),
        "editor.active_wrap_guide": aa(fg2, 0x44),
        "editor.indent_guide": aa(fg2, 0x22),
        "editor.indent_guide_active": aa(fg2, 0x55),
        "editor.document_highlight.read_background": aa(accent, 0x26),
        "editor.document_highlight.write_background": aa(orange, 0x26),
        "terminal.background": bg,
        "terminal.foreground": fg,
        "terminal.bright_foreground": fg,
        "terminal.dim_foreground": comment,
        "terminal.ansi.black": chrome,
        "terminal.ansi.red": red,
        "terminal.ansi.green": green,
        "terminal.ansi.yellow": yellow,
        "terminal.ansi.blue": cyan,
        "terminal.ansi.magenta": purple,
        "terminal.ansi.cyan": cyan,
        "terminal.ansi.white": fg,
        "terminal.ansi.bright_black": comment,
        "terminal.ansi.bright_red": red,
        "terminal.ansi.bright_green": green,
        "terminal.ansi.bright_yellow": yellow,
        "terminal.ansi.bright_blue": cyan,
        "terminal.ansi.bright_magenta": purple,
        "terminal.ansi.bright_cyan": cyan,
        "terminal.ansi.bright_white": fg,
        "terminal.ansi.dim_black": comment,
        "terminal.ansi.dim_red": red,
        "terminal.ansi.dim_green": green,
        "terminal.ansi.dim_yellow": yellow,
        "terminal.ansi.dim_blue": cyan,
        "terminal.ansi.dim_magenta": purple,
        "terminal.ansi.dim_cyan": cyan,
        "terminal.ansi.dim_white": fg2,
        "link_text.hover": accent,
        "version_control.added": green,
        "version_control.modified": yellow,
        "version_control.deleted": red,
    }
    pairs = [
        ("conflict", orange), ("created", green), ("deleted", red), ("error", red),
        ("hint", comment), ("info", cyan), ("modified", yellow), ("predictive", comment),
        ("renamed", cyan), ("success", green), ("warning", yellow),
    ]
    for name, color in pairs:
        st[name] = color
        st[name + ".background"] = aa(color, 0x22)
        st[name + ".border"] = aa(color, 0x55)
    for name in ("hidden", "ignored", "unreachable"):
        st[name] = comment
        st[name + ".background"] = chrome
        st[name + ".border"] = border
    st["players"] = players(p)
    st["syntax"] = syntax(p)
    return st

themes = [{"name": n, "appearance": p["appearance"], "style": style(p)}
          for n, p in PALETTES.items()]
family = {
    "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
    "name": "Monokai",
    "author": "Shariq Naiyer",
    "themes": themes,
}
target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "themes", "monokai.json")
with open(target, "w", encoding="utf-8") as f:
    json.dump(family, f, indent=2)
print("wrote", target, "with", len(themes), "themes:")
for t in themes:
    print("  -", t["name"], "(", t["appearance"], ")")
