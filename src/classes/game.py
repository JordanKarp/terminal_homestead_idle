import pickle

from src.classes.homestead import Homestead
from src.classes.player import Player
from src.classes.game_time import GameTime
from src.classes.environment import Environment

from src.data.profession_data import professions
from src.data.item_data import items

from src.utility.clear_terminal import clear_terminal
from src.utility.color_text import color_text
from src.utility.list_folder_items import list_folder_items
from src.utility.utility_functions import ask_question, get_number

MAIN_MENU_OPTIONS = ["New Game", "Load Game", "Settings", "Achievements"]
GAME_TYPES = ["Normal", "Custom"]
SAVE_FILE_PATH = "save_data"


class Game:
    def __init__(self):
        self.settings = None

    def run(self):
        # Main menu
        clear_terminal()
        if choice := ask_question("Terminal Homesteader", MAIN_MENU_OPTIONS):
            if choice == "New Game":
                if homestead := self.new_game():
                    self.play(homestead)
            elif choice == "Load Game":
                if homestead := self.load_game():
                    self.play(homestead)
            elif choice == "Settings":
                # TODO
                ...
            elif choice == "Achievements":
                # TODO
                ...

    def play(self, homestead):
        run = True
        while run:
            clear_terminal()
            run = homestead.game_loop()

    def new_game(self):
        name = input("Enter player name: ")
        game_type = ask_question("Choose your game type: ", GAME_TYPES)
        if game_type == "Normal":
            return self.normal_game(name)
        elif game_type == "Custom":
            return self.custom_game(name)
        else:
            return False

    def normal_game(self, name):
        show_all = True
        profession_name = ask_question("Choose your profession: ", list(professions.keys()))
        profession = professions[profession_name]
        player = Player(name=name, profession=profession)
        environment = Environment()
        game_time = GameTime()
        return Homestead(player, environment, game_time, show_all)

    def custom_game(self, name):
        show_all = True
        starting_cash = get_number("Starting Cash: ")
        player = Player(name, profession='Customizer', starting_cash=int(starting_cash))
        self.add_custom_items(player)
        environment = self.create_custom_environment()
        game_time = GameTime()
        return Homestead(player, environment, game_time, show_all)

    def create_custom_environment(self):
        print(color_text("Create Environment:", style='underline'))
        resources = Environment().prompt_custom_resources()
        return Environment(resources)
    
    def add_custom_items(self, player):
        item_name = True
        while item_name:
            if item_name := ask_question("Pick starting item(s):", list(items)):
                count = get_number("How many: ")
                player.inventory.add_item(items[item_name], count)

    def load_game(self):
        if files := list_folder_items(SAVE_FILE_PATH):
            response = ask_question("Which game?", files)
            with open(f"{SAVE_FILE_PATH}/{response}", "rb") as f:
                item = pickle.load(f)
                print(item)
                return item
        else:
            print(files)
            input("No save files found.")
