from dataclasses import dataclass
from enum import Enum, auto


class StructureTypes(Enum):
    AXE = auto()
    SHOVEL = auto()
    COOKING = auto()


@dataclass(frozen=True)
class Structure:
    """Represents a buildable structure with category and value metadata."""
    name: str
    plural_name: str
    description: str
    category: StructureTypes
    value: int

    def __hash__(self):
        # Allows using Item as a dictionary key if needed
        return hash(self.name.lower())
