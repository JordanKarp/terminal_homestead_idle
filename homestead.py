from random import randint

from environment import Environment
from game_time import GameTime
from player import Player
from task import Task
from utility import question
from natural_resource_data import natural_resources
from task_data import tasks
from item_data import items


class Homestead:
    def __init__(self):
        self.player = Player()
        self.environment = Environment()
        self.game_time = GameTime()
        self.structures = []
        self.message = "No previous task"

    def game_loop(self):
        self.display()
        # options = self.create_options_dict()
        options = self.create_options()
        task = question("What do you want to do?", options)
        if not task:
            return False
        self.handle_task(task)
        return True

    def handle_task(self, task: Task):
        self.message = f"{task.message} - {task.duration} minutes"

        # TODO
        if task.structures:
            ...

        if task.items:
            for amount, item in task.items:
                if amount > 0:
                    self.player.inventory.add_item(item, amount)
                else:
                    self.player.inventory.remove_item(item, amount * -1)
        if task.resources:
            for amount, resource in task.resources:
                self.environment.adjust_natural_resource_amount(resource, amount)

    def create_options(self):
        options = {}
        for task_name, task in tasks.items():
            options[task_name] = task
        return options

    def create_options_dict(self):
        options = {}
        if self.player.inventory.has_item("Stick", 2):
            options["Craft Fire"] = Task(self.craft_fire, "Craft Fire", 30)
        if self.natural_resources.get("trees", 0) > 0:
            options["Chop Trees"] = Task(self.chop_tree, "Chop Trees - gain 1 log", 60)
        if self.natural_resources.get("bushes", 0) > 0:
            options["Chop Bushes"] = Task(
                self.chop_bush, "Chop Bushes - gain 2 sticks", 30
            )
        if self.natural_resources.get("rocks", 0) > 0:
            options["Gather Rocks"] = Task(
                self.gather_rock, "Gather Rocks - gain 1 rock", 30
            )
        return options

    def display(self):
        print("TIME:")
        print(self.game_time)
        print("PREVIOUS TASK:")
        print(f" - {self.message}")

        print("NATURE:")
        print(self.environment)

        print("INVENTORY:")
        print(self.player.inventory)

        print("STRUCTURES:")
        for struct in self.structures:
            print(f" - {struct}")

        print("\n\n")
