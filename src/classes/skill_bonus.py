from dataclasses import dataclass


@dataclass
class SkillBonus:
    """A single skill bonus applied at a particular level."""
    bonus_type: str
    amount: float


class SkillBonusTable:
    """Container of SkillBonus entries keyed by level."""
    def __init__(self):
        # internal structure: { level_int: [SkillBonus, ...] }
        self.table = {}

    def add_bonus(self, level: int, bonus: SkillBonus):
        self.table.setdefault(level, [])
        self.table[level].append(bonus)

    @staticmethod
    def from_json(json_dict):
        """Construct a SkillBonusTable from parsed JSON mapping."""
        table = SkillBonusTable()
        for level_str, entries in json_dict.items():
            level = int(level_str)
            for entry in entries:
                bonus = SkillBonus(**entry)
                table.add_bonus(level, bonus)
        return table

    def get_bonuses_up_to_level(self, level: int):
        """Return flattened bonuses for all levels up to `level` inclusive."""
        bonuses = []
        for lvl, entries in self.table.items():
            if lvl <= level:
                bonuses.extend(entries)
        return bonuses
