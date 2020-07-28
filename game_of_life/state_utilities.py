"""Utilities for the state module.
"""

from typing import List


def is_top_left_corner(y_pos: int, x_pos: int) -> bool:
    """Checks whether the cell at a given x and y is the top left corner.

    Args:
        y_pos: y-position of the cell.
        x_pos: x-position of the cell.

    Returns:
        True if the cell is in the top left corner. False otherwise.
    """

    return x_pos == y_pos == 0


def is_top_right_corner(y_pos: int, x_pos: int, width: int) -> bool:
    """Checks whether the cell at a given x and y is the top right corner.

    Args:
        y_pos: y-position of the cell.
        x_pos: x-position of the cell.
        width: Width of the board.

    Returns:
        True if the cell is in the top right corner. False otherwise.
    """

    return x_pos == width - 1 and y_pos == 0


def is_bottom_right_corner(y_pos: int, x_pos: int, width: int, height: int) -> bool:
    """Checks whether the cell at a given x and y is the bottom right corner.

    Args:
        y_pos: y-position of the cell.
        x_pos: x-position of the cell.
        width: Width of the board.
        height: Height of the board.

    Returns:
        True if the cell is in the bottom right corner. False otherwise.
    """

    return x_pos == width - 1 and y_pos == height - 1


def is_bottom_left_corner(y_pos: int, x_pos: int, height: int) -> bool:
    """Checks whether the cell at a given x and y is the bottom left corner.

    Args:
        y_pos: y-position of the cell.
        x_pos: x-position of the cell.
        height: Height of the board.

    Returns:
        True if the cell is in the bottom left corner. False otherwise.
    """
    return x_pos == 0 and y_pos == height - 1


def is_top_side(y_pos: int) -> bool:
    """Checks whether the cell at a given x and y is at the top side.

    Args:
        y_pos: y-position of the cell.

    Returns:
        True if the cell is at the topside. False otherwise.
    """

    return y_pos == 0


def is_right_side(x_pos: int, width: int) -> bool:
    """Checks whether the cell at a given x and y is at the right side.

    Args:
        x_pos: x-position of the cell.
        width: Width of the board.

    Returns:
        True if the cell is at the right side. False otherwise.
    """

    return x_pos == width - 1


def is_bottom_side(y_pos: int, height: int) -> bool:
    """Checks whether the cell at a given x and y is at the bottom side.

    Args:
        y_pos: y-position of the cell.
        height: Height of the board.

    Returns:
        True if the cell is in at the bottom side. False otherwise.
    """

    return y_pos == height - 1


def is_left_side(x_pos: int) -> bool:
    """Checks whether the cell at a given x and y is the bottom right corner.

    Args:
        x_pos: x-position of the cell.

    Returns:
        True if the cell is in the bottom right corner. False otherwise.
    """

    return x_pos == 0


def get_alive_neighbors(y_pos: int, x_pos: int, state: List[List]) -> int:
    """Counts alive neighbors of a cell with the passed coordinates.

    Args:
        y_pos: y-position of the cell.
        x_pos: x-position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors.
    """

    width = len(state[0])
    height = len(state)

    if is_top_left_corner(y_pos, x_pos):
        right_neighbor = state[y_pos][x_pos + 1]
        bottom_right_neighbor = state[y_pos + 1][x_pos + 1]
        bottom_neighbor = state[y_pos + 1][x_pos]

        neighbors = [right_neighbor, bottom_right_neighbor, bottom_neighbor]
    elif is_top_right_corner(y_pos, x_pos, width):
        bottom_neighbor = state[y_pos + 1][x_pos]
        bottom_left_neighbor = state[y_pos + 1][x_pos - 1]
        left_neighbor = state[y_pos][x_pos - 1]

        neighbors = [bottom_neighbor, bottom_left_neighbor, left_neighbor]
    elif is_bottom_right_corner(y_pos, x_pos, width, height):
        top_left_neighbor = state[y_pos - 1][x_pos - 1]
        top_neighbor = state[y_pos - 1][x_pos]
        left_neighbor = state[y_pos][x_pos - 1]

        neighbors = [top_left_neighbor, top_neighbor, left_neighbor]
    elif is_bottom_left_corner(y_pos, x_pos, height):
        top_neighbor = state[y_pos - 1][x_pos]
        top_right_neighbor = state[y_pos - 1][x_pos + 1]
        right_neighbor = state[y_pos][x_pos + 1]

        neighbors = [top_neighbor, top_right_neighbor, right_neighbor]

    elif is_top_side(y_pos):
        right_neighbor = state[y_pos][x_pos + 1]
        bottom_right_neighbor = state[y_pos + 1][x_pos + 1]
        bottom_neighbor = state[y_pos + 1][x_pos]
        bottom_left_neighbor = state[y_pos - 1][x_pos - 1]
        left_neighbor = state[y_pos][x_pos - 1]

        neighbors = [
            right_neighbor,
            bottom_right_neighbor,
            bottom_neighbor,
            bottom_left_neighbor,
            left_neighbor,
        ]
    elif is_right_side(x_pos, width):
        top_left_neighbor = state[y_pos - 1][x_pos - 1]
        top_neighbor = state[y_pos - 1][x_pos]
        bottom_neighbor = state[y_pos + 1][x_pos]
        bottom_left_neighbor = state[y_pos + 1][x_pos - 1]
        left_neighbor = state[y_pos][x_pos - 1]

        neighbors = [
            top_left_neighbor,
            top_neighbor,
            bottom_neighbor,
            bottom_left_neighbor,
            left_neighbor,
        ]
    elif is_bottom_side(y_pos, height):
        top_left_neighbor = top_left_neighbor = state[y_pos - 1][x_pos - 1]
        top_neighbor = state[y_pos - 1][x_pos]
        top_right_neighbor = state[y_pos - 1][x_pos + 1]
        right_neighbor = state[y_pos][x_pos + 1]
        left_neighbor = state[y_pos][x_pos - 1]

        neighbors = [
            top_left_neighbor,
            top_neighbor,
            top_right_neighbor,
            right_neighbor,
            left_neighbor,
        ]
    elif is_left_side(x_pos):
        top_neighbor = state[y_pos - 1][x_pos]
        top_right_neighbor = state[y_pos - 1][x_pos + 1]
        right_neighbor = state[y_pos][x_pos + 1]
        bottom_right_neighbor = state[y_pos + 1][x_pos + 1]
        bottom_neighbor = state[y_pos + 1][x_pos]

        neighbors = [
            top_neighbor,
            top_right_neighbor,
            right_neighbor,
            bottom_right_neighbor,
            bottom_neighbor,
        ]

    else:
        top_left_neighbor = state[y_pos - 1][x_pos - 1]
        top_neighbor = state[y_pos - 1][x_pos]
        top_right_neighbor = state[y_pos - 1][x_pos + 1]
        right_neighbor = state[y_pos][x_pos + 1]
        bottom_right_neighbor = state[y_pos + 1][x_pos + 1]
        bottom_neighbor = state[y_pos + 1][x_pos]
        bottom_left_neighbor = state[y_pos + 1][x_pos - 1]
        left_neighbor = state[y_pos][x_pos - 1]

        neighbors = [
            top_left_neighbor,
            top_neighbor,
            top_right_neighbor,
            right_neighbor,
            bottom_right_neighbor,
            bottom_neighbor,
            bottom_left_neighbor,
            left_neighbor,
        ]

    return neighbors.count(1)
