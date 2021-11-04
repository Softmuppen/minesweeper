import numpy as np
import random

from enums.cells import Cell

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board_array = self.generate_empty_board(width, height)

    def generate_empty_board(self, width, height):
        print(f"Generating a empty {width}x{height} board")
        generated_board = np.zeros((height, width), dtype=object)
        return generated_board

    def print_board(self):
        row_index = 0
        while row_index < self.height:
            col_index = 0
            while col_index < self.width:
                #print(self.board_array)
                print(f"[{self.board_array[row_index, col_index]}]", end ="")
                col_index += 1
            print()
            row_index += 1

class MineBoard(Board):

    def __init__(self, width, height, difficulty):
        print(f"Generating a {width}x{height} mine board")
        Board.__init__(self, width, height)
        self.add_mines(difficulty)

    # Remove need for constants self.width and self.height
    def add_mines(self, difficulty):
        expected_mine_count = int(np.floor((self.width * self.height) * (difficulty / 100)))
        print(f"Adding {expected_mine_count} mines for difficulty {difficulty.name}")

        actual_mine_count = 0
        while actual_mine_count < expected_mine_count:
            random_row = random.randint(0, self.height-1)
            random_col = random.randint(0, self.width-1)
            if self.board_array[random_row, random_col] == Cell.EMPTY:
                self.board_array[random_row, random_col] = Cell.MINE
                actual_mine_count += 1
