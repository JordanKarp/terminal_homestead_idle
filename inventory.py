from item import Item


class Inventory:
    """Dictionary-based inventory system."""

    def __init__(self):
        self.items = {}

    def add_item(self, item: Item, count=1):
        """Add count of an item."""
        if not item.stackable and count > 1:
            raise ValueError("Non-stackable items cannot have count > 1")

        if item.name not in self.items:
            # Add new entry
            add_count = min(count, item.max_stack)
            self.items[item.name] = {"item": item, "count": add_count}
            return add_count

        # Item already exists → stack
        current_count = self.items[item.name]["count"]
        addable = item.max_stack - current_count
        amount_added = min(addable, count)
        self.items[item.name]["count"] += amount_added
        return amount_added

    def remove_item(self, item_name: str, count=1) -> bool:
        """Remove items by name. Returns True if fully removed."""
        if item_name not in self.items:
            return False

        current = self.items[item_name]["count"]
        if count > current:
            return False

        new_count = current - count

        if new_count == 0:
            del self.items[item_name]
        else:
            self.items[item_name]["count"] = new_count

        return True

    def has_item(self, item_name: str, count=1) -> bool:
        """Check if inventory has at least count of an item."""
        return item_name in self.items and self.items[item_name]["count"] >= count

    def get_count(self, item_name: str) -> int:
        """Return how many of an item you have, or 0."""
        return self.items.get(item_name, {}).get("count", 0)

    def list_items(self):
        """Return list of (name, count)."""
        return [(name, data["count"]) for name, data in self.items.items()]

    def inventory_value(self):
        return sum(data['value']*data['count'] for _, data in self.item.items())

    def __str__(self):
        if not self.items:
            return "[Empty Inventory]"
        return "".join(
            (
                f"{data['count']:5d}x {name.title()}\n"
                if data["count"] == 1
                else f"{data['count']:5d}x {data['item'].plural_name}\n"
            )
            for name, data in self.items.items()
        )
