from homestead import Homestead
from utility import question, clear_terminal

hmstd = Homestead()
run = True
while run:
    clear_terminal()
    options = hmstd.create_options_dict()
    hmstd.display()
    run = question("what do you want to do?", options)
