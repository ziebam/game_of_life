"""The starting point for Conway's Game of Life simulation.
"""

import sys
import time

from colorama import init

from .state import get_next_state, random_state, render
from .utilities import clear_screen


def main() -> None:
    """Handles the terminal setup and the game loop.

    Returns:
        None
    """

    # When testing the script in Cygwin, printing in color didn't work after
    # running Colorama's `init()`.
    #
    # After a bit of research, it turns out that this is the case when
    # `sys.stdin.isatty()` returns False, i.e. when the shell is emulated.
    #
    # The following check ensures that the initialization only happens if
    # the script is run from a not emulated terminal, e.g. cmd or bash.
    if sys.stdin.isatty():
        init()

    state = random_state(50, 50)
    while True:
        clear_screen()

        render(state)
        state = get_next_state(state)

        time.sleep(1)


if __name__ == "__main__":
    main()
