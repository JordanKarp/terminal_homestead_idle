from src.utility.color_text import color_text, rgb_text


TERRAIN_COLORS = {
    "grassland": (34, 239, 34),
    "forest": (34, 139, 34),
    "desert": (210, 180, 140),
    "water": (0, 191, 255),
    "mountain": (139, 137, 137),
    "plains": (124, 252, 0),
}   

FLORA_CHARACTERS = {
    "tree": "🌳",
    "bush": "🌿",
    "flower": "🌸",
    "cactus": "🌵",
    }

class Acre(): 
    def __init__(self, terrain: str, flora:str):
        self.terrain = terrain
        self.flora = flora

    def display(self):
        color = TERRAIN_COLORS.get(self.terrain, (255, 255, 255))
        char = FLORA_CHARACTERS.get(self.flora, "█")
        # print(color)
        # return color_text(char, fg=color)
        return rgb_text(".", *color, bg=True)
