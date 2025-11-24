from random import randint

from game_time import GameTime
from player import Player
from task import Task
from natural_resources import natural_resource_dict
from utility import question
from item_data import items


class Homestead:
    def __init__(self):
        self.natural_resources = self.create_random_natural_resources()
        self.player = Player()
        self.game_time = GameTime()
        self.structures = []
        self.message = "No previous task"

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
        self.message = task.message + f" - {task.duration} minutes"
        self.game_time.advance(minutes=task.duration)

    def give_item_to_player(self, item, count=1):
        self.player.inventory.add_item(item, count)

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
        if self.player.inventory.has_item("Stick", 2):
            options.update({"Craft Fire": Task(self.craft_fire, "Craft Fire", 30)})
        if self.natural_resources.get("trees", 0) > 0:
            options.update(
                {"Chop Trees": Task(self.chop_tree, "Chop Trees - gain 1 log", 60)}
            )
        if self.natural_resources.get("bushes", 0) > 0:
            options.update(
                {"Chop Bushes": Task(self.chop_bush, "Chop Bushes - gain 2 sticks", 30)}
            )
        if self.natural_resources.get("rocks", 0) > 0:
            options.update(
                {
                    "Gather Rocks": Task(
                        self.gather_rock, "Gather Rocks - gain 1 rock", 30
                    )
                }
            )
        return options

    def display(self):
        print("TIME:")
        print(self.game_time)
        print("PREVIOUS TASK:")
        print(f" - {self.message}")

        print("NATURE:")
        for nat_resc in self.natural_resources:
            if self.natural_resources.get(nat_resc, 0) > 0:
                print(f" - {self.natural_resources[nat_resc]} {nat_resc}")

        print("INVENTORY:")
        print(self.player.inventory)

        print("STRUCTURES:")
        for struct in self.structures:
            print(f" - {struct}")

        print("\n\n")

    def craft_fire(self):
        self.player.inventory.remove_item("Stick", 2)
        self.structures.append("Fire")

    def chop_tree(self):
        self.natural_resources["trees"] -= 1
        self.natural_resources["stumps"] += 1
        self.give_item_to_player(items["Log"], 1)
        # self.player.add_to_inventory("Log", 1)

    def chop_bush(self):
        self.natural_resources["bushes"] -= 1
        # self.player.add_to_inventory("Sticks", 2)
        self.give_item_to_player(items["Stick"], 2)

    def gather_rock(self):
        self.natural_resources["rocks"] -= 1
        # self.player.add_to_inventory("Rock(s)", 1)
        self.give_item_to_player(items["Rock"], 2)
