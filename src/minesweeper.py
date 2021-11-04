#!/usr/bin/env python3

import random
import numpy as np

from enums.difficulties import Difficulty 
from boards import MineBoard, PlayerBoard

# Board definitions
BOARD_DIFFICULTY = Difficulty.MEDIUM
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

def main():
    mine_board = MineBoard(BOARD_WIDTH,BOARD_HEIGHT,BOARD_DIFFICULTY)
    mine_board.print_board()

    player_board = PlayerBoard(BOARD_WIDTH,BOARD_HEIGHT)
    player_board.print_board()

if __name__ == "__main__":
    main()
