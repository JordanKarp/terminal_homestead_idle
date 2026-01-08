"""Thin menu abstraction used by the CLI.

This module provides a small `Menu` class encapsulating a set of
options and the visibility mode (show_all). The implementation is
minimal and intended for CLI rendering.
"""


class Menu:
    """Simple container for a list of options.

    The class intentionally keeps behaviour small; rendering and input
    gathering are performed by higher-level utilities.
    """
    def __init__(self, all_options, show_all=True):
        self.all_options = all_options
        self.show_all = show_all

    def display(self):
        # Present a menu; the CLI controls selection separately.
        if self.show_all:
            return self.all_options
        return [o for o in self.all_options if o.get("visible", True)]