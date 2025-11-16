from homestead import Homestead
from utility import question

hmstd = Homestead()
run = True
while run:
    options = hmstd.create_options_dict()
    hmstd.display()
    run = question("what do you want to do?", options)
