from src.classes.homestead import Homestead
from src.classes.player import Player
from src.classes.environment import Environment
from src.classes.game_time import GameTime
from src.classes.task import Task, TaskCategories


def test_handle_sub_menu_response_with_nonexistent():
    h = Homestead(Player("P"), Environment(), [], GameTime())
    assert h.handle_sub_menu_response("Nonexistent", {"Category": {}}, "Category") is False


def test_handle_sub_menu_response_with_task():
    h = Homestead(Player("P"), Environment(), [], GameTime())
    t = Task(message="Do Something", duration=1, category=TaskCategories.MENU)
    main_menu = {"Menu": {"Do Something": t}}
    # Using the display value, include no ANSI so strip_ansi is a no-op
    assert h.handle_sub_menu_response("Do Something", main_menu, "Menu") is True
