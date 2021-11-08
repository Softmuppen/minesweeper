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
        # Cell variables
        self.width = width
        self.height = height
        self.cell_array = self.generate_empty_board()
        self.highlighted_cell = None
        self.clicked_cell = None

        # Game variables
        self.game_difficulty = difficulty
        self.game_ongoing = False
        self.game_lost = False
        self.game_won = False

        # Flag and mine variables
        self.mines_generated = False
        self.mines_total = 0
        self.undiscovered_mineless_cells_left = 0
        self.flags_total = 0

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
                cell = Cell([row_index, col_index])
                cell.position = x_position, y_position
                row_list.append(cell)
            new_cell_array.append(row_list)
        return new_cell_array

    def print_board(self):
        row_index = self.height - 1
        while row_index >= 0:
            col_index = 0
            while col_index < self.width:
                if self.get_cell_by_index([row_index, col_index]).mine:
                    print(f"[X]", end ="")
                else:
                    print(f"[{self.get_cell_by_index([row_index, col_index]).neighboring_mines}]", end ="")

                col_index += 1
            print()
            row_index -= 1

    def calculate_total_mine_count(self, difficulty: Difficulty):
        # Calculate how many mines based on diffuculty
        expected_mine_count = int(np.floor((self.width * self.height) * (difficulty / 100)))
        print(f"Adding {expected_mine_count} mines for difficulty {difficulty.name}")
        return expected_mine_count

    def add_mines(self):
        expected_mine_count = self.calculate_total_mine_count(self.game_difficulty)

        # Add mines
        actual_mine_count = 0
        while actual_mine_count < expected_mine_count:
            # Get random cell
            random_row = random.randint(0, self.height-1)
            random_col = random.randint(0, self.width-1)
            random_index = [random_row, random_col]
            random_cell = self.get_cell_by_index(random_index)

            # Avoid random cell being clicked cell and its neighbors
            if random_cell == self.clicked_cell or random_cell in self.get_neighbors(self.clicked_cell):
                continue

            # Check if cell is already mine
            if not random_cell.mine and self.clicked_cell != random_cell:
                random_cell.mine = True
                actual_mine_count += 1
        self.mines_generated = True
        self.mines_total = actual_mine_count
        self.undiscovered_mineless_cells_left = (self.width * self.height) - actual_mine_count

    def get_neighbors(self, target_cell: Cell):
        index = target_cell.index
        neighboring_cells = []
        for neighbor_row_index in range(index[0]-1, index[0]+2):
            for neighbor_col_index in range(index[1]-1, index[1]+2):
                # Ignore target cell itself
                if neighbor_row_index == index[0] and neighbor_col_index == index[1]:
                    pass
                # Make sure we are inbounds
                is_valid_row = neighbor_row_index >= 0 and neighbor_row_index < self.height
                is_valid_col = neighbor_col_index >= 0 and neighbor_col_index < self.width
                if is_valid_row and is_valid_col:
                    neighboring_cells.append(self.get_cell_by_index([neighbor_row_index,neighbor_col_index]))
                else:
                    pass

        return neighboring_cells

    def calculate_neighbors(self):
        # Populate neighbor values
        for row_index in range(self.height):
            for col_index in range(self.width):

                # Iterate neighbor cells and count mines
                neighboring_mines = 0
                for neighbor_cell in self.get_neighbors(self.get_cell_by_index([row_index, col_index])):
                    if neighbor_cell.mine:
                        neighboring_mines += 1
                        pass

                target_cell = self.get_cell_by_index([row_index, col_index])
                target_cell.neighboring_mines = neighboring_mines

    def discover_cell_and_neighbors(self, current_cell: Cell):
        # Discover cell
        current_cell.discovered = True
        self.undiscovered_mineless_cells_left -= 1

        # Discover neighbors
        if current_cell.neighboring_mines == 0:
            for neighbor_cell in self.get_neighbors(current_cell):
                if not neighbor_cell.discovered:
                    self.discover_cell_and_neighbors(neighbor_cell)

    def get_cell_by_index(self, index):
        return self.cell_array[index[0]][index[1]]

    def get_update_cell_sprite_list(self):
        new_list = []
        for row_index in range(self.height):
            for col_index in range(self.width):
                cell = self.get_cell_by_index([row_index,col_index])
                cell.update_sprite()
                new_list.append(cell)
        return new_list

    def handleCellClick(self, clicked_cell: Cell, button: MouseClick):

        # Start game at first click
        if not self.game_ongoing:
            self.game_ongoing = True

        self.clicked_cell = clicked_cell
        if button is MouseClick.LEFT:
            if not self.clicked_cell.flagged:
                if not self.clicked_cell.discovered:
                    if not self.mines_generated:
                        self.add_mines()
                        self.calculate_neighbors()
                    self.discover_cell_and_neighbors(self.clicked_cell)
                if self.clicked_cell.mine:
                    self.game_lost = True
                    self.game_ongoing = False
                    print("You lost!")

        if button is MouseClick.RIGHT:
            if not self.clicked_cell.discovered:
                if not self.clicked_cell.flagged:
                    self.flags_total += 1
                else:
                    self.flags_total -= 1
                self.clicked_cell.flagged = not self.clicked_cell.flagged

        if self.undiscovered_mineless_cells_left == 0 and self.mines_total - self.flags_total == 0:
            self.game_won = True
            self.game_ongoing = False
            print("You won!")

    def handleCellHover(self, hovered_cell: Cell):
        if not hovered_cell == self.highlighted_cell:
            if not self.highlighted_cell == None:
                self.highlighted_cell.highlighted = False
            hovered_cell.highlighted = True
            self.highlighted_cell = hovered_cell
        else:
            pass
