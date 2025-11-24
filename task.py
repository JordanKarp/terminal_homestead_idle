from dataclasses import dataclass

from collections.abc import Callable


def do_nothing():
    pass


@dataclass(frozen=True)
class Task:
    # function: Callable = do_nothing
    message: str = "Task Mesasge"
    duration: int = 1
    add_items: list = []
    remove_items: list = []
    add_resources: list = []
    remove_resources: list = []
    create_structure: list = []
