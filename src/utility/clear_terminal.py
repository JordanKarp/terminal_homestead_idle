"""Utilities for clearing the running terminal screen.

This provides a small wrapper that uses the platform-appropriate clear
command so tests can call the same API without depending on platform.
"""

import os


def clear_terminal():
    """Clear the terminal screen using the OS-appropriate command."""
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For Mac and Linux (posix)
    else:
        _ = os.system("clear")
