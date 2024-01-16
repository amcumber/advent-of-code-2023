import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day08.part2.solution8p2 import calc_result, main


def example_input1():
    return [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    ]


def expected_directions1():
    return (1, 0)


def expected_map1():
    return {
        "11A": ("11B", "XXX"),
        "11B": ("XXX", "11Z"),
        "11Z": ("11B", "XXX"),
        "22A": ("22B", "XXX"),
        "22B": ("22C", "22C"),
        "22C": ("22Z", "22Z"),
        "22Z": ("22B", "22B"),
        "XXX": ("XXX", "XXX"),
    }


def expected_result1():
    return 6


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_result1()),
    ],
)
def test_main(input_data, expected):
    min_counts = main(input_data)
    result = calc_result(min_counts)
    assert result == expected
