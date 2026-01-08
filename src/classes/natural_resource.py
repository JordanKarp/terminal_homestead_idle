from dataclasses import dataclass


@dataclass
class NaturalResource:
    """A single natural resource with count and growth behavior."""
    name: str
    plural_name: str
    description: str
    count: int
    growth_rate: float

    def __repr__(self):
        if self.count == 1:
            return f"{self.count:5d}x {self.name.title()}"
        else:
            return f"{self.count:5d}x {self.plural_name.title()}"
