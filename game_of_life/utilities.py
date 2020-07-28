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
