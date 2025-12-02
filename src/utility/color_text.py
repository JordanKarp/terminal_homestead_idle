def color_text(text, fg=None, bg=None, style=None):
    """
    Returns ANSI-colored text without external libraries.

    Args:
        text  (str): The string to color.
        fg    (str): Foreground color name (e.g., "red", "green", "yellow").
        bg    (str): Background color name.
        style (str): Style name (e.g., "bold", "underline").
    """

    codes = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        "bright_black": 90, "bright_red": 91, "bright_green": 92,
        "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
        "bright_cyan": 96, "bright_white": 97
    }

    bg_codes = {k: v + 10 for k, v in codes.items() if v < 90}  # background versions

    styles = {
        "bold": 1,
        "dim": 2,
        "underline": 4,
        "blink": 5,
        "reverse": 7
    }

    seq = []

    if fg in codes:
        seq.append(str(codes[fg]))

    if bg in bg_codes:
        seq.append(str(bg_codes[bg]))

    if style in styles:
        seq.append(str(styles[style]))

    if seq:
        return f"\033[{';'.join(seq)}m{text}\033[0m"
    else:
        return text
