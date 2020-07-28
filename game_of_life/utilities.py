"""The project's utilities.

This module provides utility functions that don't fit any other module.
"""


import os


def clear_screen() -> None:
    """Clears the terminal screen.

    Returns:
        None
    """

    os.system("cls" if os.name == "nt" else "clear")


def load_board_state(file):
    with open(file) as data:
        data = data.read().splitlines()

        state = []
        for row in data:
            state.append([int(cell) for cell in row])

        return state
