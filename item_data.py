from item import Item

items = {
    "Log": Item(
        name="Log",
        plural_name="Logs",
        description="A product from a tree, this can be used as a building block or can be refined further.",
        value=2,
    ),
    "Stick": Item(
        name="Stick",
        plural_name="Sticks",
        description="A product from a tree, this can be used as a crafting material or can be refined further.",
        value=1,
    ),
    "Rock": Item(
        name="Rock",
        plural_name="Rocks",
        description="A stone, found on your homestead.",
        value=1,
    ),
    "Rock Shard": Item(
        name="Rock Shard",
        plural_name="Rock Shards",
        description="A stone shard, can be used as a tool.",
        value=2,
    ),
    "Mushroom": Item(
        name="Mushroom",
        plural_name="Mushrooms",
        description="A mushroom, which can be eaten.",
        value=2,
    ),
    "Mushroom Stew": Item(
        name="Mushroom Stew",
        plural_name="Mushroom Stews",
        description="A mushroom stews, which can be eaten.",
        value=20,
    ),
}
