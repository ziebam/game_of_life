"""Utilities for the state module.
"""

from typing import List, Hashable


def which_side(y_pos: int, x_pos: int, width: int, height: int) -> Hashable:
    """Determines where the cell with given y_pos and x_pos resides.

    Tuples are corners, integers are sides or middle:
      - 1 is top side,
      - 2 is right side,
      - 3 is bottom side,
      - 4 is left side,
      - 5 is middle.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        width: Board width.
        height: Board height.
    Returns:
        Hashable later used to determine which function to run via dictionary.
    """

    # Top left corner.
    if y_pos == x_pos == 0:
        side = (1, 4)

    # Top right corner.
    elif y_pos == 0 and x_pos == width - 1:
        side = (1, 2)

    # Bottom right corner.
    elif y_pos == height - 1 and x_pos == width - 1:
        side = (2, 3)

    # Bottom left corner.
    elif y_pos == height - 1 and x_pos == 0:
        side = (3, 4)

    # Top side.
    elif y_pos == 0:
        side = 1

    # Right side.
    elif x_pos == width - 1:
        side = 2

    # Bottom side.
    elif y_pos == height - 1:
        side = 3

    # Left side.
    elif x_pos == 0:
        side = 4

    return side


def top_left_corner(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell in the top left corner.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell in the top left corner.
    """

    right_neighbor = state[y_pos][x_pos + 1]
    bottom_right_neighbor = state[y_pos + 1][x_pos + 1]
    bottom_neighbor = state[y_pos + 1][x_pos]

    neighbors = [right_neighbor, bottom_right_neighbor, bottom_neighbor]

    return neighbors.count(1)


def top_right_corner(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell in the top right corner.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell in the top right corner.
    """

    bottom_neighbor = state[y_pos + 1][x_pos]
    bottom_left_neighbor = state[y_pos + 1][x_pos - 1]
    left_neighbor = state[y_pos][x_pos - 1]

    neighbors = [bottom_neighbor, bottom_left_neighbor, left_neighbor]

    return neighbors.count(1)


def bottom_right_corner(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell in the bottom right corner.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell in the bottom right corner.
    """

    top_left_neighbor = state[y_pos - 1][x_pos - 1]
    top_neighbor = state[y_pos - 1][x_pos]
    left_neighbor = state[y_pos][x_pos - 1]

    neighbors = [top_left_neighbor, top_neighbor, left_neighbor]

    return neighbors.count(1)


def bottom_left_corner(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell in the bottom left corner.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell in the bottom left corner.
    """

    top_neighbor = state[y_pos - 1][x_pos]
    top_right_neighbor = state[y_pos - 1][x_pos + 1]
    right_neighbor = state[y_pos][x_pos + 1]

    neighbors = [top_neighbor, top_right_neighbor, right_neighbor]

    return neighbors.count(1)


def top_side(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell at the top side.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell at the top side.
    """

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

    return neighbors.count(1)


def right_side(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell at the right side.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell at the right side.
    """

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

    return neighbors.count(1)


def bottom_side(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell at the bottom side.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell at the bottom side.
    """

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

    return neighbors.count(1)


def left_side(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell at the left side.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell at the left side.
    """

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

    return neighbors.count(1)


def middle(y_pos: int, x_pos: int, state: List[List[int]]) -> int:
    """Counts alive neighbors of a cell in the middle.

    Args:
        y_pos: y position of the cell.
        x_pos: x position of the cell.
        state: A list of lists representing the board in a 2D space.

    Returns:
        The count of alive neighbors for a cell in the middle.
    """

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


cases = {
    (1, 4): top_left_corner,
    (1, 2): top_right_corner,
    (2, 3): bottom_right_corner,
    (3, 4): bottom_left_corner,
    1: top_side,
    2: right_side,
    3: bottom_side,
    4: left_side,
}


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

    # The most cells are in the middle, so short-circuiting the check with
    # a try .. except is more efficient than checking for the cell position
    # every time.
    try:
        alive_neighbors = middle(y_pos, x_pos, state)
    except IndexError:
        position = which_side(y_pos, x_pos, width, height)
        alive_neighbors = cases[position](y_pos, x_pos, state)

    return alive_neighbors
