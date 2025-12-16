from src.classes.structure import StructureTypes, Structure


structures = {
    "Stone Axe": Structure(
        name="Stone Axe",
        plural_name="Stone Axes",
        description="A simple axe made from wood and sharpened stone.",
        category=StructureTypes.AXE,
        value=10,
    ),
    "Stone Shovel": Structure(
        name="Stone Shovel",
        plural_name="Stone Shovels",
        description="A simple shovel made from wood and sharpened stone.",
        category=StructureTypes.SHOVEL,
        value=10,
    ),
    "Fire Pit": Structure(
        name="Fire Pit",
        plural_name="Fire Pits",
        description="A fire pit.",
        category=StructureTypes.COOKING,
        value=5,
    ),
    "Clay Oven": Structure(
        name="Clay Oven",
        plural_name="Clay Ovens",
        description="A Clay Oven.",
        category=StructureTypes.COOKING,
        value=25,
    ),
}
