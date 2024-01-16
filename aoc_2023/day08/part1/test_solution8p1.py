import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day08.day8 import parse_directions, parse_map
from aoc_2023.day08.part1.solution8p1 import main


def example_input1():
    return [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]


def expected_directions1():
    return (1, 0)


def expected_map1():
    return {
        "AAA": ("BBB", "CCC"),
        "BBB": ("DDD", "EEE"),
        "CCC": ("ZZZ", "GGG"),
        "DDD": ("DDD", "DDD"),
        "EEE": ("EEE", "EEE"),
        "GGG": ("GGG", "GGG"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }


def example_input2():
    return [
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)",
    ]


def expected_directions2():
    return (0, 0, 1)


def expected_map2():
    return {
        "AAA": ("BBB", "BBB"),
        "BBB": ("AAA", "ZZZ"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }


def expected_result1():
    return 2


def expected_result2():
    return 6


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_directions1()),
        (example_input2(), expected_directions2()),
    ],
)
def test_parse_directions(input_data, expected):
    result = parse_directions(input_data)
    assert result == expected


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_map1()),
        (example_input2(), expected_map2()),
    ],
)
def test_parse_map(input_data, expected):
    result = parse_map(input_data)
    assert result == expected


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_result1()),
        (example_input2(), expected_result2()),
    ],
)
def test_main(input_data, expected):
    result = main(input_data)
    assert result == expected
