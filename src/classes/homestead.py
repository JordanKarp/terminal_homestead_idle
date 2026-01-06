import pickle
from pathlib import Path

from src.classes.message_log import MessageLog
from src.classes.task import Task, parse_category
from src.utility.utility_functions import ask_question
from src.data.task_data import tasks, menu_tasks, town_tasks
from src.utility.color_text import color_text, strip_ansi
from src.utility.clear_terminal import clear_terminal
from src.utility.io import default_io
from src.utility.io import default_io


class Homestead:
    def __init__(self, player, environment, structures, game_time, show_all=False, io=default_io):
        self.player = player
        self.environment = environment
        self.game_time = game_time
        self.structures = structures
        self.message = MessageLog()
        self.show_all = show_all
        self.io = io

    def get_tasks(self):
        if self.player.location == "Home":
            combined_tasks = menu_tasks | tasks
        elif self.player.location == "Town":
            combined_tasks = menu_tasks | town_tasks

        if self.show_all:
            return combined_tasks
        else:
            return {
                task_name: task
                for task_name, task in combined_tasks.items()
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

    def parse_sub_menu_response(self, response):
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
                if task_response := ask_question(
                    f"What type of {response.lower()}?",
                    task_options,
                    approved_options=approved_numbers,
                    quit=True,
                ):
                    return self.hande_sub_menu_response(
                        task_response, main_menu, task_category
                    )
                else:
                    # So that quit is back and not quit
                    return True

    def hande_sub_menu_response(self, task_response, main_menu, task_category):
        task_name = strip_ansi(task_response)
        task = main_menu[task_category][task_name]

        if isinstance(task, Task):
            self.handle_task(task)
            return True
        else:
            return False

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

        self.handle_function_tasks(task)

    def handle_function_tasks(self, task):
        if task.message == "Travel back home":
            self.player.travel_to("Home")
        elif task.message == "Travel to town":
            self.player.travel_to("Town")
        elif task.message == "View Message Log":
            self.io.clear()
            self.message.show_log()
            self.io.input("Press any key to proceed.")
        elif task.message == "Settings":
            # Simple in-game settings hook: toggle showing all tasks for this homestead
            options = ["Toggle show all tasks (view currently: {} )".format(self.show_all), "Back"]
            if choice := ask_question("Settings", options, io=self.io):
                if "Toggle show all tasks" in choice:
                    self.show_all = not self.show_all
                    self.io.print(f"Local show_all set to {self.show_all}")
                    self.io.input("Press any key to continue.")
        elif task.message == "Achievements":
            # Simple placeholder: show that achievements are unimplemented
            self.io.print("Achievements placeholder: no achievements tracked yet.")
            self.io.input("Press any key to continue.")
        elif task.message == "Settings":
            # TODO Settings
            ...
        elif task.message == "Achievements":
            # TODO Settings
            ...
        elif task.message == "Save Game":
            self.save_game()

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
        self.io.print(f"{color_text('MESSAGE LOG', style='underline')}:")
        self.io.print(self.message.show_most_recent)
        self.io.print()

        default_io.print(f"{color_text('PLAYER', style='underline')}:")
        default_io.print(self.player.profession)
        default_io.print(self.player.wallet)
        default_io.print(self.player.experience)
        default_io.print()

        default_io.print(f"{color_text('NATURE', style='underline')}:")
        default_io.print(self.environment)

        default_io.print(f"{color_text('INVENTORY', style='underline')}:")
        default_io.print(self.player.inventory)

        self.io.print(f"{color_text('STRUCTURES', style='underline')}:")
        for struct in self.structures:
            if isinstance(struct, str):
                self.io.print(struct)
            else:
                self.io.print(f" - {struct.name}")

        self.io.print("\n\n")

    def save_game(self):
        save_dir = Path("save_data")
        save_dir.mkdir(parents=True, exist_ok=True)
        # sanitize filename by replacing path separators
        safe_name = str(self.player.name).replace("/", "_").replace("\\", "_")
        file_path = save_dir / f"{safe_name}.sav"

        # If file exists, confirm overwrite
        if file_path.exists():
            if not ask_question(f"Overwrite existing save '{file_path.name}'?", ["Yes", "No"], io=self.io) == "Yes":
                self.io.print("Save cancelled.")
                self.io.input("Press any key to continue.")
                return

        try:
            with open(file_path, "wb") as f:
                pickle.dump(self, f)
            self.io.print(f"Game saved to {file_path}")
            self.io.input("Press any key to continue.")
        except Exception as e:
            self.io.print(f"Failed to save game: {e}")
            self.io.input("Press any key to continue.")
