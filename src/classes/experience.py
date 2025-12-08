import json

from src.classes.skill_bonus import SkillBonusTable


class Experience:
    def __init__(self, categories=None, bonus_tables=None):
        self.xp = {}

        # bonus_tables: dict { "GATHERING": SkillBonusTable, ... }
        self.bonus_tables = bonus_tables or {}

        if categories:
            for cat in categories:
                key = self._cat_key(cat)
                self.xp[key] = 0

    def _cat_key(self, category):
        return category.name if hasattr(category, "name") else str(category)

    def add_xp(self, category, amount):
        key = self._cat_key(category)
        self.xp.setdefault(key, 0)
        self.xp[key] += amount

    def get_xp(self, category):
        return self.xp.get(self._cat_key(category), 0)

    def get_level(self, category):
        xp = self.get_xp(category)
        return xp // 100 + 1

    def xp_to_next_level(self, category):
        xp = self.get_xp(category)
        next_level_xp = ((xp // 100) + 1) * 100
        return next_level_xp - xp

    def get_active_bonuses(self, category):
        key = self._cat_key(category)
        level = self.get_level(category)

        table = self.bonus_tables.get(key)
        return table.get_bonuses_up_to_level(level) if table else []

    def __repr__(self):
        parts = []
        for category, xp in self.xp.items():
            level = self.get_level(category)
            category_name = category.title().replace("_", " ")
            parts.append(f"{category_name.ljust(16)} ({level}): {xp}")

        return "\n".join(parts)


def load_bonus_tables_from_file(filename="skill_bonuses.json"):
    with open(filename, "r") as f:
        raw = json.load(f)

    return {
        category_name: SkillBonusTable.from_json(table_dict)
        for category_name, table_dict in raw.items()
    }
