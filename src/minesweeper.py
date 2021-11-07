#!/usr/bin/env python3

"""
Minesweeper Game
"""

import arcade

from board import Board
from enums.difficulties import Difficulty
from enums.mouse_clicks import MouseClick


# Testing
from cell import Cell

# Constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 704
SCREEN_TITLE = "Minesweeper"

# Pyglet Constants, this is needed to get OpenGL working
ANTIALIASING=False

# Board Constants
BOARD_DIFFICULTY = Difficulty.EASY
BOARD_WIDTH = 28 #28
BOARD_HEIGHT = 18 #18

class Minesweeper(arcade.Window):
    """
    Main application class.
    """

    board = None
    draw_list = None

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, antialiasing=ANTIALIASING)

        # Initialize list for all drawables
        self.draw_list = None

        arcade.set_background_color(arcade.csscolor.SLATE_GRAY)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Populate drawables
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT, BOARD_DIFFICULTY)

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        # Define draw list as sprite list
        self.draw_list = arcade.SpriteList()

        # Fetch cells and add to drawlist
        self.draw_list.extend(self.board.get_update_cell_sprite_list())

        # Draw sprites
        self.draw_list.draw()

    def on_update(self, delta_time):
        # Restart game if lost
        if self.board.lost:
            self.setup()

        # Restart game if won
        if self.board.win:
            self.setup()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        hovered_cell = arcade.get_sprites_at_point((x, y), self.draw_list)
        if len(hovered_cell) == 1:
            self.board.handleCellHover(hovered_cell[0])
        elif len(hovered_cell) > 1:
            print("Multiple cells were hovered, this should not happen")
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        clicked_cells = arcade.get_sprites_at_point((x, y), self.draw_list)
        if len(clicked_cells) == 1:
            self.board.handleCellClick(clicked_cells[0], MouseClick(button))
        elif len(clicked_cells) > 1:
            print("Multiple cells were clicked, this should not happen")

def main():
    """Main function"""
    window = Minesweeper()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
