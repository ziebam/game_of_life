"""Functions related to the game state.

This module contains all functions that are directly working with the current
game state.
"""

import copy
import random
from typing import List

from colorama import Back, Style


def random_state(width: int, height: int) -> List[List]:
    """Generates a board with all the cells randomly dead (0) or alive (1).

    Args:
        width: The width of the board to be created.
        height: The height of the board to be created.

    Returns:
        A list of lists representing the board in a 2D space.
    """
    return [[int(random.random() * 2) for _ in range(width)] for _ in range(height)]


def render(state: List[List]) -> None:
    """Pretty prints the state to the terminal.

    Args:
        state: A list of lists representing the board in a 2D space.

    Returns:
        None
    """
    for row in state:
        for cell in row:
            if cell == 1:
                print(Back.WHITE + " " + Style.RESET_ALL, end="")
            else:
                print(" ", end="")
        print()


def get_alive_neighbors(y: int, x: int, state: List[List]) -> int:
    """Counts alive neighbors of a cell with the passed coordinates.

    Args:
        y: y-position of the cell.
        x: x-position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        A count of alive neighbors.
    """

    # The board wraps around itself, so there are some extra checks necessary
    # to avoid `IndexError`s.
    is_last_column = x == len(state[0]) - 1
    is_last_row = y == len(state) - 1

    top_left_neighbor = state[y - 1][x - 1]
    top_neighbor = state[y - 1][x]
    left_neighbor = state[y][x - 1]

    if is_last_column:
        top_right_neighbor = state[y - 1][0]
        right_neighbor = state[y][0]
    else:
        top_right_neighbor = state[y - 1][x + 1]
        right_neighbor = state[y][x + 1]

    if is_last_row:
        bottom_left_neighbor = state[0][x - 1]
        bottom_neighbor = state[0][x]
    else:
        bottom_left_neighbor = state[y + 1][x - 1]
        bottom_neighbor = state[y + 1][x]

    if is_last_row and is_last_column:
        bottom_right_neighbor = state[0][0]
    elif is_last_column:
        bottom_right_neighbor = state[y + 1][0]
    elif is_last_row:
        bottom_right_neighbor = state[0][x + 1]
    else:
        bottom_right_neighbor = state[y + 1][x + 1]

    neighbors = [
        top_left_neighbor,
        top_neighbor,
        top_right_neighbor,
        left_neighbor,
        right_neighbor,
        bottom_left_neighbor,
        bottom_neighbor,
        bottom_right_neighbor,
    ]

    return neighbors.count(1)


def get_next_state(current_state: List[List]) -> List[List]:
    """Calculates the next state by the Conway's Game of Life rules.

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

    for y in range(len(current_state)):
        for x in range(len(current_state[0])):
            alive_neighbors = get_alive_neighbors(y, x, current_state)

            if current_state[y][x] == 0:
                if alive_neighbors == 3:
                    next_state[y][x] = 1
            else:
                if alive_neighbors in [0, 1]:
                    next_state[y][x] = 0
                elif alive_neighbors > 3:
                    next_state[y][x] = 0

    return next_state
