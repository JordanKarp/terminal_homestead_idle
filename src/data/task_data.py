from src.classes.task import Task, TaskCategories
from src.constants import (
    VIEW_MESSAGE_LOG,
    SETTINGS,
    ACHIEVEMENTS,
    SAVE_GAME,
    TRAVEL_BACK_HOME,
    TRAVEL_TO_TOWN,
)
from src.data.item_data import items
from src.data.structure_data import structures


menu_tasks = {
    VIEW_MESSAGE_LOG: Task(
        message=VIEW_MESSAGE_LOG,
        duration=0,
        category=TaskCategories.MENU,
    ),
    "View Encyclopedia": Task(
        message="View Encyclopedia",
        duration=0,
        category=TaskCategories.MENU,
    ),
    SETTINGS: Task(
        message=SETTINGS,
        duration=0,
        category=TaskCategories.MENU,
    ),
    ACHIEVEMENTS: Task(
        message=ACHIEVEMENTS,
        duration=0,
        category=TaskCategories.MENU,
    ),
    SAVE_GAME: Task(
        message=SAVE_GAME,
        duration=0,
        category=TaskCategories.MENU,
    ),
}

town_tasks = {
    "Sell Items": Task(
        message="Sell Items",
        duration=30,
        category=TaskCategories.OTHER,
    ),
    "Sell Structures": Task(
        message="Sell Structures",
        duration=30,
        category=TaskCategories.OTHER,
    ),
    TRAVEL_BACK_HOME: Task(
        message=TRAVEL_BACK_HOME,
        duration=120,
        xp=2,
        category=TaskCategories.OTHER,
    ),
}

tasks = {
    # HARVESTING
    "Gather Sticks": Task(
        message="Gather Sticks",
        duration=30,
        xp=1,
        category=TaskCategories.GATHERING,
        items=[(5, items["Stick"])],
        resources=[],
    ),
    "Gather Mushrooms": Task(
        message="Gather Mushrooms",
        duration=30,
        xp=1,
        category=TaskCategories.GATHERING,
        items=[(2, items["Mushroom"])],
        resources=[(-2, "mushroom")],
    ),
    "Gather Berries": Task(
        message="Gather Berries",
        duration=20,
        xp=1,
        category=TaskCategories.GATHERING,
        items=[(10, items["Berry"])],
        resources=[(-1, "berry bush")],
    ),
    "Gather Rocks": Task(
        message="Gather Rocks",
        duration=30,
        xp=1,
        category=TaskCategories.GATHERING,
        items=[(2, items["Rock"])],
        resources=[(-2, "rock")],
    ),
    "Harvest Clay": Task(
        message="Harvest Clay",
        duration=30,
        xp=2,
        category=TaskCategories.GATHERING,
        items=[(5, items["Clay"])],
        resources=[(-2, "rock")],
        requirements=[structures["Stone Shovel"]],
    ),
    # IDEAS: Gather Reeds
    # LAND MAINTENANCE
    "Chop Tree": Task(
        message="Chop Tree",
        duration=60,
        xp=2,
        category=TaskCategories.LAND_MAINTENANCE,
        items=[(2, items["Log"])],
        resources=[(-1, "tree"), (1, "stump")],
        requirements=[structures["Stone Axe"]],
    ),
    "Remove Stump": Task(
        message="Remove Stump",
        duration=120,
        xp=2,
        category=TaskCategories.LAND_MAINTENANCE,
        items=[],
        resources=[(-1, "stump")],
        requirements=[structures["Stone Axe"], structures["Stone Shovel"]],
    ),
    # REFINE MATERIALS
    "Nap Rocks": Task(
        message="Nap Rocks",
        duration=60,
        xp=2,
        category=TaskCategories.REFINE_MATERIALS,
        items=[(-1, items["Rock"]), (2, items["Rock Shard"])],
    ),
    "Whittle Handle": Task(
        message="Whittle Handle",
        duration=60,
        xp=2,
        category=TaskCategories.REFINE_MATERIALS,
        items=[(-1, items["Stick"]), (1, items["Handle"])],
    ),
    "Make Brick": Task(
        message="Shape Brick",
        duration=30,
        xp=2,
        category=TaskCategories.REFINE_MATERIALS,
        requirements=[structures["Clay Oven"]],
        items=[(-5, items["Clay"]), (1, items["Brick"])],
        resources=[],
    ),
    # BUILD
    "Build Firepit": Task(
        message="Build Firepit",
        duration=60,
        xp=3,
        category=TaskCategories.BUILD,
        structures=[structures["Fire Pit"]],
        items=[(-5, items["Rock"]), (-2, items["Log"])],
        resources=[],
    ),
    "Build Shovel": Task(
        message="Build Shovel",
        duration=60,
        xp=3,
        category=TaskCategories.BUILD,
        structures=[structures["Stone Shovel"]],
        items=[(-1, items["Handle"]), (-1, items["Rock Shard"])],
        resources=[],
    ),
    "Build Stone Axe": Task(
        message="Build Stone Axe",
        duration=60,
        xp=3,
        category=TaskCategories.BUILD,
        structures=[structures["Stone Axe"]],
        items=[(-1, items["Handle"]), (-1, items["Rock Shard"])],
        resources=[],
    ),
    "Build Oven": Task(
        message="Build Oven",
        duration=120,
        xp=3,
        category=TaskCategories.BUILD,
        structures=[structures["Clay Oven"]],
        items=[(-5, items["Rock"]), (-5, items["Clay"]), (-2, items["Log"])],
        resources=[],
    ),
    # COOK
    "Cook Mushroom Stew": Task(
        message="Cook Mushroom Stew",
        duration=60,
        xp=2,
        category=TaskCategories.COOK,
        requirements=[structures["Fire Pit"]],
        items=[(-5, items["Mushroom"]), (1, items["Mushroom Stew"])],
        resources=[],
    ),
    TRAVEL_TO_TOWN: Task(
        message=TRAVEL_TO_TOWN,
        duration=120,
        xp=2,
        category=TaskCategories.OTHER,
    ),
}
