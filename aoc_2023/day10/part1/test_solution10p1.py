import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day10.part1.solution10p1 import find_start, main


def example_input1():
    return [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    ]


def example_input2():
    return [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF",
    ]


def example_input3():
    return [
        "7-F7-",
        ".FJ|7",
        "SJLL7",
        "|F--J",
        "LJ.LJ",
    ]


def expected_result1():
    return 4


def expected_start_point1():
    return (1, 1)


def expected_result2():
    return 4


def expected_start_point2():
    return (1, 1)


def expected_result3():
    return 8


def expected_start_point3():
    return (0, 2)


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_start_point1()),
        (example_input2(), expected_start_point2()),
        (example_input3(), expected_start_point3()),
    ],
)
def test_find_start(input_data, expected):
    result = find_start(input_data)
    assert result.x == expected[0], "failed x"
    assert result.y == expected[1], "failed y"


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_result1()),
        (example_input2(), expected_result2()),
        (example_input3(), expected_result3()),
    ],
)
def test_main(input_data, expected):
    result = main(input_data)
    assert result == expected
