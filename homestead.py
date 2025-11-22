from random import randint

from player import Player
from task import Task
from natural_resources import natural_resource_dict
from utility import question


class Homestead:
    def __init__(self):
        self.natural_resources = self.create_random_natural_resources()
        self.player = Player()
        self.structures = []
        self.previous_message = "No previous task"

    def game_loop(self):
        self.display()
        options = self.create_options_dict()
        task = question("What do you want to do?", options)
        if not task:
            return False
        self.handle_task(task)
        return True

    def handle_task(self, task):
        task.function()
        self.previous_message = task.message
        self.duration = task.duration

    def create_random_natural_resources(self):
        resources = {}
        for resource, resource_data in natural_resource_dict.items():
            min = resource_data.get("minimum", 0)
            max = resource_data.get("maximum", 0)
            # growth = resource_data.get("maximum", 0)
            number = randint(min, max)
            resources[resource] = number
        return resources

    def create_options_dict(self):
        options = {}
        if self.player.has_at_least("Sticks", 2):
            options.update({"Craft Fire": Task(self.craft_fire, "Craft Fire", 1)})
        if self.natural_resources.get("trees", 0) > 0:
            options.update({"Chop Trees": Task(self.chop_tree, "Chop Trees", 1)})
        if self.natural_resources.get("bushes", 0) > 0:
            options.update({"Chop Bushes": Task(self.chop_bush, "Chop Bushes", 1)})
        if self.natural_resources.get("rocks", 0) > 0:
            options.update({"Gather Rocks": Task(self.gather_rock, "Gather Rocks", 1)})
        return options

    def display(self):
        print("PREVIOUS TASK:")
        print(f" - {self.previous_message}")

        print("NATURE:")
        for nat_resc in self.natural_resources:
            if self.natural_resources.get(nat_resc, 0) > 0:
                print(f" - {self.natural_resources[nat_resc]} {nat_resc}")

        print("INVENTORY:")
        self.player.display_inventory()

        print("STRUCTURES:")
        for struct in self.structures:
            print(f" - {struct}")

        print("\n\n")

    def craft_fire(self):
        self.player.remove_from_inventory("Sticks", 2)
        self.structures.append("Fire")
        self.previous_message = "A fire has been made"

    def chop_tree(self):
        print("chop")
        self.natural_resources["trees"] -= 1
        self.natural_resources["stumps"] += 1
        self.player.add_to_inventory("Log", 1)
        self.previous_message = "A tree has been chopped"

    def chop_bush(self):
        self.natural_resources["bushes"] -= 1
        self.player.add_to_inventory("Sticks", 2)
        self.previous_message = "A bush has been chopped"

    def gather_rock(self):
        self.natural_resources["rocks"] -= 1
        self.player.add_to_inventory("Rock(s)", 1)
        self.previous_message = "A rock has been gathered"
