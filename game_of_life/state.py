"""Functions related to the game state.

This module contains all functions that are directly working with the current
game state.
"""

import copy
import random
from enum import Enum
from typing import List

import pygame


class Color(Enum):
    """Enum for organizing pygame colors.
    """

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


def random_state(width: int, height: int) -> List[List[int]]:
    """Generates a board with all the cells randomly dead (0) or alive (1).

    Args:
        width: The width of the board to be created.
        height: The height of the board to be created.

    Returns:
        A list of lists representing the board in a 2D space.
    """
    return [[int(random.random() * 2) for _ in range(width)] for _ in range(height)]


# fmt: off
def render(
        screen: pygame.Surface,
        state: List[List[int]],
        board_width: int,
        board_height: int,
        cell_size: int,
    ) -> None:
# fmt: on
    """Displays the board in a pygame window on a 2D grid.

    Args:
        screen: A pygame surface on which we render the board.
        state: A list of lists representing the board in a 2D space.
        board_width: Width of the board in cells.
        board_height: Height of the board in cells.
        cell_size: Size of an individual cell.

    Returns:
        None
    """

    for x_pos in range(board_width):
        for y_pos in range(board_height):
            rect = pygame.Rect(
                x_pos * cell_size, y_pos * cell_size, cell_size, cell_size
            )

            if state[y_pos][x_pos]:
                pygame.draw.rect(screen, Color.WHITE.value, rect, 1)
            else:
                pygame.draw.rect(screen, Color.BLACK.value, rect, 1)
        pygame.display.update()


def get_alive_neighbors(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell with the passed coordinates.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell in state[y_pos][x_pos].
    """

    width = len(state[0])
    height = len(state)

    alive_neighbors = 0
    for neighbor_y_pos in range(y_pos - 1, y_pos + 2):
        # Make sure not to go off the grid vertically.
        if neighbor_y_pos < 0 or neighbor_y_pos >= height:
            continue

        for neighbor_x_pos in range(x_pos - 1, x_pos + 2):
            # Make sure not to compare to self.
            if neighbor_y_pos == y_pos and neighbor_x_pos == x_pos:
                continue

            # Make sure not go off the grid horizontally.
            if neighbor_x_pos < 0 or neighbor_x_pos >= width:
                continue

            alive_neighbors += state[neighbor_y_pos][neighbor_x_pos]

    return alive_neighbors


def get_next_state(current_state: List[List[int]]) -> List[List[int]]:
    """Calculates the next board state by the Conway's Game of Life rules.

    The rules are as follows:

    - Any live cell with fewer than two live neighbours dies,
      as if by underpopulation.
    - Any live cell with two or three live neighbours lives on
      to the next generation.
    - Any live cell with more than three live neighbours dies,
      as if by overpopulation.
    - Any dead cell with exactly three live neighbours becomes a live cell,
      as if by reproduction.

    Args:
        current_state: A list of lists representing the
          initial board state in a 2D space.

    Returns:
        A list of lists representing the new state of the board in a 2D space.
    """

    next_state = copy.deepcopy(current_state)

    for y_pos, _ in enumerate(current_state):
        for x_pos, _ in enumerate(current_state[0]):
            alive_neighbors = get_alive_neighbors(y_pos, x_pos, current_state)

            if current_state[y_pos][x_pos] == 0:
                if alive_neighbors == 3:
                    next_state[y_pos][x_pos] = 1
            else:
                if alive_neighbors in [0, 1]:
                    next_state[y_pos][x_pos] = 0
                elif alive_neighbors > 3:
                    next_state[y_pos][x_pos] = 0

    return next_state
