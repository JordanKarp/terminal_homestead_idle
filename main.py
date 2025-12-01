from src.classes.homestead import Homestead
from src.utility import clear_terminal

hmstd = Homestead()
run = True
while run:
    clear_terminal()
    run = hmstd.game_loop()
