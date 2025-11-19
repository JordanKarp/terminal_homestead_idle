from random import randint

from player import Player
from natural_resources import natural_resource_dict


class Homestead:
    def __init__(self):
        self.natural_resources = create_random_natural_resources()
        self.player = Player()
        self.structures = []

    def create_random_natural_resources(self):
        resources = {}
        for resource, resource_data in natural_resource_dict.items():
            min = resource_data.get('minimum', 0)
            max = resource_data.get('maximum', 0)
            growth = resource_data.get('maximum', 0)
            number = randint(min, max)
            resources[resource] = number
        return resources
    
    def create_options_dict(self):
        options = {}
        if self.player.has_at_least("Sticks", 2):
            options.update({"Craft Fire": self.craft_fire})
        if self.natural_resources.get('trees',0) >0:
            options.update({"Chop Tree": self.chop_tree})
        if self.natural_resources.get('bushes',0) >0:
            options.update({"Chop Bush": self.chop_bush})
        return options

    def display(self):
        print("NATURE:")
        for nat_resc in self.natural_resources:
            if self.natural_resources.get(nat_resc, 0) > 0:
                print(f"- {self.natural_resources[nat_resc]} {nat_resc}")
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
        self.natural_resources['trees'] -= 1
        self.natural_resources['stumps'] += 1
        self.player.add_to_inventory("Log", 1)
        print("one tree chopped")

    def chop_bush(self):
        self.natural_resources['bushes'] -= 1
        self.player.add_to_inventory("Sticks", 2)
        print("one bush chopped")
