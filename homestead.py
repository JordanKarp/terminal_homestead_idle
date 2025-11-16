from player import Player


class Homestead:
    def __init__(self):
        self.trees = 110
        self.bushes = 110
        self.player = Player()
        self.structures = []

    def create_options_dict(self):
        options = {}
        if self.player.has_at_least("Sticks", 2):
            options.update({"Craft Fire": self.craft_fire})
        if self.trees > 0:
            options.update({"Chop Tree": self.chop_tree})
        if self.bushes > 0:
            options.update({"Chop Bush": self.chop_bush})
        return options

    def display(self):
        print("NATURE:")
        print(f"\t{self.trees} trees")
        print(f"\t{self.bushes} bushes")
        print("INVENTORY:")
        self.player.display_inventory()
        print("STRUCTURES:")
        for struct in self.structures:
            print("\t", struct)
        print()
        print()

    def craft_fire(self):
        self.player.remove_from_inventory("Sticks", 2)
        self.structures.append("Fire")
        print("A fire has been made")

    def chop_tree(self):
        self.trees -= 1
        self.player.add_to_inventory("Log", 1)
        print("one tree chopped")

    def chop_bush(self):
        self.bushes -= 1
        self.player.add_to_inventory("Sticks", 2)
        print("one bush chopped")
