import pickle

from src.classes.homestead import Homestead
from src.classes.player import Player
from src.classes.game_time import GameTime
from src.classes.environment import Environment

from src.data.profession_data import professions

from src.utility.clear_terminal import clear_terminal
from src.utility.list_folder_items import list_folder_items
from src.utility.utility_functions import ask_question

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
        profession = ask_question("Choose your profession: ", list(professions.keys()))
        profession = professions[profession]
        player = Player(name=name, profession=profession)
        environment = Environment()
        game_time = GameTime()
        return Homestead(player, environment, game_time, show_all)

    def custom_game(self, name):
        pass

    def load_game(self):
        if files := list_folder_items(SAVE_FILE_PATH):
            response = ask_question("Which game?", files)
            with open(response, "rb") as f:
                return pickle.load(f)
        else:
            input("No save files found.")
