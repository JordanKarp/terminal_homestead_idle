import tempfile
import json

from src.classes.game import Game
from src.classes.homestead import Homestead
from src.data.profession_data import professions
from src.data.item_data import items


def test_homestead_serialization_roundtrip(tmp_path):
    # Setup a homestead
    profession = professions["Woodsman"]
    player = type("P", (), {})()
    player.name = "Tester"
    player.inventory = type("I", (), {"items": {}})()
    # Use actual classes for a more thorough test
    game = Game()
    homestead = game.normal_game("Tester")
    # Add an item
    homestead.player.inventory.add_item(items["Log"], 2)

    # Serialize to dict and JSON
    d = homestead.to_dict()
    # Write to a temp file and read back
    fpath = tmp_path / "save.json"
    fpath.write_text(json.dumps(d))

    data = json.loads(fpath.read_text())
    new = Homestead.from_dict(data)

    assert new.player.name == homestead.player.name
    assert new.player.inventory.get_count("Log") == homestead.player.inventory.get_count("Log")
    assert new.environment.natural_resources["Trees"].count == homestead.environment.natural_resources["Trees"].count
