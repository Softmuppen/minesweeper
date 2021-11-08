import arcade

from enum import Enum

class DigitSprite(Enum):
    _basepath = "images/display/"
    DIGIT_0 = _basepath + "0.png"
    DIGIT_1 = _basepath + "1.png"
    DIGIT_2 = _basepath + "2.png"
    DIGIT_3 = _basepath + "3.png"
    DIGIT_4 = _basepath + "4.png"
    DIGIT_5 = _basepath + "5.png"
    DIGIT_6 = _basepath + "6.png"
    DIGIT_7 = _basepath + "7.png"
    DIGIT_8 = _basepath + "8.png"
    DIGIT_9 = _basepath + "9.png"
    DIGIT_NEGATIVE = _basepath + "negative.png"

class DigitDisplay(arcade.Sprite):

    def __init__(self, display_value):
        super().__init__()

        self.display_value = display_value

    def update_sprite(self):
        if self.display_value == '-':
            self.texture = arcade.load_texture(DigitSprite.DIGIT_NEGATIVE.value)
        else:
            self.texture = arcade.load_texture(DigitSprite["DIGIT_" + self.display_value].value)