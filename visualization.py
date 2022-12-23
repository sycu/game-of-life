import pygame

from game import Board, Game
from typing import Tuple


class Visualization:
    BACKGROUND_COLOR = (255, 255, 255)
    ALIVE_COLOR = (255, 70, 0)
    DEAD_COLOR = (200, 200, 200)
    BORDER = 0
    CLOCK_TICK = 120

    def __init__(self, window_size: Tuple[int, int], board_size: Tuple[int, int]):
        self.board_size = board_size

        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption('GameOfLife')

    def visualize(self, game: Game) -> None:
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.CLOCK_TICK)
            game.tick()
            self.__draw_board(game.board())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

    def __draw_board(self, board: Board):
        self.window.fill(self.BACKGROUND_COLOR)
        height = self.window.get_height()
        width = self.window.get_width()

        cols, rows = self.board_size

        field_width = width // cols
        field_height = height // rows

        for y in range(rows):
            for x in range(cols):
                color = self.ALIVE_COLOR if board[y][x] else self.DEAD_COLOR
                pygame.draw.rect(self.window, color, (x * field_width + 1, y * field_height + 1, field_width - self.BORDER, field_height - self.BORDER))

        pygame.display.update()
