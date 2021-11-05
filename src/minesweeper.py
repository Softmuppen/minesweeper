#!/usr/bin/env python3

"""
Minesweeper Game
"""

import arcade

from enums.difficulties import Difficulty 
from boards import MineBoard, PlayerBoard

# Testing
from enums.cells import Cell

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Minesweeper"

# Pyglet Constants
ANTIALIASING=False

# Board Constants
BOARD_DIFFICULTY = Difficulty.MEDIUM
BOARD_WIDTH = 30
BOARD_HEIGHT = 18

class Minesweeper(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, antialiasing=ANTIALIASING)

        # Initialize list for all drawable cells
        self.draw_list = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        mine_board = MineBoard(BOARD_WIDTH,BOARD_HEIGHT,BOARD_DIFFICULTY)
        mine_board.print_board()

        player_board = PlayerBoard(BOARD_WIDTH,BOARD_HEIGHT)
        player_board.print_board()

        # Define draw list as sprite list
        self.draw_list = arcade.SpriteList()

        # Test draw cell
        row_index = 0
        while row_index < player_board.height:
            col_index = 0
            while col_index < player_board.width:
                cell = Cell()
                x_position = (col_index + 1) * cell.width
                y_position = (row_index + 1) * cell.height
                cell.position = x_position, y_position
                self.draw_list.append(cell)
                #print(f"[{player_board.board_array[row_index, col_index]}]", end ="")
                col_index += 1
            row_index += 1

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        # Draw cells
        self.draw_list.draw()

def main():
    """Main function"""
    window = Minesweeper()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
