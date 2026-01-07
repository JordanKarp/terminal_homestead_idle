from src.utility.utility_functions import get_non_empty_string, get_number


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


def test_get_non_empty_string_rejects_empty_and_trims():
    fake = FakeIO(inputs=["   ", "  Alice  "])
    result = get_non_empty_string("Name: ", min_length=1, max_length=10, io=fake)
    assert result == "Alice"
    # ensure error message was printed for empty submission
    assert any("Error" in o for o in fake.outputs)


def test_get_non_empty_string_respects_max_length():
    long_name = "a" * 15
    fake = FakeIO(inputs=[long_name, "Bob"])
    result = get_non_empty_string("Name: ", min_length=1, max_length=5, io=fake)
    assert result == "Bob"


def test_get_number_rejects_non_numeric_then_accepts():
    fake = FakeIO(inputs=["abc", "5"])
    result = get_number("Enter number: ", io=fake)
    assert result == 5
    assert any("Error" in o for o in fake.outputs)
