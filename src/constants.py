"""Project-wide constants for common task messages and option labels.

Centralizing these strings reduces magic literals and avoids typos when
matching task.message values across modules and tests.
"""
# Task messages
SETTINGS = "Settings"
ACHIEVEMENTS = "Achievements"
SAVE_GAME = "Save Game"
VIEW_MESSAGE_LOG = "View Message Log"
TRAVEL_BACK_HOME = "Travel back home"
TRAVEL_TO_TOWN = "Travel to town"

# UI labels
SAVE_SETTINGS = "Save settings"
NEW_GAME = "New Game"
LOAD_GAME = "Load Game"
BACK = "Back"
PRESS_ANY_KEY = "Press any key to continue."
NO_SAVE_FILES = "No save files found."
SAVE_CANCELLED = "Save cancelled."
SETTINGS_SAVED_MSG = "Settings saved."
FAILED_SAVE_GAME = "Failed to save game"
FAILED_LOAD_SAVE = "Failed to load save"
LOAD_CANCELLED = "Load cancelled."

__all__ = [
    "SETTINGS",
    "ACHIEVEMENTS",
    "SAVE_GAME",
    "VIEW_MESSAGE_LOG",
    "TRAVEL_BACK_HOME",
    "TRAVEL_TO_TOWN",
    "SAVE_SETTINGS",
]
