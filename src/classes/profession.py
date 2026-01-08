from dataclasses import dataclass, field
from src.classes.skill_bonus import SkillBonus


@dataclass(frozen=True)
class Profession:
    """Player profession metadata including starting cash and bonuses."""
    name: str
    starting_cash: int
    skill_bonus: list[SkillBonus]
    starting_items: list = field(default_factory=list)
    starting_structures: list = field(default_factory=list)

    def __repr__(self):
        return self.name
