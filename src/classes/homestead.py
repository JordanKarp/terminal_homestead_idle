from src.classes.environment import Environment
from src.classes.game_time import GameTime
from src.classes.message_log import MessageLog
from src.classes.player import Player
from src.classes.task import Task, parse_category
from src.utility.utility_functions import ask_question
from src.data.task_data import tasks
from src.utility.color_text import color_text, strip_ansi


class Homestead:
    def __init__(self, player, environment, game_time, show_all=False):
        self.player = player
        self.environment = environment
        self.game_time = game_time
        self.structures = []
        self.message = MessageLog()
        self.show_all = show_all

    def get_tasks(self):
        if self.show_all:
            return tasks
        else:
            return {
                task_name: task
                for task_name, task in tasks.items()
                if self.validate_options(task)
            }

    def create_main_menu(self, tasks):
        main_menu = {}
        for task_name, task in tasks.items():
            if task.category not in main_menu:
                main_menu[task.category] = {}
            main_menu[task.category][task_name] = task
        return main_menu

    def create_main_menu_text(self, main_menu):
        """Return a list of category strings showing available (and optionally total) tasks per category."""

        def available_count(tasks_dict):
            return sum(
                bool(self.validate_options(task)) for task in tasks_dict.values()
            )

        if self.show_all:
            return [
                f"{key} ({available_count(main_menu[key])}/{len(main_menu[key])})"
                for key in main_menu
            ]
        else:
            return [f"{key} ({available_count(main_menu[key])})" for key in main_menu]

    def create_sub_menu_text(self, main_menu, task_category):
        if self.show_all:
            task_options = []
            approved_numbers = [0]
            for counter, task in enumerate(
                list(main_menu[task_category].keys()), start=1
            ):
                if self.validate_options(main_menu[task_category][task]):
                    approved_numbers.append(counter)
                task_options.append(task)
        else:
            task_options = list(main_menu[task_category].keys())
            approved_numbers = None
        return task_options, approved_numbers
    
    def parse_sub_menu_response(self,response):
        response = response.split(" (")[0]
        task_category = parse_category(response)
        return response, task_category

    def game_loop(self):
        self.display()
        tasks = self.get_tasks()
        main_menu = self.create_main_menu(tasks)
        main_category_list = self.create_main_menu_text(main_menu)

        if response := ask_question("Where do you want to start", main_category_list):
            response, task_category = self.parse_sub_menu_response(response)

            if task_category in main_menu:
                task_options, approved_numbers = self.create_sub_menu_text(
                    main_menu=main_menu, task_category=task_category
                )
                task_response = ask_question(
                    f"What type of {response.lower()}?",
                    task_options,
                    approved_options=approved_numbers,
                    quit=True,
                )
                if not task_response:
                    return True
                
                return self.hande_sub_menu_response(task_response, main_menu, task_category)
            
    def hande_sub_menu_response(self, task_response, main_menu, task_category):
        task_name = strip_ansi(task_response)
        task = main_menu[task_category][task_name]
        print
        if isinstance(task, Task):
            self.handle_task(task)
            return True
        else:
            ...

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

        if task.xp:
            self.player.experience.add_xp(task.category, task.xp)

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

    def display(self):
        print(f"{color_text('MESSAGE LOG', style='underline')}:")
        print(self.message.show_most_recent)
        print()

        print(f"{color_text('PLAYER', style='underline')}:")
        print(self.player.wallet)
        print(self.player.experience)
        print()

        print(f"{color_text('NATURE', style='underline')}:")
        print(self.environment)

        print(f"{color_text('INVENTORY', style='underline')}:")
        print(self.player.inventory)

        print(f"{color_text('STRUCTURES', style='underline')}:")
        for struct in self.structures:
            print(f" - {struct}")

        print("\n\n")
