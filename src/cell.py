import arcade

from enum import Enum

class CellSprite(Enum):
    NEIGHBOR_0 = 0
    NEIGHBOR_1 = 1
    NEIGHBOR_2 = 2
    NEIGHBOR_3 = 3
    NEIGHBOR_4 = 4
    NEIGHBOR_5 = 5
    NEIGHBOR_6 = 6
    NEIGHBOR_7 = 7
    NEIGHBOR_8 = 8
    UNDISCOVERED = 9
    UNDISCOVERED_HIGHLIGHTED = 12
    FLAGGED = 10
    MINE = 11

class Cell(arcade.Sprite):

    discovered = None
    mine = None
    flagged = None

    def __init__(self, index):
        super().__init__()

        self.index = index
        self.discovered = False
        self.mine = False
        self.flagged = False
        self.highlighted = False
        self.neighboring_mines = 0

    def update_sprite(self):
        # Maybe move load somewhere else, this runs alot
        self.texture = arcade.load_texture(self.get_sprite_path(self.decide_sprite_integer()))

    def get_sprite_path(self, cell_sprite: CellSprite):
        basepath = "images/cell/"
        file_extension = ".png"
        return basepath + str(cell_sprite.value) + file_extension

    def decide_sprite_integer(self):

        sprite_integer = None

        if self.discovered:
            if self.mine:
                sprite_integer = CellSprite.MINE
            else:
                sprite_integer = CellSprite(self.neighboring_mines)

        if not self.discovered:
            if self.flagged:
               sprite_integer = CellSprite.FLAGGED
            elif self.highlighted:
                sprite_integer = CellSprite.UNDISCOVERED_HIGHLIGHTED
            else:
                sprite_integer = CellSprite.UNDISCOVERED

        return sprite_integer