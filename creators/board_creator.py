import pygame

from game import Board
from typing import Optional, Tuple
from visualization import Visualization


class BoardCreator:
    BACKGROUND_COLOR = Visualization.BACKGROUND_COLOR
    ALIVE_COLOR = Visualization.ALIVE_COLOR
    DEAD_COLOR = Visualization.DEAD_COLOR
    BORDER = Visualization.BORDER
    CLOCK_TICK = Visualization.CLOCK_TICK

    def __init__(self, window_size: Tuple[int, int], board_size: Tuple[int, int]):
        self.board_size = board_size

        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption('GameOfLife Creator')

    def run(self, board: Optional[Board]) -> Board:
        clock = pygame.time.Clock()

        if not board:
            board = [[False for x in range(self.board_size[0])] for y in range(self.board_size[1])]

        self.__redraw(board)

        run = True
        while run:
            clock.tick(self.CLOCK_TICK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button = event.button
                    x, y = pygame.mouse.get_pos()
                    col = x // (self.window.get_width() // self.board_size[0])
                    row = y // (self.window.get_height() // self.board_size[1])

                    if button == 1:
                        board[row][col] = True
                    elif button == 3:
                        board[row][col] = False

                    self.__redraw(board)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return board

    def __redraw(self, board: Board):
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
