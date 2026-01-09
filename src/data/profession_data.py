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
        name="Herbalist",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Miner": Profession(
        name="Miner",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Rancher": Profession(
        name="Rancher",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Gatherer": Profession(
        name="Gatherer",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Farmer": Profession(
        name="Farmer",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Hunter": Profession(
        name="Hunter",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Blacksmith": Profession(
        name="Blacksmith",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Carpenter": Profession(
        name="Carpenter",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Merchant": Profession(
        name="Merchant",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Chef": Profession(
        name="Chef",
        starting_cash=50,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
    "Banker": Profession(
        name="Banker",
        starting_cash=500,
        skill_bonus=SkillBonus(
            {"bonus_type": "speed_multiplier", "amount": 2},
            {"bonus_type": "yield_multiplier", "amount": 2},
        ),
        starting_items=[],
        starting_structures=[],
    ),
}
