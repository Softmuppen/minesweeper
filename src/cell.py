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
    FLAGGED = "10.png"
    MINE = "11.png"

class Cell(arcade.Sprite):

    discovered = None
    mine = None
    flagged = None

    def __init__(self):
        super().__init__()

        self.discovered = False
        self.mine = False
        self.flagged = False
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
            else:
                sprite_filename = CellSprite.UNDISCOVERED

        return basepath + sprite_filename

    def set_mine(self, isMine):
        self.mine = isMine

    def is_mine(self):
        return self.mine

    def set_neighboring_mines(self, neighboring_mines):
        self.neighboring_mines = neighboring_mines

    def get_neighboring_mines(self):
        return self.neighboring_mines

    def set_discovered(self, discovered):
        self.discovered = discovered

    def is_discovered(self):
        return self.discovered

    def is_undiscovered(self):
        return not self.is_discovered()

    def toggle_flagged(self):
        self.flagged = not self.is_flagged()

    def is_flagged(self):
        return self.flagged