from dataclasses import dataclass, field

from collections.abc import Callable


def do_nothing():
    pass


@dataclass(frozen=True)
class Task:
    message: str = "Task Mesasge"
    duration: int = 1
    requirements: list = field(default_factory=list)
    items: list = field(default_factory=list)
    resources: list = field(default_factory=list)
    structures: list = field(default_factory=list)
