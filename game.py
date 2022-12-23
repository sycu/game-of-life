from typing import List, Tuple

Board = List[List[bool]]


class Game:
    def __init__(self, board_size: Tuple[int, int], board: Board, range: int, birth: List[int], survive: List[int]):
        self._board_size = board_size
        self._board = board
        self._range = range
        self._birth = birth
        self._survive = survive

    def tick(self):
        cols, rows = self._board_size

        new_board = [[False for x in range(cols)] for y in range(rows)]

        for y in range(rows):
            for x in range(cols):

                neighbors = 0
                for ny in range(y - self._range, y + self._range + 1):
                    for nx in range(x - self._range, x + self._range + 1):
                        neighbors += (nx != x or ny != y) and self._board[ny % rows][nx % cols]

                if not self._board[y][x] and neighbors in self._birth:
                    new_board[y][x] = True
                elif self._board[y][x] and neighbors in self._survive:
                    new_board[y][x] = True
                else:
                    new_board[y][x] = False

        self._board = new_board

    def board(self):
        return self._board
