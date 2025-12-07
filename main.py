from src.classes.homestead import Homestead
from src.utility.clear_terminal import clear_terminal

show_all = True
hmstd = Homestead(show_all=show_all)
run = True

while run:
    clear_terminal()
    run = hmstd.game_loop()
