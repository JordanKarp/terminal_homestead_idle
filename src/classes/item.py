from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """Represents a game item with display names, description and value.

    The dataclass is intentionally hashable (by name) so Item objects can be
    used as dictionary keys if needed.
    """
    name: str
    plural_name: str
    description: str
    value: int
    stackable: bool = True
    max_stack: int = 999

    def __hash__(self):
        # Allows using Item as a dictionary key if needed
        return hash(self.name.lower())
