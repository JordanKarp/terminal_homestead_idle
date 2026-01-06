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
    original = game.settings["show_all"]
    # call settings menu directly
    game.show_settings_menu()
    assert game.settings["show_all"] != original


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
