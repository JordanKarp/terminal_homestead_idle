from random import choice

from src.classes.acre import Acre, TERRAIN_COLORS, FLORA_CHARACTERS

class Map():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = []
    
    def generate_new_map(self):
        for _ in range(self.height):
            row = []
            for col in range(self.width):
                random_terrain = choice(list(TERRAIN_COLORS.keys()))
                random_flora = choice(list(FLORA_CHARACTERS.keys()))
                row.append(Acre(random_terrain, random_flora))
            self.grid.append(row)

    def display(self):
        for row in self.grid:
            row_display = ''.join([acre.display() for acre in row])
            print(row_display)
            # print()
