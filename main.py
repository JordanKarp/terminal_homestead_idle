from src.classes.homestead import Homestead
from src.classes.player import Player
from src.classes.game_time import GameTime
from src.classes.environment import Environment
from src.utility.clear_terminal import clear_terminal


def new_game():
    show_all = True
    player = Player()
    environment = Environment()
    game_time = GameTime()
    return Homestead(
        player=player, environment=environment, game_time=game_time, show_all=show_all
    )


def run_game(homestead):
    run = True
    while run:
        clear_terminal()
        run = homestead.game_loop()


if __name__ == "__main__":
    homestead = new_game()
    run_game(homestead)
