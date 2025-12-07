from src.classes.inventory import Inventory
from src.classes.experience import Experience, load_bonus_tables_from_file
from src.classes.wallet import Wallet

from src.data.location_data import locations
from src.classes.task import TaskCategories

SKILL_DATA_PATH = "./src/data/skill_bonus_data.json"


class Player:
    def __init__(self):
        self.inventory = Inventory()
        bonus_tables = load_bonus_tables_from_file(SKILL_DATA_PATH)
        self.experience = Experience(
            categories=TaskCategories, bonus_tables=bonus_tables
        )
        self.wallet = Wallet()
        self.location = "Home"

    def travel_to(self, location):
        if location not in locations:
            print("Location incorrect")
            return False
        self.location = location
        return True
