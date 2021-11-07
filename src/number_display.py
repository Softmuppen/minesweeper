import arcade

from enum import Enum

class NumberSprite(str, Enum):
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3
    NUMBER_4 = 4
    NUMBER_5 = 5
    NUMBER_6 = 6
    NUMBER_7 = 7
    NUMBER_8 = 8
    NUMBER_9 = 9

class NumberDisplay(arcade.Sprite):

    display_value = 0

    def __init__(self, display_value):
        self.display_value = display_value

    def update_sprite(self):
        # Maybe move load somewhere else, this runs alot
        self.texture = arcade.load_texture(self.get_sprite_path(NumberSprite(self.display_value)))

    def get_sprite_path(self, number_sprite: NumberSprite):
        basepath = "images/display/"
        file_extension = ".png"
        return basepath + str(number_sprite.value) + file_extension
