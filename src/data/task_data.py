from src.classes.task import Task
from src.data.item_data import items

tasks = {
    "Chop Tree": Task(
        message="Chop Trees",
        duration=60,
        items=[(2, items["Log"])],
        resources=[(-1, "tree"), (1, "stump")],
    ),
    "Gather Mushrooms": Task(
        message="Gather Mushrooms",
        duration=60,
        items=[(2, items["Mushroom"])],
        resources=[(-2, "mushroom")],
    ),
    "Remove Stump": Task(
        message="Remove Stump",
        duration=120,
        items=[],
        resources=[(-1, "stump")],
    ),
    "Gather Rock": Task(
        message="Gather Rocks",
        duration=60,
        items=[(1, items["Rock"])],
        resources=[(-1, "rock")],
    ),
    "Nap Rocks": Task(
        message="Nap Rocks",
        duration=60,
        items=[(-1, items["Rock"]), (2, items["Rock Shard"])],
    ),
    "Build Firepit": Task(
        message="Build Firepit",
        duration=60,
        structures=["Fire Pit"],
        items=[(-5, items["Rock"]), (-2, items["Log"])],
        resources=[],
    ),
    "Cook Mushroom Stew": Task(
        message="Cook Mushroom Stew",
        duration=60,
        requirements=["Fire Pit"],
        items=[(-5, items["Mushroom"]), (1, items["Mushroom Stew"])],
        resources=[],
    ),
}
