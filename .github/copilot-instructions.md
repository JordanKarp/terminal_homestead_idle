<!-- Copilot / Agent instructions for quick onboarding to this repo -->
# Terminal Homesteader — AI Agent Guidance

Purpose: Give an AI code assistant the minimum, actionable knowledge
to be productive in this codebase (entry points, conventions, tests,
and common refactor patterns).

**Big picture**
- **Entry point**: `main.py` creates `Game()` and calls `game.run()`.
- **Core domain**: `src/classes/` contains domain objects and controllers
  (`game.py`, `homestead.py`, `player.py`, `task.py`). `Game` orchestrates
  menus and constructs `Homestead` instances.
- **Static game data**: `src/data/` provides dictionaries for items,
  professions and structures (edit these to change game content).
- **Utility layer**: `src/utility/` holds small helpers (`io.py`,
  `utility_functions.py`, `color_text.py`) used across the app.

**Key patterns & conventions**
- IO is abstracted: use `src.utility.io.default_io`. Tests inject `FakeIO`
  or assign `game.io = fake_io` to simulate user interaction.
- Menus use `ask_question` (returns a label or `False` for Back/quit).
  Preserve that `False` contract when changing prompt behavior.
- Centralize UI strings in `src/constants.py` — use these constants in
  code and tests instead of raw strings.
- Saves are JSON in `save_data/` and reconstructed via `Class.from_dict()`;
  avoid adding pickle or other executable formats.

**How to run / test**
- Run the app: `python main.py` from repo root.
- Run all tests: `pytest -q`.
- Run a single test: `pytest tests/test_io_abstraction.py::test_game_new_game_uses_injected_io -q`.
- If tests are not discovered, ensure your working directory is the repo root
  and Python path includes `src/` (tests import from `src.*`).

**Quick examples**
- Inject `FakeIO` in a test (pattern used in `tests/test_io_abstraction.py`):
```
class FakeIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []
    def input(self, prompt=""):
        return self.inputs.pop(0)
    def print(self, *args, **kwargs):
        self.outputs.append(" ".join(map(str, args)))

fake = FakeIO(["Bob", "1"])  # name, choose Normal
game = Game()
game.io = fake
homestead = game.new_game()
```

- Serialization round-trip test (recommended pattern):
```
# create an instance, serialize, deserialize, assert equality/important fields
original = Homestead(...)
data = original.to_dict()
restored = Homestead.from_dict(data)
assert restored.player.name == original.player.name
```

**PR reviewer checklist**
- If changing menu labels: update `src/constants.py` and associated tests.
- If changing save format: add migration or clear doc and update `save_data/` tests.
- When adding new items/professions/structures: add an entry in `src/data/*.py`
  and a small test ensuring the new item is pickable in `ask_question` flows.
- For changes affecting IO, add `FakeIO`-based tests instead of relying on manual testing.

Files to inspect when changing behavior
- `src/classes/game.py` — main menu and settings persistence.
- `src/utility/io.py` — IO abstraction used throughout.
- `src/utility/utility_functions.py` — prompt and validation helpers.
- `src/constants.py` — canonical UI labels used in tests.
- `src/data/*.py` — static game content.

Safety & tests guidance
- Keep saves as JSON. Implement `to_dict()`/`from_dict()` before changing
  serialization. Add tests for round-trip fidelity.
- When modifying menus or constants, update tests that assert labels.

If you'd like, I can add example test templates (pytest fixtures for `FakeIO`),
or a short `CONTRIBUTING.md` checklist — tell me which to add.
