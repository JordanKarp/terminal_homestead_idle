import json
from pathlib import Path
from datetime import datetime

from src.classes.environment import Environment
from src.classes.message_log import MessageLog
from src.classes.task import Task, parse_category
from src.classes.player import Player
from src.classes.inventory import Inventory
from src.classes.game_time import GameTime
from src.classes.natural_resource import NaturalResource
from src.classes.message_log import Message

from src.utility.utility_functions import ask_question, get_number
from src.utility.color_text import color_text, strip_ansi
from src.utility.io import default_io

from src.data.task_data import tasks, menu_tasks, town_tasks
from src.data.item_data import items as ITEMS
from src.data.structure_data import structures as STRUCTURES
from src.data.profession_data import professions as PROFESSIONS
from src.data.natural_resource_data import natural_resources as NATURAL_RESOURCE_DATA


class Homestead:
    def __init__(self, player, environment, structures, game_time, show_all=False, io=default_io, game=None):
        self.player = player
        self.environment = environment
        self.game_time = game_time
        self.structures = structures
        self.message = MessageLog()
        self.show_all = show_all
        self.io = io
        # optional reference to owning Game instance so in-game settings can
        # update and persist global settings
        self.game = game

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
                    return self.handle_sub_menu_response(
                        task_response, main_menu, task_category
                    )
                else:
                    # So that quit is back and not quit
                    return True

    def handle_sub_menu_response(self, task_response, main_menu, task_category):
        """Handle a selection from a sub-menu.

        Returns True when a Task was handled and the game loop should continue,
        otherwise False.
        """
        task_name = strip_ansi(task_response)
        task = main_menu[task_category][task_name]

        if isinstance(task, Task):
            self.handle_task(task)
            return True
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
            # show_log now returns a string; print it via IO
            log_text = self.message.show_log()
            if log_text:
                self.io.print(log_text)
            else:
                self.io.print("<no messages>")
            self.io.input("Press any key to proceed.")
        elif task.message == "Settings":
            # Delegate to the dedicated settings handler for clarity/testing
            self.show_in_game_settings()
        elif task.message == "Achievements":
            # Simple placeholder: show that achievements are unimplemented
            self.io.print("Achievements placeholder: no achievements tracked yet.")
            self.io.input("Press any key to continue.")
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

    def show_in_game_settings(self):
        """Display and handle the in-game settings menu.

        When the Homestead was created with a `game` reference, this menu
        updates the central Settings object and persists changes via
        `Game.save_settings()`. If no game is present, a minimal local-only
        toggle is shown for backwards compatibility.
        """
        if getattr(self, "game", None) is not None:
            g = self.game
            options = [
                f"Toggle show all tasks (currently: {g.settings.show_all})",
                f"Toggle autosave (currently: {g.settings.autosave})",
                f"Set autosave interval (minutes) (currently: {g.settings.autosave_interval})",
                "Save settings",
            ]
            choice = ask_question("Settings", options, io=self.io)
            if not choice:
                return

            if choice.startswith("Toggle show all tasks"):
                g.settings.show_all = not g.settings.show_all
                self.show_all = g.settings.show_all
                try:
                    g.save_settings()
                except Exception:
                    pass
                self.io.print(f"Global show_all set to {self.show_all}")
                self.io.input("Press any key to continue.")
            elif choice.startswith("Toggle autosave"):
                g.settings.autosave = not g.settings.autosave
                try:
                    g.save_settings()
                except Exception:
                    pass
                self.io.print(f"Autosave set to {g.settings.autosave}")
                self.io.input("Press any key to continue.")
            elif choice.startswith("Set autosave interval"):
                val = get_number("Autosave interval (minutes): ", io=self.io)
                g.settings.autosave_interval = int(val)
                try:
                    g.save_settings()
                except Exception:
                    pass
                self.io.print(f"Autosave interval set to {g.settings.autosave_interval} minutes")
                self.io.input("Press any key to continue.")
            elif choice == "Save settings":
                try:
                    g.save_settings()
                    self.io.print("Settings saved.")
                except Exception:
                    self.io.print("Failed to save settings.")
                self.io.input("Press any key to continue.")
        else:
            options = [f"Toggle show all tasks (view currently: {self.show_all} )", "Back"]
            if choice := ask_question("Settings", options, io=self.io):
                if "Toggle show all tasks" in choice:
                    self.show_all = not self.show_all
                    self.io.print(f"Local show_all set to {self.show_all}")
                    self.io.input("Press any key to continue.")

    def display(self):
        self.io.print(f"{color_text('MESSAGE LOG', style='underline')}:")
        self.io.print(self.message.show_most_recent)
        self.io.print()

        self.io.print(f"{color_text('PLAYER', style='underline')}:")
        self.io.print(self.player.profession)
        self.io.print(self.player.wallet)
        self.io.print(self.player.experience)
        self.io.print()

        self.io.print(f"{color_text('NATURE', style='underline')}:")
        self.io.print(self.environment)

        self.io.print(f"{color_text('INVENTORY', style='underline')}:")
        self.io.print(self.player.inventory)

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
        file_path = save_dir / f"{safe_name}.json"

        # If file exists, confirm overwrite
        if file_path.exists():
            if not ask_question(f"Overwrite existing save '{file_path.name}'?", ["Yes", "No"], io=self.io) == "Yes":
                self.io.print("Save cancelled.")
                self.io.input("Press any key to continue.")
                return

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=2)
            self.io.print(f"Game saved to {file_path}")
            self.io.input("Press any key to continue.")
        except Exception as e:
            self.io.print(f"Failed to save game: {e}")
            self.io.input("Press any key to continue.")

    def to_dict(self):
        """Serialize homestead to a JSON-safe dict."""
        return {
            "version": 1,
            "player": {
                "name": self.player.name,
                "profession": getattr(self.player.profession, "name", str(self.player.profession)),
                "wallet": getattr(self.player.wallet, "balance", 0),
                "location": self.player.location,
                "inventory": [(name, data["count"]) for name, data in self.player.inventory.items.items()],
            },
            "environment": {name: res.count for name, res in self.environment.natural_resources.items()},
            "structures": [s if isinstance(s, str) else s.name for s in self.structures],
            "game_time": self.game_time.as_tuple(),
            "messages": [
                {"text": m.text, "start": m.start_time.isoformat(), "duration": m.duration}
                for m in self.message.messages
            ],
        }

    @classmethod
    def from_dict(cls, data, io=default_io):
        """Reconstruct a Homestead from a saved dict."""
        # Player
        p = data.get("player", {})
        prof_name = p.get("profession")
        profession = PROFESSIONS.get(prof_name, prof_name)
        player = Player(name=p.get("name", "Player"), profession=profession, starting_cash=p.get("wallet", 0))
        # Reset inventory and repopulate from saved items
        player.inventory = Inventory()
        for item_name, count in p.get("inventory", []):
            if item_name in ITEMS:
                player.inventory.add_item(ITEMS[item_name], count)
        player.location = p.get("location", "Home")

        # Environment
        env_counts = data.get("environment", {})
        # Build NaturalResource objects using data file defaults where possible
        nat_resources = {}
        for name, count in env_counts.items():
            info = NATURAL_RESOURCE_DATA.get(name, {})
            plural = info.get("plural_name", name)
            desc = info.get("description", "No Description Found")
            growth = info.get("growth_rate", 0)
            nat_resources[name] = NaturalResource(name, plural, desc, count, growth)
        environment = Environment(nat_resources)

        # Structures
        struct_list = []
        for s in data.get("structures", []):
            if s in STRUCTURES:
                struct_list.append(STRUCTURES[s])
            else:
                struct_list.append(s)

        # Game time
        gt = GameTime()
        day, hour, minute = data.get("game_time", gt.as_tuple())
        gt.time = datetime(gt.time.year, gt.time.month, day, hour, minute)

        homestead = cls(player, environment, struct_list, gt, io=io)

        # Messages
        for m in data.get("messages", []):
            try:
                start = datetime.fromisoformat(m.get("start"))
            except Exception:
                start = gt.time
            homestead.message.messages.append(Message(m.get("text", ""), start, m.get("duration", 0)))

        return homestead
