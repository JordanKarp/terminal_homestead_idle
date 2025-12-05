from src.classes.environment import Environment
from src.classes.game_time import GameTime
from src.classes.message_log import MessageLog
from src.classes.player import Player
from src.classes.task import Task
from src.utility.utility_functions import question, ask_question
from src.data.task_data import tasks
from src.utility.color_text import color_text


class Homestead:
    def __init__(self):
        self.player = Player()
        self.environment = Environment()
        self.game_time = GameTime()
        self.structures = []
        self.message = MessageLog()
        self.show_all = True

    def create_menu(self):
        if not self.show_all:
            options = self.create_options()

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
        # print(tasks)
        for task_name, task in tasks.items():
            if task.category not in main_menu:
                main_menu[str(task.category.name)] = {}
            main_menu[str(task.category.name)][task_name] = task

        if self.show_all:
            # category_text_list = [f"{key} ({len(main_menu[key])})" ]
            # num_available =[main_menu[key][task_name] for key, task_name in main_menu.items()]
            # print(num_available)
            # for category in main_menu:
            #     available_tasks = 0
            #     for task_name in main_menu[category]:
            #         print(main_menu[category][task_name])
            #         if self.validate_options(main_menu[category][task_name]):
            #             available_tasks +=1
            
            main_cat_list= [f"{key} ({sum(1 for task_name in main_menu[key] if self.validate_options(main_menu[key][task_name]))}/{len(main_menu[key].keys())})" for key, task_name in main_menu.items()]
        else:
            main_cat_list = list(main_menu.keys())
        # print(len(main_menu[key]))
        response = ask_question("Where do you want to start", main_cat_list)
        if response:
            menu_cat = (response.split(' (')[0].upper()).replace(' ','_')
            if menu_cat in main_menu:
                choice = ask_question(
                    "What do you want to do now?", list(main_menu[menu_cat].keys())
                )
                if not task:
                    return False
                self.handle_task(main_menu[menu_cat][choice])
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
