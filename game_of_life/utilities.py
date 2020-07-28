"""The project's utilities.

This module provides utility functions that don't fit any other module.
"""

from typing import List


def load_board_state(path_to_file: str) -> List[List[int]]:
    """Loads the initial board state from file.

    Args:
        path_to_file: A path to the file, preferably constructed with
          os.path.join().

    Returns:
        A list of lists representing the board in a 2D space.
    """

    with open(path_to_file) as raw_data:
        read_data = raw_data.read().splitlines()

        state = []
        for row in read_data:
            state.append([int(cell) for cell in row])

        return state
