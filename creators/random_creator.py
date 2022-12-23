import random

from game import Board
from typing import Optional, Tuple


class RandomCreator:
    def __init__(self, board_size: Tuple[int, int]):
        self.board_size = board_size

    def run(self, board: Optional[Board]) -> Board:
        return [[random.choice([True, False]) for x in range(self.board_size[0])] for y in range(self.board_size[1])]
