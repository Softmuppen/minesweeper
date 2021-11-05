import arcade

from enum import IntEnum

class HiddenCellType(IntEnum):
    EMPTY = 0
    MINE = 1

class VisibleCellType(IntEnum):
    REGULAR = 0
    FLAGGED = 1
    MAYBE = 2

class Cell(arcade.Sprite):

    WIDTH = 32
    HEIGHT = 32

    def __init__(self, scale=1):
        # Image to use for the sprite when face up
        self.image_file_name = f"images/default.png"

        # Call the parent
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")