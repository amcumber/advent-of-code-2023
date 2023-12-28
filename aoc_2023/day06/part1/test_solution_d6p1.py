from functools import reduce

import pytest

from aoc_2023.day06.part1.solution_d6p1 import main


@pytest.fixture
def example_input():
    return [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]


@pytest.fixture
def expected_main_result():
    return [4, 8, 9]


@pytest.fixture
def expected_solution():
    return 4 * 8 * 9


def test_main(example_input, expected_main_result, expected_solution):
    result = main(example_input)
    assert result == expected_main_result
    assert reduce(lambda x, y: x * y, result) == expected_solution
