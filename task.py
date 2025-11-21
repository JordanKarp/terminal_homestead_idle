from dataclasses import dataclass

from collections.abc import Callable


def do_nothing():
    pass

@dataclass
class Task:
    function: Callable = do_nothing
    message: str = 'Task Mesasge'
    duration: int = 1

