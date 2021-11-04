#!/usr/bin/env python3

import random
import numpy as np

from enums import cells, difficulties 

# Board definitions
BOARD_DIFFICULTY = difficulties.Difficulty.MEDIUM
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

def generate_empty_board(width, height):
    print(f"Generating a empty {width}x{height} board")
    generated_board = np.zeros((height, width), dtype=object)
    return generated_board

# Remove need for constants BOARD_WIDTH and BOARD_HEIGHT
def add_mines_to_board(board, difficulty):
    expected_mine_count = np.floor((BOARD_WIDTH * BOARD_HEIGHT) * (difficulty / 100))
    print(f"Adding {expected_mine_count} mines for difficulty {difficulty.name}")

    actual_mine_count = 0
    while actual_mine_count < expected_mine_count:
        random_row = random.randint(0, BOARD_HEIGHT-1)
        random_col = random.randint(0, BOARD_WIDTH-1)
        if board[random_row, random_col] == cells.Cell.EMPTY:
            board[random_row, random_col] = cells.Cell.MINE
            actual_mine_count += 1

def print_board(board_array):
    row_index = 0
    while row_index < BOARD_HEIGHT:
        col_index = 0
        while col_index < BOARD_WIDTH:
            print(f"[{board_array[row_index, col_index]}]", end ="")
            col_index += 1
        print()
        row_index += 1

def main():
    board = generate_empty_board(BOARD_WIDTH,BOARD_HEIGHT)
    print_board(board)

    add_mines_to_board(board, BOARD_DIFFICULTY)
    print_board(board)


    # print()
    # board[0,0] = 'S'
    # board[BOARD_HEIGHT-1,BOARD_WIDTH-1] = 'E'
    # print_board(board)

if __name__ == "__main__":
    main()
