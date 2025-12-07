from dataclasses import dataclass


@dataclass
class SkillBonus:
    bonus_type: str
    amount: float


class SkillBonusTable:
    def __init__(self):
        # internal structure: { level_int: [SkillBonus, ...] }
        self.table = {}

    def add_bonus(self, level: int, bonus: SkillBonus):
        self.table.setdefault(level, [])
        self.table[level].append(bonus)

    @staticmethod
    def from_json(json_dict):
        """
        json_dict = { "2": [{ "bonus_type": "...", "amount": ... }], ... }
        """
        table = SkillBonusTable()
        for level_str, entries in json_dict.items():
            level = int(level_str)
            for entry in entries:
                bonus = SkillBonus(**entry)
                table.add_bonus(level, bonus)
        return table

    def get_bonuses_up_to_level(self, level: int):
        bonuses = []
        for lvl, entries in self.table.items():
            if lvl <= level:
                bonuses.extend(entries)
        return bonuses
