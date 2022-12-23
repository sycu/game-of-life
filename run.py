import os
import pickle
import sys

from creators import BoardCreator, RandomCreator
from game import Board, Game
from typing import Optional, Tuple
from visualization import Visualization


def load(name: str) -> Optional[Tuple[Tuple[int, int], Board]]:
    with open(os.path.join('data', '%s.game' % name), 'rb') as file:
        return pickle.load(file)


def save(name: str, board_size: Tuple[int, int], board: Board) -> None:
    with open(os.path.join('data', '%s.game' % name), 'wb') as file:
        pickle.dump((board_size, board), file, pickle.HIGHEST_PROTOCOL)


def run() -> None:
    if len(sys.argv) != 4:
        print('Usage:')
        print(f'python {sys.argv[0]} [name] [cols] [rows]')
        exit(1)

    name = sys.argv[1]
    board_size = (int(sys.argv[2]), int(sys.argv[3]))
    nbs = board_size

    try:
        board_size, board = load(name)
    except FileNotFoundError:
        board = None

    if board_size != nbs:
        board_size = nbs

    bok = int(1000 / board_size[0])
    print(bok * board_size[0], bok * board_size[1])

    window_size = (bok * board_size[0], bok * board_size[1])

    # creator = BoardCreator(window_size, board_size)
    creator = RandomCreator(board_size)
    board = creator.run(board)
    if name != 'nope':
        save(name, board_size, board)

    # game = Game(board_size, board, 1, [3], [2, 3])
    game = Game(board_size, board, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8])

    visualization = Visualization(window_size, board_size)
    visualization.visualize(game)


if __name__ == '__main__':
    run()
