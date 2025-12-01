from inventory import Inventory


class Player:
    def __init__(self):
        self.inventory = Inventory()
        self.money = 0