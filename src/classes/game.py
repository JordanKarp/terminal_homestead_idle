import pickle
from pathlib import Path
from datetime import datetime

from src.classes.homestead import Homestead
from src.classes.player import Player
from src.classes.game_time import GameTime
from src.classes.environment import Environment

from src.data.profession_data import professions
from src.data.item_data import items
from src.data.structure_data import structures

from src.utility.color_text import color_text
from src.utility.utility_functions import ask_question, get_number, get_non_empty_string
from src.utility.io import default_io

MAIN_MENU_OPTIONS = ["New Game", "Load Game", "Settings", "Achievements"]
GAME_TYPES = ["Normal", "Custom"]
SAVE_FILE_PATH = Path("save_data")


class Game:
    def __init__(self):
        from src.utility.io import default_io

        # Simple settings storage (expandable)
        self.settings = {
            "show_all": True,
            "achievements": [],
        }
        self.io = default_io

    def run(self):
        # Main menu (loop so returning from submenus goes back to main menu)
        while True:
            self.io.clear()
            choice = ask_question("Terminal Homesteader", MAIN_MENU_OPTIONS, io=self.io)
            if not choice:
                # 'Back' selected -> exit main menu / program
                return

            if choice == "New Game":
                if homestead := self.new_game():
                    self.play(homestead)
            elif choice == "Load Game":
                if homestead := self.load_game():
                    self.play(homestead)
            elif choice == "Settings":
                self.show_settings_menu()
            elif choice == "Achievements":
                self.show_achievements_menu()

    def show_settings_menu(self):
        options = ["Toggle show all tasks"]
        while True:
            choice = ask_question("Settings", options, io=self.io)
            if not choice or choice == "Back":
                return
            if choice == "Toggle show all tasks":
                self.settings["show_all"] = not self.settings.get("show_all", True)
                self.io.print(f"Show all tasks set to {self.settings['show_all']}")
                self.io.input("Press any key to continue.")

    def show_achievements_menu(self):
        achievements = self.settings.get("achievements", [])
        self.io.print("Achievements:")
        if not achievements:
            self.io.print("  No achievements yet.")
        else:
            for a in achievements:
                self.io.print(f"  - {a}")
        self.io.input("Press any key to continue.")

    def play(self, homestead):
        run = True
        while run:
            self.io.clear()
            run = homestead.game_loop()

    def new_game(self):
        name = get_non_empty_string("Enter player name: ", min_length=1, max_length=30, io=self.io)
        game_type = ask_question("Choose your game type: ", GAME_TYPES, io=self.io)
        if game_type == "Normal":
            return self.normal_game(name)
        elif game_type == "Custom":
            return self.custom_game(name)
        else:
            return False

    def normal_game(self, name):
        show_all = self.settings.get("show_all", True)
        profession_name = ask_question(
            "Choose your profession: ", list(professions.keys()), io=self.io
        )
        profession = professions[profession_name]
        player = Player(name=name, profession=profession)
        structures = []
        environment = Environment()
        game_time = GameTime()
        return Homestead(player, environment, structures, game_time, show_all, io=self.io)

    def custom_game(self, name):
        show_all = self.settings.get("show_all", True)
        starting_cash = get_number("Starting Cash: ", io=self.io)
        player = Player(name, profession="Customizer", starting_cash=int(starting_cash))
        self.add_custom_items(player)
        structures = self.add_custom_structures()
        environment = self.create_custom_environment()
        game_time = GameTime()
        return Homestead(player, environment, structures, game_time, show_all, io=self.io)

    def create_custom_environment(self):
        self.io.print(color_text("Create Environment:", style="underline"))
        resources = Environment().prompt_custom_resources()
        return Environment(resources)

    def add_custom_items(self, player):
        item_name = True
        while item_name:
            if item_name := ask_question("Pick starting item(s):", list(items), io=self.io):
                count = get_number("How many: ", io=self.io)
                player.inventory.add_item(items[item_name], count)

    def add_custom_structures(self):
        structures_to_add = []
        structure_name = True
        while structure_name:
            if structure_name := ask_question(
                "Pick starting structure(s):", list(structures), io=self.io
            ):
                structures_to_add.append(structures[structure_name])
        return structures_to_add

    def load_game(self):
        # Ensure save directory exists and list save files with metadata
        save_dir = SAVE_FILE_PATH
        if not save_dir.exists():
            self.io.print("No save files found.")
            self.io.input("Press any key to return to menu.")
            return False

        files = [p for p in save_dir.glob("*.sav") if p.is_file()]
        files += [p for p in save_dir.glob("*.json") if p.is_file()]
        if not files:
            self.io.print("No save files found.")
            self.io.input("Press any key to return to menu.")
            return False

        # Sort by modified time (newest first)
        files.sort(key=lambda p: p.stat().st_mtime, reverse=True)

        options = [f"{p.name} ({datetime.fromtimestamp(p.stat().st_mtime).strftime('%Y-%m-%d %H:%M')})" for p in files]
        response = ask_question("Which game?", options, io=self.io)
        # strip metadata appended to choice
        response_name = response.split(" (")[0]
        file_path = save_dir / response_name
        try:
            if file_path.suffix == ".json":
                import json

                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Reconstruct homestead from dict
                    homestead = Homestead.from_dict(data, io=self.io)
                    self.io.print(homestead)
                    return homestead
            elif file_path.suffix == ".sav":
                # Legacy pickle file — warn user and require explicit confirmation
                confirm = ask_question(
                    "This save appears to be a legacy pickle file. Loading it can execute arbitrary code. Proceed?",
                    ["Yes", "No"],
                    io=self.io,
                )
                if confirm != "Yes":
                    self.io.print("Load cancelled.")
                    self.io.input("Press any key to return to menu.")
                    return False
                with open(file_path, "rb") as f:
                    item = pickle.load(f)
                    self.io.print(item)
                    return item
            else:
                self.io.print(f"Unknown save format: {file_path.suffix}")
                self.io.input("Press any key to return to menu.")
                return False
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, json.JSONDecodeError) as e:
            self.io.print(f"Failed to load save '{response}': {e}")
            self.io.input("Press any key to return to menu.")
            return False
        except Exception as e:
            self.io.print(f"An unexpected error occurred loading '{response}': {e}")
            self.io.input("Press any key to return to menu.")
            return False
