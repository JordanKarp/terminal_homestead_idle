from src.utility.utility_functions import ask_question, get_number
from src.classes.game import Game


class FakeIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def input(self, prompt=""):
        self.outputs.append(prompt)
        if not self.inputs:
            raise EOFError("No more fake inputs")
        return self.inputs.pop(0)

    def print(self, *args, **kwargs):
        self.outputs.append(" ".join(str(a) for a in args))

    def clear(self):
        self.outputs.append("<clear>")


def test_ask_question_with_fake_io():
    fake = FakeIO(inputs=["1"])  # choose first option
    result = ask_question("Pick:", ["A", "B"], io=fake)
    assert result == "A"
    # ensure prompts were recorded
    assert any("Pick:" in o for o in fake.outputs)


def test_game_new_game_uses_injected_io():
    fake = FakeIO(inputs=["Bob", "1"])  # name, Choose game type -> Normal
    game = Game()
    game.io = fake
    homestead = game.new_game()
    # should return a Homestead instance when Normal selected
    assert homestead is not False
    assert homestead.player.name == "Bob"
