from src.classes.environment import Environment
from src.classes.game_time import GameTime
from src.classes.message_log import MessageLog
from src.classes.player import Player
from src.classes.task import Task, parse_category
from src.utility.utility_functions import question, ask_question
from src.data.task_data import tasks
from src.utility.color_text import color_text, strip_ansi


class Homestead:
    def __init__(self):
        self.player = Player()
        self.environment = Environment()
        self.game_time = GameTime()
        self.structures = []
        self.message = MessageLog()
        self.show_all = False

    def get_tasks(self):
        if self.show_all:
            return tasks
        else:
            return {
                task_name: task
                for task_name, task in tasks.items()
                if self.validate_options(task)
            }

    def menu_loop(self):
        self.display()
        main_menu = {}
        tasks = self.get_tasks()

        for task_name, task in tasks.items():
            if task.category not in main_menu:
                main_menu[task.category] = {}
            main_menu[task.category][task_name] = task

        if self.show_all:
            # Category (available tasks / total tasks)
            main_cat_list = [
                f"{key} ({sum(bool(self.validate_options(main_menu[key][task_name])) for task_name in main_menu[key])}/{len(list(main_menu[key].keys()))})"
                for key in main_menu
            ]
        else:
            # Category (available tasks)
            main_cat_list = [
                f"{key} ({sum(bool(self.validate_options(main_menu[key][task_name])) for task_name in main_menu[key])})"
                for key in main_menu
            ]
        if response := ask_question("Where do you want to start", main_cat_list):
            response = response.split(" (")[0]
            task_category = parse_category(response)
            if task_category in main_menu:
                if self.show_all:
                    task_options = []
                    approved_numbers = []
                    counter = 1
                    for task in list(main_menu[task_category].keys()):
                        if self.validate_options(main_menu[task_category][task]):
                            task_options.append(task)
                            approved_numbers.append(counter)
                        counter += 1
                else:
                    task_options = list(main_menu[task_category].keys())
                    approved_numbers = None
                task_response = ask_question(
                    f"What type of {response.lower()}?",
                    task_options,
                    approved_options=approved_numbers,
                    quit=True,
                )
                if not task_response:
                    return True
                task_name = strip_ansi(task_response)
                self.handle_task(main_menu[task_category][task_name])
                return True

    def game_loop(self):
        self.display()
        options = self.create_options()
        task = question("What do you want to do?", options)
        if not task:
            return False
        self.handle_task(task)
        return True

    def handle_task(self, task: Task):
        # self.message = f"{task.message} - {task.duration} minutes"
        self.message.add_message(task.message, self.game_time.time, task.duration)

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

        self.game_time.advance(minutes=task.duration)

    def validate_options(self, task: Task):
        items_ok = all(
            self.player.inventory.has_item(item.name, count * -1)
            for count, item in task.items
            if count < 0
        )

        resources_ok = all(
            self.environment.has(resource, count * -1)
            for count, resource in task.resources
            if count < 0
        )

        requirements_ok = all(
            structure in self.structures for structure in task.requirements
        )

        return items_ok and resources_ok and requirements_ok

    def create_options(self):
        return {
            task_name: task
            for task_name, task in tasks.items()
            if self.validate_options(task)
        }

    def display(self):
        print("MESSAGE LOG:")
        print(self.message.show_most_recent)
        print()

        print(f"{color_text('NATURE', style='underline')}:")
        print(color_text(self.environment, fg="red"))

        print("INVENTORY:")
        print(self.player.inventory)

        print("STRUCTURES:")
        for struct in self.structures:
            print(f" - {struct}")

        print("\n\n")
