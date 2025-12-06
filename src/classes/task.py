from dataclasses import dataclass, field
from enum import Enum, auto


class TaskCategories(Enum):
    DEFAULT = auto()
    GATHERING = auto()
    LAND_MAINTENANCE = auto()
    REFINE_MATERIALS = auto()
    BUILD = auto()
    COOK = auto()

    def __str__(self):
        return self.name.replace("_", " ").title()

    def __repr__(self):
        return self.name.replace("_", " ").title()


def parse_category(value: str) -> TaskCategories:
    # Normalize string format to match enum names
    normalized = value.strip().replace(" ", "_").upper()
    return TaskCategories[normalized]


@dataclass(frozen=True)
class Task:
    message: str = "Task Mesasge"
    duration: int = 1
    category: TaskCategories = TaskCategories.DEFAULT
    requirements: list = field(default_factory=list)
    items: list = field(default_factory=list)
    resources: list = field(default_factory=list)
    structures: list = field(default_factory=list)
