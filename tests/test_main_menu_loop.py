from src.classes.game import Game


def test_main_menu_returns_after_settings():
    # Simulate: choose Settings (3), then Back in settings (2), then Back in main menu (5)
    class FakeIO:
        def __init__(self):
            self.inputs = ["3", "2", "5"]
            self.outputs = []

        def input(self, prompt=""):
            self.outputs.append(prompt)
            return self.inputs.pop(0)

        def print(self, *args, **kwargs):
            self.outputs.append(" ".join(str(a) for a in args))

        def clear(self):
            self.outputs.append("<clear>")

    fake = FakeIO()
    game = Game()
    game.io = fake
    # run should return after we select Back on main menu
    game.run()
    # Ensure we saw Settings prompt and main menu cleared at least once
    from src.constants import SETTINGS
    assert any(SETTINGS in o for o in fake.outputs)
    assert "<clear>" in fake.outputs
