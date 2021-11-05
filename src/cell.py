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
        self.texture = arcade.load_texture(self.getSpritePath())

    def getSpritePath(self):
        basepath = "images/"
        sprite_filename = None
        
        if not self.discovered:
            sprite_filename = CellSprite.UNDISCOVERED
        if self.mine:
            sprite_filename = CellSprite.MINE

        return basepath + sprite_filename

    def setMine(self, isMine):
        self.mine = isMine

    def isMine(self):
        return self.mine