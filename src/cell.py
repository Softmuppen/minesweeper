import arcade

from enum import Enum

class CellSprite(str, Enum):
    BLANK = "0.png"
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
                sprite_filename = CellSprite.BLANK

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