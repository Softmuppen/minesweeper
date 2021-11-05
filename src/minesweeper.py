#!/usr/bin/env python3

"""
Minesweeper Game
"""

import arcade

from enums.difficulties import Difficulty 
from board import Board

# Testing
from cell import Cell

# Constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Minesweeper"

# Pyglet Constants
ANTIALIASING=False

# Board Constants
BOARD_DIFFICULTY = Difficulty.EASY
BOARD_WIDTH = 30
BOARD_HEIGHT = 20

# Cell constants
CELL_WIDTH = 32
CELL_HEIGHT = 32
START_X = CELL_WIDTH // 2
START_Y = CELL_HEIGHT // 2


class Minesweeper(arcade.Window):
    """
    Main application class.
    """

    board = None

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, antialiasing=ANTIALIASING)

        # Initialize list for all drawables
        self.draw_list = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Populate drawables
        self.board = Board(BOARD_WIDTH,BOARD_HEIGHT,BOARD_DIFFICULTY)
        self.board.print_board()

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        # Define draw list as sprite list
        self.draw_list = arcade.SpriteList()

        # Test draw cell
        row_index = 0
        while row_index < self.board.height:
            col_index = 0
            while col_index < self.board.width:
                cell = self.board.get_cell([row_index, col_index])
                cell.update_sprite()
                x_position = START_X + col_index * cell.width
                y_position = START_Y + row_index * cell.height
                cell.position = x_position, y_position
                self.draw_list.append(cell)
                #print(f"[{player_self.board.self.board_array[row_index, col_index]}]", end ="")
                col_index += 1
            row_index += 1

        # Draw sprites
        self.draw_list.draw()

def main():
    """Main function"""
    window = Minesweeper()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
