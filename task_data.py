from task import Task
from item_data import items

tasks = {
    "Chop Tree": Task(
        message="Chop Trees",
        duration=60,
        items=[(2, items["Log"])],
        resources=[(-1, "tree"), (1, "stump")],
    ),
    "Gather Rock": Task(
        message="Gather Rocks",
        duration=60,
        items=[(1, items["Rock"])],
        resources=[(-1, "rock"), (1, "stump")],
    ),
}
