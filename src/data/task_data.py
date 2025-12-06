from src.classes.task import Task, TaskCategories
from src.data.item_data import items

tasks = {
    ############## HARVESTING
    "Gather Branches": Task(
        message="Gather Branches",
        duration=60,
        category=TaskCategories.GATHERING,
        items=[(2, items["Stick"])],
        resources=[],
    ),
    "Gather Mushrooms": Task(
        message="Gather Mushrooms",
        duration=60,
        category=TaskCategories.GATHERING,
        items=[(2, items["Mushroom"])],
        resources=[(-2, "mushroom")],
    ),
    "Gather Rock": Task(
        message="Gather Rocks",
        duration=60,
        category=TaskCategories.GATHERING,
        items=[(1, items["Rock"])],
        resources=[(-1, "rock")],
    ),
    ############## LAND MAINTENANCE
    "Chop Tree": Task(
        message="Chop Trees",
        duration=60,
        category=TaskCategories.LAND_MAINTENANCE,
        items=[(2, items["Log"])],
        resources=[(-1, "tree"), (1, "stump")],
    ),
    "Remove Stump": Task(
        message="Remove Stump",
        duration=120,
        category=TaskCategories.LAND_MAINTENANCE,
        items=[],
        resources=[(-1, "stump")],
    ),
    ############## REFINE MATERIALS
    "Nap Rocks": Task(
        message="Nap Rocks",
        duration=60,
        category=TaskCategories.REFINE_MATERIALS,
        items=[(-1, items["Rock"]), (2, items["Rock Shard"])],
    ),
    ############## BUILD
    "Build Firepit": Task(
        message="Build Firepit",
        duration=60,
        category=TaskCategories.BUILD,
        structures=["Fire Pit"],
        items=[(-5, items["Rock"]), (-2, items["Log"])],
        resources=[],
    ),
    ################ COOK
    "Cook Mushroom Stew": Task(
        message="Cook Mushroom Stew",
        duration=60,
        category=TaskCategories.COOK,
        requirements=["Fire Pit"],
        items=[(-5, items["Mushroom"]), (1, items["Mushroom Stew"])],
        resources=[],
    ),
}
