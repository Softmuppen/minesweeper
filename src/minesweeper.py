#!/usr/bin/env python3

import numpy as np

# Board definitions
BOARD_WIDTH = 4
BOARD_HEIGHT = 3

def generate_empty_board(width, height):
    generated_board = np.zeros((height, width), dtype=object)
    return generated_board

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

    # print()
    # board[0,0] = 'S'
    # board[BOARD_HEIGHT-1,BOARD_WIDTH-1] = 'E'
    # print_board(board)

if __name__ == "__main__":
    main()
