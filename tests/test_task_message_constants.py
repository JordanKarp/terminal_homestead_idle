from src.constants import (
    VIEW_MESSAGE_LOG,
    SETTINGS,
    ACHIEVEMENTS,
    SAVE_GAME,
    TRAVEL_BACK_HOME,
    TRAVEL_TO_TOWN,
)
from src.data import task_data


def test_menu_tasks_use_constants():
    # Ensure menu tasks use the centralized constants for keys and messages
    for const in (VIEW_MESSAGE_LOG, SETTINGS, ACHIEVEMENTS, SAVE_GAME):
        assert const in task_data.menu_tasks
        assert task_data.menu_tasks[const].message == const


def test_town_tasks_use_constants():
    for const in (TRAVEL_BACK_HOME, TRAVEL_TO_TOWN):
        assert const in task_data.town_tasks
        assert task_data.town_tasks[const].message == const
