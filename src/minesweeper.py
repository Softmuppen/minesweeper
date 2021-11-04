#!/usr/bin/env python3

"""
Minesweeper Game
"""

import arcade

from enums.difficulties import Difficulty 
from boards import MineBoard, PlayerBoard

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Minesweeper"

# Pyglet Constants
ANTIALIASING=False

# Board Constants
BOARD_DIFFICULTY = Difficulty.MEDIUM
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

class Minesweeper(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, antialiasing=ANTIALIASING)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        mine_board = MineBoard(BOARD_WIDTH,BOARD_HEIGHT,BOARD_DIFFICULTY)
        mine_board.print_board()

        player_board = PlayerBoard(BOARD_WIDTH,BOARD_HEIGHT)
        player_board.print_board()
        pass

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

def main():
    """Main function"""
    window = Minesweeper()
    window.setup()
    arcade.run()

    #import pyglet
    #pyglet.window.Window()

    #from pyglet.window import Window
    #from pyglet.gl import Config;
    #w = Window(config=Config(major_version=4, minor_version=1))
    #print('{}.{}'.format(w.context.config.major_version, w.context.config.minor_version))

if __name__ == "__main__":
    main()
