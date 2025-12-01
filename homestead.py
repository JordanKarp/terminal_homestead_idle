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

        if task.structures:
            for structure in task.structures:
                self.structures.append(structure)

        if task.items:
            for amount, item in task.items:
                if amount > 0:
                    self.player.inventory.add_item(item, amount)
                else:
                    self.player.inventory.remove_item(item.name, -1 * amount)
        if task.resources:
            for amount, resource in task.resources:
                self.environment.adjust_natural_resource_amount(resource, amount)

    def validate_options(self, task: Task):
        items_ok = all(
            self.player.inventory.has_item(item.name, count * -1)
            for count, item in task.items if count < 0
        )
        
        resources_ok = all(
            self.environment.has(resource, count *-1)
            for count, resource in task.resources if count < 0
        )

        requirements_ok = all(
            structure in self.structures for structure in task.requirements
        )

        print(self.structures, task.requirements, requirements_ok)
        
        return items_ok and resources_ok and requirements_ok

    def create_options(self):
        options = {}
        for task_name, task in tasks.items():
            
            if self.validate_options(task):
                options[task_name]=task
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
