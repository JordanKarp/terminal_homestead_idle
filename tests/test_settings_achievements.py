from src.classes.game import Game


def test_toggle_settings_via_game_menu():
    game = Game()
    # simulate toggling show_all: pick settings then toggle then back
    class FakeIO:
        def __init__(self):
            self.inputs = ["1", "2"]  # Toggle show_all, then Back
            self.outputs = []

        def input(self, prompt=""):
            self.outputs.append(prompt)
            return self.inputs.pop(0)

        def print(self, *args, **kwargs):
            self.outputs.append(" ".join(str(a) for a in args))

        def clear(self):
            self.outputs.append("<clear>")

    fake = FakeIO()
    game.io = fake
    original = game.settings.show_all
    # call settings menu directly
    game.show_settings_menu()
    assert game.settings.show_all != original


def test_settings_injection():
    from src.classes.settings import Settings
    import src.classes.game as game_module
    import tempfile
    from pathlib import Path
    p = Path(tempfile.mkdtemp())
    old = game_module.SAVE_FILE_PATH
    try:
        game_module.SAVE_FILE_PATH = p
        s = Settings(show_all=False, autosave=True, autosave_interval=5)
        g = Game(settings=s)
        assert g.settings.show_all is False
        assert g.settings.autosave is True
        assert g.settings.autosave_interval == 5
    finally:
        game_module.SAVE_FILE_PATH = old


def test_achievements_menu_shows_placeholder():
    game = Game()
    class FakeIO:
        def __init__(self):
            self.inputs = [""]
            self.outputs = []

        def input(self, prompt=""):
            self.outputs.append(prompt)
            return self.inputs.pop(0)

        def print(self, *args, **kwargs):
            self.outputs.append(" ".join(str(a) for a in args))

        def clear(self):
            self.outputs.append("<clear>")

    fake = FakeIO()
    game.io = fake
    game.show_achievements_menu()
    assert any("No achievements yet" in o for o in fake.outputs)


def test_save_and_load_settings(tmp_path):
    import src.classes.game as game_module
    old = game_module.SAVE_FILE_PATH
    try:
        game_module.SAVE_FILE_PATH = tmp_path
        g = Game()
        g.settings.show_all = False
        assert g.save_settings()
        g2 = Game()
        # ensure load reads from tmp path
        assert g2.load_settings()
        assert g2.settings.show_all is False
    finally:
        game_module.SAVE_FILE_PATH = old


def test_homestead_settings_toggle_updates_game_and_persists(tmp_path):
    import src.classes.game as game_module
    from src.classes.homestead import Homestead
    from src.classes.player import Player
    from src.classes.environment import Environment
    from src.classes.game_time import GameTime

    old = game_module.SAVE_FILE_PATH
    try:
        game_module.SAVE_FILE_PATH = tmp_path
        g = Game()

        class FakeIO:
            def __init__(self):
                self.outputs = []

            def input(self, prompt=""):
                self.outputs.append(prompt)
                return ""

            def print(self, *args, **kwargs):
                self.outputs.append(" ".join(str(a) for a in args))

            def clear(self):
                self.outputs.append("<clear>")

        fake = FakeIO()
        g.io = fake

        player = Player(name="Tester", profession="Tester", starting_cash=0)
        env = Environment()
        gt = GameTime()
        h = Homestead(player, env, [], gt, show_all=True, io=g.io, game=g)

        # simulate selecting Settings via a task
        class DummyTask:
            def __init__(self, m):
                self.message = m
                self.structures = []
                self.items = []
                self.resources = []
                self.xp = {}
                self.duration = 0
                self.category = "Menu"

        # initial state
        assert g.settings.show_all is True
        # simulate selecting option 1 (toggle show_all) then press any key
        fake.inputs = ["1", ""]
        h.show_in_game_settings()
        # setting should be toggled and persisted
        assert g.settings.show_all is False
        g2 = Game()
        # read persisted settings
        assert g2.load_settings()
        assert g2.settings.show_all is False
    finally:
        game_module.SAVE_FILE_PATH = old


def test_homestead_autosave_toggle_and_interval(tmp_path):
    import src.classes.game as game_module
    from src.classes.homestead import Homestead
    from src.classes.player import Player
    from src.classes.environment import Environment
    from src.classes.game_time import GameTime

    old = game_module.SAVE_FILE_PATH
    try:
        game_module.SAVE_FILE_PATH = tmp_path
        g = Game()

        class FakeIO:
            def __init__(self):
                self.outputs = []
                self.inputs = []

            def input(self, prompt=""):
                self.outputs.append(prompt)
                return self.inputs.pop(0)

            def print(self, *args, **kwargs):
                self.outputs.append(" ".join(str(a) for a in args))

            def clear(self):
                self.outputs.append("<clear>")

        fake = FakeIO()
        g.io = fake

        player = Player(name="Tester", profession="Tester", starting_cash=0)
        env = Environment()
        gt = GameTime()
        h = Homestead(player, env, [], gt, show_all=True, io=g.io, game=g)

        # toggle autosave (option 2)
        fake.inputs = ["2", ""]
        h.show_in_game_settings()
        assert g.settings.autosave is True

        # next, set autosave interval to 15 (option 3)
        fake.inputs = ["3", "15", ""]
        h.show_in_game_settings()
        assert g.settings.autosave_interval == 15
    finally:
        game_module.SAVE_FILE_PATH = old
