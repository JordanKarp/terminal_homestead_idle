class Player:
    def __init__(self):
        self.inventory = {}

    def add_to_inventory(self, item, count):
        if item in self.inventory:
            self.inventory[item] += count
        else:
            self.inventory[item] = count

    def remove_from_inventory(self, item, count):
        if item in self.inventory:
            if self.inventory[item] > count:
                self.inventory[item] -= count
            elif self.inventory[item] == count:
                del self.inventory[item]
            else:
                print("not enough", item)
        else:
            print("no items to remove")

    def display_inventory(self):
        if self.inventory:
            for item, count in self.inventory.items():
                print(f" - {count}x {item}")
        else:
            print(f" - None")

    def has_at_least(self, item, count):
        if item in self.inventory and self.inventory[item] >= count:
            return True
        return False
