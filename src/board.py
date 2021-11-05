import numpy as np
import random
import arcade

from cell import Cell

class Board:

    def __init__(self, width, height, difficulty):
        self.width = width
        self.height = height
        self.cell_array = self.generate_empty_board()
        self.add_mines(difficulty)

    def generate_empty_board(self):
        print(f"Generating {self.width}x{self.height} board with {self.width * self.height} cells")
        new_cell_array = []
        for row in range(self.height):
            row = []
            for col in range(self.width):
                cell = Cell()
                row.append(cell)
            new_cell_array.append(row)
        return new_cell_array

    def print_board(self):
        row_index = 0
        while row_index < self.height:
            col_index = 0
            while col_index < self.width:
                print(f"[{str(self.get_cell([row_index, col_index]).isMine())[0]}]", end ="")
                col_index += 1
            print()
            row_index += 1

    def add_mines(self, difficulty):

        print("Mine add")

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
            if not random_cell.isMine():
                random_cell.setMine(True)
                actual_mine_count += 1            

    def get_cell(self, index):
        return self.cell_array[index[0]][index[1]]

