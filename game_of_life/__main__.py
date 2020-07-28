"""The starting point for Conway's Game of Life simulation.
"""

import sys
import os

import pygame

from .state import get_next_state, random_state, render
from .utilities import load_board_state


def setup(arguments: list = None) -> tuple:
    """Sets up the GUI.

    Args:
        arguments: A list of appropriate arguments. Valid forms:
          ["random", width, height]
          ["file", path_to_file]
          Defaults to None when no arguments are provided. Then we
          set the arguments manually.
    Returns:
        Tuple containing pygame surface, initial board state,
        grid width, grid height and block size.
    """

    pygame.display.set_caption("Conway's Game of Life")

    cell_size = 25

    if not arguments:
        arguments = ["random", 25, 25]

    if arguments[0] == "random":
        grid_width = int(arguments[1])
        grid_height = int(arguments[2])

        state = random_state(grid_width, grid_height)

        screen = pygame.display.set_mode(
            (grid_width * cell_size, grid_height * cell_size)
        )
    elif arguments[0] == "file":
        state = load_board_state(os.path.join("patterns", arguments[1]))

        grid_width = len(state[0])
        grid_height = len(state)

        screen = pygame.display.set_mode(
            (grid_width * cell_size, grid_height * cell_size)
        )

    return (screen, state, grid_width, grid_height, cell_size)


def main() -> None:
    """Handles the game loop.

    Returns:
        None
    """

    pygame.init()

    if len(sys.argv) > 1:
        screen, state, grid_width, grid_height, cell_size = setup(
            arguments=sys.argv[1:]
        )
    else:
        screen, state, grid_width, grid_height, cell_size = setup()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        render(screen, state, grid_width, grid_height, cell_size)

        state = get_next_state(state)

        pygame.time.wait(100)


if __name__ == "__main__":
    main()
