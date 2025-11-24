from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    description: str
    value: int
    stackable: bool = True
    max_stack: int = 999

    def __hash__(self):
        # Allows using Item as a dictionary key if needed
        return hash(self.name.lower())
