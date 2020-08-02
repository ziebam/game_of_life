"""Tests for the game_of_life/state.py module."""

import json
import os

from game_of_life.state import get_next_state

with open(os.path.join("tests", "data", "test_state_data.json")) as json_data:
    data = json.load(json_data)


def test_dead_cell_with_no_live_neighbors():
    """Tests the board with only dead cells on it."""

    # fmt: off
    init_state = data["test_dead_cell_with_no_live_neighbors"]["init_state"]
    expected_next_state = data["test_dead_cell_with_no_live_neighbors"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state


def test_live_cell_with_zero_live_neighbors():
    """Tests the board with a live cell without any neighbors on it."""

    # fmt: off
    init_state = data["test_live_cell_with_zero_live_neighbors"]["init_state"]
    expected_next_state = data["test_live_cell_with_zero_live_neighbors"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state


def test_live_cell_with_one_live_neighbor():
    """Tests the board with a live cell with one live neighbor on it."""

    # fmt: off
    init_state = data["test_live_cell_with_one_live_neighbor"]["init_state"]
    expected_next_state = data["test_live_cell_with_one_live_neighbor"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state


def test_live_cell_with_two_live_neighbors():
    """Tests the board with a live cell with two live neighbors on it.
    """

    # fmt: off
    init_state = data["test_live_cell_with_two_live_neighbors"]["init_state"]
    expected_next_state = data["test_live_cell_with_two_live_neighbors"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state


def test_live_cell_with_three_live_neighbors():
    """Tests the board with a live cell with three live neighbor on it.
    """

    # fmt: off
    init_state = data["test_live_cell_with_three_live_neighbors"]["init_state"]
    expected_next_state = data["test_live_cell_with_three_live_neighbors"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state


def test_live_cell_with_more_than_three_live_neighbors():
    """Tests the board with a live cell with more than three live neighbor on it.
    """

    # fmt: off
    init_state = data["test_live_cell_with_more_than_three_live_neighbors"]["init_state"]
    expected_next_state = data["test_live_cell_with_more_than_three_live_neighbors"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state


def test_dead_cell_with_exactly_three_live_neighbors():
    """Tests the board with a dead cell with exactly three live neighbor on it.
    """

    # fmt: off
    init_state = data["test_dead_cell_with_exactly_three_live_neighbors"]["init_state"]
    expected_next_state = data["test_dead_cell_with_exactly_three_live_neighbors"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state


def test_dead_cell_with_more_than_three_live_neighbors():
    """Tests the board with a dead cell with more than three live neighbor on it.
    """

    # fmt: off
    init_state = data["test_dead_cell_with_more_than_three_live_neighbors"]["init_state"]
    expected_next_state = data["test_dead_cell_with_more_than_three_live_neighbors"]["expected_next_state"]
    # fmt: on

    actual_next_state = get_next_state(init_state)

    assert expected_next_state == actual_next_state
