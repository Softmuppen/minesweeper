import arcade

from enum import Enum

class CellSprite(str, Enum):
    NEIGHBOR_0 = "0.png"
    NEIGHBOR_1 = "1.png"
    NEIGHBOR_2 = "2.png"
    NEIGHBOR_3 = "3.png"
    NEIGHBOR_4 = "4.png"
    NEIGHBOR_5 = "5.png"
    NEIGHBOR_6 = "6.png"
    NEIGHBOR_7 = "7.png"
    NEIGHBOR_8 = "8.png"
    UNDISCOVERED = "9.png"
    UNDISCOVERED_HIGHLIGHTED = "12.png"
    FLAGGED = "10.png"
    MINE = "11.png"

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
        self.texture = arcade.load_texture(self.get_sprite_path())

    def get_sprite_path(self):
        basepath = "images/"
        sprite_filename = None

        if self.is_discovered():
            if self.mine:
                sprite_filename = CellSprite.MINE
            else:
                if self.neighboring_mines == 0:
                    sprite_filename = CellSprite.NEIGHBOR_0
                if self.neighboring_mines == 1:
                    sprite_filename = CellSprite.NEIGHBOR_1
                if self.neighboring_mines == 2:
                    sprite_filename = CellSprite.NEIGHBOR_2
                if self.neighboring_mines == 3:
                    sprite_filename = CellSprite.NEIGHBOR_3
                if self.neighboring_mines == 4:
                    sprite_filename = CellSprite.NEIGHBOR_4
                if self.neighboring_mines == 5:
                    sprite_filename = CellSprite.NEIGHBOR_5
                if self.neighboring_mines == 6:
                    sprite_filename = CellSprite.NEIGHBOR_6
                if self.neighboring_mines == 7:
                    sprite_filename = CellSprite.NEIGHBOR_7
                if self.neighboring_mines == 8:
                    sprite_filename = CellSprite.NEIGHBOR_8

        if self.is_undiscovered():
            if self.flagged:
               sprite_filename = CellSprite.FLAGGED
            elif self.highlighted:
                sprite_filename = CellSprite.UNDISCOVERED_HIGHLIGHTED
            else:
                sprite_filename = CellSprite.UNDISCOVERED

        return basepath + sprite_filename

    def get_index(self):
        return self.index

    def set_discovered(self, discovered):
        self.discovered = discovered

    def is_discovered(self):
        return self.discovered

    def is_undiscovered(self):
        return not self.is_discovered()