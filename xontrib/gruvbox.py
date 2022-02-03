"""
Gruvbox Theme, by Pavel Pertsev & others

https://github.com/morhetz/gruvbox

Code licensed under the MIT license
http://zenorocha.mit-license.org
"""

from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Escape,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
)
from xonsh.pyghooks import register_custom_pygments_style
from xonsh.ansi_colors import register_custom_ansi_style


ANSI_STYLE = {
    "BLACK": "#282828",
    "BLUE": "#458588",
    "CYAN": "#689d6a",
    "DEFAULT": "#d4be98",
    "GREEN": "#98971a",
    "ORANGE": "#d65d0e",
    "PURPLE": "#b16286",
    "RED": "#cc241d",
    "WHITE": "#ebdbb2",
    "YELLOW": "#d79921",
    "INTENSE_BLACK": "#665c54",
    "INTENSE_BLUE": "#83a598",
    "INTENSE_CYAN": "#8ec07c",
    "INTENSE_GREEN": "#b8bb26",
    "INTENSE_ORANGE": "#fe8019",
    "INTENSE_PURPLE": "#d3869b",
    "INTENSE_RED": "#fb4934",
    "INTENSE_WHITE": "#fbf1c7",
    "INTENSE_YELLOW": "#fabd2f",
}

BG_COLOR = "#282828"

PG_STYLE = {
    Comment: f"{ANSI_STYLE['INTENSE_BLACK']} italic",
    Comment.Hashbang: f"{ANSI_STYLE['INTENSE_BLACK']} italic",
    Comment.Multiline: f"{ANSI_STYLE['INTENSE_BLACK']} italic",
    Comment.Preproc: f"{ANSI_STYLE['INTENSE_BLACK']} italic",
    Comment.Single: f"{ANSI_STYLE['INTENSE_BLACK']} italic",
    Comment.Special: f"{ANSI_STYLE['INTENSE_BLACK']} italic",
    Generic: ANSI_STYLE["DEFAULT"],
    Generic.Deleted: ANSI_STYLE["INTENSE_BLACK"],
    Generic.Emph: ANSI_STYLE["WHITE"],
    Generic.Error: f"{ANSI_STYLE['RED']} bold",
    Generic.Heading: ANSI_STYLE["INTENSE_WHITE"],
    Generic.Inserted: ANSI_STYLE["INTENSE_WHITE"],
    Generic.Output: "#44475a",
    Generic.Prompt: ANSI_STYLE["WHITE"],
    Generic.Strong: f"{ANSI_STYLE['WHITE']} bold",
    Generic.Subheading: ANSI_STYLE["INTENSE_WHITE"],
    Generic.Traceback: ANSI_STYLE["ORANGE"],
    Error: f"{ANSI_STYLE['RED']} bold",
    Keyword: ANSI_STYLE["INTENSE_RED"],
    Keyword.Constant: ANSI_STYLE["INTENSE_RED"],
    Keyword.Declaration: ANSI_STYLE["INTENSE_RED"],
    Keyword.Namespace: f"{ANSI_STYLE['RED']} bold",
    Keyword.Pseudo: ANSI_STYLE["INTENSE_RED"],
    Keyword.Reserved: ANSI_STYLE["INTENSE_CYAN"],
    Keyword.Type: ANSI_STYLE["YELLOW"],
    Literal: ANSI_STYLE["INTENSE_WHITE"],
    Literal.Date: ANSI_STYLE["INTENSE_WHITE"],
    Name: ANSI_STYLE["INTENSE_BLUE"],
    Name.Attribute: ANSI_STYLE["INTENSE_CYAN"],
    Name.Builtin: ANSI_STYLE["WHITE"],
    Name.Builtin.Pseudo: ANSI_STYLE["INTENSE_ORANGE"],
    Name.Class: ANSI_STYLE["INTENSE_ORANGE"],
    Name.Constant: ANSI_STYLE["PURPLE"],
    Name.Decorator: ANSI_STYLE["INTENSE_RED"],
    Name.Entity: ANSI_STYLE["INTENSE_WHITE"],
    Name.Exception: ANSI_STYLE["INTENSE_PURPLE"],
    Name.Function: ANSI_STYLE["INTENSE_CYAN"],
    Name.Label: ANSI_STYLE["INTENSE_RED"],
    Name.Namespace: ANSI_STYLE["INTENSE_GREEN"],
    Name.Other: ANSI_STYLE["WHITE"],
    Name.Tag: ANSI_STYLE["INTENSE_ORANGE"],
    Name.Variable: ANSI_STYLE["WHITE"],
    Name.Variable.Class: f"{ANSI_STYLE['BLUE']} italic",
    Name.Variable.Global: f"{ANSI_STYLE['BLUE']} italic",
    Name.Variable.Instance: f"{ANSI_STYLE['BLUE']} italic",
    Number: ANSI_STYLE["INTENSE_PURPLE"],
    Number.Bin: ANSI_STYLE["INTENSE_PURPLE"],
    Number.Float: ANSI_STYLE["INTENSE_PURPLE"],
    Number.Hex: ANSI_STYLE["INTENSE_PURPLE"],
    Number.Integer: ANSI_STYLE["INTENSE_PURPLE"],
    Number.Integer.Long: ANSI_STYLE["INTENSE_PURPLE"],
    Number.Oct: ANSI_STYLE["INTENSE_PURPLE"],
    Operator: ANSI_STYLE["WHITE"],
    Operator.Word: ANSI_STYLE["RED"],
    Other: ANSI_STYLE["WHITE"],
    Punctuation: ANSI_STYLE["WHITE"],
    String: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Backtick: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Char: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Doc: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Double: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Escape: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Heredoc: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Interpol: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Other: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Regex: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Single: f"{ANSI_STYLE['INTENSE_GREEN']}",
    String.Symbol: f"{ANSI_STYLE['INTENSE_GREEN']}",
    Text: ANSI_STYLE["WHITE"],
    Whitespace: ANSI_STYLE["WHITE"],
}

register_custom_pygments_style("gruvbox", PG_STYLE, background_color=BG_COLOR)

register_custom_ansi_style("gruvbox", ANSI_STYLE)
