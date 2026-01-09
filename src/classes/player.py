from src.classes.inventory import Inventory
from src.classes.experience import Experience, load_bonus_tables_from_file
from src.classes.wallet import Wallet
from src.classes.profession import Profession
from src.constants import LOCATION_INCORRECT

from src.data.location_data import locations
from src.classes.task import TaskCategories

SKILL_DATA_PATH = "./src/data/skill_bonus_data.json"


class Player:
    """Tracks player state including inventory, experience and location."""

    def __init__(self, name, profession, starting_cash=None):
        self.name = name
        self.inventory = Inventory()
        self.profession = profession
        bonus_tables = self.apply_profession()
        self.experience = Experience(
            categories=TaskCategories, bonus_tables=bonus_tables
        )
        if starting_cash is not None:
            self.wallet=Wallet(starting_amount=starting_cash)
        else:
            self.wallet = Wallet(starting_amount=self.profession.starting_cash)
        self.location = "Home"

    def apply_profession(self):
        """Apply profession-specific starting items and load bonuses.

        Returns bonus tables used by Experience if the profession provides them.
        """
        if isinstance(self.profession, Profession):
            for item in self.profession.starting_items:
                self.inventory.add_item(item)
            bonus_tables = load_bonus_tables_from_file(SKILL_DATA_PATH)
            # TODO add profession to bonus_tables
            return bonus_tables
        return []

    def travel_to(self, location):
        """Move the player to ``location`` if it exists, returning success."""
        if location not in locations:
            raise ValueError(f"Location '{location}' not found.")
        self.location = location
        return True
