from task import Task
from item_data import items

tasks = {
    "Chop Tree": Task(
        message="Chop Trees",
        duration=60,
        items=[(2, items["Log"])],
        resources=[(-1, "tree"), (1, "stump")],
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
}
