import arcade

from enum import Enum

class GameButtonSprite(Enum):
    SMILEY_REGULAR = "0.png"
    SMILEY_PRESSED = "1.png"
    SMILEY_COOL = "3.png"
    SMILEY_DEAD = "4.png"

class GameButton(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.game_lost = False
        self.game_won = False
        self.update_sprite()

        self.scale = 2

    def decide_sprite(self):
        sprite_integer = None
        if self.game_won:
            sprite_integer = GameButtonSprite.SMILEY_COOL
        elif self.game_lost:
            sprite_integer = GameButtonSprite.SMILEY_DEAD
        else:
            sprite_integer = GameButtonSprite.SMILEY_REGULAR
        return sprite_integer

    def update_sprite(self):
        self.texture = arcade.load_texture(self.get_sprite_path(GameButtonSprite(self.decide_sprite())))

    def get_sprite_path(self, sprite: GameButtonSprite):
        basepath = "images/smiley/"
        return basepath + sprite.value
