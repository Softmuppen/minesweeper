import numpy as np
import random

from cell import Cell
from enums.difficulties import Difficulty
from enums.mouse_clicks import MouseClick

# Cell constants
CELL_WIDTH = 32
CELL_HEIGHT = 32
START_X = CELL_WIDTH + (CELL_WIDTH // 2)
START_Y = CELL_HEIGHT + (CELL_HEIGHT // 2)

class Board:

    def __init__(self, width, height, difficulty):
        self.width = width
        self.height = height
        self.cell_array = self.generate_empty_board()
        self.add_mines(difficulty)

    def generate_empty_board(self):
        print(f"Generating {self.width}x{self.height} board with {self.width * self.height} cells")
        new_cell_array = []
        for row_index in range(self.height):
            row_list = []
            for col_index in range(self.width):
                # Calculate position for new cell
                x_position = START_X + col_index * CELL_WIDTH
                y_position = START_Y + row_index * CELL_HEIGHT
                
                # Create new cell and add to list
                cell = Cell()
                cell.position = x_position, y_position
                row_list.append(cell)
            new_cell_array.append(row_list)
        return new_cell_array

    def print_board(self):
        row_index = self.height - 1
        while row_index >= 0:
            col_index = 0
            while col_index < self.width:
                print(f"[{str(self.get_cell([row_index, col_index]).is_mine())[0]}]", end ="")
                col_index += 1
            print()
            row_index -= 1

    def add_mines(self, difficulty: Difficulty):
        # Calculate how many mines based on diffuculty
        expected_mine_count = int(np.floor((self.width * self.height) * (difficulty / 100)))
        print(f"Adding {expected_mine_count} mines for difficulty {difficulty.name}")

        actual_mine_count = 0
        while actual_mine_count < expected_mine_count:
            # Get random index
            random_row = random.randint(0, self.height-1)
            random_col = random.randint(0, self.width-1)
            random_index = [random_row, random_col]
            
            # Check if index is already mine
            random_cell = self.get_cell(random_index)
            if not random_cell.is_mine():
                random_cell.set_mine(True)
                actual_mine_count += 1

    def get_cell(self, index):
        return self.cell_array[index[0]][index[1]]

    def get_update_cell_sprite_list(self):
        new_list = []
        for row_index in range(self.height):
            for col_index in range(self.width):
                cell = self.get_cell([row_index,col_index])
                cell.update_sprite()
                new_list.append(cell)
        return new_list

    def handleCellClick(self, cell: Cell, button: MouseClick):
        if button is MouseClick.LEFT:
            if cell.is_discovered():
                print("Already discovered")

            if cell.is_undiscovered():
                print("Discover cell")
                cell.set_discovered(True)

            if cell.is_mine():
                print("You lost!")

        if button is MouseClick.RIGHT:
            if cell.is_undiscovered():
                print("Toggle flag!")
                cell.toggle_flagged()