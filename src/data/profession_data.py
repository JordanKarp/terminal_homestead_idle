"""FORESTRY = auto()
FORAGING = auto()
ROCKWORKING = auto()
AGRICULTURE = auto()
ANIMAL_HUSBANDRY = auto()
HUNTING = auto()
COOKING = auto()
CONSTRUCTION = auto()
TOOLCRAFT = auto()
LAND_MAINTENANCE = auto()
HOUSEHOLD = auto()"""

from src.classes.skill_bonus import SkillBonus
from src.classes.profession import Profession
from src.data.item_data import items

professions = {
    "Woodsman": Profession(
        name="Woodsman",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[items["Log"], items["Log"]],
        starting_structures=["Axe"],
    ),
    "Herbalist": Profession(
        "Herbalist",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Miner": Profession(
        "Miner",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Rancher": Profession(
        "Rancher",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Gatherer": Profession(
        "Gatherer",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Farmer": Profession(
        "Farmer",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Hunter": Profession(
        "Hunter",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Blacksmith": Profession(
        "Blacksmith",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Carpenter": Profession(
        "Carpenter",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Merchant": Profession(
        "Merchant",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Chef": Profession(
        "Chef",
        50,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        ["Axe"],
    ),
    "Banker": Profession(
        "Banker",
        500,
        SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        [],
    ),
}
