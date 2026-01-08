"""IO abstraction layer used to decouple console operations for testing."""

from src.utility.clear_terminal import clear_terminal


class IO:
    """Small IO abstraction to allow swapping input/print/clear for tests."""

    def __init__(self, input_fn=input, print_fn=print, clear_fn=clear_terminal):
        self._input = input_fn
        self._print = print_fn
        self._clear = clear_fn

    def input(self, prompt: str = "") -> str:
        return self._input(prompt)

    def print(self, *args, **kwargs) -> None:
        return self._print(*args, **kwargs)

    def clear(self) -> None:
        return self._clear()


# Default console IO
default_io = IO()
