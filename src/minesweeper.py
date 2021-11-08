#!/usr/bin/env python3

"""
Minesweeper Game
"""

import arcade

from board import Board
from game_button import GameButton
from digit_display import DigitDisplay
from enums.difficulties import Difficulty
from enums.mouse_clicks import MouseClick


# Testing
from cell import Cell

# Constants
SCREEN_WIDTH = 960 #960
SCREEN_HEIGHT = 704 #704
SCREEN_TITLE = "Minesweeper"

# Pyglet Constants, this is needed to get OpenGL working
ANTIALIASING=False

# Board Constants
BOARD_DIFFICULTY = Difficulty.VERY_EASY
BOARD_WIDTH = 28 #28
BOARD_HEIGHT = 18 #18

# Debug settings
DEBUG_MODE = False
if DEBUG_MODE:
    arcade.enable_timings()

class Minesweeper(arcade.Window):
    """
    Main application class.
    """

    board = None
    mine_left_display = None
    total_time = 0.0

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True, antialiasing=ANTIALIASING)

        # Frame counter
        self.frame_count = 0

        # Initialize list for all drawables
        self.draw_list = arcade.SpriteList(use_spatial_hash=True)

        arcade.set_background_color(arcade.csscolor.SLATE_GRAY)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Create board
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT, BOARD_DIFFICULTY)

        # Create mines left display
        self.mine_left_display = DigitDisplay(4, 0, 681)

        # Create Game button
        self.game_button = GameButton()
        self.game_button.position = self.mine_left_display.width + (self.game_button.width // 2), 681

        # Create timer display
        self.time_counter = DigitDisplay(4, self.mine_left_display.width + self.game_button.width, 681)

        # Start game timer
        self.total_time = 0.0

    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """

        # Call the parent. Failing to do this will mess up the coordinates,
        # and default to 0,0 at the center and the edges being -1 to 1.
        super().on_resize(width, height)

        print(f"Window resized to: {width}, {height}")

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()

        # Define draw list as sprite list
        self.draw_list = arcade.SpriteList(use_spatial_hash=True)

        # Fetch cells and add to drawlist
        self.draw_list.extend(self.board.get_update_cell_sprite_list())

        # Fetch cells and add to drawlist
        self.draw_list.append(self.game_button)

        # Fetch displays and add to drawlist
        self.draw_list.extend(self.mine_left_display.get_sprite_list())
        self.draw_list.extend(self.time_counter.get_sprite_list())

        # Draw sprites
        self.draw_list.draw()

    def on_update(self, delta_time):
        # Update game timer
        if self.board.game_ongoing:
            self.total_time += delta_time
            seconds = int(self.total_time) % 60
            self.time_counter.update_display_value(seconds)

        # Update mine left counter
        self.mine_left_display.update_display_value(self.board.mines_total-self.board.flags_total)

        # Update game button
        self.game_button.game_lost = self.board.game_lost
        self.game_button.game_won = self.board.game_won
        self.game_button.update_sprite()

        # Performance analysis
        if DEBUG_MODE:
            self.frame_count += 1
            if self.frame_count % 60 == 0:
                arcade.print_timings()
                arcade.clear_timings()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        hovered_cell = arcade.get_sprites_at_point((x, y), self.draw_list)
        if len(hovered_cell) == 1:
            self.board.handleCellHover(hovered_cell[0])
        elif len(hovered_cell) > 1:
            print("Multiple cells were hovered, this should not happen")
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.draw_list)
        if len(clicked_sprites) == 1:
            if isinstance(clicked_sprites[0], GameButton):
                self.setup()
            elif (not self.board.game_lost) and (not self.board.game_won):
                self.board.handleCellClick(clicked_sprites[0], MouseClick(button))
            else:
                print("Should not happen")
        elif len(clicked_sprites) > 1:
            print("Multiple cells were clicked, this should not happen")

def main():
    """Main function"""
    window = Minesweeper()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
